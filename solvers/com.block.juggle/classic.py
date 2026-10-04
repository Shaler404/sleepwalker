"""Block Blast! classic (endless 8x8) solver: reads the board and the 3-piece tray, searches every order and
placement of the tray pieces, and returns the drags that place them. Keeps a memory between rounds.

Reading (full-resolution frame, any size; tuned on 1080x2340):
- the page background is blue (58,80,145); the board is the large non-background block in the upper half,
  refined to its dark frame line (left/right columns and the bottom row dark along their length; the top
  from the square): the rough block includes the rim, the shadow and the dot ring and put the lattice
  0.1-0.2 cell off at the far edges;
- a board cell is empty when its centre patch is the dark navy (34,43,83), filled when it is a bright
  saturated block colour (max channel > 150); anything else (popup dim, line-clear flash, "Good!" text)
  makes the solver refuse;
- the tray is the band 0.5..4.5 cells under the board, split in three slots (thirds of the board width);
  each slot holds 0 or 1 piece: block pixels (colour distance from the page blue > 70: the shadow is
  under 60, the dark bevels of green and purple blocks are above), bounding box, cell pitch 0.45 of a board cell (or a full board cell: the tutorial
  piece), occupancy sampled per tray cell. A slot that cannot be read (a dimmed piece that does not fit)
  is skipped with a note; the other pieces are still played.

Rules modelled: a piece cannot rotate, must lie on empty cells; after a placement every full row and full
column clears at once; the tray refills only after all three pieces are placed; the game is lost when no
tray piece fits.

Search: every order of the remaining pieces x every legal placement (bitboards), clears applied, leaf
scored by lines cleared, open cells, room for the hard pieces (3x3, 1x5, 5x1, 2x3 L), fragmentation
(empty/filled transitions) and isolated holes. When no order places all pieces, the line placing the most
is returned and the note says the game is about to end. Modes: "gameover" (the default since lab
2026-10-03: a classic level is played to its end screen) fills the board with the fewest clears; a --board
file with {"mode": "score"} plays for score instead (scored as above). The mode is kept in the memory.
Game over: no tray piece fits, or the "No Space Left" banner (a dark band over the tray) -> done.

Drag (lab 2026-10-03 refit on v10.8.1: 73 landed drops of sessions 20261003-193423 and -212548, plus the
screen recording): the game centres the lifted piece on the touch point, lifts it DRAG_LIFT cells and moves
it DRAG_GAIN times faster than the finger: piece bbox centre = touch + GAIN * (finger - touch) - (0, LIFT),
board cells. The old lift 2.84 (fit on v10.6.5 landings) was 0.5 cell too high: the recording shows a
1-row piece held at the tray touch point (finger not moving up) floating at 8.05 cells, half under the
board, and the landings fit lift 2.40 (69 of 73 rows right; with 2.84 pieces landed 0.37 row lower than
predicted on average, the "one row low" drops). So the bottom row is reached by moving the finger about
0.55 cell up from the touch point: every drag to row 7 the old model sent was held near the tray with
the piece under the board, which the game rejects (session -212548 got stuck with only row 7 empty).
- The touch goes on the centre of a filled tray block (the one nearest the bbox centre): touches on the
  bbox centre that fell on an empty cell or on the seam between two blocks failed again and again (the
  same drop 13 times in a row in session -230945) while every manual drag started on a block worked. A
  retried barred drop touches another block (session -212548: a Z failed twice from a top block and
  landed from its bottom-right block).
- Errors are one-sided: a drop lands right or a row short (lower), more often than not for drops predicted
  at x.3-x.5. So the aim is AIM_UP cells above the target centre and, on leftward drags, up to LEAD cells
  ahead sideways. Rightward drags overshoot instead (4 of 65 landed a column right with the lead, lab
  2026-10-04): they aim LEAD_RIGHT (0.1 cell) behind.
- A drop is rejected when the piece is off the board at release (it flies back). The finger may end far
  under the board: drops landed with the finger 1.72 cells under it (row 7, session -193423). The old
  "finger more than 1.65 cells under the board is ignored" rule (v10.6.5) was the wrong lift seen from
  the landings. MAX_FINGER_BELOW_BOARD = 2.1 only keeps the finger off the tray pieces.
- After a refill the first move is a warm-up: the first piece is touched and pulled 0.4 cell down (the
  finger ends far under the board, so the game puts it back), then the real drags follow.

Memory (state): the last board, tray and plan. A planned piece still in its slot whose target cells were
and still are empty did not drop: that placement is barred for this tray and the next best line is
played, so a failing drag is never repeated. The note starts with what the last round did.

Moves are all the tray pieces in order (their outcome is known: the tray does not refill before the last
one); rescan is always true (the refill is random).

Fallback: --board FILE with {"board": ["........", ...8 rows, '#' filled], "pieces": [[".#.", "###"], null,
["###"]] (per slot, null = empty slot)} uses the frame only for geometry.
"""
import itertools

