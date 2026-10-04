"""Pages v2: clean frames (nothing drawn), clips cut from the recording, the documenter's scope and backlog, pages
held against the feature map (case ids, checklist items, outcomes), the new sections, and the original kept until
its session is documented. The feature model's fields are written as journal ops, as its contract has them."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP, frames_dir  # noqa: E402
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

import yaml
from PIL import Image, ImageChops

T = TMP / "pagesv2"
shutil.rmtree(T, ignore_errors=True)
T.mkdir(parents=True)
G = "com.maroieqrwlk.unpin"


def find_tool(name: str) -> str | None:
    """ffmpeg / ffprobe from this checkout's local.yaml tools, else from PATH."""
    p = ROOT / "local.yaml"
    tools = ((yaml.safe_load(p.read_text(encoding="utf-8")) or {}).get("tools") or {}) if p.exists() else {}
    t = tools.get(name)
    if isinstance(t, str) and (shutil.which(t) or Path(t).exists()):
        return shutil.which(t) or t
    return shutil.which(name)


FF, FP = find_tool("ffmpeg"), find_tool("ffprobe")
tools = f'tools: {{ffmpeg: "{Path(FF).as_posix()}", ffprobe: "{Path(FP).as_posix()}"}}\n' if FF and FP else ""
(T / "local.yaml").write_text(f"""machine: testbox
games: [{G}]
android: {{serials: [nophone]}}
fake_devices: {{fake1: "{frames_dir().as_posix()}"}}
video: {{record: false}}
state_dir: "{(T / 'state').as_posix()}"
raw_dir: "{(T / 'raw').as_posix()}"
wiki_dir: "{(T / 'gwiki').as_posix()}"
""" + tools, encoding="utf-8")
ENV = {**os.environ, "SW_LOCAL": str(T / "local.yaml"), "PYTHONIOENCODING": "utf-8"}
STATE, RAW = T / "state" / G, T / "raw" / G


def sw(*a, expect_ok=True, device=True):
    r = subprocess.run([sys.executable, str(ROOT / "harness" / "sw.py"), *(["-d", "fake1"] if device else []), *a],
                       capture_output=True, text=True, encoding="utf-8", env=ENV, cwd=ROOT)
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


