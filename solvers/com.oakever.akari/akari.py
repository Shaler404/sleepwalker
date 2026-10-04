"""Akari (Light Up) solver for MeowTrail: reads the board from the frame and double-taps every missing cat.

Reading (full-resolution frame, any size; tuned on 1080x2340):
- the board sits on the page background (247,242,238) between the cat counter and the boosters; the
  column gaps give the cell pitch, the gap phases give the lattice (rows and columns, 3..12 each);
- each cell is classed by the share of its upper half that is: white (a numbered wall), unlit floor
  (232,224,213), cardboard (a box: tan top or yellow tape), page background (outside the board: a wall),
  or saturated colour (floor lit by a cat, or the cat itself). The upper half is used because a cat
  overlaps the lower part of the cell above it and walls are drawn raised;
- the number on a white wall is read by the hue of its digit: 0 green, 1 blue, 2 pink, 3 orange, 4 purple;
- the cat counter "k/N" above the board is read with 10x14 glyph templates (k dark, "/N" grey).

Checks before any move (otherwise no moves and a note): the page background is the game's, every cell is
one of the classes (no faded or half-drawn cells: the board-appear animation), every white wall has a
digit, the grid is 3..12 a side, outside cells are clean background and confirmed by the counter, the
puzzle has exactly one solution, the lit cells are exactly the
cells seen by the solution cats already on the board (any cat on the board is right: the game rejects a
wrong cat with a red X), and, when the counter is readable, N is the number of cats in the solution and
k the number already placed. The moves are the solution cells that are still unlit, as double taps.
The next round reads the board again: no unlit solution cell left means the level is done.

Screens that are not a level board (2026-10-03):
- the win screen (the page under a dark veil): the counter is read with the veil taken off; N/N -> done
  (no moves), so `solve --run` ends as "solved"; any other dimmed screen is refused with its counter;
- the tutorial (page veiled to (150,149,147), the cell(s) to tap left bright): double taps on exactly the
  bright floor cells (at most 4, never two that see each other); the finished tutorial board on the light
  page (250,249,245) with every cell lit and the orange "Got it!" button -> done.

Fallback: --board FILE with {"rows": ["..3..", ...], "x": [col centres], "y": [row centres], "count": N,
"frame_scale": k} in frame pixels ('.' empty, '#' wall or outside cell, '0'-'4' numbered wall, 'C' cat).
"""
import colorsys

import numpy as np

BG = np.array([247, 242, 238])
UNLIT = np.array([232, 224, 213])
TUT_BG = np.array([150, 149, 147])  # the tutorial's veil over the page; the cells to tap stay bright
TUT_DONE_BG = np.array([250, 249, 245])  # a finished tutorial board with "Got it!" (also the home screen)
BOX_TOP = np.array([229, 193, 140])
BOX_TAPE = np.array([234, 210, 114])
# digit -> hue window (degrees) of the digit's colour
DIGIT_HUES = {"0": (55, 100), "1": (185, 230), "2": (285, 330), "3": (5, 45), "4": (235, 275)}
MIN_SIDE, MAX_SIDE = 3, 12
GAP = 8  # px between cells at 1080 px width; scaled by the frame width
# counter glyphs, 10 wide x 14 high, row by row ('#' ink); learned from 265 counters of levels 1-83
GLYPHS = {
    "/": ".....####......#####....######....#####....######....#####.....#####....######....#####....######....#####.....#####....#####......####.....",
    "0": "...####.....######...########..###..###.####..#######....######....######....######....#######..####.###..###..########...######.....####...",
    "1": "....#####..#############################.....#####.....#####.....#####.....#####.....#####.....#####.....#####.....#####.....#####.....#####",
    "2": "..#####....########.#########..#....####......####......####.....####.....####....#####....#####....#####.....##############################",
    "3": "..#####...#########.#########..#...#####......###......####...######....#######.......####......######....#######################...#####...",
    "4": ".....###......#####.....#####....######...#######...###.###..###..###..###..###.##############################......###.......###.......###.",
    "5": ".########..########..########.####......####......########..#########..#########......####......######....#############.#########...#####...",
    "6": "...#####....#######..########..###......####......###.####..#########.#############...#######...########..####.########...#######....####...",
    "7": "##############################......####.....####......####.....####......####......###......####......####.....####......####......###.....",
    "8": "..#####....#######...########.####..###.####..###.####.####..#######...########.####..#######...########..##############.########...#####...",
    "9": "...####....#######...########.####..###.####..########..##############.#########..########......###......####..########..#######....####....",
}
_GLYPH_BITS = {k: np.array([ch == "#" for ch in v]) for k, v in GLYPHS.items()}


