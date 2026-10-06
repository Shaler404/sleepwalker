"""The phone side without a phone (adb answers mocked): the app in front by package, launch and restart with
the Play Store in front, the ad loop, screen sleep and touch protection, the stay-awake setting (off by default)."""
import sys as _sys
_sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from util import ROOT, TMP, frames_dir  # noqa: E402
import argparse
import copy
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import time

from PIL import Image

T = TMP / "phtest"
shutil.rmtree(T, ignore_errors=True)
T.mkdir()
G = "com.king.candycrushsaga"
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
os.environ.update(ENV)
spec = importlib.util.spec_from_file_location("sw", ROOT / "harness" / "sw.py")
swm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(swm)


def check(cond, msg):
    print(("OK   " if cond else "FAIL ") + msg)
    if not cond:
        raise SystemExit(1)


def sw(*a):
    r = subprocess.run([sys.executable, str(ROOT / "harness" / "sw.py"), "-d", "fake1", *a], capture_output=True,
                       text=True, encoding="utf-8", env=ENV, cwd=ROOT)
    if r.returncode != 0:
        raise SystemExit(f"FAIL {a}: {r.stdout}\n{r.stderr}")
    return json.loads(r.stdout)


# --- the app in front: `dumpsys window | grep -E 'mCurrentFocus|mFocusedApp|Window #| package='` ---------------
GAME_ACT = f"{G}/{G}.CandyCrushSagaActivity"
WINDOWS = {"8f1a2b3": ("NotificationShade", "com.android.systemui"), "4c5d6e7": ("StatusBar", "com.android.systemui"),
           "a1b2c3d": ("Panel", G), "5d6e7f8": (f"Splash Screen {G}", G), "e4f5a6b": (GAME_ACT, G),
           "c0ffee1": ("com.android.vending/com.google.android.finsky.activities.MainActivity", "com.android.vending"),
           "c0ffee2": ("com.android.vending/com.google.android.finsky.billing.acquire.SheetUiBuilderHostActivity",
                       "com.android.vending"),
           "d00d001": ("com.google.android.permissioncontroller/com.android.permissioncontroller.permission.ui."
                       "GrantPermissionsActivity", "com.google.android.permissioncontroller")}


def dump(key, window_list=True):
    lines = []
    if window_list:
        for n, (k, (title, pkg)) in enumerate(WINDOWS.items()):
            lines += [f"  Window #{n} Window{{{k} u0 {title}}}:",
                      f"    mOwnerUid=10{n} showForAllUsers=false package={pkg} appop=NONE"]
    lines += [f"  mCurrentFocus=Window{{{key} u0 {WINDOWS[key][0]}}}",
              f"  mFocusedApp=ActivityRecord{{77aa88b u0 {G}/.CandyCrushSagaActivity t412}}"]
    return "\n".join(lines) + "\n"


check(swm.parse_focus(dump("a1b2c3d")) == (G, "Panel"),
      "the game's own window titled Panel: the app is the game's package, the title is kept")
check(swm.parse_focus(dump("e4f5a6b")) == (G, GAME_ACT), "an activity: its package, as before")
check(swm.parse_focus(dump("a1b2c3d", window_list=False)) == (G, "Panel"),
      "no window list: the package of the activity that has the focus")
check(swm.parse_focus(dump("8f1a2b3"))[0] == "com.android.systemui",
      "the notification shade over the game is not the game")
check(swm.parse_focus(dump("5d6e7f8")) == (G, f"Splash Screen {G}"), "a window title with spaces")
check(swm.parse_focus(dump("d00d001"))[0] == "com.google.android.permissioncontroller",
      "the permission prompt keeps its package")
check(swm.parse_focus("  mCurrentFocus=null\n") == (None, ""), "no focused window: None")
check(swm.PAYMENT_WINDOW.search(swm.parse_focus(dump("c0ffee2"))[1]) is not None,
      "focus_window keeps the activity name the payment check needs")

# a fake adb: the focused window, the window list, power, settings; Back removes what is in front of the game
S = {"behind": "e4f5a6b", "front": None, "need": 0, "backs": 0, "touch": False, "summary": "0x1", "stay": "0",
     "maker": "samsung", "protect": "1"}
sent = []


def put(value):
    return any(c.endswith(f"settings put global stay_on_while_plugged_in {value}") for c in sent)


