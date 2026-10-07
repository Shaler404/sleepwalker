"""A common device interface and its Android implementation over ADB.

Dependencies: pip install adbutils uiautomator2 pillow
Optional: pip install scrcpy-client av  (fast video stream, the ScrcpyScreen class)

The same interface is implemented by a USB phone, the Google Play Games Developer
Emulator (adb connect localhost:6520) and the Google Play Games window on a PC (gpg_windows.py).
Coordinates in all methods are physical pixels of the device screen.
"""
from __future__ import annotations

import base64
import re
import shlex
import time
from typing import Protocol, runtime_checkable

from PIL import Image


@runtime_checkable
class Device(Protocol):
    name: str
    width: int
    height: int

    def screenshot(self) -> Image.Image: ...
    def tap(self, x: int, y: int) -> None: ...
    def double_tap(self, x: int, y: int) -> None: ...
    def long_press(self, x: int, y: int, duration_ms: int = 800) -> None: ...
    def swipe(self, x1: int, y1: int, x2: int, y2: int, duration_ms: int = 300) -> None: ...
    def type_text(self, text: str) -> None: ...
    def key(self, name: str) -> None: ...
    def launch(self, package: str) -> None: ...
    def stop(self, package: str) -> None: ...
    def current_app(self) -> str | None: ...
    def app_version(self, package: str) -> str | None: ...
    def install_from_store(self, package: str, timeout_s: int = 900) -> None: ...
    def healthy(self) -> bool: ...


# Errors of a connection adb drops and brings back by itself: on Windows a "[WinError 10054] An existing
# connection was forcibly closed by the remote host" (ConnectionResetError) in the middle of a tap, a wait or a
# solver run. Six sessions of 2026-10-03/04 met it; the three that reached the command crashed it (a `solve --run`
# [s:20261003-235233-chrono-2FYKPJ#35], a `wait 15` that lost the only frame of a win screen
# [s:20261003-194350-chrono-2FYKPJ#6], a tap [s:20261003-195050-chrono-2FYKPJ#6]); the next command worked.
TRANSIENT = (ConnectionResetError, ConnectionAbortedError, BrokenPipeError)
# The phone drops off USB and is back seconds later: 2026-10-06, 12 of 36 sessions met "device 'R5GL72FYKPJ' not
# found" (adb's answer while the phone re-enumerates) or a reset; the next command, seconds later, worked in nine
# of them, and four sessions ended blocked on it [s:20261006-105231-chrono-2FYKPJ#15]
# [s:20261006-104733-chrono-2FYKPJ#4] [s:20261006-113518-chrono-2FYKPJ#27] [s:20261006-122751-chrono-2FYKPJ#48].
# The one retry a second later was too early for most: now the phone is waited for (local.yaml android.reconnect_s,
# 30 s by default) before the call is made once more.
RECONNECT_S = 30


def device_gone(ex: Exception) -> bool:
    """adb's errors while the phone is off the bus: the serial not found, or the server itself unreachable."""
    msg = str(ex)
    return "not found" in msg or "connect to adb server failed" in msg


class Retrying:
    """adbutils' device behind one retry: a call that dies of a transient error, or finds the device gone, waits
    for the device to be back (up to reconnect_s) and is made once more on a fresh connection. Anything else
    comes through as it is."""

    def __init__(self, make, sleep_s: float = 1.0, present=None, reconnect_s: float = RECONNECT_S):
        self._make, self._sleep, self._present, self._reconnect_s = make, sleep_s, present, reconnect_s
        self._dev = make()
        self.reconnects = 0
        self.waited_s = 0.0

    def _back(self) -> bool:
        """Wait for the device to be present again; True when it is (or when nothing can tell)."""
        time.sleep(self._sleep)
        if self._present is None:
            return True
        t0 = time.monotonic()
        waited = 0.0
        while True:
            try:
                if self._present():
                    self.waited_s += waited
                    return True
            except Exception:
                pass
            if waited >= self._reconnect_s:
                self.waited_s += waited
                return False
            time.sleep(self._sleep)
            waited = max(waited + self._sleep, time.monotonic() - t0)

    def __getattr__(self, name):
        attr = getattr(self._dev, name)
        if not callable(attr):
            return attr

        def call(*a, **k):
            try:
                return attr(*a, **k)
            except TRANSIENT:
                self._back()
            except Exception as ex:
                if not device_gone(ex) or not self._back():
                    raise
            self._dev = self._make()
            self.reconnects += 1
            return getattr(self._dev, name)(*a, **k)

        return call


