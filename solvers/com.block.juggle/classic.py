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
is returned and the note says the game is about to end. Gameover mode first looks for a BLOCK line
(block_search, lab 2026-10-06 (4)): 1-2 placements after which no other tray piece fits, so the game ends
with pieces left in the tray; filling alone never ended a game (the game deals trays that fit). Modes: "gameover" (the default since lab
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

Adventure (lab 2026-10-06): the same solver plays the Adventure levels. The mode follows the screen (back
chevron top left = adventure = score mode; gold crown = classic = gameover) unless --board sets it. Done
(no moves) on: the goal header all checked, the result panel (won: purple Next Level; lost: green Retry).
A passing animation (gem fly, line clear, refill glow) gets a "WAIT" round: a tray piece pulled down and
let go, so the run takes a new frame instead of stopping (at most 3 in a row).

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
# Score mode values a placement by the game's points for its clears, not by the line count (lab 2026-10-06 (7),
# read off the Adventure score bar of session 20261006-141221, L11 and L12, 47 rounds exact): a placement
# scores 1 per cell plus 10 * k(k+1)/2 for k lines cleared at once (1 line 10, 2 lines 30, 3 lines 60), and
# past ~81% of a score target the cells stop counting (only clears). SCORE_TRI counts k lines at once as
# k(k+1)/2 in the search. OFF: an offline game simulator (96 games x 30 random trays drawn from the 504 logged
# score-mode tray pieces, true scoring) gave only +3% points (845 -> 870) and more game overs (21 -> 26 of 96).
SCORE_TRI = False
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


# ---------------------------------------------------------------- screens around the board (lab 2026-10-06)
# Measured on 1080x2340 frames, regions in 730-wide model px (scaled by W/730). Adventure sessions -235233,
# -004506, -015205 ended 7 of 8 runs "gave up" on screens that are the level's natural end or a passing gem
# animation: the goal header all green-checked, the result panel, gems flying over the board.

def _reg(a, x0, y0, x1, y1):
    s = a.shape[1] / 730
    return a[int(y0 * s):int(y1 * s), int(x0 * s):int(x1 * s)].reshape(-1, 3)


def is_adventure(a):
    """Adventure shows a light back chevron at the top left; classic a gold crown with the best score
    (chevron 0.10 of the patch, gold 0 / gold 0.24, chevron 0)."""
    tl = _reg(a, 30, 95, 110, 175)
    gold = ((tl[:, 0] > 200) & (tl[:, 1] > 140) & (tl[:, 2] < 100)).mean()
    chev = ((tl[:, 2] > 200) & (tl[:, 0] > 130) & (tl[:, 0] < 220)).mean()
    return chev > 0.05 and gold < 0.02


def goals_done(a):
    """Adventure gem goals: under each goal icon a white counter, a green check once collected. All checked
    (green 0.085 of the band, white 0) = the level is won; the result panel follows (-015205 frame 22: the
    solver planned a drop on the emptied board, which 'did not drop')."""
    hb = _reg(a, 150, 258, 580, 318)
    green = ((hb[:, 1] > 150) & (hb[:, 0] < 140) & (hb[:, 2] < 110)).mean()
    white = (hb.min(1) > 215).mean()
    return green > 0.03 and white < 0.005


def result_panel(a):
    """'won' / 'lost' / None: the adventure result screen, a dark navy page with the light 'Consecutive
    Victories' banner on top and a purple 'Next (Hard) Level' button (won) or a green 'Retry' (lost).
    The button sits lower on gem levels (y ~1100-1180 of 730 wide) than on the score-target "Well Done!"
    panel (y ~1030-1125, session 20261006-133549 frame 150, missed before lab 2026-10-06 (7)): the button
    band is searched over y 980-1240."""
    page = _reg(a, 5, 1350, 60, 1550).mean(0)
    ban = _reg(a, 180, 175, 550, 290).mean(0)
    if not (page.max() < 90 and page[2] > page[0] and ban.min() > 170):
        return None
    s = a.shape[1] / 730
    y0 = 980
    reg = a[int(y0 * s):int(1240 * s), int(180 * s):int(550 * s)]
    purple = ((reg[..., 2] > 190) & (reg[..., 0] > 130) & (reg[..., 1] < 150)).mean(1)
    green = ((reg[..., 1] > 150) & (reg[..., 0] < 130) & (reg[..., 2] < 100)).mean(1)
    if (purple > 0.6).sum() > 30 * s:
        return "won"  # purple "Next Hard Level"
    rows = np.where(green > 0.6)[0]
    if len(rows) < 30 * s:
        return None
    # green: "Next Level" (won, text ends at x ~512 of 730) or "Retry" (lost, text ends at ~470)
    strip = a[int(y0 * s + rows[0]):int(y0 * s + rows[-1]), int(160 * s):int(570 * s)]
    cols = np.where((strip.min(2) > 215).sum(0) > 2)[0]
    if not len(cols):
        return None
    return "won" if 160 + cols[-1] / s > 495 else "lost"


def game_page(a):
    """The game's own pages are blue (board page (61,84,149), classic result (22,100,198), dimmed result
    page (16,30,70), map (60,77,135)) along the left edge; interstitials are not (black loading frame,
    videos, store pages: session 20261006-133549 frames 21-28, 48-50, 100-108, 142-148)."""
    left = _reg(a, 0, 300, 25, 1400).mean(0)
    return left[2] > left[0] + 35 and left[2] > left[1] + 30


def result_arriving(a):
    """The Adventure result is coming in: the page dims to navy (16,30,70) and the board is gone, while the
    Consecutive Victories banner slides down (frame 91 of session 20261006-133549) or the score counts up
    in a disc on the emptied board (frame 149, a score-target level). Not yet the panel: no button."""
    left = _reg(a, 0, 300, 25, 1400).mean(0)
    page = _reg(a, 5, 1350, 60, 1550).mean(0)
    if not (left.max() < 90 and page.max() < 90 and left[2] > left[0] + 35 and page[2] > page[0] + 35):
        return False
    # dimmed popups over the game (Open with sheet, Award, a leave dialog) dim the page the same way: ask for
    # the banner (>= 30 light rows of 730 px in the top 330) or the bright blue score disc in the board centre
    s = a.shape[1] / 730
    top = a[:int(330 * s), int(180 * s):int(550 * s)]
    if ((top.min(2) > 200).mean(1) > 0.8).sum() / s >= 30:
        return True
    # the disc on the dark emptied board (bright 0.03 of the board area; an Award or leave-dialog panel 0.5-1)
    disc = _reg(a, 320, 610, 410, 700)
    bright = (_reg(a, 40, 370, 690, 1020).max(1) > 150).mean()
    return ((disc[:, 2] > 180) & (disc[:, 0] < 120)).mean() > 0.5 and bright < 0.06


def classic_result(a):
    """The classic game-over result screen (session 20261006-105231 frames 21, 46, 60, 85): a bright blue (or, on
    a new best, purple) page
    with no board, a gold title that rotates (Can you Top that?, Your Best is Next, ...), Score and Best Score
    and a green Play button. When the game ended without an interstitial the run reached it straight after
    the BLOCK round and stopped as "not a classic board" (gave up), game 2 of that session.
    (button green 0.91, title gold 0.12-0.27, top page (24,67,181); boards and ads: green <= 0.05)"""
    btn = _reg(a, 180, 1070, 550, 1150)
    green = ((btn[:, 1] > 150) & (btn[:, 0] < 120) & (btn[:, 2] < 80)).mean()
    orange = ((btn[:, 0] > 190) & (btn[:, 1] > 120) & (btn[:, 1] < 200) & (btn[:, 2] < 90)).mean()
    title = _reg(a, 20, 380, 710, 560)
    gold = ((title[:, 0] > 200) & (title[:, 1] > 140) & (title[:, 2] < 120)).mean()
    top = _reg(a, 0, 0, 730, 300).mean(0)
    # blue page + green Play, or the purple page + orange Play of a new best ("Can you Top that?",
    # session 20261003-193423 frame 39: button (218,159,38), top (83,21,168))
    return max(green, orange) > 0.6 and gold > 0.05 and top[2] > 150 and top[0] < 120 and top[1] < 100


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
                gain = ln * (ln + 1) // 2 if (mode == "normal" and SCORE_TRI) else ln
                rec(nb, tuple(x for x in left if x != s), lines + gain, line + [(s, r0, c0, ln)], frag + weak)
        if not moved or not left:
            n = len(line)
            v = evaluate(bb, lines, mode) - pen * frag - (50 * len(left) if left else 0)
            if (n, v) > best[0][:2]:
                best[0] = (n, v, line)

    rec(bb, tuple(s for s, _ in pieces), 0, [], 0)
    return best[0]


def block_search(bb, pieces, reachable):
    """Gameover mode, lab 2026-10-06 (4): a line of 1 or 2 placements after which NO remaining tray piece fits
    anywhere, so the game ends at once ("No Space Left"). The game deals trays that fit the board as dealt
    (84 trays of session 20261006-084209 all placed in full, filling only made it deal 1x1s and diagonals and
    forced clears: 10.7 min, no game over), but it does not check the order: in that game 79 of the 84 trays
    from round 5 on had such a blocking line (73 of 110 recorded trays over three sessions).
    Returns (line, robust) or None; line items are (slot, r0, c0, lines). Ranked: fewest fragile drops
    (cells one row lower blocked), then the block still holding if a drop lands one row low or a column off
    (robust), then the fewest pieces placed."""
    if len(pieces) < 2:
        return None
    pls = {s: [p for p in placements(shape) if reachable(s, shape, p[0], p[1])] for s, shape in pieces}
    allm = {s: [m for _, _, m in placements(shape)] for s, shape in pieces}
    hs = {s: len(shape) for s, shape in pieces}
    ws = {s: len(shape[0]) for s, shape in pieces}
    shp = dict(pieces)

    def blocked(b, rest):
        return all(all(b & m for m in allm[s]) for s in rest)

    def twins(s, r0, c0):
        out = []
        for dr, dc in ((1, 0), (0, -1), (0, 1)):
            r, c = r0 + dr, c0 + dc
            if 0 <= r <= N - hs[s] and 0 <= c <= N - ws[s]:
                out.append(mask_of(shp[s], r, c))
        return out

    best = None
    slots = [s for s, _ in pieces]
    for k in (1, 2):
        if k >= len(slots):
            break
        for order in itertools.permutations(slots, k):
            rest = [s for s in slots if s not in order]

            def rec(b, i, line, frag):
                nonlocal best
                if i == k:
                    if not blocked(b, rest):
                        return
                    # robustness: the last drop landing one row low or a column off still blocks
                    s, r0, c0 = line[-1][:3]
                    prev = line[-2][4] if k == 2 else bb
                    rob = 0
                    for tm in twins(s, r0, c0):
                        if not prev & tm and blocked(place(prev, tm)[0], rest):
                            rob += 1
                    key = (frag, -rob, k, sum(x[3] for x in line))
                    if best is None or key < best[0]:
                        best = (key, [x[:4] for x in line], rob)
                    return
                s = order[i]
                for r0, c0, m in pls[s]:
                    if b & m:
                        continue
                    weak = r0 + hs[s] < N and bool(b & (m << 8))
                    nb, ln = place(b, m)
                    rec(nb, i + 1, line + [(s, r0, c0, ln, nb)], frag + weak)

            rec(bb, 0, [], 0)
        if best is not None and best[0][0] == 0:
            break  # a sure 1-piece block: no need to look at 2-piece lines
    return None if best is None else (best[1], best[2])


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
    """What the last round did, from the memory: (barred placements for this tray, note, new tray?, nothing
    changed?)."""
    shapes = [p["shape"] if p else None for p in tray]
    if not state or "tray" not in state:
        return [], "", True, False
    prev = state["tray"]
    new_tray = any(cur is not None and cur != old for cur, old in zip(shapes, prev))
    if new_tray:
        return [], "", True, False
    barred = [tuple(b) for b in state.get("barred", [])]
    pbb = int(state.get("board", "0"), 16)
    plan = state.get("plan", [])
    # Nothing of the last plan happened (same board, every planned piece still in its slot): the moves were
    # most likely never sent. Session 20261006-105231 lost the adb link inside `solve --run` four times; the
    # memory had the plan of the round that crashed and the next call barred all three placements as "did not
    # drop" and skipped the warm-up (games 3 and 5). All drags of a plan missing together is the seam-touch bug
    # of session -230945, fixed since: so the first time, the plan is simply played again (with the warm-up);
    # a second unchanged round in a row bars as before.
    if (plan and bb == pbb and not state.get("unchanged")
            and all(shapes[s] is not None and shapes[s] == prev[s] for s, _, _ in plan)):
        return barred, ("last round: nothing changed (the moves were probably not sent: adb drop?): planned "
                        "again once. "), True, True
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
    return barred, ("last round: " + "; ".join(said) + ". ") if said else "", False, False


# ---------------------------------------------------------------- entry

def solve(image, board=None, frame_scale=1.0, state=None):
    a = np.asarray(image.convert("RGB")).astype(int)
    H, W, _ = a.shape
    # Every classic level is played to its game-over screen (an endless game played for score never ends
    # within the budget), so filling is the default and needs no --board: a typed --board in every call is
    # what the lab reads as a bypassed solver. {"mode": "score"} plays for score (clears lines).
    # Adventure (the same board with a goal) plays for score with no --board: the back chevron at the top left
    # says which mode it is, on every board frame (lab 2026-10-06: two adventure sessions passed --board or
    # typed the JSON inline, which failed once). An explicit mode (--board, kept in the memory) still wins;
    # memories older than this kept "mode" for every run: only their score mode counts as explicit.
    st = state or {}
    explicit = st.get("mode") if (st.get("mode_set") or st.get("mode") == "normal") else None
    if board and board.get("mode"):
        explicit = "normal" if board["mode"] in ("score", "normal") else board["mode"]
    keep = {"mode": explicit, "mode_set": True} if explicit else {}
    rp = result_panel(a)
    if rp:
        return {"moves": [], "rescan": False, "done": True, "state": keep,
                "note": ("LEVEL WON: the result panel (Consecutive Victories, Next Level)" if rp == "won" else
                         "LEVEL LOST: the result panel (You Can Do It!, Retry)") + ": level end " + rp}
    if classic_result(a):
        return {"moves": [], "rescan": False, "done": True, "state": keep,
                "note": "GAME OVER: the classic result screen (Score, Best Score, Play): level end lost"}
    adventure = is_adventure(a)
    mode = explicit or ("normal" if adventure else DEFAULT_MODE)
    geo = find_board(a)
    if isinstance(geo, str):
        # Lab 2026-10-06 (7): 3 of 4 Adventure runs of session 20261006-133549 stopped here as "gave up" right
        # after the winning round: on the result panel sliding in (frame 91) and on the interstitial that
        # plays BEFORE the result panel (frames 100, 142). The memory says this level was being played.
        if st.get("adv") or adventure:
            if result_arriving(a):
                return {"moves": [], "rescan": False, "done": True, "state": keep,
                        "note": "LEVEL OVER: the Adventure result panel is coming in (dimmed page, no board): "
                                "take a shot when the button is up; Next Level = level end won, Retry = lost"}
            if st.get("adv") and not game_page(a):
                return {"moves": [], "rescan": False, "done": True, "state": keep,
                        "note": "LEVEL OVER: an interstitial covers the screen right after an Adventure round "
                                "(in Adventure the ad plays before the result panel): close the ad, then take "
                                "a shot of the result panel; Next Level = level end won, Retry = lost"}
        return _no(f"not a classic board: {geo}", state={**st, **keep})
    x0, y0, cell = geo
    if adventure and goals_done(a):
        return {"moves": [], "rescan": False, "done": True, "state": keep,
                "note": "LEVEL WON: every goal in the header is checked (the result panel follows)"}

    def wait(why):
        """A passing animation (gems flying to their counters, a line clearing, the refill glow): instead of
        stopping the run, pull a tray piece down and let it go back (the refill warm-up, harmless) so the run
        takes a fresh frame. At most 3 in a row; the pull length differs each time (the harness stops a run
        that repeats its moves)."""
        k = st.get("waits", 0)
        if k >= 3 or (board and board.get("board")):
            return _no(f"{why} ({k} waits)", state={**st, **keep})
        tray_w, _ = read_tray(a, x0, y0, cell)
        ps = [p for p in tray_w if p]
        # no readable piece (a new game's tray still growing in, session 20261006-105231 frame 22): the pull
        # starts on the middle slot, which is harmless whether a piece is there or not
        t = (min(ps, key=lambda p: len(p["shape"]))["touch"] if ps
             else (x0 + 4 * cell, y0 + 8 * cell + TRAY_BELOW_BOARD * cell))
        pull = min(H - 2, t[1] + (WARMUP_PULL + 0.1 * k) * cell)
        return {"moves": [[round(t[0]), round(t[1]), round(t[0]), round(pull)]], "rescan": True, "done": False,
                "note": f"WAIT {k + 1}: {why}; pulled a tray piece back as a pause", "state": {**st, **keep, "waits": k + 1, **({"adv": True} if adventure else {})}}
    # page background left of the board and under it, clear of the glowing dot ring (score ~319 on)
    bg_probe = np.vstack([a[int(y0):int(y0 + 8 * cell), :int(x0 * .3)].reshape(-1, 3),
                          a[int(y0 + 8 * cell + .55 * cell):int(y0 + 8 * cell + .8 * cell)].reshape(-1, 3)])
    # median, not mean: gems flying over the page under the board (stars of session 20261006-141221 frame 102)
    # moved the mean to (74,91,140) and the run stopped as gave up; the median stays the page blue there,
    # while a dimmed page (105231, (8,37,63)) is still refused
    bg_med = np.median(bg_probe, 0)
    if np.abs(bg_med - BG).sum() > 30:
        return _no(f"page background {bg_med.astype(int).tolist()} is not the game's blue: popup or dim",
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
            return wait(f"{len(bad)} board cell(s) neither empty nor a block (animation or popup): {bad[:3]}")
        # a refilled tray glows (light-blue halo around each new piece) for ~1 s: the halo read as blocks
        # (session 20261003-212548 frame 39: a 1x2 and two 1x4 read as 3x4 crosses). Pixels slightly off
        # the page blue cover ~7% of a slot normally, 24-28% with the glow.
        tb = a[int(y0 + 8.5 * cell):int(min(H, y0 + 12.5 * cell))]
        dist = np.abs(tb - BG).sum(2)
        halo = max((((dist > 20) & (dist <= 70))[:, int(x0 + k * 8 * cell / 3):int(x0 + (k + 1) * 8 * cell / 3)]).mean()
                   for k in range(3))
        if halo > 0.18:
            return wait(f"tray glow ({halo:.2f}): the refill is animating")
        tray, tray_notes = read_tray(a, x0, y0, cell)
    bb = _bb_of(grid)
    if place(bb, 0)[1]:
        return wait("the board has a full line: a clear is still animating")
    pieces = [(s, p["shape"]) for s, p in enumerate(tray) if p]
    board_txt = "/".join("".join("#" if v else "." for v in row) for row in grid)
    if not pieces:
        if tray_notes:
            return _no(f"tray unreadable: {'; '.join(tray_notes)}", state={**(state or {}), **keep})
        return wait("tray empty: the refill or a new game's tray is still animating")
    barred, said, new_tray, unchanged = recall(state, tray, bb)

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

    blk = block_search(bb, pieces, droppable) if mode == "gameover" else None
    if blk:
        line, rob = blk
        moves = []
        if new_tray and len(pieces) == 3:
            f = tray[line[0][0]]["touch"]
            moves.append([round(f[0]), round(f[1]), round(f[0]), round(min(H - 2, f[1] + WARMUP_PULL * cell))])
        desc = []
        for s, r0, c0, ln in line:
            shape = tray[s]["shape"]
            t = touch_of(s, r0, c0)
            up = extra_up_of(s, r0, c0)
            sx, sy, fx, fy = (drag(t, shape, r0, c0, x0, y0, cell, up) or drag(t, shape, r0, c0, x0, y0, cell)
                              or drag_any(t, shape, r0, c0, x0, y0, cell))
            moves.append([round(sx), round(sy), round(min(max(fx, 1), W - 2)), round(min(max(fy, 1), H - 2))])
            desc.append(f"slot{s + 1} {'/'.join(shape)} -> r{r0}c{c0}" + (f" clears {ln}" if ln else ""))
        left = [f"slot{s + 1}" for s, _ in pieces if s not in [x[0] for x in line]]
        tray_txt = " | ".join("/".join(p["shape"]) if p else "-" for p in tray)
        note = (f"[mode gameover] {said}BLOCK: after {'; '.join(desc)} no room is left for {', '.join(left)}: "
                f"the game should end now (No Space Left; run again to see it). "
                f"Still blocks if the last drop lands a row low / a column off: {rob} of 3. "
                f"board {board_txt}; tray {tray_txt}")
        mem = {**keep, "tray": [p["shape"] if p else None for p in tray], "board": format(bb, "x"),
               "plan": [[s, r0, c0] for s, r0, c0, _ in line], "barred": [list(b) for b in barred],
               "unchanged": unchanged}
        return {"moves": moves, "note": note, "rescan": True, "done": False, "state": mem}
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
           "plan": [[s, r0, c0] for s, r0, c0, _ in line], "barred": [list(b) for b in barred],
               "unchanged": unchanged}
    if adventure:
        mem["adv"] = True
    return {"moves": moves, "note": note, "rescan": True, "done": False, "state": mem}
