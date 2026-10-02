"""A stand-in for `claude -p` in tests: plays a benchmark slot through sw.py and prints a JSON result."""
import json
import re
import subprocess
import sys
from pathlib import Path

args = sys.argv[1:]
brief = args[args.index("-p") + 1]
model = args[args.index("--model") + 1]
effort = args[args.index("--effort") + 1] if "--effort" in args else None
if brief.startswith("You advise an agent"):  # sw.py ask: a consultation
    print(json.dumps({"type": "result", "is_error": False, "result": "Tap (10, 10).", "total_cost_usd": 0.07}))
    sys.exit(0)
m = re.search(r"-d (\S+) start (\S+) --model \S+(?: --effort \S+)? --bench (\S+) --budget (\d+)", brief)
dev, game, bench, budget = m.groups()
levels = int(re.search(r"play (\d+) levels", brief).group(1))
SW = [sys.executable, str(Path(__file__).resolve().parents[1] / "harness" / "sw.py"), "-d", dev]


def sw(*a):
    r = subprocess.run(SW + list(a), capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        print(json.dumps({"is_error": True, "result": r.stdout[-300:] + r.stderr[-300:]}))
        sys.exit(1)
    return r.stdout


sw("start", game, "--model", model, *(["--effort", effort] if effort else []), "--bench", bench, "--budget", budget)
for i in range(1, levels + 1):
    o = sw("level", "start", f"level {i}", "--value", str(i), "--mechanic", "core", "--plan", "by the playbook")
    if '"handoff"' in o:  # a benchmark slot must never be told to hand off
        print(json.dumps({"is_error": True, "result": "handoff in a benchmark slot: " + o[-300:]}))
        sys.exit(1)
    if i == 1:
        bad = subprocess.run(SW + ["mechanic", "core", "--status", "broken"], capture_output=True, text=True)
        if bad.returncode == 0:
            print(json.dumps({"is_error": True, "result": "a bench slot changed a mechanic's status"}))
            sys.exit(1)
    sw("taps", "10,10 20,20", "--why", "moves")
    if model == "haiku" and i == 2:
        sw("ask", "which pin first?")
    sw("shot")  # the win screen before level end
    sw("level", "end", "lost" if model == "haiku" and i == 1 else "won", "--note", "x")
sw("end", "--status", "ok", "--summary", f"bench slot: {levels} levels")
print(json.dumps({"type": "result", "is_error": False, "num_turns": 7, "duration_ms": 1234,
                  "total_cost_usd": {"opus": 0.9, "sonnet": 0.3, "haiku": 0.1}.get(model, 0.5),
                  "modelUsage": {f"claude-{model}-x": {}}}))
