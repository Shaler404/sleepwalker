"""Meowdoku (Queens-like): one cat per color region, row and column; no two cats touch (8-neighbourhood).
Reads the board from the screenshot, solves it by backtracking, returns double taps ([x, y, 2]) for every
missing cat in ONE round with done=True (the moves finish the level, the run stops: no second look at the
win popup). It returns no moves when the read is not plausible: a grid
outside 4-12, a colour region that is not connected, more cats than rows, no solution or more than one."""
import numpy as np

# cells per round. It was 3 (fear of lost double taps in long batches), so `solve --run` needed 4-5 rounds
# and players placed the cats by hand in one batch instead (L84-L128: 9-10 double taps per batch never lost
# a cat). All cats in one round; the rescan round re-taps any cat that did not land and reports done.
MAX_CELLS = 12


def _runs(profile, thr):
    runs, start = [], None
    for i, v in enumerate(profile):
        if v > thr and start is None:
            start = i
        elif v <= thr and start is not None:
            runs.append((start, i - 1))
            start = None
    if start is not None:
        runs.append((start, len(profile) - 1))
    return runs


def _read(image):
    a = np.asarray(image.convert("RGB")).astype(int)
    H, W, _ = a.shape
    y0, y1 = int(H * 0.28), int(H * 0.78)
    band = a[y0:y1]
    sat = band.max(axis=2) - band.min(axis=2)
    mask = sat > 25
    rows = _runs(mask.sum(axis=1), W * 0.25)
    rows = [r for r in rows if r[1] - r[0] > H * 0.02]
    # columns: use only the rows' span
    ry0, ry1 = rows[0][0], rows[-1][1]
    cols = _runs(mask[ry0:ry1 + 1].sum(axis=0), (ry1 - ry0) * 0.25)
    cols = [c for c in cols if c[1] - c[0] > W * 0.03]
    n = len(cols)
    if len(rows) != n:
        # merge/split fallback: assume a square grid from the column pitch
        pitch = (cols[-1][1] - cols[0][0]) / n
        rows = [(int(ry0 + i * pitch), int(ry0 + (i + 1) * pitch) - 4) for i in range(n)]
    cells = []
    for (ra, rb) in rows:
        line = []
        for (ca, cb) in cols:
            h, w = rb - ra, cb - ca
            cell = band[ra:rb, ca:cb]
            m = max(2, int(min(h, w) * 0.06))
            k = max(3, int(min(h, w) * 0.16))
            ring = np.concatenate([cell[m:k, m:-m].reshape(-1, 3), cell[-k:-m, m:-m].reshape(-1, 3),
                                   cell[m:-m, m:k].reshape(-1, 3), cell[m:-m, -k:-m].reshape(-1, 3)])
            s = ring.max(axis=1) - ring.min(axis=1)
            ring = ring[s > 25] if (s > 25).sum() > 10 else ring
            color = np.median(ring, axis=0)
            core = cell[int(h * 0.3):int(h * 0.7), int(w * 0.25):int(w * 0.75)]
            dark = (core.max(axis=2) < 70).mean()
            cx, cy = (ca + cb) / 2, y0 + (ra + rb) / 2
            line.append({"color": color, "cat": dark > 0.05, "xy": (cx, cy)})
        cells.append(line)
    # cluster colors: merge the closest groups until there are n (sparkles and highlights shift a few cells)
    n = len(cells)
    groups = [[(r, c)] for r in range(n) for c in range(n)]
    import colorsys
    col = {}
    for r in range(n):
        for c in range(n):
            R, G, B = (float(v) / 255 for v in cells[r][c]["color"])
            col[(r, c)] = colorsys.rgb_to_hsv(R, G, B)

    def d1(a, b):
        dh = abs(a[0] - b[0])
        dh = min(dh, 1 - dh) * 360
        return dh + 40 * abs(a[1] - b[1]) + 40 * abs(a[2] - b[2])

    def dist(g1, g2):
        return max(d1(col[a], col[b]) for a in g1 for b in g2)

    while len(groups) > n:
        best = None
        for i in range(len(groups)):
            for j in range(i + 1, len(groups)):
                d = dist(groups[i], groups[j])
                if best is None or d < best[0]:
                    best = (d, i, j)
        _, i, j = best
        groups[i] += groups.pop(j)
    labels = [[0] * n for _ in range(n)]
    for gi, g in enumerate(groups):
        for r, c in g:
            labels[r][c] = gi
    centers = groups
    return cells, labels, len(centers)


