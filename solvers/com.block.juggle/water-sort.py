"""Block Blast! More Games > Water Sort: reads the tubes and their colour layers, searches a full solution
(every pour known: no hidden layers seen) and returns the taps (source tube, then target tube).

Reading (lab 2026-10-06 on 1080x2340 frames of session 20261005-231555, levels 1-2):
- page: dark violet (30,23,65); tube glass outline light grey-lilac (190-215, 185-210, 200-230);
- tubes are the tall connected outline components between 15% and 80% of the frame height; a tube with the
  white lock icon is locked (skipped); the small add-tube booster tube has its own capacity;
- a standard tube: liquid fills from bbox top + 0.136 h (full) to bbox bottom - 0.015 h; 4 layers of equal
  height (75 model px). Each layer is sampled at its middle, right of the glass highlight: a dark sample is
  empty, a saturated one a colour; colours are grouped by RGB distance < 60;
- a cork can split a tube's outline into two components: intersecting tall components are merged (lab
  2026-10-06 (3), session 20261006-053412 frame 7);
- refused: a tube raised above its row (selected, or a pour animating), corks (a finished level animating),
  a colour count that is not a multiple of the capacity, a layer floating over an empty one.

Rules: pour moves the top run of one colour from a tube into an empty tube or onto the same top colour,
as much as fits. Win: every tube empty or full of one colour. Search: depth-first with memo over canonical
states (tube order ignored), pours that move a whole uniform tube into an empty one skipped.

Moves: taps [x, y] on tube centres, source then target, MAX_POURS pours per round; a pour whose source took part
in the previous pour is never next (its tap is lost): a later independent pour (no tube shared with any unplayed
pour before it) is moved forward instead, else the round ends (rescan after) (schedule(), lab 2026-10-06 (5));
done when the last pour of the solution is in the batch.
"""
import numpy as np

BG = np.array([30, 23, 65])
CAP = 4
FULL_TOP = 0.136       # liquid top of a full tube, fraction of the outline bbox height from its top
BOTTOM = 0.015         # liquid bottom above the bbox bottom
MAX_POURS = 8


def _no(note):
    return {"moves": [], "note": note, "rescan": False, "done": False}


def _components(mask):
    import cv2
    n, lab, stats, _ = cv2.connectedComponentsWithStats(mask.astype(np.uint8), connectivity=8)
    return [tuple(int(v) for v in stats[i][:4]) for i in range(1, n)], lab


def read_tubes(a):
    H, W, _ = a.shape
    mn, mx = a.min(2), a.max(2)
    glass = (mn > 150) & (mx - mn < 60) & (a[:, :, 2] >= a[:, :, 0] - 10)
    glass[:int(H * .15)] = False
    glass[int(H * .80):] = False
    comps, _ = _components(glass)
    # a cork (or confetti over the rim) can split one tube's outline in two: session 20261006-053412 frame 7
    # read the corked red tube as a full tube plus a phantom 1-layer tube (5 reds). Tall pieces whose boxes
    # intersect are one tube.
    big = [list(c) for c in comps if c[3] >= H * .05]
    merged = True
    while merged:
        merged = False
        for i in range(len(big)):
            for j in range(i + 1, len(big)):
                x1, y1, w1, h1 = big[i]
                x2, y2, w2, h2 = big[j]
                if x1 < x2 + w2 and x2 < x1 + w1 and y1 < y2 + h2 and y2 < y1 + h1:
                    nx, ny = min(x1, x2), min(y1, y2)
                    big[i] = [nx, ny, max(x1 + w1, x2 + w2) - nx, max(y1 + h1, y2 + h2) - ny]
                    del big[j]
                    merged = True
                    break
            if merged:
                break
    comps = [tuple(c) for c in big]
    tubes = []
    for x, y, w, h in comps:
        if h < H * .05 or w < W * .08 or w > W * .25 or h < w:
            continue
        tubes.append({"x": x, "y": y, "w": w, "h": h})
    if not tubes:
        return "no tubes"
    tall = max(t["h"] for t in tubes)
    out = []
    for t in tubes:
        x, y, w, h = t["x"], t["y"], t["w"], t["h"]
        inner = a[y + int(h * .2):y + int(h * .9), x + int(w * .3):x + int(w * .7)]
        white = (inner.min(2) > 230).mean()
        cap_h = tall * (1 - FULL_TOP - BOTTOM) / CAP
        if white > 0.04 and h < tall * .8:
            continue  # locked booster tube (lock icon)
        bot = y + h - h * BOTTOM
        top = y + tall * FULL_TOP if h > tall * .8 else y + h * FULL_TOP * tall / h
        cap = max(1, int(round((bot - top) / cap_h)))
        unit = (bot - top) / cap
        layers = []
        for k in range(cap):  # from the bottom
            cy = bot - (k + .5) * unit
            p = a[int(cy - unit * .2):int(cy + unit * .2), x + int(w * .45):x + int(w * .75)].reshape(-1, 3)
            m = p.mean(0)
            if np.abs(m - BG).sum() < 60:
                layers.append(None)
            elif m.max() - m.min() > 80 and p.std(0).max() < 40:
                layers.append(m)
            else:
                return f"tube at x{x + w // 2}: layer {k + 1} is neither empty nor one colour ({m.astype(int).tolist()})"
        out.append({"cx": x + w / 2, "cy": y + h / 2, "top": y, "h": h, "w": w, "cap": cap, "layers": layers})
    return out


