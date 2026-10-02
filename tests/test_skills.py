"""skill new: each step's wait from the transcript, --wait overrides, a precondition on a region of the frame;
skill run reports how long it waited."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP  # noqa: E402
import importlib.util
import json
import os
import random
import shutil
import subprocess
import sys
import time

import yaml
from PIL import Image, ImageDraw

T = TMP / "sktest"
DEV = ROOT
shutil.rmtree(T, ignore_errors=True)
T.mkdir()
G = "com.block.juggle"


def frame(seed: int, gear: bool) -> Image.Image:
    """A board of random blocks that is never the same, with the gear (or another control) at the top right."""
    rnd = random.Random(seed)
    img = Image.new("RGB", (1080, 2340), tuple(rnd.randrange(256) for _ in range(3)))
    d = ImageDraw.Draw(img)
    for _ in range(14):
        x, y = rnd.randrange(0, 900), rnd.randrange(300, 2200)
        d.rectangle((x, y, x + rnd.randrange(150, 500), y + rnd.randrange(150, 600)),
                    fill=tuple(rnd.randrange(256) for _ in range(3)))
    d.rectangle((918, 70, 1080, 281), fill=(250, 250, 250))
    if gear:
        d.ellipse((950, 110, 1050, 210), outline=(20, 20, 20), width=18)
        d.rectangle((993, 85, 1007, 235), fill=(20, 20, 20))
        d.rectangle((925, 153, 1075, 167), fill=(20, 20, 20))
    else:
        d.polygon([(930, 250), (1000, 90), (1070, 250)], fill=(200, 30, 30))
    return img


kf = T / "kframes"
kf.mkdir()
for i, (seed, gear) in enumerate(((1, True), (2, False), (3, True))):  # a board, Settings, another board
    frame(seed, gear).save(kf / f"k{i}.png")
(T / "local.yaml").write_text(f"""machine: testbox
games: [{G}]
android: {{serials: [nophone]}}
fake_devices: {{fake1: "{kf.as_posix()}"}}
video: {{record: false}}
state_dir: "{(T / 'state').as_posix()}"
raw_dir: "{(T / 'raw').as_posix()}"
wiki_dir: "{(T / 'gwiki').as_posix()}"
""", encoding="utf-8")
ENV = {**os.environ, "SW_LOCAL": str(T / "local.yaml"), "PYTHONIOENCODING": "utf-8"}


def sw(*a, device=True):
    r = subprocess.run([sys.executable, str(DEV / "harness" / "sw.py"), *(["-d", "fake1"] if device else []), *a],
                       capture_output=True, text=True, encoding="utf-8", env=ENV, cwd=DEV)
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


# a transcript: the video button, a 30 s wait, the ad's close cross, Next Level, Back
H = "94e225eb6b8c529d"
SID = "20261001-054205-testbox-fake1"
tap = {"type": "tap", "model_size": [730, 1583], "settle": 1.0, "hash": H}
rows = [{"t": 1000.0, "step": 52, "type": "shot", "shot": 10, "hash": H},
        {**tap, "t": 1002.0, "step": 53, "x": 224, "y": 1083, "shot": 11},
        {"t": 1020.0, "step": 53, "type": "note", "kind": "ui", "text": "a rewarded video"},
        {"t": 1036.5, "step": 53, "type": "wait", "seconds": 30, "shot": 12, "hash": H},
        {**tap, "t": 1040.0, "step": 54, "x": 46, "y": 109, "shot": 13},
        {**tap, "t": 1043.2, "step": 55, "x": 364, "y": 1270, "shot": 14},
        {"t": 1047.0, "step": 56, "type": "key", "key": "back", "settle": 1.0, "shot": 15, "hash": H}]
(T / "raw" / G / SID).mkdir(parents=True)
(T / "raw" / G / SID / "steps.jsonl").write_bytes("".join(json.dumps(r) + "\n" for r in rows).encode("utf-8"))
out = T / "skills"
r = ok("skill", "new", G, "jump", "--session", SID, "--steps", "53-56", "--desc", "t", "--out", str(out), device=False)
sk = yaml.safe_load((out / "jump.yaml").read_text(encoding="utf-8"))
check([s["wait"] for s in sk["steps"]] == [38.0, 3.5, 4.0, 1.5] == r["waits"],
      f"waits from the transcript: the step before the video waits it out, the others 3-4 s, the last settle+0.5: {r['waits']}")
r = ok("skill", "new", G, "jump", "--session", SID, "--steps", "53-56", "--desc", "t", "--out", str(out),
       "--wait", "55:2.5", device=False)
check(r["waits"] == [38.0, 3.5, 2.5, 1.5], f"--wait STEP:SECONDS overrides one step: {r['waits']}")
for bad in ("57:3", "54:0", "54", "54:99", "x:3"):
    rc, r = sw("skill", "new", G, "jump", "--session", SID, "--steps", "53-56", "--desc", "t", "--out", str(out),
               "--wait", bad, device=False)
    check(rc == 2 and "--wait" in r["error"], f"--wait {bad} is refused: {r['error']}")
spec = importlib.util.spec_from_file_location("sw", DEV / "harness" / "sw.py")
os.environ["SW_LOCAL"] = str(T / "local.yaml")
swm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(swm)
check(swm.skill_waits([{"t": 0, "step": 1, "settle": 1.0}, {"t": 500, "step": 2, "settle": 1.0}], {}) == [60.0, 1.5],
      "a wait is at most 60 s")
check(swm.skill_waits([{"t": 0, "step": 1, "settle": 2.0}, {"t": 0.2, "step": 2, "settle": 1.0}], {})[0] == 2.5,
      "never less than the action's settle + 0.5")

# a skill that starts on a board: the precondition is the gear's region, not the whole frame
sdir = DEV / "skills" / G
made = not sdir.exists()
assert not list(sdir.glob("zz-test-*.yaml")), "the test would overwrite a skill"
try:
    s1 = ok("start", G)["session"]
    ok("tap", "672", "119", "--why", "the gear opens Settings")
    ok("end", "--status", "ok", "--summary", "settings")
    rc, r = sw("skill", "new", G, "zz-test-gear", "--session", s1, "--steps", "1-1", "--desc", "x", "--out", str(sdir),
               "--pre-region", "0.9,0.1,0.8,0.2", device=False)
    check(rc == 2 and "--pre-region" in r["error"], "a malformed region is refused")
    r = ok("skill", "new", G, "zz-test-gear", "--session", s1, "--steps", "1-1", "--desc", "Open Settings", "--out",
           str(sdir), "--pre-region", "0.85,0.03,1,0.12", device=False)
    sk = yaml.safe_load((sdir / "zz-test-gear.yaml").read_text(encoding="utf-8"))
    check(sk["pre_region"] == [0.85, 0.03, 1.0, 0.12] and sk["pre_hash"] != rows[0]["hash"], "the skill keeps its region")
    ok("skill", "new", G, "zz-test-whole", "--session", s1, "--steps", "1-1", "--desc", "x", "--out", str(sdir), device=False)
    time.sleep(1.1)
    ok("start", G)
    ok("tap", "10", "10", "--why", "x")
    ok("tap", "10", "10", "--why", "another board")
    rc, r = sw("skill", "run", "zz-test-gear", "--why", "open", "Settings")
    check(rc == 0 and r["waited_s"] == 1.5, f"on another board the gear's region matches: the skill runs ({rc}, {r})")
    st = [json.loads(x) for x in open(next((T / "state" / G).glob("skills.jsonl")), encoding="utf-8")]
    check(st[-1]["waited_s"] == 1.5, "skills.jsonl keeps waited_s for the dream")
    ok("tap", "10", "10", "--why", "x")
    ok("tap", "10", "10", "--why", "another board")
    rc, r = sw("skill", "run", "zz-test-whole", "--why", "x")
    check(rc == 5 and "not the screen the skill starts from" in r["error"],
          "without a region the whole board must match, and another board does not")
    ok("end", "--status", "ok", "--summary", "skills")
finally:
    for p in sdir.glob("zz-test-*.yaml"):
        p.unlink()
    if made:
        shutil.rmtree(sdir, ignore_errors=True)
print("all ok")
shutil.rmtree(T, ignore_errors=True)