def fake_adb(dev, *a, **k):
    cmd = " ".join(a)
    sent.append(cmd)
    if "KEYCODE_BACK" in cmd:
        S["backs"] += 1
    if "mCurrentFocus|mFocusedApp" in cmd:
        return dump(S["front"] if S["front"] and S["backs"] < S["need"] else S["behind"])
    if "isKeyguardShowing" in cmd:
        return "    isKeyguardShowing=false\n"
    if "dumpsys window windows" in cmd:
        return "  Window #3 Window{1 u0 IgniteTouchProtectionPresenter}:\n    isVisible=true\n" if S["touch"] else ""
    if "dumpsys power" in cmd:
        return f"  mWakefulness=Awake\n  mUserActivitySummary={S['summary']}\n"
    answers = {"screen_brightness": "120", "screen_off_timeout": "30000", "stay_on_while_plugged_in": S["stay"],
               "ro.product.manufacturer": S["maker"], "accidental_touch_protection": S["protect"]}
    return next((v for key, v in answers.items() if key in cmd and "settings put" not in cmd), "")


class NoSleep:
    def __getattr__(self, name):
        return getattr(time, name)

    @staticmethod
    def sleep(s):
        pass


class Phone:
    def __init__(self):
        self.launches = 0

    def screenshot(self):
        return Image.new("RGB", (1080, 2340), (40, 80, 120))

    def launch(self, package):
        self.launches += 1

    def stop(self, package):
        pass


D = T / "sess"
(D / "shots").mkdir(parents=True)


def new_cur(**kw):
    return {"status": "active", "id": "20261002-000000-testbox-fake1", "game": G, "title": "Candy", "platform": "android",
            "device": "fake1", "dir": str(D), "t0": time.time(), "last_action": time.time(), "step": 0, "shots": 0,
            "scale": 1.0, "same_streak": 0, "budget_min": 10, "max_steps": 40, "clips": [], "clip_open": None,
            "model": "opus", "moves": 0, **kw}


def last_step():
    return [json.loads(x) for x in open(D / "steps.jsonl", encoding="utf-8")][-1]


replies = []
swm.adb, swm.time, swm.out = fake_adb, NoSleep(), replies.append
phone, cur = Phone(), new_cur()
swm.pick_session = lambda args, active=True: cur
swm.open_device = lambda c, prepare=False: phone

S.update(behind="a1b2c3d")
info = swm.take_shot(cur, phone)
check(info["app"] == G and info["window"] == "Panel" and cur["last_app"] == G and not info.get("warnings"),
      f"the account panel: app {info['app']}, window {info.get('window')}, no 'not the game' warning, mark accepts it")
S.update(behind="e4f5a6b")
info = swm.take_shot(cur, phone)
check("window" not in info, "an activity in front: no window field")

# --- launch and restart with the store in front ------------------------------------------------------------------
S.update(front="c0ffee1", need=1, backs=0)
info = swm.take_shot(cur, phone)
check(any("not the game on screen (com.android.vending)" in w and "presses back" in w for w in info.get("warnings", [])),
      "a store listing in front: the not-the-game warning, with launch as the way out")
S.update(backs=0)
swm.cmd_launch(argparse.Namespace())
r, step = replies[-1], last_step()
check(r["back_pressed"] == 1 and r["app"] == G and phone.launches == 2 and step["back_pressed"] == 1
      and "store_in_front" not in r, f"launch with the listing in front: back once, the game again: {r['back_pressed']}")
S.update(front="c0ffee1", need=99, backs=0)
swm.cmd_restart(argparse.Namespace(why="the store will not go"))
r = replies[-1]
check(r["back_pressed"] == 2 and "key back by hand" in r.get("store_in_front", ""),
      f"the store stays after two backs: the reply says so: {r.get('store_in_front')}")
S.update(front="c0ffee2", need=1, backs=0)
n0 = len([c for c in sent if "KEYCODE_BACK" in c])
swm.cmd_launch(argparse.Namespace())
r, step = replies[-1], last_step()
check(r["back_pressed"] == 0 and r.get("payment_sheet_closed") and r["app"] == G
      and len([c for c in sent if "KEYCODE_BACK" in c]) == n0 + 1,
      "a payment sheet is not launch's to press back on: take_shot closes it, once")
S.update(front=None, need=0)

# --- touch protection and screen sleep -----------------------------------------------------------------------------
S.update(touch=True, summary="0x2")
try:
    swm.guard(cur)
    code = None
except SystemExit as ex:
    code = ex.code
step, saved = last_step(), json.loads(swm.session_path("fake1").read_text(encoding="utf-8"))
check(code == 3 and step["type"] == "error" and step["touch_blocked"] and step["brightness"] == 120
      and step["wakefulness"] == "Awake" and step["dimmed"],
      f"touches blocked: exit 3 and an error step with the brightness and wakefulness: {step}")
check("touch protection" in saved.get("blocked_reason", ""), "the reason stays in the session")
swm.cmd_wait(argparse.Namespace(seconds=60, hi=False))
r, step = replies[-1], last_step()
check(r.get("screen") == "dimmed" and r.get("touch_blocked") is True
      and any("every tap is refused" in w and "end --status blocked" in w for w in r.get("warnings", []))
      and step.get("screen") == "dimmed" and step.get("touch_blocked") is True,
      "wait on a dimmed screen with touch protection up says taps are refused and how to end")
