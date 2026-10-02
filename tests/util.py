"""Shared test helpers: the repository root, a scratch folder, synthetic phone frames."""
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TMP = Path(tempfile.gettempdir()) / "sleepwalker-tests"
TMP.mkdir(exist_ok=True)


def frames_dir() -> Path:
    """17 synthetic 1080x2340 frames for the fake phone: different from each other, no real game content."""
    from PIL import Image, ImageDraw

    d = TMP / "frames"
    if len(list(d.glob("*.png"))) == 17:
        return d
    d.mkdir(exist_ok=True)
    for i in range(17):
        img = Image.new("RGB", (1080, 2340), ((i * 37) % 200 + 30, (i * 71) % 200 + 30, (i * 113) % 200 + 30))
        dr = ImageDraw.Draw(img)
        for k in range(6):  # blocks in different places, so frames differ in hash and in pixels
            x, y = (i * 97 + k * 151) % 900, (i * 211 + k * 307) % 2100
            dr.rectangle((x, y, x + 160, y + 220), fill=((k * 50 + i * 13) % 255, (k * 90) % 255, (i * 29) % 255))
        img.save(d / f"frame_{i:02d}.png")
    return d
