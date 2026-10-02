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


class AndroidDevice:
    """A phone/tablet over USB or Wi-Fi ADB, or an emulator with ADB."""

    KEYS = {
        "back": "KEYCODE_BACK",
        "home": "KEYCODE_HOME",
        "enter": "KEYCODE_ENTER",
        "app_switch": "KEYCODE_APP_SWITCH",
        "wake": "KEYCODE_WAKEUP",
    }

    def __init__(self, serial: str, prepare: bool = True):
        import adbutils

        self.name = serial
        self.adb = adbutils.adb.device(serial=serial)
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
