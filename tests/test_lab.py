"""The lab: which mechanics need work (a solver worked around too), one lab per game, level frames, the method
set without a session."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP, frames_dir  # noqa: E402
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

SP = Path(__file__).resolve().parent
T = TMP / "labtest"
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


r = sw("lab-check", G, device=False)
check(r["needed"] == [] and not r["running"], "nothing to do for a game without mechanics")

sw("start", G)
for i in (1, 2):
    sw("level", "start", f"level {i}", "--mechanic", "pins", "--plan", "x", "--value", str(i))
    sw("taps", "10,10 20,20", "--why", "moves")
    sw("tap", "30", "30", "--why", "one more")
    sw("shot")
    sw("level", "end", "won" if i == 1 else "lost", "--note", "slow by eye")
sw("end", "--status", "ok", "--summary", "two levels")

r = sw("lab-check", G, device=False)
check([m["id"] for m in r["needed"]] == ["pins"] and r["needed"][0]["why"] == "studying", f"a studying mechanic needs the lab: {r['needed']}")
r = sw("lab-check", G, "--claim", device=False)
check(r.get("claimed") is True, "the lab is claimed")
r = sw("lab-check", G, "--claim", device=False)
check(r["running"] and not r.get("claimed"), "one lab per game at a time")

r = sw("level-frames", G, "pins", device=False)
check(r["levels"] == 2 and len(r["start_frames"]) == 2 and all(Path(f).exists() for f in r["start_frames"])
      and [s["result"] for s in r["spans"]] == ["won", "lost"] and all(s["frames"] >= 2 for s in r["spans"]),
      f"level frames: {r['spans']}")

sd = T / "state" / G / "solvers"
sd.mkdir(parents=True, exist_ok=True)
(sd / "pins.py").write_text("def solve(image, board=None, frame_scale=1.0):\n    return {'moves': [[5, 5]], 'note': 'x'}\n",
                            encoding="utf-8")
r = sw("solve", "pins", "--image", r["start_frames"][0], "--game", G, device=False)
check(r["moves"] == 1, "the solver is checked on a recorded start frame without the phone")
r = sw("mechanic", "pins", "--game", G, "--method", "solver", "--note", "lab: solver from 2 boards", device=False)
check(r["mechanic"]["method"] == "solver" and r["mechanic"]["status"] == "studying",
      "the lab sets the method without a session; the status stays for the phone to decide")
r = sw("lab-done", G, "--note", "solver written, checked on 2 start frames", device=False)
check(Path(r["log"]).read_text(encoding="utf-8").count("solver written") == 1, "lab-done logs and frees the lab")
r = sw("lab-check", G, "--claim", device=False)
check(r.get("claimed") is True, "the next lab can run")

# a solver mechanic the player works around: fast levels, a mastered label, and the lab still takes it
# (2026-10-01: Meowdoku queens placed by hand, MeowTrail akari boards typed, solvers returning nothing)
solvers = {
    "queens": "return {'moves': [[5, 5]], 'note': 'one cat, the rest unread'}",
    "akari": "return {'moves': [[5, 5], [6, 6]], 'done': True} if board else {'moves': [], 'note': 'no board'}",
    "tiles": "return {'moves': [[5, 5], [6, 6]], 'note': 'the same pairs', 'rescan': True}",
    "fast": "return {'moves': [[5, 5], [6, 6], [7, 7]], 'note': 'whole board', 'done': True}",
}
for mech, body in solvers.items():
    (sd / f"{mech}.py").write_text(f"def solve(image, board=None, frame_scale=1.0):\n    {body}\n", encoding="utf-8")
    sw("mechanic", mech, mech.title(), "--status", "mastered", "--method", "solver", "--game", G, device=False)
board = T / "board.json"
board.write_text('{"grid": ["..#", "#..", "..."]}', encoding="utf-8")
sw("start", G)


def level(mech, n, *plays):
    sw("level", "start", f"level {n}", "--mechanic", mech, "--plan", "x", "--value", str(n))
    for p in plays:
        sw(*p, "--settle", "0")
    sw("shot")  # a frame of the win screen: level end won needs one after the last move
    sw("level", "end", "won", "--note", "fast")


for n in (44, 45, 46):  # the solver places one cat, the model the rest by hand
    level("queens", n, ("solve", "queens", "--run"), ("taps", "10,10 20,20 30,30", "--why", "cats by hand"))
for n in (1, 2):  # the board read by eye and typed for the solver every level
    level("akari", n, ("solve", "akari", "--board", str(board)), ("solve", "akari", "--board", str(board), "--run"))
level("tiles", 7, ("solve", "tiles", "--run", "--rounds", "4"))  # the same moves again: stopped
(sd / "tiles.py").write_text("def solve(image, board=None, frame_scale=1.0):\n    return {'moves': [], 'note': 'misread'}\n",
                             encoding="utf-8")
# no moves; the pair is found by hand (a win with no moves at all would be refused as a stale win screen)
level("tiles", 8, ("solve", "tiles", "--run"), ("tap", "40", "40", "--why", "the pair by hand"))
for n in range(10, 15):  # the solver plays the level; one tap closes a popup
    level("fast", n, ("solve", "fast", "--run", "--rounds", "5"), ("tap", "40", "40", "--why", "close the hint popup"))
sw("end", "--status", "ok", "--summary", "solver levels")
steps = [json.loads(x) for x in open(sorted((T / "raw" / G).glob("*/steps.jsonl"))[-1], encoding="utf-8")]
ends = [x for x in steps if x["type"] == "solve_end"]
check([x["board"] for x in ends if x["mechanic"] == "akari"] == [True, True]
      and [x["gave_up"] for x in ends if x["mechanic"] == "tiles"] == [True, True]
      and not any(x["gave_up"] for x in ends if x["mechanic"] in ("queens", "fast")),
      "the steps keep how each solve run ended and whether it took a typed board")
need = {m["id"]: m["why"] for m in sw("lab-check", G, device=False)["needed"]}
check(need.get("queens") == "solver bypassed: 3 of 3 levels placed by hand", f"queens: {need.get('queens')}")
check("board typed by hand (--board) in every solver call of 2 levels" in need.get("akari", ""), f"akari: {need.get('akari')}")
check(need.get("tiles", "").startswith("solver gave up in 2 of 2 levels"), f"tiles: {need.get('tiles')}")
check("fast" not in need, "a solver that plays its levels within the budget: no lab")
check(need.get("pins") == "studying; solver bypassed: 2 of 2 levels placed by hand", f"pins: {need.get('pins')}")
pb = sw("playbook", "--game", G, device=False)
check("solver_sign: 'solver bypassed: 3 of 3 levels placed by hand'" in pb and pb.count("solver_sign") == 4,
      "the playbook shows the sign next to the mechanic")
spec = importlib.util.spec_from_file_location("sw", DEV / "harness" / "sw.py")
os.environ.update(ENV)
swm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(swm)
lv = lambda h, s, **k: {"play": {"hand": h, "solver": s, "calls": 0, "boards": 0, "gave_up": 0, **k}}  # noqa: E731
check(swm.solver_bypassed([lv(9, 0), lv(1, 20), lv(0, 30), lv(2, 25), lv(0, 0)]) is None,
      "one level of five by hand, nothing else: no sign")
check(swm.solver_bypassed([lv(9, 0), lv(9, 0)] + [lv(0, 30)] * 5) is None, "only the last five levels count")
check(swm.solver_bypassed([lv(0, 9, calls=1, boards=1), lv(0, 9, calls=2, boards=1)]) is None,
      "a board typed once, then read by the solver: no sign")

off = "com.crypt.gram.puzz"  # in games.yaml, not played on this machine (or off)
r = sw("lab-check", off, device=False)
check(r["game"] == off and r["needed"] == [], "the lab and the review work on a game this machine does not play")
r = sw("start", off, expect_ok=False)
check("is off on this machine" in json.dumps(r), "but a session of it is refused")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
