"""Process fixes of the 2026-10-04 dream (chrono): a wait run beside other commands reloads the session, a level with
no move is no level record, `level end won` takes the frame it asks for, a case is closed only with an observation,
a mark without --feature is kept, a point that opened the store is not tapped again, a window titled
"Panel:<package>/…" is the game, adb's transient resets are retried, a handoff under a mastered mechanic stands."""
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

T = TMP / "pf1004"
shutil.rmtree(T, ignore_errors=True)
T.mkdir()
G = "com.king.candycrushsaga"
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
dspec = importlib.util.spec_from_file_location("device", ROOT / "harness" / "device.py")
dvm = importlib.util.module_from_spec(dspec)
dspec.loader.exec_module(dvm)


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
            if v is None:
                s.pop(k, None)
            else:
                s[k] = v
        SESS.write_text(json.dumps(s), encoding="utf-8")
    return s


def steps(sid):
    return [json.loads(x) for x in (T / "raw" / G / sid / "steps.jsonl").read_text(encoding="utf-8").splitlines()]


def ops(kind="level"):
    p = T / "state" / G / "research.jsonl"
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if json.loads(x).get("op") == kind]


# --- 1. the focused window "Panel:<package>/…" (parse_focus) ---------------------------------------------------
KING = "com.king.candycrushsaga"
dump = (f"  mCurrentFocus=Window{{a1b2c3d u0 Panel:{KING}/{KING}.CandyCrushSagaActivity}}\n"
        f"  mFocusedApp=ActivityRecord{{1 u0 {KING}/.CandyCrushSagaActivity t5}}\n")
check(swm.parse_focus(dump) == (KING, "Panel"),
      f"a window named Panel:<package>/activity: the app is the package, the window its title: {swm.parse_focus(dump)}")
plain = f"  mCurrentFocus=Window{{e4f5a6b u0 {KING}/{KING}.CandyCrushSagaActivity}}\n"
check(swm.parse_focus(plain) == (KING, f"{KING}/{KING}.CandyCrushSagaActivity"), "a plain activity window: as before")

# --- 2. adb's transient resets: one retry on a fresh connection ---------------------------------------------
made = []


class Flaky:
    def __init__(self, fail_first: bool):
        self.calls, self.fail_first = 0, fail_first

    def click(self, x, y):
        self.calls += 1
        if self.fail_first and self.calls == 1:
            raise ConnectionResetError(10054, "An existing connection was forcibly closed by the remote host")
        return ("clicked", x, y)

    def shell(self, cmd):
        raise RuntimeError("device offline")

    width = 1080


def make():
    made.append(Flaky(fail_first=len(made) == 0))
    return made[-1]


dvm.time.sleep = lambda s: None  # the retry waits a second; not in a test
dev = dvm.Retrying(make)
check(dev.click(1, 2) == ("clicked", 1, 2) and len(made) == 2 and dev.reconnects == 1 and dev.width == 1080,
      "a ConnectionResetError in a call: a fresh connection, the call made once more, attributes pass through")
check(dev.click(3, 4) == ("clicked", 3, 4) and len(made) == 2, "the next call runs on the new connection, no reconnect")
try:
    dev.shell("echo")
    other = False
except RuntimeError:
    other = True
check(other and len(made) == 2, "any other error comes through as it is, no retry")
check(ConnectionResetError in dvm.TRANSIENT and OSError not in dvm.TRANSIENT, "TRANSIENT names the reset errors only")

# --- 3. a handoff under a mechanic that was mastered already stands: see test_handoff.py ---------------------

# --- 4. in a session: wait beside other commands, void levels, the win frame, cases, marks, store taps -------
sid = sw("start", G)["session"]

