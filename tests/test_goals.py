"""Scenario test of goal-driven sessions: map, unlock, study, experiment, the post-session review."""
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
T = TMP / "goaltest"
DEV = ROOT
shutil.rmtree(T, ignore_errors=True)
T.mkdir()
(T / "local.yaml").write_text(f"""machine: testbox
games: [com.maroieqrwlk.unpin]
android: {{serials: [nophone]}}
fake_devices: {{fake1: "{frames_dir().as_posix()}"}}
video: {{record: false}}
state_dir: "{(T / 'state').as_posix()}"
raw_dir: "{(T / 'raw').as_posix()}"
wiki_dir: "{(T / 'gwiki').as_posix()}"
""", encoding="utf-8")
ENV = {**os.environ, "SW_LOCAL": str(T / "local.yaml"), "PYTHONIOENCODING": "utf-8"}
G = "com.maroieqrwlk.unpin"


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


def view():
    return yaml.safe_load(sw("research", G, device=False))


# a new game: the first goal is the map; "analyze" is never handed to a session
c = sw("claim")["assignments"][0]
ids = [t["id"] for t in c["tasks"]]
check(ids == ["scout-1"] and c["mode"] == "goals", f"new game -> the map first: {ids}, mode {c['mode']}")
s = sw("start", G)
check([t["id"] for t in s["tasks"]] == ["scout-1"], "start: the session's goals")

# the map: open features, locked entry points with targets, an unclear badge
sw("progress", "level 3", "--value", "3")
sw("feature", "shop", "Shop")
sw("feature", "daily-reward", "Daily reward")
r = sw("task", "add", "unlock-leagues", "Reach level 20 to unlock Leagues", "--kind", "unlock", "--feature", "leagues",
       expect_ok=False)
check("target" in json.dumps(r), "an unlock goal without a target is refused")
sw("task", "add", "unlock-leagues", "Reach level 20 to unlock Leagues", "--kind", "unlock", "--feature", "leagues",
   "--target", "level 20", "--target-value", "20")
sw("task", "add", "unlock-events", "Reach level 8 to unlock Events", "--kind", "unlock", "--feature", "events",
   "--target", "level 8", "--target-value", "8")
r = sw("task", "add", "badge", "The red badge on the map is a daily quest", "--kind", "experiment", expect_ok=False)
check("--plan" in json.dumps(r), "an experiment without a plan is refused")
sw("task", "add", "badge", "The red badge on the map is a daily quest", "--kind", "experiment",
   "--plan", "tap the badge; confirmed if a quest list opens")
r = sw("task", "add", "study-x", "Study X", "--kind", "study", expect_ok=False)
check("--feature" in json.dumps(r), "a study goal without its feature is refused")
r = sw("task", "done", "scout-1", "--note", "x", expect_ok=False)
check("--new-entries" in json.dumps(r), "a map is closed with --new-entries")
sw("task", "done", "scout-1", "--new-entries", "5", "--note", "home, map, shop, daily, two locks")
sw("end", "--status", "ok", "--summary", "mapped")

# the planner adds study goals for open features; a session gets at most 3 goals, in order
c = sw("claim")["assignments"][0]
ids = [t["id"] for t in c["tasks"]]
v = view()
check({"study-shop", "study-daily-reward"} <= {t["id"] for t in v["tasks"]}, "study goals for the open features")
check(len(ids) == 3 and ids[:2] == ["study-daily-reward", "study-shop"] and ids[2] == "badge" and c["more_goals"] == 2,
      f"3 goals per session, studies first, then the experiment: {ids}, more {c['more_goals']}")
sw("end", "--status", "ok", "--summary", "release")

# unlock goals: nearest target first; a gate holds them, studies stay ready
os.environ.update(ENV)
spec = importlib.util.spec_from_file_location("sw", DEV / "harness" / "sw.py")
swm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(swm)
for t in ("study-shop", "study-daily-reward", "badge"):
    swm.write_op(G, {"op": "task_done", "id": t, "source": "test", **({"result": "confirmed"} if t == "badge" else {})})
