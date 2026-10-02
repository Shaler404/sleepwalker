"""Screen change by two measures (the perceptual hash and the share of changed pixels) and the batch guard."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP  # noqa: E402
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw

T = TMP / "frtest"
shutil.rmtree(T, ignore_errors=True)
(T / "frames").mkdir(parents=True)
G = "com.maroieqrwlk.unpin"


def check(cond, msg):
    print(("OK   " if cond else "FAIL ") + msg)
    if not cond:
        raise SystemExit(1)


def board(removed=(), ad=False, clock=0):
    """A 1080x2340 board of 48 tiles; `removed` tiles are gone, `ad` covers it, `clock` changes the status bar."""
    img = Image.new("RGB", (1080, 2340), (30, 90, 60))
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 1080, 90), fill=(0, 0, 0))
    d.rectangle((900, 20, 900 + 30 * clock, 70), fill=(255, 255, 255))
    if ad:
        d.rectangle((0, 300, 1080, 2340), fill=(240, 220, 40))
        return img
    for i in range(48):
        if i not in removed:
            x, y = 60 + i % 6 * 165, 500 + i // 6 * 200
            d.rectangle((x, y, x + 140, y + 180), fill=((i * 53) % 200 + 40, (i * 97) % 200 + 40, 200))
    return img


# the fake phone shows these in order, one more per move
seq = [board(), board((5,)), board((5, 20)), board((5, 20, 33)), board(ad=True)]
for n, img in enumerate(seq):
    img.save(T / "frames" / f"f{n:02d}.png")
(T / "local.yaml").write_text(f"""machine: testbox
games: [{G}]
android: {{serials: [nophone]}}
fake_devices: {{fake1: "{(T / 'frames').as_posix()}"}}
video: {{record: false}}
state_dir: "{(T / 'state').as_posix()}"
raw_dir: "{(T / 'raw').as_posix()}"
wiki_dir: "{(T / 'gwiki').as_posix()}"
""", encoding="utf-8")
ENV = {**os.environ, "SW_LOCAL": str(T / "local.yaml"), "PYTHONIOENCODING": "utf-8"}
os.environ.update(ENV)
spec = importlib.util.spec_from_file_location("sw", ROOT / "harness" / "sw.py")
swm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(swm)
from perception import changed_share, hash_distance, screen_hash  # noqa: E402


def sw(*a):
    r = subprocess.run([sys.executable, str(ROOT / "harness" / "sw.py"), "-d", "fake1", *a], capture_output=True,
                       text=True, encoding="utf-8", env=ENV, cwd=ROOT)
    if r.returncode != 0:
        raise SystemExit(f"FAIL {a}: {r.stdout}\n{r.stderr}")
    return json.loads(r.stdout)


# the measure itself
hd = [hash_distance(screen_hash(a), screen_hash(b)) for a, b in zip(seq[:3], seq[1:4])]
check(all(d <= 10 for d in hd), f"one tile gone: the hash calls the frames the same ({hd} bits)")
sh = [changed_share(a, b) for a, b in zip(seq[:3], seq[1:4])]
check(all(s >= swm.SAME_SHARE for s in sh), f"... the changed pixels do not: {sh}")
check(changed_share(seq[0], seq[0]) == 0 and changed_share(board(), board(clock=3)) == 0,
      "the same frame and a status bar change (the clock) are no change")
check(changed_share(seq[3], seq[4]) > swm.BIG_CHANGE, "an ad over the board changes most of the frame")

# a session: a level being played is a small change, never stuck; an idle screen is the same by both measures
s = sw("start", G)
r = sw("shot")
check(r["same_as_prev"] and r["changed"] == 0, f"nothing moved: same by both measures ({r['changed']})")
for n in (1, 2, 3):
    r = sw("tap", "100", "100", "--why", "a pair of tiles")
    check(not r["same_as_prev"] and r["same_streak"] == 0 and r["changed"] >= swm.SAME_SHARE,
          f"tile {n} gone: not the same screen (changed {r['changed']})")
check(r.get("small_change") == "3 steps" and not any("unchanged" in w or "stuck" in w for w in r.get("warnings", [])),
      f"three small changes in a row: reported as a small change, no stuck warning: {r.get('small_change')}")
for _ in range(3):
    r = sw("shot")
check(r["same_streak"] == 3 and any("unchanged for 3 steps" in w for w in r.get("warnings", [])),
      "three frames the same by both measures: the unchanged warning")
r = sw("tap", "100", "100", "--why", "the last pair")
check(not r["same_as_prev"] and r["changed"] > swm.BIG_CHANGE and "small_change" not in r, "an ad: a big change")
steps = [json.loads(x) for x in open(Path(s["shot"]).parents[1] / "steps.jsonl", encoding="utf-8")]
taps = [x for x in steps if x["type"] == "tap"]
check(all("changed" in x and "same" in x for x in taps) and [bool(x.get("small")) for x in taps] == [True] * 3 + [False],
      "the step records keep both measures and mark the small changes")
sw("end", "--status", "ok", "--summary", "frames")
st = sw("stats", G)["games"][G]["sessions"][-1]
check(st["same_screen_rate"] == 0 and st["small_change_rate"] == 0.75,
      f"stats: same_screen_rate by both measures, small_change_rate: {st['same_screen_rate']}, {st['small_change_rate']}")


# the batch guard: a long batch looks every 5 moves and stops when most of the frame changed
class Dev:
    def __init__(self, frames, switch_at=None):
        self.frames, self.switch_at, self.taps = frames, switch_at, 0

    def tap(self, x, y):
        self.taps += 1

    def screenshot(self):
        if self.switch_at is not None and self.taps >= self.switch_at:
            return seq[4]
        return self.frames[min(self.taps // 4, len(self.frames) - 1)]


cur = {"device": "fake1", "game": G, "platform": "fake"}
moves = [(10, 10)] * 15
d = Dev(seq[:4], switch_at=6)
done, why = swm.run_moves(cur, d, moves, 1.0, 0)
check(done == 10 and why == "the screen changed a lot after move 10: look before the rest",
      f"an ad after move 6: the batch stops at the next look: {done}, {why}")
d = Dev(seq[:4])
done, why = swm.run_moves(cur, d, moves, 1.0, 0)
check(done == 15 and why is None, "tiles going one by one: the whole batch is played")
d = Dev(seq[:4], switch_at=0)
done, why = swm.run_moves(cur, d, moves[:10], 1.0, 0)
check(done == 10 and why is None, "a batch of 10 is not looked at")


def lit(rows):
    """The board with bands of it lit, like cells an Akari batch lights: a third of the frame per band."""
    img = board()
    for r in rows:
        ImageDraw.Draw(img).rectangle((0, 300 + r * 700, 1080, 1000 + r * 700), fill=(240, 220, 40))
    return img


bands = [lit(()), lit((0,)), lit((0, 1)), lit((0, 1, 2))]
check(all(changed_share(a, b) < swm.BIG_CHANGE for a, b in zip(bands, bands[1:]))
      and changed_share(bands[0], bands[2]) > swm.BIG_CHANGE, "precondition: each band a third, two bands most")
d = Dev([bands[0]] * 4 + [bands[1]] * 5 + [bands[2]] * 5 + [bands[3]] * 5)
d.screenshot = lambda: d.frames[min(d.taps, len(d.frames) - 1)]
done, why = swm.run_moves(cur, d, [(10, 10)] * 16, 1.0, 0)
check(done == 16 and why is None, f"a board that changes a third at a time is played to the end: {done}, {why}")
shots = T / "lk" / "shots"
shots.mkdir(parents=True)
seq[0].save(shots / "00007.jpg", quality=90)
d = Dev(seq[:4], switch_at=0)  # the ad came up after the last screenshot, before the batch
done, why = swm.run_moves({**cur, "dir": str(T / "lk"), "last_shot": 7}, d, moves, 1.0, 0)
check(done == 5 and "changed a lot" in why, "the reference is the frame the batch was planned on: stops at move 5")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
