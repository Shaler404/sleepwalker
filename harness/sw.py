"""sw — руки и глаза агента Sleepwalker на телефонах и эмуляторах Android.

Команды запускаются из корня репозитория. Если идёт несколько сессий (несколько телефонов),
сессию выбирает -d SERIAL или переменная SW_DEVICE.

Планирование
  claim                                  занять свободные телефоны играми, у которых есть работа
  status                                 что идёт сейчас на каждом телефоне
  sync                                   подтянуть origin/main (только fast-forward)
Сессия
  start GAME KIND                        запуск игры и записи экрана, первый кадр (KIND: explore | update)
  shot | wait SEC | launch               кадр / подождать и кадр / вернуть игру на экран
  tap X Y --why ... | swipe X1 Y1 X2 Y2 --why ... | key back --why ... | text "..." --why ...
  note TYPE "факт" | mark "заголовок" "описание" | clip begin "заголовок" | clip end "описание"
  feature ID "Название" [--status seen|in_progress|documented]
  case FEATURE ID "что проверить" [--done] [--after-hours N | --after 2026-10-01T09:00]
  discovery open|closed                  все ли разделы игры найдены
  skill list | skill run NAME --why ...
  end --status ok|stuck|crashed|blocked|interrupted --summary "..."
Знания
  features GAME                          карта фичей: из вики + свежие записи этой машины
  pending                                сессии этой машины, которые ещё не прошли «сон»
  stats [GAME]                           скорость наигрыша по сессиям
«Сон»
  snapshot GAME OUT --until ISO          карта фичей в вики с отметкой, до какого момента учтены журналы
  render GAME_DIR                        features.md из features.yaml
  skill new GAME NAME --session SID --steps A-B --desc "..." --out SKILLS_DIR
  wiki-img SRC GAME_DIR SLUG | wiki-clip SRC GAME_DIR SLUG
  check-zones WORKTREE [--process]       правки только в разрешённых зонах, медиа в лимитах
Обслуживание
  gc | install-agents
"""
from __future__ import annotations

import argparse
import contextlib
import copy
import datetime as dt
import functools
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import time
from pathlib import Path

import yaml
from PIL import Image

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from perception import hash_distance, is_same_screen, prepare_for_model, save_for_wiki, screen_hash  # noqa: E402

ROOT = HERE.parent
KIND_RANK = {"update": 0, "explore": 1}
OPEN_STATUSES = ("seen", "in_progress", "recheck")
SHOT_TOKENS = 1500
HASH_MATCH = 12  # расстояние pHash, при котором экран считается тем же
# Окна поверх игры, которые не значат, что агент из неё ушёл
SYSTEM_OVERLAYS = ("com.google.android.permissioncontroller", "com.android.vending", "com.google.android.gms")
ZEN = {"0": "off", "1": "priority", "2": "none", "3": "alarms"}
DREAM_ZONES = ("wiki/", "skills/", "dreams/")
PROCESS_ZONES = ("runbooks/", "schema/", "harness/", "docs/", ".claude/", "project.yaml", "games.yaml",
                 "CLAUDE.md", "README.md", "local.example.yaml")

PROJECT_DEFAULTS = {"maintainers": [], "repo": "",
                    "session": {"budget_min": {"explore": 30, "update": 25}, "steps_per_min": 4,
                                "hard_limit": 1.5, "stale_min": 20}}
LOCAL_DEFAULTS = {
    "machine": "",
    "games": [],
    "android": {"serials": [], "hours": "0-24", "dnd": True, "max_temp_c": 42, "min_battery": 20},
    "fake_devices": {},
    "tools": {"ffmpeg": "ffmpeg", "ffprobe": "ffprobe"},
    "video": {"record": True, "record_short_edge": 720, "record_bitrate": 2500000, "clip_max_seconds": 20,
              "clip_max_mb": 8, "clip_long_edge": 720, "clip_fps": 12, "clip_quality": 70},
    "youtube": {"enabled": False, "privacy": "private"},
    "raw": {"keep_originals_days": 3, "keep_shots_days": 14},
    "state_dir": "",
    "raw_dir": "",
}


# --- конфиги ---------------------------------------------------------------------

def merge(base: dict, over: dict) -> dict:
    out = dict(base)
    for k, v in (over or {}).items():
        out[k] = merge(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else v
    return out


def read_yaml(p: Path) -> dict:
    return (yaml.safe_load(p.read_text(encoding="utf-8")) or {}) if p.exists() else {}


@functools.cache
def P() -> dict:
    """Глобальные правила из project.yaml."""
    return merge(PROJECT_DEFAULTS, read_yaml(ROOT / "project.yaml"))


@functools.cache
def L() -> dict:
    """Настройки этой машины из local.yaml (путь можно подменить переменной SW_LOCAL)."""
    return merge(LOCAL_DEFAULTS, read_yaml(Path(os.environ.get("SW_LOCAL") or ROOT / "local.yaml")))


def machine() -> str:
    return re.sub(r"[^a-z0-9]+", "", (L()["machine"] or socket.gethostname()).lower())[:16] or "machine"


def STATE() -> Path:
    return Path(L()["state_dir"] or ROOT / "state")


def RAW() -> Path:
    return Path(L()["raw_dir"] or ROOT / "raw")


def games() -> list[dict]:
    only = set(L()["games"])
    res = []
    for i, g in enumerate(read_yaml(ROOT / "games.yaml").get("games") or []):
        e = {"enabled": True, "priority": i, "focus": [], **g}
        if e["enabled"] and (not only or e["id"] in only):
            res.append(e)
    return res


def find_game(game: str) -> dict:
    for e in games():
        if e["id"] == game:
            return e
    fail(f"игры {game} нет в games.yaml (или она выключена, или её нет в local.yaml games)")


# --- вывод и мелочи -----------------------------------------------------------------

def out(obj) -> None:
    print(json.dumps(obj, ensure_ascii=False, indent=1))


def fail(msg: str, code: int = 2, **extra) -> None:
    out({"error": msg, **extra})
    sys.exit(code)


def now_iso(t: float | None = None) -> str:
    return dt.datetime.fromtimestamp(t or time.time()).isoformat(timespec="seconds")


def iso_to_t(s) -> float:
    if not s:
        return 0.0
    return dt.datetime.fromisoformat(str(s)).timestamp()


def slug(text: str) -> str:
    tr = dict(zip("абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
                  ["a", "b", "v", "g", "d", "e", "e", "zh", "z", "i", "y", "k", "l", "m", "n", "o", "p", "r", "s",
                   "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya"]))
    s = "".join(tr.get(c, c) for c in text.lower())
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:40] or "item"


def devkey(dev: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", dev)


def append_jsonl(p: Path, rec: dict) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def read_jsonl(p: Path) -> list[dict]:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


@contextlib.contextmanager
def machine_lock(name: str = "claim", wait_s: int = 120):
    """Замок на всю машину: захват телефонов и git не идут из двух процессов сразу."""
    p = STATE() / "locks" / f"{name}.lock"
    p.parent.mkdir(parents=True, exist_ok=True)
    deadline = time.time() + wait_s
    while True:
        try:
            fd = os.open(p, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, str(os.getpid()).encode())
            os.close(fd)
            break
        except FileExistsError:
            if time.time() - p.stat().st_mtime > 600:  # замок от упавшего процесса
                p.unlink(missing_ok=True)
            elif time.time() > deadline:
                fail(f"замок {name} занят дольше {wait_s} с")
            time.sleep(0.5)
    try:
        yield
    finally:
        p.unlink(missing_ok=True)


# --- сессии -----------------------------------------------------------------------

def session_path(dev: str) -> Path:
    return STATE() / "sessions" / f"{devkey(dev)}.json"


def all_sessions() -> list[dict]:
    return [json.loads(p.read_text(encoding="utf-8")) for p in (STATE() / "sessions").glob("*.json")]


def save_session(cur: dict) -> None:
    p = session_path(cur["device"])
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(cur, ensure_ascii=False, indent=1), encoding="utf-8")


