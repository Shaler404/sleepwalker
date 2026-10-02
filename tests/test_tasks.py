"""Scenario test of the sw.py task model on fake devices (no phone)."""
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
T = TMP / "tasktest"
DEV = ROOT
shutil.rmtree(T, ignore_errors=True)
T.mkdir()
(T / "local.yaml").write_text(f"""machine: testbox
android: {{serials: [nophone]}}
fake_devices: {{fake1: "{frames_dir().as_posix()}", fake2: "{frames_dir().as_posix()}"}}
tools: {{ffmpeg: C:/Code/ffmpeg_latest/ffmpeg.exe, ffprobe: C:/Code/ffmpeg_latest/ffprobe.exe}}
video: {{record: false}}
state_dir: "{(T / 'state').as_posix()}"
raw_dir: "{(T / 'raw').as_posix()}"
wiki_dir: "{(T / 'gwiki').as_posix()}"
""", encoding="utf-8")
ENV = {**os.environ, "SW_LOCAL": str(T / "local.yaml"), "PYTHONIOENCODING": "utf-8"}
G = "com.maroieqrwlk.unpin"
CYR = __import__("re").compile("[А-Яа-яЁё]")


def sw(*a, device=None, expect_ok=True):
    cmd = [sys.executable, str(DEV / "harness" / "sw.py")] + (["-d", device] if device else []) + list(a)
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", env=ENV, cwd=DEV)
    if expect_ok and r.returncode != 0:
        raise SystemExit(f"FAIL {a}: {r.stdout}\n{r.stderr}")
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return r.stdout


def research():
    return yaml.safe_load(sw("research", G))


def check(cond, msg):
    print(("OK   " if cond else "FAIL ") + msg)
    if not cond:
        raise SystemExit(1)


# 1. first claim: the planner adds "analyze version X" for every game
c = sw("claim")
a = {x["device"]: x for x in c["assignments"]}
check(all(x["action"] == "play" for x in a.values()), "both devices got a game")
check(a["fake1"]["game"] == G and a["fake1"]["tasks"][0]["id"] == "scout-1" and
      all(t["id"] != "analyze" for t in a["fake1"]["tasks"]), "fake1: Pull the Pin, the first goal is the map, never 'analyze'")
r = research()
t = next(t for t in r["tasks"] if t["id"] == "analyze")
check(t["title"] == "Analyze the game" and not t.get("version"), f"analyze title, no version tie: {t['title']}")
check(not CYR.search(json.dumps(c, ensure_ascii=False)), "claim output has no Russian")

# 2. session on fake1: progressed install -> harvest, gap tasks, timer, daily activity
s = sw("start", G, device="fake1")
check(s["device_state"] == "unknown" and "tasks" in s, "start: state unknown, session tasks in the answer")
check(not CYR.search(s["hint"]), f"start hint in English: {s['hint'][:60]}")
sw("device-state", "progressed", "--note", "level 36, shop and chests open", device="fake1")
sw("tap", "100", "100", "--why", "open the map", "--settle", "0", device="fake1")
sw("feature", "level-map", "Level map", "--status", "documented", device="fake1")
sw("feature", "chest", "Level chest", device="fake1")
sw("case", "chest", "open", "Open the chest", "--done", device="fake1")
sw("task", "add", "ftue", "Play FTUE from scratch", "--kind", "ftue", "--requires", "fresh", device="fake1")
sw("task", "add", "unlock-chest", "How the chest unlocks", "--kind", "replay", "--requires", "fresh",
   "--feature", "chest", device="fake1")
sw("task", "add", "chest-timer", "Open the chest after the timer", "--after-hours", "3", "--feature", "chest",
   device="fake1")
r2 = sw("task", "add", "daily-bonus", "Claim the daily bonus", "--kind", "daily", "--days", "3", device="fake1")
check(len(r2["tasks"]) == 3 and r2["tasks"][0]["not_before"] < r2["tasks"][2]["not_before"], "daily: 3 tasks, one per day")
sw("feature", "chest", "Level chest", "--status", "documented", device="fake1")
sw("task", "done", "scout-1", "--new-entries", "2", "--note", "map and chest", device="fake1")
sw("discovery", "closed", device="fake1")
e = sw("end", "--status", "ok", "--summary", "harvest", device="fake1")
check(len(e["tasks_added"]) == 6, f"end: {len(e['tasks_added'])} tasks added")
sw("end", "--status", "ok", "--summary", "x", device="fake2", expect_ok=False)

# 3. next claim: analyze closed itself, Pull the Pin waits for timers and a fresh install
c = sw("claim", device="fake1")
check(c["assignments"][0]["game"] != G, f"fake1 got another game ({c['assignments'][0].get('game')})")
sw("end", "--status", "ok", "--summary", "x", device="fake1", expect_ok=False)
r = research()
t = next(t for t in r["tasks"] if t["id"] == "analyze")
check(t["status"] == "done" and t.get("closed_by") == "planner", "analyze closed by the planner")
check(r["summary"]["status"] in ("waiting", "needs_human"), f"game status {r['summary']['status']}")

