"""Scenario test of levels, mechanics, model roles, batches and solvers on a fake device."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP, frames_dir  # noqa: E402
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

import yaml

SP = Path(__file__).resolve().parent
T = TMP / "lvtest"
DEV = ROOT
shutil.rmtree(T, ignore_errors=True)
T.mkdir()
(T / "local.yaml").write_text(f"""machine: testbox
games: [com.maroieqrwlk.unpin, com.block.juggle]
android: {{serials: [nophone]}}
fake_devices: {{fake1: "{frames_dir().as_posix()}"}}
video: {{record: false}}
state_dir: "{(T / 'state').as_posix()}"
raw_dir: "{(T / 'raw').as_posix()}"
wiki_dir: "{(T / 'gwiki').as_posix()}"
""", encoding="utf-8")
ENV = {**os.environ, "SW_LOCAL": str(T / "local.yaml"), "PYTHONIOENCODING": "utf-8"}
G, G2 = "com.maroieqrwlk.unpin", "com.block.juggle"
SESS = T / "state" / "sessions" / "fake1.json"


def sw(*a, expect_ok=True):
    r = subprocess.run([sys.executable, str(DEV / "harness" / "sw.py"), "-d", "fake1", *a], capture_output=True,
                       text=True, encoding="utf-8", env=ENV, cwd=DEV)
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


def shift_level(seconds_back, plan_too=True):
    """Pretend the open level started earlier."""
    s = json.loads(SESS.read_text(encoding="utf-8"))
    s["level"]["t0"] -= seconds_back
    if plan_too:
        s["level"]["plan_t"] -= seconds_back
    SESS.write_text(json.dumps(s), encoding="utf-8")


# a new game: the strong model learns the gameplay
c = sw("claim")["assignments"][0]
check(c["action"] == "play" and c["game"] == G and c["model_role"] == "study" and c["model"] == "opus",
      f"new game -> study model: {c.get('model_role')} / {c.get('model')} ({c.get('model_why')})")
s = sw("start", G)
check(s["model"] == "opus" and s["model_role"] == "study" and Path(s["playbook"]).exists(),
      "start: model from the reservation, local playbook created")
check("How to play" in Path(s["playbook"]).read_text(encoding="utf-8"), "playbook starts from the template")

r = sw("level", "start", "level 1", "--mechanic", "Pull pins", "--plan", "read the tutorial, pull the pin above the gold",
       "--value", "1")
check(r["new_mechanic"] and r["mechanic"]["status"] == "studying" and "handoff" not in r,
      "level start registers a new mechanic as studying; the study model keeps it")
r = sw("level", "start", "level 2", "--mechanic", "pull-pins", "--plan", "x", expect_ok=False)
check("still open" in json.dumps(r), "a second level cannot start while one is open")

r = sw("taps", "10,10 20,20;30,30>40,60", "--why", "three moves in a row")
check(r["moves_done"] == 3 and r["level"]["moves"] == 3 and r["level"]["decisions"] == 1,
      f"taps: 3 moves, one decision: {r.get('level')}")
r = sw("taps", "10,10 99999,5", "--why", "x", expect_ok=False)
check("outside" in json.dumps(r), "taps outside the screenshot are refused")
r = sw("taps", "10,10 abc", "--why", "x", expect_ok=False)
check("bad move" in json.dumps(r), "a malformed move is refused")
r = sw("taps", "10,10 !20,20 30,30", "--why", "x", expect_ok=False)
check("risky move" in json.dumps(r) and "ends a batch" in json.dumps(r), "a risky move in the middle of a batch is refused")
r = sw("taps", "10,10 12,12 !20,20", "--why", "two safe, one risky")
check(r["moves_done"] == 3 and "risky_move" in r, "a risky move last: played, and the reply says to check its result")
r = sw("taps", "10,10:2 20,20 !30,30:2", "--why", "double taps")
check(r["moves_done"] == 3, "double taps (X,Y:2) in a batch, a risky double tap last")
step = [json.loads(x) for x in open(next((T / "raw" / G).glob("*/steps.jsonl")), encoding="utf-8")][-1]
check(step["moves"][0] == [10.0, 10.0, 2.0] and step["moves"][1] == [20.0, 20.0], f"the log keeps double taps: {step['moves']}")
for bad in ("10,10:3", "10,10>20,20:2", "10:2"):
    r = sw("taps", bad, "--why", "x", expect_ok=False)
    check("bad move" in json.dumps(r), f"malformed double tap refused: {bad}")
r = sw("tap", "15", "15", "--double", "--why", "place a cat")
check(r["shot_n"] > 0, "tap --double")
hi = sw("shot", "--hi")
check("the next tap needs --frame" in hi["coords"], f"a --hi frame after normal ones says so: {hi['coords']}")
r = sw("tap", "10", "10", "--why", "keyboard A", expect_ok=False)
check("--frame" in json.dumps(r) and str(hi["shot_n"]) in json.dumps(r),
      "right after a --hi frame a tap without --frame is refused and the frames are named")
r = sw("taps", "10,10 20,20", "--why", "x", expect_ok=False)
check("--frame" in json.dumps(r), "the same for taps")
r = sw("tap", "10", "10", "--frame", str(hi["shot_n"]), "--why", "keyboard A from the --hi frame")
check(r["shot_n"] > hi["shot_n"], "with --frame <the --hi frame> the tap goes through")
r = sw("tap", "10", "10", "--why", "x", expect_ok=False)
check("--frame" in json.dumps(r), "back to a normal frame: the next tap needs --frame again")
r = sw("tap", "10", "10", "--frame", "99999", "--why", "x", expect_ok=False)
check("not among the recent frames" in json.dumps(r), "an unknown frame is refused")
sw("tap", "10", "10", "--frame", str(r.get("recent", ["1"])[-1] if isinstance(r, dict) else 1), "--why", "x",
   expect_ok=False)
sw("shot")
r = sw("tap", "10", "10", "--why", "normal frame after normal frame")
check(r["shot_n"] > 0, "normal frames in a row: no --frame needed")
r = sw("restart", "--why", "a playable ad that will not close")
step = [json.loads(x) for x in open(next((T / "raw" / G).glob("*/steps.jsonl")), encoding="utf-8")][-1]
check(r["restarted"] == G and step["type"] == "restart" and "playable ad" in step["why"], "restart: force-stop and start again, logged")

# the level clock: over the human's time -> change the method; then rethink without a new plan
shift_level(320)
r = sw("shot")
check(any("the time a human needs" in w for w in r.get("warnings", [])), "over 5 min: change the method, not the moves")
r = sw("shot")
check(any("stop trying moves" in w for w in r.get("warnings", [])), "2 min on one plan: rethink")
r = sw("shot")
check(not any("stop trying" in w for w in r.get("warnings", [])), "the rethink warning is not repeated for the same plan")
r = sw("level", "plan", "pull the right pin first, the lava goes down the left")
check(r["replans"] == 1, "level plan counts a replan")
r = sw("level", "end", "won", "--note", "right pin first; the tutorial hand shows the pin")
check(r["result"] == "won" and r["minutes"] >= 5 and r["mechanic"]["status"] == "studying",
      f"level 1 won in {r['minutes']} min: still studying")
v = yaml.safe_load(sw("research", G))
check(v["summary"]["progress"]["text"] == "level 1", "a won level records the progress")

# two fast levels in a row -> mastered
for n in (2, 3):
    sw("level", "start", f"level {n}", "--mechanic", "pull-pins", "--plan", "by the playbook", "--value", str(n))
    sw("taps", "50,50 60,60", "--why", "pins")
    r = sw("level", "end", "won", "--note", "fast")
check(r["mechanic"]["status"] == "mastered" and r.get("mechanic_change", {}).get("status") == "mastered",
      f"two fast levels -> mastered: {r.get('mechanic_change')}")
check(r["mechanic"]["levels"]["won"] == 3 and r["mechanic"]["typical_min"] is not None, "level stats kept")

# a level left open when the session ends counts as quit
sw("level", "start", "level 4", "--mechanic", "pull-pins", "--plan", "x")
sw("end", "--status", "ok", "--summary", "learned pull-pins")
v = yaml.safe_load(sw("research", G))
m = next(x for x in v["mechanics"] if x["id"] == "pull-pins")
check(m["levels"].get("quit") == 1 and m["status"] == "mastered", "open level at the end -> quit; quit does not demote")
meta = json.loads(next((T / "raw" / G).glob("*/session.json")).read_text(encoding="utf-8"))
check(meta["model"] == "opus" and meta["levels"]["won"] == 3 and meta["moves"] >= 7 and meta["gap_s_median"] is not None,
      f"session meta: model, levels, moves, gap: {meta['levels']} moves {meta['moves']}")

# every mechanic mastered -> the fast model (the second game was just played elsewhere: no turn for it now)
(T / "state" / G2).mkdir(parents=True, exist_ok=True)
with open(T / "state" / G2 / "sessions.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps({"id": "elsewhere", "device": "other", "game": G2, "started": time.strftime("%Y-%m-%dT%H:%M:%S"),
                        "minutes": 1, "steps": 0, "status": "ok"}) + chr(10))
c = sw("claim")["assignments"][0]
check(c["game"] == G and c["model_role"] == "play" and (c["model"], c["effort"]) == ("opus", "low"),
      f"mastered -> the game's own play model from games.yaml (Pull the Pin: opus:low): {c.get('model')}:{c.get('effort')}")
sw("end", "--status", "ok", "--summary", "release the reservation")

# the second game (lower priority) is played by the fast model and hands a new mechanic off
sw("start", G2, "--model", "sonnet")
s = json.loads(SESS.read_text(encoding="utf-8"))
s["model_role"] = "play"  # as if claim had given the play role
SESS.write_text(json.dumps(s), encoding="utf-8")
r = sw("level", "start", "level 20", "--mechanic", "lava-gates", "--plan", "look", "--mechanic-name", "Lava gates")
check("handoff" in r, "the play model meets a new mechanic -> told to hand off")
sw("level", "end", "quit", "--note", "new mechanic: gates open with a lever")
sw("end", "--status", "handoff", "--summary", "new mechanic lava-gates")
c = sw("claim")["assignments"][0]
check(c["game"] == G2 and c["model_role"] == "study" and "lava-gates" in c["model_why"],
      f"after a handoff that game goes first, with the study model: {c['game']} {c.get('model_why')}")
sw("end", "--status", "ok", "--summary", "release the reservation")
sw("start", G)

# a mastered mechanic that goes slow twice -> broken
for n in (21, 22):
    sw("level", "start", f"level {n}", "--mechanic", "pull-pins", "--plan", "x")
    shift_level(400)
    r = sw("level", "end", "won", "--note", "slow")
check(r.get("mechanic_change", {}).get("status") == "broken", "two slow levels -> broken")

# solvers: a local solver, dry run draws the moves, --run plays them; an unsafe one is refused
sd = T / "state" / G / "solvers"
sd.mkdir(parents=True, exist_ok=True)
(sd / "pull-pins.py").write_text('''
import numpy as np


def solve(image, board=None, frame_scale=1.0):
    a = np.asarray(image)
    h, w = a.shape[:2]
    return {"moves": [[w // 2, h // 2], [100, 200, 300, 400]], "note": f"board {w}x{h}"}
''', encoding="utf-8")
r = sw("solve", "pull-pins")
check(r["moves"] == 2 and Path(r["drawn"]).exists() and "board" in r["note"], f"solve (check): {r.get('note')}")
r = sw("solve", "pull-pins", "--run")
check(r["moves_done"] == 2 and r["rounds"] == 1, "solve --run plays the moves (one round)")
(sd / "rounds.py").write_text('''
def solve(image, board=None, frame_scale=1.0):
    return {"moves": [[10, 10], [20, 20]], "note": "two safe pairs, then look again", "rescan": True}
''', encoding="utf-8")
(sd / "rounds.py").write_text('''
def solve(image, board=None, frame_scale=1.0):
    w, h = image.size
    k = sum(image.convert("L").resize((1, 1)).getpixel((0, 0)) for _ in [0]) % 50  # differs per frame
    return {"moves": [[w // 3 + k, h // 3], [w // 2, h // 2]], "note": f"frame {w}x{h}, look again", "rescan": True}
''', encoding="utf-8")
r = sw("solve", "rounds", "--run", "--rounds", "3")
check(r["rounds"] == 3 and r["moves_done"] == 6 and "rescan" in r["stopped"],
      f"--rounds: frame -> solver -> moves three times: {r['stopped']}")
(sd / "same.py").write_text('''
def solve(image, board=None, frame_scale=1.0):
    return {"moves": [[10, 10], [20, 20]], "note": "1x1 board", "rescan": True}
''', encoding="utf-8")
r = sw("solve", "same", "--run", "--rounds", "5")
check(r["rounds"] == 2 and r["moves_done"] == 2 and "repeats the moves" in r["stopped"],
      f"the same moves again: stop instead of tapping blind: {r['stopped']}")
(sd / "finish.py").write_text('''
def solve(image, board=None, frame_scale=1.0):
    return {"moves": [[10, 10]], "note": "last pair", "done": True}
''', encoding="utf-8")
r = sw("solve", "finish", "--run", "--rounds", "5")
check(r["rounds"] == 1 and "finish the level" in r["stopped"], "a solver that finishes the level stops the rounds")
(sd / "stuck.py").write_text('''
def solve(image, board=None, frame_scale=1.0):
    return {"moves": [], "note": "no free pair: needs the tray"}
''', encoding="utf-8")
r = sw("solve", "stuck", "--run", "--rounds", "5")
check(r["moves_done"] == 0 and "no moves" in r["stopped"] and "tray" in r["stopped"], "no moves: stops and says why")
frame = next((T / "raw" / G).glob("*/shots/00001.jpg"))
r = sw("solve", "rounds", "--image", str(frame), "--game", G)
check(r["moves"] == 2 and r["rescan"] and Path(r["drawn"]).exists(), "--image: the solver is checked on a saved frame")
r = sw("mechanic", "pull-pins", "--method", "solver", "--status", "mastered")
check(r["mechanic"]["method"] == "solver" and r["mechanic"]["solver"] == f"solvers/{G}/pull-pins.py",
      "mechanic method solver points at the solver")
(sd / "bad.py").write_text("import subprocess\ndef solve(image, board=None, frame_scale=1.0):\n"
                           "    subprocess.run(['calc'])\n    return {'moves': []}\n", encoding="utf-8")
r = sw("solve", "bad", expect_ok=False)
check("refused" in json.dumps(r), "a solver that starts processes is refused")
r = sw("solve", "nosuch", expect_ok=False)
check("no solver" in json.dumps(r) and "solve(image" in json.dumps(r), "missing solver: the contract is explained")
sw("end", "--status", "ok", "--summary", "solver")

spec = importlib.util.spec_from_file_location("sw", DEV / "harness" / "sw.py")
os.environ.update(ENV)
swm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(swm)
check(swm.solver_problems("import cv2\nimport numpy as np\nx = np.zeros(3)") == [], "a pure solver passes the check")
check(swm.solver_problems("from os import system\nopen('x','w')") != [] and
      swm.solver_problems("requests.get(u)") != [] and swm.solver_problems("eval('1')") != [],
      "network, files and eval are caught")


class Dev:
    def __init__(self):
        self.taps = 0

    def tap(self, x, y):
        self.taps += 1

    def double_tap(self, x, y):
        self.taps += 1
        self.doubles = getattr(self, "doubles", 0) + 1

    swipe = tap


d = Dev()
done, why = swm.run_moves({"device": "fake1", "game": G, "platform": "fake"}, d, [(1, 1, 2), (2, 2)], 1.0, 0)
check(done == 2 and d.doubles == 1 and why is None, "run_moves: (x, y, 2) is a double tap on the device")
check(swm.solver_moves({"moves": [[5, 5, 2], [6, 6]]}, 100, 100) == [(5.0, 5.0, 2.0), (6.0, 6.0)],
      "a solver may return double taps [x, y, 2]")
d = Dev()
swm.app_on_screen = lambda c: "com.android.vending" if d.taps >= 2 else c["game"]
done, why = swm.run_moves({"device": "fake1", "game": G}, d, [(1, 1), (2, 2), (3, 3), (4, 4)], 1.0, 0)
check(done == 2 and "com.android.vending came on screen after move 2" in why,
      "a batch stops when a store or payment sheet comes on screen")
lc = T / "lc"
lc.mkdir()
(lc / "steps.jsonl").write_text(json.dumps({"t": 1, "step": 1, "type": "tap", "app": "com.android.chrome"}) + chr(10),
                                encoding="utf-8")
sent = []
swm.adb = lambda dev, *a, **k: sent.append(a) or ""
for fg, expect in (("com.android.chrome", "com.android.chrome"), ("com.whatsapp", None),
                   ("com.sec.android.app.launcher", None)):
    sent.clear()
    swm.focus = lambda d, fg=fg: fg
    got = swm.leave_clean({"device": "fake1", "game": G, "dir": str(lc)})
    check(got == expect and bool(sent) == bool(expect),
          f"session end, {fg} on screen: {'go home' if expect else 'leave it'}")
imgs = sorted(frames_dir().glob("*.png"))
check(swm.changed_px(imgs[0], imgs[0]) == 0 and swm.changed_px(imgs[0], imgs[1]) > 0,
      "frame change detection: same frame 0, different frames > 0")

from PIL import Image  # noqa: E402


class Phone:
    def screenshot(self):
        return Image.new("RGB", (1080, 2340), (40, 80, 120))


hd = T / "hi"
(hd / "shots").mkdir(parents=True)
hc = {"shots": 0, "dir": str(hd), "game": G, "platform": "fake", "same_streak": 0, "t0": time.time(), "budget_min": 10,
      "step": 0, "max_steps": 40}
info = swm.take_shot(hc, Phone(), hi=True)
check(max(info["size"]) <= 2000 and info["size"][0] > 730 and "tap in pixels of this" in info["coords"],
      f"a --hi frame fits the viewer unscaled: {info['size']}")
info = swm.take_shot(hc, Phone())
check(info["size"] == [730, 1583], f"a normal frame: {info['size']}")
check(info["step"] == 0 and "steps" in info, "every reply carries the step number")

# a Google Play payment sheet is closed by sw.py before anything can tap it
check(bool(swm.PAYMENT_WINDOW.search("com.android.vending/com.google.android.finsky.billing.acquire.LockToPortraitUiBuilderHostActivity"))
      and not swm.PAYMENT_WINDOW.search("com.android.vending/com.google.android.finsky.activities.MainActivity"),
      "payment windows are told apart from store pages")
seen = {"n": 0}


def on_screen(c):
    seen["n"] += 1
    return "com.android.vending" if seen["n"] == 1 else G


swm.app_on_screen = on_screen
swm.focus_window = lambda d: "com.android.vending/com.google.android.finsky.billing.acquire.SheetUiBuilderHostActivity"
sent.clear()
pc = {**hc, "platform": "android", "device": "fake1"}
info = swm.take_shot(pc, Phone())
check(info.get("payment_sheet_closed") and any("KEYCODE_BACK" in " ".join(a) for a in sent)
      and info["app"] == G and any("payment sheet" in w for w in info.get("warnings", [])),
      "a payment sheet on screen: sw.py presses back, warns, and the frame shows the game again")
import youtube  # noqa: E402

check(youtube.clean("Out of space -> Revive <b>", 100) == "Out of space → Revive ‹b›", "YouTube text without < >")

# playbook: a newer global playbook (a merged dream) replaces the local copy, the old one is kept
(T / "gwiki" / G / "agent").mkdir(parents=True, exist_ok=True)
time.sleep(1.1)
(T / "gwiki" / G / "agent" / "playbook.md").write_text("# How to play: merged\n", encoding="utf-8")
p = swm.ensure_playbook(G)
check(p.read_text(encoding="utf-8") == "# How to play: merged\n" and (p.parent / "playbook.prev.md").exists(),
      "a newer global playbook replaces the local copy; the old one is kept")
p.write_text("# How to play: merged\n\n## pull-pins\n- local edit\n", encoding="utf-8")
check("local edit" in swm.ensure_playbook(G).read_text(encoding="utf-8"), "local edits newer than the global stay")

# stats by model, render
st = sw("stats", "--by-model")
check({"opus", "sonnet"} <= set(st["by_model"]) and st["by_model"]["opus"]["levels_won_per_hour"] > 0,
      f"stats by model: {sorted(st['by_model'])}")
w = T / "wiki"
sw("snapshot", G, str(w / G / "research.yaml"), "--until", swm.now_iso(time.time() + 2))
sw("render", str(w))
tm = (w / G / "tasks.md").read_text(encoding="utf-8")
check("Gameplay (target: a level within 5 min" in tm and "**pull-pins** — mastered, solver" in tm,
      "tasks.md shows the gameplay and how it is learned")
sw("snapshot", G2, str(w / G2 / "research.yaml"), "--until", swm.now_iso(time.time() + 2))
sw("render", str(w))
check("**Lava gates** — studying" in (w / G2 / "tasks.md").read_text(encoding="utf-8"),
      "the handed-off mechanic shows as studying")
ry = yaml.safe_load((w / G / "research.yaml").read_text(encoding="utf-8"))
check(any(m["id"] == "pull-pins" and m["levels"]["won"] >= 5 for m in ry["mechanics"]), "research.yaml keeps mechanics")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
