"""The lab: which mechanics need work, one lab per game, level frames, the method set without a session."""
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
off = "com.crypt.gram.puzz"  # in games.yaml, not played on this machine (or off)
r = sw("lab-check", off, device=False)
check(r["game"] == off and r["needed"] == [], "the lab and the review work on a game this machine does not play")
r = sw("start", off, expect_ok=False)
check("is off on this machine" in json.dumps(r), "but a session of it is refused")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
