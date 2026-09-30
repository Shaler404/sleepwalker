"""Оркестратор 24/7: очередь игр, воркер на каждое устройство, сторож, ночная компиляция.

Запуск: python harness/scheduler.py --devices R58M12345 localhost:6520
Игры берутся из games.yaml (включённые, с platform: android).

Приоритеты задач (что выбирает воркер, когда освобождается):
  1. onboard      — игра ещё не изучена
  2. update_diff  — версия в Play Store новее установленной
  3. event_scan   — прошло > 24 ч с последнего осмотра событий
  4. deep_revisit — прошло > 7 дней с последнего углублённого захода
Ночью (03:00) — compile_wiki для игр с новыми рефлексиями и lint раз в неделю.
"""
from __future__ import annotations

import argparse
import datetime as dt
import logging
import os
import sqlite3
import threading
import time
import traceback
from pathlib import Path

from compile_wiki import compile_game
from device import AndroidDevice
from explorer import run_session
from reflect import reflect

ROOT = Path(os.environ.get("SW_ROOT") or Path(__file__).resolve().parent.parent)  # корень репозитория (или worktree «сна»)
DB = ROOT / "state.sqlite"
log = logging.getLogger("scheduler")

BUDGET_MIN = {"onboard": 40, "update_diff": 25, "event_scan": 10, "deep_revisit": 30}
CADENCE_H = {"event_scan": 24, "deep_revisit": 24 * 7}
GOALS = {
    "onboard": "Первый запуск. Пройди обучение целиком, изучи главное меню, магазин, настройки, профиль; "
               "сыграй 3–5 раундов основного цикла. Запиши валюты, таймеры, офферы.",
    "update_diff": "Игра обновилась. Пройди по всем известным экранам и отметь изменения (NEW:/CHANGED: в mark_screen).",
    "event_scan": "Короткий осмотр: всплывающие окна при входе, раздел событий/новостей, магазин. "
                  "Для каждого события — название, условия, награды, таймер. Ничего не проходи.",
    "deep_revisit": "Закрой открытые вопросы из вики и играй дальше по основному циклу, фиксируя новые экраны и экономику.",
}

SCHEMA = """
create table if not exists games(
  package text primary key, priority int default 5, state text default 'new',
  store_version text, installed_version text, last_event_scan real default 0,
  last_deep real default 0, last_error text);
create table if not exists sessions(
  id text primary key, package text, device text, kind text,
  started real, ended real, status text);
"""


def db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB, check_same_thread=False, timeout=30)
    conn.executescript(SCHEMA)
    return conn


def next_task(conn: sqlite3.Connection, now: float) -> tuple[str, str] | None:
    row = conn.execute("select package from games where state='new' order by priority limit 1").fetchone()
    if row:
        return row[0], "onboard"
    row = conn.execute(
        "select package from games where state='known' and store_version is not null "
        "and installed_version is not null and store_version != installed_version order by priority limit 1").fetchone()
    if row:
        return row[0], "update_diff"
    for kind, col in (("event_scan", "last_event_scan"), ("deep_revisit", "last_deep")):
        row = conn.execute(
            f"select package from games where state='known' and {col} < ? order by {col} limit 1",
            (now - CADENCE_H[kind] * 3600,)).fetchone()
        if row:
            return row[0], kind
    return None


def check_store_versions(conn: sqlite3.Connection) -> None:
    """Раз в час: версия в Play Store. В google-play-scraper 1.2.7 поле recentChanges
    недоступно, поэтому смотрим version/updated, а «что нового» читает агент в игре."""
    from google_play_scraper import app

    for (pkg,) in conn.execute("select package from games").fetchall():
        try:
            info = app(pkg, lang="ru", country="ru")
            conn.execute("update games set store_version=? where package=?", (info.get("version"), pkg))
            conn.commit()
        except Exception as e:  # сеть, регион, снятая с публикации игра
            log.warning("store check %s: %s", pkg, e)


