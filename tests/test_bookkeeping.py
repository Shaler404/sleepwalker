"""Session bookkeeping: orphan raw sessions are adopted, a stopped bench slot is ended, waits log what they slept,
footnotes get the video links of originals uploaded later."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP, frames_dir  # noqa: E402
import argparse
import contextlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

import yaml

T = TMP / "bktest"
DEV = ROOT
shutil.rmtree(T, ignore_errors=True)
T.mkdir()
G = "com.maroieqrwlk.unpin"
(T / "local.yaml").write_text(f"""machine: testbox
games: [{G}]
android: {{serials: [nophone]}}
fake_devices: {{fake1: "{frames_dir().as_posix()}"}}
video: {{record: false}}
youtube: {{enabled: true, uploads_per_gc: 2}}
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


def rows():
    return [json.loads(x) for x in (T / "state" / G / "sessions.jsonl").read_text(encoding="utf-8").splitlines()]


def orphan(back_s: float) -> str:
    """A session whose process died: steps, no session.json, no session file, the steps back_s seconds old."""
    sid = sw("start", G)["session"]
    sw("tap", "10", "10", "--why", "x")
    sw("level", "start", "level 3", "--mechanic", "pins", "--plan", "x")
    sw("taps", "10,10 20,20 30,30", "--why", "three moves")
    SESS.unlink()
    p = T / "raw" / G / sid / "steps.jsonl"
    old = [{**s, "t": s["t"] - back_s} for s in map(json.loads, p.read_text(encoding="utf-8").splitlines())]
    p.write_bytes("".join(json.dumps(s) + "\n" for s in old).encode("utf-8"))
    time.sleep(1.1)  # session ids are per second
    return sid


# a session nobody ended is adopted by claim: recorded as abandoned from its steps, then listed for the dream
sid = orphan(3600)
check(not any(p["id"] == sid for p in sw("pending", device=False)["pending"]), "an orphan is invisible to pending")
c = sw("claim")
check(c.get("adopted") == [sid], f"claim adopts it: {c.get('adopted')}")
meta = json.loads((T / "raw" / G / sid / "session.json").read_text(encoding="utf-8"))
row = next(r for r in rows() if r["id"] == sid)
check(row["status"] == "abandoned" and row["steps"] == 2 and row["moves"] == 4 and row["minutes"] < 5
      and row["device"] == "fake1" and row["youtube"] is None and meta["levels"] == {"won": 0, "lost": 0, "won_s_median": None},
      f"its record: steps, moves, its own length (not until now), the device from the id: {row}")
check(abs(os.path.getmtime(T / "raw" / G / sid / "session.json") - (time.time() - 3600)) < 120,
      "session.json is dated at the session's end: gc keeps the original for keep_originals_days from there")
v = yaml.safe_load(sw("research", G, device=False))
m = next(x for x in v["mechanics"] if x["id"] == "pins")
check(m["levels"].get("quit") == 1, "the level it left open counts as quit, as at a normal end")
check(any(p["id"] == sid for p in sw("pending", device=False)["pending"]), "pending lists it now")
check(sw("claim").get("adopted") is None, "adopted once only")
sw("end", "--status", "ok", "--summary", "release the reservation", expect_ok=False)

# a fresh one (younger than session.stale_min) and a live one are left alone
young = orphan(60)
live = sw("start", G)["session"]
lp = T / "raw" / G / live / "steps.jsonl"
lp.write_bytes("".join(json.dumps({**json.loads(x), "t": json.loads(x)["t"] - 3600}) + "\n"
                       for x in lp.read_text(encoding="utf-8").splitlines()).encode("utf-8"))
check(sw("gc", device=False).get("adopted") is None and not (T / "raw" / G / young / "session.json").exists(),
      "a session whose last step is younger than stale_min is not adopted, nor a live one")
sw("end", "--status", "ok", "--summary", "live")
shutil.rmtree(T / "raw" / G / young)

# stop on a bench slot ends the session itself: its `claude -p` may be gone
bsid = sw("start", G, "--bench", "b1:1", "--budget", "10")["session"]
sw("tap", "10", "10", "--why", "x")
r = sw("stop")
bmeta = json.loads((T / "raw" / G / bsid / "session.json").read_text(encoding="utf-8"))
check(not SESS.exists() and bmeta["status"] == "interrupted" and bmeta["bench"] == "b1:1" and "ended" in r["devices"][0]["session"],
      f"stop ends a bench slot (interrupted): {r['devices'][0]['session']}")
sw("resume")

