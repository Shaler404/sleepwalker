"""Process fixes of the 2026-10-06 dream (chrono): `level end won` right after a move is accepted when the frame
taken now shows the same screen as the one claimed on; `--source <session>#<step>` beyond the session's steps is a
frame number and is refused with the step that took it; a placeholder case text is refused; `task list` exists; a
wait that finds the screen dimmed says whether touch protection is already up."""
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

T = TMP / "pf1006"
shutil.rmtree(T, ignore_errors=True)
T.mkdir()
G = "com.oakever.meowdoku"
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
os.environ.update(ENV)
SESS = T / "state" / "sessions" / "fake1.json"
spec = importlib.util.spec_from_file_location("sw", ROOT / "harness" / "sw.py")
swm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(swm)


def check(cond, msg):
    print(("OK   " if cond else "FAIL ") + msg)
    if not cond:
        raise SystemExit(1)


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


def session(**change) -> dict:
    s = json.loads(SESS.read_text(encoding="utf-8"))
    if change:
        for k, v in change.items():
            s[k] = v
        SESS.write_text(json.dumps(s), encoding="utf-8")
    return s


def ops(kind):
    p = T / "state" / G / "research.jsonl"
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if json.loads(x).get("op") == kind]


def steps():
    return [json.loads(x) for x in (Path(session()["dir"]) / "steps.jsonl").read_text(encoding="utf-8").splitlines()]


def feature(fid):
    return next(f for f in swm.research_view(G)["features"] if f["id"] == fid)


sid = sw("start", G)["session"]

# --- 1. level end won right after a move: accepted on an unchanged screen, refused on a changed one ---------------
sw("level", "start", "level 1", "--mechanic", "queens", "--plan", "x", "--value", "1")
sw("taps", "10,10 20,20", "--why", "cats")
claimed = session()["last_shot"]
r = sw("level", "end", "won", "--note", "solver")
op = ops("level")[-1]
check(r["result"] == "won" and r.get("frame") and r["shot"] == claimed + 1 and op["shot"] == claimed + 1,
      f"the claim on a stable screen is accepted in one call, recorded on the frame taken now: {r.get('shot')} after {claimed}")
look = [x for x in steps() if x.get("type") == "shot" and str(x.get("why", "")).startswith("level end won")]
check(len(look) == 1 and look[-1]["shot"] == claimed + 1 and look[-1].get("same") is True,
      "the frame taken for the claim is a shot step of the session, the same screen as the move's frame")
check(session().get("level") is None, "the level is closed: the next level start is not refused")

sw("level", "start", "level 2", "--mechanic", "queens", "--plan", "x", "--value", "2")
sw("taps", "10,10", "--why", "cats")
claimed = session()["last_shot"]
session(fake_i=session().get("fake_i", 0) + 1)  # the screen moves on after the move: a win animation, a popup
r = sw("level", "end", "won", "--note", "solver", expect_ok=False)
check("take a frame" in json.dumps(r) and r.get("shot_n") == claimed + 1 and "--shot N" in json.dumps(r),
      f"a screen that changed after the move is refused as before, with the frame taken now: {r.get('shot_n')}")
check(session().get("level") and session()["level"]["name"] == "level 2", "the level stays open after the refusal")
r = sw("level", "end", "won", "--note", "solver")
check(r["result"] == "won" and "frame" not in r and ops("level")[-1]["shot"] == claimed + 1,
      "the repeated claim after the look records the win as before")

sw("level", "start", "level 3", "--mechanic", "queens", "--plan", "x", "--value", "3")
r = sw("level", "end", "won", "--note", "x", expect_ok=False)
check("no moves" in json.dumps(r), "a stable screen does not excuse a win with no moves: the zero-move refusal stands")
sw("taps", "10,10", "--why", "cats")
sw("key", "back", "--why", "leave the win screen")  # the screen after Back is stable too, but it is not the win screen
r = sw("level", "end", "won", "--note", "x", expect_ok=False)
check("take a frame" in json.dumps(r) and "--shot N" in json.dumps(r) and session().get("level"),
      "a stable screen after Back (not a move) is refused as before: the win frame is named with --shot")
sw("level", "end", "quit", "--note", "x")

# --- 2. --source beyond the session's steps is a frame number ------------------------------------------------------
sw("feature", "settings", "Settings", "--type", "system", "--appeared", "on the home screen")
step = session()["step"]
last_shot = session()["last_shot"]
check(last_shot > step, f"the fake session has more frames ({last_shot}) than steps ({step}): the slip is possible")
r = sw("case", "settings", "chk-screen", "a gear, five rows", "--done", "--source", f"{sid}#{last_shot}", expect_ok=False)
at = next(x["step"] for x in steps() if x.get("shot") == last_shot and x.get("type") not in ("mark", "research"))
check("not the frame number" in json.dumps(r) and r.get("last_step") == step and r.get("frame_step") == at
      and f"--source {sid}#{at}" in r["error"],
      f"a step the session does not have is refused as a frame number, with the step that took it: {at}")
