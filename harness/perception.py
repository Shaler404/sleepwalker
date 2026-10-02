"""Perception: preparing frames for the model, screen signatures, OCR, annotations.

Key facts (Claude docs, Vision / Coordinates section):
- an image costs ceil(w/28) * ceil(h/28) visual tokens;
- Claude 4.7+ models (Opus/Sonnet 5.x) keep frames up to 2576 px on the long edge and 4784 tokens
  without downscaling; Haiku 4.5 and older, up to 1568 px / 1568 tokens;
- the model returns coordinates in pixels of the image it sees,
  so downscale the frame yourself and keep the scale.
"""
from __future__ import annotations

import math
from typing import Iterable

from PIL import Image, ImageDraw

HIGH_RES = {"max_edge": 2576, "max_tokens": 4784}  # Opus 5.5 / Sonnet 5.5 / Opus 4.7+
STANDARD = {"max_edge": 1568, "max_tokens": 1568}  # Haiku 4.5 and older


def image_tokens(width: int, height: int) -> int:
    return math.ceil(width / 28) * math.ceil(height / 28)


def resized_size(width: int, height: int, max_edge: int = 2576, max_tokens: int = 4784) -> tuple[int, int]:
    """The size the API itself will downscale the frame to (reference code from the docs)."""

    def fits(w: int, h: int) -> bool:
        return (
            math.ceil(w / 28) * 28 <= max_edge
            and math.ceil(h / 28) * 28 <= max_edge
            and image_tokens(w, h) <= max_tokens
        )

    if fits(width, height):
        return width, height
    if height > width:
        rh, rw = resized_size(height, width, max_edge, max_tokens)
        return rw, rh
    aspect = width / height
    lo, hi = 1, width
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if fits(mid, max(round(mid / aspect), 1)):
            lo = mid
        else:
            hi = mid
    return lo, max(round(lo / aspect), 1)


def prepare_for_model(img: Image.Image, budget_tokens: int = 1500, tier: dict = HIGH_RES) -> tuple[Image.Image, float]:
    """Downscale the frame so that (a) the API does not resize it (coordinates 1:1) and
    (b) it costs no more than budget_tokens. Returns (frame, scale):
    physical_coordinate = model_coordinate * scale.

    A 1080x2400 phone: 3354 tokens without downscaling; budget 1500 -> ~720x1600 (1508);
    budget 900 -> ~540x1200 (860). For small text use zoom_crop().
    """
    w, h = resized_size(img.width, img.height, **tier)
    if image_tokens(w, h) > budget_tokens:
        k = math.sqrt(budget_tokens / image_tokens(w, h))
        w, h = max(1, int(w * k)), max(1, int(h * k))
    small = img.resize((w, h), Image.LANCZOS)
    return small, img.width / w


def zoom_crop(img: Image.Image, x: int, y: int, size: int = 400) -> tuple[Image.Image, tuple[int, int]]:
    """Cut a square around a point at full resolution (for small text).
    Returns (crop, offset); coordinate on the crop + offset = physical coordinate."""
    left = max(0, min(img.width - size, x - size // 2))
    top = max(0, min(img.height - size, y - size // 2))
    return img.crop((left, top, left + size, top + size)), (left, top)


# --- screen signatures ----------------------------------------------------

def screen_hash(img: Image.Image) -> str:
    """Perceptual hash (64 bits): the same screen gives close hashes even when
    timers and numbers change. pip install imagehash"""
    import imagehash

    return str(imagehash.phash(img, hash_size=8))


def hash_distance(a: str, b: str) -> int:
    import imagehash

    return int(imagehash.hex_to_hash(a) - imagehash.hex_to_hash(b))


def is_same_screen(a: str | None, b: str | None, threshold: int = 10) -> bool:
    # int()/bool() matter: imagehash returns numpy types that json cannot serialize.
    return bool(a is not None and b is not None and hash_distance(a, b) <= threshold)


STATUS_BAR = 0.04  # the top of the frame: the clock and notification icons change there, not the game


def small_gray(img: Image.Image, top: float = STATUS_BAR) -> Image.Image:
    """A small grayscale copy of the game area (90 px on the short edge, without the status bar)."""
    g = img.convert("L")
    g = g.crop((0, round(g.height * top), g.width, g.height))
    k = 90 / min(g.size)
    return g.resize((max(1, round(g.width * k)), max(1, round(g.height * k))))


def changed_share(a: Image.Image, b: Image.Image) -> float:
    """The share of the game area (0..1) whose pixels changed noticeably between two frames. pHash moves by
    2–10 bits when a batch removes a few mahjong tiles, so the hash alone called a board that was being won
    "unchanged" for 25 steps (Vita Mahjong 20261001-110957, 2026-10-01); this sees a single tile go."""
    from PIL import ImageChops

    ta, tb = small_gray(a), small_gray(b.resize(a.size) if b.size != a.size else b)
    changed = ImageChops.difference(ta, tb).point(lambda v: 255 if v > 25 else 0).histogram()[255]
    return round(changed / (ta.width * ta.height), 4)


# --- OCR ------------------------------------------------------------------

def ocr(img: Image.Image) -> list[dict]:
    """Lightweight OCR without a GPU: pip install rapidocr-onnxruntime numpy.
    Returns [{"text", "box": [[x,y]x4], "score"}] in physical frame coordinates."""
    import numpy as np
    from rapidocr_onnxruntime import RapidOCR

    engine = _ocr_engine()
    result, _ = engine(np.array(img))
    return [{"text": t, "box": box, "score": float(s)} for box, t, s in (result or [])]


_ENGINE = None


def _ocr_engine():
    global _ENGINE
    if _ENGINE is None:
        from rapidocr_onnxruntime import RapidOCR

        _ENGINE = RapidOCR()
    return _ENGINE


# --- annotations for the wiki and Set-of-Mark -------------------------------

def annotate(img: Image.Image, marks: Iterable[tuple[int, int, str]]) -> Image.Image:
    """Draw numbered marks: [(x, y, 'label'), ...] in physical coordinates."""
    out = img.copy()
    draw = ImageDraw.Draw(out)
    r = max(12, img.width // 60)
    for x, y, label in marks:
        draw.ellipse((x - r, y - r, x + r, y + r), outline=(255, 40, 40), width=4)
        draw.text((x + r + 4, y - r), label, fill=(255, 40, 40))
    return out


def save_for_wiki(img: Image.Image, path: str, long_edge: int = 1080, quality: int = 85) -> None:
    """A frame for the wiki: WebP, long edge <= long_edge."""
    k = min(1.0, long_edge / max(img.size))
    if k < 1.0:
        img = img.resize((int(img.width * k), int(img.height * k)), Image.LANCZOS)
    img.save(path, format="WEBP", quality=quality)