import numpy as np

BG = np.array([58, 80, 145])
EMPTY = np.array([34, 43, 83])
N = 8
TRAY_PITCH = 0.45          # tray cell / board cell
DEFAULT_MODE = "gameover"  # fill the board to reach the end screen fast; "normal" = play for score
FRAGILE = {"gameover": 4.0, "normal": 2.0}  # cost of a placement whose one-row-lower twin is blocked
FRAME_INSET = 0.0055       # board dark frame line, fraction of the frame's outer width (5 px of 962)
# drag model, board-cell units (cell ~81 px at 730 px width), measured from the touch point
DRAG_GAIN = 1.46
DRAG_LIFT = 2.40           # lab 2026-10-03 on v10.8.1 (was 2.84: rows 7 never reached, drops one row low)
# the finger may end this far under the board (drops landed at 1.72; a tray piece sits at ~2.4)
MAX_FINGER_BELOW_BOARD = 2.1
AIM_UP = 0.2               # aim this far above the target centre (drops land right or short; lab 2026-10-03: 0.3 with the true lift left 0.2 margin above)
AIM_UP_MIN = -0.05         # a low target may be aimed down to here (less margin) when AIM_UP is out of reach
RETRY_UP = 0.2             # a barred drop retried after every block was touched: aim this much higher per cycle
RETRY_UP_MAX = 0.4         # ... up to this (misses land short: a row low, never high)
LEAD = 0.2                 # leftward drags: aim up to this far ahead (left) of the target centre
# rightward drags: aim this far BEHIND (left of) the target centre. Lab 2026-10-04 replay of 156 solver drops
# (sessions -193423, -212548, -235233): 0 horizontal misses in 60 leftward drags, but 4 of 65 rightward drags
# overshot one column right with the +0.2 lead (all needed >= 0.3 cell less), while every rightward drop that
# landed would still have landed 0.3-0.5 cell further left. Rightward drops do not land short.
LEAD_RIGHT = -0.1
WARMUP_PULL = 0.4          # warm-up after a refill: touch the first piece and pull it this far down
TRAY_BELOW_BOARD = 2.35    # tray piece centre, cells under the board (for the room estimate)

FULL = (1 << 64) - 1
ROWS = [sum(1 << (r * 8 + c) for c in range(8)) for r in range(8)]
COLS = [sum(1 << (r * 8 + c) for r in range(8)) for c in range(8)]


def _no(note, **extra):
    return {"moves": [], "note": note, "rescan": False, "done": False, **extra}


def _runs(mask, min_len=1, max_gap=0):
    out, start, gap = [], None, 0
    for i, v in enumerate(list(mask) + [False] * (max_gap + 1)):
        if v:
            if start is None:
                start = i
            gap = 0
            end = i
        elif start is not None:
            gap += 1
            if gap > max_gap:
                if end - start + 1 >= min_len:
                    out.append((start, end))
                start, gap = None, 0
    return out


# ---------------------------------------------------------------- reading

