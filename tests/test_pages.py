"""Feature pages: marks with places, the page skeleton, tagging old frames, the page check."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP, frames_dir  # noqa: E402
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

SP = Path(__file__).resolve().parent
T = TMP / "pagetest"
DEV = ROOT
shutil.rmtree(T, ignore_errors=True)
T.mkdir()
G = "com.maroieqrwlk.unpin"
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


s = sw("start", G)
sid = s["session"]
r = sw("mark", "map", "the map", "--as", "entry", expect_ok=False)
check("--feature" in json.dumps(r), "--as needs --feature")
r = sw("mark", "map", "the map", "--feature", "collections", "--as", "corner", expect_ok=False)
check("tab:<name>" in json.dumps(r), "an unknown place is refused")
r = sw("mark", "map", "the map", "--feature", "collections", "--as", "entry", "--at", "12", expect_ok=False)
check("X,Y" in json.dumps(r), "a malformed --at is refused")
sw("mark", "Level map", "the coin box right of Play! opens Collections", "--feature", "collections", "--as", "entry",
   "--at", "300,500")
sw("tap", "300", "500", "--why", "open collections")
sw("mark", "Collections", "four tabs, the gacha machine first", "--feature", "collections", "--as", "screen")
sw("mark", "Gacha", "Spin! for coins or a video", "--feature", "collections", "--as", "tab:Gacha")
sw("tap", "100", "100", "--why", "skins tab")
sw("mark", "Skins", "Themes, Trails, Walls", "--feature", "collections", "--as", "tab:Skins")
sw("feature", "collections", "Collections")
sw("case", "collections", "open", "Open Collections from the map", "--done")
sw("end", "--status", "ok", "--summary", "collections")

pages = T / "state" / G / "pages"
r = sw("page-skeleton", G, "collections", "--out", str(pages), device=False)
page = Path(r["page"])
s = page.read_text(encoding="utf-8")
check(r["tabs"] == ["Gacha", "Skins"] and not r["missing_frames"] and page.name == "collections.md",
      f"skeleton: entry, screen and both tabs have frames: {r['frames']}")
check("## Where to find it" in s and "## What it looks like" in s and "### Gacha" in s and "### Skins" in s
      and "[^s1]:" in s and f"session {sid}" in s and "[s:" not in s, "the page layout with footnoted sources")
imgs = list((pages / "img").glob("*.webp"))
check(len(imgs) == 4 and all(i.stat().st_size > 0 for i in imgs), f"frames as WebP next to the page: {len(imgs)}")
r = sw("check-pages", str(pages), device=False)
check(r["ok"] == 1 and not r["problems"], f"the skeleton passes the page check: {r['problems']}")

# the check catches what was wrong in the first wiki
bad = s.replace(next(line for line in s.splitlines() if line.startswith("![") and "Themes" in line), "")
(pages / "features" / "skins-missing.md").write_text(bad, encoding="utf-8")
(pages / "features" / "old.md").write_text("# Old\\n\\nThe box opens Collections [s:20260930-x#29].\\n", encoding="utf-8")
r = sw("check-pages", str(pages), expect_ok=False, device=False)
p = r["problems"]
check(any("tab 'Skins' has no frame" in x for x in p[str(Path("features") / "skins-missing.md")]),
      "a tab without its frame is caught")
check(any("Where to find it" in x for x in p[str(Path("features") / "old.md")]) and
      any("inline [s:" in x for x in p[str(Path("features") / "old.md")]), "missing sections and inline sources are caught")

# an existing page is never overwritten; old frames can be tagged afterwards
r = sw("page-skeleton", G, "collections", "--out", str(pages), device=False)
check(r["page"].endswith("collections.skeleton.md"), "an existing page gets a .skeleton.md next to it")
r = sw("mark-tag", G, sid, "1", "--feature", "shop", "--as", "screen", "--desc", "the shop", device=False)
check(r["tagged"]["feature"] == "shop" and r["tagged"]["role"] == "screen", "an old frame tagged for a page")
r = sw("page-skeleton", G, "shop", "--out", str(pages), device=False)
check(r["frames"].get("screen") == 1 and "entry" in r["missing_frames"], "the tagged frame is used; the gap is named")
# a frame of another app (a store, a system dialog, the status bar) never goes to a page
sd = T / "raw" / G / sid
for suf in (".jpg", "_m.jpg"):
    shutil.copy(sd / "shots" / f"00001{suf}", sd / "shots" / f"00090{suf}")
with open(sd / "steps.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps({"step": 90, "type": "tap", "shot": 90, "app": "com.android.vending"}) + "\n")
r = sw("mark-tag", G, sid, "90", "--feature", "shop", "--as", "entry", "--desc", "the store", expect_ok=False, device=False)
check("not the game" in json.dumps(r), "mark-tag refuses a frame of another app")
# personal data inside the game's own frame (a user id, the status bar, a real player's name) is blacked out
img = sorted((pages / "img").glob("*.webp"))[0]
r = sw("redact-image", str(img), "--box", "0,0,1,0.05", "--box", "10,200,60,230", device=False)
from PIL import Image  # noqa: E402
with Image.open(img) as im:
    w, h = im.size
    top, box, rest = im.convert("RGB").getpixel((w // 2, 2)), im.convert("RGB").getpixel((30, 215)), im.convert("RGB").getpixel((w // 2, h // 2))
check(r["size"] == [w, h] and r["boxes"] == 2 and max(top) < 20 and max(box) < 20,
      f"redact-image blacks out boxes in fractions or pixels: {top} {box} {rest}")
r = sw("redact-image", str(img), "--box", "0,0,9999,10", expect_ok=False, device=False)
check("outside" in json.dumps(r), "a box outside the image is refused")
from PIL import ImageSequence  # noqa: E402
clip = pages / "clip.webp"
fr = [Image.new("RGB", (200, 300), c) for c in ((200, 50, 50), (50, 200, 50), (50, 50, 200))]
fr[0].save(clip, format="WEBP", save_all=True, append_images=fr[1:], duration=[100, 150, 200], loop=0)
r = sw("redact-image", str(clip), "--box", "0,0,1,0.1", device=False)
with Image.open(clip) as im:
    seq = [(f.convert("RGB").getpixel((100, 10)), f.convert("RGB").getpixel((100, 200)), f.info.get("duration"))
           for f in ImageSequence.Iterator(im)]
check(r.get("frames") == 3 and len(seq) == 3 and all(max(a) < 20 and max(b) > 150 for a, b, _ in seq)
      and [d for _, _, d in seq] == [100, 150, 200], f"a clip keeps its frames and timing, every frame blacked out: {seq}")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
