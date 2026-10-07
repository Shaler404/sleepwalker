"""Process fixes of the 2026-10-07 dream (chrono): the local playbook and solver are reconciled with the merged copy
by content (a base sidecar, a three-way merge, an .incoming copy on a conflict), never by file time; `solve --run`
ends a phone loss as a refusal with its solve_end step; `Retrying` waits for a phone that dropped off USB;
`level end lost --shot N`; local.yaml privacy.names (texts refused, the snapshot redacted); "Open (video): ..." is a
button, not the status word "open"."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP, frames_dir  # noqa: E402
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

T = TMP / "pf1007"
shutil.rmtree(T, ignore_errors=True)
T.mkdir()
G = "com.oakever.meowdoku"
LOCAL = T / "local.yaml"


def write_local(names=""):
    LOCAL.write_text(f"""machine: testbox
games: [{G}]
android: {{serials: [nophone]}}
fake_devices: {{fake1: "{frames_dir().as_posix()}"}}
video: {{record: false}}
state_dir: "{(T / 'state').as_posix()}"
raw_dir: "{(T / 'raw').as_posix()}"
wiki_dir: "{(T / 'gwiki').as_posix()}"
privacy: {{names: [{names}]}}
""", encoding="utf-8")


write_local()
ENV = {**os.environ, "SW_LOCAL": str(LOCAL), "PYTHONIOENCODING": "utf-8"}
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
            s[k] = v
        SESS.write_text(json.dumps(s), encoding="utf-8")
    return s


def ops(kind):
    p = T / "state" / G / "research.jsonl"
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if json.loads(x).get("op") == kind]


def steps():
    return [json.loads(x) for x in (Path(session()["dir"]) / "steps.jsonl").read_text(encoding="utf-8").splitlines()]


def older(p: Path, s: float = 3600):
    os.utime(p, (time.time() - s, time.time() - s))


# --- 1. the local copy against the merged one: content, not file time ---------------------------------------------
D = T / "rc"
local, merged = D / "state" / "playbook.md", D / "wiki" / "playbook.md"
merged.parent.mkdir(parents=True)
merged.write_text("# How to play\n\n## queens\n- one cat per row\n", encoding="utf-8")
check(swm.reconcile_copy(local, merged, "playbook") == "taken" and local.read_text(encoding="utf-8") == merged.read_text(encoding="utf-8")
      and (D / "state" / "playbook.base.md").read_text(encoding="utf-8") == merged.read_text(encoding="utf-8"),
      "no local copy: the merged one is taken and recorded as the base")
local.write_text(local.read_text(encoding="utf-8") + "- lab 2026-10-06: a column rule\n", encoding="utf-8")
older(local)  # the lab wrote it an hour ago
merged.write_text(merged.read_text(encoding="utf-8"), encoding="utf-8")  # a git pull: the same content, written now
check(merged.stat().st_mtime > local.stat().st_mtime, "the pulled merged file is newer than the local work (the old rule's trigger)")
check(swm.reconcile_copy(local, merged, "playbook") is None and "column rule" in local.read_text(encoding="utf-8")
      and not (D / "state" / "playbook.prev.md").exists(),
      "a pulled merged file with nothing new does not replace the local work (it did, by file time: 2026-10-06 18:47 and the 2026-10-07 sync)")
merged.write_text("# How to play (dream edit)\n\n## queens\n- one cat per row\n", encoding="utf-8")
r = swm.reconcile_copy(local, merged, "playbook")
text = local.read_text(encoding="utf-8")
check(r == "merged" and text.startswith("# How to play (dream edit)") and "column rule" in text
      and (D / "state" / "playbook.prev.md").exists() and not (D / "state" / "playbook.incoming.md").exists(),
      "a merged edit elsewhere in the file and the local work: merged three ways, the old local copy kept as .prev")
check((D / "state" / "playbook.base.md").read_text(encoding="utf-8") == merged.read_text(encoding="utf-8"),
      "the base is the merged version just reconciled")
check(swm.reconcile_copy(local, merged, "playbook") is None and local.read_text(encoding="utf-8") == text,
      "a second call changes nothing")
# both sides changed the same lines: the local copy stays, the merged one waits as .incoming
local.write_text(text.replace("one cat per row", "one cat per row and column"), encoding="utf-8")
merged.write_text(merged.read_text(encoding="utf-8").replace("one cat per row", "one cat per row, none adjacent"), encoding="utf-8")
r = swm.reconcile_copy(local, merged, "playbook")
check(r == "incoming" and "row and column" in local.read_text(encoding="utf-8")
      and "none adjacent" in (D / "state" / "playbook.incoming.md").read_text(encoding="utf-8"),
      "a conflict: the local copy is untouched, the merged one waits as playbook.incoming.md")
check(swm.reconcile_copy(local, merged, "playbook") == "incoming", "the conflict is reported again while the .incoming file exists")
(D / "state" / "playbook.incoming.md").unlink()
check(swm.reconcile_copy(local, merged, "playbook") is None, "the .incoming file deleted (merged by hand): silence")
local.write_text(merged.read_text(encoding="utf-8"), encoding="utf-8")
older(local)
check(swm.reconcile_copy(local, merged, "playbook") is None, "a local copy equal to the merged one: nothing to do")
merged.write_text(merged.read_text(encoding="utf-8") + "- a later merged line\n", encoding="utf-8")
check(swm.reconcile_copy(local, merged, "playbook") == "taken" and "later merged line" in local.read_text(encoding="utf-8"),
      "a local copy untouched since the last take is replaced by the newer merged one")
# no base yet (the first run after this rule): the template counts as untouched, anything else is not overwritten
(D / "state" / "playbook.base.md").unlink()
local.write_text("# template\n", encoding="utf-8")
check(swm.reconcile_copy(local, merged, "playbook", template="# template\n") == "taken", "no base: the untouched template is replaced")
(D / "state" / "playbook.base.md").unlink()
local.write_text("# the lab's own text\n", encoding="utf-8")
older(local)
check(swm.reconcile_copy(local, merged, "playbook", template="# template\n") == "incoming" and "lab's own" in local.read_text(encoding="utf-8"),
      "no base and a local copy of unknown origin: kept, the merged one waits as .incoming")
check(swm.committed_versions(merged) == [], "a file outside the repository has no committed versions")
# a solver: the three-way result must compile, else it waits as .incoming
sl, sm = D / "state" / "solvers" / "m.py", D / "solvers" / "m.py"
sm.parent.mkdir(parents=True)
sm.write_text("def solve(image, board=None, frame_scale=1.0):\n    return {'moves': []}\n", encoding="utf-8")
swm.reconcile_copy(sl, sm, "solver")
sl.write_text("def solve(image, board=None, frame_scale=1.0):\n    return {'moves': []}\n\n\ndef helper():\n    return 1\n", encoding="utf-8")
sm.write_text("import re\n\n\ndef solve(image, board=None, frame_scale=1.0):\n    return {'moves': []}\n", encoding="utf-8")
check(swm.reconcile_copy(sl, sm, "solver") == "merged" and "import re" in sl.read_text(encoding="utf-8") and "helper" in sl.read_text(encoding="utf-8"),
      "a solver: the lab's function and the merged import are merged three ways")
sl.write_text(sl.read_text(encoding="utf-8") + "def solve2(:\n", encoding="utf-8")  # the local copy does not compile
sm.write_text(sm.read_text(encoding="utf-8") + "\n\ndef other():\n    return 2\n", encoding="utf-8")
r = swm.reconcile_copy(sl, sm, "solver")
check(r == "incoming" and "solve2(:" in sl.read_text(encoding="utf-8") and (D / "state" / "solvers" / "m.incoming.py").exists(),
      "a three-way result that does not compile is not written: the merged copy waits as .incoming")

# in a session: the warning about an .incoming copy comes with start, level start, solve and playbook
(T / "gwiki" / G / "agent").mkdir(parents=True, exist_ok=True)
(T / "gwiki" / G / "agent" / "playbook.md").write_text("# How to play: Meowdoku\n\n## queens\n- one cat per row\n", encoding="utf-8")
sid = sw("start", G)["session"]
pb = T / "state" / G / "playbook.md"
check(pb.read_text(encoding="utf-8").startswith("# How to play: Meowdoku") and (T / "state" / G / "playbook.base.md").exists(),
      "start: the local playbook starts from the merged one, with its base")
pb.write_text(pb.read_text(encoding="utf-8").replace("per row", "per row (local)"), encoding="utf-8")
(T / "gwiki" / G / "agent" / "playbook.md").write_text("# How to play: Meowdoku\n\n## queens\n- one cat per row (merged)\n", encoding="utf-8")
sw("end", "--status", "ok", "--summary", "x")
r = sw("start", G)
check(any("playbook.incoming.md" in w for w in r.get("warnings", [])) and "(local)" in pb.read_text(encoding="utf-8"),
      "start warns about the merged playbook that waits as .incoming; the local edit stands")
r = sw("level", "start", "level 1", "--mechanic", "queens", "--plan", "x", "--value", "1")
check(any("playbook.incoming.md" in w for w in r.get("warnings", [])), "level start carries the warning too")
out = run("playbook", "--game", G, device=False).stdout
check("WARNING" in out and "playbook.incoming.md" in out, "sw.py playbook prints the warning before the text")
(T / "state" / G / "playbook.incoming.md").unlink()
sw("level", "end", "quit", "--note", "x")
r = sw("level", "start", "level 1", "--mechanic", "queens", "--plan", "x", "--value", "1")
check(not r.get("warnings"), "the .incoming file deleted: no warning")
sw("level", "end", "quit", "--note", "x")

# --- 2. level end lost --shot N -----------------------------------------------------------------------------------
sw("level", "start", "level 2", "--mechanic", "queens", "--plan", "x", "--value", "2")
sw("taps", "10,10 20,20", "--why", "cats")
over = session()["last_shot"]
sw("key", "back", "--why", "leave the game-over screen")
r = sw("level", "end", "lost", "--shot", str(over), "--note", "game over, the frame before Back")
op = ops("level")[-1]
check(r["result"] == "lost" and op["shot"] == over and op.get("shot_named"), f"level end lost --shot {over}: recorded on that frame")
sw("level", "start", "level 3", "--mechanic", "queens", "--plan", "x", "--value", "3")
sw("taps", "10,10", "--why", "cats")
r = sw("level", "end", "quit", "--shot", str(session()["last_shot"]), "--note", "x", expect_ok=False)
check("won|lost --shot N" in json.dumps(r), "a quit names no frame: refused with both uses")
sw("level", "end", "quit", "--note", "x")

# --- 3. solve --run with the phone lost mid-round: a refusal with its steps, not a traceback ------------------------
sd = T / "state" / G / "solvers"
sd.mkdir(parents=True, exist_ok=True)
(sd / "dropper.py").write_text("def solve(image, board=None, frame_scale=1.0):\n    return {'moves': [[50, 50]], 'note': 'one'}\n",
                               encoding="utf-8")


class Dropping(swm.FakeDevice):
    def tap(self, *a, **k):
        raise RuntimeError("device 'fake1' not found")


swm.open_device = lambda cur, prepare=False: Dropping(cur)
sw("level", "start", "level 4", "--mechanic", "dropper", "--plan", "x", "--value", "4")
args = swm.parser().parse_args(["-d", "fake1", "solve", "dropper", "--run", "--rounds", "3"])
swm.tidy_args(args)
try:
    swm.cmd_solve(args)
    code = 0
except SystemExit as ex:
    code = ex.code
last = steps()[-2:]
check(code == 3 and last[0]["type"] == "solve_end" and "phone lost in round 1" in last[0]["stopped"]
      and last[1]["type"] == "error" and last[1]["code"] == 3 and "not found" in last[1]["text"] and last[1].get("rounds") == 1,
      f"a phone lost in a round: exit 3, the solve_end step and the error step with the round: {last[0].get('stopped')}")
check(session().get("blocked_reason") and session()["level"]["name"] == "level 4",
      "the session says why and the level stays open for the player to close")
sw("level", "end", "quit", "--note", "x")
sw("end", "--status", "blocked", "--summary", "x")

# --- 4. Retrying waits for a phone that dropped off USB -----------------------------------------------------------
made, present = [], {"back_after": 0, "polls": 0}


class Flaky:
    def __init__(self, fail_first):
        self.fail_first = fail_first

    def click(self, x, y):
        if self.fail_first:
            self.fail_first = False
            raise RuntimeError("device 'R5GL72FYKPJ' not found")
        return ("clicked", x, y)


def make():
    made.append(Flaky(fail_first=len(made) == 0))
    return made[-1]


def is_present():
    present["polls"] += 1
    return present["polls"] > present["back_after"]


dvm.time.sleep = lambda s: None
present["back_after"] = 3
dev = dvm.Retrying(make, present=is_present, reconnect_s=30)
check(dev.click(1, 2) == ("clicked", 1, 2) and dev.reconnects == 1 and present["polls"] == 4 and len(made) == 2,
      "'device not found': the device is polled until it is back, then a fresh connection and the call once more")
made.clear()
present.update(back_after=10 ** 6, polls=0)
dev = dvm.Retrying(make, present=is_present, reconnect_s=5)
try:
    dev.click(1, 2)
    gone = False
except RuntimeError as ex:
    gone = "not found" in str(ex)
check(gone and len(made) == 1 and dev.waited_s >= 5, "a device that does not come back within reconnect_s: the error comes through")
made.clear()


class Other:
    def click(self, x, y):
        raise RuntimeError("something else")


dev = dvm.Retrying(lambda: Other(), present=lambda: True)
try:
    dev.click(1, 2)
    other = False
except RuntimeError:
    other = True
check(other and dev.reconnects == 0, "any other error comes through at once")
check(dvm.device_gone(RuntimeError("AdbConnectionError: connect to adb server failed: [WinError 10061]")),
      "the adb server gone counts as the device gone")

# --- 5. privacy.names: the texts are refused, the snapshot is redacted -------------------------------------------
sid = sw("start", G)["session"]
sw("feature", "profile", "Profile", "--type", "system", "--appeared", "on the home screen")
sw("case", "profile", "chk-screen", "the card shows the name 8W2G1Y and 17 hearts", "--done")  # the name is not listed yet
write_local('8W2G1Y, "Amaze-JtL"')
r = sw("case", "profile", "chk-name", "the name 8W2G1Y is auto-assigned", "--done", expect_ok=False)
check("player's name or id" in json.dumps(r) and "[auto-assigned id]" in json.dumps(r), "a case text with a listed name is refused")
r = sw("case", "profile", "chk-name", "the name is auto-assigned ([auto-assigned id]); 8W2G1Yx is not the name", "--done")
check(r.get("ok", True) is not False and "error" not in r, "the redacted wording passes; a longer word is not the name")
r = sw("task", "add", "league-amaze", "Watch Amaze-JtL climb the league", "--kind", "followup", expect_ok=False)
check("Amaze-JtL" in json.dumps(r) and "privacy.names" in json.dumps(r), "a task title with a listed name is refused")
r = sw("mark", "League", "the row of Amaze-JtL in the league", "--as", "screen", expect_ok=False)
check("player's name or id" in json.dumps(r), "a mark description with a listed name is refused")
snap = T / "snap" / "research.yaml"
sw("snapshot", G, str(snap), "--until", "2099-01-01T00:00:00", device=False)
text = snap.read_text(encoding="utf-8")
check(not re.search(r"(?<![\w-])8W2G1Y(?![\w-])", text) and "[auto-assigned id] and 17 hearts" in text and "8W2G1Yx" in text,
      "the snapshot writes [auto-assigned id] for a listed name written before it was listed")

# --- 6. "Open (video): ..." is a button, not the status word "open" -----------------------------------------------
sw("feature", "post-win-gift", "Post-win gift", "--type", "system", "--appeared", "after a win")
r = sw("case", "post-win-gift", "open-video", "Open (video): about 60 s rewarded video, 'Reward granted' X returns to the meter", "--done")
check("error" not in r, "a case text that starts with the button 'Open (video):' is accepted")
r = sw("case", "post-win-gift", "open-never", "Open: never at 0", "--done", expect_ok=False)
check("leave the case open" in json.dumps(r), "'Open:' as a status word is still refused")
sw("end", "--status", "ok", "--summary", "x")
print("ALL OK")