def label(tubes):
    cols, names = [], []
    seq = []
    for t in tubes:
        row = []
        for m in t["layers"]:
            if m is None:
                break
            for i, c in enumerate(cols):
                if np.abs(m - c).sum() < 60:
                    row.append(i)
                    break
            else:
                cols.append(m)
                row.append(len(cols) - 1)
        if len(row) < sum(m is not None for m in t["layers"]):
            return f"a layer floats over an empty one in the tube at x{int(t['cx'])}"
        seq.append(tuple(row))
    return seq, cols


def solved(st, caps):
    return all(not t or (len(t) == c and len(set(t)) == 1) for t, c in zip(st, caps))


def moves_from(st, caps):
    out = []
    for i, s in enumerate(st):
        if not s:
            continue
        col = s[-1]
        run = 1
        while run < len(s) and s[-1 - run] == col:
            run += 1
        if run == len(s) and len(s) == caps[i]:
            continue  # finished tube
        for j, d in enumerate(st):
            if i == j or len(d) >= caps[j]:
                continue
            if d and d[-1] != col:
                continue
            if not d and run == len(s):
                continue  # moving a uniform tube into an empty one gains nothing
            n = min(run, caps[j] - len(d))
            out.append((i, j, n))
    return out


def bfs(start, caps, limit=150000):
    """Fewest pours (each pour is a tap pair and an animation): breadth-first over canonical states."""
    from collections import deque

    def key(st):
        return tuple(sorted(zip(st, caps)))

    start = tuple(start)
    prev = {key(start): None}
    q = deque([(start, [])])
    while q:
        st, path = q.popleft()
        if solved(st, caps):
            return path
        for i, j, n in moves_from(st, caps):
            nst = list(st)
            nst[j] = st[j] + st[i][-n:]
            nst[i] = st[i][:-n]
            nst = tuple(nst)
            k = key(nst)
            if k in prev:
                continue
            prev[k] = 1
            if len(prev) > limit:
                return None
            q.append((nst, path + [(i, j)]))
    return None


def search(start, caps, limit=200000):
    p = bfs(start, caps)
    if p is not None:
        return p
    return dfs(start, caps, limit)


def dfs(start, caps, limit=200000):
    seen = set()
    path = []

    def key(st):
        return tuple(sorted(zip(st, caps)))

    def rec(st):
        if solved(st, caps):
            return True
        k = key(st)
        if k in seen or len(seen) > limit:
            return False
        seen.add(k)
        # prefer pours that complete a tube or land on the same colour
        ms = moves_from(st, caps)
        ms.sort(key=lambda m: (-(len(st[m[1]]) + m[2] == caps[m[1]] and len(set(st[m[1]] + (st[m[0]][-1],))) == 1),
                               not st[m[1]]))
        for i, j, n in ms:
            nst = list(st)
            nst[j] = st[j] + st[i][-n:]
            nst[i] = st[i][:-n]
            path.append((i, j))
            if rec(tuple(nst)):
                return True
            path.pop()
        return False

    return path if rec(tuple(start)) else None


def schedule(path):
    """The pours of one round: (batch, rest). A pour only touches its two tubes, so two pours on four different
    tubes commute exactly; a later pour may be played early when it shares no tube with any unplayed pour
    before it. The batch takes, in order, the first such ready pour whose source is not a tube of the pour
    just before (that tube is still moving and loses the tap, session -231555 step 32), up to MAX_POURS. Two
    pours into one tube in a row land (session -084209 step 10: 1>2 4>2, tube 2 read AAAA after).
    Lab 2026-10-06 (5): the plain cut of the BFS order played 1-2 pours a round (L5 of session -084209: 10
    rounds for 14 pours); the same rule with independent pours moved forward needs fewer rounds."""
    rest = list(path)
    batch = [rest.pop(0)]
    while rest and len(batch) < MAX_POURS:
        busy = set()
        pick = None
        for k, (i, j) in enumerate(rest):
            if i not in busy and j not in busy and i not in batch[-1]:
                pick = k
                break
            busy |= {i, j}
        if pick is None:
            break
        batch.append(rest.pop(pick))
    return batch, rest


