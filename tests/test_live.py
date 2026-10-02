"""Live tables: the Wiki tab shows the tasks as the players see them now, not as of the last dream."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP  # noqa: E402

import importlib.util
import json
import os
import shutil
import subprocess
import sys

T = TMP / "livetest"
shutil.rmtree(T, ignore_errors=True)
G = "com.maroieqrwlk.unpin"
w = T / "wiki"
(w / G).mkdir(parents=True)
(w / G / "research.yaml").write_text(f"game: {G}\nfeatures: []\ntasks: []\nmechanics: []\n", encoding="utf-8")
(w / G / "index.md").write_text("# Pull the Pin\n", encoding="utf-8")
(w / G / "tasks.md").write_text("# Tasks: Pull the Pin\n\nas of the last dream\n", encoding="utf-8")
(w / G / "features.md").write_text("# Features: Pull the Pin\n", encoding="utf-8")
(w / "index.md").write_text("# Game wiki\n", encoding="utf-8")
(w / "tasks.md").write_text("# Tasks by game\n", encoding="utf-8")
(T / "local.yaml").write_text(f'machine: livebox\ngames: [{G}]\nwiki_dir: "{w.as_posix()}"\n'
                              f'state_dir: "{(T / "state").as_posix()}"\nraw_dir: "{(T / "raw").as_posix()}"\n',
                              encoding="utf-8")
ENV = {**os.environ, "SW_LOCAL": str(T / "local.yaml"), "PYTHONIOENCODING": "utf-8"}
os.environ["SW_LOCAL"] = str(T / "local.yaml")


def check(cond, msg):
    print(("OK   " if cond else "FAIL ") + msg)
    if not cond:
        raise SystemExit(1)


# a goal the reviewer sets right after a session goes into this machine's journal, not into the wiki
r = subprocess.run([sys.executable, str(ROOT / "harness" / "sw.py"), "task", "add", "live-check",
                    "Check that the live table shows this goal", "--kind", "experiment", "--plan", "x", "--game", G],
                   capture_output=True, text=True, encoding="utf-8", env=ENV)
check(r.returncode == 0, f"a goal added after a session: {r.stdout[-200:]}{r.stderr[-200:]}")

spec = importlib.util.spec_from_file_location("sw", ROOT / "harness" / "sw.py")
swm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(swm)
pages = swm.live_tables([G])
check("Check that the live table shows this goal" in pages[f"{G}/tasks.md"]
      and f"{G}/features.md" in pages and "# Tasks by game" in pages["tasks.md"],
      "the live tables carry the new goal, with the features and the overview")
check("Check that the live table shows this goal" not in (w / G / "tasks.md").read_text(encoding="utf-8"),
      "the repository's copy waits for the dream")
clone = T / "clone"
clone.mkdir()
names = swm.wiki_page_names(w)
written = swm.write_live(clone, names, "Owner/repo", [G])
page = (clone / f"{swm.wiki_file(names[f'{G}/tasks.md'])}.md").read_text(encoding="utf-8")
check(f"{G}/tasks.md" in written and page.startswith("*Live: generated from the newest sessions on livebox")
      and "Check that the live table shows this goal" in page and "blob/main/wiki/" in page,
      "the Wiki tab page is the live table with a note pointing at the reviewed copy")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