class Watchdog(threading.Thread):
    """Если игра вылетела или ушла с переднего плана — вернуть её. Зависание по экрану
    ловит сам Explorer (same_streak) и завершает сессию."""

    def __init__(self, device: AndroidDevice, package: str):
        super().__init__(daemon=True)
        self.device, self.package, self.stop_flag = device, package, threading.Event()

    def run(self) -> None:
        while not self.stop_flag.wait(30):
            try:
                if self.device.current_app() != self.package:
                    log.warning("%s: %s не на переднем плане, перезапуск", self.device.name, self.package)
                    self.device.launch(self.package)
            except Exception as e:
                log.error("watchdog %s: %s", self.device.name, e)


def recover(device: AndroidDevice) -> None:
    """ADB отвалился: переподключение; если не помогло — ждать, пока устройство вернётся."""
    import adbutils

    for _ in range(10):
        try:
            adbutils.adb.connect(device.name, timeout=5) if ":" in device.name else None
            if device.healthy():
                return
        except Exception:
            pass
        time.sleep(30)
    raise RuntimeError(f"{device.name}: устройство недоступно")


def worker(serial: str, stop: threading.Event) -> None:
    conn = db()
    device = AndroidDevice(serial)
    while not stop.is_set():
        task = next_task(conn, time.time())
        if not task:
            time.sleep(60)
            continue
        pkg, kind = task
        sid = f"{int(time.time())}-{serial}"
        conn.execute("insert into sessions values(?,?,?,?,?,?,?)", (sid, pkg, serial, kind, time.time(), None, "running"))
        conn.commit()
        try:
            if not device.healthy():
                recover(device)
            if kind in ("onboard", "update_diff"):
                device.install_from_store(pkg)
            device.launch(pkg)
            time.sleep(8)
            wd = Watchdog(device, pkg)
            wd.start()
            try:
                session_dir = run_session(device, pkg, GOALS[kind], minutes=BUDGET_MIN[kind])
            finally:
                wd.stop_flag.set()
            reflect(pkg, session_dir)
            now = time.time()
            conn.execute(
                "update games set state='known', installed_version=?, last_error=null, "
                "last_event_scan=case when ? in ('event_scan','onboard','update_diff') then ? else last_event_scan end, "
                "last_deep=case when ? in ('deep_revisit','onboard') then ? else last_deep end where package=?",
                (device.app_version(pkg), kind, now, kind, now, pkg))
            conn.execute("update sessions set ended=?, status='ok' where id=?", (now, sid))
            conn.commit()
        except Exception as e:
            log.error("%s %s %s: %s\n%s", serial, pkg, kind, e, traceback.format_exc())
            conn.execute("update games set last_error=? where package=?", (str(e)[:500], pkg))
            conn.execute("update sessions set ended=?, status='error' where id=?", (time.time(), sid))
            conn.commit()
            try:
                device.stop(pkg)
            except Exception:
                pass
            time.sleep(60)


def nightly(stop: threading.Event) -> None:
    conn = db()
    last_day = None
    while not stop.is_set():
        now = dt.datetime.now()
        if now.hour == 3 and last_day != now.date():
            last_day = now.date()
            for (pkg,) in conn.execute("select package from games where state='known'").fetchall():
                try:
                    compile_game(pkg, lint=(now.weekday() == 6))
                except Exception as e:
                    log.error("compile %s: %s", pkg, e)
        if now.minute == 7:  # раз в час проверить версии в сторе
            check_store_versions(conn)
        stop.wait(60)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--devices", nargs="+", required=True)
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    import yaml

    conn = db()
    cfg = yaml.safe_load((ROOT / "games.yaml").read_text(encoding="utf-8"))
    platform = (cfg.get("defaults") or {}).get("platform", "gpg")
    for i, g in enumerate(cfg.get("games") or []):
        if g.get("enabled", True) and g.get("platform", platform) == "android":
            conn.execute("insert or ignore into games(package, priority) values(?, ?)", (g["id"], g.get("priority", i)))
    conn.commit()

    stop = threading.Event()
    threads = [threading.Thread(target=worker, args=(d, stop), daemon=True, name=f"worker-{d}") for d in args.devices]
    threads.append(threading.Thread(target=nightly, args=(stop,), daemon=True, name="nightly"))
    for t in threads:
        t.start()
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        stop.set()


if __name__ == "__main__":
    main()
