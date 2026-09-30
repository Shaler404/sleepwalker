"""Reflector: превращает трассу сессии в факты, уроки и заявки на обновление вики.

Запуск: python reflect.py --game com.example.game --session raw/com.example.game/20260928-0015-a1b2c3
Результат: <session>/reflection.json + новые кандидаты в wiki/<game>/agent/lessons.md
"""
from __future__ import annotations

import argparse
import base64
import io
import json
import os
import time
from pathlib import Path

import anthropic
from PIL import Image
from pydantic import BaseModel, Field

from perception import prepare_for_model

MODEL = "claude-opus-5-5"
ROOT = Path(os.environ.get("SW_ROOT") or Path(__file__).resolve().parent.parent)  # корень репозитория (или worktree «сна»)

REFLECTOR_SYSTEM = """Ты анализируешь трассу одной игровой сессии агента-исследователя: шаги (действие, ожидание,
заметка, изменился ли экран) и ключевые кадры. Извлеки знания для вики и уроки для агента.
Факт — только то, что видно на кадрах или записано в заметках; каждому факту — номера шагов; догадки —
confidence <= 0.5. Урок — правило «в ситуации X делай Y, потому что Z», проверяемое в следующей сессии;
ошибки агента (зацикливание, неверные координаты) описывай как уроки, не как факты об игре.
wiki_updates — только новое или противоречащее известному, с указанием страницы по схеме вики и кадров.
skill_candidates — последовательности действий, повторившиеся >= 2 раз с ожидаемым результатом."""


class Fact(BaseModel):
    topic: str = Field(description="mechanics | economy | monetization | ui | progression | events | meta")
    statement: str
    evidence_steps: list[int]
    confidence: float


class Lesson(BaseModel):
    scope: str = Field(description="game — про эту игру; general — про мобильные игры вообще")
    context: str = Field(description="Когда правило применяется")
    rule: str = Field(description="Что делать / чего не делать и почему")
    evidence_steps: list[int]
    confidence: float


class WikiUpdate(BaseModel):
    page: str = Field(description="Путь страницы по схеме, например screens/shop.md")
    action: str = Field(description="create | append | replace_section")
    section: str | None = None
    markdown: str
    images: list[str] = Field(description="Имена кадров из трассы, например 00042.png")


class Reflection(BaseModel):
    summary: str
    goals_done: list[str]
    goals_failed: list[str]
    facts: list[Fact]
    lessons: list[Lesson]
    wiki_updates: list[WikiUpdate]
    open_questions: list[str]
    skill_candidates: list[str]


def load_steps(session_dir: Path) -> list[dict]:
    with (session_dir / "steps.jsonl").open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def keyframes(session_dir: Path, steps: list[dict], limit: int = 16) -> list[int]:
    """Помеченные кадры + кадры, где сменился экран; первый и последний обязательно."""
    marked = {m["step"] for m in json.loads((session_dir / "marked.json").read_text(encoding="utf-8"))} \
        if (session_dir / "marked.json").exists() else set()
    changed = [s["step"] for s in steps if "step" in s and "shot" in s and not s.get("same_screen", True)]
    ordered = sorted(set(marked) | set(changed[:limit]))
    if ordered and len(ordered) > limit:
        # приоритет помеченным, остальные — равномерно
        rest = [s for s in ordered if s not in marked]
        stride = max(1, len(rest) // max(1, limit - len(marked)))
        ordered = sorted(set(marked) | set(rest[::stride]))[:limit]
    return ordered


def compact_trace(steps: list[dict]) -> str:
    lines = []
    for s in steps:
        if "action" in s:
            lines.append(f"[{s.get('t', 0):.0f}] действие {s['action']} {json.dumps({k: v for k, v in s.items() if k not in ('t', 'action')}, ensure_ascii=False)}")
        elif "note" in s and isinstance(s["note"], str) and s.get("kind"):
            lines.append(f"[шаг {s.get('step')}] заметка ({s['kind']}): {s['note']}")
        elif "mark" in s:
            lines.append(f"[шаг {s['mark']['step']}] помечен экран: {s['mark']['title']} — {s['mark']['description']}")
        elif "step" in s and "shot" in s:
            lines.append(f"[шаг {s['step']}] кадр {s['shot']} экран {'тот же' if s.get('same_screen') else 'новый'}")
        elif "finish" in s:
            lines.append(f"[итог] {json.dumps(s['finish'], ensure_ascii=False)}")
    return "\n".join(lines)


def image_block(path: Path, budget_tokens: int = 700) -> dict:
    small, _ = prepare_for_model(Image.open(path).convert("RGB"), budget_tokens=budget_tokens)
    buf = io.BytesIO()
    small.save(buf, format="WEBP", quality=80)
    return {"type": "image", "source": {"type": "base64", "media_type": "image/webp",
                                        "data": base64.b64encode(buf.getvalue()).decode()}}


def reflect(game: str, session_dir: Path) -> Reflection:
    client = anthropic.Anthropic()
    steps = load_steps(session_dir)
    content: list[dict] = []
    for step in keyframes(session_dir, steps):
        shot = session_dir / "shots" / f"{step:05d}.png"
        if shot.exists():
            content.append({"type": "text", "text": f"Кадр шага {step}:"})
            content.append(image_block(shot))
    content.append({"type": "text", "text": f"Игра: {game}. Сессия: {session_dir.name}.\n\nТрасса:\n{compact_trace(steps)}"})

    response = client.messages.parse(
        model=MODEL,
        max_tokens=16000,
        system=REFLECTOR_SYSTEM,
        output_config={"effort": "high"},
        messages=[{"role": "user", "content": content}],
        output_format=Reflection,
    )
    reflection = response.parsed_output
    (session_dir / "reflection.json").write_text(reflection.model_dump_json(indent=2), encoding="utf-8")

    # Кандидаты в уроки дописываются в конец; сливает и сокращает их компилятор вики.
    lessons_path = ROOT / "wiki" / game / "agent" / "lessons.md"
    lessons_path.parent.mkdir(parents=True, exist_ok=True)
    with lessons_path.open("a", encoding="utf-8") as f:
        for lesson in reflection.lessons:
            f.write(f"- [{lesson.scope}, c={lesson.confidence:.1f}, {session_dir.name}] {lesson.context}: {lesson.rule}\n")
    return reflection


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--game", required=True)
    ap.add_argument("--session", required=True)
    args = ap.parse_args()
    t0 = time.time()
    r = reflect(args.game, Path(args.session))
    print(f"фактов: {len(r.facts)}, уроков: {len(r.lessons)}, заявок в вики: {len(r.wiki_updates)}, {time.time() - t0:.0f} с")