def _solve(n, labels, fixed):
    sol = [None] * n
    for r, c in fixed:
        if sol[r] is not None:
            return None
        sol[r] = c

    def ok(r, c, placed):
        for (pr, pc) in placed:
            if pc == c or labels[pr][pc] == labels[r][c] or (abs(pr - r) <= 1 and abs(pc - c) <= 1):
                return False
        return True

    order = [r for r in range(n) if sol[r] is None]
    placed = [(r, sol[r]) for r in range(n) if sol[r] is not None]
    for i, a in enumerate(placed):
        for b in placed[i + 1:]:
            if not ok(b[0], b[1], [a]):
                return None

    def bt(i):
        if i == len(order):
            return True
        r = order[i]
        for c in range(n):
            if ok(r, c, placed):
                placed.append((r, c))
                if bt(i + 1):
                    return True
                placed.pop()
        return False

    if not bt(0):
        return None
    return placed


def _regions_connected(n, labels):
    # every colour region of a real board is one connected piece; a misread colour splits or scatters it
    for g in {labels[r][c] for r in range(n) for c in range(n)}:
        cells = [(r, c) for r in range(n) for c in range(n) if labels[r][c] == g]
        seen, stack = {cells[0]}, [cells[0]]
        while stack:
            r, c = stack.pop()
            for rr, cc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= rr < n and 0 <= cc < n and labels[rr][cc] == g and (rr, cc) not in seen:
                    seen.add((rr, cc))
                    stack.append((rr, cc))
        if len(seen) != len(cells):
            return False
    return True


def _count_solutions(n, labels, fixed, limit=2):
    # a real board has exactly one solution: a second one means the board was misread
    rows = {r: c for r, c in fixed}
    order = [r for r in range(n) if r not in rows]
    placed = list(fixed)
    found = [0]

    def ok(r, c):
        return all(pc != c and labels[pr][pc] != labels[r][c] and not (abs(pr - r) <= 1 and abs(pc - c) <= 1)
                   for pr, pc in placed)

    def bt(i):
        if found[0] >= limit:
            return
        if i == len(order):
            found[0] += 1
            return
        r = order[i]
        for c in range(n):
            if ok(r, c):
                placed.append((r, c))
                bt(i + 1)
                placed.pop()

    bt(0)
    return found[0]


def solve(image, board=None, frame_scale=1.0):
    def none(note):
        return {"moves": [], "note": note, "rescan": False, "done": False}

    try:
        cells, labels, k = _read(image)
    except Exception as e:  # noqa: BLE001
        return none(f"could not read the board: {e}")
    n = len(cells)
    if not 4 <= n <= 12:
        return none(f"read a {n}x{n} grid: not a board (popup or ad on screen?)")
    fixed = [(r, c) for r in range(n) for c in range(n) if cells[r][c]["cat"]]
    if len(fixed) > n:
        bright = np.median([max(cells[r][c]["color"]) for r in range(n) for c in range(n)])
        if bright < 110:
            # a dark veil over the whole board (Golden Fish "Only Golden Fish - Be careful!" tooltip): the cells
            # are too dark to tell a cat from a colour, and taps there may only close the tooltip
            return none(f"{n}x{n}: the board is dimmed by an overlay (tooltip or popup, median brightness "
                        f"{bright:.0f}): tap a neutral area to close it, then solve")
        return none(f"{n}x{n}: read {len(fixed)} cats, more than {n}: cats misread")
    if len(fixed) == n and all(a[0] != b[0] and a[1] != b[1] and max(abs(a[0] - b[0]), abs(a[1] - b[1])) > 1
                               for i, a in enumerate(fixed) for b in fixed[i + 1:]):
        # the win animation dims the colours: judge a full board by the cats alone
        return {"moves": [], "note": f"{n}x{n}: all {n} cats are on the board", "rescan": False, "done": True}
    if not _regions_connected(n, labels):
        return none(f"{n}x{n}: a colour region is not connected, colours misread; labels={labels}")
    placed = _solve(n, labels, fixed)
    if placed is None:
        return none(f"{n}x{n}, no solution with cats {fixed}; labels={labels}")
    if _count_solutions(n, labels, fixed) > 1:
        return none(f"{n}x{n}: more than one solution, the board was misread; labels={labels}")
    missing = [rc for rc in sorted(placed) if rc not in fixed]
    moves = [[round(cells[r][c]["xy"][0]), round(cells[r][c]["xy"][1]), 2] for r, c in missing[:MAX_CELLS]]
    # The board has exactly one solution and these moves place every missing cat: they finish the level, so
    # the run stops after this round without a second look. The second look used to land on whatever the
    # game shows after the last cat (Daily: "New trial skin" popup, "Pure logic" banner over the board), read
    # it as no board and end the run as given up (lab 2026-10-06: 3 of 5 such runs, all of them wins).
    complete = len(moves) == len(missing)
    return {"moves": moves, "note": f"{n}x{n}, {k} colors, given cats {fixed}, solution {sorted(placed)}; "
                                    f"labels={labels}", "rescan": not complete, "done": complete}
