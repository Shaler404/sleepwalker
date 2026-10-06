"""Block Blast! More Games > Sudoku: reads the N x N board (6x6 with 2x3 boxes at level 1) and the digit tray,
solves it (backtracking, unique solution checked) and returns the taps: a tray digit, then every empty cell
that takes it, digit after digit.

Reading (lab 2026-10-06 on 1080x2340 frames of session 20261005-153835, level 1):
- grid: dark brown lines (R<120, G<80, B<50) crossing 90%+ of the board; the outer lines and the thick
  (box) lines give N and the box shape (6x6: thick every 2 rows and every 3 columns);
- a cell is empty when its centre is plain wood (no glyph pixels); otherwise a tile (pink, or yellow when its
  digit is the selected one) with a dark brown glyph (about (95,45,18));
- digits: the glyph bbox is cut to a 10x14 bitmap and matched against the glyphs of the tray (digits 1..N
  slot by slot, same font) and the bitmaps kept below (1-6, from the level-1 tray) for the digits the tray
  no longer shows (a digit leaves the tray once all of it is placed). A glyph matching no digit well, or a board that breaks a rule, is refused.
- refused: a dimmed page (the out-of-hearts sheet, the Pass Level panel), a red-outlined (wrong) cell.

Input (session -153835 step 46): tapping a tray digit selects it (it stays selected, its tiles turn
yellow); tapping an empty cell then puts that digit there. A wrong digit costs one of 3 hearts.
"""
import numpy as np

GW, GH = 10, 14
# bitmaps of the level-1 tray glyphs (rows of GW bits, '#' = glyph) and their aspect (w/h), taken from frame
# 00050 of session -153835; used for the digits the tray no longer shows (a digit leaves the tray once all of
# it is placed: frames 51-54)
KNOWN = {
    1: (['........##', '...#######', '##########', '##....####', '......####', '......####', '......####', '......####', '......####', '......####', '......####', '......####', '......####', '......####'], 0.394),
    2: (['...####...', '.########.', '.##....##.', '##.....##.', '##.....##.', '.......##.', '......##..', '.....###..', '....###...', '...###....', '..###.....', '.###......', '.#########', '##########'], 0.682),
    3: (['...#####..', '.########.', '.##....###', '###....###', '.......###', '.......##.', '...#####..', '...######.', '.......###', '........##', '##......##', '###....###', '.########.', '...#####..'], 0.642),
    4: (['......##..', '.....###..', '.....###..', '....####..', '...##.##..', '...##.##..', '..##..##..', '..##..##..', '.##...##..', '##########', '##########', '......##..', '......##..', '......##..'], 0.754),
    5: (['.#########', '.#########', '.##.......', '.##.......', '.##.......', '.#######..', '.########.', '.......###', '........##', '........##', '##......##', '###....###', '.########.', '..######..'], 0.636),
    6: (['.....###..', '...#####..', '..###.....', '.###......', '###.......', '########..', '#####..##.', '###....###', '###.....#.', '###.....##', '###.....##', '.###...###', '..#.#####.', '...####...'], 0.618),
}
KNOWN = {d: (np.array([[ch == "#" for ch in row] for row in rows]), asp) for d, (rows, asp) in KNOWN.items()}


def _no(note):
    return {"moves": [], "note": note, "rescan": False, "done": False}


def _runs(mask, min_len=1):
    out, start = [], None
    for i, v in enumerate(list(mask) + [False]):
        if v and start is None:
            start = i
        elif not v and start is not None:
            if i - start >= min_len:
                out.append((start, i - 1))
            start = None
    return out


def glyph_mask(a):
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    return (r < 160) & (g < 100) & (b < 70) & (r > g + 25)


def bitmap(m):
    ys, xs = np.nonzero(m)
    if len(ys) < 10:
        return None
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    g = m[y0:y1, x0:x1].astype(float)
    h, w = g.shape
    out = np.zeros((GH, GW))
    for i in range(GH):
        for j in range(GW):
            out[i, j] = g[int(i * h / GH):max(int(i * h / GH) + 1, int((i + 1) * h / GH)),
                          int(j * w / GW):max(int(j * w / GW) + 1, int((j + 1) * w / GW))].mean()
    return out > .5, w / h