def stale(cur: dict) -> bool:
    return time.time() - cur["last_action"] > P()["session"]["stale_min"] * 60


def pick_session(args, active: bool = True) -> dict:
    dev = getattr(args, "device", None) or os.environ.get("SW_DEVICE")
    sessions = [s for s in all_sessions() if not active or s["status"] == "active"]
    if dev:
        sessions = [s for s in sessions if s["device"] == dev]
    if len(sessions) == 1:
        return sessions[0]
    if not sessions:
        fail("нет активной сессии" + (f" на {dev}" if dev else "") + ": сначала sw.py claim и sw.py start")
    fail("идёт несколько сессий: укажи телефон через -d SERIAL", devices=[s["device"] for s in sessions])


def log_step(cur: dict, rec: dict) -> None:
    append_jsonl(Path(cur["dir"]) / "steps.jsonl", {"t": round(time.time(), 2), "step": cur["step"], **rec})


# --- телефоны -------------------------------------------------------------------------

def in_hours(spec: str, hour: int) -> bool:
    a, b = (int(x) for x in str(spec).split("-"))
    return a <= hour < b if a <= b else hour >= a or hour < b


def adb(serial: str, *args: str, timeout: int = 30) -> str:
    return subprocess.run(["adb", "-s", serial, *args], capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=timeout).stdout


def devices() -> dict[str, str]:
    """Все устройства этой машины: {serial: платформа}. Эмуляторы видны в adb как обычные телефоны."""
    res: dict[str, str] = {}
    try:
        lines = subprocess.run(["adb", "devices"], capture_output=True, text=True, timeout=15).stdout.splitlines()
        wanted = L()["android"]["serials"]
        for ln in lines[1:]:
            if ln.endswith("\tdevice"):
                s = ln.split("\t")[0]
                if not wanted or s in wanted:
                    res[s] = "android"
    except (OSError, subprocess.TimeoutExpired):
        pass
    for name in L()["fake_devices"]:
        res[name] = "fake"
    return res


def installed(serial: str) -> set[str]:
    # --user 0: на Samsung есть второй пользователь (Secure Folder), без флага pm падает
    return {ln.replace("package:", "").strip() for ln in adb(serial, "shell", "pm list packages --user 0").splitlines()}


def app_version(serial: str, package: str) -> str | None:
    m = re.search(r"versionName=(\S+)", adb(serial, "shell", f"dumpsys package {package}"))
    return m.group(1) if m else None


def focus(serial: str) -> str | None:
    m = re.search(r"mCurrentFocus=Window\{\S+ \S+ ([\w.]+)", adb(serial, "shell", "dumpsys window | grep mCurrentFocus"))
    return m.group(1) if m else None


def locked(serial: str) -> bool:
    return "isKeyguardShowing=true" in adb(serial, "shell", "dumpsys window | grep isKeyguardShowing")


TOUCH_BLOCKED = ("касания блокирует защита Samsung от случайных касаний: закрыт датчик приближения. "
                 "Положите телефон экраном вверх и уберите всё с его верхнего края")


def touch_blocked(serial: str) -> bool:
    """Samsung затемняет экран и глотает касания, когда датчик приближения закрыт:
    видимо окно IgniteTouchProtectionPresenter."""
    cur = None
    for line in adb(serial, "shell", "dumpsys window windows").splitlines():
        if "Window #" in line:
            cur = line
        elif "isVisible=true" in line and cur and "TouchProtection" in cur:
            return True
    return False


def phone_status(serial: str, game_ids: set[str]) -> tuple[bool, str]:
    """Телефон может быть личным: не занимать его, когда им пользуются, он заблокирован, горячий или садится."""
    a = L()["android"]
    if not in_hours(a["hours"], dt.datetime.now().hour):
        return False, f"вне часов {a['hours']}"
    if locked(serial):
        return False, "экран заблокирован: PIN агент не вводит, разблокируйте телефон (на зарядке он не гаснет)"
    if touch_blocked(serial):
        return False, TOUCH_BLOCKED
    bat = adb(serial, "shell", "dumpsys battery")
    temp = int(re.search(r"temperature: (\d+)", bat).group(1)) / 10 if "temperature:" in bat else 0
    level = int(re.search(r"level: (\d+)", bat).group(1)) if "level:" in bat else 100
    if temp > a["max_temp_c"]:
        return False, f"телефон нагрет до {temp} °C"
    if level < a["min_battery"] and not re.search(r"(AC|USB) powered: true", bat):
        return False, f"заряд {level}% и нет зарядки"
    awake = "mWakefulness=Awake" in adb(serial, "shell", "dumpsys power | grep mWakefulness")
    app = focus(serial) or ""
    if awake and app and "launcher" not in app and app not in game_ids and app not in SYSTEM_OVERLAYS:
        return False, f"телефоном пользуются: на экране {app}"
    return True, "ok"


class FakeDevice:
    """Проверка без телефона (fake_devices в local.yaml): кадры по кругу из папки с картинками."""

    def __init__(self, cur: dict):
        folder = L()["fake_devices"][cur["device"]]
        self.files = sorted(p for p in Path(folder).iterdir() if p.suffix.lower() in (".png", ".jpg", ".webp"))
        self.cur = cur

    def screenshot(self) -> Image.Image:
        return Image.open(self.files[self.cur.get("fake_i", 0) % len(self.files)]).convert("RGB")

    def _next(self, *a, **k) -> None:
        self.cur["fake_i"] = self.cur.get("fake_i", 0) + 1

    tap = long_press = swipe = key = type_text = _next

    def launch(self, package: str) -> None: ...
    def stop(self, package: str) -> None: ...
    def app_version(self, package: str) -> None: return None


def open_device(cur: dict, prepare: bool = False):
    if cur["platform"] == "fake":
        return FakeDevice(cur)
    from device import AndroidDevice

    try:
        return AndroidDevice(cur["device"], prepare=prepare)
    except Exception as ex:
        fail(f"телефон {cur['device']} недоступен: {ex}", 3, hint="sw.py end --status blocked --summary ...")


def app_on_screen(cur: dict) -> str | None:
    return cur["game"] if cur["platform"] == "fake" else focus(cur["device"])


def guard(cur: dict) -> None:
    s = P()["session"]
    elapsed = (time.time() - cur["t0"]) / 60
    if elapsed > cur["budget_min"] * s["hard_limit"] or cur["step"] >= cur["max_steps"] * s["hard_limit"]:
        fail("жёсткий лимит сессии: действия больше не выполняются", 4,
             hint="обнови state/<game>/progress.md и заверши: sw.py end --status ok --summary ...")
    if cur["platform"] == "fake":
        return
    if locked(cur["device"]):
        fail("экран заблокирован: PIN агент не вводит", 3, hint="sw.py end --status blocked --summary ...")
    if touch_blocked(cur["device"]):
        fail(TOUCH_BLOCKED, 3, hint="sw.py end --status blocked --summary ...")


# --- кадры ----------------------------------------------------------------------------

def take_shot(cur: dict, dev) -> dict:
    img = dev.screenshot()
    app = app_on_screen(cur)
    cur["shots"] += 1
    k = cur["shots"]
    shots = Path(cur["dir"]) / "shots"
    img.save(shots / f"{k:05d}.jpg", quality=90)
    small, scale = prepare_for_model(img, SHOT_TOKENS)
    small_path = shots / f"{k:05d}_m.jpg"
    small.save(small_path, quality=85)
    h = screen_hash(img)
    same = is_same_screen(cur.get("last_hash"), h)
    cur["same_streak"] = cur["same_streak"] + 1 if same else 0
    cur.update(last_hash=h, scale=scale, last_shot=k, last_app=app, model_size=[small.width, small.height],
               phys=[img.width, img.height])
    elapsed = (time.time() - cur["t0"]) / 60
    info = {"shot": str(small_path), "shot_n": k, "size": [small.width, small.height], "app": app,
            "same_as_prev": same, "same_streak": cur["same_streak"],
            "time": f"{elapsed:.1f} / {cur['budget_min']} мин", "steps": f"{cur['step']} / {cur['max_steps']}"}
    warn = []
    if app == "com.google.android.permissioncontroller":
        warn.append("системный запрос разрешения: нажми «Don't allow» / «Не разрешать»")
    elif app and app != cur["game"] and app not in SYSTEM_OVERLAYS:
        warn.append(f"на экране не игра ({app}): back или sw.py launch. Этот кадр в вики не пойдёт")
    if cur["same_streak"] >= 3:
        warn.append(f"экран не меняется {cur['same_streak']} шага подряд: смени стратегию (back, другая зона, свайп, подождать)")
    if cur["same_streak"] >= 15:
        warn.append("застрял: заверши сессию, end --status stuck")
    if elapsed >= cur["budget_min"] or cur["step"] >= cur["max_steps"]:
        warn.append("бюджет исчерпан: запиши план следующей сессии и заверши эту (sw.py end). "
                    f"После {P()['session']['hard_limit']}× бюджета действия блокируются")
    if warn:
        info["warnings"] = warn
    return info


