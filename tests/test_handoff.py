"""Model roles for a broken mechanic: follow-ups that play levels go to the strong model, a handoff names its
mechanic and the next brief carries it, stats count the handoffs that did nothing."""
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

T = TMP / "handofftest"
DEV = ROOT
shutil.rmtree(T, ignore_errors=True)
T.mkdir()
G = "com.vitastudio.mahjong"
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


def sessions():
    return [json.loads(x) for x in (T / "state" / G / "sessions.jsonl").read_text(encoding="utf-8").splitlines()]


def as_play_role():
    """As if claim had given this session to the fast model."""
    s = json.loads(SESS.read_text(encoding="utf-8"))
    s["model_role"] = "play"
    SESS.write_text(json.dumps(s), encoding="utf-8")


os.environ.update(ENV)
spec = importlib.util.spec_from_file_location("sw", DEV / "harness" / "sw.py")
swm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(swm)


def view(*statuses):
    return {"game": G, "mechanics": [{"id": f"m{i}", "status": s} for i, s in enumerate(statuses)]}


def tasks(*kinds):
    return [{"id": f"t{i}", "kind": k} for i, k in enumerate(kinds)]


# model_role: Vita Mahjong 2026-10-01 — three follow-ups needing a level won, core-match broken
role, why = swm.model_role(view("broken"), tasks("followup", "followup", "followup"))
check(role == "study" and "m0 (broken)" in why and "the tasks need levels" in why,
      f"a broken mechanic and follow-ups -> the strong model: {role} ({why})")
for kinds in (("ftue",), ("replay",), ("followup", "daily")):
    check(swm.model_role(view("mastered", "studying"), tasks(*kinds))[0] == "study",
          f"a studying mechanic and {kinds} -> the strong model")
role, why = swm.model_role(view("mastered", "mastered"), tasks("followup", "followup", "followup"))
check(role == "play" and "checks and studies" in why, f"every mechanic mastered and follow-ups -> the fast model: {why}")
check(swm.model_role(view("broken"), tasks("study", "daily", "survey"))[0] == "play",
      "a broken mechanic but only menu work (study, daily, survey) -> the fast model")
check(swm.model_role(view(), tasks("followup"))[0] == "play", "no mechanic yet and a check -> the fast model, as before")
check(swm.model_role(view(), tasks("scout"))[0] == "study", "no mechanic yet and a scout -> the strong model, as before")
check(swm.model_role(view("mastered"), tasks("unlock"))[0] == "play", "mastered and an unlock -> the fast model, as before")
last = {"id": "s1", "status": "handoff", "handoff_to": "m0"}
role, why = swm.model_role(view("broken"), tasks("daily"), last)
check(role == "study" and why == "handoff from s1: m0 is broken", f"after a handoff the brief names the mechanic: {why}")
# the mechanic was mastered already when the player gave up (Amaze GO! Hard L5 under a mastered arrows-escape,
# 20261003-232357 -> 233756 stuck; Pull the Pin Space theme under a mastered pin-pull, 20261004-003223 -> 004411
# handed off again): the handoff stands. Mastered after the handoff (the lab fixed it): the usual rule
last_t = {**last, "started": "2026-10-04T00:00:00", "minutes": 10}
role, why = swm.model_role(view("mastered"), tasks("daily"), last_t)
check(role == "study" and "m0 is mastered" in why and "the handoff stands" in why,
      f"a handoff whose mechanic was mastered already: the strong model takes the next session: {why}")
fixed = [{"op": "mechanic", "id": "m0", "status": "mastered", "t": swm.session_end_t(last_t) + 60}]
check(swm.model_role(view("mastered"), tasks("daily"), last_t, fixed)[0] == "play",
      "a handoff whose mechanic was mastered after it (the lab fixed it): the usual rule")
stale = [{"op": "mechanic", "id": "m0", "status": "mastered", "t": swm.session_end_t(last_t) - 3600}]
check(swm.model_role(view("mastered"), tasks("daily"), last_t, stale)[0] == "study",
      "mastered an hour before the handoff: the handoff stands")