def find_board(a):
    """(x0, y0, cell) of the board in image pixels, or a reason string."""
    H, W, _ = a.shape
    nonbg = np.abs(a - BG).sum(2) > 40
    rf = nonbg[:, int(W * .1):int(W * .9)].mean(1)
    runs = [r for r in _runs(rf > 0.6, min_len=int(W * .5), max_gap=int(W * .02)) if r[0] < H * .75]
    if not runs:
        return "no board-sized block on the page background"
    y0, y1 = max(runs, key=lambda r: r[1] - r[0])
    cf = nonbg[y0:y1 + 1].mean(0)
    cruns = _runs(cf > 0.6, min_len=int(W * .5), max_gap=int(W * .02))
    if not cruns:
        return "no board columns"
    x0, x1 = max(cruns, key=lambda r: r[1] - r[0])
    w, h = x1 - x0 + 1, y1 - y0 + 1
    if abs(w - h) > 0.04 * w or w < 0.6 * W:
        return f"board block is not square ({w}x{h})"
    # The block found above is the board plus its soft rim and shadow, and from score ~319 on also the
    # glowing dot ring around it: 10-20 px too wide at 1080 px, so the lattice was off by 0.1-0.2 cell at
    # the far edges (session 20261003-193423: a drop to r5c5 missed). Refine on the board's dark frame
    # line: the outermost columns/rows near the rough edges that are dark along their whole length.
    dark = a.max(2) < 90
    e = int(w * 0.03)
    cf = dark[y0 + e * 4:y1 - e * 4].mean(0)
    xs = [x for x in range(max(0, x0 - e), min(W, x1 + e)) if cf[x] > 0.95]
    if xs and xs[0] < x0 + 2 * e and xs[-1] > x1 - 2 * e:
        x0, x1 = xs[0], xs[-1]
    # the top edge has a dark bevel above the frame line (rows 532-547 at 1080 wide): take the bottom
    # frame line, which is sharp, and the square
    rf = dark[:, x0 + e * 4:x1 - e * 4].mean(1)
    ys = [y for y in range(max(0, y1 - 2 * e), min(H, y1 + e)) if rf[y] > 0.95]
    if ys:
        y1 = ys[-1]
    w = x1 - x0 + 1
    y0 = y1 - w + 1
    # the dark frame is ~5 px of 962 at 1080 wide: the cells sit inside it
    inset = w * FRAME_INSET
    cell = (w - 2 * inset) / N
    return x0 + inset, y0 + inset, cell


def classify_cells(a, x0, y0, cell):
    board, bad = [[0] * N for _ in range(N)], []
    for r in range(N):
        for c in range(N):
            cx, cy = x0 + (c + .5) * cell, y0 + (r + .5) * cell
            h = cell * .2
            p = a[int(cy - h):int(cy + h), int(cx - h):int(cx + h)].reshape(-1, 3)
            m = p.mean(0)
            if np.abs(m - EMPTY).sum() < 35 and p.std(0).max() < 14:
                board[r][c] = 0
            elif m.max() > 150 and m.max() - m.min() > 60:
                board[r][c] = 1
            else:
                bad.append((r, c, [int(v) for v in m]))
    return board, bad


