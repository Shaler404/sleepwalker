"""page-footnotes: inline [s:SESSION#STEP] sources become footnotes; existing footnotes keep their numbers."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP, frames_dir  # noqa: E402
import importlib.util
import json
import os
import shutil
from pathlib import Path

SP = Path(__file__).resolve().parent
T = TMP / "fntest"
DEV = ROOT
shutil.rmtree(T, ignore_errors=True)
G = "com.maroieqrwlk.unpin"
A, B = "20260930-192115-chrono-2FYKPJ", "20260930-201034-chrono-2FYKPJ"
for sid in (A, B):
    d = T / "raw" / G / sid
    d.mkdir(parents=True)
    (d / "session.json").write_text(json.dumps({"id": sid}), encoding="utf-8")
    (d / "steps.jsonl").write_text("".join(json.dumps({"step": i, "t": 1000.0 + i}) + "\n" for i in range(40)),
                                   encoding="utf-8")
(T / "local.yaml").write_text(f'machine: t\nraw_dir: "{(T / "raw").as_posix()}"\nstate_dir: "{(T / "state").as_posix()}"\n',
                              encoding="utf-8")
os.environ["SW_LOCAL"] = str(T / "local.yaml")
spec = importlib.util.spec_from_file_location("sw", DEV / "harness" / "sw.py")
swm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(swm)


def check(cond, msg):
    print(("OK   " if cond else "FAIL ") + msg)
    if not cond:
        raise SystemExit(1)


page = (f"---\ngame: {G}\n---\n# X\n\nOpens from the map [s:{A}#29] [s:{B}#1]. Tabs [s:{B}#5].\n\n"
        f"| Open | done | [s:{B}#5] |\n\n[^s1]: an older footnote\n")
s, n = swm.page_footnotes(page, G)
check(n == 3 and "[s:" not in s, f"three distinct sources became footnotes: {n}")
check("[^s1]: an older footnote" in s and f"[^s2]: session {A}, step 29" in s, "an existing footnote keeps its number")
check(s.count("[^s4]") == 3 and s.count("[^s4]:") == 1, "the same source gets the same footnote")
s2, n2 = swm.page_footnotes(s + f"\nOne more fact [s:{A}#29] and [s:{A}#30].\n", G)
check(n2 == 1 and s2.count("[^s2]") == 3 and "[^s5]:" in s2, "a second run reuses its footnotes and adds only new ones")
s3, n3 = swm.page_footnotes(s2, G)
check(n3 == 0 and s3 == s2, "nothing left to convert: the page is unchanged")

# the original went up after the page was written (uploadLimitExceeded at the end): its footnotes get the link
s4, k = swm.link_footnotes(s3, G)
check(k == 0 and s4 == s3, "no video yet: the footnotes stay as they are")
(T / "raw" / G / A / "session.json").write_text(json.dumps({"id": A, "youtube": "abc123"}), encoding="utf-8")
s4, k = swm.link_footnotes(s3, G)
la, lb = " — [video at 0:29](https://youtu.be/abc123?t=29)", " — [video at 0:30](https://youtu.be/abc123?t=30)"
check(k == 2 and f"[^s2]: session {A}, step 29{la}\n" in s4 and f"[^s5]: session {A}, step 30{lb}\n" in s4
      and f"[^s3]: session {B}, step 1\n" in s4, "footnotes of the session now on YouTube get the link")
check(s4.replace(la, "").replace(lb, "") == s3, "nothing else on the page changes")
s5, k5 = swm.link_footnotes(s4, G)
check(k5 == 0 and s5 == s4, "a linked footnote is left alone")
s6, k6 = swm.link_footnotes(s3, G, only={B})
check(k6 == 0 and s6 == s3, "only: the sessions just uploaded")
print("all ok")
shutil.rmtree(T, ignore_errors=True)
