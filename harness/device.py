"""Единый интерфейс устройства и реализация для Android через ADB.

Зависимости: pip install adbutils uiautomator2 pillow
Опционально: pip install scrcpy-client av  (быстрый видеопоток, класс ScrcpyScreen)

Один и тот же интерфейс реализуют телефон по USB, Google Play Games Developer
Emulator (adb connect localhost:6520) и окно Google Play Games на ПК (gpg_windows.py).
Координаты во всех методах — физические пиксели экрана устройства.
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
    """Телефон/планшет по USB или Wi-Fi ADB, либо эмулятор с ADB."""

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

    # --- служебное -------------------------------------------------------
    def _prepare(self) -> None:
        """Минимум для круглосуточной работы. Яркость и автоповорот не трогаем: телефон
        может быть личным, а ориентацию игра выставляет сама."""
        if self.adb.shell("settings get global stay_on_while_plugged_in").strip() in ("", "0", "null"):
            self.adb.shell("settings put global stay_on_while_plugged_in 7")  # экран не гаснет на зарядке
        self.adb.shell("input keyevent KEYCODE_WAKEUP")

    # --- восприятие ------------------------------------------------------
    def screenshot(self) -> Image.Image:
        # ~0.2–0.5 с через screencap; для игр с быстрой реакцией см. ScrcpyScreen.
        return self.adb.screenshot().convert("RGB")

    # --- действия --------------------------------------------------------
    def tap(self, x: int, y: int) -> None:
        self.adb.click(int(x), int(y))

    def long_press(self, x: int, y: int, duration_ms: int = 800) -> None:
        self.adb.swipe(int(x), int(y), int(x), int(y), duration_ms / 1000)

    def swipe(self, x1: int, y1: int, x2: int, y2: int, duration_ms: int = 300) -> None:
        self.adb.swipe(int(x1), int(y1), int(x2), int(y2), duration_ms / 1000)

    def type_text(self, text: str) -> None:
        if text.isascii():
            self.adb.shell(f"input text {shlex.quote(text.replace(' ', '%s'))}")
            return
        # Кириллица и прочий Unicode: нужна клавиатура ADBKeyboard (установите её APK
        # и выберите как текущий IME), она принимает текст через broadcast.
        payload = base64.b64encode(text.encode("utf-8")).decode()
        self.adb.shell(f"am broadcast -a ADB_INPUT_B64 --es msg {payload}")

    def key(self, name: str) -> None:
        self.adb.keyevent(self.KEYS.get(name, name))

    # --- приложения ------------------------------------------------------
    def launch(self, package: str) -> None:
        self.adb.app_start(package)  # adbutils сам находит launcher-activity

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
        """Установить или обновить игру через Play Store.

        Play Store — обычное Android-приложение с деревом UI, поэтому кнопки можно
        находить по тексту через uiautomator2. Игры на Unity так автоматизировать
        нельзя (у них дерево пустое) — для них только зрение.
        """
        import uiautomator2 as u2

        ui = u2.connect(self.name)
        self.adb.shell(f"am start -a android.intent.action.VIEW -d market://details?id={package}")
        action = ui(textMatches="(?i)^(install|update|установить|обновить)$")
        if action.wait(timeout=30):
            action.click()
        else:
            # Кнопки нет: либо уже установлено и актуально, либо игра недоступна в регионе.
            # --user 0: на Samsung есть второй пользователь (Secure Folder), без флага pm падает
            if f"package:{package}" in self.adb.shell(f"pm list packages --user 0 {package}"):
                return
            raise RuntimeError(f"{package}: нет кнопки установки в Play Store")
        done = ui(textMatches="(?i)^(open|play|открыть|играть)$")
        if not done.wait(timeout=timeout_s):
            raise TimeoutError(f"{package}: установка не завершилась за {timeout_s} с")

    def healthy(self) -> bool:
        try:
            return self.adb.get_state() == "device" and self.adb.shell("echo ok").strip() == "ok"
        except Exception:
            return False


class ScrcpyScreen:
    """Быстрые кадры (до 30–60 fps) вместо screencap — для игр, где важна реакция.

    pip install scrcpy-client av. Кадр приходит уменьшенным до max_width, поэтому
    координаты из него нужно умножать на device.width / frame.width.
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