def _read_slot(m, cell, s):
    """One tray slot (block mask) -> (shape, touch point in slot pixels) or (None, why)."""
    rows = _runs(m.sum(1) > cell * .15, max_gap=int(cell * .15))
    cols = _runs(m.sum(0) > cell * .15, max_gap=int(cell * .15))
    if len(rows) != 1 or len(cols) != 1:
        return None, f"slot {s + 1}: piece is not one block (rows {rows}, cols {cols})"
    (py0, py1), (px0, px1) = rows[0], cols[0]
    w, h = px1 - px0 + 1, py1 - py0 + 1
    best = None
    for pitch in (cell * TRAY_PITCH, cell):
        nw, nh = w / pitch, h / pitch
        err = abs(nw - round(nw)) + abs(nh - round(nh))
        if 1 <= round(nw) <= 5 and 1 <= round(nh) <= 5 and (best is None or err < best[0]):
            best = (err, pitch, int(round(nw)), int(round(nh)))
    if best is None or best[0] > 0.5:
        return None, f"slot {s + 1}: piece size {w}x{h} px is not a whole number of cells"
    _, pitch, nw, nh = best
    pw, ph = w / nw, h / nh
    shape = []
    for r in range(nh):
        row = ""
        for c in range(nw):
            cy, cx = py0 + (r + .5) * ph, px0 + (c + .5) * pw
            q = m[int(cy - ph * .25):int(cy + ph * .25) + 1, int(cx - pw * .25):int(cx + pw * .25) + 1]
            f = q.mean()
            if .2 < f < .6:
                return None, f"slot {s + 1}: tray cell ({r},{c}) half filled ({f:.2f})"
            row += "#" if f >= .6 else "."
        shape.append(row)
    if any("#" not in row for row in shape) or any(all(row[c] == "." for row in shape) for c in range(nw)):
        return None, f"slot {s + 1}: shape {shape} has an empty edge row/column"
    # touch the filled block nearest the bbox centre (a touch on an empty cell or a seam may miss)
    bcx, bcy = (px0 + px1) / 2, (py0 + py1) / 2
    blocks = [(px0 + (c + .5) * pw, py0 + (r + .5) * ph) for r, c in cells_of(shape)]
    blocks.sort(key=lambda p: (p[0] - bcx) ** 2 + (p[1] - bcy) ** 2)
    return {"shape": shape, "centre": (bcx, bcy), "touch": blocks[0], "blocks": blocks}, None


def read_tray(a, x0, y0, cell):
    """[piece or None] * 3 and notes about skipped slots; a piece is {"shape", "centre", "touch"} (image px)."""
    H, W, _ = a.shape
    bw = cell * N
    ty0, ty1 = int(y0 + bw + .5 * cell), int(min(H, y0 + bw + 4.5 * cell))
    band = a[ty0:ty1]
    # block pixels: far from the page blue. The piece shadow is 44-56 away, the dark bevel of a purple
    # block 88 (a 120 cut read a purple corner cell as half filled, session 20261003-193423 frame 32)
    blockpx = np.abs(band - BG).sum(2) > 70
    pieces, notes = [], []
    for s in range(3):
        sx0, sx1 = int(x0 + s * bw / 3), int(x0 + (s + 1) * bw / 3)
        m = blockpx[:, sx0:sx1]
        if m.sum() < (cell * .3) ** 2:
            pieces.append(None)
            continue
        p, why = _read_slot(m, cell, s)
        if p is None:
            pieces.append(None)
            notes.append(why)
            continue
        p["centre"] = (sx0 + p["centre"][0], ty0 + p["centre"][1])
        p["touch"] = (sx0 + p["touch"][0], ty0 + p["touch"][1])
        p["blocks"] = [(sx0 + bx, ty0 + by) for bx, by in p["blocks"]]
        pieces.append(p)
    return pieces, notes


# ---------------------------------------------------------------- rules

def cells_of(shape):
    return [(r, c) for r, row in enumerate(shape) for c, ch in enumerate(row) if ch == "#"]


def mask_of(shape, r0, c0):
    return sum(1 << ((r0 + r) * 8 + c0 + c) for r, c in cells_of(shape))


def placements(shape):
    h, w = len(shape), len(shape[0])
    return [(r0, c0, mask_of(shape, r0, c0)) for r0 in range(N - h + 1) for c0 in range(N - w + 1)]


def place(bb, pm):
    bb |= pm
    full = 0
    lines = 0
    for m in ROWS:
        if bb & m == m:
            full |= m
            lines += 1
    for m in COLS:
        if bb & m == m:
            full |= m
            lines += 1
    return bb & ~full, lines