def match(bm, templates):
    """(digit, distance) of the nearest template; the distance mixes bitmap mismatch and aspect ratio."""
    best = (None, 9.0)
    for d, (t, asp) in templates.items():
        dist = (bm[0] != t).mean() + abs(bm[1] - asp) * .5
        if dist < best[1]:
            best = (d, dist)
    return best


def find_grid(a):
    H, W, _ = a.shape
    dark = (a[..., 0] < 120) & (a[..., 1] < 80) & (a[..., 2] < 50)
    rows = _runs(dark[:, int(W * .1):int(W * .9)].mean(1) > .9)
    rows = [r for r in rows if H * .1 < r[0] < H * .8]
    if len(rows) < 4:
        return "no grid lines"
    y0, y1 = rows[0][0], rows[-1][1]
    cols = _runs(dark[y0:y1].mean(0) > .9)
    if len(cols) < 4:
        return "no grid columns"
    x0, x1 = cols[0][0], cols[-1][1]
    if abs((x1 - x0) - (y1 - y0)) > .04 * (x1 - x0):
        return f"grid is not square ({x1 - x0}x{y1 - y0})"
    n = len(rows) - 1
    if n != len(cols) - 1 or n not in (4, 6, 8, 9):
        return f"grid of {len(rows) - 1}x{len(cols) - 1} lines"
    thick_r = [i for i, (s, e) in enumerate(rows) if e - s + 1 >= 1.6 * min(e2 - s2 + 1 for s2, e2 in rows)]
    thick_c = [i for i, (s, e) in enumerate(cols) if e - s + 1 >= 1.6 * min(e2 - s2 + 1 for s2, e2 in cols)]
    bh = min(b - a_ for a_, b in zip(thick_r, thick_r[1:])) if len(thick_r) > 2 else n
    bw = min(b - a_ for a_, b in zip(thick_c, thick_c[1:])) if len(thick_c) > 2 else n
    if n % bh or n % bw or bh * bw != n:
        return f"box shape {bh}x{bw} does not tile {n}x{n}"
    ys = [(s + e) / 2 for s, e in rows]
    xs = [(s + e) / 2 for s, e in cols]
    return n, bh, bw, xs, ys


def read_tray(a, gy1, n):
    """Glyphs of the tray under the board: [(digit, (cx, cy), bitmap)], left to right."""
    H, W, _ = a.shape
    band = a[int(gy1 + H * .03):int(H * .91)]
    m = glyph_mask(band)
    import cv2
    k, lab, st, cen = cv2.connectedComponentsWithStats(m.astype(np.uint8), connectivity=8)
    comps = [(st[i], cen[i]) for i in range(1, k) if st[i][3] > H * .015 and st[i][4] > 30 and st[i][2] < W * .1]
    comps.sort(key=lambda c: c[0][0])
    out = []
    for i, (s, c) in enumerate(comps):
        x, y, w, h = s[:4]
        bm = bitmap(m[y:y + h, x:x + w])
        out.append((i + 1, (x + w / 2, gy1 + H * .03 + y + h / 2), bm))
    return out


def solve_grid(g, n, bh, bw, limit=2):
    sols = []
    cells = [(r, c) for r in range(n) for c in range(n)]

    def ok(r, c, d):
        if any(g[r][k] == d for k in range(n)) or any(g[k][c] == d for k in range(n)):
            return False
        r0, c0 = r - r % bh, c - c % bw
        return not any(g[r0 + i][c0 + j] == d for i in range(bh) for j in range(bw))

    def rec():
        best = None
        for r, c in cells:
            if g[r][c]:
                continue
            opts = [d for d in range(1, n + 1) if ok(r, c, d)]
            if not opts:
                return
            if best is None or len(opts) < len(best[2]):
                best = (r, c, opts)
        if best is None:
            sols.append([row[:] for row in g])
            return
        r, c, opts = best
        for d in opts:
            g[r][c] = d
            rec()
            g[r][c] = 0
            if len(sols) >= limit:
                return

    rec()
    return sols