def solve(image, board=None, frame_scale=1.0):
    a = np.asarray(image.convert("RGB")).astype(int)
    H, W, _ = a.shape
    if np.abs(a[int(H * .02):int(H * .06), :int(W * .1)].reshape(-1, 3).mean(0) - BG).sum() > 40:
        return _no("not the Water Sort page (the corner is not its dark violet): popup, ad or another screen")
    tubes = read_tubes(a)
    if isinstance(tubes, str):
        return _no(f"not a water sort board: {tubes}")
    if len(tubes) < 3:
        return _no(f"only {len(tubes)} tube(s) read")
    # tubes of a row share their top: a raised tube is selected (or pouring). One raised tube = the selection
    # (session -231555 frame 53): tap it first to put it down, then play (untested: check the first pour)
    ws = sorted(t["w"] for t in tubes)
    if ws[-1] > ws[len(ws) // 2] * 1.3:
        return _no("a tube is tilted (pouring): wait and look again")
    rows, raised = [], []
    for t in sorted(tubes, key=lambda t: t["cy"]):
        if rows and t["cy"] - rows[-1][-1]["cy"] < H * .1:
            rows[-1].append(t)
        else:
            rows.append([t])
    tubes[:] = [t for r in rows for t in sorted(r, key=lambda t: t["cx"])]  # reading order, as the note numbers them
    for r in rows:
        full = [t for t in r if t["cap"] == CAP]
        if len(full) > 1:
            low = max(t["top"] for t in full)
            raised += [t for t in full if low - t["top"] > H * .008]
    if len(raised) > 1:
        return _no(f"{len(raised)} tubes raised (pouring): wait and look again")
    # the add-tube booster tube is small and its capacity is a guess: planned only when nothing else works
    small = [i for i, t in enumerate(tubes) if t["cap"] < CAP]
    lab = label(tubes)
    if isinstance(lab, str):
        return _no(lab)
    seq, cols = lab
    caps = [t["cap"] for t in tubes]
    counts = [sum(s.count(i) for s in seq) for i in range(len(cols))]
    if any(c % CAP for c in counts):
        return _no(f"colour counts {counts} are not multiples of {CAP}: misread (or a hidden layer)")
    txt = " | ".join("".join(chr(65 + c) for c in s) or "-" for s in seq)
    if solved(seq, caps):
        return {"moves": [], "note": f"solved already: {txt}", "rescan": False, "done": True}
    big = [i for i in range(len(tubes)) if i not in small]
    path = search([seq[i] for i in big], [caps[i] for i in big])
    if path is not None:
        path = [(big[i], big[j]) for i, j in path]
    elif small:
        path = search(seq, caps)
    if path is None:
        return _no(f"no solution found for {txt} (add a tube with the booster, or undo)")
    # a tube still busy with the previous pour does not take a tap: session -231555 step 32 sent 1>4 2>1 3>2 3>4
    # with 0.35 s between taps and the tap on tube 3 (the source of the pour before) was lost, so the tap on
    # tube 4 only selected it. schedule() never plays such a pour next: a later pour that shares no tube with any
    # unplayed pour before it is played in its place, and the batch ends only when none is ready (lab 2026-10-06 (5)).
    batch, rest = schedule(path)
    path = batch + rest  # the same pours, independent ones moved forward: the note shows the order played
    moves = [[round(raised[0]["cx"]), round(raised[0]["cy"])]] if raised else []
    for i, j in batch:
        moves.append([round(tubes[i]["cx"]), round(tubes[i]["cy"])])
        moves.append([round(tubes[j]["cx"]), round(tubes[j]["cy"])])
    last = len(batch) == len(path)
    note = (f"tubes (bottom->top) {txt}; caps {caps}; solution {len(path)} pours: "
            + " ".join(f"{i + 1}>{j + 1}" for i, j in path) + ("" if last else f"; playing the first {len(batch)}"))
    if raised:
        note = f"tube at x{int(raised[0]['cx'])} is raised (selected): tapped first to put it down. " + note
    return {"moves": moves, "note": note, "rescan": not last, "done": last}