def _low_ok(shape, r0):
    """Whether a placement is droppable from a tray piece at the usual height (cell units)."""
    sy = N + TRAY_BELOW_BOARD
    ty_max = sy - DRAG_LIFT + DRAG_GAIN * (N + MAX_FINGER_BELOW_BOARD - sy)
    return r0 + len(shape) / 2 - AIM_UP_MIN <= ty_max


HARD = [[p for p in placements(s) if _low_ok(s, p[0])] for s in (["###", "###", "###"], ["#####"], ["#", "#", "#", "#", "#"],
                               ["##", "##"], ["###", "#..", "#.."], ["###", "..#", "..#"],
                               ["#..", "#..", "###"], ["..#", "..#", "###"])]
HARD_W = [3.0, 1.5, 1.5, 0.6, 0.8, 0.8, 0.8, 0.8]


def evaluate(bb, lines, mode="normal"):
    empty = 64 - bin(bb).count("1")
    if mode == "gameover":  # fill the board: no clears, few open cells
        return -lines * 6 - empty * 0.6
    # room for hard pieces
    room = 0.0
    for pl, w in zip(HARD, HARD_W):
        n = sum(1 for _, _, m in pl if not bb & m)
        room += w * (min(n, 4) / 4) + (-w * 3 if n == 0 else 0)
    # fragmentation: empty/filled transitions along rows and columns (walls count as filled)
    trans = 0
    holes = 0
    for r in range(N):
        prev = 1
        for c in range(N):
            v = (bb >> (r * 8 + c)) & 1
            trans += v != prev
            prev = v
        trans += prev != 1
    for c in range(N):
        prev = 1
        for r in range(N):
            v = (bb >> (r * 8 + c)) & 1
            trans += v != prev
            prev = v
        trans += prev != 1
    for r in range(N):
        for c in range(N):
            if (bb >> (r * 8 + c)) & 1:
                continue
            nb = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            if all(not (0 <= rr < N and 0 <= cc < N) or (bb >> (rr * 8 + cc)) & 1 for rr, cc in nb):
                holes += 1
    return lines * 6 + empty * 0.6 + room * 2 - trans * 1.0 - holes * 4


def search(bb, pieces, reachable, mode="normal"):
    """Best line over orders/placements. pieces: list of (slot, shape). Returns (n_placed, value, line).
    A placement is fragile when the cells one row lower are not free: about 4 drops in 10 of session
    20261003-193423 landed one row lower than aimed (once two), and a fragile drop then hits a block and
    flies back; a robust one still lands (one row off). Fragile placements cost FRAGILE[mode] each."""
    pls = {s: [p for p in placements(shape) if reachable(s, shape, p[0], p[1])] for s, shape in pieces}
    hs = {s: len(shape) for s, shape in pieces}
    pen = FRAGILE.get(mode, FRAGILE["normal"])
    best = [(-1, -1e9, [])]
    seen = {}

    def rec(bb, left, lines, line, frag):
        key = (bb, left, lines, frag)
        if key in seen:
            return
        seen[key] = 1
        moved = False
        for s in left:
            for r0, c0, m in pls[s]:
                if bb & m:
                    continue
                moved = True
                weak = r0 + hs[s] < N and bool(bb & (m << 8))
                nb, ln = place(bb, m)
                rec(nb, tuple(x for x in left if x != s), lines + ln, line + [(s, r0, c0, ln)], frag + weak)
        if not moved or not left:
            n = len(line)
            v = evaluate(bb, lines, mode) - pen * frag - (50 * len(left) if left else 0)
            if (n, v) > best[0][:2]:
                best[0] = (n, v, line)

    rec(bb, tuple(s for s, _ in pieces), 0, [], 0)
    return best[0]


# ---------------------------------------------------------------- drag