check(not next(c for c in feature("settings")["cases"] if c["id"] == "chk-screen").get("done"),
      "the refused case stays open")
r = sw("case", "settings", "chk-screen", "a gear, five rows", "--done", "--source", f"{sid}#{step}")
check(next(c for c in feature("settings")["cases"] if c["id"] == "chk-screen")["source"] == f"{sid}#{step}",
      "a step the session has is accepted as given")
r = sw("case", "settings", "chk-entry", "the gear top right", "--done", "--source", f"{sid}#999", expect_ok=False)
check("not the frame number" in json.dumps(r) and "frame_step" not in r,
      "a number that is neither a step nor a frame is refused without a mapping")
other = "20261005-000000-testbox-FAKE"
d = T / "raw" / G / other
d.mkdir(parents=True)
with open(d / "steps.jsonl", "w", encoding="utf-8") as f:
    for n, t in ((0, "start"), (1, "tap"), (2, "tap"), (3, "shot"), (4, "tap"), (5, "end")):
        f.write(json.dumps({"t": time.time(), "step": n, "type": t, **({"shot": n + 3} if t in ("tap", "shot") else {})}) + "\n")
r = sw("case", "settings", "chk-entry", "the gear top right", "--done", "--source", f"{other}#7", expect_ok=False)
check(f"{other} ended at step 5" in r["error"] and r.get("frame_step") == 4,
      "another session's steps.jsonl bounds its sources too, with the frame's step")
r = sw("case", "settings", "chk-entry", "the gear top right", "--done", "--game", G, "--source", f"{other}#7",
       device=False, expect_ok=False)
check("not the frame number" in json.dumps(r) and r.get("frame_step") == 4,
      "the review's --source (case --game, no session in hand) is checked the same way")
r = sw("case", "settings", "chk-entry", "the gear top right", "--done", "--source", f"{other}#3")
check(next(c for c in feature("settings")["cases"] if c["id"] == "chk-entry")["source"] == f"{other}#3",
      "a step the other session has is accepted")
gone = "20261001-000000-gone-FAKE#40"
r = sw("case", "settings", "about", "About opens a web page", "--done", "--source", gone)
check(next(c for c in feature("settings")["cases"] if c["id"] == "about")["source"] == gone,
      "a session whose raw is gone is not checked")
sw("task", "add", "look-shop", "Look at the shop")

# --- 3. a placeholder case text ------------------------------------------------------------------------------------
before = next(c for c in feature("settings")["cases"] if c["id"] == "chk-screen")["text"]
r = sw("case", "settings", "chk-screen", "x", "--done", expect_ok=False)
check("placeholder" in json.dumps(r), "a one-letter case text is refused")
check(next(c for c in feature("settings")["cases"] if c["id"] == "chk-screen")["text"] == before,
      "the case keeps its text")
r = sw("case", "settings", "stuck", "-", expect_ok=False)
check("placeholder" in json.dumps(r), "a dash is refused")
r = sw("case", "settings", "stuck", "OK")
check(any(c["id"] == "stuck" and c["text"] == "OK" for c in feature("settings")["cases"]),
      "two letters are a text (the rule is about placeholders, not length)")

# --- 4. task list --------------------------------------------------------------------------------------------------
sw("task", "add", "later", "Come back for the chest", "--after-hours", "5")
r = sw("task", "list")
check([t["id"] for t in r["open"]] == ["look-shop"] and [t["id"] for t in r["waiting"]] == ["later"]
      and r["waiting"][0].get("not_before"),
      f"task list gives the open and the waiting tasks: {[t['id'] for t in r['open']]} / {[t['id'] for t in r['waiting']]}")
r = sw("task", "list", "--game", G, device=False)
check(r["game"] == G and [t["id"] for t in r["open"]] == ["look-shop"], "task list --game works outside a session")

# --- 5. the wait's dim warning says whether touch protection is up --------------------------------------------------
up, down = swm.dim_warning(True), swm.dim_warning(False)
check("refused" in up and "end --status blocked" in up and "harmless" not in up,
      "with touch protection up the wait says taps are refused and how to end, not to tap")
check("harmless" in down and "touch protection" in down, "without it the wait still says to tap, and what idling brings")

sw("end", "--status", "ok", "--summary", "procfix 1006")
print("done")
