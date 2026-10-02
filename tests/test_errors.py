"""Refused and failed commands become error steps of the session; forgiving arguments that never do something else."""
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

T = TMP / "errtest"
DEV = ROOT
shutil.rmtree(T, ignore_errors=True)
T.mkdir()
G = "com.maroieqrwlk.unpin"
PY = Path(sys.executable).as_posix()
BASE = f"""machine: testbox
games: [{G}]
android: {{serials: [nophone]}}
fake_devices: {{fake1: "{frames_dir().as_posix()}"}}
video: {{record: false}}
state_dir: "{(T / 'state').as_posix()}"
raw_dir: "{(T / 'raw').as_posix()}"
wiki_dir: "{(T / 'gwiki').as_posix()}"
"""
# a consultant that never answers in time, and one that says whether the prompt carries the session rules
(T / "slow.yaml").write_text(BASE + f'consult: {{timeout_s: 1}}\ntools: {{claude: ["{PY}", "-c", "import time; time.sleep(8)"]}}\n',
                             encoding="utf-8")
(T / "rules.py").write_text("import json, sys\np = sys.argv[sys.argv.index('-p') + 1]\n"
                            "print(json.dumps({'result': 'RULES' if 'never opens payment sheets' in p else 'NO RULES'}))\n",
                            encoding="utf-8")
(T / "local.yaml").write_text(BASE + f'tools: {{claude: ["{PY}", "{(T / "rules.py").as_posix()}"]}}\n', encoding="utf-8")
ENV = {**os.environ, "SW_LOCAL": str(T / "local.yaml"), "PYTHONIOENCODING": "utf-8"}


def sw(*a, env=ENV, device=True):
    """(exit code, the JSON reply or the raw output)"""
    r = subprocess.run([sys.executable, str(DEV / "harness" / "sw.py"), *(["-d", "fake1"] if device else []), *a],
                       capture_output=True, text=True, encoding="utf-8", env=env, cwd=DEV)
    try:
        return r.returncode, json.loads(r.stdout)
    except json.JSONDecodeError:
        return r.returncode, r.stdout + r.stderr


def ok(*a, **k):
    rc, res = sw(*a, **k)
    if rc != 0:
        raise SystemExit(f"FAIL {a}: {res}")
    return res


def check(cond, msg):
    print(("OK   " if cond else "FAIL ") + msg)
    if not cond:
        raise SystemExit(1)


def steps():
    return [json.loads(x) for x in open(next((T / "raw" / G).glob("*/steps.jsonl")), encoding="utf-8")]


def errors():
    return [s for s in steps() if s["type"] == "error"]


sid = ok("start", G)["session"]
r = ok("tap", "10,10", "--why", "test", "tap")
s = steps()[-1]
check(s["type"] == "tap" and (s["x"], s["y"]) == (10.0, 10.0) and s["why"] == "test tap",
      f"tap X,Y works, and --why takes several words without quotes: {s.get('why')!r}")
ok("tap", "12", "12", "--why", "the usual way")
check(steps()[-1]["type"] == "tap" and not errors(), "tap X Y still works; nothing refused so far")

rc, r = sw("tap", "10", "--why", "a", "secret", "reason")
e = errors()
check(rc == 2 and "X Y or X,Y" in json.dumps(r) and len(e) == 1, f"tap with one number is refused: {r}")
check(e[0]["cmd"] == "tap 10 --why …" and "X Y or X,Y" in e[0]["text"] and e[0]["code"] == 2
      and "secret" not in json.dumps(e[0]) and e[0]["seconds"] >= 0 and e[0]["since_prev_s"] >= 0,
      f"the refusal is an error step: the command without the --why text, the message, seconds: {e[0]}")
check(e[0]["step"] == steps()[-2]["step"], "an error step does not take a step number of its own")
for bad in (("10,10", "20"), ("10,10,10",), ("10;10",)):
    rc, r = sw("tap", *bad, "--why", "x")
    check(rc == 2 and "X Y or X,Y" in json.dumps(r), f"a slip never taps somewhere else: tap {' '.join(bad)} refused")
rc, r = sw("tap", "10", "20", "30", "--why", "x")
check(rc == 2 and "unrecognized arguments: 30" in errors()[-1]["text"], "an argparse error is an error step too")
rc, r = sw("restart", "--why")
check(rc == 2 and errors()[-1]["cmd"] == "restart --why …", "a missing --why text: refused and logged")
n = len(errors())