def drag(touch, shape, r0, c0, x0, y0, cell, extra_up=0.0):
    """Finger swipe (sx, sy, fx, fy) that drops the piece with its top-left cell at (r0, c0), or None when
    the finger would have to end too low (the game ignores such a drop)."""
    h, w = len(shape), len(shape[0])
    tx, ty = x0 + (c0 + w / 2) * cell, y0 + (r0 + h / 2) * cell
    sx, sy = touch
    # drops land right or short along the drag: aim a little up and ahead, still inside the cell
    k = max(-1.0, min(1.0, (tx - sx) / (2 * cell)))
    tx += (LEAD if k < 0 else LEAD_RIGHT) * cell * abs(k) * (1 if k >= 0 else -1)
    ty_max = sy - DRAG_LIFT * cell + DRAG_GAIN * (y0 + (N + MAX_FINGER_BELOW_BOARD) * cell - sy)
    aim = ty - (AIM_UP + extra_up) * cell
    if aim > ty_max:
        if ty - AIM_UP_MIN * cell > ty_max + 0.5:
            return None
        aim = ty_max
    fx = sx + (tx - sx) / DRAG_GAIN
    fy = sy + (aim - sy + DRAG_LIFT * cell) / DRAG_GAIN
    return sx, sy, fx, fy


def drag_any(touch, shape, r0, c0, x0, y0, cell):
    """The plain aimed drag, whatever the finger height (for the last-resort low drops)."""
    h, w = len(shape), len(shape[0])
    tx, ty = x0 + (c0 + w / 2) * cell, y0 + (r0 + h / 2) * cell
    sx, sy = touch
    return sx, sy, sx + (tx - sx) / DRAG_GAIN, sy + (ty - sy + DRAG_LIFT * cell) / DRAG_GAIN


# ---------------------------------------------------------------- memory

def _bb_of(grid):
    return sum(1 << (r * 8 + c) for r in range(N) for c in range(N) if grid[r][c])


def recall(state, tray, bb):
    """What the last round did, from the memory: (barred placements for this tray, note, new tray?)."""
    shapes = [p["shape"] if p else None for p in tray]
    if not state or "tray" not in state:
        return [], "", True
    prev = state["tray"]
    new_tray = any(cur is not None and cur != old for cur, old in zip(shapes, prev))
    if new_tray:
        return [], "", True
    barred = [tuple(b) for b in state.get("barred", [])]
    pbb = int(state.get("board", "0"), 16)
    said = []
    missed_before = False  # an earlier piece of the plan is still in the tray: the clears it made did not happen
    for s, r0, c0 in state.get("plan", []):
        if shapes[s] is None or shapes[s] != prev[s]:
            continue  # placed
        m = mask_of(shapes[s], r0, c0)
        waited = missed_before and bool(pbb & m)
        missed_before = True
        if waited:  # its cells were blocked and an earlier drop missed: not tried for real (session -212548 step 13)
            said.append(f"slot{s + 1} -> r{r0}c{c0} not placed (the clear it waited for did not happen)")
        elif not bb & m:  # its cells are free now and it is still in the tray: the drag was tried and missed
            barred.append((s, r0, c0))  # once per miss: the count picks another touch block on a retry
            said.append(f"slot{s + 1} -> r{r0}c{c0} did not drop (barred)")
        elif pbb & m:
            said.append(f"slot{s + 1} -> r{r0}c{c0} not placed (the clear it waited for did not happen)")
        else:
            said.append(f"slot{s + 1} -> r{r0}c{c0} not placed (an earlier piece landed on its cells)")
    return barred, ("last round: " + "; ".join(said) + ". ") if said else "", False


# ---------------------------------------------------------------- entry