S.update(touch=False)
swm.cmd_wait(argparse.Namespace(seconds=60, hi=False))
r, step = replies[-1], last_step()
check(r.get("screen") == "dimmed" and "touch_blocked" not in r and "touch_blocked" not in step
      and any("harmless" in w for w in r.get("warnings", [])),
      "wait on a dimmed screen without the protection says to tap something harmless")
S.update(touch=False, summary="0x1")
swm.cmd_wait(argparse.Namespace(seconds=60, hi=False))
check("screen" not in replies[-1], "wait on a bright screen says nothing")
res = swm.finish(saved, "blocked", "touches blocked")
meta = json.loads((D / "session.json").read_text(encoding="utf-8"))
check("touch protection" in (meta.get("blocked_reason") or ""), "end --status blocked writes blocked_reason")

# --- the screen settings at start: read and reported; changed only when local.yaml turns it on ---------------------
sent.clear()
cur = new_cur()
screen, warn = swm.screen_settings(cur)
check(screen == {"timeout_s": 30, "stay_awake": False} and not any("settings put" in c for c in sent)
      and "stay_prev" not in cur, f"by default the settings are only read: {screen}")
check(any("Accidental touch protection is on" in w for w in warn), "a Samsung with touch protection on: a warning")
S.update(maker="Google")
check(swm.screen_settings(cur)[1] == [], "another maker: no touch protection warning")
cfg = copy.deepcopy(swm.L())
cfg["android"]["stay_awake"] = True
orig_L, swm.L = swm.L, lambda: cfg
screen, _ = swm.screen_settings(cur)
check(put("3") and screen["stay_awake"] and cur["stay_prev"] == "0"
      and swm.device_profile("fake1").get("_stay_restore") == "0",
      "android.stay_awake: on for the session, the previous value kept in the session and the device profile")
sent.clear()
swm.restore_session_settings(cur)
check(put("0") and "_stay_restore" not in swm.device_profile("fake1"),
      "end restores the previous value")
S.update(stay="7")
sent.clear()
screen, _ = swm.screen_settings(new_cur())
check(screen["stay_awake"] and not any("settings put" in c for c in sent), "already on: nothing to change")
swm.L = orig_L
swm.set_pending("fake1", "_stay_restore", "0")
sent.clear()
swm.restore_pending("fake1")
check(put("0") and not swm.device_profile("fake1").get("_stay_restore"),
      "a phone unplugged mid-session gets the previous value back on the next connection")

sys.path.insert(0, str(ROOT / "harness"))
from device import AndroidDevice  # noqa: E402


class Shell:
    def __init__(self):
        self.cmds = []

    def shell(self, cmd):
        self.cmds.append(cmd)
        return "0"


ad = AndroidDevice.__new__(AndroidDevice)
ad.adb = Shell()
ad._prepare()
check(not any("settings put" in c for c in ad.adb.cmds), f"opening the phone changes no setting: {ad.adb.cmds}")

# --- the ad loop and restarts in stats, on the fake phone ---------------------------------------------------------
sw("start", G)
r1, r2, r3 = (sw("restart", "--why", "the same ad") for _ in range(3))
check(not any("ad loop" in w for w in r1.get("warnings", []) + r2.get("warnings", []))
      and any("ad loop" in w for w in r3.get("warnings", [])), "the third restart in 10 minutes: the ad loop warning")
sw("level", "start", "level 5", "--mechanic", "match", "--plan", "x")
r = sw("restart", "--why", "a new level, a new problem")
check(not any("ad loop" in w for w in r.get("warnings", [])), "a level in between: the count starts again")
sw("end", "--status", "ok", "--summary", "restarts")
st = sw("stats", G)["games"][G]["sessions"][-1]
check(st["restarts"] == 4, f"stats counts restarts per session: {st['restarts']}")
# --- the owner's use of the phone is a hold, not a guess from the app on screen (2026-10-05) ---------------------
_saved = (swm.adb, swm.locked, swm.touch_blocked, swm.focus, swm.in_hours)
swm.adb = lambda d, *a, **k: ("level: 90\ntemperature: 300\nAC powered: true" if "battery" in " ".join(a)
                              else "mWakefulness=Awake")
swm.locked, swm.touch_blocked, swm.in_hours = (lambda d: False), (lambda d: False), (lambda *a: True)
swm.focus = lambda d: "com.android.chrome"
ok, why = swm.phone_status("nophone", {G})
check(ok, f"a browser on screen does not make claim idle (the agent itself may have opened it): {why}")
swm.locked = lambda d: True
ok, why = swm.phone_status("nophone", {G})
check(not ok and "locked" in why, f"a locked phone is still refused: {why}")
swm.adb, swm.locked, swm.touch_blocked, swm.focus, swm.in_hours = _saved
print("all ok")
shutil.rmtree(T, ignore_errors=True)
