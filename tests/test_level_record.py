"""The level record: a win needs a frame, moves with no level open are counted, late starts, retries, bonus boards."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP, frames_dir  # noqa: E402
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

T = TMP / "recordtest"
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
SESS = T / "state" / "sessions" / "fake1.json"


def run(*a, device=True):
    return subprocess.run([sys.executable, str(ROOT / "harness" / "sw.py"), *(["-d", "fake1"] if device else []), *a],
                          capture_output=True, text=True, encoding="utf-8", env=ENV, cwd=ROOT)


def sw(*a, expect_ok=True, device=True):
    r = run(*a, device=device)
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


def session(**change) -> dict:
    s = json.loads(SESS.read_text(encoding="utf-8"))
    if change:
        s.update(change)
        SESS.write_text(json.dumps(s), encoding="utf-8")
    return s


def ops(kind="level"):
    return [json.loads(x) for x in (T / "state" / G / "research.jsonl").read_text(encoding="utf-8").splitlines()
            if json.loads(x).get("op") == kind]


def steps(sid):
    return [json.loads(x) for x in (T / "raw" / G / sid / "steps.jsonl").read_text(encoding="utf-8").splitlines()]


def warned(r, text):
    return any(text in w for w in (r.get("warnings") or []))


sid = sw("start", G)["session"]
sd = T / "state" / G / "solvers"
sd.mkdir(parents=True, exist_ok=True)
(sd / "reader.py").write_text('''
def solve(image, board=None, frame_scale=1.0):
    k = image.convert("L").resize((1, 1)).getpixel((0, 0)) % 50  # differs per frame
    return {"moves": [[300 + k, 400]], "note": "one move"}
''', encoding="utf-8")
(sd / "finisher.py").write_text('''
def solve(image, board=None, frame_scale=1.0, state=None):
    n = (state or {}).get("n", 0) + 1
    if n == 1:
        return {"moves": [[100, 100]], "note": "the last pair", "rescan": True, "state": {"n": n}}
    return {"moves": [], "note": "board solved", "done": True, "state": {"n": n}}
''', encoding="utf-8")

# a game with no mechanics yet: taps walk menus, nothing to warn about
r = sw("taps", "10,10", "--why", "menu")
check(not warned(r, "no level is open"), "no mechanics yet: taps outside a level are menus, no warning")

# a won level needs a frame after its last move, of the game
r = sw("level", "start", "level 1", "--mechanic", "pins", "--plan", "x", "--value", "1")
check("moves_before" not in r, "the menu taps before the first mechanic are not a late start")
sw("taps", "10,10 20,20", "--why", "pins")
r = sw("level", "end", "won", "--note", "x", expect_ok=False)
check("take a frame of the win screen first" in json.dumps(r), "level end won right after the moves is refused")
sw("shot")
session(last_app="com.android.vending")
r = sw("level", "end", "won", "--note", "x", expect_ok=False)
check("not the game" in json.dumps(r) and "com.android.vending" in json.dumps(r),
      "level end won on a frame of the Play Store is refused")
shot = sw("shot")["shot_n"]
s = session()
s["level"]["t0"] -= 100  # level 1 took 100 s: the best time
session(level=s["level"])
r = sw("level", "end", "won", "--note", "x")
op = ops()[-1]
check(r["result"] == "won" and op["shot"] == shot and op.get("solve_s") is not None,
      f"after a shot the win is recorded with its frame and the time from the first move: {op.get('shot')}, {op.get('solve_s')}")

# a restart right after a win may undo it
r = run("restart", "--why", "an ad")
check(r.returncode != 0 and "--after-win" in r.stdout and "launch" in r.stdout,
      "restart within two minutes of a win is refused: launch, wait, then --after-win")
r = sw("restart", "--why", "an ad", "--after-win")
check(r["restarted"] == G, "restart --after-win goes through")

# moves with no level open in a game with levels: warned, counted; a late start says so
r = sw("taps", "30,30", "--why", "read and play before the start")
check(warned(r, "no level is open"), "taps with no level open in a game with mechanics: warned")
r = sw("solve", "reader")
check(warned(r, "no level is open"), "a solver call with no level open: warned")
r = sw("level", "start", "level 2", "--mechanic", "pins", "--plan", "x", "--value", "2")
st = [x for x in steps(sid) if x["type"] == "level_start"][-1]
check(r.get("moves_before") == 2 and warned(r, "not in this level") and st.get("moves_before") == 2,
      f"a late start: one move and one solver call before it, in the reply and the step: {r.get('moves_before')}")
sw("taps", "40,40", "--why", "x")
sw("shot")
sw("level", "end", "won", "--note", "late")
m = next(x for x in yaml.safe_load(sw("research", G, device=False))["mechanics"] if x["id"] == "pins")
check(ops()[-1].get("moves_before") == 2 and m["best_s"] >= 100 and m["recent"][-1].get("moves_before") == 2,
      f"the late level is recorded with moves_before and its short time is not the best time: {m['best_s']}")

# a win with no moves in 15 s is a leftover screen, unless it is a skip for a video
sw("level", "start", "level 3", "--mechanic", "pins", "--plan", "x", "--value", "3")
r = sw("level", "end", "won", "--note", "x", expect_ok=False)
check("no moves" in json.dumps(r) and "--skipped" in json.dumps(r), "a zero-move win in 15 s is refused")
r = sw("level", "end", "lost", "--note", "x", "--skipped", expect_ok=False)
check("--skipped" in json.dumps(r) and "won" in json.dumps(r), "--skipped is for wins only")
sw("level", "end", "won", "--note", "skipped for a video", "--skipped")
v = yaml.safe_load(sw("research", G, device=False))
m = next(x for x in v["mechanics"] if x["id"] == "pins")
check(ops()[-1].get("skipped") is True and m["best_s"] >= 100 and v["summary"]["progress"]["text"] == "level 3",
      "a skipped win: recorded as skipped, not a best time, the progress moves on")

# a stage lost and retried: one call, the loss recorded, the same level on a new clock
sw("level", "start", "level 4", "--mechanic", "pins", "--plan", "pins left first", "--value", "4")
sw("taps", "50,50", "--why", "x")
r = sw("level", "end", "won", "--note", "x", "--retry", expect_ok=False)
check("--retry" in json.dumps(r) and "lost" in json.dumps(r), "--retry follows a loss only")
r = sw("level", "end", "lost", "--note", "the bomb fell", "--retry")
lv = session()["level"]
check("retry" in r and lv["name"] == "level 4" and lv["value"] == 4 and lv["plan"] == "pins left first"
      and ops()[-1]["result"] == "lost", "level end lost --retry records the loss and opens the same level again")
sw("taps", "60,60", "--why", "x")
sw("shot")
r = sw("level", "end", "won", "--note", "right first")
check(r["mechanic"]["levels"] == {"won": 4, "lost": 1, "quit": 0}, f"the retry's win is a second record: {r['mechanic']['levels']}")

# a bonus board: no level number, no progress
r = sw("level", "start", "golden after L4", "--mechanic", "pins", "--plan", "x", "--bonus", "--value", "5",
       expect_ok=False)
check("bonus board has no level number" in json.dumps(r), "--bonus with --value is refused")
sw("level", "start", "golden after L4", "--mechanic", "pins", "--plan", "x", "--bonus")
sw("taps", "70,70", "--why", "x")
sw("shot")
sw("level", "end", "won", "--note", "golden board")
v = yaml.safe_load(sw("research", G, device=False))
check(ops()[-1].get("bonus") is True and v["summary"]["progress"]["text"] == "level 4",
      "a bonus board's win is recorded as bonus and does not move the progress")

# solve --run says "solved" only after a round that changed the frame
sw("level", "start", "level 5", "--mechanic", "pins", "--plan", "x", "--value", "5")
r = sw("solve", "finisher", "--run", "--rounds", "3")
check(r["stopped"] == "solved" and r["moves_done"] == 1 and "level end won" in r.get("next", ""),
      f"the moves changed the board, then the solver says done: solved, and a frame is asked for: {r['stopped']}")
r = sw("solve", "finisher", "--run", "--rounds", "3")
check(r["stopped"] != "solved" and "did not change" in r["stopped"] and r["moves_done"] == 0,
      f"done on a frame no round of this call changed: look at it: {r['stopped']}")

# a restart with a level open says it will be recorded as quit
r = sw("restart", "--why", "an ad that will not close")
check(warned(r, "still open") and warned(r, "quit"), "restart with an open level: the reply says it ends as quit")
sw("end", "--status", "ok", "--summary", "level records")
meta = json.loads((T / "raw" / G / sid / "session.json").read_text(encoding="utf-8"))
check(meta["moves_outside_level"] == 1 and meta["levels"]["won"] == 5 and ops()[-1]["result"] == "quit",
      f"session.json: moves outside a level (the taps; a solver check plays none): {meta['moves_outside_level']}")
st = sw("stats", G, device=False)
row = st["games"][G]["sessions"][0]
check(row["moves_outside_level"] == 1 and st["games"][G]["moves_outside_level"] == 1 and row["levels_won"] == 5
      and "repeated_steps" in row, "stats: moves outside a level per session and per game")

# the level frames: a late start begins after the previous level; a bonus board is filed under its name
restart = next(x for x in steps(sid) if x["type"] == "restart")
fr = sw("level-frames", G, "pins", device=False)
lv2 = fr["start_frames"][1]
check(lv2.endswith(f"{restart['shot']:05d}.jpg"),
      f"a late start's first frame is the first after the previous level ended, not a win screen: {Path(lv2).name}")
out = T / "wiki" / G
r = sw("level-catalog", G, "--out", str(out), device=False)
names = sorted(p.name for p in (out / "levels").glob("*.webp"))
check("golden-after-l4.webp" in names and "0005.webp" in names and len(names) == 6,
      f"the catalog files the bonus board under its name, not the next number: {names}")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
