"""A solver's memory between the rounds of a level; the level catalog."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP, frames_dir  # noqa: E402
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

SP = Path(__file__).resolve().parent
T = TMP / "memtest"
DEV = ROOT
shutil.rmtree(T, ignore_errors=True)
T.mkdir()
G = "com.maroieqrwlk.unpin"
(T / "local.yaml").write_text(f"""machine: testbox
games: [{G}]
android: {{serials: [nophone]}}
fake_devices: {{fake1: "{frames_dir().as_posix()}"}}
video: {{record: false}}
state_dir: "{(T / 'state').as_posix()}"
raw_dir: "{(T / 'raw').as_posix()}"
wiki_dir: "{(T / 'gwiki').as_posix()}"
""", encoding="utf-8")
ENV = {**os.environ, "SW_LOCAL": str(T / "local.yaml"), "PYTHONIOENCODING": "utf-8"}


def sw(*a, expect_ok=True, device=True):
    r = subprocess.run([sys.executable, str(DEV / "harness" / "sw.py"), *(["-d", "fake1"] if device else []), *a],
                       capture_output=True, text=True, encoding="utf-8", env=ENV, cwd=DEV)
    if expect_ok and r.returncode != 0:
        raise SystemExit(f"FAIL {a}: {r.stdout}\n{r.stderr}")
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return r.stdout


def check(cond, msg):
    print(("OK   " if cond else "FAIL ") + msg)
    if not cond:
        raise SystemExit(1)


def notes(sid):
    return [x.get("note") for x in map(json.loads, (T / "raw" / G / sid / "steps.jsonl").read_text(encoding="utf-8")
                                       .splitlines()) if x.get("type") == "solve"]


s = sw("start", G)
sid = s["session"]
sd = T / "state" / G / "solvers"
sd.mkdir(parents=True, exist_ok=True)
(sd / "mem.py").write_text('''
def solve(image, board=None, frame_scale=1.0, state=None):
    n = (state or {}).get("n", 0) + 1
    w, h = image.size
    k = image.convert("L").resize((1, 1)).getpixel((0, 0)) % 50  # differs per frame: no repeated moves
    return {"moves": [[w // 3 + k + n, h // 3]], "note": f"round {n}", "rescan": True,
            "state": {"n": n, "seen": list(range(n))}}
''', encoding="utf-8")
sw("level", "start", "level 1", "--mechanic", "pins", "--plan", "x", "--value", "1")
sw("solve", "mem", "--run", "--rounds", "3")
check(notes(sid) == ["round 1", "round 2", "round 3"], f"the memory comes back in every round: {notes(sid)}")
r = sw("solve", "mem")
check(r["note"] == "round 4", "a check sees the memory")
sw("solve", "mem", "--run", "--rounds", "1")
check(notes(sid)[-1] == "round 4", f"a check does not change it; a later call in the level continues: {notes(sid)}")
sw("shot")
sw("level", "end", "won", "--note", "first level with a bomb")
sw("level", "start", "level 2", "--mechanic", "pins", "--plan", "x", "--value", "2")
sw("solve", "mem", "--run", "--rounds", "1")
check(notes(sid)[-1] == "round 1", "a new level starts with no memory")
(sd / "big.py").write_text('''
def solve(image, board=None, frame_scale=1.0, state=None):
    w, h = image.size
    return {"moves": [[w // 2, h // 2]], "note": "big", "state": {"x": "y" * 300000}}
''', encoding="utf-8")
r = sw("solve", "big", "--run", "--rounds", "1")
check("memory dropped" in json.dumps(r), "a memory over 200 KB is dropped with a note")
sw("level", "end", "lost", "--note", "bomb fell on the balls")
sw("level", "start", "level 2", "--mechanic", "pins", "--plan", "y", "--value", "2")
sw("taps", "10,10", "--why", "pin")
sw("shot")
sw("level", "end", "won", "--note", "bombs first")
sw("end", "--status", "ok", "--summary", "memory and catalog")

frame = next((T / "raw" / G / sid / "shots").glob("00001.jpg"))
st = T / "chain.json"
r1 = sw("solve", "mem", "--image", str(frame), "--game", G, "--state", str(st), device=False)
r2 = sw("solve", "mem", "--image", str(frame), "--game", G, "--state", str(st), device=False)
check(r1["note"] == "round 1" and r2["note"] == "round 2" and json.loads(st.read_text())["n"] == 2,
      "--image --state chains recorded frames like rounds")

out = T / "wiki" / G
r = sw("level-catalog", G, "--out", str(out), device=False)
page = (out / "levels.md").read_text(encoding="utf-8")
thumbs = sorted((out / "levels").glob("*.webp"))
check(r["levels"] == 2 and [t.name for t in thumbs] == ["0001.webp", "0002.webp"], f"one thumbnail per level: {thumbs}")
check("![level 1](levels/0001.webp)" in page and "| level 2 | pins | 1 won, 1 lost |" in page
      and "first level with a bomb" in page and "bombs first" in page, "the grid and the tries with the player's notes")
spans = sw("level-frames", G, "pins", device=False)
steps = [json.loads(x) for x in (T / "raw" / G / sid / "steps.jsonl").read_text(encoding="utf-8").splitlines()]
i = next(k for k, x in enumerate(steps) if x.get("type") == "level_start")
before = max(x["shot"] for x in steps[:i] if x.get("shot") and x.get("type") != "mark")
check(spans["start_frames"][0].endswith(f"{before + 1:05d}.jpg"),
      "a level's start frame is the solver's own frame before its first moves")
last = [k for k, x in enumerate(steps) if x.get("type") == "level_start"][-1]
before = max(x["shot"] for x in steps[:last] if x.get("shot") and x.get("type") != "mark")
check(spans["start_frames"][-1].endswith(f"{before:05d}.jpg"),
      "with no look before the first tap, it is the frame seen before the level began")
r = sw("level-catalog", G, "--out", str(out), "--set", "0002=none", device=False)
check(not (out / "levels" / "0002.webp").exists() and "no frame" in (out / "levels.md").read_text(encoding="utf-8")
      and r["levels"] == 2, "a level's frame can be dropped by hand, and it stays dropped")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
