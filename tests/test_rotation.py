"""Games take turns on a phone; a game waiting for an update shows up as work for a human."""
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

SP = Path(__file__).resolve().parent
T = TMP / "rottest"
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


def play(expect_game, status="ok"):
    c = sw("claim")["assignments"][0]
    sw("start", c["game"])
    sw("tap", "10", "10", "--why", "x")
    time.sleep(1.1)  # session ids and start times are per second
    sw("end", "--status", status, "--summary", "x")
    return c


c = play(G)
check(c["game"] == G and "rotation" not in c, "1st session: the first game in the list")
c = play(G2)
check(c["game"] == G2 and "turn" in c, f"2nd session: a game never played gets its turn: {c.get('turn')}")
c = play(G)
check(c["game"] == G, "3rd session: back to priority")
c = play(G)
check(c["game"] == G, "4th session: still the first game (max_in_a_row 2)")
c = play(G2)
check(c["game"] == G2 and "unpin had 2 sessions in a row" in c.get("rotation", ""),
      f"5th session: after two in a row the other game goes: {c.get('rotation')}")
c = play(G)
check(c["game"] == G, "6th session: back to the first game (priority)")
c = play(G, status="handoff")
check(c["game"] == G, "7th session: the first game again")
c = sw("claim")["assignments"][0]
check(c["game"] == G and c["model_role"] == "study",
      "a handoff continues the same game even after two sessions in a row")
sw("end", "--status", "ok", "--summary", "release")

# wait-free: nothing busy -> at once; busy -> waits until it frees up
t = time.time()
r = sw("wait-free", "--max-minutes", "1")
check(r["free"] == ["fake1"] and r["busy"] == [] and time.time() - t < 10, "wait-free with nothing busy returns at once")
sw("start", G)
t = time.time()
r = sw("wait-free", "--max-minutes", "0.1")
check(r["busy"] and r["busy"][0]["game"] == G and not r["freed"] and time.time() - t >= 5,
      "wait-free on a busy phone waits, then reports it still busy")
ender = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(4)"])
ender.wait()
subprocess.Popen([sys.executable, str(DEV / "harness" / "sw.py"), "-d", "fake1", "end", "--status", "ok", "--summary", "x"],
                 env=ENV, cwd=DEV, stdout=open(T / "ender.out", "w"), stderr=subprocess.STDOUT)
r = sw("wait-free", "--max-minutes", "1")
check(r["freed"] == ["fake1"] or (not r["busy"] and "fake1" in r["free"]),
      f"wait-free returns when the phone frees up: {r} / ender: {(T / 'ender.out').read_text()[-600:]}")

# a game whose turn it is goes before another game's survey (the task kind no longer outranks turns)
spec0 = importlib.util.spec_from_file_location("sw0", DEV / "harness" / "sw.py")
os.environ.update(ENV)
sw0 = importlib.util.module_from_spec(spec0)
spec0.loader.exec_module(sw0)
sw0.write_op(G, {"op": "task", "id": "survey-9", "kind": "survey", "title": "Survey", "requires": "any"})
with open(T / "state" / G2 / "sessions.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps({"id": "old", "device": "other", "game": G2, "started": sw0.now_iso(time.time() - 3 * 3600),
                        "minutes": 1, "steps": 1, "status": "ok"}) + chr(10))
c = sw("claim")["assignments"][0]
check(c["game"] == G2 and "turn" in c, f"a game not played for 2 h goes before another game's survey: {c['game']}")
sw("end", "--status", "ok", "--summary", "release")
with open(T / "state" / G / "sessions.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps({"id": "old2", "device": "other", "game": G, "started": sw0.now_iso(time.time() - 2.5 * 3600),
                        "minutes": 1, "steps": 1, "status": "ok"}) + chr(10))
c = sw("claim")["assignments"][0]
check(c["game"] == G2, f"both waited over 2 h: the longer-waiting game goes first, not the higher priority: {c['game']}")
sw("end", "--status", "ok", "--summary", "release")

# an older version on the phone than on Google Play: work for a human, shown in the wiki
spec = importlib.util.spec_from_file_location("sw", DEV / "harness" / "sw.py")
os.environ.update(ENV)
swm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(swm)
swm.write_op(G2, {"op": "task", "id": "update-999.0.0", "kind": "update", "version": "999.0.0",
                  "title": "Recheck the features on version 999.0.0"})
swm.write_op(G2, {"op": "phone_version", "value": "10.6.5"})
swm.write_op(G2, {"op": "play_version", "value": "999.0.0", "checked": swm.now_iso()})
v = swm.research_view(G2)
st = swm.game_status(v, time.time())
# needs_human when nothing else is ready; with other work ready (a survey) the status still carries the hint
check(st[0] in ("needs_human", "active") and "installed 10.6.5, Google Play 999.0.0" in st[1],
      f"version behind Google Play -> the status says to update: {st[0]}: {st[1]}")
v["tasks"] = [t for t in v["tasks"] if t["kind"] == "update"]
st = swm.game_status(v, time.time())
check(st[0] == "needs_human", f"only the version-blocked analysis left -> needs a human: {st[1]}")
w = T / "wiki"
sw("snapshot", G2, str(w / G2 / "research.yaml"), "--until", swm.now_iso(time.time() + 2))
sw("snapshot", G, str(w / G / "research.yaml"), "--until", swm.now_iso(time.time() + 2))
sw("render", str(w))
tm = (w / G2 / "tasks.md").read_text(encoding="utf-8")
ov = (w / "tasks.md").read_text(encoding="utf-8")
check("installed 10.6.5, Google Play 999.0.0" in tm, "tasks.md: Needs a human says to update")
ready_part = tm.split("## Ready now")[1].split("## Waiting")[0]
check("version 999.0.0" not in ready_part, "the recheck waiting for an update is not listed as ready now")
check("Block Blast" in ov and "update the game on the phone" in ov, "wiki/tasks.md: which phone is needed says to update")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
