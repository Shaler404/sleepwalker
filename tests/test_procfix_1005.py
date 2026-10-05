"""Process fixes of the 2026-10-05 dream (chrono): a task id with dots is closed as typed and an unknown one is
refused instead of becoming a stray; `--board` takes the JSON itself; `level end won --shot N` names the frame that
showed the win after the win screen was left; the solver's time-budget stop is said once a level."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP, frames_dir  # noqa: E402
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

import yaml

T = TMP / "pf1005"
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


def ops(kind):
    p = T / "state" / G / "research.jsonl"
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if json.loads(x).get("op") == kind]


def tasks():
    return {t["id"]: t for t in yaml.safe_load(sw("research", G, device=False))["tasks"]}


sid = sw("start", G)["session"]

# --- 1. a task id with dots: closed as typed, no stray; an unknown id is refused -------------------------------
# the planner writes update tasks with the version in the id, dots included
(T / "state" / G).mkdir(parents=True, exist_ok=True)
with open(T / "state" / G / "research.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps({"t": time.time() - 60, "session": "planner", "op": "task", "id": "update-241.5.2",
                        "title": "Recheck the features on version 241.5.2", "kind": "update", "version": "241.5.2",
                        "requires": "any", "source": "external"}) + "\n")
check(tasks()["update-241.5.2"]["status"] == "open", "the planner's dotted update task is open")
r = sw("task", "done", "update-241.5.2", "--note", "phone already on 241.5.2, map unchanged")
check(r["task"]["id"] == "update-241.5.2" and r["task"]["status"] == "done",
      f"task done on a dotted id closes that task: {r['task']['id']} {r['task']['status']}")
check("update-241-5-2" not in tasks(), "no stray slugged task was made")
check(ops("task_done")[-1]["id"] == "update-241.5.2", "the journal op carries the id as typed")
sw("task", "add", "look-at-shop", "Look at the shop")
r = sw("task", "done", "Look at Shop", "--note", "seen")
check(r["task"]["id"] == "look-at-shop" and r["task"]["status"] == "done", "a title-like id still resolves by its slug")
r = sw("task", "done", "update-241.5.3", "--note", "x", expect_ok=False)
check("no task" in json.dumps(r) and "update-241.5.2" in json.dumps(r) and "update-241.5.3" not in tasks(),
      f"an id the map does not have is refused with the nearest ids, no stray task: {json.dumps(r)[:200]}")
r = sw("task", "cancel", "analyze", "--reason", "x")
check(r["task"]["id"] == "analyze" and r["task"]["status"] == "cancelled",
      "task cancel on a task that does not exist yet stays allowed (it keeps the planner from making it)")
with open(T / "state" / G / "research.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps({"t": time.time() - 30, "session": "planner", "op": "task", "id": "update-242.0.1",
                        "title": "Recheck the features on version 242.0.1", "kind": "update", "version": "242.0.1",
                        "requires": "any", "source": "external"}) + "\n")
r = sw("task", "cancel", "update-242.0.1", "--reason", "duplicate")
check(r["task"]["id"] == "update-242.0.1" and r["task"]["status"] == "cancelled" and "update-242-0-1" not in tasks(),
      "task cancel on a dotted id cancels that task, no stray")

# --- 2. --board takes the JSON itself -----------------------------------------------------------------------------
sd = T / "state" / G / "solvers"
sd.mkdir(parents=True, exist_ok=True)
(sd / "modes.py").write_text("def solve(image, board=None, frame_scale=1.0):\n"
                             "    return {'moves': [[5, 5]], 'note': f\"mode {(board or {}).get('mode')}\"}\n",
                             encoding="utf-8")
r = sw("solve", "modes", "--board", '{"mode":"score"}')
check(r["note"] == "mode score", f"--board with inline JSON reaches the solver as a board: {r.get('note')}")
r = sw("solve", "modes", "--board", '{"mode":', expect_ok=False)
check("does not parse" in json.dumps(r), "--board with broken JSON says so")
r = sw("solve", "modes", "--board", "nosuch.json", expect_ok=False)
check("no such file" in json.dumps(r) and "JSON itself" in json.dumps(r), "--board with a missing file still says so")
(T / "b.json").write_text('{"mode":"gameover"}', encoding="utf-8")
r = sw("solve", "modes", "--board", str(T / "b.json"))
check(r["note"] == "mode gameover", "--board with a file path works as before")

# --- 3. level end won --shot N: the frame that showed the win, after leaving the win screen -----------------------
sw("level", "start", "level 1", "--mechanic", "pins", "--plan", "x", "--value", "1")
first = session()["level"]["shot0"]
sw("taps", "10,10 20,20", "--why", "pins")
r = sw("level", "end", "won", "--note", "x", expect_ok=False)
check("--shot N" in json.dumps(r) and r.get("shot_n"), f"the refusal takes the frame and names --shot as the way out: {r.get('shot_n')}")
win_shot = r["shot_n"]
sw("key", "back", "--why", "leave the win screen")  # resets the look: the second claim used to be refused again
r = sw("level", "end", "won", "--note", "x", expect_ok=False)
check("take a frame" in json.dumps(r) and "--shot N" in json.dumps(r), "after Back the plain claim is refused again, with the hint")
r = sw("level", "end", "won", "--note", "x", "--shot", str(win_shot))
op = ops("level")[-1]
check(r["result"] == "won" and op["shot"] == win_shot and op.get("shot_named") is True,
      f"--shot N records the win on the named frame: {op.get('shot')} named {op.get('shot_named')}")
sw("level", "start", "level 2", "--mechanic", "pins", "--plan", "x", "--value", "2")
sw("taps", "10,10", "--why", "pins")
last = session()["last_shot"]
r = sw("level", "end", "won", "--note", "x", "--shot", str(first), expect_ok=False)
check("not a frame of this level" in json.dumps(r), "a frame from before the level is refused")
r = sw("level", "end", "won", "--note", "x", "--shot", str(last + 5), expect_ok=False)
check("not a frame of this level" in json.dumps(r), "a frame that does not exist is refused")
r = sw("level", "end", "lost", "--note", "x", "--shot", str(last), expect_ok=False)
check("level end won --shot" in json.dumps(r), "--shot is for wins")
sw("shot")
sw("level", "end", "won", "--note", "x")
check(ops("level")[-1]["shot"] == session()["last_shot"] and "shot_named" not in ops("level")[-1],
      "without --shot the record keeps the last frame, as before")

# --- 4. the solver's time-budget stop is said once a level -----------------------------------------------------
(sd / "rounds.py").write_text('''
def solve(image, board=None, frame_scale=1.0, state=None):
    n = (state or {}).get("n", 0) + 1  # differs per round, whatever the frame
    return {"moves": [[100 + 10 * n, 300], [500, 700]], "note": "look again", "rescan": True, "state": {"n": n}}
''', encoding="utf-8")
sw("level", "start", "level 3", "--mechanic", "pins", "--plan", "x", "--value", "3")
s = session()
s["level"]["t0"] -= 3600  # an hour in: far over the budget
session(level=s["level"])
r = sw("solve", "rounds", "--run", "--rounds", "3")
check(r["rounds"] == 1 and "time budget" in r["stopped"] and "said once" in r["stopped"],
      f"over the budget: the first run stops after one round and says it is said once: {r['stopped']}")
r = sw("solve", "rounds", "--run", "--rounds", "3")
check(r["rounds"] == 3 and "time budget" not in r["stopped"],
      f"the next run in the same level plays its rounds: {r['rounds']} rounds, {r['stopped']}")
sw("shot")
sw("level", "end", "lost", "--note", "x")
sw("level", "start", "level 4", "--mechanic", "pins", "--plan", "x", "--value", "4")
s = session()
s["level"]["t0"] -= 3600
session(level=s["level"])
r = sw("solve", "rounds", "--run", "--rounds", "3")
check(r["rounds"] == 1 and "time budget" in r["stopped"], "a new level gets its own budget stop")
sw("shot")
sw("level", "end", "quit", "--note", "x")
sw("end", "--status", "ok", "--summary", "procfix 1005")
print("done")
