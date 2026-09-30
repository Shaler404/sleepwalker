"""Explorer: агент, который играет на устройстве и пишет трассу сессии (слой raw).

pip install anthropic pillow imagehash adbutils
Запуск: python explorer.py --serial R58M12345 --package com.example.game --minutes 15 \
        --goal "Пройди обучение и опиши главное меню"

Что здесь происходит:
- цикл «наблюдение -> решение -> действие» ведёт tool runner из SDK (client.beta.messages.tool_runner);
- каждое действие возвращает свежий кадр, так что модель всегда видит результат;
- memory tool даёт агенту каталог /memories (memory/<game>) для заметок между сессиями;
- старые скриншоты вычищаются из контекста (context editing), чтобы сессия не упиралась в окно;
- всё, что модель увидела и сделала, пишется в raw/<game>/<session>/steps.jsonl.
"""
from __future__ import annotations

import argparse
import base64
import io
import json
import os
import time
import uuid
from pathlib import Path

import anthropic
from anthropic import beta_tool
from anthropic.tools import BetaLocalFilesystemMemoryTool

from device import AndroidDevice, Device
from perception import is_same_screen, prepare_for_model, screen_hash

MODEL = "claude-opus-5-5"  # решения; для рутинных шагов можно claude-sonnet-5-5
ROOT = Path(os.environ.get("SW_ROOT") or Path(__file__).resolve().parent.parent)  # корень репозитория (или worktree «сна»)
PROMPTS = ROOT / "schema" / "PROMPTS.md"

# Системный промпт Explorer'а лежит в PROMPTS.md (раздел 1); здесь — короткая версия.
EXPLORER_SYSTEM = """Ты — исследователь мобильных игр. Ты управляешь реальным устройством через инструменты
и изучаешь игру, чтобы по ней можно было написать подробную вики.
Перед первым действием прочитай /memories. Один шаг = одно действие; в why пиши, что ожидаешь увидеть,
и сверяй ожидание с новым кадром. Три действия без изменения экрана — смени стратегию.
Всплывающие окна и офферы — контент: сначала mark_screen, потом закрывай. Факты записывай через note сразу.
Координаты — в пикселях последнего скриншота. Не совершай покупок за реальные деньги, не меняй настройки
аккаунта, не пиши другим игрокам. Закончив, вызови finish и обнови /memories/progress.md."""


class Session:
    """Состояние одной сессии + запись трассы."""

    def __init__(self, device: Device, game: str, goal: str):
        self.device, self.game, self.goal = device, game, goal
        self.id = time.strftime("%Y%m%d-%H%M") + "-" + uuid.uuid4().hex[:6]
        self.dir = ROOT / "raw" / game / self.id
        (self.dir / "shots").mkdir(parents=True, exist_ok=True)
        self._log = (self.dir / "steps.jsonl").open("a", encoding="utf-8")
        self.steps = 0
        self.scale = 1.0
        self.last_hash: str | None = None
        self.same_streak = 0
        self.marked: list[dict] = []
        self.finished = False
        self.record({"session": self.id, "game": game, "goal": goal, "device": device.name,
                     "screen": [device.width, device.height], "t": time.time()})

    def record(self, item: dict) -> None:
        item.setdefault("t", time.time())
        self._log.write(json.dumps(item, ensure_ascii=False) + "\n")
        self._log.flush()

    def observe(self, note: str = "") -> list[dict]:
        """Снять кадр, сохранить оригинал, вернуть блоки контента для модели."""
        img = self.device.screenshot()
        self.steps += 1
        path = self.dir / "shots" / f"{self.steps:05d}.png"
        img.save(path)
        h = screen_hash(img)
        same = is_same_screen(self.last_hash, h)
        self.same_streak = self.same_streak + 1 if same else 0
        self.last_hash = h
        small, self.scale = prepare_for_model(img, budget_tokens=1500)
        self.record({"step": self.steps, "shot": path.name, "hash": h, "same_screen": same, "note": note})
        buf = io.BytesIO()
        small.save(buf, format="WEBP", quality=85)
        text = f"Кадр {self.steps}: {small.width}x{small.height} px. Экран {'НЕ изменился' if same else 'изменился'}."
        if self.same_streak >= 3:
            text += f" Экран не меняется уже {self.same_streak} шага(ов) — смени стратегию."
        return [
            {"type": "text", "text": text},
            {"type": "image", "source": {"type": "base64", "media_type": "image/webp",
                                          "data": base64.b64encode(buf.getvalue()).decode()}},
        ]

    def close(self) -> None:
        (self.dir / "marked.json").write_text(json.dumps(self.marked, ensure_ascii=False, indent=2), encoding="utf-8")
        self._log.close()


