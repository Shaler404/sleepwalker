"""Компиляция вики («сон» агента): раз в сутки слить новые рефлексии в wiki/<game>/.

Модель правит страницы через memory tool: каталог /memories отображается на
wiki/<game>/ (view / create / str_replace / insert / delete / rename). Так не
нужно писать свой файловый редактор, а правки получаются точечными.

Запуск: python compile_wiki.py --game com.example.game [--lint]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import time
from pathlib import Path

import anthropic
from anthropic.tools import BetaLocalFilesystemMemoryTool
from PIL import Image

from perception import save_for_wiki, screen_hash

MODEL = "claude-opus-5-5"
ROOT = Path(os.environ.get("SW_ROOT") or Path(__file__).resolve().parent.parent)  # корень репозитория (или worktree «сна»)
SCHEMA = (ROOT / "schema" / "WIKI-SCHEMA.md").read_text(encoding="utf-8")

COMPILER_SYSTEM = """Ты — единственный редактор вики по игре. Каталог /memories — это wiki/<game>/ этой игры.
Соблюдай схему вики буквально. Сначала view /memories и прочитай index.md, log.md, open-questions.md,
agent/lessons.md. Затем разбери новые материалы из сообщения: для каждого факта реши — новая страница,
дополнение, противоречие (блок «⚠️ Ранее …») или уже известно. Правь точечно (str_replace / insert),
обновляй фронтматтер (version_seen, verified_at, sources, confidence), вставляй изображения только из
манифеста с содержательными подписями. Обнови index.md, log.md, open-questions.md, слей agent/lessons.md
(<= 60 пунктов). Не выдумывай факты. В конце перечисли изменённые страницы и нерешённые противоречия."""

LINTER_SYSTEM = """Ты проверяешь вики по игре (каталог /memories) по разделу «Lint» схемы. Механические проблемы
исправляй сам (битые ссылки, index.md, изображения без ссылок). Содержательные (противоречия в числах, факты
без источников, страницы старше 30 дней) — не исправляй, а опиши в agent/lint.md как задачи для следующих
сессий: приоритет, страница, что перепроверить в игре и на каком экране."""


def slug(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text.lower(), flags=re.UNICODE)
    return re.sub(r"[\s_-]+", "-", text).strip("-")[:40] or "screen"


def import_images(game: str, sessions: list[Path]) -> list[str]:
    """Помеченные кадры -> wiki/<game>/img/YYYYMMDD-<slug>-<hash8>.webp (без дублей). Возвращает манифест."""
    img_dir = ROOT / "wiki" / game / "img"
    img_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    for sdir in sessions:
        marked_file = sdir / "marked.json"
        if not marked_file.exists():
            continue
        day = sdir.name[:8]
        for m in json.loads(marked_file.read_text(encoding="utf-8")):
            shot = sdir / "shots" / m["shot"]
            if not shot.exists():
                continue
            img = Image.open(shot).convert("RGB")
            h8 = hashlib.sha1(screen_hash(img).encode()).hexdigest()[:8]
            name = f"{day}-{slug(m['title'])}-{h8}.webp"
            if not (img_dir / name).exists():
                save_for_wiki(img, str(img_dir / name))
                save_for_wiki(img, str(img_dir / name.replace(".webp", "-thumb.webp")), long_edge=360, quality=70)
            manifest.append(f"img/{name} | {m['title']} | {m['description']} | {sdir.name}#{m['step']}")
    return manifest


def new_sessions(game: str, since: float) -> list[Path]:
    raw = ROOT / "raw" / game
    if not raw.exists():
        return []
    return sorted(p for p in raw.iterdir() if (p / "reflection.json").exists() and (p / "reflection.json").stat().st_mtime > since)


def run_editor(game: str, system: str, user_text: str, max_iterations: int = 300) -> str:
    client = anthropic.Anthropic()
    memory = BetaLocalFilesystemMemoryTool(base_path=str(ROOT / "wiki" / game))
    runner = client.beta.messages.tool_runner(
        model=MODEL,
        max_tokens=16000,
        system=[
            {"type": "text", "text": system},
            {"type": "text", "text": "Схема вики:\n\n" + SCHEMA, "cache_control": {"type": "ephemeral"}},
        ],
        messages=[{"role": "user", "content": user_text}],
        tools=[memory],
        max_iterations=max_iterations,
        output_config={"effort": "high"},
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
    )
    final = runner.until_done()
    return "\n".join(b.text for b in final.content if b.type == "text")


def compile_game(game: str, lint: bool = False) -> None:
    state_file = ROOT / "wiki" / game / ".compile-state.json"
    state = json.loads(state_file.read_text(encoding="utf-8")) if state_file.exists() else {"last_compiled": 0}
    sessions = new_sessions(game, state["last_compiled"])
    if not sessions:
        print(f"{game}: новых рефлексий нет")
        return

    manifest = import_images(game, sessions)
    reflections = []
    for sdir in sessions:
        r = json.loads((sdir / "reflection.json").read_text(encoding="utf-8"))
        reflections.append({"session": sdir.name, **r})

    user_text = (
        f"Игра: {game}. Новых сессий: {len(sessions)}.\n\n"
        f"Рефлексии (JSON):\n{json.dumps(reflections, ensure_ascii=False)[:180000]}\n\n"
        "Доступные изображения (path | title | description | источник):\n" + "\n".join(manifest)
    )
    report = run_editor(game, COMPILER_SYSTEM, user_text)
    print(report)

    if lint:
        print(run_editor(game, LINTER_SYSTEM, f"Игра: {game}. Проведи lint-проверку и запиши agent/lint.md."))

    state["last_compiled"] = time.time()
    state_file.write_text(json.dumps(state), encoding="utf-8")
    subprocess.run(["git", "-C", str(ROOT), "add", "-A", f"wiki/{game}"], check=False)
    subprocess.run(["git", "-C", str(ROOT), "commit", "-q", "-m", f"wiki({game}): compile {len(sessions)} sessions"], check=False)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--game", required=True)
    ap.add_argument("--lint", action="store_true")
    args = ap.parse_args()
    compile_game(args.game, lint=args.lint)
