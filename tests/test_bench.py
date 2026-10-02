"""Choosing models: per-game model and effort, player agents per variant, the local benchmark."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP, frames_dir  # noqa: E402
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

SP = Path(__file__).resolve().parent
T = TMP / "benchtest"
DEV = ROOT
shutil.rmtree(T, ignore_errors=True)
T.mkdir()
G = "com.maroieqrwlk.unpin"
(T / "local.yaml").write_text(f"""machine: testbox
games: [{G}]
onboarding:
  - id: com.example.newgame
    title: New Game
android: {{serials: [nophone]}}
fake_devices: {{fake1: "{frames_dir().as_posix()}"}}
video: {{record: false}}
state_dir: "{(T / 'state').as_posix()}"
raw_dir: "{(T / 'raw').as_posix()}"
wiki_dir: "{(T / 'gwiki').as_posix()}"
models: {{study: "opus:high", play: "sonnet:low"}}
tools: {{claude: ["{Path(sys.executable).as_posix()}", "{(SP / 'fakeclaude.py').as_posix()}"]}}
""", encoding="utf-8")
ENV = {**os.environ, "SW_LOCAL": str(T / "local.yaml"), "PYTHONIOENCODING": "utf-8", "USERPROFILE": str(T / "home"),
       "HOME": str(T / "home")}


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


os.environ.update(ENV)
spec = importlib.util.spec_from_file_location("sw", DEV / "harness" / "sw.py")
swm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(swm)
check(swm.model_spec("opus:high") == {"model": "opus", "effort": "high"} and
      swm.model_spec("haiku") == {"model": "haiku", "effort": None} and
      swm.model_spec({"model": "sonnet", "effort": "low"}) == {"model": "sonnet", "effort": "low"}, "model specs parse")
check(swm.player_agent({"model": "sonnet", "effort": "low"}) == "sleepwalker-player-sonnet-low" and
      swm.player_agent({"model": "haiku", "effort": None}) == "sleepwalker-player-haiku", "player agent names")

# claim names the model, the effort and the player agent; onboarding games are never handed out
c = sw("claim")["assignments"][0]
check(c["game"] == G and c["model_role"] == "study" and c["model"] == "opus" and c["effort"] == "high"
      and c["agent"] == "sleepwalker-player-opus-high", f"claim: {c.get('agent')}")
check(any(g["id"] == "com.example.newgame" and g.get("onboarding") for g in swm.games()), "onboarding games are known")
sw("end", "--status", "ok", "--summary", "release")

# install-agents writes one player definition per model and effort
r = sw("install-agents", device=False)
agents = T / "home" / ".claude" / "agents"
v = (agents / "sleepwalker-player-sonnet-low.md").read_text(encoding="utf-8")
check((agents / "sleepwalker-player-haiku.md").exists() and not (agents / "sleepwalker-player-haiku-low.md").exists()
      and "model: sonnet" in v and "effort: low" in v and "name: sleepwalker-player-sonnet-low" in v
      and "runbooks/session.md" in v, f"player definitions per model and effort ({r['installed']})")
d, rv = (agents / "sleepwalker-documenter.md").read_text(encoding="utf-8"), (agents / "sleepwalker-reviewer.md").read_text(encoding="utf-8")
check(d.startswith("---\nname: sleepwalker-documenter") and "\nmodel: opus\neffort: medium\n---" in d
      and "runbooks/document.md" in d and "\nmodel: opus\n---" in rv and r["roles"]["documenter"] == "opus:medium",
      "role definitions carry their model and effort from project.yaml")

# a benchmark: interleaved, rotated slots; haiku takes no effort
r = sw("bench", "new", G, "--variants", "haiku:low", expect_ok=False, device=False)
check("no effort" in json.dumps(r), "haiku with an effort is refused")
plan = sw("bench", "new", G, "--variants", "sonnet:low,opus:medium,haiku", "--rounds", "2", "--levels", "2",
          "--budget", "5", device=False)
order = [s["model"] for s in plan["slots"]]
check(order == ["sonnet", "opus", "haiku", "opus", "haiku", "sonnet"], f"slots interleaved and rotated: {order}")

# run: every slot plays through `claude -p` (a fake here) with its model and effort
r = sw("bench", "run", plan["id"], "--max", "3")
check(len(r["ran"]) == 3 and all(x["status"] == "done" for x in r["ran"]) and r["left"] == 3, f"run 3 slots: {r}")
r = sw("bench", "run", plan["id"])
check(len(r["ran"]) == 3 and r["left"] == 0, "run the rest")
ops = [json.loads(x) for x in (T / "state" / G / "research.jsonl").read_text(encoding="utf-8").splitlines()]
st = [o.get("status") for o in ops if o.get("op") == "mechanic" and o.get("id") == "core"]
check(st == ["studying"], f"benchmark slots never change a mechanic's status nor hand off: {st}")
sess = [json.loads(x) for x in (T / "state" / G / "sessions.jsonl").read_text(encoding="utf-8").splitlines()]
b = [s for s in sess if s.get("bench")]
check(len(b) == 6 and {s["effort"] for s in b if s["model"] == "sonnet"} == {"low"}
      and all(s.get("effort") is None for s in b if s["model"] == "haiku"), "sessions record the model, effort and slot")

# report: per variant, losses sort last, cost from the CLI result
rep = sw("bench", "report", plan["id"], device=False)
t = {x["variant"]: x for x in rep["variants"]}
check(set(t) == {"sonnet:low", "opus:medium", "haiku"} and t["haiku"]["levels_lost"] == 2
      and rep["variants"][-1]["variant"] == "haiku", f"report: {[(x['variant'], x['levels_won'], x['levels_lost']) for x in rep['variants']]}")
check(t["sonnet:low"]["levels_won"] == 4 and t["sonnet:low"]["cost_usd"] == 0.6 and t["opus:medium"]["cost_per_won_usd"] == 0.45,
      f"won levels and cost per variant: {t['sonnet:low']}")
check(t["sonnet:low"]["model_ids"] == ["claude-sonnet-x"], "the report shows the model the CLI really ran")
check(all(x["solve_s_median"] is not None and x["late_starts"] == 0 for x in rep["variants"]),
      "the report times levels from their first move too (solve_s), next to the level time")
check(t["haiku"]["asks"] == 2 and t["haiku"]["cost_usd"] == round(2 * 0.1 + 2 * 0.07, 2),
      f"consultations count in the player's cost: {t['haiku']}")
st = sw("stats", "--by-model", device=False)
check("sonnet:low" in st["by_model"] and "opus:medium" in st["by_model"], "stats tell model and effort apart")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
