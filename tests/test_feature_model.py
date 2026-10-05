"""The feature model: the type catalog and its checklists, why a feature appeared, the base level's outcomes and the
matrix under flow-affecting features, locks as data and the first look, the type designer's local types, the audit,
and the existing games' untyped maps (fake phone, a scratch wiki and state)."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP, frames_dir  # noqa: E402
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

import yaml

T = TMP / "featuremodel"
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
LOCAL_TYPES = T / "state" / "feature-types.local.yaml"


def sw(*a, expect_ok=True, device=True, env=None):
    r = subprocess.run([sys.executable, str(DEV / "harness" / "sw.py"), *(["-d", "fake1"] if device else []), *a],
                       capture_output=True, text=True, encoding="utf-8", env=env or ENV, cwd=DEV)
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


def feat(v, fid):
    return next((f for f in v["features"] if f["id"] == fid), None)


def task(v, tid):
    return next((t for t in v["tasks"] if t["id"] == tid), None)


def case_ids(f, prefix=""):
    return [c["id"] for c in f.get("cases", []) if c["id"].startswith(prefix)]


def journal_len():
    p = T / "state" / G / "research.jsonl"
    return len(p.read_text(encoding="utf-8").splitlines()) if p.exists() else 0


def planned_ids(r):
    return [p["id"] for p in r.get("planned", [])] if isinstance(r, dict) else []


os.environ.update(ENV)
spec = importlib.util.spec_from_file_location("sw", DEV / "harness" / "sw.py")
swm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(swm)

# --- 1. the catalog ---------------------------------------------------------------------------------------
r = sw("types", device=False)
types = {t["id"]: t for t in r["types"]}
check({"core-level", "level-type", "mode", "event", "streak", "offer", "currency-booster", "meta-progress", "daily",
       "ad-placement", "social", "system"} <= set(types), f"the first set of types: {sorted(types)}")
check(all([i["id"] for i in t["checklist"][:3]] == ["appeared", "entry", "screen"] for t in types.values()),
      "every type's checklist starts with the universal items")
check(all(set(t) >= {"id", "name", "description", "base", "affects_level_flow", "checklist"} and
          all(set(i) == {"id", "text", "kind"} and i["kind"] in ("look", "outcome", "experiment") for i in t["checklist"])
          for t in types.values()), "every type has the contract's fields; items are {id, text, kind}")
lt = types["level-type"]
check(lt["base"] == "core-level" and lt["affects_level_flow"] and
      {"announce", "differs", "win", "loss", "retry", "frequency"} <= {i["id"] for i in lt["checklist"]},
      "level-type: based on core-level, affects the level flow, its own items")
check({i["id"] for i in types["core-level"]["checklist"] if i["kind"] == "outcome"} == {"win", "restart", "quit", "exit-app"},
      "core-level asks for every outcome: win, restart, quit, exit (and each loss as an outcome of its own)")
check(types["event"]["affects_level_flow"] and types["streak"]["affects_level_flow"] and
      not any(types[t]["affects_level_flow"] for t in ("core-level", "offer", "system", "mode", "daily")),
      "events and streaks affect the level flow; offers, systems, modes do not")
check("never pay" in " ".join(i["text"] for i in types["offer"]["checklist"]), "offers stop before paying")

# --- 2. a session: a new feature without a type or a trigger is accepted with warnings --------------------
c = sw("claim")["assignments"][0]
check(c["game"] == G, "claim: the game")
s = sw("start", G)
check("currency-booster" in s.get("feature_types", {}) and "level-type" in s["feature_types"],
      "the start reply shows the type catalog, so a feature is typed at once")
sid = next((T / "raw" / G).glob("*/steps.jsonl")).parent.name
sw("progress", "level 3", "--value", "3")
r = sw("feature", "shop", "Shop")
w = " ".join(r.get("warnings", []))
check("untyped" in w and "why did it appear" in w and not r["feature"].get("cases"),
      "a new feature without --type or --appeared: accepted, the reply warns it is untyped and asks why it appeared")
r = sw("feature", "x", "X", "--type", "nosuch", expect_ok=False)
check("no feature type nosuch" in json.dumps(r) and "unknown" in json.dumps(r), "an unknown type id is refused")
r = sw("feature", "brand-new", expect_ok=False)
check("needs its name" in json.dumps(r), "a new feature needs its name")
r = sw("feature", "y", "Y", "--appeared", "a", "--appeared-guess", "b", expect_ok=False)
check("give one" in json.dumps(r), "a fact and a guess at once are refused")

# --- 3. the base level: its checklist, its outcomes, a fact closes chk-appeared ---------------------------
r = sw("feature", "core", "Core level", "--type", "core-level", "--appeared", "the first board after the launch")
f, cs = r["feature"], {c["id"]: c for c in r["feature"]["cases"]}
check(set(cs) == {f"chk-{i['id']}" for i in types["core-level"]["checklist"]} and "warnings" not in r,
      "--type core-level: its checklist as open cases chk-<item>")
check(f["appeared"]["certainty"] == "fact" and f["appeared"]["text"] == "the first board after the launch" and
      f["appeared"]["source"].startswith(sid + "#"), "--appeared: a fact with the session step as its source")
check(cs["chk-appeared"]["done"] and cs["chk-appeared"]["source"] == f["appeared"]["source"] and
      not cs["chk-entry"]["done"], "the fact closes chk-appeared")
check(all(cs[f"chk-{k}"].get("outcome") for k in ("win", "restart", "quit", "exit-app")) and
      not cs["chk-loss"].get("outcome"), "the core-level outcome items are the base level's outcomes")

# --- 4. a flow-affecting feature: a case per existing outcome, an appeared experiment, a matrix goal ---------
r = sw("feature", "hard", "Hard levels", "--type", "level-type", "--appeared-guess", "every 10th level")
f = r["feature"]
check(sorted(case_ids(f, "under-")) == ["under-exit-app", "under-quit", "under-restart", "under-win"],
      f"a new flow-affecting feature gets a case for each existing outcome: {case_ids(f, 'under-')}")
check(next(c for c in f["cases"] if c["id"] == "under-win")["text"] == "Win under Hard levels: as the base, or what differs",
      "under-win: '<outcome> under <feature>: as the base, or what differs'")
check({"appeared-hard", "outcomes-hard"} <= set(planned_ids(r)), f"the reply names the planned goals: {planned_ids(r)}")
v = view()
t = task(v, "appeared-hard")
check(t["kind"] == "experiment" and t["title"] == "Find why Hard levels appeared: every 10th level" and t.get("plan"),
      "a hypothesis: the experiment 'Find why <feature> appeared: <hypothesis>'")
t = task(v, "outcomes-hard")
check(t["kind"] == "experiment" and t["rank"] == 7 and t["feature"] == "hard" and t.get("plan") and
      t["title"].startswith("Run each outcome once under Hard levels: ") and "Win" in t["title"],
      f"the matrix goal: {t['title']}")
check(task(v, "appeared-core") is None, "a fact makes no appeared experiment")

# --- 5. a new outcome: a case on every existing flow feature; outcomes only on the base level ---------------
r = sw("case", "core", "out-of-moves", "Out of moves: no move left", "--outcome")
v = view()
c = next(c for c in feat(v, "core")["cases"] if c["id"] == "out-of-moves")
check(c.get("outcome") is True, "case --outcome marks an outcome of the base level")
f = feat(v, "hard")
check("under-out-of-moves" in case_ids(f) and
      next(c for c in f["cases"] if c["id"] == "under-out-of-moves")["text"].startswith("Out of moves under Hard levels"),
      "a new outcome creates its under-* case on the existing flow-affecting feature")
check("Out of moves" in task(v, "outcomes-hard")["title"], "the matrix goal lists the new outcome")
r = sw("case", "shop", "boom", "Boom", "--outcome", expect_ok=False)
check("core-level" in json.dumps(r), "an outcome on a feature that is not the base level is refused")
r = sw("case", "core", "under-win", "x", "--outcome", expect_ok=False)
check("not chk- or under-" in json.dumps(r), "an outcome is not named chk- or under-")

# --- 6. idempotence ----------------------------------------------------------------------------------------
before = case_ids(feat(view(), "hard"))
n0 = journal_len()
r = sw("feature", "hard", "Hard levels", "--type", "level-type")
check(journal_len() == n0 + 1 and "planned" not in r and case_ids(feat(view(), "hard")) == before,
      "the same type again: one feature op, no new cases, nothing planned")
swm.plan_game(G, [], time.time())  # the planner's own goals (studies) for the new features
n1 = journal_len()
swm.plan_game(G, [], time.time())
check(journal_len() == n1 and swm.plan_feature_goals(G) == [], "the planner run twice writes nothing the second time")
v = view()
check(all(len(case_ids(f)) == len(set(case_ids(f))) for f in v["features"]), "no duplicate case anywhere")
check(task(v, "study-hard") and task(v, "study-core"), "the planner's study goals for the open features")

# --- 7. a type change adds the new type's missing items and keeps the old ones -----------------------------
sw("feature", "shop", "--type", "offer")
check({"chk-contents", "chk-buy-path"} <= set(case_ids(feat(view(), "shop"), "chk-")), "typed offer: its checklist")
sw("case", "shop", "chk-contents", "Three packs: 0.99, 4.99, 9.99", "--done")
r = sw("feature", "shop", "--type", "system")
ids = case_ids(r["feature"], "chk-")
check({"chk-options", "chk-answers", "chk-links", "chk-appeared", "chk-entry", "chk-screen"} <= set(ids) and
      "chk-contents" in ids and "chk-buy-path" not in ids and len(ids) == len(set(ids)) and
      r["feature"]["type"] == "system",
      "a type change adds the new type's missing items; the former type's done items stay, its open ones go")
check(task(view(), "appeared-shop")["title"] == "Find why Shop appeared: unknown",
      "a typed feature with no trigger: 'Find why Shop appeared: unknown'")
r = sw("feature", "coins", "Coins", "--type", "unknown", "--appeared", "on the first win", expect_ok=False)
check("closest" in r and r["closest"][0]["type"] == "currency-booster",
      f"unknown without a reason is refused, with the closest types: {r}")
r = sw("feature", "odd", "Odd thing", "--type", "unknown", "--appeared", "a banner after level 2",
       "--why-unknown", "a banner that is no offer, no event and no ad")
check(sorted(case_ids(r["feature"])) == ["chk-appeared", "chk-entry", "chk-screen"],
      "--type unknown is allowed: the universal items only")

# --- 8. locks as data -------------------------------------------------------------------------------------
r = sw("feature", "mode-x", "Mode X", "--type", "mode", "--locked", "level 5", "--locked-value", "5",
       "--appeared", "the modes menu lists it from level 3")
check(r["feature"]["locked"] == {"text": "level 5", "value": 5.0} and "unlock-mode-x" in planned_ids(r),
      "--locked records the lock, and its unlock goal is planned at once")
t = task(view(), "unlock-mode-x")
check(t["kind"] == "unlock" and t["feature"] == "mode-x" and t["target_text"] == "level 5" and t["target_value"] == 5,
      "unlock-<feature> with the lock's target")
r = sw("feature", "mode-y", "Mode Y", "--type", "mode", "--locked", "collect 3 keys",
       "--appeared", "the modes menu lists it from level 3")
t = task(view(), "unlock-mode-y")
check(t and t["target_text"] == "collect 3 keys" and "target_value" not in t, "one lock per locked entry: its own goal")
r = sw("feature", "mode-z", "Mode Z", "--type", "mode", "--locked", "level 6", "--locked-value", "6",
       "--appeared", "the modes menu lists it from level 3")
r = sw("feature", "mode-z", "--locked-value", "3", expect_ok=False)
check("goes with --locked" in json.dumps(r), "--locked-value alone is refused")
swm.plan_game(G, [], time.time())
v = view()
check(not any(task(v, f"study-{m}") for m in ("mode-x", "mode-y", "mode-z")), "a locked feature gets no study goal")
check(not any(task(v, f"appeared-{m}") for m in ("mode-x",)), "a fact: no appeared goal for the locked mode")
# the threshold passed: a first look at once, first in the session
r = sw("progress", "level 5", "--value", "5")
check("first-look-mode-x" in planned_ids(r) and "first-look-mode-z" not in planned_ids(r),
      "progress passing the lock plans the first look at once (only for the lock it passed)")
t = task(view(), "first-look-mode-x")
check(t["kind"] == "study" and t["rank"] == 0 and t["feature"] == "mode-x" and
      t["title"] == "First look at Mode X: open it once, record what it is and decide whether it needs a full study",
      "the first look: a study goal ranked first")
swm.P()["session"]["max_goals"] = 99
st = swm.session_tasks(G, "fake1", "fake", time.time())
order = [t["id"] for t in st["ready"]]
check(order[0] == "first-look-mode-x", f"the first look goes first: {order[:3]}")
studies = [i for i, x in enumerate(order) if x.startswith("study-")]
check(order.index("outcomes-hard") > max([order.index("unlock-mode-y"), order.index("unlock-mode-z")] + studies),
      "the matrix goal waits behind the unlock and study goals")
check(all(order.index(f"appeared-{x}") < order.index("unlock-mode-y") for x in ("hard", "shop")),
      "appeared experiments rank as experiments")
# a won level passing a lock: the first look comes in the level end reply
sw("level", "start", "level 6", "--mechanic", "pin", "--plan", "pull the left pin", "--value", "6")
sw("taps", "50,50 60,60", "--why", "pins")
sw("shot")
r = sw("level", "end", "won", "--note", "left pin first")
check("first-look-mode-z" in planned_ids(r), "a won level that passes a lock plans its first look at once")
# seen open: the lock goes, unlocked_at keeps it, the unlock goal closes
r = sw("feature", "mode-x", "--unlocked")
f = r["feature"]
check("locked" not in f and f["unlocked_at"]["lock"] == "level 5" and f["unlocked_at"]["text"] == "level 6" and
      f["unlocked_at"]["source"].startswith(sid), f"--unlocked: unlocked_at {f.get('unlocked_at')}")
t = task(view(), "unlock-mode-x")
check(t["status"] == "done" and t["closed_by"] == "planner", "seen open: the planner closes its unlock goal")
r = sw("feature", "mode-x", "--locked", "level 5", "--unlocked", expect_ok=False)
check("give one" in json.dumps(r), "--locked and --unlocked at once are refused")
# an unlock goal done on a recorded lock: the feature is seen open, its first look comes, not a study
r = sw("task", "done", "unlock-mode-y", "--note", "3 keys collected, the mode opened")
v = view()
check(r.get("created") == "first-look-mode-y" and feat(v, "mode-y")["unlocked_at"]["lock"] == "collect 3 keys" and
      task(v, "study-mode-y") is None, "a done unlock goal on a recorded lock: seen open, a first look")

# --- 9. why it appeared: a fact closes the experiment; a guess never replaces a fact ------------------------
sw("feature", "hard", "--appeared", "every 5th level from level 10")
v = view()
f = feat(v, "hard")
check(task(v, "appeared-hard")["status"] == "done" and task(v, "appeared-hard")["closed_by"] == "planner" and
      next(c for c in f["cases"] if c["id"] == "chk-appeared")["done"], "a fact closes the experiment and chk-appeared")
sw("feature", "hard", "--appeared-guess", "every 7th level")
check(feat(view(), "hard")["appeared"]["text"] == "every 5th level from level 10", "a later guess does not replace a fact")
sw("feature", "shop", "--appeared-guess", "after the first loss")
check(task(view(), "appeared-shop")["title"] == "Find why Shop appeared: after the first loss",
      "a new hypothesis retitles the open experiment")

# --- 10. the matrix: one cell at a time; the goal closes with the last; a new outcome reopens it ------------
sw("mechanic", "pin", "Pin", "--status", "mastered")
for k in (7, 8):
    sw("level", "start", f"level {k}", "--mechanic", "pin", "--plan", "lose on purpose: no moves", "--value", str(k))
    r = sw("level", "end", "lost", "--deliberate", "--note", "out of moves under the hard level, on purpose")
check(r["mechanic"]["status"] == "mastered" and "mechanic_change" not in r,
      "two deliberate losses in a row do not count against a mastered mechanic")
lv = [json.loads(x) for x in (T / "state" / G / "research.jsonl").read_text(encoding="utf-8").splitlines()]
check([o.get("deliberate") for o in lv if o["op"] == "level"][-2:] == [True, True], "the level records keep --deliberate")
sw("level", "start", "level 9", "--mechanic", "pin", "--plan", "x", "--value", "9")
r = sw("level", "end", "won", "--deliberate", "--note", "x", expect_ok=False)
check("lost --deliberate" in json.dumps(r), "--deliberate on a win is refused")
sw("level", "end", "quit", "--note", "end the try")
cells = case_ids(feat(view(), "hard"), "under-")
for cid in cells[:-1]:
    sw("case", "hard", cid, "as the base", "--done")
t = task(view(), "outcomes-hard")
label = dict(swm.known_outcomes(swm.research_view(G)))[cells[-1][6:]]
check(t["status"] == "open" and t["title"] == f"Run each outcome once under Hard levels: {label}",
      f"one cell left: the goal names it ({t['title']})")
sw("case", "hard", cells[-1], "Stage failed window: Tap to restart goes back to stage 1", "--done")
t = task(view(), "outcomes-hard")
check(t["status"] == "done" and t["closed_by"] == "planner", "the last cell closes the matrix goal")
sw("case", "core", "bomb", "Bomb: a bomb reaches the cup", "--outcome")
v = view()
t = task(v, "outcomes-hard")
check(t["status"] == "open" and t["title"] == "Run each outcome once under Hard levels: Bomb" and
      "under-bomb" in case_ids(feat(v, "hard")), "a new outcome reopens the matrix goal with its cell")
r = sw("feature", "race", "Level race", "--type", "event", "--appeared", "after level 4")
check(set(case_ids(r["feature"], "under-")) == {"under-win", "under-restart", "under-quit", "under-exit-app",
                                                 "under-out-of-moves", "under-bomb"},
      "an event registered later gets a case for every known outcome")
sw("end", "--status", "ok", "--summary", "feature model")

# --- 11. the type designer: a local type used at once --------------------------------------------------------
r = sw("type-add", "puzzle-race", "--name", "Puzzle race", "--description", "A race whose points come from puzzles",
       "--base", "event", "--affects-level-flow", "--item", "board:The race board: ranks and points:look",
       "--item", "finish:Finish: the reward:outcome", device=False)
ty = r["type"]
check([i["id"] for i in ty["checklist"]] == ["appeared", "entry", "screen", "board", "finish"] and ty["local"] and
      ty["affects_level_flow"] and ty["base"] == "event" and ty["checklist"][3]["text"] == "The race board: ranks and points",
      f"type-add: universal items first, the text keeps its colons, marked local: {ty}")
raw = LOCAL_TYPES.read_bytes()
check(b"puzzle-race" in raw and b"\r\n" not in raw, "written to state/feature-types.local.yaml with LF endings")
check(any(t["id"] == "puzzle-race" and t.get("local") for t in sw("types", device=False)["types"]), "types lists it")
for bad, why in ((["event"], "a published type"), (["new-a", "--item", "x:y:feel"], "--item is ID:TEXT:KIND"),
                 (["new-b", "--item", "entry:Where:look"], "not the universal"), (["new-c"], "its own checklist"),
                 (["new-d", "--base", "nosuch", "--item", "a:b:look"], "to base it on")):
    r = sw("type-add", *bad[:1], "--name", "N", "--description", "D", *bad[1:], expect_ok=False, device=False)
    check(why in json.dumps(r), f"type-add refuses: {why}")
r = sw("feature", "fx", "FX race", "--type", "puzzle-race", "--appeared-guess", "every weekend", "--game", G,
       "--source", "20261002-120000-testbox-X#5", device=False)
f = r["feature"]
check({"chk-board", "chk-finish"} <= set(case_ids(f)) and "under-bomb" in case_ids(f) and
      f["appeared"] == {"text": "every weekend", "certainty": "hypothesis", "source": "20261002-120000-testbox-X#5"},
      "the review types a feature with the new type at once: its checklist and the matrix")
# a local override of a published type reaches every feature of that type
loc = yaml.safe_load(LOCAL_TYPES.read_text(encoding="utf-8"))
loc["types"].append({"id": "system", "checklist": [{"id": "privacy", "text": "Privacy: the policy link", "kind": "look"}]})
LOCAL_TYPES.write_text(yaml.safe_dump(loc, sort_keys=False), encoding="utf-8")
check("chk-privacy" in case_ids(feat(view(), "shop")), "a local override adds its item to the published type")
r = sw("types", "--prune", device=False)
check(r["pruned"] == ["system"] and [t["id"] for t in yaml.safe_load(LOCAL_TYPES.read_text(encoding="utf-8"))["types"]]
      == ["puzzle-race"], "types --prune drops the local types the published catalog has")

# --- 12. the audit -----------------------------------------------------------------------------------------
swm.write_op(G, {"op": "feature", "id": "legacy", "name": "Legacy thing"})
swm.write_op(G, {"op": "feature", "id": "locked-w", "name": "W", "type": "mode", "locked": {"text": "level 50", "value": 50}})
a = sw("audit", G, device=False)
check([x["id"] for x in a["untyped"]] == ["legacy"] and [x["id"] for x in a["unknown_type"]] == ["odd"],
      "audit: the untyped and the unknown-type features")
check("legacy" in a["appeared_missing"] and "core" not in a["appeared_missing"] and
      any(x["feature"] == "shop" and x["hypothesis"] == "after the first loss" and x["goal"]["status"] == "open"
          for x in a["appeared_hypothesis"]), "audit: features without a trigger, and hypotheses with their goals")
check(a["locks_without_unlock_goal"] == ["locked-w"] and any("unlock goal" in h for h in a["hints"]),
      "audit: a lock without an unlock goal")
cl = {x["feature"]: x for x in a["checklist_open"]}
check("chk-entry" in [c["id"] for c in cl["shop"]["open"]] and cl["core"]["total"] == len(types["core-level"]["checklist"]),
      "audit: open checklist items per feature")
m = {x["feature"]: x for x in a["matrix"]}
check(set(m) == {"hard", "race", "fx"} and m["hard"]["open"] == ["bomb"] and len(m["hard"]["closed"]) == 5 and
      m["hard"]["goal"] == {"id": "outcomes-hard", "status": "open"} and a["base_levels"] == ["core"],
      "audit: the matrix, cells open and closed per condition feature")
check({o["id"] for o in a["outcomes"]} == {"win", "restart", "quit", "exit-app", "out-of-moves", "bomb"} and
      a["counts"]["untyped"] == 1, "audit: the known outcomes and the counts")
planned = swm.plan_feature_goals(G)
check([p["id"] for p in planned] == ["unlock-locked-w"] and sw("audit", G, device=False)["locks_without_unlock_goal"] == [],
      "the planner makes the missing unlock goal; nothing for the untyped legacy feature")
check(task(view(), "appeared-legacy") is None and view()["summary"]["untyped"] == 1,
      "an untyped feature gets no appeared experiment and counts as untyped")

# --- 13. the snapshot keeps the model; a view on top of it adds nothing ----------------------------------
before = {f["id"]: case_ids(f) for f in view()["features"]}
gw = T / "gwiki" / G / "research.yaml"
sw("snapshot", G, str(gw), "--until", swm.now_iso(time.time() + 2), device=False)
snap = yaml.safe_load(gw.read_text(encoding="utf-8"))
sf = {f["id"]: f for f in snap["features"]}
check(sf["mode-x"]["unlocked_at"]["lock"] == "level 5" and sf["hard"]["type"] == "level-type" and
      sf["shop"]["appeared"]["certainty"] == "hypothesis" and sf["locked-w"]["locked"]["value"] == 50 and
      any(c["id"] == "under-bomb" for c in sf["race"]["cases"]), "research.yaml carries type, appeared, locks and cases")
check({f["id"]: case_ids(f) for f in view()["features"]} == before and swm.plan_feature_goals(G) == [],
      "the view over the snapshot adds no case and plans nothing")

# --- 14. the existing games: untyped maps work, nothing is planned for them, the wiki is not touched -------
(T / "local2.yaml").write_text(f"""machine: testbox2
android: {{serials: [nophone]}}
state_dir: "{(T / 'state2').as_posix()}"
raw_dir: "{(T / 'raw2').as_posix()}"
""", encoding="utf-8")
ENV2 = {**ENV, "SW_LOCAL": str(T / "local2.yaml")}
games = sorted(p.parent.name for p in (ROOT / "wiki").glob("*/research.yaml"))
digest = {g: hashlib.sha1((ROOT / "wiki" / g / "research.yaml").read_bytes()).hexdigest() for g in games}
maps = {g: yaml.safe_load((ROOT / "wiki" / g / "research.yaml").read_text(encoding="utf-8")) for g in games}
# the maps the type designer has not reached yet (the dreams type them one by one: com.block.juggle was typed by
# 2026-10-05, and the audit of a typed map has a checklist and a matrix by design)
legacy = [g for g in games if all(not f.get("type") for f in maps[g]["features"])]
for g in games:
    a = sw("audit", g, device=False, env=ENV2)
    n = len(maps[g]["features"])
    if g in legacy:
        check(a["counts"]["untyped"] == n == a["counts"]["features"] and a["matrix"] == [] and a["checklist_open"] == [],
              f"{g}: {n} features, all untyped, no checklist, no matrix")
    else:
        check(a["counts"]["features"] == n and a["counts"]["untyped"] < n, f"{g}: {n} features, the audit reads a typed map")
os.environ["SW_LOCAL"] = str(T / "local2.yaml")
spec2 = importlib.util.spec_from_file_location("sw2", DEV / "harness" / "sw.py")
swm2 = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(swm2)
check(all(swm2.plan_feature_goals(g) == [] for g in legacy) and not (T / "state2").exists(),
      "the planner plans nothing for the untyped maps and writes no journal")
check(all(len(swm2.research_view(g)["features"]) for g in games) and
      all(swm2.feature_audit(swm2.research_view(g))["counts"]["untyped"] for g in legacy),
      "research views of the existing games")
check(all(hashlib.sha1((ROOT / "wiki" / g / "research.yaml").read_bytes()).hexdigest() == digest[g] for g in games),
      "the wiki's research.yaml files are untouched")
os.environ["SW_LOCAL"] = ENV["SW_LOCAL"]
print("all ok")
shutil.rmtree(T, ignore_errors=True)
