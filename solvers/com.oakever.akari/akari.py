"""Akari (Light Up) solver for MeowTrail.

Board is passed as JSON (--board FILE): {"rows": ["..3..", ...], "x": [col centers], "y": [row centers],
"count": the number of cats from the level counter "0/N" (optional), "frame_scale": optional factor from
frame pixels to device pixels}.
Cells: '.' empty, '#' plain wall, '0'-'4' numbered wall, 'C' cat already placed.
Moves are the cells to double-tap, in device pixels (x,y are given in frame pixels and scaled).
Every cat is fully deduced (the puzzle is solved completely before returning), so there is nothing hidden.
"""


def _solve_grid(rows, count=None):
    g = [list(r) for r in rows]
    R, C = len(g), len(g[0])
    wall = lambda r, c: g[r][c] in "#01234"  # noqa: E731
    empties = [(r, c) for r in range(R) for c in range(C) if not wall(r, c)]
    # segments: which cells each cell sees (including itself)
    sees = {}
    for (r, c) in empties:
        s = {(r, c)}
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            rr, cc = r + dr, c + dc
            while 0 <= rr < R and 0 <= cc < C and not wall(rr, cc):
                s.add((rr, cc))
                rr += dr
                cc += dc
        sees[(r, c)] = s
    clues = []
    for r in range(R):
        for c in range(C):
            if g[r][c] in "01234":
                nb = [(r + dr, c + dc) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
                      if 0 <= r + dr < R and 0 <= c + dc < C and not wall(r + dr, c + dc)]
                clues.append((int(g[r][c]), nb))
    cats = {p for p in empties if g[p[0]][p[1]] == "C"}
    banned = set()

    def ok(cats, banned):
        for n, nb in clues:
            k = sum(p in cats for p in nb)
            free = sum(p not in cats and p not in banned and not any(q in cats for q in sees[p]) for p in nb)
            if k > n or k + free < n:
                return False
        lit = set()
        for p in cats:
            lit |= sees[p]
        for p in empties:
            if p in lit:
                continue
            if not any(q not in banned and not any(z in cats for z in sees[q]) for q in sees[p]):
                return False
        return True

    def rec(cats, banned):
        if not ok(cats, banned) or (count is not None and len(cats) > count):
            return None
        lit = set()
        for p in cats:
            lit |= sees[p]
        if len(lit) == len(empties) and all(sum(p in cats for p in nb) == n for n, nb in clues):
            return cats if count is None or len(cats) == count else None
        # choose: prefer a clue cell, else the dark cell with fewest candidates
        cands = None
        for n, nb in clues:
            k = sum(p in cats for p in nb)
            if k < n:
                free = [p for p in nb if p not in cats and p not in banned and not any(q in cats for q in sees[p])]
                if cands is None or len(free) < len(cands):
                    cands = free
        if cands is None:
            best = None
            for p in empties:
                if p in lit:
                    continue
                f = [q for q in sees[p] if q not in banned and not any(z in cats for z in sees[q])]
                if best is None or len(f) < len(best):
                    best = f
            cands = best
        if not cands:
            return None
        p = cands[0]
        res = rec(cats | {p}, banned)
        if res:
            return res
        return rec(cats, banned | {p})

    return rec(cats, banned)


def solve(image, board=None, frame_scale=1.0):
    if not board:
        return {"moves": [], "note": "no board given: pass --board FILE", "rescan": False, "done": False}
    rows = board["rows"]
    if len({len(r) for r in rows}) != 1 or len(board["x"]) != len(rows[0]) or len(board["y"]) != len(rows):
        return {"moves": [], "note": "board shape does not match x/y centers", "rescan": False, "done": False}
    bad = {ch for r in rows for ch in r} - set(".#01234C")
    if bad:
        return {"moves": [], "note": f"unknown cells {sorted(bad)}: use . # 0-4 C", "rescan": False, "done": False}
    res = _solve_grid(rows, board.get("count"))
    if not res:
        return {"moves": [], "note": "no solution: board misread?", "rescan": False, "done": False}
    k = board.get("frame_scale", frame_scale)
    new = sorted(p for p in res if rows[p[0]][p[1]] != "C")
    moves = [[round(board["x"][c] * k), round(board["y"][r] * k), 2] for r, c in new]
    return {"moves": moves, "note": f"{len(res)} cats total, {len(new)} to place (double tap each): {new}",
            "rescan": False, "done": True}