def build_tools(s: Session) -> list:
    """Инструменты замыкаются на сессию; схемы аргументов SDK строит из сигнатур и докстрингов."""

    @beta_tool
    def screenshot() -> list:
        """Сделать скриншот текущего экрана. Координаты для tap/swipe указывай в пикселях этого изображения."""
        return s.observe()

    @beta_tool
    def tap(x: int, y: int, why: str) -> list:
        """Тап по точке (x, y) в пикселях последнего скриншота. why — что ожидаешь увидеть после тапа."""
        s.device.tap(round(x * s.scale), round(y * s.scale))
        s.record({"action": "tap", "x": x, "y": y, "why": why})
        time.sleep(1.0)
        return s.observe()

    @beta_tool
    def long_press(x: int, y: int, why: str) -> list:
        """Долгое нажатие (0.8 с) по точке в пикселях последнего скриншота."""
        s.device.long_press(round(x * s.scale), round(y * s.scale))
        s.record({"action": "long_press", "x": x, "y": y, "why": why})
        time.sleep(1.0)
        return s.observe()

    @beta_tool
    def swipe(x1: int, y1: int, x2: int, y2: int, why: str) -> list:
        """Свайп от (x1, y1) к (x2, y2) в пикселях последнего скриншота (прокрутка, перетаскивание)."""
        s.device.swipe(round(x1 * s.scale), round(y1 * s.scale), round(x2 * s.scale), round(y2 * s.scale))
        s.record({"action": "swipe", "from": [x1, y1], "to": [x2, y2], "why": why})
        time.sleep(1.0)
        return s.observe()

    @beta_tool
    def type_text(text: str) -> list:
        """Ввести текст в активное поле ввода."""
        s.device.type_text(text)
        s.record({"action": "type_text", "text": text})
        time.sleep(0.8)
        return s.observe()

    @beta_tool
    def press(key: str) -> list:
        """Нажать системную клавишу: back | home | enter."""
        s.device.key(key)
        s.record({"action": "press", "key": key})
        time.sleep(1.0)
        return s.observe()

    @beta_tool
    def wait(seconds: float) -> list:
        """Подождать (анимация, загрузка, таймер). Не больше 30 секунд за раз."""
        time.sleep(min(max(seconds, 0.2), 30))
        s.record({"action": "wait", "seconds": seconds})
        return s.observe()

    @beta_tool
    def note(text: str, kind: str = "observation") -> str:
        """Записать факт об игре. kind: observation | mechanic | economy | monetization | ui | event | bug | question."""
        s.record({"note": text, "kind": kind, "step": s.steps})
        return "записано"

    @beta_tool
    def mark_screen(title: str, description: str) -> str:
        """Пометить текущий экран как значимый для вики: короткое название и что на нём важно."""
        item = {"step": s.steps, "shot": f"{s.steps:05d}.png", "title": title, "description": description}
        s.marked.append(item)
        s.record({"mark": item})
        return f"экран '{title}' помечен (кадр {s.steps})"

    @beta_tool
    def finish(summary: str, goals_done: list[str], goals_failed: list[str]) -> str:
        """Завершить сессию: краткий итог, что из целей сделано и что нет."""
        s.record({"finish": {"summary": summary, "done": goals_done, "failed": goals_failed}})
        s.finished = True
        return "сессия завершена"

    return [screenshot, tap, long_press, swipe, type_text, press, wait, note, mark_screen, finish]


def read_text(path: Path, limit: int = 6000) -> str:
    return path.read_text(encoding="utf-8")[:limit] if path.exists() else "пока нет"


def run_session(device: Device, game: str, goal: str, minutes: int = 15, max_steps: int = 150) -> Path:
    client = anthropic.Anthropic()
    s = Session(device, game, goal)
    memory = BetaLocalFilesystemMemoryTool(base_path=str(ROOT / "memory" / game))
    tools = build_tools(s) + [memory]

    lessons = read_text(ROOT / "wiki" / game / "agent" / "lessons.md")
    questions = read_text(ROOT / "wiki" / game / "open-questions.md", 3000)
    first_message = (
        f"Игра: {game}. Устройство: {device.name}.\nЦель сессии: {goal}\n"
        f"Бюджет: {minutes} минут, не более {max_steps} действий.\n"
        f"Уроки прошлых сессий по этой игре:\n{lessons}\n\nОткрытые вопросы из вики:\n{questions}\n\n"
        "Начни с чтения памяти, затем сделай screenshot."
    )

    runner = client.beta.messages.tool_runner(
        model=MODEL,
        max_tokens=8000,
        system=[{"type": "text", "text": EXPLORER_SYSTEM, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": first_message}],
        tools=tools,
        max_iterations=max_steps,
        output_config={"effort": "medium"},
        # Opus 5.5: thinking всегда включён, параметр не передаём; глубина — через effort.
        betas=["server-side-fallback-2026-07-01", "context-management-2025-06-27"],
        fallbacks="default",  # при отказе классификатора запрос дорабатывает запасная модель
        context_management={"edits": [{
            "type": "clear_tool_uses_20250919",
            "trigger": {"type": "input_tokens", "value": 80000},
            "keep": {"type": "tool_uses", "value": 8},   # последние 8 кадров остаются
            "exclude_tools": ["memory", "note", "mark_screen"],
        }]},
        cache_control={"type": "ephemeral"},  # кэшируем хвост диалога между шагами
    )

    deadline = time.time() + minutes * 60
    for message in runner:
        s.record({
            "assistant": [b.text for b in message.content if b.type == "text"],
            "stop_reason": message.stop_reason,
            "usage": message.usage.to_dict(),
        })
        if message.stop_reason == "refusal":
            s.record({"error": "refusal", "details": message.stop_details.to_dict() if message.stop_details else None})
            break
        if s.finished or time.time() > deadline or s.same_streak >= 20:
            break  # сессия закончилась; следующая продолжит по /memories/progress.md

    s.close()
    return s.dir


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--serial", required=True)
    ap.add_argument("--package", required=True)
    ap.add_argument("--goal", default="Первый запуск: пройди обучение, изучи главное меню и магазин, сыграй 3 раунда.")
    ap.add_argument("--minutes", type=int, default=15)
    ap.add_argument("--max-steps", type=int, default=150)
    args = ap.parse_args()

    dev = AndroidDevice(args.serial)
    dev.launch(args.package)
    time.sleep(5)
    out = run_session(dev, args.package, args.goal, args.minutes, args.max_steps)
    print("трасса:", out)