def _no(note, **extra):
    return {"moves": [], "note": note, "rescan": False, "done": False, **extra}


def _runs(mask):
    out, start = [], None
    for i, v in enumerate(mask):
        if v and start is None:
            start = i
        elif not v and start is not None:
            out.append((start, i - 1))
            start = None
    if start is not None:
        out.append((start, len(mask) - 1))
    return out


def _phase(profile, p, lo, hi):
    """Offset of the gap lines (period p) in [lo, hi]: the profile is low on the lines and high halfway."""
    best, n = None, len(profile)
    for phi in np.arange(0, p, 0.5):
        s, cnt = 0.0, 0
        k0 = int(np.floor((lo - phi) / p)) - 1
        for k in range(k0, k0 + int((hi - lo) / p) + 4):
            line = phi + k * p
            mid = line + p / 2
            if mid < lo or mid > hi:
                continue
            i, j = int(round(line)), int(round(mid))
            if 2 <= i < n - 2 and 0 <= j < n:
                s += profile[j] - profile[i - 2:i + 3].min()
                cnt += 1
        if cnt and (best is None or s / cnt > best[0]):
            best = (s / cnt, phi)
    return best


def _classify(cell, bg):
    """One cell (upper half, raised walls included) -> class letter and the fractions."""
    h, w, _ = cell.shape
    reg = cell[int(0.05 * h):int(0.55 * h), int(0.1 * w):int(0.9 * w)].reshape(-1, 3)
    white = (reg.min(axis=1) >= 245).mean()
    unlit = (np.abs(reg - UNLIT).sum(axis=1) <= 15).mean()
    box = ((np.abs(reg - BOX_TOP).sum(axis=1) <= 24) | (np.abs(reg - BOX_TAPE).sum(axis=1) <= 20)).mean()
    back = (np.abs(reg - bg).sum(axis=1) <= 8).mean()
    sat = ((reg.max(axis=1) - reg.min(axis=1)) > 40).mean()
    if white >= 0.6:
        return "N"
    if unlit >= 0.75:
        return "."
    if box >= 0.5:
        return "#"
    if back >= 0.9:
        return " "
    if sat >= 0.6:
        return "L"
    return "?"


def _classify_tutorial(cell, bg):
    """A cell under the tutorial's veil: 'H' the cell the game points at (left bright: unlit floor colour),
    '.' veiled floor, 'n' veiled number, 'N' bright number, 'L' lit floor or a cat, '?' else (the hand)."""
    h, w, _ = cell.shape
    reg = cell[int(0.05 * h):int(0.55 * h), int(0.1 * w):int(0.9 * w)].reshape(-1, 3)
    full = cell[int(0.1 * h):int(0.9 * h), int(0.1 * w):int(0.9 * w)].reshape(-1, 3)
    k = bg / BG
    bright_floor = (np.abs(full - UNLIT).sum(axis=1) <= 30).mean()
    bright = (full.min(axis=1) >= 200).mean()
    veiled = (np.abs(reg - UNLIT * k).sum(axis=1) <= 20).mean()
    white = (reg.min(axis=1) >= 245).mean()
    vwhite = (np.abs(reg - 255 * k).sum(axis=1) <= 20).mean()
    sat = ((reg.max(axis=1) - reg.min(axis=1)) > 25).mean()
    if bright_floor >= 0.4 and bright >= 0.8:
        return "H"
    if white >= 0.6:
        return "N"
    if vwhite >= 0.6:
        return "n"
    if veiled >= 0.75:
        return "."
    if sat >= 0.6:
        return "L"
    return "?"