role, why = swm.model_role(view("mastered"), tasks("daily"), {"id": "s0", "status": "handoff"})
check(role == "study" and "met gameplay to learn" in why, f"a handoff with no mechanic named -> the strong model: {why}")
check(swm.model_role(view("broken"), tasks("daily"), {"id": "s2", "status": "ok"})[0] == "play",
      "the last session was not a handoff: the usual rule")

# claim: core-match broken, the open tasks are only follow-ups that play levels
sw("mechanic", "core-match", "Core match", "--status", "broken", "--game", G, device=False)
sw("task", "cancel", "analyze", "--reason", "test: a game with follow-ups only", "--game", G, device=False)
sw("discovery", "closed", "--why", "test", "--game", G, device=False)
for tid in ("auto-complete-trigger", "hard-levels-streak", "interstitials"):
    sw("task", "add", tid, f"Check {tid} after a won level", "--game", G, device=False)
c = sw("claim")["assignments"][0]
check(c["game"] == G and [t["kind"] for t in c["tasks"]] == ["followup"] * 3,
      f"claim hands out the three follow-ups: {[t['id'] for t in c.get('tasks', [])]}")
check(c["model_role"] == "study" and c["model"] == "opus" and "core-match (broken)" in c["model_why"],
      f"follow-ups while core-match is broken -> the strong model: {c['model_role']} {c['model']} ({c['model_why']})")
sw("end", "--status", "ok", "--summary", "release the reservation")

# the fast model meets the broken mechanic: the hint names --to; end without --to takes the open level's mechanic
sw("start", G, "--model", "sonnet")
as_play_role()
r = sw("level", "start", "level 18", "--mechanic", "core-match", "--plan", "look", "--value", "18")
check("--to core-match" in r.get("handoff", ""), f"the handoff hint names the mechanic: {r.get('handoff')}")
r = sw("end", "--status", "handoff", "--summary", "core-match is broken: not mine to learn")
s1 = sessions()[-1]
check(r.get("handoff_to") == "core-match" and s1["handoff_to"] == "core-match" and s1["status"] == "handoff",
      f"end --status handoff takes the open level's mechanic into sessions.jsonl: {s1.get('handoff_to')}")
c = sw("claim")["assignments"][0]
check(c["game"] == G and c["model_role"] == "study" and c["model_why"] == f"handoff from {s1['id']}: core-match is broken",
      f"the next claim brings the game back with the strong model and the mechanic: {c['model_why']}")
sw("end", "--status", "ok", "--summary", "release the reservation")

r = sw("end", "--status", "ok", "--summary", "x", "--to", "core-match", expect_ok=False)
check("use it with --status handoff" in json.dumps(r), "--to without a handoff is refused")

# a handoff after a won level of another mechanic, named with --to: not a wasted one
time.sleep(1.1)  # session ids are per second
sw("start", G, "--model", "sonnet")
as_play_role()
sw("level", "start", "level 5", "--mechanic", "Easy pairs", "--plan", "pairs", "--value", "5")
sw("taps", "10,10 20,20", "--why", "two pairs", "--settle", "0")
sw("shot")  # a frame of the win screen: level end won needs one after the last move
sw("level", "end", "won", "--note", "fast")
r = sw("end", "--status", "handoff", "--to", "Core match", "--summary", "met core-match after a won level")
check(r.get("handoff_to") == "core-match" and sessions()[-1]["handoff_to"] == "core-match",
      "end --status handoff --to <mechanic> records it (as an id)")

# stats: a handoff that did nothing is wasted; one after a won level is not
st = sw("stats", G, device=False)
w = st["games"][G]["wasted_handoffs"]
check(w["sessions"] == 1 and w["minutes"] == sessions()[0]["minutes"], f"stats count the wasted handoffs: {w}")
st = sw("stats", "--by-model", device=False)
check(st["by_model"]["sonnet"]["wasted_handoffs"] == 1 and st["by_model"]["sonnet"]["stuck_or_handoff"] == 2,
      f"stats by model: {st['by_model']['sonnet']}")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
