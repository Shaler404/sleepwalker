"""sw — руки и глаза агента в рутине Claude Code (runbooks/play.md). Играет на телефоне по USB.

Команды вызываются из корня репозитория. Каждая пишет шаг в
raw/<game>/<session>/steps.jsonl: это транскрипт сессии, по которому «сон» ищет паттерны.
Координаты в tap/swipe — пиксели последнего кадра, который видела модель; в физические
пиксели их переводит sw.

  python harness/sw.py next                          что играть сейчас (JSON)
  python harness/sw.py start GAME KIND               запуск игры и записи экрана, первый кадр
  python harness/sw.py shot                          новый кадр
  python harness/sw.py tap X Y --why "..."           действие, в ответ новый кадр
  python harness/sw.py swipe X1 Y1 X2 Y2 --why "..."
  python harness/sw.py key back --why "..."          back | home | enter
  python harness/sw.py text "..." --why "..."
  python harness/sw.py wait SECONDS
  python harness/sw.py launch                        вернуть игру на экран
  python harness/sw.py note TYPE "факт"              economy | mechanic | ui | event | bug | question
  python harness/sw.py mark "заголовок" "что на кадре и что важно"
  python harness/sw.py clip begin "заголовок"        начало клипа для вики
  python harness/sw.py clip end "что показано"
  python harness/sw.py end --status ok --summary "..." [--onboarded]
  python harness/sw.py pending                       сессии, которые ещё не прошли «сон»
  python harness/sw.py wiki-img SRC GAME_DIR SLUG    кадр в вики: WebP <= 1080 px
  python harness/sw.py wiki-clip SRC GAME_DIR SLUG   клип (анимированный WebP) в вики
  python harness/sw.py gc                            чистка raw/ по срокам из local.yaml
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

import yaml
from PIL import Image

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from perception import is_same_screen, prepare_for_model, save_for_wiki, screen_hash  # noqa: E402

ROOT = HERE.parent
RAW = ROOT / "raw"
CURRENT = RAW / ".current.json"
KIND_RANK = {"update_diff": 0, "onboard": 1, "event_scan": 2, "deep_revisit": 3}
STALE_HOURS = 3  # сессия без действий дольше этого считается брошенной
SHOT_TOKENS = 1500
# Окна, которые появляются поверх игры и не значат, что агент ушёл из неё
SYSTEM_OVERLAYS = ("com.google.android.permissioncontroller", "com.android.vending", "com.google.android.gms")
ZEN = {"0": "off", "1": "priority", "2": "none", "3": "alarms"}

GAME_DEFAULTS = {
    "enabled": True,
    "event_scan_hours": 24,
    "revisit_hours": 72,
    "steps_per_min": 4,
    "budget_min": {"onboard": 30, "update_diff": 20, "event_scan": 10, "deep_revisit": 25},
    "goals": [],
    "kind_goals": {},
}
LOCAL_DEFAULTS = {
    "android": {"serials": [], "hours": "0-24", "dnd": True, "max_temp_c": 42, "min_battery": 20},
    "tools": {"ffmpeg": "ffmpeg", "ffprobe": "ffprobe"},
    "video": {"record": True, "record_short_edge": 720, "record_bitrate": 2500000, "clip_max_seconds": 20,
              "clip_max_mb": 8, "clip_long_edge": 720, "clip_fps": 12, "clip_quality": 70},
    "youtube": {"enabled": False, "privacy": "private"},
    "raw": {"keep_originals_days": 3, "keep_shots_days": 14},
}


# --- конфиги и состояние ------------------------------------------------------

def merge(base: dict, over: dict) -> dict:
    out = dict(base)
    for k, v in (over or {}).items():
        out[k] = merge(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else v
    return out


def local_cfg() -> dict:
    p = ROOT / "local.yaml"
    return merge(LOCAL_DEFAULTS, yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else {})


def game_entries() -> list[dict]:
    cfg = yaml.safe_load((ROOT / "games.yaml").read_text(encoding="utf-8")) or {}
    base = merge(GAME_DEFAULTS, cfg.get("defaults") or {})
    return [merge(base, g) for g in cfg.get("games") or []]


def find_game(game: str) -> dict:
    for e in game_entries():
        if e["id"] == game:
            return e
    fail(f"игры {game} нет в games.yaml")


def state_path(game: str) -> Path:
    return ROOT / "memory" / game / "state.json"


def load_state(game: str) -> dict:
    p = state_path(game)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {"onboarded": False, "last": {}}


def save_state(game: str, st: dict) -> None:
    p = state_path(game)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(st, ensure_ascii=False, indent=1), encoding="utf-8")


def load_current() -> dict | None:
    return json.loads(CURRENT.read_text(encoding="utf-8")) if CURRENT.exists() else None


def save_current(cur: dict) -> None:
    CURRENT.write_text(json.dumps(cur, ensure_ascii=False, indent=1), encoding="utf-8")


def need_current() -> dict:
    cur = load_current()
    if not cur:
        fail("нет активной сессии: сначала sw.py start")
    return cur


def log_step(cur: dict, rec: dict) -> None:
    rec = {"t": round(time.time(), 2), "step": cur["step"], **rec}
    with open(Path(cur["dir"]) / "steps.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def out(obj: dict) -> None:
    print(json.dumps(obj, ensure_ascii=False, indent=1))


def fail(msg: str, code: int = 2, **extra) -> None:
    out({"error": msg, **extra})
    sys.exit(code)


def slug(text: str) -> str:
    tr = dict(zip("абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
                  ["a", "b", "v", "g", "d", "e", "e", "zh", "z", "i", "y", "k", "l", "m", "n", "o", "p", "r", "s",
                   "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya"]))
    s = "".join(tr.get(c, c) for c in text.lower())
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:40] or "clip"


# --- телефон --------------------------------------------------------------------

def in_hours(spec: str, hour: int) -> bool:
    a, b = (int(x) for x in str(spec).split("-"))
    return a <= hour < b if a <= b else hour >= a or hour < b


def adb(serial: str, *args: str, timeout: int = 30) -> str:
    return subprocess.run(["adb", "-s", serial, *args], capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=timeout).stdout


def serials(L: dict) -> list[str]:
    try:
        lines = subprocess.run(["adb", "devices"], capture_output=True, text=True, timeout=15).stdout.splitlines()
    except (OSError, subprocess.TimeoutExpired):
        return []
    found = [ln.split("\t")[0] for ln in lines[1:] if ln.endswith("\tdevice")]
    return [s for s in found if not L["android"]["serials"] or s in L["android"]["serials"]]


def installed(serial: str) -> set[str]:
    # --user 0: на Samsung есть второй пользователь (Secure Folder), без флага pm падает
    return {ln.replace("package:", "").strip() for ln in adb(serial, "shell", "pm list packages --user 0").splitlines()}


def focus(serial: str) -> str | None:
    m = re.search(r"mCurrentFocus=Window\{\S+ \S+ ([\w.]+)", adb(serial, "shell", "dumpsys window | grep mCurrentFocus"))
    return m.group(1) if m else None


def locked(serial: str) -> bool:
    return "isKeyguardShowing=true" in adb(serial, "shell", "dumpsys window | grep isKeyguardShowing")


TOUCH_BLOCKED = ("касания блокирует защита Samsung от случайных касаний: закрыт датчик приближения. "
                 "Положите телефон экраном вверх и уберите всё с его верхнего края")


def touch_blocked(serial: str) -> bool:
    """Samsung затемняет экран и глотает касания, когда датчик приближения закрыт
    (телефон экраном вниз, в чехле-книжке, в кармане): окно IgniteTouchProtectionPresenter."""
    visible, cur = False, None
    for line in adb(serial, "shell", "dumpsys window windows").splitlines():
        if "Window #" in line:
            cur = line
        elif "isVisible=true" in line and cur and "TouchProtection" in cur:
            visible = True
    return visible


def phone_status(serial: str, L: dict, games: set[str]) -> tuple[bool, str]:
    """Телефон личный: не занимать его, когда им пользуются, он заблокирован, горячий или садится."""
    a = L["android"]
    if not in_hours(a["hours"], dt.datetime.now().hour):
        return False, f"вне часов {a['hours']}"
    if locked(serial):
        return False, "экран заблокирован: PIN агент не вводит, разблокируйте телефон (на зарядке он не гаснет)"
    bat = adb(serial, "shell", "dumpsys battery")
    temp = int(re.search(r"temperature: (\d+)", bat).group(1)) / 10 if "temperature:" in bat else 0
    level = int(re.search(r"level: (\d+)", bat).group(1)) if "level:" in bat else 100
    powered = re.search(r"(AC|USB) powered: true", bat) is not None
    if touch_blocked(serial):
        return False, TOUCH_BLOCKED
    if temp > a["max_temp_c"]:
        return False, f"телефон нагрет до {temp} °C"
    if level < a["min_battery"] and not powered:
        return False, f"заряд {level}% и нет зарядки"
    awake = "mWakefulness=Awake" in adb(serial, "shell", "dumpsys power | grep mWakefulness")
    app = focus(serial) or ""
    if awake and app and "launcher" not in app and app not in games and app not in SYSTEM_OVERLAYS:
        return False, f"телефоном пользуются: на экране {app}"
    return True, "ok"


class FakeDevice:
    """Проверка без телефона: кадры по кругу из папки с картинками."""

    def __init__(self, folder: str, cur: dict):
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
        return FakeDevice(cur["device"], cur)
    from device import AndroidDevice

    try:
        return AndroidDevice(cur["device"], prepare=prepare)
    except Exception as ex:
        fail(f"телефон {cur['device']} недоступен: {ex}", 3, hint="sw.py end --status blocked --summary ...")


def app_on_screen(cur: dict) -> str | None:
    return cur["game"] if cur["platform"] == "fake" else focus(cur["device"])


def guard(cur: dict) -> None:
    if cur["platform"] == "fake":
        return
    if locked(cur["device"]):
        fail("экран заблокирован: PIN агент не вводит", 3, hint="sw.py end --status blocked --summary ...")
    if touch_blocked(cur["device"]):
        fail(TOUCH_BLOCKED, 3, hint="sw.py end --status blocked --summary ...")


# --- кадры ----------------------------------------------------------------------

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
    cur.update(last_hash=h, scale=scale, last_shot=k, last_app=app)
    elapsed = (time.time() - cur["t0"]) / 60
    info = {"shot": str(small_path), "shot_n": k, "size": [small.width, small.height], "app": app,
            "same_as_prev": same, "same_streak": cur["same_streak"], "elapsed_min": round(elapsed, 1),
            "budget_min": cur["budget_min"], "steps": cur["step"], "max_steps": cur["max_steps"]}
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
        warn.append("бюджет исчерпан: обнови memory/<game>/progress.md и заверши сессию (end)")
    if warn:
        info["warnings"] = warn
    return info


def action(args, name: str, fn, rec: dict) -> None:
    cur = need_current()
    guard(cur)
    dev = open_device(cur)
    fn(dev, cur["scale"])
    cur["step"] += 1
    cur["last_action"] = time.time()
    time.sleep(args.settle)
    info = take_shot(cur, dev)
    log_step(cur, {"type": name, **rec, "why": args.why, "shot": info["shot_n"], "same": info["same_as_prev"],
                   "app": info["app"], "hash": cur["last_hash"]})
    save_current(cur)
    out(info)


# --- запись экрана и клипы -------------------------------------------------------

def start_recording(cur: dict, L: dict) -> None:
    if not L["video"]["record"]:
        return
    d, v = Path(cur["dir"]), L["video"]
    if cur["platform"] == "fake":
        spec = {"kind": "ffmpeg", "cmd": [L["tools"]["ffmpeg"], "-y", "-loglevel", "error", "-re", "-f", "lavfi", "-i",
                                          "testsrc=size=360x780:rate=15", "-c:v", "libx264", "-preset", "ultrafast",
                                          "-pix_fmt", "yuv420p", str(d / "original.mkv")]}
    else:
        # На полном разрешении screenrecord этого телефона не стартует (Encoder failed), поэтому
        # короткая сторона 720: 1080x2340 -> 720x1560.
        w, h = (int(x) for x in re.search(r"(\d+)x(\d+)", adb(cur["device"], "shell", "wm size")).groups())
        k = v["record_short_edge"] / min(w, h)
        spec = {"kind": "screenrecord", "serial": cur["device"], "size": f"{int(w * k) // 2 * 2}x{int(h * k) // 2 * 2}",
                "bitrate": str(v["record_bitrate"])}
    spec["ffmpeg"] = L["tools"]["ffmpeg"]
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
            remote, t = f"/sdcard/sw_rec_{i:03d}.mp4", time.time()
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
                with open(d / "segments.jsonl", "a", encoding="utf-8") as f:
                    f.write(json.dumps({"file": local.name, "t": t, "t_end": t_end}) + "\n")
            i += 1
        segs = read_segments(d)
        if segs:
            (d / "segments.txt").write_text("".join(f"file '{s['file']}'\n" for s in segs), encoding="utf-8")
            subprocess.run([spec["ffmpeg"], "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                            "-i", str(d / "segments.txt"), "-map", "0:v", "-c", "copy", str(d / "original.mkv")])
    (d / "rec.done").write_text("1")


def read_segments(d: Path) -> list[dict]:
    p = d / "segments.jsonl"
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines()] if p.exists() else []


def probe(L: dict, path: Path, what: str) -> str:
    return subprocess.run([L["tools"]["ffprobe"], "-v", "error", "-show_entries", what, "-of", "csv=p=0", str(path)],
                          capture_output=True, text=True).stdout.strip()


def timeline(cur: dict, L: dict) -> list[tuple[float, float, float]]:
    """(начало по часам, позиция в original.mkv, длительность) для каждого сегмента записи.
    Длительность — по ffprobe, а если в файле её нет (так пишет этот телефон) — по часам."""
    segs = read_segments(Path(cur["dir"]))
    if not segs:
        return [(cur["rec"]["t0"], 0.0, float("inf"))]
    pos, tl = 0.0, []
    for s in segs:
        raw = probe(L, Path(cur["dir"]) / s["file"], "format=duration")
        dur = float(raw) if re.fullmatch(r"[\d.]+", raw or "") else s["t_end"] - s["t"]
        tl.append((s["t"], pos, dur))
        pos += dur
    return tl


def to_pos(tl, t: float) -> float | None:
    for t0, pos, dur in reversed(tl):
        if t >= t0:
            return pos + min(t - t0, dur)
    return tl[0][1] if tl else None


def encode_clip(L: dict, src: Path, start: float, dur: float, dest: Path) -> None:
    """Клип — анимированный WebP: GitHub не показывает <video> из репозитория, а WebP
    проигрывается прямо в статье. Не влез в лимит — меньше качество, кадров и размер."""
    v = L["video"]
    w, h = (int(x) for x in probe(L, src, "stream=width,height").splitlines()[0].split(","))
    for quality, fps, edge in ((v["clip_quality"], v["clip_fps"], v["clip_long_edge"]),
                               (v["clip_quality"] - 15, max(6, v["clip_fps"] - 4), v["clip_long_edge"] * 3 // 4),
                               (40, 6, v["clip_long_edge"] // 2)):
        k = min(1.0, edge / max(w, h))
        subprocess.run([L["tools"]["ffmpeg"], "-y", "-loglevel", "error", "-ss", f"{start:.2f}", "-i", str(src),
                        "-t", f"{dur:.2f}", "-vf", f"fps={fps},scale={int(w * k)}:{int(h * k)}:flags=lanczos",
                        "-c:v", "libwebp_anim", "-lossless", "0", "-quality", str(quality), "-compression_level", "4",
                        "-loop", "0", "-an", str(dest)], check=True)
        if dest.stat().st_size <= v["clip_max_mb"] * 1024 * 1024:
            return


def cut_clips(cur: dict, L: dict) -> list[dict]:
    d = Path(cur["dir"])
    src = d / "original.mkv"
    if not cur["clips"] or not src.exists():
        return []
    tl, max_s, res = timeline(cur, L), L["video"]["clip_max_seconds"], []
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
            encode_clip(L, src, s + j * step, step, dest)
            res.append({"file": dest.relative_to(ROOT).as_posix(),
                        "title": c["title"] + (f" ({j + 1}/{parts})" if parts > 1 else ""), "desc": c.get("desc", ""),
                        "original_start_s": round(s + j * step, 1), "seconds": round(step, 1),
                        "mb": round(dest.stat().st_size / 1048576, 2)})
    (d / "clips.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return res


# --- команды --------------------------------------------------------------------

def due_kind(e: dict, st: dict, version: str | None, now: float) -> str | None:
    last = st.get("last", {})
    if version and st.get("installed_version") and version != st["installed_version"]:
        return "update_diff"  # телефон обновил игру — задокументировать изменения
    if not st.get("onboarded"):
        return "onboard"
    if now - last.get("event_scan", 0) > e["event_scan_hours"] * 3600:
        return "event_scan"
    if now - last.get("deep_revisit", 0) > e["revisit_hours"] * 3600:
        return "deep_revisit"
    return None


def app_version(serial: str, package: str) -> str | None:
    m = re.search(r"versionName=(\S+)", adb(serial, "shell", f"dumpsys package {package}"))
    return m.group(1) if m else None


def cmd_next(args) -> None:
    cur = load_current()
    if cur and time.time() - cur["last_action"] < STALE_HOURS * 3600:
        return out({"action": "wait", "reason": f"идёт сессия {cur['id']}"})
    if cur:
        finish(cur, "abandoned", "сессия брошена: рутина не завершила её", False)
    L = local_cfg()
    phones = serials(L)
    if not phones:
        return out({"action": "idle", "reason": "телефон не подключён (adb devices пуст)"})
    serial, entries = phones[0], [e for e in game_entries() if e["enabled"]]
    ok, reason = phone_status(serial, L, {e["id"] for e in entries})
    if not ok:
        return out({"action": "idle", "reason": reason})
    have, now, cands, missing = installed(serial), time.time(), [], []
    for i, e in enumerate(entries):
        if e["id"] not in have:
            missing.append(e["id"])
            continue
        kind = due_kind(e, load_state(e["id"]), app_version(serial, e["id"]), now)
        if kind:
            cands.append((KIND_RANK[kind], e.get("priority", 100 + i), i, e, kind))
    if not cands:
        return out({"action": "idle", "reason": "нечего играть сейчас", "not_installed": missing})
    _, _, _, e, kind = min(cands, key=lambda c: c[:3])
    budget = e["budget_min"][kind]
    goals = list(e["kind_goals"].get(kind, [])) + (list(e["goals"]) if kind in ("onboard", "deep_revisit") else [])
    context = [p for p in ("wiki/_common/agent-lessons.md", f"wiki/{e['id']}/agent/lessons.md",
                           f"wiki/{e['id']}/open-questions.md", f"memory/{e['id']}/progress.md") if (ROOT / p).exists()]
    out({"action": "play", "game": e["id"], "title": e.get("title", e["id"]), "device": serial, "kind": kind,
         "budget_min": budget, "max_steps": budget * e["steps_per_min"], "goals": goals, "read_first": context,
         "not_installed": missing})


def cmd_start(args) -> None:
    cur = load_current()
    if cur:
        fail(f"уже идёт сессия {cur['id']}", hint="sw.py end ...")
    e, L = find_game(args.game), local_cfg()
    platform = "fake" if args.fake else "android"
    device = args.fake or args.device or (serials(L)[:1] or [None])[0]
    if not device:
        fail("телефон не подключён (adb devices пуст)")
    budget = args.budget or e["budget_min"][args.kind]
    sid = f"{dt.datetime.now():%Y%m%d-%H%M%S}-{args.kind}"
    d = RAW / args.game / sid
    (d / "shots").mkdir(parents=True)
    cur = {"id": sid, "game": args.game, "title": e.get("title", args.game), "kind": args.kind, "platform": platform,
           "device": device, "dir": str(d), "t0": time.time(), "last_action": time.time(), "step": 0, "shots": 0,
           "scale": 1.0, "same_streak": 0, "budget_min": budget, "max_steps": budget * e["steps_per_min"],
           "clips": [], "clip_open": None}
    if platform == "android":
        if locked(device):
            shutil.rmtree(d)
            fail("экран заблокирован: PIN агент не вводит")
        if L["android"]["dnd"]:
            # «Не беспокоить: только будильники» на время сессии, чтобы уведомления
            # мессенджеров не всплывали поверх игры и не попадали в кадры
            cur["zen_prev"] = adb(device, "shell", "settings get global zen_mode").strip()
            adb(device, "shell", "cmd notification set_dnd alarms")
    dev = open_device(cur, prepare=True)
    dev.launch(args.game)
    time.sleep(8)
    cur["version"] = dev.app_version(args.game)
    start_recording(cur, L)
    log_step(cur, {"type": "start", "kind": args.kind, "platform": platform, "version": cur["version"]})
    info = take_shot(cur, dev)
    save_current(cur)
    out({"session": sid, "version": cur["version"], **info})


def cmd_shot(args) -> None:
    cur = need_current()
    info = take_shot(cur, open_device(cur))
    log_step(cur, {"type": "shot", "shot": info["shot_n"], "app": info["app"], "hash": cur["last_hash"]})
    save_current(cur)
    out(info)


def cmd_wait(args) -> None:
    cur = need_current()
    time.sleep(min(args.seconds, 60))
    info = take_shot(cur, open_device(cur))
    log_step(cur, {"type": "wait", "seconds": args.seconds, "shot": info["shot_n"], "same": info["same_as_prev"]})
    save_current(cur)
    out(info)


def cmd_launch(args) -> None:
    cur = need_current()
    guard(cur)
    dev = open_device(cur)
    dev.launch(cur["game"])
    cur["step"] += 1
    cur["last_action"] = time.time()
    time.sleep(4)
    info = take_shot(cur, dev)
    log_step(cur, {"type": "launch", "shot": info["shot_n"], "app": info["app"]})
    save_current(cur)
    out(info)


def cmd_note(args) -> None:
    cur = need_current()
    log_step(cur, {"type": "note", "kind": args.kind, "text": args.text, "shot": cur["last_shot"]})
    out({"ok": True})


def cmd_mark(args) -> None:
    cur = need_current()
    if cur.get("last_app") not in (cur["game"], None):
        fail(f"последний кадр не из игры ({cur['last_app']}): в вики он не пойдёт")
    shot = Path(cur["dir"]) / "shots" / f"{cur['last_shot']:05d}.jpg"
    log_step(cur, {"type": "mark", "title": args.title, "desc": args.desc, "shot": cur["last_shot"],
                   "file": shot.relative_to(ROOT).as_posix()})
    out({"ok": True, "marked": str(shot)})


def cmd_clip(args) -> None:
    cur = need_current()
    if args.edge == "begin":
        cur["clip_open"] = {"title": args.text, "t0": time.time() - 2}
    else:
        if not cur["clip_open"]:
            fail("клип не начат: sw.py clip begin \"заголовок\"")
        cur["clips"].append({**cur["clip_open"], "desc": args.text, "t1": time.time() + 1})
        cur["clip_open"] = None
    log_step(cur, {"type": f"clip_{args.edge}", "text": args.text})
    save_current(cur)
    out({"ok": True, "clips": len(cur["clips"])})


def finish(cur: dict, status: str, summary: str, onboarded: bool) -> dict:
    L, d = local_cfg(), Path(cur["dir"])
    if cur.get("clip_open"):
        cur["clips"].append({**cur["clip_open"], "desc": "", "t1": cur["last_action"] + 2})
    if cur.get("rec"):
        (d / "rec.stop").write_text("1")
        for _ in range(600):
            if (d / "rec.done").exists():
                break
            time.sleep(0.5)
    clips = cut_clips(cur, L)
    if cur["platform"] == "android":
        try:
            cur["version"] = app_version(cur["device"], cur["game"]) or cur.get("version")
            adb(cur["device"], "shell", f"am force-stop {cur['game']}")
            if cur.get("zen_prev") is not None:
                adb(cur["device"], "shell", f"cmd notification set_dnd {ZEN.get(cur['zen_prev'], 'off')}")
        except Exception as ex:
            log_step(cur, {"type": "warn", "text": f"stop: {ex}"})
    youtube = None
    if L["youtube"]["enabled"] and (d / "original.mkv").exists():
        try:
            import youtube as yt

            youtube = yt.upload(d / "original.mkv", f"{cur['title']} · {cur['kind']} · {cur['id'][:8]}",
                                f"sleepwalker session {cur['id']}\n{summary}", L["youtube"])
            (d / "original.mkv").unlink()
            for seg in d.glob("seg_*.mp4"):
                seg.unlink()
        except Exception as ex:
            log_step(cur, {"type": "warn", "text": f"youtube: {ex}"})
    marks = [json.loads(x) for x in (d / "steps.jsonl").read_text(encoding="utf-8").splitlines()
             if '"type": "mark"' in x]
    meta = {"id": cur["id"], "game": cur["game"], "kind": cur["kind"], "version": cur.get("version"),
            "started": dt.datetime.fromtimestamp(cur["t0"]).isoformat(timespec="seconds"),
            "minutes": round((time.time() - cur["t0"]) / 60, 1), "steps": cur["step"], "status": status,
            "summary": summary, "marks": len(marks), "clips": clips, "youtube": youtube}
    (d / "session.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    if cur["platform"] != "fake":
        mem = ROOT / "memory" / cur["game"]
        mem.mkdir(parents=True, exist_ok=True)
        with open(mem / "sessions.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps({k: v for k, v in meta.items() if k != "clips"} | {"clips": len(clips)},
                               ensure_ascii=False) + "\n")
        st = load_state(cur["game"])
        if status in ("ok", "stuck", "interrupted"):
            extra = {"onboard": ["event_scan", "deep_revisit"], "update_diff": ["event_scan"]}.get(cur["kind"], [])
            for k in [cur["kind"], *extra]:
                st.setdefault("last", {})[k] = cur["t0"]
            if cur["kind"] == "onboard" and onboarded:
                st["onboarded"] = True
        st["installed_version"] = cur.get("version")
        save_state(cur["game"], st)
    log_step(cur, {"type": "end", "status": status, "summary": summary})
    CURRENT.unlink(missing_ok=True)
    return {"ended": cur["id"], "status": status, "dir": str(d), "steps_log": str(d / "steps.jsonl"),
            "marks": [m["file"] for m in marks], "clips": [c["file"] for c in clips], "youtube": youtube}


def cmd_end(args) -> None:
    out(finish(need_current(), args.status, args.summary, args.onboarded))


def dreamed_ids() -> set[str]:
    ids: set[str] = set()
    for p in (ROOT / "dreams").glob("*.md"):
        ids |= set(re.findall(r"\d{8}-\d{6}-[a-z_]+", p.read_text(encoding="utf-8")))
    return ids


def cmd_pending(args) -> None:
    done, res = dreamed_ids(), []
    for f in sorted((ROOT / "memory").glob("*/sessions.jsonl")):
        for line in f.read_text(encoding="utf-8").splitlines():
            s = json.loads(line)
            if s["id"] not in done:
                d = RAW / s["game"] / s["id"]
                res.append({**s, "raw": str(d) if d.exists() else None})
    out({"pending": res, "count": len(res)})


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
    L, now, freed = local_cfg(), time.time(), 0
    done = dreamed_ids()
    for d in RAW.glob("*/*/"):
        meta = d / "session.json"
        if not meta.exists():
            continue
        age_days = (now - meta.stat().st_mtime) / 86400
        m = json.loads(meta.read_text(encoding="utf-8"))
        victims = []
        if m.get("youtube") or age_days > L["raw"]["keep_originals_days"]:
            victims += [d / "original.mkv", *d.glob("seg_*.mp4")]
        if m["id"] in done and age_days > L["raw"]["keep_shots_days"]:
            victims += [d / "shots", d / "clips"]
        for v in victims:
            if v.exists():
                freed += sum(f.stat().st_size for f in v.rglob("*")) if v.is_dir() else v.stat().st_size
                shutil.rmtree(v) if v.is_dir() else v.unlink()
    out({"freed_mb": round(freed / 1048576, 1)})


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(prog="sw")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("next")
    p = sub.add_parser("start")
    p.add_argument("game")
    p.add_argument("kind", choices=list(KIND_RANK))
    p.add_argument("--device", help="серийный номер телефона, если их несколько")
    p.add_argument("--budget", type=int, help="минуты вместо значения из games.yaml")
    p.add_argument("--fake", metavar="DIR", help="проверка без телефона: папка с картинками-кадрами")
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
    p = sub.add_parser("end")
    p.add_argument("--status", required=True, choices=["ok", "stuck", "interrupted", "crashed", "blocked"])
    p.add_argument("--summary", required=True)
    p.add_argument("--onboarded", action="store_true", help="обучение пройдено, игра изучена в первом приближении")
    sub.add_parser("pending")
    for name in ("wiki-img", "wiki-clip"):
        p = sub.add_parser(name)
        p.add_argument("src")
        p.add_argument("game_dir")
        p.add_argument("slug")
    sub.add_parser("gc")
    p = sub.add_parser("_rec")
    p.add_argument("dir")
    args = ap.parse_args()

    s = lambda v, k: int(round(v * k))  # noqa: E731
    handlers = {
        "next": cmd_next, "start": cmd_start, "shot": cmd_shot, "wait": cmd_wait, "launch": cmd_launch,
        "note": cmd_note, "mark": cmd_mark, "clip": cmd_clip, "end": cmd_end, "pending": cmd_pending,
        "wiki-img": cmd_wiki_img, "wiki-clip": cmd_wiki_clip, "gc": cmd_gc, "_rec": cmd_rec,
        "tap": lambda a: action(a, "tap", lambda d, k: d.tap(s(a.x, k), s(a.y, k)), {"x": a.x, "y": a.y}),
        "swipe": lambda a: action(a, "swipe", lambda d, k: d.swipe(s(a.x1, k), s(a.y1, k), s(a.x2, k), s(a.y2, k)),
                                  {"from": [a.x1, a.y1], "to": [a.x2, a.y2]}),
        "key": lambda a: action(a, "key", lambda d, k: d.key(a.name), {"key": a.name}),
        "text": lambda a: action(a, "text", lambda d, k: d.type_text(a.value), {"text": a.value}),
    }
    handlers[args.cmd](args)


if __name__ == "__main__":
    main()