def _digit(cell):
    h, w, _ = cell.shape
    reg = cell[int(0.08 * h):int(0.62 * h), int(0.2 * w):int(0.8 * w)].reshape(-1, 3)
    sat = reg.max(axis=1) - reg.min(axis=1)
    px = reg[sat > 50]
    if len(px) < 0.01 * len(reg):
        return None
    px = px[::max(1, len(px) // 300)]
    hues = np.array([colorsys.rgb_to_hsv(*(q / 255.0))[0] * 360 for q in px])
    votes = {d: int(((hues >= lo) & (hues < hi)).sum()) for d, (lo, hi) in DIGIT_HUES.items()}
    d = max(votes, key=votes.get)
    return d if votes[d] >= 0.7 * len(hues) else None


def _marks(cell):
    """Marks on an unlit cell: 'r' red X (a rejected cat), 'x' grey X (a single tap or a hint), '' none."""
    h, w, _ = cell.shape
    reg = cell[int(0.25 * h):int(0.75 * h), int(0.25 * w):int(0.75 * w)].reshape(-1, 3)
    red = ((reg[:, 0] > 190) & (reg[:, 1] < 160) & (reg[:, 2] < 160)).mean()
    grey = ((np.abs(reg - UNLIT).sum(axis=1) > 60) & ((reg.max(axis=1) - reg.min(axis=1)) < 45)).mean()
    return "r" if red > 0.02 else "x" if grey > 0.03 else ""


def _counter(a, dimmed=False):
    """The cat counter "k/N" in the white bar above the board -> (k, N), or None when it does not read.
    dimmed: the win screen's dark veil (the bar's white at ~51): the colours are scaled back first and
    the cat icon is the first wide run of saturated columns (confetti flies over the bar)."""
    H, W, _ = a.shape
    reg = a[int(H * 0.235):int(H * 0.275), int(W * 0.38):int(W * 0.95)]
    if dimmed:
        white = float(np.median(reg.max(axis=2)))
        if not 30 <= white <= 200:
            return None
        reg = np.clip(reg.astype(np.float32) * (255.0 / white), 0, 255).astype(np.int16)
    mx = reg.max(axis=2)
    sat = mx - reg.min(axis=2)
    satcol = (sat > 60).sum(axis=0) > 3
    if dimmed:
        runs = []
        for s, e in _runs(satcol):
            if runs and s - runs[-1][1] <= 0.01 * W:
                runs[-1] = (runs[-1][0], e)
            else:
                runs.append((s, e))
        wide = [r for r in runs if r[1] - r[0] >= 0.03 * W]
        icon = np.array([wide[0][1]]) if wide else np.array([], dtype=int)
    else:
        icon = np.where(satcol)[0]  # the cat icon left of the text
    dark = (mx < 95) & (sat < 30)
    grey = (mx >= 95) & (mx < 175) & (sat < 30)
    ink = dark | grey
    ink[:, :icon.max() + 4 if len(icon) else 0] = False
    text, kinds = "", ""
    for s, e in _runs(ink.any(axis=0)):
        if e - s < 3:
            continue
        m = ink[:, s:e + 1]
        rr = np.where(m.any(axis=1))[0]
        sub = m[rr[0]:rr[-1] + 1]
        h, w = sub.shape
        if not (0.6 * H * 0.018 < h < 1.6 * H * 0.018):  # glyphs are ~42 px high on a 2340 px frame
            return None
        bits = sub[((np.arange(14) + 0.5) * h / 14).astype(int)][:, ((np.arange(10) + 0.5) * w / 10).astype(int)]
        dist = {k: int((bits.reshape(-1) != v).sum()) for k, v in _GLYPH_BITS.items()}
        best = sorted(dist, key=dist.get)
        if dist[best[0]] > 30 or dist[best[1]] - dist[best[0]] < 8:
            return None
        text += best[0]
        kinds += "d" if dark[:, s:e + 1].sum() > grey[:, s:e + 1].sum() else "g"
    if text.count("/") != 1:
        return None
    k, n = text.split("/")
    if not (k.isdigit() and n.isdigit()) or kinds != "d" * len(k) + "g" * (len(n) + 1):
        return None
    return int(k), int(n)


class _Dimmed(ValueError):
    """The game's page under a dark veil: a popup, the win screen or the fail screen."""

    def __init__(self, msg, a):
        super().__init__(msg)
        self.a = a


def _page(image):
    """-> (array, page background, mode): "play" the level page, "tutorial" the dimmed tutorial page with
    the cells to tap left bright, "tutorial_done" the light page of a finished tutorial board ("Got it!")."""
    a = np.asarray(image.convert("RGB")).astype(np.int16)
    H, W, _ = a.shape
    y0, y1 = int(H * 0.285), int(H * 0.78)
    bg = np.median(a[y0:y1, 3:max(6, int(W * 0.025))].reshape(-1, 3), axis=0)
    if np.abs(bg - BG).sum() <= 15:
        return a, bg, "play"
    if np.abs(bg - TUT_DONE_BG).sum() <= 8:
        return a, bg, "tutorial_done"
    ratio = bg / BG
    dim = ratio.max() < 0.8 and ratio.max() - ratio.min() < 0.06  # the game's page under a dark veil
    if np.abs(bg - TUT_BG).sum() <= 12:
        return a, bg, "tutorial"
    msg = (f"not the board: the page background is {bg.astype(int).tolist()}"
           + (" (dimmed: a popup or the win screen)" if dim else " (an ad or another screen)"))
    raise _Dimmed(msg, a) if dim else ValueError(msg)


def _read(image, page=None):
    a, bg, mode = page or _page(image)
    H, W, _ = a.shape
    y0, y1 = int(H * 0.285), int(H * 0.78)
    # the finished tutorial's caption panel is the play page's colour, 17 off its own background
    nb = np.abs(a - bg).sum(axis=2) > (30 if mode == "tutorial_done" else 14)
    Q = nb[y0:y1].mean(axis=0)
    xs = np.where(Q > 0.05)[0]
    if len(xs) < W * 0.2:
        raise ValueError("not the board: nothing in the board area")
    L, R = int(xs[0]), int(xs[-1])
    if mode == "play":
        inner = Q[L:R + 1]
        gaps = [L + (s + e) / 2 for s, e in _runs(inner < 0.3 * np.median(inner)) if e - s >= 2]
    else:
        # the tutorial: a glow, the hand and the caption fill parts of the gaps; over the board's rows only,
        # a gap column is still page background in at least a quarter of the rows, a cell column in nearly none
        Qr0 = nb[y0:y1, L:R + 1].mean(axis=1)
        rr = np.where(Qr0 > 0.5)[0]
        if len(rr) == 0:
            raise ValueError("not the board: no board rows")
        inner = nb[y0 + rr[0]:y0 + rr[-1] + 1, L:R + 1].mean(axis=0)
        gaps = [L + (s + e) / 2 for s, e in _runs(inner < 0.5) if 2 <= e - s <= W * 0.04]
    if len(gaps) < 2:
        raise ValueError("not the board: no gaps between cells")
    p = float(np.median(np.diff(gaps)))
    if not (W * 0.06 < p < W * 0.36):
        raise ValueError(f"not the board: cell pitch {p:.0f} px"
                         + (" (a light page without a grid: the home screen?)" if mode == "tutorial_done" else ""))
    bx = _phase(Q, p, L, R)
    Qr = nb[:, L:R + 1].mean(axis=1)
    ys = [y for y in range(y0, y1) if Qr[y] > 0.35]
    if bx is None or not ys:
        raise ValueError("not the board: no cell lattice")
    by = _phase(Qr, p, ys[0], ys[-1])
    if by is None:
        raise ValueError("not the board: no row lattice")
    g = GAP * W / 1080
    cols, x = [], bx[1] - p * np.floor(bx[1] / p)
    while x + p <= W:
        cols.append((x + g / 2, x + p - g / 2))
        x += p
    rows, y = [], by[1] - p * np.floor((by[1] - y0 + p) / p)
    while y + p <= y1 + p:
        if y >= y0 - 0.1 * p and y + p <= H:
            rows.append((y + g / 2, y + p - g / 2))
        y += p
    # a lattice cell is on the board when its upper half is not page background
    fill = np.zeros((len(rows), len(cols)))
    for i, (ya, yb) in enumerate(rows):
        for j, (xa, xb) in enumerate(cols):
            hh, ww = yb - ya, xb - xa
            fill[i, j] = nb[int(ya + 0.1 * hh):int(ya + 0.5 * hh), int(xa + 0.15 * ww):int(xa + 0.85 * ww)].mean()
    on = fill > 0.85
    ri, ci = np.where(on.any(axis=1))[0], np.where(on.any(axis=0))[0]
    if len(ri) == 0:
        raise ValueError("not the board: no cells")
    r0, r1, c0, c1 = ri[0], ri[-1], ci[0], ci[-1]
    grid, marks, cx, cy = [], {}, [], []
    for j in range(c0, c1 + 1):
        cx.append((cols[j][0] + cols[j][1]) / 2)
    for i in range(r0, r1 + 1):
        ya, yb = rows[i]
        cy.append((ya + yb) / 2)
        line = ""
        for j in range(c0, c1 + 1):
            xa, xb = cols[j]
            cell = a[int(ya):int(yb), int(xa):int(xb)]
            k = _classify_tutorial(cell, bg) if mode == "tutorial" else _classify(cell, bg)
            if k == "H":
                line += k
                continue
            if k == "n":  # a number under the tutorial's veil: read the digit with the veil taken off
                cell = np.clip(cell * (BG / bg), 0, 255).astype(np.int16)
                k = "N"
            if k == " " and nb[int(ya):int(yb), int(xa):int(xb)].mean() > 0.03:
                k = "?"  # outside cells must be clean page background (not a cell fading in)
            if k == "N":
                d = _digit(cell)
                if d is None:
                    raise ValueError(f"a white cell without a readable number at row {i - r0 + 1}, col {j - c0 + 1} "
                                     "(a popup over the board?)")
                k = d
            elif k == ".":
                m = _marks(cell)
                if m:
                    marks[(i - r0, j - c0)] = m
            line += k
        grid.append(line)
    return {"grid": grid, "x": cx, "y": cy, "pitch": p, "marks": marks,
            "edge": (cols[c0][0], W - cols[c1][1]), "counter": _counter(a) if mode == "play" else None,
            "mode": mode, "a": a}


class _Solver:
    """Light Up with propagation; counts solutions up to `limit`."""

    def __init__(self, grid):
        self.R, self.C = len(grid), len(grid[0])
        wall = lambda r, c: grid[r][c] not in ".LC"  # noqa: E731
        self.cells = [(r, c) for r in range(self.R) for c in range(self.C) if not wall(r, c)]
        idx = {p: i for i, p in enumerate(self.cells)}
        self.sees = []
        for (r, c) in self.cells:
            s = []
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                rr, cc = r + dr, c + dc
                while 0 <= rr < self.R and 0 <= cc < self.C and not wall(rr, cc):
                    s.append(idx[(rr, cc)])
                    rr += dr
                    cc += dc
            self.sees.append(s)
        self.clues = []
        for r in range(self.R):
            for c in range(self.C):
                if grid[r][c] in "01234":
                    nb = [idx[(r + dr, c + dc)] for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
                          if (r + dr, c + dc) in idx]
                    self.clues.append((int(grid[r][c]), nb))
        self.solutions, self.nodes, self.exhausted, self.count = [], 0, False, None

    def _light(self, st, i):
        if st[i] == -1:
            return False
        st[i] = 1
        for j in self.sees[i]:
            if st[j] == 1:
                return False
            st[j] = -1
        return True

    def _propagate(self, st):
        changed = True
        while changed:
            changed = False
            for n, nb in self.clues:
                lights = sum(1 for i in nb if st[i] == 1)
                unk = [i for i in nb if st[i] == 0]
                if lights > n or lights + len(unk) < n:
                    return False
                if unk and lights == n:
                    for i in unk:
                        st[i] = -1
                    changed = True
                elif unk and lights + len(unk) == n:
                    for i in unk:
                        if not self._light(st, i):
                            return False
                    changed = True
            for i in range(len(self.cells)):
                if st[i] == 1 or any(st[j] == 1 for j in self.sees[i]):
                    continue
                cand = [j for j in [i] + self.sees[i] if st[j] == 0]
                if not cand:
                    return False
                if len(cand) == 1:
                    if not self._light(st, cand[0]):
                        return False
                    changed = True
        return True

    def _dfs(self, st, limit):
        self.nodes += 1
        if self.nodes > 200000:
            self.exhausted = True
        if self.exhausted or len(self.solutions) >= limit:
            return
        if not self._propagate(st):
            return
        if self.count is not None and st.count(1) > self.count:
            return
        best = None
        for i in range(len(self.cells)):
            if st[i] == 1 or any(st[j] == 1 for j in self.sees[i]):
                continue
            cand = [j for j in [i] + self.sees[i] if st[j] == 0]
            if best is None or len(cand) < len(best):
                best = cand
        if best is None:
            for n, nb in self.clues:
                if sum(1 for i in nb if st[i] == 1) != n:
                    return
            if self.count is not None and st.count(1) != self.count:
                return
            sol = frozenset(self.cells[i] for i in range(len(self.cells)) if st[i] == 1)
            if sol not in self.solutions:
                self.solutions.append(sol)
            return
        j = best[0]
        s1 = list(st)
        if self._light(s1, j):
            self._dfs(s1, limit)
        s2 = list(st)
        s2[j] = -1
        self._dfs(s2, limit)

    def solve(self, limit=2, given=(), count=None):
        """Up to `limit` solutions; `exhausted` is set when the search budget ran out (then unknown)."""
        self.count = count
        st = [0] * len(self.cells)
        idx = {p: i for i, p in enumerate(self.cells)}
        for p in given:
            if not self._light(st, idx[p]):
                return []
        self._dfs(st, limit)
        return self.solutions


def _lit_by(grid, cats):
    R, C = len(grid), len(grid[0])
    lit = set()
    for (r, c) in cats:
        lit.add((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            rr, cc = r + dr, c + dc
            while 0 <= rr < R and 0 <= cc < C and grid[rr][cc] in ".L":
                lit.add((rr, cc))
                rr += dr
                cc += dc
    return lit


def _orange_button(a, y0=0.88, y1=0.92, share=0.5):
    """The orange "Got it!" button under a finished tutorial board (default band), or the bulb hint's
    "Apply" button (y 0.835-0.865) on the veiled page."""
    H, W, _ = a.shape
    reg = a[int(H * y0):int(H * y1), int(W * 0.4):int(W * 0.6)].reshape(-1, 3)
    return ((reg[:, 0] > 200) & (reg[:, 1] > 120) & (reg[:, 1] < 200) & (reg[:, 2] < 90)).mean() > share


def _tutorial(rd, R, C, shown):
    """The tutorial's two scripted boards: the game veils the page and leaves the cell(s) to tap bright."""
    grid = rd["grid"]
    if rd["mode"] == "tutorial_done":
        if any(ch not in "L01234" for row in grid for ch in row) or not _orange_button(rd["a"]):
            return _no(f"not the board: a light page that is not a finished tutorial board. Read: {shown}")
        return {"moves": [], "rescan": False, "done": True,
                "note": f"the tutorial board {R}x{C} is complete: tap \"Got it!\" (364,1425 in a 730x1583 frame) "
                        f"and run solve again on the next tutorial board. Read: {shown}"}
    if _orange_button(rd["a"], 0.835, 0.865, 0.3):
        # the bulb booster's hint has the tutorial's veil, but an orange "Apply" button under the board
        return _no("the bulb hint is up: veiled page with an orange Apply button: tap Apply (364,1348 in a 730x1583 "
                   f"frame) to place its cats, wait 1 s and run solve again. Read: {shown}")
    hot = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == "H"]
    if not hot:
        return _no(f"tutorial: no cell is pointed at (the next hint is still coming): look again. Read: {shown}")
    if len(hot) > 4:
        return _no(f"tutorial: {len(hot)} bright cells, more than a hint shows: misread? Read: {shown}")
    walls = [[ch in "01234#" for ch in row] for row in grid]
    for i, (r, c) in enumerate(hot):
        for r2, c2 in hot[i + 1:]:
            if (r == r2 and not any(walls[r][k] for k in range(min(c, c2) + 1, max(c, c2)))) or                     (c == c2 and not any(walls[k][c] for k in range(min(r, r2) + 1, max(r, r2)))):
                return _no(f"tutorial: the bright cells {(r + 1, c + 1)} and {(r2 + 1, c2 + 1)} see each other: "
                           f"misread? Read: {shown}")
    moves = [[round(rd["x"][c]), round(rd["y"][r]), 2] for r, c in hot]
    return {"moves": moves, "rescan": True, "done": False,
            "note": f"tutorial {R}x{C}: double tap the cell(s) the game lights up {[(r + 1, c + 1) for r, c in hot]} "
                    f"(row, col from 1; H bright, L lit, ? under the hand). Read: {shown}"}


def _from_image(image):
    try:
        rd = _read(image)
    except _Dimmed as e:
        cnt = _counter(e.a, dimmed=True)
        if cnt and cnt[0] == cnt[1] > 0:
            return {"moves": [], "rescan": False, "done": True,
                    "note": f"the win screen: the counter reads {cnt[0]}/{cnt[1]} under the veil, the level is won. "
                            "Take a shot of it for level end won, then tap the \"Level N+1\" button (364,1285)"}
        return _no(str(e) + (f"; the counter reads {cnt[0]}/{cnt[1]}" if cnt else ""))
    except ValueError as e:
        return _no(str(e))
    grid = rd["grid"]
    R, C = len(grid), len(grid[0])
    shown = "|".join(row.replace(" ", "#") for row in grid)
    if not (MIN_SIDE <= R <= MAX_SIDE and MIN_SIDE <= C <= MAX_SIDE):
        return _no(f"implausible grid {R}x{C}: {shown}")
    if rd["mode"] != "play":
        return _tutorial(rd, R, C, shown)
    bad = [(r + 1, c + 1) for r in range(R) for c in range(C) if grid[r][c] == "?"]
    if bad:
        return _no(f"{R}x{C}: cells at (row, col) {bad[:6]} are none of floor/wall/box (the board is still "
                   f"appearing or something covers it): look again in a second. Read: {shown}")
    left, right = rd["edge"]
    if abs(left - right) > rd["pitch"] * 0.6:
        return _no(f"{R}x{C}: the board is not centred (margins {left:.0f}/{right:.0f} px): not the board? {shown}")
    holes = sum(row.count(" ") for row in grid)
    if holes > R * C // 2:
        return _no(f"{R}x{C}: {holes} cells are page background: the board is still appearing or this is not "
                   f"a board. Read: {shown}")
    if holes and not rd["counter"]:
        return _no(f"{R}x{C}: {holes} lattice cells are outside the board (an irregular board, or the board is "
                   f"still appearing) and the counter does not read to confirm: look again. Read: {shown}")
    walls = "".join(ch if ch in "01234" else "#" if ch in "# " else "." for row in grid for ch in row)
    plain = [walls[r * C:(r + 1) * C] for r in range(R)]
    solver = _Solver(plain)
    sols = solver.solve(limit=2)
    if solver.exhausted:
        return _no(f"{R}x{C}: the search ran out of budget on the board read as {shown}: misread?")
    if not sols:
        return _no(f"{R}x{C}: no solution for the board read as {shown}: misread?")
    if len(sols) > 1:
        return _no(f"{R}x{C}: several solutions for the board read as {shown}: misread?")
    sol = sols[0]
    lit = {(r, c) for r in range(R) for c in range(C) if grid[r][c] == "L"}
    placed = sorted(p for p in sol if p in lit)
    expect = _lit_by(grid, placed)
    if expect != lit:
        extra = sorted((r + 1, c + 1) for r, c in lit - expect)
        missing = sorted((r + 1, c + 1) for r, c in expect - lit)
        return _no(f"{R}x{C}: lit cells do not match the cats on the board (lit without a cat {extra[:6]}, "
                   f"dark but lit by a cat {missing[:6]}): an animation or a misread. Read: {shown}")
    todo = sorted(p for p in sol if p not in lit)
    cnt = rd["counter"]
    if cnt and (cnt[1] != len(sol) or cnt[0] != len(placed)):
        return _no(f"{R}x{C}: the counter says {cnt[0]}/{cnt[1]} but the board read gives {len(placed)} placed of "
                   f"{len(sol)}: misread or still animating. Read: {shown}")
    marks = rd["marks"]
    rejected = [(r + 1, c + 1) for r, c in todo if marks.get((r, c)) == "r"]
    if rejected:
        return _no(f"{R}x{C}: the solution puts a cat on {rejected}, where the game already rejected one (red X): "
                   f"the board is misread. Read: {shown}")
    xmarked = [(r + 1, c + 1) for r, c in todo if marks.get((r, c)) == "x"]
    reds = sorted((int(r) + 1, int(c) + 1) for (r, c), m in marks.items() if m == "r")
    info = (f"{R}x{C}, {len(sol)} cats in the solution, {len(placed)} on the board, {len(todo)} to place"
            + (f" (counter {cnt[0]}/{cnt[1]} agrees)" if cnt else " (counter not read)")
            + (f"; {holes} cells outside an irregular board count as walls" if holes else "")
            + (f"; red X (rejected cat) at {reds}" if reds else "")
            + (f"; grey X on solution cells {xmarked}: a single tap may have marked them" if xmarked else "")
            + f". Read (row by row, # box or outside, L lit): {shown}")
    if not todo:
        return {"moves": [], "note": "all cats are placed: the level is done. " + info, "rescan": False,
                "done": True}
    moves = [[round(rd["x"][c]), round(rd["y"][r]), 2] for r, c in todo]
    return {"moves": moves, "note": f"double tap {[(r + 1, c + 1) for r, c in todo]} (row, col from 1). " + info,
            "rescan": True, "done": False}


def _from_board(board, frame_scale):
    rows = board["rows"]
    if len({len(r) for r in rows}) != 1 or len(board["x"]) != len(rows[0]) or len(board["y"]) != len(rows):
        return _no("board shape does not match x/y centers")
    bad = {ch for r in rows for ch in r} - set(".#01234C")
    if bad:
        return _no(f"unknown cells {sorted(bad)}: use . # 0-4 C")
    given = [(r, c) for r in range(len(rows)) for c in range(len(rows[0])) if rows[r][c] == "C"]
    plain = [row.replace("C", ".") for row in rows]
    solver = _Solver(plain)
    sols = solver.solve(limit=2, given=given, count=board.get("count"))
    if solver.exhausted:
        return _no("the search ran out of budget: board misread?")
    if not sols:
        return _no("no solution: board misread?")
    if len(sols) > 1:
        return _no("several solutions: board misread?")
    k = board.get("frame_scale", frame_scale)
    new = sorted(p for p in sols[0] if p not in given)
    moves = [[round(board["x"][c] * k), round(board["y"][r] * k), 2] for r, c in new]
    return {"moves": moves, "note": f"{len(sols[0])} cats total, {len(new)} to place (double tap each): {new}",
            "rescan": True, "done": False}


def solve(image, board=None, frame_scale=1.0):
    if board:
        return _from_board(board, frame_scale)
    return _from_image(image)
