"""The GitHub Wiki mirror: flat unique page names, rewritten links and images."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP, frames_dir  # noqa: E402
import importlib.util
import os
import shutil
from pathlib import Path

SP = Path(__file__).resolve().parent
T = TMP / "mirtest"
DEV = ROOT
shutil.rmtree(T, ignore_errors=True)
w = T / "wiki"
G = "com.maroieqrwlk.unpin"
(w / G / "features").mkdir(parents=True)
(w / G / "agent").mkdir()
(w / "index.md").write_text(f"# Game wiki\n\n[Pull the Pin]({G}/index.md) · [games](../games.yaml)\n", encoding="utf-8")
(w / G / "index.md").write_text("# Pull the Pin\n\n[Settings](features/settings.md) · [tasks](tasks.md) · "
                                "[map](research.yaml)\n", encoding="utf-8")
(w / G / "tasks.md").write_text("# Tasks: Pull the Pin\n", encoding="utf-8")
(w / G / "agent" / "playbook.md").write_text("# How to play: Pull the Pin\n", encoding="utf-8")
(w / G / "features" / "settings.md").write_text(
    '---\ngame: x\ntitle: "Settings (gear)"\n---\n\n# Settings (gear)\n\n![the gear](../img/a.webp)\n'
    "See [Collections](collections.md#tabs) and [Google Play](https://play.google.com).\n", encoding="utf-8")
(w / G / "features" / "collections.md").write_text('---\ntitle: "Collections"\n---\n# Collections\n', encoding="utf-8")
(w / G / "features" / "collections.skeleton.md").write_text("# skeleton\n", encoding="utf-8")
(T / "local.yaml").write_text(f'machine: t\nwiki_dir: "{w.as_posix()}"\nstate_dir: "{(T / "state").as_posix()}"\n',
                              encoding="utf-8")
os.environ.update({"SW_LOCAL": str(T / "local.yaml")})
spec = importlib.util.spec_from_file_location("sw", DEV / "harness" / "sw.py")
swm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(swm)


def check(cond, msg):
    print(("OK   " if cond else "FAIL ") + msg)
    if not cond:
        raise SystemExit(1)


names = swm.wiki_page_names(w)
check(names["index.md"] == "Home" and names[f"{G}/index.md"] == "Pull the Pin"
      and names[f"{G}/features/settings.md"] == "Pull the Pin · Settings gear"
      and names[f"{G}/agent/playbook.md"] == "Pull the Pin · How to play"
      and f"{G}/features/collections.skeleton.md" not in names, f"page names: {names}")
check(len(set(names.values())) == len(names), "page names are unique")
s = swm.mirror_page(w, f"{G}/features/settings.md", names, "Owner/repo")
check(s.startswith("*A mirror of") and "title:" not in s, "a mirror note instead of the front matter")
check(f"(https://raw.githubusercontent.com/Owner/repo/main/wiki/{G}/img/a.webp)" in s, "images come from the repository")
check("[Collections](Pull-the-Pin-·-Collections#tabs)" in s and "(https://play.google.com)" in s,
      "links between pages become wiki links, anchors and external links stay")
s = swm.mirror_page(w, f"{G}/index.md", names, "Owner/repo")
check(f"(https://github.com/Owner/repo/blob/main/wiki/{G}/research.yaml)" in s, "links to repository files point to GitHub")
s = swm.mirror_page(w, "index.md", names, "Owner/repo")
check("(https://github.com/Owner/repo/blob/main/games.yaml)" in s and "[Pull the Pin](Pull-the-Pin)" in s,
      "files outside the wiki point to the repository")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