# 4. the owner provides a fresh install -> fresh-only tasks become available
sw("device-state", "fresh", "--game", G, device="fake1")
os.environ.update(ENV)
spec = importlib.util.spec_from_file_location("sw", DEV / "harness" / "sw.py")
swm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(swm)
st = swm.session_tasks(G, "fake1", "fake", time.time())
check({t["id"] for t in st["ready"]} == {"ftue", "unlock-chest"}, f"fresh install: ready {[t['id'] for t in st['ready']]}")

# 5. a newer version on Google Play -> a recheck task that waits for the phone; nothing moves to recheck yet
swm.write_op(G, {"op": "version", "value": "1.0.0", "force": True})
swm.write_op(G, {"op": "play_version", "value": "999.0.0", "checked": swm.now_iso()})
swm.plan_game(G, ["1.0.0"], time.time())
view = swm.research_view(G)
upd = swm.find_task(view, "update-999.0.0")
check(upd is not None and upd["title"] == "Recheck the features on version 999.0.0", f"recheck task: {upd and upd['title']}")
check(not any(f["status"] == "recheck" for f in view["features"]), "Google Play alone does not send features to recheck")
check(swm.eligible(upd, "progressed", "1.0.0", time.time())[0] is False and
      swm.eligible({"id": "analyze", "kind": "analyze", "status": "open", "version": "999.0.0"}, "progressed", "1.0.0",
                   time.time())[0] is True,
      "the recheck waits for the update; the analysis is not blocked")
check(swm.game_status(view, time.time())[0] in ("needs_human", "active", "waiting") and swm.find_task(view, "update-999.0.0")["status"] == "open",
      f"status: {swm.game_status(view, time.time())}")
# the phone gets the new version -> documented features move to recheck, the recheck task is ready
swm.plan_game(G, ["999.0.0"], time.time())
view = swm.research_view(G)
check(view["version"] == "999.0.0" and all(f["status"] == "recheck" for f in view["features"] if f.get("version_seen")),
      "the phone has 999.0.0: documented features to recheck")
check(swm.eligible(swm.find_task(view, "update-999.0.0"), "progressed", "999.0.0", time.time())[0], "the recheck is ready")

# 5b. FTUE is rechecked only with a new version and only if the last run from scratch is older than 180 days
old = time.time() - 200 * 86400
swm.append_jsonl(T / "state" / G / "research.jsonl", {"t": old, "session": "old", "op": "task_done", "id": "ftue",
                                                      "kind": "ftue", "title": "FTUE"})
swm.plan_game(G, [], time.time())
view = swm.research_view(G)
check(view["ftue_verified"] and not [t for t in swm.open_tasks(view) if t["kind"] == "ftue" and t["id"] != "ftue"],
      "old FTUE but no new version: no FTUE task")
swm.write_op(G, {"op": "play_version", "value": "1000.0.0", "checked": swm.now_iso()})
swm.plan_game(G, ["1000.0.0"], time.time())
t = swm.find_task(swm.research_view(G), "ftue-1000.0.0")
check(t is not None and t["title"] == "Check whether FTUE changed in version 1000.0.0" and t["requires"] == "fresh",
      f"new version + old FTUE: {t and t['title']}")

# 6. old journal: a case with a deadline becomes a task
swm.append_jsonl(T / "state" / G / "features.jsonl", {"t": 1.0, "session": "old", "op": "case", "feature": "shop",
                                                      "id": "offer", "text": "Offer after a day",
                                                      "after": "2030-01-01T00:00:00"})
check(swm.find_task(swm.research_view(G), "shop-offer") is not None, "old-journal case with a deadline became a task")

# 7. snapshot into the wiki and render
w = T / "wiki"
p = sw("pending")
sw("snapshot", G, str(w / G / "research.yaml"), "--until", p["until"] or swm.now_iso())
sw("render", str(w))
tm = (w / G / "tasks.md").read_text(encoding="utf-8")
ov = (w / "tasks.md").read_text(encoding="utf-8")
for h in ("# Tasks: ", "## Ready now", "## Waiting", "## Needs a human", "## Done"):
    check(h in tm, f"tasks.md has «{h}»")
check("fresh install" in tm, "tasks.md: the fresh-install hint")
check("# Tasks by game" in ov and "## Which phone is needed" in ov, "wiki/tasks.md overview")
for name, text in (("tasks.md", tm), ("overview", ov), ("features.md", (w / G / "features.md").read_text(encoding="utf-8"))):
    check(not CYR.search(text), f"{name} has no Russian")
print("\n" + tm[:1200])