def solve(image, board=None, frame_scale=1.0, state=None):
    a = np.asarray(image.convert("RGB")).astype(int)
    H, W, _ = a.shape
    # Every classic level is played to its game-over screen (an endless game played for score never ends
    # within the budget), so filling is the default and needs no --board: a typed --board in every call is
    # what the lab reads as a bypassed solver. {"mode": "score"} plays for score (clears lines).
    mode = (state or {}).get("mode", DEFAULT_MODE)
    if board and board.get("mode"):
        mode = "normal" if board["mode"] in ("score", "normal") else board["mode"]
    keep = {"mode": mode}
    geo = find_board(a)
    if isinstance(geo, str):
        return _no(f"not a classic board: {geo}", state={**(state or {}), **keep})
    x0, y0, cell = geo
    # page background left of the board and under it, clear of the glowing dot ring (score ~319 on)
    bg_probe = np.vstack([a[int(y0):int(y0 + 8 * cell), :int(x0 * .3)].reshape(-1, 3),
                          a[int(y0 + 8 * cell + .55 * cell):int(y0 + 8 * cell + .8 * cell)].reshape(-1, 3)])
    if np.abs(bg_probe.mean(0) - BG).sum() > 30:
        return _no(f"page background {bg_probe.mean(0).astype(int).tolist()} is not the game's blue: popup or dim",
                   state={**(state or {}), **keep})
    # "No Space Left": the game over banner, a dark band across the whole width over the tray, the board
    # full of colour behind it (session 20261003-193423 frames 33, 38: read before as "a clear is animating")
    band = a[int(y0 + 8 * cell + .5 * cell):int(min(H, y0 + 8 * cell + 4.5 * cell))]
    if (( band.max(2) < 100).mean(1) > 0.9).sum() > cell:
        return {"moves": [], "note": "GAME OVER: the No Space Left banner is up (the interstitial and the "
                "'Can you Top that?' screen follow)", "rescan": False, "done": True, "state": keep}
    tray_notes = []
    if board and board.get("board"):
        grid = [[1 if ch == "#" else 0 for ch in row] for row in board["board"]]
        tray = []
        for s, shp in enumerate(board.get("pieces", [None] * 3)):
            c = (x0 + (s + .5) * 8 * cell / 3, y0 + 8 * cell + 2.35 * cell)
            tray.append(None if shp is None else {"shape": shp, "centre": c, "touch": c})
    else:
        grid, bad = classify_cells(a, x0, y0, cell)
        if bad:
            return _no(f"{len(bad)} board cell(s) neither empty nor a block (animation or popup): {bad[:3]}",
                       state={**(state or {}), **keep})
        # a refilled tray glows (light-blue halo around each new piece) for ~1 s: the halo read as blocks
        # (session 20261003-212548 frame 39: a 1x2 and two 1x4 read as 3x4 crosses). Pixels slightly off
        # the page blue cover ~7% of a slot normally, 24-28% with the glow.
        tb = a[int(y0 + 8.5 * cell):int(min(H, y0 + 12.5 * cell))]
        dist = np.abs(tb - BG).sum(2)
        halo = max((((dist > 20) & (dist <= 70))[:, int(x0 + k * 8 * cell / 3):int(x0 + (k + 1) * 8 * cell / 3)]).mean()
                   for k in range(3))
        if halo > 0.18:
            return _no(f"tray glow ({halo:.2f}): the refill is animating", state={**(state or {}), **keep})
        tray, tray_notes = read_tray(a, x0, y0, cell)
    bb = _bb_of(grid)
    if place(bb, 0)[1]:
        return _no("the board has a full line: a clear is still animating", state={**(state or {}), **keep})
    pieces = [(s, p["shape"]) for s, p in enumerate(tray) if p]
    board_txt = "/".join("".join("#" if v else "." for v in row) for row in grid)
    if not pieces:
        why = f"tray unreadable: {'; '.join(tray_notes)}" if tray_notes else "tray empty (refill animating?)"
        return _no(why, state={**(state or {}), **keep})
    barred, said, new_tray = recall(state, tray, bb)

    def touch_of(s, r0, c0):
        """The block nearest the bbox centre; a placement that missed before touches the next block."""
        bl = tray[s].get("blocks") or [tray[s]["touch"]]
        return bl[barred.count((s, r0, c0)) % len(bl)]

    def extra_up_of(s, r0, c0):
        """Every block touched and still missed: the touch was not the cause, aim higher (misses land short)."""
        bl = tray[s].get("blocks") or [tray[s]["touch"]]
        return min(RETRY_UP_MAX, RETRY_UP * (barred.count((s, r0, c0)) // len(bl)))

    def droppable(s, shape, r0, c0):
        return (s, r0, c0) not in barred and drag(tray[s]["touch"], shape, r0, c0, x0, y0, cell) is not None

    n, val, line = search(bb, pieces, droppable, mode)
    risky_low = retry = False
    if n < len(pieces):
        unbarred = lambda s, shape, r0, c0: drag(tray[s]["touch"], shape, r0, c0, x0, y0, cell) is not None  # noqa: E731
        n2, val2, line2 = search(bb, pieces, unbarred, mode)
        if n2 > n:  # only a barred placement lets more pieces in: try it once more
            n, val, line, retry = n2, val2, line2, True
    if n < len(pieces):
        n2, val2, line2 = search(bb, pieces, lambda *a_: True, mode)
        if n2 > n:
            n, val, line, risky_low = n2, val2, line2, True
    tray_txt = " | ".join("x".join(map(str, (len(p["shape"][0]), len(p["shape"])))) + ":" + "/".join(p["shape"])
                          if p else "-" for p in tray)
    if tray_notes:
        tray_txt += f" (skipped: {'; '.join(tray_notes)})"
    if n <= 0:
        if tray_notes:
            return _no(f"{said}no readable tray piece fits; unread slot(s): {'; '.join(tray_notes)}. board {board_txt}",
                       state={**(state or {}), **keep})
        return {"moves": [], "note": f"{said}GAME OVER: no tray piece fits. board {board_txt}; tray {tray_txt}",
                "rescan": False, "done": True, "state": keep}
    moves, desc, retry_desc = [], [], []
    first = tray[line[0][0]]["touch"]
    warm = new_tray and len(pieces) == 3
    if warm:
        moves.append([round(first[0]), round(first[1]), round(first[0]), round(min(H - 2, first[1] + WARMUP_PULL * cell))])
    for s, r0, c0, ln in line:
        shape = tray[s]["shape"]
        t = touch_of(s, r0, c0)
        up = extra_up_of(s, r0, c0)
        d = (drag(t, shape, r0, c0, x0, y0, cell, up) or drag(t, shape, r0, c0, x0, y0, cell)
             or drag_any(t, shape, r0, c0, x0, y0, cell))
        k = barred.count((s, r0, c0))
        if k:
            retry_desc.append(f"slot{s + 1} missed {k}x, touch block {k % len(tray[s].get('blocks') or [0]) + 1}"
                              + (f", aim +{up:.1f} cell higher" if up else ""))
        sx, sy, fx, fy = d
        fx = min(max(fx, 1), W - 2)
        fy = min(max(fy, 1), H - 2)
        moves.append([round(sx), round(sy), round(fx), round(fy)])
        desc.append(f"slot{s + 1} {'/'.join(shape)} -> r{r0}c{c0}" + (f" clears {ln}" if ln else ""))
    note = (f"{said}board {board_txt}; tray {tray_txt}; plan: " + ("warm-up pull; " if warm else "")
            + "; ".join(desc))
    note = f"[mode {'score' if mode == 'normal' else mode}] " + note
    if retry:
        note = (f"RETRY of a barred drop (nothing else fits; {'; '.join(retry_desc)}"
                + ("; 4+ misses: place it by hand from a tray block" if any(
                    barred.count((s, r0, c0)) >= 4 for s, r0, c0, _ in line) else "") + "): " + note)
    if risky_low:
        note = "UNTESTED low drop (finger ends near the tray; it failed before): check the result. " + note
    if n < len(pieces):
        note = f"only {n} of {len(pieces)} pieces fit: game over after these. " + note
    mem = {**keep, "tray": [p["shape"] if p else None for p in tray], "board": format(bb, "x"),
           "plan": [[s, r0, c0] for s, r0, c0, _ in line], "barred": [list(b) for b in barred]}
    return {"moves": moves, "note": note, "rescan": True, "done": False, "state": mem}
