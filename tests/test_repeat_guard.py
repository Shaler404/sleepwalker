"""The same tap or the same solver plan again on a screen it did not change: warned, then held back."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP, frames_dir  # noqa: E402
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

T = TMP / "repeattest"
shutil.rmtree(T, ignore_errors=True)
T.mkdir()
G = "com.maroieqrwlk.unpin"
STILL = T / "still"  # a phone whose screen never changes: every tap misses
STILL.mkdir()
shutil.copy(sorted(frames_dir().glob("*.png"))[0], STILL / "frame.png")
(T / "local.yaml").write_text(f"""machine: testbox
games: [{G}]
android: {{serials: [nophone]}}
fake_devices: {{fake1: "{frames_dir().as_posix()}", still: "{STILL.as_posix()}"}}
video: {{record: false}}
state_dir: "{(T / 'state').as_posix()}"
raw_dir: "{(T / 'raw').as_posix()}"
wiki_dir: "{(T / 'gwiki').as_posix()}"
""", encoding="utf-8")
ENV = {**os.environ, "SW_LOCAL": str(T / "local.yaml"), "PYTHONIOENCODING": "utf-8"}


def run(*a, device="still"):
    return subprocess.run([sys.executable, str(ROOT / "harness" / "sw.py"), *(["-d", device] if device else []), *a],
                          capture_output=True, text=True, encoding="utf-8", env=ENV, cwd=ROOT)


def sw(*a, expect_ok=True, device="still"):
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


def warned(r, text):
    return any(text in w for w in (r.get("warnings") or []))


def steps(sid):
    return [json.loads(x) for x in (T / "raw" / G / sid / "steps.jsonl").read_text(encoding="utf-8").splitlines()]


sid = sw("start", G)["session"]

# taps: the second identical tap with no change warns, the third is refused with exit 5 unless --force
r = sw("tap", "100", "100", "--why", "Level button")
check(r["same_as_prev"] and not warned(r, "same tap twice"), "the first tap that changes nothing: no warning yet")
r = sw("tap", "110", "95", "--why", "Level button again")
check(warned(r, "same tap twice"), "a second tap within 25 px with no change: warned")
r = run("tap", "100", "100", "--why", "and again")
o = json.loads(r.stdout)
check(r.returncode == 5 and "third time" in o["error"] and Path(o["shot"]).exists(),
      "the third is refused with exit 5, and the reply carries the frame to look at")
r = sw("tap", "100", "100", "--why", "sure", "--force")
check(r["shot_n"] > 0, "tap --force goes through")
r = sw("tap", "400", "400", "--why", "another control")
check(not warned(r, "same tap twice"), "a tap elsewhere is a new tap")
sw("tap", "400", "400", "--why", "x")
sw("wait", "0")
r = sw("tap", "400", "400", "--why", "after the timer")
check(not warned(r, "same tap twice"), "a wait in between: time may have made the control work")
sw("taps", "10,10 20,20", "--why", "x")
r = sw("taps", "10,10 20,20", "--why", "x")
check(warned(r, "same tap twice"), "taps: the same batch twice with no change is warned")
r = run("taps", "12,8 20,20", "--why", "x")
check(r.returncode == 5, "and a third time refused")

# a phone where the screen changes: the same point again is fine
sw("end", "--status", "ok", "--summary", "taps")
s2 = sw("start", G, device="fake1")["session"]
for _ in range(3):
    r = sw("tap", "100", "100", "--why", "next card", device="fake1")
check(not warned(r, "same tap twice"), "taps on the same point that change the screen are never held back")
sw("end", "--status", "ok", "--summary", "changing screen", device="fake1")

# solve: the same moves on the same frame are not sent again; a check before a run is the normal flow
sid2 = sw("start", G)["session"]
sd = T / "state" / G / "solvers"
sd.mkdir(parents=True, exist_ok=True)
(sd / "same.py").write_text('''
def solve(image, board=None, frame_scale=1.0, state=None):
    n = (state or {}).get("n", 0) + 1
    return {"moves": [[10, 10], [20, 20]], "note": f"call {n}", "state": {"n": n}}
''', encoding="utf-8")
sw("level", "start", "level 1", "--mechanic", "blocks", "--plan", "x", "--value", "1")
r = sw("solve", "same")
check(r["moves"] == 2 and not warned(r, "do not land"), "a check draws the moves")
r = sw("solve", "same", "--run")
check(r["moves_done"] == 2, "a run after the check plays them (the check sent nothing)")
r = sw("solve", "same", "--run")
st = steps(sid2)[-1]
check(r.get("repeated") is True and r["moves_done"] == 0 and "moves of step" in r["stopped"]
      and Path(r["drawn"]).exists() and st["type"] == "solve" and st["repeated"] and st["n"] == 0,
      f"the same moves on the same frame: not sent, drawn, logged as a repeat: {r['stopped']}")
r = sw("solve", "same")
check(r["note"] == "call 2" and warned(r, "do not land"),
      f"the held-back call kept the solver's memory as it was; a check warns too: {r['note']}")
r = sw("solve", "same", "--run", "--force")
st = steps(sid2)[-1]
check(r["moves_done"] == 2 and st.get("forced") and st.get("repeated"), "--force sends them anyway")
r = sw("level", "end", "lost", "--note", "the piece never landed", "--retry")
r = sw("solve", "same", "--run")
check(r["moves_done"] == 2 and not r.get("repeated"), "a new try of the level (the same board again) starts over")
sw("end", "--status", "ok", "--summary", "solver repeats")

# stats: the loops are visible without reading transcripts
st = sw("stats", G, device=None)
rows = {x["session"]: x for x in st["games"][G]["sessions"]}
meta = json.loads((T / "raw" / G / sid / "session.json").read_text(encoding="utf-8"))
check(rows[sid]["repeated_steps"] == 6 and meta["repeated_steps"] == 6,
      f"taps: four warned (the forced one too) and two refused: {rows[sid]['repeated_steps']}")
check(rows[sid2]["repeated_steps"] == 2 and rows[s2]["repeated_steps"] == 0 and st["games"][G]["repeated_steps"] == 8,
      f"solve: one held back and one forced: {rows[sid2]['repeated_steps']}")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