def action(args, name: str, fn, rec: dict, points: tuple = ()) -> None:
    cur = pick_session(args)
    w, h = cur.get("model_size") or (10 ** 6, 10 ** 6)
    if any(not (0 <= x <= w and 0 <= y <= h) for x, y in points):
        fail(f"координаты вне кадра {w}x{h}: указывай пиксели последнего кадра")
    guard(cur)
    dev = open_device(cur)
    fn(dev, cur["scale"])
    cur["step"] += 1
    cur["last_action"] = time.time()
    time.sleep(args.settle)
    size = cur.get("model_size")
    info = take_shot(cur, dev)
    log_step(cur, {"type": name, **rec, "why": args.why, "model_size": size, "settle": args.settle,
                   "shot": info["shot_n"], "same": info["same_as_prev"], "app": info["app"], "hash": cur["last_hash"]})
    save_session(cur)
    out(info)


# --- запись экрана и клипы ----------------------------------------------------------------

def start_recording(cur: dict) -> None:
    Lc = L()
    if not Lc["video"]["record"]:
        return
    d, v = Path(cur["dir"]), Lc["video"]
    if cur["platform"] == "fake":
        spec = {"kind": "ffmpeg", "cmd": [Lc["tools"]["ffmpeg"], "-y", "-loglevel", "error", "-re", "-f", "lavfi", "-i",
                                          "testsrc=size=360x780:rate=15", "-c:v", "libx264", "-preset", "ultrafast",
                                          "-pix_fmt", "yuv420p", str(d / "original.mkv")]}
    else:
        # На полном разрешении screenrecord многих телефонов не стартует (Encoder failed):
        # короткая сторона 720, 1080x2340 -> 720x1560.
        w, h = (int(x) for x in re.search(r"(\d+)x(\d+)", adb(cur["device"], "shell", "wm size")).groups())
        k = v["record_short_edge"] / min(w, h)
        spec = {"kind": "screenrecord", "serial": cur["device"], "sid": cur["id"],
                "size": f"{int(w * k) // 2 * 2}x{int(h * k) // 2 * 2}", "bitrate": str(v["record_bitrate"])}
    spec["ffmpeg"] = Lc["tools"]["ffmpeg"]
    (d / "rec.cmd.json").write_text(json.dumps(spec), encoding="utf-8")
    flags = 0x00000008 | 0x00000200  # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
    subprocess.Popen([sys.executable, str(HERE / "sw.py"), "_rec", str(d)], creationflags=flags,
                     stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=open(d / "rec.log", "a"))
    cur["rec"] = {"kind": spec["kind"], "t0": time.time()}


