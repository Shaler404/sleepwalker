"""Run every test suite: python tests/run.py [name ...]. Exit code 1 when any suite fails."""
import os
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
names = sys.argv[1:] or sorted(p.stem for p in HERE.glob("test_*.py"))
env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
bad = []
for n in names:
    t0 = time.time()
    r = subprocess.run([sys.executable, str(HERE / f"{n}.py")], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=env)
    oks, fails = r.stdout.count("\nOK ") + r.stdout.startswith("OK "), r.stdout.count("FAIL")
    ok = r.returncode == 0
    print(f"{'ok  ' if ok else 'FAIL'} {n}: {oks} checks, {round(time.time() - t0)} s")
    if not ok:
        bad.append(n)
        print("\n".join((r.stdout + r.stderr).strip().splitlines()[-15:]))
print(f"{len(names) - len(bad)} of {len(names)} suites pass" + (f"; failing: {', '.join(bad)}" if bad else ""))
sys.exit(1 if bad else 0)