st = swm.session_tasks(G, "fake1", "fake", time.time())
check([t["id"] for t in st["ready"]] == ["unlock-events", "unlock-leagues"], f"unlocks, nearest first: {[t['id'] for t in st['ready']]}")
swm.write_op(G, {"op": "gate", "type": "lives", "until": swm.now_iso(time.time() + 1800)})
st = swm.session_tasks(G, "fake1", "fake", time.time())
check(st["ready"] == [] and any("lives" in b["why"] for b in st["blocked"]), "a gate holds the unlock goals")
swm.write_op(G, {"op": "gate", "clear": True})

# reaching the target: the reply hints; closing the unlock creates the study goal
s = sw("start", G)
sw("progress", "level 8", "--value", "8")
st = swm.session_tasks(G, "fake1", "fake", time.time())
check(st["ready"][0]["id"] == "unlock-events" and "target is reached" in st["ready"][0].get("hint", ""),
      "the unlock goal says its target is reached")
r = sw("task", "done", "unlock-events", "--note", "Events opened at level 8")
check(r.get("created") == "study-events", f"a done unlock goal creates the study goal: {r.get('created')}")
r = sw("task", "add", "race", "Winning the race needs about 10 level wins", "--kind", "experiment",
       "--feature", "events", "--plan", "play levels while the race runs; confirmed if it is won by 10 wins")
r = sw("task", "done", "race", "--note", "x", expect_ok=False)
check("--result" in json.dumps(r), "an experiment is closed with --result")
sw("task", "done", "race", "--result", "refuted", "--note", "13 wins and still second: the bots are faster")
sw("end", "--status", "ok", "--summary", "unlock")
t = next(t for t in view()["tasks"] if t["id"] == "race")
check(t["result"] == "refuted" and "13 wins" in t["note"], "the experiment keeps its result and conclusion")

# the post-session review works without a session: closes goals with sources, closes discovery
r = sw("task", "done", "study-events", "--game", G, "--source", "20261001-x#12", "--note", "studied in session x",
       device=False)
check(r["task"]["status"] == "done" and r["task"]["closed_by"] == "20261001-x#12", "review: a goal closed with its source")
sw("case", "events", "open", "Open the events screen", "--done", "--game", G, "--source", "20261001-x#14", device=False)
sw("discovery", "closed", "--game", G, "--why", "map complete at level 8, Leagues has its unlock goal", device=False)
v = view()
check(v["discovery"] == "closed" and "Leagues" in v.get("discovery_note", ""), "review: discovery closed with a reason")
check(not swm.research_complete(swm.research_view(G)), "the analysis is not complete while goals are open")

# no goal left while discovery is open -> a new map
swm.write_op(G, {"op": "discovery", "value": "open"})
for t in [x for x in swm.open_tasks(swm.research_view(G)) if x["kind"] in swm.GOAL_KINDS]:
    swm.write_op(G, {"op": "task_cancel", "id": t["id"], "note": "test"})
swm.plan_goals(G, swm.research_view(G), time.time())
check(any(t["id"] == "scout-2" and t.get("status", "open") == "open" for t in swm.research_view(G)["tasks"]),
      "nothing left to do while the search is open: a new map")

# tasks.md shows the goals
w = T / "wiki"
sw("snapshot", G, str(w / G / "research.yaml"), "--until", swm.now_iso(time.time() + 2), device=False)
sw("render", str(w), device=False)
tm = (w / G / "tasks.md").read_text(encoding="utf-8")
ready = tm.split("## Ready now")[1].split("## Waiting")[0]
check("Goals: map 1" in tm and "| map |" in ready and "Analyze the game" not in ready,
      "tasks.md: the goals line; the analysis container is not listed as work")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