# a wait that ends after other commands ran: the session is reloaded, nothing numbered twice, no frame overwritten
bg = subprocess.Popen([sys.executable, str(ROOT / "harness" / "sw.py"), "-d", "fake1", "wait", "7", "--why", "beside taps"],
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", env=ENV, cwd=ROOT)
time.sleep(1.5)
sw("tap", "100", "100", "--why", "first tap while waiting")
sw("tap", "200", "200", "--why", "second tap while waiting")
outp, err = bg.communicate(timeout=60)
check(bg.returncode == 0, "the wait beside taps ends well" + ("" if bg.returncode == 0 else f": {outp[-300:]} {err[-300:]}"))
w = json.loads(outp)
st = steps(sid)
shots = [x["shot"] for x in st if x["type"] in ("shot", "tap", "wait")]
wait_step = next(x for x in st if x["type"] == "wait")
check(w.get("ran_meanwhile", 0) >= 1 and any("one command at a time" in x for x in w.get("warnings", [])),
      f"the reply says other commands ran meanwhile: ran_meanwhile={w.get('ran_meanwhile')}")
check(len(shots) == len(set(shots)) and wait_step["shot"] == max(shots) and wait_step.get("ran_meanwhile", 0) >= 1,
      f"no frame number twice: the wait took the frame after the taps' ones: {shots}")
check(session()["step"] == 2 and session()["shots"] == max(shots),
      f"the session keeps the taps' counters, not the wait's stale copy: step {session()['step']}, shots {session()['shots']}")
for p in sorted((T / "raw" / G / sid / "shots").glob("0000?.jpg")):
    pass
check(len(list((T / "raw" / G / sid / "shots").glob("*_m.jpg"))) == max(shots), "every frame is on disk once")

# a level opened and never played: no quit record, a level_void step
sw("level", "start", "level 9", "--mechanic", "match", "--plan", "look only", "--value", "9")
r = sw("level", "end", "quit", "--note", "opened to look at the HUD")
check(r["result"] == "void" and not any(o.get("name") == "level 9" for o in ops())
      and steps(sid)[-1]["type"] == "level_void" and steps(sid)[-1]["name"] == "level 9",
      f"level end quit with no move: result void, no level op, a level_void step: {r}")
check(session().get("level") is None, "the void level is closed")
sw("level", "start", "level 9", "--mechanic", "match", "--plan", "play", "--value", "9")
sw("taps", "100,100", "--why", "a move")
r = sw("level", "end", "quit", "--note", "left after one move")
check(r["result"] == "quit" and ops()[-1]["name"] == "level 9" and ops()[-1]["result"] == "quit",
      "level end quit after a move: the quit is recorded, as before")

# `level end won` right after a move: the refusal takes the frame; the next `level end won` goes through
sw("level", "start", "level 10", "--mechanic", "match", "--plan", "play", "--value", "10")
sw("taps", "100,100 200,200", "--why", "moves")
n_shots = session()["shots"]
session(fake_i=session().get("fake_i", 0) + 1)  # the screen moves on after the move (2026-10-06: an unchanged one is accepted)
r = run("level", "end", "won", "--note", "solved")
rep = json.loads(r.stdout)
check(r.returncode == 2 and "frame was taken now" in rep["error"] and rep.get("shot_n") == n_shots + 1
      and steps(sid)[-2]["type"] == "shot" and steps(sid)[-1]["type"] == "error",
      f"the win refusal takes the frame and returns it: {rep.get('error')} shot_n={rep.get('shot_n')}")
r = sw("level", "end", "won", "--note", "solved, the frame shows the win")
check(r["result"] == "won" and ops()[-1]["result"] == "won" and ops()[-1]["shot"] == n_shots + 1,
      "level end won after the refusal's frame: recorded with that frame, no separate shot call")
session(last_app="com.android.vending")
sw("level", "start", "level 11", "--mechanic", "match", "--plan", "play", "--value", "11")
sw("taps", "100,100", "--why", "a move")
session(last_app="com.android.vending", looked=False)
r = run("level", "end", "won", "--note", "x")
check(r.returncode == 2 and "not the game" in r.stdout and "frame was taken now" not in r.stdout,
      "with the store in front the refusal still says launch first, no frame is taken")
session(last_app=G)
sw("level", "end", "quit", "--note", "x")

# a case is closed only with what was seen; a new case needs its text
sw("feature", "boosters", "Boosters", "--type", "currency-booster", "--appeared", "on the level HUD from the first level")
r = run("case", "boosters", "list")
check(r.returncode == 2 and "needs its text" in r.stdout and "sw.py research" in r.stdout,
      f"`case <feature> list` is refused: no empty case named list: {r.stdout[:120]}")
f = sw("research", G, device=False)
check("list" not in f, "no case 'list' in the map")
for text in ("Not verified this session; see booster-refill task", "Not tested (would need spending all units)",
             "Not reached this session (2 left)", "Open: never at 0", "unverified", "not yet seen"):
    r = run("case", "boosters", "chk-refill", text, "--done")
    check(r.returncode == 2 and "closed with what the frames showed" in r.stdout, f"case --done {text[:22]!r}: refused")
r = sw("case", "boosters", "chk-refill", "No refill seen in 3 levels: the count only goes down with use", "--done")
check(any(c["id"] == "chk-refill" and c.get("done") for c in r["feature"]["cases"]), "an observation closes the case")
r = sw("case", "boosters", "chk-empty", "Does not apply: boosters have no empty state, the badge shows AD at 0", "--done")
check(any(c["id"] == "chk-empty" and c.get("done") for c in r["feature"]["cases"]), "'Does not apply: …' closes it")
r = sw("case", "boosters", "chk-sinks", "One unit per use; leaving mid-way not tested", "--done")
check(any(c["id"] == "chk-sinks" and c.get("done") for c in r["feature"]["cases"]),
      "a partial observation ('…; leaving mid-way not tested') is an observation")
r = sw("case", "boosters", "chk-sources", "--done", expect_ok=False)
check(isinstance(r, dict) and r.get("ok") is True, "a known case closed without a text: as before")
r = sw("case", "boosters", "refill-timer", "Does a timer refill the boosters?")
check(any(c["id"] == "refill-timer" for c in r["feature"]["cases"]), "a new case with its text: as before")

# a mark with --as and no --feature is kept, the reply says what is missing
sw("shot")
r = sw("mark", "Title screen", "Play, Retrieve My Progress, settings gear", "--as", "screen")
m = steps(sid)[-1]
check(r["ok"] and any("needs --feature" in x and "the mark is kept" in x for x in r.get("warnings", []))
      and m["type"] == "mark" and "feature" not in m and "role" not in m and m["title"] == "Title screen",
      f"mark --as without --feature: kept without a page, a warning instead of a refusal: {r.get('warnings')}")
r = sw("mark", "Boosters row", "the three boosters", "--feature", "boosters", "--as", "screen")
check(steps(sid)[-1].get("feature") == "boosters" and steps(sid)[-1].get("role") == "screen", "with --feature: as before")

# a tap that opened the Play Store is not sent again at that point
session(fake_app="com.android.vending")
r = sw("tap", "45", "108", "--why", "skip the interstitial")
check(r["app"] == "com.android.vending" and any("opened the Play Store" in x for x in r.get("warnings", []))
      and session().get("store_taps") and session()["store_taps"][-1]["step"] == session()["step"],
      f"a tap that put the store in front is remembered: {session().get('store_taps')}")
session(fake_app=None)
sw("launch")
r = run("tap", "47", "110", "--why", "skip again")
check(r.returncode == 5 and "opened the Play Store at step" in r.stdout and steps(sid)[-1]["type"] == "error"
      and steps(sid)[-1].get("store_tap"), f"the same point again: refused with exit 5, an error step: {r.stdout[:100]}")
r = sw("tap", "47", "110", "--why", "the frame shows a real X here", "--force")
check(r.get("shot_n"), "--force sends it")
r = sw("tap", "600", "1200", "--why", "elsewhere")
check(r.get("shot_n") and not any("opened the Play Store at step" in x for x in r.get("warnings", [])),
      "a tap elsewhere is free")

# the session ends on a level with no move: a level_void step, no quit record
sw("level", "start", "level 12", "--mechanic", "match", "--plan", "x", "--value", "12")
before = len(ops())
sw("end", "--status", "blocked", "--summary", "the phone was lost before the first tap")
st = steps(sid)
check(len(ops()) == before and any(x["type"] == "level_void" and x["name"] == "level 12" for x in st)
      and st[-1]["type"] == "end", "a level open at the end with no move: void, no quit record")
meta = json.loads((T / "raw" / G / sid / "session.json").read_text(encoding="utf-8"))
check(meta["levels"]["won"] == 1 and meta["levels"]["lost"] == 0 and "level 12" not in [o.get("name") for o in ops()],
      f"session.json counts the played levels only: {meta['levels']}")
fr = sw("level-frames", G, "match", device=False)
check(len(fr["start_frames"]) == 3,
      f"level-frames: the void levels have no span (one quit after a move, one won, one quit on 11): {len(fr['start_frames'])}")
print("done")