class AndroidDevice:
    """A phone/tablet over USB or Wi-Fi ADB, or an emulator with ADB."""

    KEYS = {
        "back": "KEYCODE_BACK",
        "home": "KEYCODE_HOME",
        "enter": "KEYCODE_ENTER",
        "app_switch": "KEYCODE_APP_SWITCH",
        "wake": "KEYCODE_WAKEUP",
    }

    def __init__(self, serial: str, prepare: bool = True, reconnect_s: float = RECONNECT_S):
        import adbutils

        self.name = serial

        def present() -> bool:
            return any(d.serial == serial for d in adbutils.adb.device_list())

        self.adb = Retrying(lambda: adbutils.adb.device(serial=serial), present=present, reconnect_s=reconnect_s)
        size = self.adb.window_size()
        self.width, self.height = size.width, size.height
        if prepare:
            self._prepare()

    # --- internals -------------------------------------------------------
    def _prepare(self) -> None:
        """Wake the screen. The phone's settings are left alone: it may be personal, and a phone setting is
        changed only when local.yaml turns it on (the owner, 2026-10-02). Staying awake while charging was
        set here for good; now sw.py start sets it for a session with android.stay_awake and end restores it."""
        self.adb.shell("input keyevent KEYCODE_WAKEUP")

    # --- perception ------------------------------------------------------
    def screenshot(self) -> Image.Image:
        # ~0.2–0.5 s via screencap; for games that need fast reactions see ScrcpyScreen.
        return self.adb.screenshot().convert("RGB")

    # --- actions ---------------------------------------------------------
    def tap(self, x: int, y: int) -> None:
        self.adb.click(int(x), int(y))

    def double_tap(self, x: int, y: int) -> None:
        # Two separate adb calls are too far apart for a double tap; the first tap goes to the background
        # and the second follows 80 ms later in the same shell (found by the player in Akari, 2026-10-01).
        self.adb.shell(f"input tap {int(x)} {int(y)} & sleep 0.08; input tap {int(x)} {int(y)}")

    def long_press(self, x: int, y: int, duration_ms: int = 800) -> None:
        self.adb.swipe(int(x), int(y), int(x), int(y), duration_ms / 1000)

    def swipe(self, x1: int, y1: int, x2: int, y2: int, duration_ms: int = 300) -> None:
        self.adb.swipe(int(x1), int(y1), int(x2), int(y2), duration_ms / 1000)

    def type_text(self, text: str) -> None:
        if text.isascii():
            self.adb.shell(f"input text {shlex.quote(text.replace(' ', '%s'))}")
            return
        # Cyrillic and other Unicode: needs the ADBKeyboard keyboard (install its APK
        # and select it as the current IME); it accepts text via broadcast.
        payload = base64.b64encode(text.encode("utf-8")).decode()
        self.adb.shell(f"am broadcast -a ADB_INPUT_B64 --es msg {payload}")

    def key(self, name: str) -> None:
        self.adb.keyevent(self.KEYS.get(name, name))

    # --- apps ------------------------------------------------------------
    def launch(self, package: str) -> None:
        self.adb.app_start(package)  # adbutils finds the launcher activity itself

    def stop(self, package: str) -> None:
        self.adb.app_stop(package)

    def current_app(self) -> str | None:
        try:
            return self.adb.app_current().package
        except Exception:
            return None

    def app_version(self, package: str) -> str | None:
        out = self.adb.shell(f"dumpsys package {package}")
        m = re.search(r"versionName=(\S+)", out)
        return m.group(1) if m else None

    def install_from_store(self, package: str, timeout_s: int = 900) -> None:
        """Install or update the game through the Play Store.

        The Play Store is an ordinary Android app with a UI tree, so buttons can be
        found by text through uiautomator2. Unity games cannot be automated this way
        (their tree is empty): for them, vision only.
        """
        import uiautomator2 as u2

        ui = u2.connect(self.name)
        self.adb.shell(f"am start -a android.intent.action.VIEW -d market://details?id={package}")
        # Button labels in English and Russian (the Russian ones are written as \u escapes)
        action = ui(textMatches="(?i)^(install|update|\u0443\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c|\u043e\u0431\u043d\u043e\u0432\u0438\u0442\u044c)$")
        if action.wait(timeout=30):
            action.click()
        else:
            # No button: either the game is already installed and up to date, or it is unavailable in the region.
            # --user 0: Samsung has a second user (Secure Folder); without the flag pm fails
            if f"package:{package}" in self.adb.shell(f"pm list packages --user 0 {package}"):
                return
            raise RuntimeError(f"{package}: no install button in the Play Store")
        done = ui(textMatches="(?i)^(open|play|\u043e\u0442\u043a\u0440\u044b\u0442\u044c|\u0438\u0433\u0440\u0430\u0442\u044c)$")
        if not done.wait(timeout=timeout_s):
            raise TimeoutError(f"{package}: installation did not finish within {timeout_s} s")

    def healthy(self) -> bool:
        try:
            return self.adb.get_state() == "device" and self.adb.shell("echo ok").strip() == "ok"
        except Exception:
            return False


class ScrcpyScreen:
    """Fast frames (up to 30–60 fps) instead of screencap, for games where reaction time matters.

    pip install scrcpy-client av. The frame arrives downscaled to max_width, so
    coordinates taken from it must be multiplied by device.width / frame.width.
    """

    def __init__(self, serial: str, max_width: int = 720, max_fps: int = 15):
        import scrcpy

        self.client = scrcpy.Client(device=serial, max_width=max_width, max_fps=max_fps, stay_awake=True)
        self.client.start(threaded=True)
        deadline = time.time() + 10
        while self.client.last_frame is None and time.time() < deadline:
            time.sleep(0.05)

    def frame(self) -> Image.Image:
        return Image.fromarray(self.client.last_frame[:, :, ::-1])  # BGR -> RGB

    def close(self) -> None:
        self.client.stop()