def solve(image, board=None, frame_scale=1.0):
    a = np.asarray(image.convert("RGB")).astype(int)
    H, W, _ = a.shape
    top = a[int(H * .01):int(H * .04), int(W * .3):int(W * .7)].reshape(-1, 3).mean(0)
    if not (top[0] > 180 and top[0] > top[2] + 50):
        return _no(f"not the Sudoku page (top {top.astype(int).tolist()} is not light wood): popup or another screen")
    gr = find_grid(a)
    if isinstance(gr, str):
        return _no(f"not a sudoku board: {gr}")
    n, bh, bw, xs, ys = gr
    tray = read_tray(a, ys[-1], n)
    # a tray slot per digit, evenly over the board width (level 1: x 80..645 of 730, within 12 px of this)
    slot_x = [xs[0] + (i + .5) * (xs[-1] - xs[0]) / n for i in range(n)]
    tray = [(int(np.argmin([abs(cx - sx) for sx in slot_x])) + 1, (cx, cy), bm) for _, (cx, cy), bm in tray]
    if len({d for d, _, _ in tray}) != len(tray):
        return _no(f"tray glyphs do not sit one per slot: {[(d, int(cx)) for d, (cx, _), _ in tray]}")
    templates = dict(KNOWN)
    templates.update({d: bm for d, _, bm in tray if bm})
    if len(templates) < n:
        return _no(f"no glyph for digits {sorted(set(range(1, n + 1)) - set(templates))}: the tray does not show them")
    gm = glyph_mask(a)
    grid, worst = [[0] * n for _ in range(n)], 0.0
    for r in range(n):
        for c in range(n):
            x0, x1, y0, y1 = xs[c], xs[c + 1], ys[r], ys[r + 1]
            ins = (x1 - x0) * .15
            cell = a[int(y0 + ins):int(y1 - ins), int(x0 + ins):int(x1 - ins)]
            red = ((cell[..., 0] > 200) & (cell[..., 1] < 80) & (cell[..., 2] < 80)).mean()
            if red > .02:
                return _no(f"cell r{r + 1}c{c + 1} is outlined red (a wrong digit): wait and look again")
            m = gm[int(y0 + ins):int(y1 - ins), int(x0 + ins):int(x1 - ins)]
            if m.mean() < .01:
                continue
            bm = bitmap(m)
            d, dist = match(bm, templates)
            if d is None or dist > .25:
                return _no(f"cell r{r + 1}c{c + 1}: glyph matches no digit (best {d}, {dist:.2f})")
            grid[r][c] = d
            worst = max(worst, dist)
    txt = "/".join("".join(str(v) if v else "." for v in row) for row in grid)
    sols = solve_grid([row[:] for row in grid], n, bh, bw)
    if not sols:
        return _no(f"board {txt} has no solution: misread (or a wrong digit on the board)")
    sol = sols[0]
    agree = [[all(s[r][c] == sol[r][c] for s in sols) for c in range(n)] for r in range(n)]
    tap = {d: (cx, cy) for d, (cx, cy), _ in tray}
    moves, plan = [], []
    for d in range(1, n + 1):
        cells = [(r, c) for r in range(n) for c in range(n) if not grid[r][c] and sol[r][c] == d and agree[r][c]]
        if not cells:
            continue
        if d not in tap:
            return _no(f"board {txt}: digit {d} is still needed but not in the tray: misread")
        moves.append([round(tap[d][0]), round(tap[d][1])])
        for r, c in cells:
            moves.append([round((xs[c] + xs[c + 1]) / 2), round((ys[r] + ys[r + 1]) / 2)])
        plan.append(f"{d}: " + " ".join(f"r{r + 1}c{c + 1}" for r, c in cells))
    if not moves:
        return {"moves": [], "note": f"board {txt} is full", "rescan": False, "done": True}
    complete = all(agree[r][c] for r in range(n) for c in range(n))
    note = (f"{n}x{n} boxes {bh}x{bw}; board {txt}; worst glyph match {worst:.2f}; "
            + ("unique solution" if len(sols) == 1 else "two solutions: only the cells they share")
            + "; " + "; ".join(plan))
    return {"moves": moves, "note": note, "rescan": not complete, "done": complete}
