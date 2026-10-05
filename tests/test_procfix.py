"""A merged solver reaches the phone; a game whose sessions keep crashing waits."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP, frames_dir  # noqa: E402
import datetime as dt
import importlib.util
import json
import os
import shutil
import time
from pathlib import Path

SP = Path(__file__).resolve().parent
T = TMP / "pftest"
DEV = ROOT
shutil.rmtree(T, ignore_errors=True)
T.mkdir()
G = "com.maroieqrwlk.unpin"
(T / "local.yaml").write_text(f'machine: t\nstate_dir: "{(T / "state").as_posix()}"\nraw_dir: "{(T / "raw").as_posix()}"\n',
                              encoding="utf-8")
os.environ["SW_LOCAL"] = str(T / "local.yaml")
spec = importlib.util.spec_from_file_location("sw", DEV / "harness" / "sw.py")
swm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(swm)


def check(cond, msg):
    print(("OK   " if cond else "FAIL ") + msg)
    if not cond:
        raise SystemExit(1)


merged_dir = DEV / "solvers" / G
made_dir = not merged_dir.exists()
assert not (merged_dir / "tmech.py").exists(), "the test would overwrite a real solver"
try:
    local = T / "state" / G / "solvers" / "tmech.py"
    local.parent.mkdir(parents=True)
    local.write_text("# local draft\n", encoding="utf-8")
    os.utime(local, (time.time() - 3600, time.time() - 3600))
    check(swm.solver_path(G, "tmech") == local and "draft" in local.read_text(), "only a local solver: it runs")
    merged_dir.mkdir(parents=True, exist_ok=True)  # solvers/<game>/ exists once a solver of the game is published
    merged = merged_dir / "tmech.py"
    merged.write_text("# merged fix\n", encoding="utf-8")
    p = swm.solver_path(G, "tmech")
    check(p == local and "merged fix" in local.read_text() and "draft" in (local.parent / "tmech.prev.py").read_text(),
          "a newer merged solver replaces the local draft, which is kept as .prev.py")
    time.sleep(0.05)
    local.write_text("# the lab's newer work\n", encoding="utf-8")
    swm.solver_path(G, "tmech")
    check("lab's newer work" in local.read_text(), "a local solver newer than the merged one is kept")
    check(swm.solver_path(G, "nothing") is None, "no solver at all: None")
finally:
    (merged_dir / "tmech.py").unlink(missing_ok=True)
    if made_dir:
        shutil.rmtree(merged_dir, ignore_errors=True)

now = time.time()


def sessions(*rows):
    p = T / "state" / G / "sessions.jsonl"
    p.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")


def ago(h):
    return dt.datetime.fromtimestamp(now - h * 3600).isoformat(timespec="seconds")


sessions({"started": ago(5), "minutes": 30, "status": "ok"}, {"started": ago(3), "minutes": 10, "status": "crashed",
                                                               "summary": "API error: output blocked"})
check(swm.crash_loop(G, now) is None, "one crash: the game is handed out")
sessions({"started": ago(5), "minutes": 30, "status": "crashed"},
         {"started": ago(3), "minutes": 10, "status": "crashed", "summary": "API error: output blocked"})
r = swm.crash_loop(G, now)
check(r and "output blocked" in r and "waits until" in r, f"two crashes in a row: the game waits ({r})")
sessions({"started": ago(20), "minutes": 30, "status": "crashed"}, {"started": ago(14), "minutes": 10, "status": "abandoned"})
check(swm.crash_loop(G, now) is None, "after crash_backoff_hours the game is tried again")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