def cmd_rec(args) -> None:
    """Фоновый процесс записи. Останавливается файлом rec.stop: screenrecord получает SIGINT
    и дописывает сегмент, ffmpeg — 'q' в stdin."""
    d = Path(args.dir)
    spec = json.loads((d / "rec.cmd.json").read_text(encoding="utf-8"))
    stop = d / "rec.stop"
    if spec["kind"] == "ffmpeg":
        p = subprocess.Popen(spec["cmd"], stdin=subprocess.PIPE)
        while p.poll() is None and not stop.exists():
            time.sleep(0.5)
        if p.poll() is None:
            p.stdin.write(b"q")
            p.stdin.flush()
            try:
                p.wait(30)
            except subprocess.TimeoutExpired:
                p.kill()
    else:
        serial, i = spec["serial"], 0
        while not stop.exists():
            remote, t = f"/sdcard/sw_rec_{spec['sid']}_{i:03d}.mp4", time.time()
            # screenrecord пишет не дольше 180 с, поэтому запись идёт сегментами
            p = subprocess.Popen(["adb", "-s", serial, "shell", "screenrecord", "--size", spec["size"],
                                  "--bit-rate", spec["bitrate"], "--time-limit", "180", remote])
            while p.poll() is None and not stop.exists():
                time.sleep(0.5)
            if p.poll() is None:
                subprocess.run(["adb", "-s", serial, "shell", "pkill", "-INT", "screenrecord"], timeout=15)
                try:
                    p.wait(20)
                except subprocess.TimeoutExpired:
                    p.kill()
            t_end = time.time()
            time.sleep(1)
            local = d / f"seg_{i:03d}.mp4"
            subprocess.run(["adb", "-s", serial, "pull", remote, str(local)], capture_output=True, timeout=600)
            subprocess.run(["adb", "-s", serial, "shell", "rm", "-f", remote], timeout=15)
            if local.exists() and local.stat().st_size > 0:
                append_jsonl(d / "segments.jsonl", {"file": local.name, "t": t, "t_end": t_end})
            i += 1
        segs = read_jsonl(d / "segments.jsonl")
        if segs:
            (d / "segments.txt").write_text("".join(f"file '{s['file']}'\n" for s in segs), encoding="utf-8")
            subprocess.run([spec["ffmpeg"], "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                            "-i", str(d / "segments.txt"), "-map", "0:v", "-c", "copy", str(d / "original.mkv")])
    (d / "rec.done").write_text("1")


def probe(path: Path, what: str) -> str:
    return subprocess.run([L()["tools"]["ffprobe"], "-v", "error", "-show_entries", what, "-of", "csv=p=0", str(path)],
                          capture_output=True, text=True).stdout.strip()


def timeline(cur: dict) -> list[tuple[float, float, float]]:
    """(начало по часам, позиция в original.mkv, длительность) для каждого сегмента записи.
    Длительность — по ffprobe, а если в файле её нет (так пишут некоторые телефоны) — по часам."""
    segs = read_jsonl(Path(cur["dir"]) / "segments.jsonl")
    if not segs:
        return [(cur["rec"]["t0"], 0.0, float("inf"))]
    pos, tl = 0.0, []
    for s in segs:
        raw = probe(Path(cur["dir"]) / s["file"], "format=duration")
        dur = float(raw) if re.fullmatch(r"[\d.]+", raw or "") else s["t_end"] - s["t"]
        tl.append((s["t"], pos, dur))
        pos += dur
    return tl


def to_pos(tl, t: float) -> float | None:
    for t0, pos, dur in reversed(tl):
        if t >= t0:
            return pos + min(t - t0, dur)
    return tl[0][1] if tl else None


def encode_clip(src: Path, start: float, dur: float, dest: Path) -> None:
    """Клип — анимированный WebP: GitHub не показывает <video> из репозитория, а WebP
    проигрывается прямо в статье. Не влез в лимит — меньше качество, кадров и размер."""
    v = L()["video"]
    w, h = (int(x) for x in probe(src, "stream=width,height").splitlines()[0].split(","))
    for quality, fps, edge in ((v["clip_quality"], v["clip_fps"], v["clip_long_edge"]),
                               (v["clip_quality"] - 15, max(6, v["clip_fps"] - 4), v["clip_long_edge"] * 3 // 4),
                               (40, 6, v["clip_long_edge"] // 2)):
        k = min(1.0, edge / max(w, h))
        subprocess.run([L()["tools"]["ffmpeg"], "-y", "-loglevel", "error", "-ss", f"{start:.2f}", "-i", str(src),
                        "-t", f"{dur:.2f}", "-vf", f"fps={fps},scale={int(w * k)}:{int(h * k)}:flags=lanczos",
                        "-c:v", "libwebp_anim", "-lossless", "0", "-quality", str(quality), "-compression_level", "4",
                        "-loop", "0", "-an", str(dest)], check=True)
        if dest.stat().st_size <= v["clip_max_mb"] * 1024 * 1024:
            return


def cut_clips(cur: dict) -> list[dict]:
    d = Path(cur["dir"])
    src = d / "original.mkv"
    if not cur["clips"] or not src.exists():
        return []
    tl, max_s, res = timeline(cur), L()["video"]["clip_max_seconds"], []
    (d / "clips").mkdir(exist_ok=True)
    for n, c in enumerate(cur["clips"], 1):
        s, e = to_pos(tl, c["t0"]), to_pos(tl, c["t1"])
        if s is None or e is None or e - s < 1:
            continue
        parts = max(1, -(-int(e - s) // max_s))
        step = (e - s) / parts
        for j in range(parts):
            base = f"c{n:02d}-{slug(c['title'])}" + (f"-{j + 1}" if parts > 1 else "")
            dest = d / "clips" / f"{base}.webp"
            encode_clip(src, s + j * step, step, dest)
            res.append({"file": dest.as_posix(), "title": c["title"] + (f" ({j + 1}/{parts})" if parts > 1 else ""),
                        "desc": c.get("desc", ""), "original_start_s": round(s + j * step, 1),
                        "seconds": round(step, 1), "mb": round(dest.stat().st_size / 1048576, 2)})
    (d / "clips.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return res


# --- карта фичей ------------------------------------------------------------------------------
# Глобальная карта лежит в wiki/<game>/features.yaml и меняется только «сном» через pull request.
# Во время игры агент пишет изменения в локальный журнал state/<game>/features.jsonl. Текущая
# картина = глобальная карта + записи журнала новее отметки synced[<машина>] в этой карте.

def global_features(game: str, base: Path | None = None) -> dict:
    snap = read_yaml(base or ROOT / "wiki" / game / "features.yaml")
    snap.setdefault("game", game)
    snap.setdefault("version", None)
    snap.setdefault("discovery", "open")
    snap.setdefault("synced", {})
    snap.setdefault("features", [])
    return snap


def feature_ops(game: str) -> list[dict]:
    return read_jsonl(STATE() / game / "features.jsonl")


def find_feature(view: dict, fid: str, create: bool = True) -> dict | None:
    for f in view["features"]:
        if f["id"] == fid:
            return f
    if not create:
        return None
    f = {"id": fid, "name": fid, "status": "seen", "cases": []}
    view["features"].append(f)
    return f


def apply_op(view: dict, op: dict) -> None:
    kind = op["op"]
    if kind == "feature":
        f = find_feature(view, op["id"])
        for k in ("name", "status", "page"):
            if op.get(k):
                f[k] = op[k]
        if op.get("status") == "documented":
            f["version_seen"] = view.get("version")
    elif kind == "case":
        f = find_feature(view, op["feature"])
        c = next((c for c in f.setdefault("cases", []) if c["id"] == op["id"]), None)
        if c is None:
            c = {"id": op["id"], "text": op.get("text") or op["id"], "done": False}
            f["cases"].append(c)
        if op.get("text"):
            c["text"] = op["text"]
        if "after" in op:
            c["after"] = op["after"]
        if op.get("done"):
            c.update(done=True, source=op.get("source"), after=None)
        if f["status"] == "seen":
            f["status"] = "in_progress"
    elif kind == "discovery":
        view["discovery"] = op["value"]
    elif kind == "version" and not view.get("version"):
        view["version"] = op["value"]
    elif kind == "new_version":
        view["version"] = op["to"]
        view["discovery"] = "open"
        for f in view["features"]:
            if f.get("status") == "documented":
                f["status"] = "recheck"


def feature_view(game: str, until: float | None = None, base: Path | None = None) -> dict:
    view = copy.deepcopy(global_features(game, base))
    since = iso_to_t(view["synced"].get(machine()))
    for op in feature_ops(game):
        if op["t"] > since and (until is None or op["t"] <= until):
            apply_op(view, op)
    return view


def research_state(view: dict, now: float) -> dict:
    open_f = [f["id"] for f in view["features"] if f.get("status") in OPEN_STATUSES]
    due, waiting = [], []
    for f in view["features"]:
        for c in f.get("cases", []):
            if c.get("done"):
                continue
            after = iso_to_t(c.get("after"))
            (waiting if after > now else due).append({"feature": f["id"], "case": c["id"], "after": c.get("after")})
    wake = min((w["after"] for w in waiting), default=None)
    complete = view["discovery"] == "closed" and not open_f and not due and not waiting and view["features"]
    return {"open_features": open_f, "due_cases": due, "waiting_cases": waiting, "wake": wake,
            "discovery": view["discovery"], "complete": bool(complete)}


def due_kind(view: dict, installed_version: str | None, now: float) -> tuple[str | None, str]:
    rs = research_state(view, now)
    if installed_version and view.get("version") and installed_version != view["version"]:
        return "update", f"новая версия {view['version']} → {installed_version}: перепроверить фичи и найти новые"
    if not view["features"]:
        return "explore", "игра ещё не изучена: первая сессия — обзор и список фичей"
    if rs["due_cases"] or rs["open_features"] or rs["discovery"] == "open":
        return "explore", (f"не разобрано фичей: {len(rs['open_features'])}, кейсов к проверке: {len(rs['due_cases'])}, "
                           f"разделы найдены: {'да' if rs['discovery'] == 'closed' else 'нет'}")
    if rs["waiting_cases"]:
        return None, f"ждёт до {rs['wake']}: кейсы, которые нельзя проверить раньше"
    return None, "всё изучено: спит до новой версии"


def log_op(cur: dict, op: dict) -> None:
    op = {"t": round(time.time(), 2), "session": cur["id"], "step": cur["step"], **op}
    append_jsonl(STATE() / cur["game"] / "features.jsonl", op)
    log_step(cur, {"type": "research", **{k: v for k, v in op.items() if k not in ("t", "step")}})


def summary_of(view: dict) -> dict:
    rs = research_state(view, time.time())
    return {"version": view.get("version"), "features": len(view["features"]),
            "documented": sum(f.get("status") == "documented" for f in view["features"]),
            **{k: rs[k] for k in ("open_features", "discovery", "wake", "complete")},
            "due_cases": len(rs["due_cases"]), "waiting_cases": len(rs["waiting_cases"])}


# --- команды: планирование -------------------------------------------------------------------

def last_session_t(game: str) -> float:
    rows = read_jsonl(STATE() / game / "sessions.jsonl")
    return iso_to_t(rows[-1]["started"]) if rows else 0.0


def read_first(game: str) -> list[str]:
    files = [ROOT / "wiki" / "_common" / "agent-lessons.md"] + \
            [ROOT / "wiki" / game / "agent" / n for n in ("lessons.md", "routes.md", "tactics.md")] + \
            [STATE() / game / "progress.md"]
    return [str(f) for f in files if f.exists()]


def cmd_claim(args) -> None:
    res, now = [], time.time()
    with machine_lock():
        for cur in all_sessions():
            if stale(cur):
                finish(cur, "abandoned", "сессия брошена: процесс не завершил её вовремя")
        sessions = all_sessions()
        busy_games = {s["game"] for s in sessions}
        busy_devs = {s["device"]: s for s in sessions}
        entries = games()
        for dev, platform in devices().items():
            if args.device and dev != args.device:
                continue
            if dev in busy_devs:
                res.append({"device": dev, "action": "busy", "game": busy_devs[dev]["game"]})
                continue
            if platform == "android":
                ok, reason = phone_status(dev, {e["id"] for e in entries})
                if not ok:
                    res.append({"device": dev, "action": "idle", "reason": reason})
                    continue
                have = installed(dev)
            else:
                have = {e["id"] for e in entries}
            cands, sleeping, missing = [], [], []
            for e in entries:
                if e["id"] in busy_games:
                    continue
                if e["id"] not in have:
                    missing.append(e["id"])
                    continue
                view = feature_view(e["id"])
                v = app_version(dev, e["id"]) if platform == "android" else view.get("version")
                kind, why = due_kind(view, v, now)
                if kind:
                    cands.append((KIND_RANK[kind], e["priority"], last_session_t(e["id"]), e, kind, why))
                else:
                    sleeping.append({"game": e["id"], "why": why})
            if not cands:
                res.append({"device": dev, "action": "idle", "reason": "нечего играть", "sleeping": sleeping,
                            "not_installed": missing})
                continue
            _, _, _, e, kind, why = min(cands, key=lambda c: c[:3])
            s = P()["session"]
            budget = s["budget_min"][kind]
            save_session({"status": "reserved", "device": dev, "platform": platform, "game": e["id"], "kind": kind,
                          "t0": now, "last_action": now})
            busy_games.add(e["id"])
            res.append({"device": dev, "action": "play", "game": e["id"], "title": e.get("title", e["id"]),
                        "kind": kind, "why": why, "budget_min": budget, "max_steps": budget * s["steps_per_min"],
                        "focus": e["focus"], "read_first": read_first(e["id"])})
    out({"machine": machine(), "assignments": res})


def cmd_status(args) -> None:
    rows = []
    for cur in all_sessions():
        row = {"device": cur["device"], "game": cur["game"], "kind": cur["kind"], "status": cur["status"],
               "minutes": round((time.time() - cur["t0"]) / 60, 1), "stale": stale(cur)}
        if cur["status"] == "active":
            steps = read_jsonl(Path(cur["dir"]) / "steps.jsonl")
            row.update(session=cur["id"], steps=cur["step"], last_shot=str(Path(cur["dir"]) / "shots" /
                                                                           f"{cur.get('last_shot', 0):05d}.jpg"),
                       recent=[{k: s.get(k) for k in ("step", "type", "why", "text", "title") if s.get(k) is not None}
                               for s in steps[-6:]])
        rows.append(row)
    free = [d for d in devices() if d not in {r["device"] for r in rows}]
    out({"machine": machine(), "sessions": rows, "free_devices": free})


def cmd_sync(args) -> None:
    with machine_lock("git"):
        f = subprocess.run(["git", "-C", str(ROOT), "fetch", "-q", "origin"], capture_output=True, text=True)
        m = subprocess.run(["git", "-C", str(ROOT), "merge", "--ff-only", "-q", "origin/main"], capture_output=True,
                           text=True)
    ok = f.returncode == 0 and m.returncode == 0
    out({"synced": ok, "head": subprocess.run(["git", "-C", str(ROOT), "log", "-1", "--format=%h %s"],
                                              capture_output=True, text=True).stdout.strip(),
         **({} if ok else {"error": (f.stderr + m.stderr).strip()[-400:]})})


# --- команды: сессия ------------------------------------------------------------------------------

def cmd_start(args) -> None:
    e = find_game(args.game)
    s = P()["session"]
    with machine_lock():
        devs = devices()
        dev = args.device or os.environ.get("SW_DEVICE")
        if not dev:
            reserved = [x for x in all_sessions() if x["status"] == "reserved" and x["game"] == args.game]
            dev = reserved[0]["device"] if reserved else (list(devs)[:1] or [None])[0]
        if not dev or dev not in devs:
            fail(f"устройство {dev} не подключено", devices=list(devs))
        for other in all_sessions():
            if other["device"] == dev and not (other["status"] == "reserved" and other["game"] == args.game):
                if not stale(other):
                    fail(f"на {dev} уже идёт {other['game']}")
                finish(other, "abandoned", "сессия брошена")
            if other["device"] != dev and other["game"] == args.game and not stale(other):
                fail(f"{args.game} уже изучается на {other['device']}: одна игра — один процесс")
        platform, budget = devs[dev], args.budget or s["budget_min"][args.kind]
        sid = f"{dt.datetime.now():%Y%m%d-%H%M%S}-{machine()}-{devkey(dev)[-6:]}"
        d = RAW() / args.game / sid
        (d / "shots").mkdir(parents=True)
        cur = {"status": "active", "id": sid, "game": args.game, "title": e.get("title", args.game),
               "kind": args.kind, "platform": platform, "device": dev, "dir": str(d), "t0": time.time(),
               "last_action": time.time(), "step": 0, "shots": 0, "scale": 1.0, "same_streak": 0,
               "budget_min": budget, "max_steps": budget * s["steps_per_min"], "clips": [], "clip_open": None}
        save_session(cur)
    if platform == "android":
        if locked(dev):
            session_path(dev).unlink(missing_ok=True)
            shutil.rmtree(d)
            fail("экран заблокирован: PIN агент не вводит")
        if L()["android"]["dnd"]:
            # «Не беспокоить: только будильники» на время сессии: уведомления мессенджеров
            # не всплывают поверх игры и не попадают в кадры
            cur["zen_prev"] = adb(dev, "shell", "settings get global zen_mode").strip()
            adb(dev, "shell", "cmd notification set_dnd alarms")
    devobj = open_device(cur, prepare=True)
    devobj.launch(args.game)
    time.sleep(8 if platform == "android" else 0)
    cur["version"] = devobj.app_version(args.game)
    view = feature_view(args.game)
    if args.kind == "update" and cur["version"] and view.get("version") != cur["version"]:
        log_op(cur, {"op": "new_version", "from": view.get("version"), "to": cur["version"]})
    elif cur["version"] and not view.get("version"):
        log_op(cur, {"op": "version", "value": cur["version"]})
    start_recording(cur)
    log_step(cur, {"type": "start", "kind": args.kind, "platform": platform, "version": cur["version"]})
    info = take_shot(cur, devobj)
    log_step(cur, {"type": "shot", "shot": info["shot_n"], "app": info["app"], "hash": cur["last_hash"]})
    save_session(cur)
    out({"session": sid, "device": dev, "version": cur["version"], "research": summary_of(feature_view(args.game)),
         **info})


def cmd_shot(args) -> None:
    cur = pick_session(args)
    info = take_shot(cur, open_device(cur))
    log_step(cur, {"type": "shot", "shot": info["shot_n"], "app": info["app"], "hash": cur["last_hash"]})
    save_session(cur)
    out(info)


def cmd_wait(args) -> None:
    cur = pick_session(args)
    time.sleep(min(args.seconds, 60))
    cur["last_action"] = time.time()
    info = take_shot(cur, open_device(cur))
    log_step(cur, {"type": "wait", "seconds": args.seconds, "shot": info["shot_n"], "same": info["same_as_prev"],
                   "hash": cur["last_hash"]})
    save_session(cur)
    out(info)


def cmd_launch(args) -> None:
    cur = pick_session(args)
    guard(cur)
    dev = open_device(cur)
    dev.launch(cur["game"])
    cur["step"] += 1
    cur["last_action"] = time.time()
    time.sleep(4)
    info = take_shot(cur, dev)
    log_step(cur, {"type": "launch", "shot": info["shot_n"], "app": info["app"], "hash": cur["last_hash"]})
    save_session(cur)
    out(info)


def cmd_note(args) -> None:
    cur = pick_session(args)
    log_step(cur, {"type": "note", "kind": args.kind, "text": args.text, "shot": cur["last_shot"]})
    out({"ok": True})


def cmd_mark(args) -> None:
    cur = pick_session(args)
    if cur.get("last_app") not in (cur["game"], None):
        fail(f"последний кадр не из игры ({cur['last_app']}): в вики он не пойдёт")
    shot = Path(cur["dir"]) / "shots" / f"{cur['last_shot']:05d}.jpg"
    log_step(cur, {"type": "mark", "title": args.title, "desc": args.desc, "shot": cur["last_shot"],
                   "file": shot.as_posix()})
    out({"ok": True, "marked": str(shot)})


def cmd_clip(args) -> None:
    cur = pick_session(args)
    if args.edge == "begin":
        cur["clip_open"] = {"title": args.text, "t0": time.time() - 2}
    else:
        if not cur["clip_open"]:
            fail("клип не начат: sw.py clip begin \"заголовок\"")
        cur["clips"].append({**cur["clip_open"], "desc": args.text, "t1": time.time() + 1})
        cur["clip_open"] = None
    log_step(cur, {"type": f"clip_{args.edge}", "text": args.text})
    save_session(cur)
    out({"ok": True, "clips": len(cur["clips"])})


def cmd_feature(args) -> None:
    cur = pick_session(args)
    op = {"op": "feature", "id": slug(args.id), "name": args.name}
    if args.status:
        op["status"] = args.status
    log_op(cur, op)
    out({"ok": True, "feature": find_feature(feature_view(cur["game"]), slug(args.id), create=False)})


def cmd_case(args) -> None:
    cur = pick_session(args)
    op = {"op": "case", "feature": slug(args.feature), "id": slug(args.id)}
    if args.text:
        op["text"] = args.text
    if args.done:
        op.update(done=True, source=f"{cur['id']}#{cur['step']}")
    elif args.after_hours is not None:
        op["after"] = now_iso(time.time() + args.after_hours * 3600)
    elif args.after:
        op["after"] = dt.datetime.fromisoformat(args.after).isoformat(timespec="seconds")
    log_op(cur, op)
    out({"ok": True, "feature": find_feature(feature_view(cur["game"]), slug(args.feature), create=False)})


def cmd_discovery(args) -> None:
    cur = pick_session(args)
    log_op(cur, {"op": "discovery", "value": args.value})
    out({"ok": True, "research": summary_of(feature_view(cur["game"]))})


def finish(cur: dict, status: str, summary: str) -> dict:
    if cur["status"] == "reserved":
        session_path(cur["device"]).unlink(missing_ok=True)
        return {"released": cur["device"], "game": cur["game"]}
    d = Path(cur["dir"])
    if cur.get("clip_open"):
        cur["clips"].append({**cur["clip_open"], "desc": "", "t1": cur["last_action"] + 2})
    if cur.get("rec"):
        (d / "rec.stop").write_text("1")
        for _ in range(600):
            if (d / "rec.done").exists():
                break
            time.sleep(0.5)
    clips = cut_clips(cur)
    if cur["platform"] == "android":
        try:
            cur["version"] = app_version(cur["device"], cur["game"]) or cur.get("version")
            adb(cur["device"], "shell", f"am force-stop {cur['game']}")
            if cur.get("zen_prev") is not None:
                adb(cur["device"], "shell", f"cmd notification set_dnd {ZEN.get(cur['zen_prev'], 'off')}")
        except Exception as ex:
            log_step(cur, {"type": "warn", "text": f"stop: {ex}"})
    youtube = None
    if L()["youtube"]["enabled"] and (d / "original.mkv").exists():
        try:
            import youtube as yt

            youtube = yt.upload(d / "original.mkv", f"{cur['title']} · {cur['kind']} · {cur['id'][:15]}",
                                f"sleepwalker session {cur['id']}\n{summary}", L()["youtube"])
            (d / "original.mkv").unlink()
            for seg in d.glob("seg_*.mp4"):
                seg.unlink()
        except Exception as ex:
            log_step(cur, {"type": "warn", "text": f"youtube: {ex}"})
    progress = STATE() / cur["game"] / "progress.md"
    if progress.exists():
        shutil.copy2(progress, d / "progress.md")  # версия рабочей памяти на конец сессии
    steps = read_jsonl(d / "steps.jsonl")
    ops = [o for o in feature_ops(cur["game"]) if o.get("session") == cur["id"]]
    meta = {"id": cur["id"], "machine": machine(), "device": cur["device"], "game": cur["game"], "kind": cur["kind"],
            "version": cur.get("version"), "started": now_iso(cur["t0"]),
            "minutes": round((time.time() - cur["t0"]) / 60, 1), "steps": cur["step"], "status": status,
            "summary": summary, "marks": sum(s["type"] == "mark" for s in steps),
            "features_touched": len({o.get("id") if o["op"] == "feature" else o.get("feature") for o in ops
                                     if o["op"] in ("feature", "case")}),
            "cases_done": sum(1 for o in ops if o["op"] == "case" and o.get("done")),
            "clips": clips, "youtube": youtube}
    (d / "session.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    append_jsonl(STATE() / cur["game"] / "sessions.jsonl", {k: v for k, v in meta.items() if k != "clips"}
                 | {"clips": len(clips)})
    log_step(cur, {"type": "end", "status": status, "summary": summary})
    session_path(cur["device"]).unlink(missing_ok=True)
    return {"ended": cur["id"], "status": status, "dir": str(d), "marks": meta["marks"],
            "cases_done": meta["cases_done"], "clips": [c["file"] for c in clips], "youtube": youtube,
            "research": summary_of(feature_view(cur["game"]))}


def cmd_end(args) -> None:
    out(finish(pick_session(args, active=False), args.status, args.summary))


# --- навыки ---------------------------------------------------------------------------------------

def skills_dir(game: str) -> Path:
    return ROOT / "skills" / game


def cmd_skill(args) -> None:
    if args.skill_cmd == "list":
        game = args.game or pick_session(args)["game"]
        res = []
        for p in sorted(skills_dir(game).glob("*.yaml")):
            s = read_yaml(p)
            res.append({k: s.get(k) for k in ("name", "status", "description", "version")})
        return out({"game": game, "skills": res})
    if args.skill_cmd == "run":
        return skill_run(args)
    if args.skill_cmd == "new":
        return skill_new(args)


def skill_run(args) -> None:
    cur = pick_session(args)
    p = skills_dir(cur["game"]) / f"{args.name}.yaml"
    if not p.exists():
        fail(f"навыка {args.name} нет", hint="sw.py skill list")
    sk = read_yaml(p)
    if sk.get("status") == "broken":
        fail(f"навык {args.name} помечен broken: сделай руками")
    guard(cur)
    dev = open_device(cur)
    pre = take_shot(cur, dev)
    if hash_distance(sk["pre_hash"], cur["last_hash"]) > HASH_MATCH:
        log_step(cur, {"type": "skill", "name": args.name, "ok": False, "reason": "pre", "why": args.why})
        append_jsonl(STATE() / cur["game"] / "skills.jsonl", {"t": time.time(), "session": cur["id"], "skill": args.name,
                                                               "ok": False, "reason": "pre", "version": cur.get("version")})
        save_session(cur)
        fail("экран не тот, с которого начинается навык: сделай шаги руками", 5, shot=pre["shot"])
    w, h = cur["phys"]
    for st in sk["steps"]:
        if "tap" in st:
            dev.tap(int(st["tap"][0] * w), int(st["tap"][1] * h))
        elif "swipe" in st:
            x1, y1, x2, y2 = st["swipe"]
            dev.swipe(int(x1 * w), int(y1 * h), int(x2 * w), int(y2 * h))
        elif "key" in st:
            dev.key(st["key"])
        time.sleep(st.get("wait", 1.0))
    cur["step"] += len(sk["steps"])
    cur["last_action"] = time.time()
    info = take_shot(cur, dev)
    ok = hash_distance(sk["post_hash"], cur["last_hash"]) <= HASH_MATCH
    log_step(cur, {"type": "skill", "name": args.name, "ok": ok, "why": args.why, "shot": info["shot_n"],
                   "hash": cur["last_hash"]})
    append_jsonl(STATE() / cur["game"] / "skills.jsonl", {"t": time.time(), "session": cur["id"], "skill": args.name,
                                                           "ok": ok, "version": cur.get("version")})
    save_session(cur)
    out({"skill": args.name, "ok": ok, **info})


def skill_new(args) -> None:
    """Навык из транскрипта: шаги A..B сессии становятся макросом в долях экрана, экран до
    первого шага — предусловием, экран после последнего — постусловием."""
    d = next(RAW().glob(f"*/{args.session}"), None)
    if not d:
        fail(f"сессии {args.session} нет в raw/")
    a, b = (int(x) for x in args.steps.split("-"))
    rows = read_jsonl(d / "steps.jsonl")
    acts = [r for r in rows if r["type"] in ("tap", "swipe", "key") and a <= r["step"] <= b]
    if not acts:
        fail("в этом диапазоне нет действий tap/swipe/key")
    first_i = rows.index(acts[0])
    pre = next((r["hash"] for r in reversed(rows[:first_i]) if r.get("hash")), None)
    if not pre:
        fail("не найден кадр перед первым шагом")
    steps = []
    rel = lambda v, size: round(min(1.0, max(0.0, v / size)), 4)  # noqa: E731
    for r in acts:
        mw, mh = r.get("model_size") or [1, 1]
        wait = round(float(r.get("settle", 1.0)) + 0.5, 1)
        if r["type"] == "tap":
            steps.append({"tap": [rel(r["x"], mw), rel(r["y"], mh)], "wait": wait})
        elif r["type"] == "swipe":
            steps.append({"swipe": [rel(r["from"][0], mw), rel(r["from"][1], mh),
                                    rel(r["to"][0], mw), rel(r["to"][1], mh)], "wait": wait})
        else:
            steps.append({"key": r["key"], "wait": wait})
    meta = read_jsonl(d / "steps.jsonl")[0]
    sk = {"name": slug(args.name), "game": args.game, "description": args.desc, "status": "candidate",
          "version": meta.get("version"), "pre_hash": pre, "post_hash": acts[-1]["hash"], "steps": steps,
          "source": f"{args.session}#{a}-{b}"}
    outdir = Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)
    path = outdir / f"{sk['name']}.yaml"
    path.write_text(yaml.safe_dump(sk, allow_unicode=True, sort_keys=False), encoding="utf-8")
    out({"skill": str(path), "steps": len(steps)})


# --- команды: знания и «сон» ----------------------------------------------------------------------

def cmd_features(args) -> None:
    view = feature_view(args.game)
    print(yaml.safe_dump({"summary": summary_of(view), **view}, allow_unicode=True, sort_keys=False))


def dreamed_ids() -> set[str]:
    ids: set[str] = set()
    for p in (ROOT / "dreams").glob("*.md"):
        ids |= set(re.findall(r"\b\d{8}-\d{6}-[a-z0-9]+-[A-Za-z0-9_]+\b", p.read_text(encoding="utf-8")))
    return ids


def cmd_pending(args) -> None:
    done, res = dreamed_ids(), []
    for f in sorted(STATE().glob("*/sessions.jsonl")):
        for s in read_jsonl(f):
            if s["id"] in done or (s["status"] == "abandoned" and not s.get("steps")):
                continue
            d = RAW() / s["game"] / s["id"]
            res.append({**s, "raw": str(d) if d.exists() else None})
    # until — момент после конца последней сессии: snapshot учтёт журнал фичей до него
    end = max((iso_to_t(s["started"]) + s["minutes"] * 60 + 60 for s in res), default=None)
    out({"machine": machine(), "pending": res, "count": len(res), "until": now_iso(end) if end else None})


def cmd_stats(args) -> None:
    """Учится ли наигрыш: по сессиям — шагов на закрытый кейс, доля шагов без смены экрана,
    навыки. Сравнение первой и второй половины сессий каждой игры."""
    per_game = {}
    for f in sorted(STATE().glob("*/sessions.jsonl")):
        game = f.parent.name
        if args.game and game != args.game:
            continue
        rows = []
        runs = read_jsonl(STATE() / game / "skills.jsonl")
        for s in read_jsonl(f):
            steps = read_jsonl(RAW() / game / s["id"] / "steps.jsonl")
            acts = [x for x in steps if x["type"] in ("tap", "swipe", "key", "text", "launch")]
            sk = [r for r in runs if r["session"] == s["id"]]
            rows.append({"session": s["id"], "kind": s["kind"], "status": s["status"], "minutes": s["minutes"],
                         "steps": s["steps"], "cases_done": s.get("cases_done", 0),
                         "steps_per_case": round(s["steps"] / s["cases_done"], 1) if s.get("cases_done") else None,
                         "same_screen_rate": round(sum(bool(x.get("same")) for x in acts) / len(acts), 2) if acts else None,
                         "skills_ok": sum(r["ok"] for r in sk), "skills_fail": sum(not r["ok"] for r in sk)})
        half = len(rows) // 2

        def avg(xs, key):
            vals = [x[key] for x in xs if x[key] is not None]
            return round(sum(vals) / len(vals), 2) if vals else None

        per_game[game] = {"sessions": rows,
                          "trend": {k: {"first_half": avg(rows[:half], k), "second_half": avg(rows[half:], k)}
                                    for k in ("steps_per_case", "same_screen_rate")} if half else None}
    out({"machine": machine(), "games": per_game})


def cmd_snapshot(args) -> None:
    outp = Path(args.out)
    until = iso_to_t(args.until)
    view = feature_view(args.game, until=until, base=outp if outp.exists() else None)
    view["synced"][machine()] = now_iso(until)
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text("# Карта фичей. Пишет только «сон» (sw.py snapshot + правки по схеме).\n" +
                    yaml.safe_dump(view, allow_unicode=True, sort_keys=False), encoding="utf-8")
    out({"written": str(outp), **summary_of(view)})


def cmd_render(args) -> None:
    gd = Path(args.game_dir)
    view = global_features(gd.name, gd / "features.yaml")
    rs = research_state(view, time.time())
    docs = sum(f.get("status") == "documented" for f in view["features"])
    cases = [c for f in view["features"] for c in f.get("cases", [])]
    icon = {"seen": "🔎 замечена", "in_progress": "🛠 в работе", "documented": "✅ описана", "recheck": "🔁 перепроверить"}
    lines = [
        "# Фичи", "",
        f"Версия игры: **{view.get('version') or '—'}** · фичей: **{len(view['features'])}**, описано: **{docs}** · "
        f"кейсов закрыто: **{sum(c.get('done', False) for c in cases)} / {len(cases)}** · "
        f"все разделы найдены: **{'да' if view['discovery'] == 'closed' else 'нет'}**"
        + (f" · следующая проверка по таймеру: **{rs['wake']}**" if rs["wake"] else "")
        + (" · **изучено полностью, ждёт новой версии**" if rs["complete"] else ""), "",
        "Файл собирается из [`features.yaml`](features.yaml) командой `sw.py render`, руками не правится.", "",
        "| Фича | Статус | Кейсы | Ждёт до | Версия |", "|---|---|---|---|---|"]
    for f in view["features"]:
        fc = f.get("cases", [])
        wait = min((c["after"] for c in fc if not c.get("done") and c.get("after")), default="")
        name = f"[{f['name']}]({f['page']})" if f.get("page") else f["name"]
        lines.append(f"| {name} | {icon.get(f.get('status'), f.get('status'))} | "
                     f"{sum(c.get('done', False) for c in fc)} / {len(fc)} | {wait} | {f.get('version_seen') or ''} |")
    (gd / "features.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    out({"written": str(gd / "features.md"), "features": len(view["features"])})


def cmd_check_zones(args) -> None:
    w = Path(args.worktree)
    names = subprocess.run(["git", "-C", str(w), "diff", "--name-only", "origin/main"], capture_output=True,
                           text=True).stdout.split()
    names += [ln[3:] for ln in subprocess.run(["git", "-C", str(w), "status", "--porcelain", "--untracked-files=all"], capture_output=True,
                                              text=True).stdout.splitlines() if ln.startswith("??")]
    allowed = DREAM_ZONES + (PROCESS_ZONES if args.process else ())
    bad = sorted({n for n in names if not n.startswith(allowed)})
    media = []
    limit = L()["video"]["clip_max_mb"] * 1048576
    for n in set(names):
        p = w / n
        if p.is_file() and (p.suffix.lower() in (".mp4", ".mov", ".mkv") or
                            ("/clips/" in n and p.stat().st_size > limit) or
                            ("/img/" in n and p.stat().st_size > 1.5 * 1048576)):
            media.append(n)
    ok = not bad and not media
    out({"ok": ok, "outside_zones": bad, "media_over_limits": media, "changed": len(set(names))})
    sys.exit(0 if ok else 1)


def cmd_wiki_img(args) -> None:
    img = Image.open(args.src).convert("RGB")
    name = f"{dt.date.today():%Y%m%d}-{slug(args.slug)}-{screen_hash(img)[:8]}.webp"
    dest = Path(args.game_dir) / "img" / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        save_for_wiki(img, str(dest))
    out({"path": f"img/{name}", "kb": round(dest.stat().st_size / 1024)})


def cmd_wiki_clip(args) -> None:
    src, gd = Path(args.src), Path(args.game_dir)
    name = f"{dt.date.today():%Y%m%d}-{slug(args.slug)}.webp"
    (gd / "clips").mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, gd / "clips" / name)
    out({"path": f"clips/{name}", "mb": round((gd / "clips" / name).stat().st_size / 1048576, 2)})


def cmd_gc(args) -> None:
    now, freed, done = time.time(), 0, dreamed_ids()
    keep = L()["raw"]
    for d in RAW().glob("*/*/"):
        meta = d / "session.json"
        if not meta.exists():
            continue
        age_days = (now - meta.stat().st_mtime) / 86400
        m = json.loads(meta.read_text(encoding="utf-8"))
        victims = []
        if m.get("youtube") or age_days > keep["keep_originals_days"]:
            victims += [d / "original.mkv", *d.glob("seg_*.mp4")]
        if m["id"] in done and age_days > keep["keep_shots_days"]:
            victims += [d / "shots", d / "clips"]
        for v in victims:
            if v.exists():
                freed += sum(f.stat().st_size for f in v.rglob("*")) if v.is_dir() else v.stat().st_size
                shutil.rmtree(v) if v.is_dir() else v.unlink()
    out({"freed_mb": round(freed / 1048576, 1)})


def cmd_install_agents(args) -> None:
    """Роли с ограниченными инструментами (.claude/agents) в ~/.claude/agents: так их видят
    запланированные задачи, в какой бы папке они ни запускались."""
    dest = Path.home() / ".claude" / "agents"
    dest.mkdir(parents=True, exist_ok=True)
    done = []
    for p in (ROOT / ".claude" / "agents").glob("sleepwalker-*.md"):
        shutil.copy2(p, dest / p.name)
        done.append(p.name)
    out({"installed": done, "to": str(dest)})


# --- разбор аргументов --------------------------------------------------------------------------

def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(prog="sw", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-d", "--device", help="телефон (serial из adb devices); по умолчанию SW_DEVICE или единственная сессия")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("claim")
    sub.add_parser("status")
    sub.add_parser("sync")
    p = sub.add_parser("start")
    p.add_argument("game")
    p.add_argument("kind", choices=list(KIND_RANK))
    p.add_argument("--budget", type=int, help="минуты вместо значения из project.yaml")
    sub.add_parser("shot")
    sub.add_parser("launch")
    for name, nargs in (("tap", ["x", "y"]), ("swipe", ["x1", "y1", "x2", "y2"])):
        p = sub.add_parser(name)
        for n in nargs:
            p.add_argument(n, type=float)
    p = sub.add_parser("key")
    p.add_argument("name")
    p = sub.add_parser("text")
    p.add_argument("value")
    for name in ("tap", "swipe", "key", "text"):
        sp = sub.choices[name]
        sp.add_argument("--why", required=True, help="что ожидаешь увидеть после действия")
        sp.add_argument("--settle", type=float, default=1.0)
    p = sub.add_parser("wait")
    p.add_argument("seconds", type=float)
    p = sub.add_parser("note")
    p.add_argument("kind")
    p.add_argument("text")
    p = sub.add_parser("mark")
    p.add_argument("title")
    p.add_argument("desc")
    p = sub.add_parser("clip")
    p.add_argument("edge", choices=["begin", "end"])
    p.add_argument("text")
    p = sub.add_parser("feature")
    p.add_argument("id")
    p.add_argument("name")
    p.add_argument("--status", choices=["seen", "in_progress", "documented"])
    p = sub.add_parser("case")
    p.add_argument("feature")
    p.add_argument("id")
    p.add_argument("text", nargs="?")
    p.add_argument("--done", action="store_true")
    p.add_argument("--after-hours", type=float)
    p.add_argument("--after", help="не раньше этого времени, например 2026-10-01T09:00")
    p = sub.add_parser("discovery")
    p.add_argument("value", choices=["open", "closed"])
    p = sub.add_parser("skill")
    ss = p.add_subparsers(dest="skill_cmd", required=True)
    q = ss.add_parser("list")
    q.add_argument("game", nargs="?")
    q = ss.add_parser("run")
    q.add_argument("name")
    q.add_argument("--why", required=True)
    q = ss.add_parser("new")
    q.add_argument("game")
    q.add_argument("name")
    q.add_argument("--session", required=True)
    q.add_argument("--steps", required=True, help="диапазон шагов, например 12-15")
    q.add_argument("--desc", required=True)
    q.add_argument("--out", required=True, help="папка skills/<game> в worktree «сна»")
    p = sub.add_parser("end")
    p.add_argument("--status", required=True, choices=["ok", "stuck", "interrupted", "crashed", "blocked"])
    p.add_argument("--summary", required=True)
    p = sub.add_parser("features")
    p.add_argument("game")
    sub.add_parser("pending")
    p = sub.add_parser("stats")
    p.add_argument("game", nargs="?")
    p = sub.add_parser("snapshot")
    p.add_argument("game")
    p.add_argument("out")
    p.add_argument("--until", required=True)
    p = sub.add_parser("render")
    p.add_argument("game_dir")
    for name in ("wiki-img", "wiki-clip"):
        p = sub.add_parser(name)
        p.add_argument("src")
        p.add_argument("game_dir")
        p.add_argument("slug")
    p = sub.add_parser("check-zones")
    p.add_argument("worktree")
    p.add_argument("--process", action="store_true", help="разрешить правки процесса по замечанию мейнтейнера")
    sub.add_parser("gc")
    sub.add_parser("install-agents")
    p = sub.add_parser("_rec")
    p.add_argument("dir")
    args = ap.parse_args()

    s = lambda v, k: int(round(v * k))  # noqa: E731
    handlers = {
        "claim": cmd_claim, "status": cmd_status, "sync": cmd_sync, "start": cmd_start, "shot": cmd_shot,
        "wait": cmd_wait, "launch": cmd_launch, "note": cmd_note, "mark": cmd_mark, "clip": cmd_clip,
        "feature": cmd_feature, "case": cmd_case, "discovery": cmd_discovery, "skill": cmd_skill, "end": cmd_end,
        "features": cmd_features, "pending": cmd_pending, "stats": cmd_stats, "snapshot": cmd_snapshot,
        "render": cmd_render, "check-zones": cmd_check_zones, "wiki-img": cmd_wiki_img, "wiki-clip": cmd_wiki_clip,
        "gc": cmd_gc, "install-agents": cmd_install_agents, "_rec": cmd_rec,
        "tap": lambda a: action(a, "tap", lambda d, k: d.tap(s(a.x, k), s(a.y, k)), {"x": a.x, "y": a.y},
                                ((a.x, a.y),)),
        "swipe": lambda a: action(a, "swipe", lambda d, k: d.swipe(s(a.x1, k), s(a.y1, k), s(a.x2, k), s(a.y2, k)),
                                  {"from": [a.x1, a.y1], "to": [a.x2, a.y2]}, ((a.x1, a.y1), (a.x2, a.y2))),
        "key": lambda a: action(a, "key", lambda d, k: d.key(a.name), {"key": a.name}),
        "text": lambda a: action(a, "text", lambda d, k: d.type_text(a.value), {"text": a.value}),
    }
    handlers[args.cmd](args)


if __name__ == "__main__":
    main()