# in-process: waits, a command in flight after the end, gc with the uploads and the footnotes
os.environ["SW_LOCAL"] = str(T / "local.yaml")
spec = importlib.util.spec_from_file_location("sw", DEV / "harness" / "sw.py")
swm = importlib.util.module_from_spec(spec)
sys.modules["sw"] = swm  # youtube.upload_pending imports it
spec.loader.exec_module(swm)
swm.save_session({"id": bsid, "device": "fake1", "dir": str(T / "raw" / G / bsid), "status": "active", "step": 1})
check(not SESS.exists(), "a command in flight after the session ended does not bring its file back")


def call(fn, **kw):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn(argparse.Namespace(**kw))
    return json.loads(buf.getvalue())


wsid = sw("start", G)["session"]
slept, real_sleep = [], swm.time.sleep
swm.time.sleep = lambda s: slept.append(s)
try:
    r = call(swm.cmd_wait, device="fake1", seconds=280, hi=False, why=None)
    r2 = call(swm.cmd_wait, device="fake1", seconds=5, hi=False, why="the ad timer")
finally:
    swm.time.sleep = real_sleep
st = [json.loads(x) for x in (T / "raw" / G / wsid / "steps.jsonl").read_text(encoding="utf-8").splitlines()][-2:]
check(slept == [60, 5] and (r["seconds"], r["asked"], r["capped"]) == (60, 280, 60) and "shot_n" in r,
      f"wait 280 sleeps 60 and the reply says so: {r['seconds']}, asked {r['asked']}, capped {r['capped']}")
check((st[0]["seconds"], st[0]["asked"], st[0]["capped"]) == (60, 280, 60) and "asked" not in r2
      and st[1]["seconds"] == 5 and "asked" not in st[1], "the step logs the seconds slept; a short wait is not capped")
sw("end", "--status", "ok", "--summary", "waits")


def fake_session(sid: str, youtube=None, original=True):
    d = T / "raw" / G / sid
    d.mkdir(parents=True)
    (d / "steps.jsonl").write_bytes("".join(json.dumps({"t": 1000.0 + i, "step": i, "type": "tap"}) + "\n"
                                            for i in range(5)).encode("utf-8"))
    (d / "session.json").write_text(json.dumps({"id": sid, "game": G, "youtube": youtube}), encoding="utf-8")
    if original:
        (d / "original.mkv").write_bytes(b"x" * 1000)


A, C = "20261001-100000-testbox-fake1", "20261001-120000-testbox-fake1"
fake_session(A)
fake_session(C)
O = orphan(7200)
(T / "raw" / G / O / "original.mkv").write_bytes(b"x" * 1000)
check(O > C, "the orphan sorts after the two others")
pages = T / "state" / G / "pages" / "features"
pages.mkdir(parents=True)
page = (f"---\ngame: {G}\n---\n# Shop\n\nOpens from the map.[^s1] Tabs.[^s2] Prices.[^s3]\n\n"
        f"[^s1]: session {A}, step 2\n[^s2]: session {C}, step 3\n[^s3]: session {O}, step 2\n[^s4]: a note\n")
(pages / "shop.md").write_bytes(page.encode("utf-8"))
import youtube  # noqa: E402

ups = []
youtube.upload = lambda path, title, desc, cfg: ups.append(path.parent.name) or f"VID{len(ups)}"
r = call(swm.cmd_gc)
s = (pages / "shop.md").read_text(encoding="utf-8")
check(r.get("adopted") == [O], f"gc adopts an orphan too: {r.get('adopted')}")
check(ups == [A, C] and [u["session"] for u in r["youtube"]] == [A, C],
      f"youtube.uploads_per_gc from local.yaml: 2 of the 3 originals go up: {ups}")
check(f"[^s1]: session {A}, step 2 — [video at 0:02](https://youtu.be/VID1?t=2)" in s
      and f"[^s2]: session {C}, step 3 — [video at 0:03](https://youtu.be/VID2?t=3)" in s
      and f"[^s3]: session {O}, step 2\n" in s and r["pages_linked"] == {str(pages / "shop.md"): 2},
      "the footnotes of the uploaded sessions get their links; the others wait")
check(s.replace(" — [video at 0:02](https://youtu.be/VID1?t=2)", "").replace(" — [video at 0:03](https://youtu.be/VID2?t=3)", "")
      == page, "nothing else on the page changes")
r = call(swm.cmd_gc)
s = (pages / "shop.md").read_text(encoding="utf-8")
check(ups == [A, C, O] and "youtu.be/VID3" in s and json.loads((T / "raw" / G / O / "session.json").read_text())["youtube"] == "VID3",
      "the adopted orphan's original goes up on the next run, and its footnote gets the link")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