r = ok("launch", "--why", "back", "to", "the", "game")
check(steps()[-1]["type"] == "launch" and steps()[-1]["why"] == "back to the game", "launch takes --why")
ok("shot", "--why", "look again")
ok("wait", "0.2", "--why", "the ad timer")
check([x.get("why") for x in steps()[-2:]] == ["look again", "the ad timer"], "shot and wait take --why")
ok("shot")
check("why" not in steps()[-1], "--why stays optional on shot")
ok("restart", "--why", "next", "level")
check(steps()[-1]["why"] == "next level", "restart --why in several words")
check(len(errors()) == n, "the forgiving forms leave no error steps")

# mark --frame N marks that frame, not the last one
ok("tap", "20", "20", "--why", "x")
r = ok("mark", "Earlier", "the frame before", "--frame", "1", "--feature", "map", "--as", "screen", "--at", "5,5")
m = steps()[-1]
check(m["type"] == "mark" and m["shot"] == 1 and m["file"].endswith("shots/00001.jpg") and m["model_size"] == [730, 1583],
      f"mark --frame 1 marks shot 1 with its size: {m['shot']} {m['file'][-20:]}")
rc, r = sw("mark", "x", "y", "--frame", "999")
check(rc == 2 and "no frame 999" in json.dumps(r) and "no frame 999" in errors()[-1]["text"], "an unknown frame is refused")

# task done --new-entries: a count, or names that are counted; numbers in a list are refused
ok("task", "add", "scout-1", "Map the game", "--kind", "scout")
rc, r = sw("task", "done", "scout-1", "--new-entries", "2,3")
check(rc == 2 and "--new-entries" in errors()[-1]["text"], "--new-entries 2,3 is refused, not counted as two")
ok("task", "done", "scout-1", "--new-entries", "Shop, Leagues", "--note", "two new")
v = yaml.safe_load(ok("research", G, device=False))
t = next(x for x in v["tasks"] if x["id"] == "scout-1")
check(t["new_entries"] == 2 and t["new_entry_names"] == ["Shop", "Leagues"], f"names are counted and kept: {t}")
ok("task", "add", "scout-2", "Map again", "--kind", "scout")
ok("task", "done", "scout-2", "--new-entries", "0", "--note", "nothing new")
v = yaml.safe_load(ok("research", G, device=False))
check(next(x for x in v["tasks"] if x["id"] == "scout-2")["new_entries"] == 0, "a count still works")

# the review's and the dream's commands never land in a player's session
n = len(errors())
rc, r = sw("task", "done", "scout-1", "--game", G, "--new-entries", "2,3", device=False)
rc2, r2 = sw("skill", "new", G, "x", "--session", "nosuch", "--steps", "1-2", "--desc", "x", "--out", str(T / "sk"),
             device=False)
check(rc == 2 and rc2 == 2 and len(errors()) == n, "a refused command with --game or skill new is not the player's error")

# ask: the session rules are in the prompt; a timeout is fast, says how long it waited and is logged
r = ok("ask", "which pin first?")
check(r["answer"] == "RULES", "the consultant's prompt carries the session rules (no ads, no payment sheets)")
t0 = time.time()
rc, r = sw("ask", "which pin first?", env={**ENV, "SW_LOCAL": str(T / "slow.yaml")})
e = errors()[-1]
check(rc == 2 and time.time() - t0 < 7 and "within 1 s" in r["error"] and r["seconds"] >= 1,
      f"ask times out at consult.timeout_s and says how long it waited: {r}")
check(e["cmd"].startswith("ask") and "within 1 s" in e["text"] and e["seconds"] >= 1, f"the timeout is an error step: {e}")
import importlib.util  # noqa: E402
spec = importlib.util.spec_from_file_location("sw_defaults", DEV / "harness" / "sw.py")
swd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(swd)
check(swd.LOCAL_DEFAULTS["consult"]["timeout_s"] == 90, "the default consult timeout is 90 s")

# stats and the session record count them
n = len(errors())
ok("end", "--status", "ok", "--summary", "errors")
meta = json.loads((T / "raw" / G / sid / "session.json").read_text(encoding="utf-8"))
st = ok("stats", G, device=False)["games"][G]["sessions"][0]
check(meta["errors"] == n == st["errors"] and st["error_minutes"] >= 0 and meta["error_minutes"] == st["error_minutes"],
      f"session.json and stats count the errors: {meta['errors']} / {st['errors']}, {st['error_minutes']} min")
rc, r = sw("tap", "10", "--why", "x")
check(rc == 2 and len(errors()) == n, "no session: nothing to log into, the refusal still comes back")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