def op(rec: dict) -> None:
    """A journal op as the feature model writes it."""
    with open(STATE / "research.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({"t": round(time.time(), 3), **rec}) + "\n")


# --- a session: an entry point marked with --at, the feature's screen, steps to cite --------------------------
sid = sw("start", G)["session"]
sw("tap", "100", "200", "--why", "the level map")
sw("mark", "Level map", "the Multi Stage label over level 5, the Play! button under it", "--feature", "multi-stage",
   "--as", "entry", "--at", "300,500")
sw("tap", "300", "500", "--why", "start level 5")
sw("mark", "Stage 1", "the Stage panel on the right: stage 1 active, 3 locked", "--feature", "multi-stage",
   "--as", "screen")
sw("tap", "320", "520", "--why", "pull the pin")
sw("tap", "330", "530", "--why", "the stage failed window")
sw("feature", "keys", "Keys")
sw("case", "keys", "chest", "Three keys open the key chest", "--done")
sw("end", "--status", "ok", "--summary", "multi stage")
steps = [json.loads(x) for x in (RAW / sid / "steps.jsonl").read_text(encoding="utf-8").splitlines()]
entry = next(x for x in steps if x.get("type") == "mark" and x.get("role") == "entry")
check(entry.get("at") == [300.0, 500.0], "--at stays in the mark record")

# the feature model's ops: a type catalog, a base level with its outcomes, a level type over it
(T / "state").mkdir(exist_ok=True)
(T / "state" / "feature-types.local.yaml").write_text(yaml.safe_dump({"types": [
    # test-only type ids: the published catalog's types carry their own checklists, which this test does not use
    {"id": "t-core", "name": "Base level", "base": None, "affects_level_flow": False, "checklist": []},
    {"id": "t-level", "name": "Level type", "base": "t-core", "affects_level_flow": True,
     "checklist": [{"id": "appeared", "text": "Why it appeared", "kind": "look"}]},
    {"id": "t-competition", "name": "Competition", "base": None, "affects_level_flow": True, "checklist": []}]}),
    encoding="utf-8")
op({"session": sid, "step": 1, "op": "feature", "id": "core-level", "name": "Core level", "type": "t-core"})
op({"session": sid, "step": 3, "op": "case", "feature": "core-level", "id": "win", "text": "Win: the Fantastic! screen",
    "outcome": True, "done": True, "source": f"{sid}#3"})
op({"session": sid, "step": 3, "op": "case", "feature": "core-level", "id": "bomb", "text": "Defeat by a bomb in the cup",
    "outcome": True})
op({"session": sid, "step": 2, "op": "feature", "id": "multi-stage", "name": "Multi Stage levels", "type": "t-level",
    "appeared": {"text": "after winning level 4", "certainty": "fact", "source": f"{sid}#2"},
    "locked": {"text": "level 5", "value": 5}})
for c in ({"id": "chk-appeared", "text": "Why it appeared", "done": True, "source": f"{sid}#2"},
          {"id": "chk-entry", "text": "Where to find it", "done": True, "source": f"{sid}#2"},
          {"id": "chk-screen", "text": "What the level screen looks like"},
          {"id": "under-win", "text": "The base level's outcome win under this feature", "done": True,
           "source": f"{sid}#3", "note": "the same as the base, after the last stage only"},
          {"id": "under-bomb", "text": "The base level's outcome bomb under this feature"},
          {"id": "play", "text": "Play a multi-stage level through all its stages", "done": True, "source": f"{sid}#3"},
          {"id": "tap-to-restart", "text": "Stage failed screen: Tap to restart goes back to stage 1", "done": True,
           "source": f"{sid}#4"}):
    op({"session": sid, "step": 4, "op": "case", "feature": "multi-stage", **c})
# a feature whose type affects the level flow but has no base: its under- cases stay in Cases
op({"session": sid, "step": 4, "op": "feature", "id": "win-streak", "name": "Win streak", "type": "t-competition"})
op({"session": sid, "step": 4, "op": "case", "feature": "win-streak", "id": "under-win", "text": "A win under a streak"})
# the review closes a case later, citing a step of this session
op({"session": "review-20261002", "op": "case", "feature": "leagues", "id": "points", "text": "Pins are league points",
    "done": True, "source": f"{sid}#3"})

view = yaml.safe_load(sw("research", G, device=False))
ms = next(f for f in view["features"] if f["id"] == "multi-stage")
cl = next(f for f in view["features"] if f["id"] == "core-level")
check(ms.get("type") == "t-level" and ms["appeared"]["certainty"] == "fact" and ms["locked"]["value"] == 5
      and next(c for c in cl["cases"] if c["id"] == "win").get("outcome") is True
      and next(c for c in ms["cases"] if c["id"] == "under-win").get("note"),
      "apply_op keeps the feature model's fields: type, appeared, locked, a case's outcome and note")

# --- 1. clean screenshots: the exported image is the source frame scaled, nothing drawn -------------------------
pages = STATE / "pages"
r = sw("page-skeleton", G, "multi-stage", "--out", str(pages), device=False)
page = Path(r["page"])
s = page.read_text(encoding="utf-8")
ent = next(ln for ln in s.splitlines() if ln.startswith("![") and "Multi Stage label" in ln)
exported = pages / "features" / re.search(r"\]\(([^)]+)\)", ent).group(1)
sys.path.insert(0, str(ROOT / "harness"))
from perception import save_for_wiki  # noqa: E402
ref = T / "reference.webp"
save_for_wiki(Image.open(entry["file"]).convert("RGB"), str(ref))
with Image.open(exported) as a, Image.open(ref) as b:
    same = a.size == b.size and ImageChops.difference(a.convert("RGB"), b.convert("RGB")).getbbox() is None
check(same, "no circle: the entry frame on the page equals the source frame scaled")
lines = s.splitlines()
check(lines[lines.index(ent) + 1] == "*the Multi Stage label over level 5, the Play! button under it*",
      "the caption under the entry frame names the control")

# --- 5. the new sections from the skeleton ------------------------------------------------------------------------
heads = [ln for ln in lines if ln.startswith("## ")]
check(heads[:3] == ["## Why it appeared", "## Where to find it", "## What it looks like"]
      and heads.index("## Outcomes") == heads.index("## Cases") - 1, f"the layout: {heads}")
why = s.split("## Why it appeared", 1)[1].split("## ", 1)[0]
check(re.search(r"After winning level 4 \[\^s\d+\]\.", why) is not None, f"why it appeared: the fact with its source: {why.strip()}")
check("locked until level 5" in s, "the lock from the map is noted for the documenter")
outc = s.split("## Outcomes", 1)[1].split("## ", 1)[0]
rows = [ln for ln in outc.splitlines() if ln.startswith("| ") and "case:" in ln]
win = next((r for r in rows if "<!-- case:under-win -->" in r), "")
bomb = next((r for r in rows if "<!-- case:under-bomb -->" in r), "")
# the feature model derives a cell for every outcome of the base level (its checklist's win, restart, quit,
# exit-app and the game's own losses), so the table has a row for each, open ones "not verified"
check(len(rows) >= 2 and "Win: the Fantastic! screen" in win and "after the last stage only" in win and "](../img/" in win
      and "not verified" in bomb and all("case:under-" in r for r in rows),
      f"Outcomes: a row per under- case, the base outcome's name, what differs and its frame: {rows}")
cases = s.split("## Cases", 1)[1].split("## ", 1)[0]
nv = s.split("## Not verified", 1)[1]
check(all(f"<!-- case:{c} -->" in cases for c in ("chk-appeared", "chk-entry", "chk-screen", "play", "tap-to-restart"))
      and "case:under-" not in cases and "<!-- case:chk-screen -->" in nv and "<!-- case:under-bomb -->" in nv,
      f"every Cases row carries its case id; open items are under Not verified with theirs: {cases} || {nv}")
r = sw("check-pages", str(pages), device=False)
check(r["ok"] == 1 and not r["problems"] and not r.get("notes"), f"the skeleton passes the page check: {r}")
r = sw("page-skeleton", G, "win-streak", "--out", str(T / "ws"), device=False)
ws = Path(r["page"]).read_text(encoding="utf-8")
check(not r["outcomes"] and "## Outcomes" not in ws and "<!-- case:under-win -->" in ws.split("## Cases")[1],
      "a type without a base (in the catalog): no Outcomes table, its under- case is a Cases row")
wsw = ws.split("## Why it appeared", 1)[1].split("## ", 1)[0]
check(not re.sub(r"<!--.*?-->", "", wsw, flags=re.S).strip() and 'The map has no "appeared"' in wsw,
      "no appeared in the map: the section is left to the documenter")
r = sw("check-pages", str(T / "ws"), expect_ok=False, device=False)
check(any("'Why it appeared' is empty" in x for x in r["problems"][str(Path("features") / "win-streak.md")]),
      "an empty 'Why it appeared' fails the check")

# --- 4. the map check ---------------------------------------------------------------------------------------------
def variant(name: str, text: str) -> list[str]:
    (pages / "features" / f"{name}.md").write_text(text, encoding="utf-8")
    res = sw("check-pages", str(pages), expect_ok=False, device=False)
    (pages / "features" / f"{name}.md").unlink()
    return res["problems"].get(str(Path("features") / f"{name}.md"), []), res.get("notes", {}).get(
        str(Path("features") / f"{name}.md"), [])


drop = lambda text, key: "\n".join(ln for ln in text.splitlines() if key not in ln) + "\n"  # noqa: E731
p, _ = variant("x1", drop(s, "case:tap-to-restart"))
check(len(p) == 1 and "case 'tap-to-restart' is done in the map" in p[0], f"a done case missing from the page: {p}")
p, _ = variant("x2", drop(s, "case:chk-screen"))
check(len(p) == 1 and "checklist item 'chk-screen'" in p[0], f"an open checklist item neither on the page nor "
                                                               f"under Not verified: {p}")
p, _ = variant("x3", drop(s, "case:under-bomb"))
check(len(p) == 1 and "checklist item 'under-bomb'" in p[0], f"an under-<outcome> item missing: {p}")
p, _ = variant("x4", s.replace(outc, "\n").replace("## Outcomes", ""))
check(any("no '## Outcomes' section" in x for x in p), f"a level type without its Outcomes table: {p}")
p, _ = variant("x5", s.replace("After winning level 4", "Hypothesis: after winning level 4, not verified"))
check(not p, "a hypothesis is a valid 'Why it appeared'")
p, _ = variant("x6", re.sub(r"## Why it appeared.*?(?=## Where)", "", s, flags=re.S))
check(any("no '## Why it appeared'" in x for x in p), "a page without 'Why it appeared' is caught")
p, _ = variant("x7", s.replace("<!-- One paragraph", "The stages are designed to keep players in the level. <!-- x"))
check(any("design intent" in x for x in p), f"a note on why it was designed so is caught: {p}")
nv_moved = s.replace("| Stage failed screen: Tap to restart goes back to stage 1 <!-- case:tap-to-restart --> |", "| x |")
nv_moved = nv_moved.replace("## Not verified\n", "## Not verified\n\n- Stage failed screen: Tap to restart goes back "
                                                "to stage 1 (the frame did not show it)\n", 1)
p, _ = variant("x8", nv_moved)
check(not p, f"a done case the documenter put under Not verified (by its text) is shown: {p}")
# a page written before case ids: the player's cases matched by their text, one note instead of a problem per row;
# the checklist items (made by the harness from templates) only by their ids
old = re.sub(r" ?<!-- case:[^>]+ -->", "", s)
chk = ["chk-appeared", "chk-entry", "chk-screen", "under-win", "under-bomb"]
p, n = variant("old", old)
# with the type catalog, the level type's own checklist items (chk-announce, chk-differs, ...) and the derived
# outcome cells (under-restart, ...) are reported too; no player case ("play", "tap-to-restart") is
check(len(n) == 1 and "no case ids" in n[0] and all(any(f"'{c}'" in x for x in p) for c in chk)
      and all(("'chk-" in x or "'under-" in x) for x in p),
      f"an old page without ids: one note; its rows match by text, the checklist items need their ids: {p} {n}")
p, n = variant("old2", drop(old, "Tap to restart"))
check(len(p) == 6 and any("'tap-to-restart' is done" in x for x in p) and len(n) == 1,
      f"an old page missing a done case: one problem for it: {p}")
p, n = variant("old3", old.replace("| Play a multi-stage level through all its stages |", "| Play a multi-stage level |"))
check(len(p) == 5 and not any("'play'" in x for x in p), f"an old page's row in shorter words still matches: {p}")
p, _ = variant("x9", s.replace("<!-- case:under-win -->", ""))
check(len(p) == 1 and "'under-win' is done" in p[0],
      f"a checklist item is not shown by a sibling's line (under-bomb's text is like under-win's): {p}")
# the other way round: a Cases row ticked ✅ for a case the map has open (2026-10-04: pages kept their ✅ for cases
# the dream had reopened and passed the check; the documenters fixed them by hand)
ticked = re.sub(r"^(\|[^\n]*<!-- case:chk-screen -->[^\n]*\| )not verified( \|)", r"\1✅\2", s, count=1, flags=re.M)
assert ticked != s, "the fixture's chk-screen row is not 'not verified'"
p, _ = variant("x10", ticked)
check(len(p) == 1 and "'chk-screen' is shown done (✅)" in p[0] and "open in the map" in p[0],
      f"a row ticked ✅ for a case the map has open fails the check: {p}")

# the dream's worktree map (merges, renames, cases it closed) is the one its pages are held against
wt = T / "wt"
(wt / G).mkdir(parents=True)
(wt / G / "research.yaml").write_text(yaml.safe_dump({"game": G, "features": [{
    "id": "multi-stage", "name": "Multi Stage levels", "status": "documented", "cases": [
    {"id": "stage-panel", "text": "The Stage panel checks off each cleared stage", "done": True,
     "source": f"{sid}#3"}]}]}), encoding="utf-8")
r = sw("check-pages", str(pages), device=False)
check(r["ok"] == 1, "without --map: the published map, the page passes")
r = sw("check-pages", str(pages), "--map", str(wt), expect_ok=False, device=False)
p = r["problems"].get(str(Path("features") / "multi-stage.md"), [])
check(len(p) == 1 and "'stage-panel' is done" in p[0], f"--map: held against the worktree's map: {p}")
(wt / G / "features").mkdir()
shutil.copy(page, wt / G / "features" / "multi-stage.md")
r = sw("check-pages", str(wt), expect_ok=False, device=False)
check(any("'stage-panel' is done" in x for x in r["problems"].get(str(Path(G) / "features" / "multi-stage.md"), [])),
      "a wiki's pages are held against the research.yaml next to them")

# --- 3. doc-scope and pending-docs ------------------------------------------------------------------------------
r = sw("doc-scope", G, sid, device=False)
sc = {f["feature"]: f for f in r["features"]}
check(set(sc) == {"multi-stage", "core-level", "keys", "win-streak", "leagues"},
      f"doc-scope: the features the session changed, marked or not, and the review's closure citing it: {sorted(sc)}")
m = sc["multi-stage"]
check({"type", "appeared", "locked", "case"} <= set(m["changed"]) and m["marks"] == ["entry", "screen"]
      and m["open_checklist"] == ["chk-screen", "under-bomb"] and m["outcomes_table"] and m["type"] == "t-level"
      and m["appeared"]["certainty"] == "fact" and m["page"] and m["page"].endswith("multi-stage.md"),
      "doc-scope: its type, why it appeared, the lock, the marks, the open checklist items, the page")
check("outcome" in sc["core-level"]["changed"] and not sc["keys"]["marks"] and sc["keys"]["cases"][0]["id"] == "chest",
      "doc-scope: outcome cases; a feature with no marked frame is in scope too")
bench = sw("start", G, "--bench", "b1:1", "--model", "sonnet")["session"]
sw("tap", "100", "100", "--why", "a level")
sw("case", "core-level", "bomb", "--done")
sw("end", "--status", "ok", "--summary", "bench slot 1")
empty = sw("start", G)["session"]
sw("tap", "100", "100", "--why", "look")
sw("end", "--status", "ok", "--summary", "nothing")
check(set(f["feature"] for f in sw("doc-scope", G, bench, device=False)["features"]) == {"core-level"},
      "doc-scope of another session lists only its own features")
with open(STATE / "sessions.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps({"id": "20261001-010101-otherbox-x", "game": G, "machine": "otherbox", "status": "ok"}) + "\n")
    f.write(json.dumps({"id": "20261001-020202-testbox-gone", "game": G, "machine": "testbox", "status": "ok"}) + "\n")
r = sw("pending-docs", device=False)
check([x["session"] for x in r["pending"]] == [sid, bench] and r["pending"][1].get("bench") == "b1:1"
      and r["nothing_to_document"] == 1 and r["raw_gone"] == 1,
      f"pending-docs: this machine's undocumented sessions, oldest first, bench included: {r}")
(STATE / "docs-log.md").write_text(f"## {sid} · 2026-10-02\n- pages: multi-stage\n", encoding="utf-8")
r = sw("pending-docs", device=False)
check([x["session"] for x in r["pending"]] == [bench], "a session in docs-log.md is no longer pending")

# --- 2. clip-cut on a recording -----------------------------------------------------------------------------------
C = "20261002-101500-testbox-clip"
cd = RAW / C
(cd / "shots").mkdir(parents=True)
recs = [{"t": 1000.0, "step": 0, "type": "start"}]
recs += [{"t": 1000.0 + 2 * i, "step": i, "type": "tap", "shot": i, "settle": 1.0} for i in range(1, 15)]
recs.append({"t": 1010.2, "step": 5, "type": "research", "op": "case", "feature": "multi-stage", "id": "retry-stage",
             "done": True})
(cd / "steps.jsonl").write_text("".join(json.dumps(x) + "\n" for x in sorted(recs, key=lambda x: x["t"])),
                                encoding="utf-8")
(cd / "session.json").write_text(json.dumps({"id": C, "game": G}), encoding="utf-8")
gd = T / "clipout"
r = sw("clip-cut", G, C, "--from-step", "1", "--to-step", "12", "--slug", "whole level", "--out", str(gd),
       expect_ok=False, device=False)
check("one moment" in r.get("error", ""), f"a span over --max-s is refused: {r.get('error')}")
r = sw("clip-cut", G, C, "--from-step", "5", "--to-step", "7", "--slug", "x", "--out", str(gd), "--max-s", "30",
       expect_ok=False, device=False)
check("clip_max_seconds" in r.get("error", ""), "--max-s above the media limit is refused")
r = sw("clip-cut", G, C, "--from-step", "5", "--to-step", "7", "--slug", "x", "--out", str(gd),
       expect_ok=False, device=False)
check("no recording" in r.get("error", ""), "no original and no video: refused")
if FF and FP:
    made = subprocess.run([FF, "-y", "-loglevel", "error", "-f", "lavfi", "-i", "testsrc=size=180x320:rate=10",
                           "-t", "30", "-c:v", "mpeg4", "-pix_fmt", "yuv420p", str(cd / "original.mkv")],
                          capture_output=True, text=True)
    check(made.returncode == 0, f"a 30 s test recording: {made.stderr[-300:]}")
    r = sw("clip-cut", G, C, "--from-step", "5", "--to-step", "7", "--slug", "Stage failed: tap to restart",
           "--out", str(gd), device=False)
    clip = gd / "clips" / "20261002-stage-failed-tap-to-restart.webp"
    with Image.open(clip) as im:
        frames, size = getattr(im, "n_frames", 1), im.size
    check(clip.exists() and r["clip"] == "../clips/20261002-stage-failed-tap-to-restart.webp" and frames > 10
          and r["mb"] <= 8 and abs(r["seconds"] - 7.0) < 0.2 and r["original_from_s"] == 7.5,
          f"clip-cut: steps 5-7 (from just before the move to after the result) as an animated WebP: {r} {frames} {size}")
    check(r["footnote"] == f"session {C}, step 5" and r["caption"] == "*Clip 7 s*",
          f"clip-cut returns the footnote text and the caption: {r['footnote']} / {r['caption']}")
    r = sw("clip-cut", G, C, "--from-step", "5", "--to-step", "7", "--slug", "Stage failed: tap to restart",
           "--out", str(gd), expect_ok=False, device=False)
    check("one clip per moment" in r.get("error", ""), "the same clip twice is refused")
else:
    print("SKIP clip-cut encoding: no ffmpeg/ffprobe in this checkout's local.yaml tools or on PATH")
    (cd / "original.mkv").write_bytes(b"x" * 1000)

# the original stays after the upload until the session is documented, then gc deletes it
(cd / "session.json").write_text(json.dumps({"id": C, "game": G, "youtube": "VIDX"}), encoding="utf-8")
if FF and FP:
    r = sw("clip-cut", G, C, "--from-step", "9", "--to-step", "9", "--slug", "the result", "--out", str(gd), device=False)
    check(r["caption"] == "*Clip 3 s · [original on YouTube from 0:15](https://youtu.be/VIDX?t=15)*",
          f"uploaded and still here: the clip's caption links the original at the moment: {r['caption']}")
r = sw("gc", device=False)
check((cd / "original.mkv").exists(), "gc keeps an uploaded original while the session is not documented")
with open(STATE / "docs-log.md", "a", encoding="utf-8") as f:
    f.write(f"## {C} · 2026-10-02\n- pages: multi-stage (clip)\n")
r = sw("gc", device=False)
check(not (cd / "original.mkv").exists(), "once documented, gc deletes the uploaded original")
r = sw("clip-cut", G, C, "--from-step", "5", "--to-step", "7", "--slug", "again", "--out", str(gd),
       expect_ok=False, device=False)
check("gone" in r.get("error", "") and r.get("youtube") == "https://youtu.be/VIDX?t=7"
      and r.get("footnote") == f"session {C}, step 5 — [video at 0:10](https://youtu.be/VIDX?t=10)",
      f"the original gone (uploaded and cleaned up): refused with the moment's YouTube link: {r}")

# a lock seen open: None clears the field, unlocked_at is kept
op({"session": sid, "op": "feature", "id": "multi-stage", "locked": None, "unlocked_at": {"text": "level 5"}})
ms = next(f for f in yaml.safe_load(sw("research", G, device=False))["features"] if f["id"] == "multi-stage")
check("locked" not in ms and ms["unlocked_at"] == {"text": "level 5"}, "a lock seen open: locked cleared, unlocked_at kept")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
