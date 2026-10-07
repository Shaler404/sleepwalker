"""Pull the Pin (com.maroieqrwlk.unpin), mechanic pin-pull: the zone model.

Not physics: a level is a set of places (compartments) separated by pins. Pulling a pin lets the
content of a place pour where its first free exit leads, and things that end up in one place mix:

  bomb + balls      -> lost (the blast throws the balls out of the level)
  bomb + bomb       -> both vanish (fine)
  colour + grey     -> all of that colour (good)
  bomb -> out       -> good;      balls -> out -> lost
  grey or bomb -> cup -> lost;    colour -> its cup -> collected
  goal: every ball in the cup, painted

The player writes the level once as a board (JSON, pixels of the 730-px frame the model sees):

{"level": "level 11",
 "places": {
   "G":  {"has": ["grey"],   "exits": [{"to": "BOX", "via": ["E"]}, {"to": "BOX", "via": ["C"]}]},
   "BR": {"has": ["bomb"],   "exits": [{"to": "CH", "via": ["E"]}]},
   "P":  {"has": ["colour"], "exits": [{"to": "BR", "via": ["W"]}, {"to": "out", "via": ["P"]}]},
   "BOX": {"exits": [{"to": "CH", "via": ["F"]}]},
   "CH": {"has": ["bomb"],   "exits": [{"to": "cup", "via": ["B"]}]}},
 "pins": {"E": [570, 470], "W": [505, 385], "P": [612, 530], "C": [105, 505], "F": [105, 597],
          "B": [160, 812], "V": [420, 385]}}

- has: "colour" (or a colour name: "yellow", "blue" for levels with coloured cups), "grey", "bomb".
- exits: in order; the first exit whose pins ("via") are all pulled takes the whole pile. An exit with
  "via": [] is always free (a pile resting on a slope pin rolls on). "only": "balls" or "bombs" limits
  an exit to that kind (balls slip through a gap a bomb cannot). "to" is a place, "cup", "cup:<colour>",
  "out" (out of the level) or "?" (unknown: the solver never lets anything go there); a list of
  places splits the pile (it lands on both).
- pins: [x, y] of the ring, or {"at": [x, y], "joins": [["A", "B"]]} for a divider whose removal makes
  two places one, {"swipe": [x1, y1, x2, y2]} for a slider pin with a dotted track, "check": false for
  a pin whose ring is not a plain ring (skips the ring check).
- optional: "gap" (seconds between pulls, 5), "max_moves" (challenge and boss levels), "stage": "2/4"
  (multi-stage: look again after the stage), "scrolling": true (the camera moves after pulls: one pin at
  a time), "try": ["E", "W"] (simulate this order instead of searching), "frame_width" (730).
- scrolling levels taller than the screen (challenge): "scrolling": true with "height" (level pixels, the start
  view at 0), "views": {place: y} (where the camera rests while the colour is in that place), "together":
  [["T", "D1"]] (pins pulled in one round), "plan" (an order checked first); a pin may carry "tap": [x, y]
  (tap there, not on the ring centre, when the centre pulls a neighbour). Such boards in the library are placed
  in the level frame by frame by their rings (_match_scrolling).

Without a board the solver reads the frame itself, only for the grey stacks of levels 1-8 (_read_stack):
floor pins one under the other in one container over the cup. Anything else is refused with the reason.

The solver searches every pin order (shortest first) and returns the pulls in order as taps, with the
`sw.py taps` string in the note. It refuses boards it cannot model: unknown names, an exit that can
never be taken, flows that loop, no way to get every ball into a cup, pins not seen as rings on the frame.
"""

import json
import time
from collections import deque

import numpy as np

SINKS = ("cup", "out", "?")
MAX_STATES = 300000
TIME_BUDGET_S = 35  # sw.py stops a solver after 60 s


# --- reading the board -------------------------------------------------------------------------------
def _kind(token):
    t = str(token).strip().lower()
    if t in ("grey", "gray", "g", "greys", "grays"):
        return "grey"
    if t in ("bomb", "bombs", "b"):
        return "bomb"
    return t or "colour"


def _parse(board):
    errs, warns = [], []
    if not isinstance(board, dict):
        return None, ["the board must be a JSON object with places and pins"], warns
    places = board.get("places")
    pins = board.get("pins")
    if not isinstance(places, dict) or not places:
        errs.append("no places")
    if not isinstance(pins, dict) or not pins:
        errs.append("no pins")
    if errs:
        return None, errs, warns
    fw = float(board.get("frame_width") or 730)
    # a scrolling level (challenge) is written in level pixels from its top view down: "height" lets pins lie
    # below the first frame
    fh = max(fw * 2340 / 1080, float(board.get("height") or 0))
    cups = set()
    pin = {}
    for pid, spec in pins.items():
        p = {"id": pid, "joins": [], "check": True}
        if isinstance(spec, (list, tuple)):
            spec = {"at": spec}
        if not isinstance(spec, dict):
            errs.append(f"pin {pid}: give [x, y] or an object")
            continue
        if "swipe" in spec:
            s = spec["swipe"]
            if not (isinstance(s, (list, tuple)) and len(s) == 4):
                errs.append(f"pin {pid}: swipe needs [x1, y1, x2, y2]")
                continue
            p["swipe"] = [float(v) for v in s]
            p["at"] = p["swipe"][:2]
            p["check"] = False
        else:
            a = spec.get("at")
            if not (isinstance(a, (list, tuple)) and len(a) == 2):
                errs.append(f"pin {pid}: no ring position")
                continue
            p["at"] = [float(a[0]), float(a[1])]
            w = spec.get("with")
            if w is not None:
                if not (isinstance(w, (list, tuple)) and len(w) == 2):
                    errs.append(f"pin {pid}: with needs [x, y] (the second ring pulled together)")
                    continue
                p["with"] = [float(w[0]), float(w[1])]
            t = spec.get("tap")
            if t is not None:
                # where to tap when the ring centre would pull a neighbour (challenge 1 TD: a tap on its ring
                # centre pulled TV, whose rod runs 24 px beside it, and the greys fell out, 2026-10-06)
                if not (isinstance(t, (list, tuple)) and len(t) == 2):
                    errs.append(f"pin {pid}: tap needs [x, y]")
                    continue
                p["tap"] = [float(t[0]), float(t[1])]
        pts = [p["swipe"][:2], p["swipe"][2:]] if "swipe" in p else [p["at"]] + ([p["with"]] if "with" in p else [])
        for x, y in pts + ([p["tap"]] if "tap" in p else []):
            if not (0 < x < fw and 0 < y < fh):
                errs.append(f"pin {pid}: ({x:.0f},{y:.0f}) is outside the {fw:.0f}-px frame")
        if spec.get("check") is False:
            p["check"] = False
        p["gold"] = bool(spec.get("gold"))
        for pair in spec.get("joins") or []:
            if not (isinstance(pair, (list, tuple)) and len(pair) == 2):
                errs.append(f"pin {pid}: joins takes pairs of places")
                continue
            p["joins"].append([str(pair[0]), str(pair[1])])
        pin[pid] = p
    place = {}
    for name, spec in places.items():
        if name in SINKS or name.startswith("cup:"):
            errs.append(f"place {name}: that name is a sink")
            continue
        spec = spec or {}
        has = spec.get("has") or []
        if isinstance(has, str):
            has = [has]
        exits = []
        for i, e in enumerate(spec.get("exits") or []):
            to = e.get("to")
            to = [to] if isinstance(to, str) else list(to or [])
            via = e.get("via") or []
            via = [via] if isinstance(via, str) else list(via)
            only = e.get("only")
            if not to:
                errs.append(f"place {name}, exit {i + 1}: no 'to'")
            if only not in (None, "balls", "bombs"):
                errs.append(f"place {name}, exit {i + 1}: only must be balls or bombs")
            for v in via:
                if v not in pins:
                    errs.append(f"place {name}, exit {i + 1}: unknown pin {v}")
            for t in to:
                if t.startswith("cup:"):
                    cups.add(t[4:].strip().lower())
            exits.append({"to": to, "via": frozenset(via), "only": only})
        place[name] = {"has": [_kind(h) for h in has], "exits": exits}
    for name, p in place.items():
        for i, e in enumerate(p["exits"]):
            for t in e["to"]:
                if t not in place and t not in SINKS and not t.startswith("cup:"):
                    errs.append(f"place {name}, exit {i + 1}: unknown place {t}")
            for j, f in enumerate(p["exits"][:i]):
                scope_f, scope_e = f["only"], e["only"]
                if f["via"] <= e["via"] and (scope_f is None or scope_f == scope_e):
                    errs.append(f"place {name}: exit {i + 1} (to {'+'.join(e['to'])}) can never be taken, "
                                f"exit {j + 1} is free whenever it is; list the exit that needs more pins first")
    for pid, p in pin.items():
        for a, b in p["joins"]:
            for n in (a, b):
                if n not in place:
                    errs.append(f"pin {pid}: joins unknown place {n}")
    if len(pin) > 18:
        errs.append(f"{len(pin)} pins: too many for one board, write the part you can see and play it first")
    # positions too close to tap safely
    ids = list(pin)
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            (ax, ay), (bx, by) = pin[a]["at"], pin[b]["at"]
            if (ax - bx) ** 2 + (ay - by) ** 2 < 32 ** 2:
                warns.append(f"rings {a} and {b} are {((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5:.0f} px apart: "
                             f"tap the far side of each ring")
    coloured = bool(cups)
    for name, p in place.items():
        p["has"] = [h if h in ("grey", "bomb") or coloured else "colour" for h in p["has"]]
        for h in p["has"]:
            if coloured and h not in ("grey", "bomb") and h not in cups:
                errs.append(f"place {name}: colour {h} has no cup:{h}")
    if not any(h != "bomb" for p in place.values() for h in p["has"]):
        errs.append("no balls on the board")
    if not any(t == "cup" or t.startswith("cup:") for p in place.values() for e in p["exits"] for t in e["to"]):
        errs.append("no exit leads to the cup")
    model = {"place": place, "pin": pin, "order": list(place), "pins": ids, "coloured": coloured, "fw": fw,
             "gap": float(board.get("gap") or 5), "max_moves": board.get("max_moves"),
             "stage": board.get("stage"), "scrolling": bool(board.get("scrolling")), "try": board.get("try"),
             "level": board.get("level") or "", "reframe": [str(r) for r in board.get("reframe") or []]}
    for r in model["reframe"]:
        if r not in pin:
            errs.append(f"reframe: unknown pin {r}")
    # scrolling levels (challenge 1, 2026-10-06): "views": {place: y} = the top of the view (level pixels) when
    # the coloured pile rests in that place (the camera follows it); "together": [["T", "D1"]] = pins pulled in
    # one round, in that order (the second one leaves the view once the first pile falls); "plan": an order to
    # check first (not yet won on the phone)
    model["views"] = {}
    for pl, v in (board.get("views") or {}).items():
        if pl not in place:
            errs.append(f"views: unknown place {pl}")
            continue
        try:
            model["views"][pl] = float(v)
        except (TypeError, ValueError):
            errs.append(f"views: {pl} needs a number")
    model["together"] = []
    seen_t = set()
    for g in board.get("together") or []:
        g = [str(x) for x in (g or [])]
        if len(g) < 2 or any(x not in pin for x in g) or seen_t & set(g):
            errs.append(f"together: {g} needs two or more known pins, each in one group")
            continue
        seen_t |= set(g)
        model["together"].append(tuple(g))
    model["plan"] = [str(x) for x in board.get("plan") or []]
    for x in model["plan"]:
        if x not in pin:
            errs.append(f"plan: unknown pin {x}")
    # "waits": {"M": 10}: at least that many seconds between the previous pull and this one (a pile still
    # running over a steering pin, level 20). The solver itself sleeps the rest before it returns the pull.
    model["waits"] = {}
    for pid, w in (board.get("waits") or {}).items():
        if pid not in pin:
            errs.append(f"waits: unknown pin {pid}")
            continue
        try:
            model["waits"][pid] = max(0.0, min(30.0, float(w)))
        except (TypeError, ValueError):
            errs.append(f"waits: {pid} needs seconds")
    return model, errs, warns


# --- the rules -----------------------------------------------------------------------------------------
# a pile is (colours: frozenset, grey: bool, bombs: int)
EMPTY = (frozenset(), False, 0)


def _balls(p):
    return bool(p[0]) or p[1]


def _what(p):
    w = sorted(p[0]) + (["grey"] if p[1] else []) + ([f"{p[2]} bomb" + ("s" if p[2] > 1 else "")] if p[2] else [])
    return "+".join(w) or "nothing"


def _merge(a, b, where, events):
    cols, grey, bombs = a[0] | b[0], a[1] or b[1], a[2] + b[2]
    if bombs and (cols or grey):
        return None, f"bomb meets balls in {where}"
    if bombs >= 2:
        events.append(f"{bombs} bombs meet in {where} and vanish")
        bombs = 0
    if len(cols) > 1:
        return None, f"colours {', '.join(sorted(cols))} mix in {where}"
    if grey and cols:
        events.append(f"greys painted in {where}")
        grey = False
    return (cols, grey, bombs), None


def _initial(model):
    st = {}
    for name in model["order"]:
        has = model["place"][name]["has"]
        if has:
            cols = frozenset(h for h in has if h not in ("grey", "bomb"))
            pile = (cols, "grey" in has, sum(h == "bomb" for h in has))
            if pile[2] >= 2 or (pile[2] and _balls(pile)) or (pile[1] and pile[0]) or len(pile[0]) > 1:
                return None, f"place {name} holds things that would already have reacted: split it"
            st[name] = pile
    return st, None


class State:
    __slots__ = ("pulled", "parent", "piles", "done")

    def __init__(self, pulled, parent, piles, done):
        self.pulled, self.parent, self.piles, self.done = pulled, parent, piles, done

    def key(self):
        return self.pulled, tuple(sorted(self.piles.items(), key=lambda kv: kv[0]))


def _find(parent, n):
    while parent.get(n, n) != n:
        n = parent[n]
    return n


def _exits(model, parent, root):
    out = []
    for name in model["order"]:
        if _find(parent, name) == root:
            out.extend(model["place"][name]["exits"])
    return out


def _deliver(model, st, part, dest, events, bomb_seen):
    """part arrives at dest; returns a loss/unknown message or None"""
    if dest == "?":
        return "something goes where the board says '?' (unknown)"
    if dest == "out":
        if _balls(part):
            return "balls fall out of the level"
        return None
    if dest == "cup" or dest.startswith("cup:"):
        if part[2]:
            return f"a bomb reaches the {dest}"
        if part[1]:
            return f"grey balls reach the {dest}"
        if dest.startswith("cup:") and part[0] != frozenset([dest[4:].strip().lower()]):
            return f"{', '.join(sorted(part[0]))} balls reach the {dest}"
        st.done = st.done | part[0]
        return None
    root = _find(st.parent, dest)
    if _balls(part) and bomb_seen.get(root):
        return f"balls reach {root} in the same pull as a bomb"
    if part[2]:
        bomb_seen[root] = True
        if _balls(st.piles.get(root, EMPTY)):
            return f"bomb meets balls in {root}"
    new, loss = _merge(st.piles.get(root, EMPTY), part, root, events)
    if loss:
        return loss
    if new == EMPTY:
        st.piles.pop(root, None)
    else:
        st.piles[root] = new
    return None


def _settle(model, st, events, passed):
    bomb_seen = {r: True for r, p in st.piles.items() if p[2]}
    for _ in range(400):
        moved = False
        for root in sorted(st.piles):
            pile = st.piles.get(root)
            if not pile:
                continue
            for kind in ("balls", "bombs"):
                pile = st.piles.get(root)
                if not pile:
                    break
                part = (pile[0], pile[1], 0) if kind == "balls" else (frozenset(), False, pile[2])
                if part == EMPTY:
                    continue
                ex = None
                for e in _exits(model, st.parent, root):
                    if e["only"] not in (None, kind) or not e["via"] <= st.pulled:
                        continue
                    if all(t not in SINKS and not t.startswith("cup:") and _find(st.parent, t) == root
                           for t in e["to"]):
                        continue  # leads into itself after a join
                    ex = e
                    break
                if ex is None:
                    continue
                rest = (frozenset(), False, pile[2]) if kind == "balls" else (pile[0], pile[1], 0)
                if rest == EMPTY:
                    st.piles.pop(root, None)
                else:
                    st.piles[root] = rest
                passed.add(root)
                events.append(f"{_what(part)} {root}->{'+'.join(_find(st.parent, t) for t in ex['to'])}")
                for t in ex["to"]:
                    loss = _deliver(model, st, part, t, events, bomb_seen)
                    if loss:
                        return loss
                moved = True
        if not moved:
            return None
    return "LOOP"


def _pull(model, st, pid):
    ns = State(st.pulled | {pid}, dict(st.parent), dict(st.piles), st.done)
    events, passed = [], set()
    for a, b in model["pin"][pid]["joins"]:
        ra, rb = _find(ns.parent, a), _find(ns.parent, b)
        if ra == rb:
            continue
        keep, gone = (ra, rb) if model["order"].index(ra) < model["order"].index(rb) else (rb, ra)
        ns.parent[gone] = keep
        merged, loss = _merge(ns.piles.get(keep, EMPTY), ns.piles.get(gone, EMPTY), keep, events)
        ns.piles.pop(gone, None)
        if loss:
            return None, events, loss, passed
        if merged == EMPTY:
            ns.piles.pop(keep, None)
        else:
            ns.piles[keep] = merged
        events.append(f"{gone} joins {keep}")
    loss = _settle(model, ns, events, passed)
    return ns, events, loss, passed


def _balls_left(st):
    return sorted(r for r, p in st.piles.items() if _balls(p))


def _timing(model, prev_passed, pid):
    """a pull that changes where a place drains right after balls ran through that place"""
    for name in prev_passed:
        for e in model["place"].get(name, {}).get("exits", []):
            if pid in e["via"]:
                return True
    return False


# --- search --------------------------------------------------------------------------------------------
VIS_TOP, VIS_BOTTOM = 275, 1360  # a ring is tappable between the level header and the race bar (challenge)


def _steps(model):
    """what one round may pull: a 'together' group, or one pin outside the groups"""
    members = {p for g in model["together"] for p in g}
    return list(model["together"]) + [(p,) for p in model["pins"] if p not in members]


def _view(model, st):
    """the top of the view (level pixels) where the camera rests: on the coloured pile (scrolling boards)"""
    vs = [model["views"][r] for r, p in sorted(st.piles.items()) if p[0] and r in model["views"]]
    return vs[0] if vs else None


def _in_view(model, pid, view):
    p = model["pin"][pid]
    return all(VIS_TOP <= y - view <= VIS_BOTTOM for _x, y in [p["at"]] + ([p["tap"]] if "tap" in p else []))


def _step_ok(model, st, step):
    """(new state, events, loss) after the step, or (None, [], why) when a pin of it is out of the view"""
    v = _view(model, st) if model["views"] else None
    if v is not None and not all(_in_view(model, p, v) for p in step):
        return None, [], "out of the view"
    ns, evs, loss = st, [], None
    for p in step:
        ns, ev, loss, _ = _pull(model, ns, p)
        evs += ev
        if loss:
            break
    return ns, evs, loss


def _search(model, start):
    if model["views"] or model["together"]:
        return _search_steps(model, start)
    pins = model["pins"]
    limit = (model["max_moves"] - len(start.pulled)) if model["max_moves"] else len(pins)
    q = deque([(start, ())])
    seen = {start.key()}
    found, best_partial, depth_found = [], None, None
    n, t0 = 0, time.monotonic()
    while q:
        st, path = q.popleft()
        if time.monotonic() - t0 > TIME_BUDGET_S:
            if found:
                return found, best_partial, None
            return found, best_partial, f"no complete order within {TIME_BUDGET_S} s: split the board"
        if depth_found is not None and len(path) >= depth_found:
            continue
        if len(path) >= limit:
            continue
        for pid in pins:
            if pid in st.pulled:
                continue
            ns, _, loss, _ = _pull(model, st, pid)
            n += 1
            if n > MAX_STATES:
                return found, best_partial, "the search is too big: split the board"
            if loss == "LOOP":
                return [], None, f"flows loop after pulling {pid}: a place pours back into itself"
            if loss:
                continue
            np_ = path + (pid,)
            left = _balls_left(ns)
            if not left:
                if depth_found is None:
                    depth_found = len(np_)
                found.append(np_)
                if len(found) >= 400:
                    return found, best_partial, None
                continue
            score = (len(left), len(np_))
            if best_partial is None or score < best_partial[0]:
                best_partial = (score, np_, left)
            k = ns.key()
            if k in seen:
                continue
            seen.add(k)
            q.append((ns, np_))
    return found, best_partial, None


def _search_steps(model, start):
    """the search of a scrolling board: a round pulls a step (a pin or a 'together' group) whose rings are in
    the view the camera rests at, and the move limit counts from the pins already pulled"""
    steps = _steps(model)
    limit = (model["max_moves"] - len(start.pulled)) if model["max_moves"] else len(model["pins"])
    q = deque([(start, ())])
    seen = {start.key()}
    found, best_partial, depth_found = [], None, None
    n, t0 = 0, time.monotonic()
    while q:
        st, path = q.popleft()
        if time.monotonic() - t0 > TIME_BUDGET_S:
            return found, best_partial, (None if found else f"no complete order within {TIME_BUDGET_S} s: split the board")
        if depth_found is not None and len(path) >= depth_found:
            continue
        for step in steps:
            if any(p in st.pulled for p in step) or len(path) + len(step) > limit:
                continue
            ns, _, loss = _step_ok(model, st, step)
            n += 1
            if n > MAX_STATES:
                return found, best_partial, "the search is too big: split the board"
            if loss == "LOOP":
                return [], None, f"flows loop after pulling {' '.join(step)}: a place pours back into itself"
            if loss or ns is None:
                continue
            np_ = path + step
            left = _balls_left(ns)
            if not left:
                if depth_found is None:
                    depth_found = len(np_)
                found.append(np_)
                if len(found) >= 400:
                    return found, best_partial, None
                continue
            score = (len(left), len(np_))
            if best_partial is None or score < best_partial[0]:
                best_partial = (score, np_, left)
            k = ns.key()
            if k in seen:
                continue
            seen.add(k)
            q.append((ns, np_))
    return found, best_partial, None


def _split_steps(model, order):
    """the order cut into rounds: a 'together' group must come whole and in its order, or None"""
    groups = {g[0]: g for g in model["together"]}
    members = {p for g in model["together"] for p in g}
    out, i = [], 0
    while i < len(order):
        g = groups.get(order[i])
        if g:
            if tuple(order[i:i + len(g)]) != g:
                return None
            out.append(g)
            i += len(g)
        elif order[i] in members:
            return None
        else:
            out.append((order[i],))
            i += 1
    return out


def _replay(model, start, order):
    st, steps, prev = start, [], set()
    for pid in order:
        if pid not in model["pin"]:
            return st, steps, f"unknown pin {pid}"
        if pid in st.pulled:
            return st, steps, f"pin {pid} pulled twice"
        ns, events, loss, passed = _pull(model, st, pid)
        steps.append({"pin": pid, "events": events, "timing": _timing(model, prev, pid), "loss": loss})
        if loss:
            return st, steps, loss
        st, prev = ns, passed
    return st, steps, None


# --- the frame ------------------------------------------------------------------------------------------
def _ring_score(met, col, k, x, y, search=14):
    best, at = 0.0, None
    r1, r2, hole = 9, 19, 5
    h, w = met.shape
    for dy in range(-search, search + 1, 2):
        for dx in range(-search, search + 1, 2):
            cx, cy = (x + dx) * k, (y + dy) * k
            x0, x1 = int(cx - r2 * k) - 1, int(cx + r2 * k) + 2
            y0, y1 = int(cy - r2 * k) - 1, int(cy + r2 * k) + 2
            if x0 < 0 or y0 < 0 or x1 > w or y1 > h:
                continue
            yy, xx = np.mgrid[y0:y1, x0:x1]
            d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / k
            ann, hol = (d >= r1) & (d <= r2), d < hole
            m, hc = met[y0:y1, x0:x1], col[y0:y1, x0:x1][hol].mean()
            s = m[ann].mean() * hc
            # a ring half hidden behind a wall: one half all metal, the opposite half not
            halves = [m[ann & sel].mean() for sel in (yy < cy, yy > cy, xx < cx, xx > cx)]
            for i, j in ((0, 1), (1, 0), (2, 3), (3, 2)):
                if halves[i] > 0.8 and halves[j] < 0.35:
                    s = max(s, 0.8 * halves[i] * hc)
            if s > best:
                best, at = s, (x + dx, y + dy)
    return best, at


def _gold_score(gold, k, x, y, r=26):
    h, w = gold.shape
    cx, cy = x * k, y * k
    x0, x1, y0, y1 = max(0, int(cx - r * k)), min(w, int(cx + r * k)), max(0, int(cy - r * k)), min(h, int(cy + r * k))
    if x1 <= x0 or y1 <= y0:
        return 0.0
    return float(gold[y0:y1, x0:x1].mean())


def _find_gold(image, fw=730):
    """Golden star-wand pins (league golden pins, 241.5.1): a yellow five-point star where the ring would be,
    on a gold rod. The circle search never sees them (2026-10-04, level 12: round 1 matched the library with
    "ring B not found by the circle search but seen by the ring check", round 2 after A had two rings left plus
    the unseen star, matched nothing and gave up). A star: a solid gold core 30-62 px wide after an opening
    that removes the rod and single yellow balls, gold over >= 55 % of the disc r 28, a concave outline
    (solidity <= 0.85: balls, coins and ad icons are 0.87-0.99) and little gold around it (only the rod).
    Returns star centres in the 730-px frame; the library uses them only to explain a pin, never as a ring
    that must be explained (a yellow ball pile is not a level)."""
    try:
        import cv2
    except ImportError:
        return []
    im = image.convert("RGB")
    if im.size[0] != fw:
        im = im.resize((int(fw), max(1, round(im.size[1] * fw / im.size[0]))))
    a = np.asarray(im).astype(np.int16)
    R, G, B = a[..., 0], a[..., 1], a[..., 2]
    m = ((R > 200) & (G > 140) & (B < 190) & (R - B > 50)).astype(np.uint8)
    m[:RING_TOP] = 0
    m[BOARD_BOTTOM:] = 0
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
    core = cv2.morphologyEx(m, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17, 17)))
    n, _, st, cen = cv2.connectedComponentsWithStats(core, 8)
    H, W = m.shape
    out = []
    for i in range(1, n):
        _x, _y, w, h, area = st[i]
        if not (30 <= w <= 62 and 30 <= h <= 62 and 700 <= area <= 2400):
            continue
        cx, cy = int(round(cen[i][0])), int(round(cen[i][1]))
        x0, x1, y0, y1 = max(0, cx - 62), min(W, cx + 63), max(0, cy - 62), min(H, cy + 63)
        Y, X = np.mgrid[y0:y1, x0:x1]
        d = np.hypot(X - cx, Y - cy)
        sub = m[y0:y1, x0:x1] > 0
        if sub[d < 28].mean() < 0.55 or int((sub & (d >= 34) & (d <= 60)).sum()) > 800:
            continue
        disc = (sub & (d < 30)).astype(np.uint8)
        cs, _ = cv2.findContours(disc, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if not cs:
            continue
        c = max(cs, key=cv2.contourArea)
        solidity = cv2.contourArea(c) / max(1.0, cv2.contourArea(cv2.convexHull(c)))
        if solidity <= 0.85:
            out.append((cx, cy))
    return out


def _small(image, fw=730):
    """the frame at the model's width (730 px): grey level and chroma as float32"""
    im = image.convert("RGB")
    if im.size[0] != fw:
        im = im.resize((int(fw), max(1, round(im.size[1] * fw / im.size[0]))))
    a = np.asarray(im).astype(np.int16)
    return a.mean(2).astype(np.float32), (a.max(2) - a.min(2)).astype(np.float32)


def _ring_profile(g, ch, cx, cy, away=None):
    """A pin ring seen as concentric circles from its centre, whatever the background: a flat hole (the
    background), a dark circle, a light band, a dark circle. The older test (_ring_score) wants a coloured
    hole, so on the grey levels 1-8 (grey background) it saw no ring at all and refused every board
    (2026-10-03, levels 1-2: both played by hand). Returns the profile radii or None.
    away = (x, y) of a neighbour ring that overlaps this one: the profile is then taken only on the side
    away from it (the sector within AWAY_DEG degrees of the neighbour's direction is left out, the hole
    included: the neighbour's ring and rod cross it)."""
    h, w = g.shape
    cx, cy = int(round(cx)), int(round(cy))
    if cx < 26 or cy < 26 or cx > w - 27 or cy > h - 27:
        return None
    yy, xx = np.mgrid[cy - 25:cy + 26, cx - 25:cx + 26]
    dist = np.hypot(xx - cx, yy - cy)
    d = dist.astype(np.int32)
    G, C = g[cy - 25:cy + 26, cx - 25:cx + 26].ravel(), ch[cy - 25:cy + 26, cx - 25:cx + 26].ravel()
    d = d.ravel()
    sel = d < 25
    if away is not None:
        ax, ay = away[0] - cx, away[1] - cy
        n = max(1e-6, float(np.hypot(ax, ay)))
        cosang = ((xx - cx) * ax + (yy - cy) * ay) / (np.maximum(dist, 1e-6) * n)
        sel = sel & (cosang.ravel() < np.cos(np.radians(AWAY_DEG)))
    cnt = np.bincount(d[sel], minlength=25).astype(np.float64)
    m = np.bincount(d[sel], G[sel], minlength=25) / np.maximum(cnt, 1)
    sq = np.bincount(d[sel], G[sel].astype(np.float64) ** 2, minlength=25) / np.maximum(cnt, 1)
    s = np.sqrt(np.maximum(sq - m ** 2, 0))
    c = np.bincount(d[sel], C[sel], minlength=25) / np.maximum(cnt, 1)
    hole, hs = m[:6].mean(), s[1:6].max()
    i1 = int(np.argmin(m[7:14])) + 7
    b = int(np.argmax(m[i1 + 1:i1 + 6])) + i1 + 1
    o = int(np.argmin(m[b + 1:b + 7])) + b + 1
    ok = (hs < 14 and m[i1] < hole - 45 and m[b] > m[i1] + 45 and m[o] < m[b] - 45
          and c[i1] < 30 and c[o] < 35 and m[i1] < 175 and m[o] < 175)
    if ok:
        return (i1, b, o)
    # A dark background (the Space theme, Collections > Themes, 2026-10-04: L10 stage 4 refused with "no pin
    # ring on this frame"): the hole is darker than the ring, so the "dark circle" inside is missing. The
    # ring itself is the same on every theme: grey metal (100-150), a light band (175-250), grey metal, then
    # the background again. Its size differs between levels (the band at r 12-17), so the metal is found
    # around the band, and it must be the same all around (low spread at each radius): a white letter on a
    # dark Play Store sheet has a hump but no even metal circles.
    if hs < 25 and hole < 110:
        b = int(np.argmax(m[11:20])) + 11
        metal = [r for r in range(b - 6, min(b + 7, 25)) if r != b and 100 <= m[r] <= 150 and c[r] < 30
                 and m[r] >= hole + 45]
        inner, outer = [r for r in metal if r < b], [r for r in metal if r > b]
        ok = (len(inner) >= 2 and len(outer) >= 2 and len(metal) >= 5 and m[b] >= 175 and c[b] < 20
              and m[b] - max(m[r] for r in metal) >= 25 and float(np.mean([s[r] for r in metal])) < 25)
        if ok:
            return (inner[0], b, outer[-1])
    return None


def _profile_near(g, ch, x, y, search=10, away=None):
    best = None
    for dy in range(-search, search + 1):
        for dx in range(-search, search + 1):
            if _ring_profile(g, ch, x + dx, y + dy, away=away) is not None:
                dd = dx * dx + dy * dy
                if best is None or dd < best[0]:
                    best = (dd, (x + dx, y + dy))
    return best[1] if best else None


CLOSE_RINGS = 32  # rings closer than this overlap: the circle search sees neither (level 14 H/LR)
AWAY_DEG = 80  # half-angle of the sector toward the overlapping ring left out of its profile (60-100 all read L14)


def _close_pin(model, pid, x, y):
    """the centre of another pin's ring that overlaps this one (closer than CLOSE_RINGS), or None"""
    best = None
    for q, p in model["pin"].items():
        if q == pid or "at" not in p or "swipe" in p:
            continue
        for qx, qy in [p["at"]] + ([p["with"]] if "with" in p else []):
            d = ((qx - x) ** 2 + (qy - y) ** 2) ** 0.5
            if 4 < d < CLOSE_RINGS and (best is None or d < best[0]):
                best = (d, (qx, qy))
    return best[1] if best else None


HALF_DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0))  # the side a wall may hide: below, above, right, left


def _half_ring(g, ch, x, y, search=6):
    """A ring half hidden behind the container's white wall (level 17 on 241.5.2, 2026-10-05: the rings of the
    two top pins V1/V2 stand on the top wall, their lower half behind it; neither the circle search nor the
    full ring profile saw them and the level was played by hand): the ring profile on the visible side only
    (the sector toward the wall left out, as for overlapping rings). Returns the centre or None."""
    for dx, dy in HALF_DIRS:
        at = _profile_near(g, ch, int(round(x)), int(round(y)), search=search, away=(x + 30 * dx, y + 30 * dy))
        if at is not None:
            return at
    return None


def _check_rings(image, model, skip=()):
    a = np.asarray(image.convert("RGB")).astype(np.int16)
    k = a.shape[1] / model["fw"]
    mx, mn = a.max(2), a.min(2)
    ch = mx - mn
    gold = (a[..., 0] > 180) & (a[..., 1] > 120) & (a[..., 2] < 130) & (a[..., 0] - a[..., 2] > 70)
    met = ((ch < 28) & (mx >= 95) & (mx <= 245)) | gold
    col = (ch >= 28) & ~gold
    missing, off = [], []
    small = None
    for pid, x, y in [(pid, *pt) for pid, p in model["pin"].items() if p["check"] and pid not in skip
                      for pt in [p["at"]] + ([p["with"]] if "with" in p else [])]:
        if model["pin"][pid].get("gold") and _gold_score(gold, k, x, y) >= 0.12:
            continue  # a star, not a ring: the ring score finds a false centre on its rod (L12 B "~(242,624)")
        s, at = _ring_score(met, col, k, x, y)
        if s >= 0.55:
            if at and ((at[0] - x) ** 2 + (at[1] - y) ** 2) ** 0.5 > 9:
                off.append(f"{pid} ring centre ~({at[0]:.0f},{at[1]:.0f})")
            continue
        if _gold_score(gold, k, x, y) >= 0.12:
            continue
        if small is None:
            small = _small(image, model["fw"])
        at = _profile_near(small[0], small[1], int(round(x)), int(round(y)))
        if at is None:
            # two rings that overlap (level 14 H/LR on 241.5.2, 21 px apart, 2026-10-05: neither was seen and
            # the level was played by hand): read each on its side away from the other
            nb = _close_pin(model, pid, x, y)
            if nb is not None:
                at = _profile_near(small[0], small[1], int(round(x)), int(round(y)), search=6, away=nb)
        if at is None:
            at = _half_ring(small[0], small[1], x, y)
        if at is not None:
            if ((at[0] - x) ** 2 + (at[1] - y) ** 2) ** 0.5 > 9:
                off.append(f"{pid} ring centre ~({at[0]:.0f},{at[1]:.0f})")
            continue
        missing.append(f"{pid} ({x:.0f},{y:.0f})")
    return missing, off, k


# --- reading a simple level from the frame (no board) ----------------------------------------------------
# The grey levels of a fresh install (1-8, version 241.5.1) are stacks: one container, floor pins one under
# the other, every ring on the same side, the funnel under the lowest floor leads to the cup. Those the
# solver reads by itself; anything else (slanted or crossing pins, two columns, bombs, the purple theme of
# level 9 on, pipes) is refused with "write a board". (2026-10-03: levels 1 and 2 were placed by hand.)
BOARD_TOP, BOARD_BOTTOM = 300, 1400  # 730-px frame: under the level header and the ADS button, above banners
RING_TOP = 275  # top rings sit at y 298-311 (levels 3, 6, 5 stage 4): BOARD_TOP cut them off


def _find_rings(g, ch):
    try:
        import cv2
    except ImportError:
        return []
    cs = cv2.HoughCircles(np.clip(g, 0, 255).astype(np.uint8), cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                          param1=80, param2=18, minRadius=15, maxRadius=24)
    out = []
    for x, y, _r in ([] if cs is None else cs[0]):
        if not RING_TOP <= y <= BOARD_BOTTOM:
            continue
        at = _profile_near(g, ch, int(round(x)), int(round(y)), search=3)
        if at and all((at[0] - q[0]) ** 2 + (at[1] - q[1]) ** 2 > 144 for q in out):
            out.append(at)
    return out


def _rod(g, ch, rx, ry):
    """the floor rod from a ring, horizontal, toward the middle of the frame: (x_inner_end, length)"""
    step = -1 if rx > g.shape[1] / 2 else 1
    x, last, gap = rx + step * 22, None, 0
    rows = slice(ry + 1, ry + 8)
    while 0 <= x < g.shape[1]:
        col = (g[rows, x] < 175) & (ch[rows, x] < 25)
        if col.any():
            last, gap = x, 0
        elif (g[rows, x] > 245).all():
            gap = 0  # the rod runs behind the container's white wall
        else:
            gap += 1
            if gap > 6:
                break
        x += step
    if last is None:
        return None, 0
    return last, abs(last - rx) - 22


def _band(g, ch, x0, x1, y0, y1):
    G, C = g[y0:y1, x0:x1], ch[y0:y1, x0:x1]
    if G.size == 0:
        return {"col": 0.0, "grey": 0.0}
    return {"col": float((C > 60).mean()), "grey": float(((C < 25) & (G > 140) & (G < 195)).mean())}


def _bombs(g, ch):
    """dark blobs (a bomb is a black ball about 50 px wide) in the board area"""
    try:
        import cv2
    except ImportError:
        return []
    dark = ((g[BOARD_TOP:BOARD_BOTTOM] < 80) & (ch[BOARD_TOP:BOARD_BOTTOM] < 40)).astype(np.uint8)
    n, _, st, cen = cv2.connectedComponentsWithStats(dark, 8)
    # a bomb: 630-1240 px, a quarter of its box dark (the face breaks it); the tutorial hand's outline on
    # levels 1-2: about 530 px but only 12 % of its box
    return [(int(cen[i][0]), int(cen[i][1]) + BOARD_TOP) for i in range(1, n)
            if st[i][4] >= 500 and st[i][4] / float(st[i][2] * st[i][3]) >= 0.18]


def _read_stack(image):
    """(board, how it was read) or (None, why not)"""
    g, ch = _small(image)
    area = (slice(200, BOARD_BOTTOM), slice(0, g.shape[1]))
    if np.median(ch[area]) > 8 or not 190 <= np.median(g[area]) <= 232:
        return None, "not a grey-background level (the purple levels from 9 on need a board)"
    rings = _find_rings(g, ch)
    if not rings:
        return None, "no pin ring on this frame"
    if len(rings) > 6:
        return None, f"{len(rings)} rings: too many for a stack"
    bombs = _bombs(g, ch)
    if bombs:
        return None, f"a bomb (dark blob) at {', '.join(f'({x},{y})' for x, y in bombs[:3])}"
    rings.sort(key=lambda p: p[1])
    floors = []
    for rx, ry in rings:
        end, length = _rod(g, ch, rx, ry)
        if length < 150:
            return None, f"ring ({rx},{ry}) has no long horizontal floor rod (slanted, short or a divider)"
        floors.append((rx, ry, min(rx, end), max(rx, end)))
    sides = {rx > g.shape[1] / 2 for rx, *_ in floors}
    if len(sides) > 1 or max(f[0] for f in floors) - min(f[0] for f in floors) > 15:
        return None, "the rings are not one above the other on one side (not a single stack)"
    inner = [f[2] if f[0] > g.shape[1] / 2 else f[3] for f in floors]
    if max(inner) - min(inner) > 25:
        return None, "the floors do not span the same column (not a single stack)"
    if any(b[1] - a[1] < 60 for a, b in zip(floors, floors[1:])):
        return None, "two floors closer than 60 px"
    x0, x1 = min(inner) + 8, min(f[0] for f in floors) - 30
    if floors[0][0] < g.shape[1] / 2:
        x0, x1 = max(f[0] for f in floors) + 30, max(inner) - 8
    places, pins, seen = {}, {}, []
    tops = [floors[0][1] - 140] + [f[1] + 8 for f in floors[:-1]]
    for i, ((rx, ry, *_), y0) in enumerate(zip(floors, tops)):
        b = _band(g, ch, x0, x1, max(y0, BOARD_TOP - 60), ry - 6)
        has = ["colour"] if b["col"] > 0.03 else (["grey"] if b["grey"] > 0.10 else [])
        seen.append(f"Z{i + 1}={'+'.join(has) or 'empty'}")
        nxt = f"Z{i + 2}" if i + 1 < len(floors) else "cup"
        places[f"Z{i + 1}"] = {"has": has, "exits": [{"to": nxt, "via": [f"P{i + 1}"]}]}
        pins[f"P{i + 1}"] = [rx, ry]
    below = _band(g, ch, x0, x1, floors[-1][1] + 10, floors[-1][1] + 200)
    if below["col"] > 0.01 or below["grey"] > 0.03:
        return None, "balls under the lowest floor (not a single stack)"
    if not any(p["has"] for p in places.values()):
        return None, "no balls seen on the floors"
    board = {"level": "", "places": places, "pins": pins}
    how = (f"read from the frame: a stack of {len(floors)} floor pin(s) "
           f"{' '.join(f'P{i + 1}({rx},{ry})' for i, (rx, ry, *_) in enumerate(floors))}, top to bottom "
           f"{' '.join(seen)}, the lowest over the cup")
    return board, how


# --- the entry point -----------------------------------------------------------------------------------
def _taps(model, order):
    out = []
    for pid in order:
        p = model["pin"][pid]
        if "swipe" in p:
            s = p["swipe"]
            out.append(f"{s[0]:.0f},{s[1]:.0f}>{s[2]:.0f},{s[3]:.0f}")
        else:
            at = p.get("tap") or p["at"]
            out.append(f"{at[0]:.0f},{at[1]:.0f}")
            if "with" in p:
                out.append(f"{p['with'][0]:.0f},{p['with'][1]:.0f}")
    return " ".join(out)


def _moves(model, order, k):
    mv = []
    for pid in order:
        p = model["pin"][pid]
        if "swipe" in p:
            mv.append([round(v * k) for v in p["swipe"]])
        else:
            at = p.get("tap") or p["at"]
            mv.append([round(at[0] * k), round(at[1] * k)])
            if "with" in p:
                mv.append([round(p["with"][0] * k), round(p["with"][1] * k)])
    return mv


def _describe(steps):
    parts = []
    for s in steps:
        ev = "; ".join(s["events"]) or "nothing moves"
        parts.append(f"{s['pin']}: {ev}" + (" (wait for the channel to empty first)" if s["timing"] else ""))
    return " | ".join(parts)


# --- the level library: boards the solver recognises on the frame by their rings -------------------------
# A fresh install replays the same levels, and the player used to type each board or tap a stored order by
# hand (2026-10-03, session 203702: levels 3-8 placed by hand, level 9 tapped from the playbook's library).
# The solver finds the rings itself (Hough circles + the ring profile), and a library board whose rings are
# exactly those (each within RING_TOL px, no ring left over; the background colour does not
# matter: level 9 was purple on 2026-10-01 and grey on 2026-10-03) is the board of this
# frame. A ring hidden by the tutorial hand may be missing if the ring check still sees it there. After pulls
# in an earlier round of the same level (the solver's memory), the pins it sent whose rings are gone count as
# pulled. LIBRARY_JSON below is generated from the local boards (state/<game>/solvers/boards/*.json).
RING_TOL = 16


def _lib_points(board):
    pts = []
    for pid, spec in board["pins"].items():
        spec = {"at": spec} if isinstance(spec, (list, tuple)) else spec
        if "swipe" in spec or spec.get("check") is False:
            continue
        pts.append((pid, spec["at"]))
        if spec.get("with"):
            pts.append((pid, spec["with"]))
    return pts


def _match_library(image, state):
    """(name, board, pulled, how) or (None, None, None, why not)"""
    g, ch = _small(image)
    rings = _find_rings(g, ch)
    stars = _find_gold(image)
    mem = state if isinstance(state, dict) else {}
    if not rings and not stars:
        kept = _match_remembered(image, rings, mem)
        if kept:
            return kept
        return None, None, None, "no pin ring on this frame"
    cands = list(rings) + list(stars)  # every ring must be a pin of the board; a star may be one
    found = []
    for name, b in LIBRARY.items():
        pts = _lib_points(b)
        used, missing = set(), []
        for pid, (x, y) in pts:
            best = None
            for j, (rx, ry) in enumerate(cands):
                d = ((rx - x) ** 2 + (ry - y) ** 2) ** 0.5
                if j not in used and d <= RING_TOL and (best is None or d < best[0]):
                    best = (d, j)
            if best:
                used.add(best[1])
            else:
                missing.append(pid)
        if not used or any(j not in used for j in range(len(rings))):
            continue
        missing = list(dict.fromkeys(missing))
        if not missing:
            why = "every ring seen" + (" (a golden star pin among them)" if used - set(range(len(rings))) else "")
            shift = _ring_shift(pts, cands, len(rings))
            if shift:
                b = _scaled_board(b, 1.0, *shift)
                why += f"; the view moved {shift[0]:+.0f},{shift[1]:+.0f} px: every pin shifted with it"
            found.append((0, name, (), why, b))
            continue
        sent = (mem.get("sent") or []) if mem.get("entry") == name else []
        pulled = tuple(p for p in sent if p in missing)
        rest = [p for p in missing if p not in pulled]
        # the view moved (level 16 after I2): the pins still to find are looked for where the rings went
        shift = _ring_shift([pt for pt in pts if pt[0] not in pulled], cands, len(rings))
        if shift:
            b = _scaled_board(b, 1.0, *shift)
        model, errs, _ = _parse(b)
        if errs:
            continue
        # a pin the circle search missed (a ring under the tutorial hand, a star the star test missed) still
        # counts when the ring check sees it; at most one such pin, so a half-seen board is not taken. Rings
        # that overlap another pin's ring (closer than CLOSE_RINGS) do not count in that one: the circle search
        # never sees them (level 14 H/LR, 2026-10-05), the ring check reads them on their free side
        lone = [p for p in rest if _close_pin(model, p, *model["pin"][p]["at"]) is None]
        # a ring half hidden behind a wall (level 17 V1/V2 on the top wall) is never seen by the circle search
        # either: it does not count as lone when its visible half reads as a ring at the library position
        half = [p for p in lone if not model["pin"][p].get("gold") and "with" not in model["pin"][p]
                and _half_ring(g, ch, *model["pin"][p]["at"]) is not None]
        lone = [p for p in lone if p not in half]
        if len(lone) > 1 or len(rest) > 3 or (rest and len(model["pin"]) < 2) or len(rest) >= len(model["pin"]) - 1:
            continue
        if rest:
            hidden, _, _ = _check_rings(image, model, skip=[p for p in model["pin"] if p not in rest])
            if hidden:
                continue
        why = []
        if pulled:
            why.append(f"pins {' '.join(pulled)} pulled in an earlier round")
        if rest:
            kinds = [k for k, on in (("overlapping rings", len(rest) > len(lone) + len(half)),
                                     (f"{' '.join(half)} half hidden behind a wall", bool(half))) if on]
            why.append(f"ring{'s' if len(rest) > 1 else ''} {' '.join(rest)} not found by the circle search but "
                       f"seen by the ring check{' (' + '; '.join(kinds) + ')' if kinds else ''}")
        if shift:
            why.append(f"the view moved {shift[0]:+.0f},{shift[1]:+.0f} px: every pin shifted with it")
        found.append((2 if pulled else 1, name, pulled, "; ".join(why), b))
    if not found:
        moved = (_match_reframed(rings, mem) or (stars and _match_reframed(list(rings) + list(stars), mem))
                 or _match_reframed_part(image, rings, mem))
        if moved:
            return moved
        kept = _match_remembered(image, rings, mem)
        if kept:
            return kept
        return None, None, None, (f"{len(rings)} ring(s) at {' '.join(f'({x},{y})' for x, y in rings[:8])}"
                                  + (f" and {len(stars)} golden star(s) at {' '.join(f'({x},{y})' for x, y in stars[:4])}"
                                     if stars else "") + " on a frame match no level in the library")
    found.sort(key=lambda f: (f[0], f[1]))
    top = [f for f in found if f[0] == found[0][0]]
    if len(top) > 1:
        return None, None, None, f"the rings fit several library boards ({', '.join(f[1] for f in top)})"
    _, name, pulled, why, b = top[0]
    return name, b, pulled, f"library board {name} recognised ({why})"


SHIFT_MIN = 5  # px: a smaller common offset is the hand-read board's own error


def _ring_shift(pts, cands, nrings):
    """The common offset of the rings found from their library positions when the game moved the view (level
    16 on 241.5.2, 2026-10-05: after I1 and I2 every ring and the cup sat ~15 px higher; the match within
    RING_TOL still named L16, then the ring check (9 px) refused RP and F and the rest was tapped by hand).
    Only rings count (a star centre is read less exactly), all agreeing within 5 px of the median; one ring
    alone moves the board too (the last pin of L17 after the view moved: the tap goes on the ring found, not
    15 px beside it). Returns (dx, dy) or None when the board sits where the library says."""
    pairs, used = [], set()
    for _pid, (x, y) in pts:
        best = None
        for j, (rx, ry) in enumerate(cands[:nrings]):
            d = ((rx - x) ** 2 + (ry - y) ** 2) ** 0.5
            if j not in used and d <= RING_TOL and (best is None or d < best[0]):
                best = (d, j)
        if best:
            used.add(best[1])
            rx, ry = cands[best[1]]
            pairs.append((rx - x, ry - y))
    if not pairs:
        return None
    dx, dy = float(np.median([p[0] for p in pairs])), float(np.median([p[1] for p in pairs]))
    if (dx * dx + dy * dy) ** 0.5 < SHIFT_MIN:
        return None
    if any(((px - dx) ** 2 + (py - dy) ** 2) ** 0.5 > 5 for px, py in pairs):
        return None
    return round(dx), round(dy)


def _scaled_board(board, sc, tx, ty):
    """the board with every pin position zoomed by sc and moved by (tx, ty)"""
    f = lambda x, y: [round(x * sc + tx, 1), round(y * sc + ty, 1)]  # noqa: E731
    out = json.loads(json.dumps(board))
    for pid, spec in out["pins"].items():
        if isinstance(spec, (list, tuple)):
            out["pins"][pid] = f(*spec)
            continue
        if "at" in spec:
            spec["at"] = f(*spec["at"])
        if spec.get("with"):
            spec["with"] = f(*spec["with"])
        if "swipe" in spec:
            spec["swipe"] = f(*spec["swipe"][:2]) + f(*spec["swipe"][2:])
    return out


def _match_reframed_part(image, rings, mem):
    """The view moved and some pins still expected are not found by the circle search (level 17 on 241.5.2,
    2026-10-05: after V1 DR H the bombs met, the view moved ~11 px right and up, and V2's ring sat further
    behind the top wall): one zoom and shift must put every ring found within 8 px of a distinct pin still
    expected (at least two rings, at most two pins left unmatched), and the unmatched pins must then pass the
    ring check (half rings included) where the transform puts them."""
    name, sent = mem.get("entry"), mem.get("sent") or []
    if name not in LIBRARY or not sent or len(rings) < 2:
        return None
    pts = [(pid, xy) for pid, xy in _lib_points(LIBRARY[name]) if pid not in sent]
    if not 0 < len(pts) - len(rings) <= 2:
        return None
    cands = []
    for sc in np.arange(0.92, 1.12, 0.005):
        rx, ry = rings[0]
        for _, (x, y) in pts:
            tx, ty = rx - sc * x, ry - sc * y
            err, used = 0.0, set()
            for qx, qy in rings:
                d, i = min((((qx - (sc * px + tx)) ** 2 + (qy - (sc * py + ty)) ** 2) ** 0.5, i)
                           for i, (_, (px, py)) in enumerate(pts) if i not in used)
                if d > 8:
                    break
                used.add(i)
                err = max(err, d)
            else:
                cands.append((err + 50 * abs(float(sc) - 1), float(sc), tx, ty, frozenset(used)))
    # two rings close together fix the zoom poorly (L17 DL/F: 1.00-1.05 fit within 3 px, and 1.02 puts V2
    # 17 px off): the zoom nearest 1 that fits wins, and the next ones are tried while the check fails
    cands.sort(key=lambda c: c[0])
    tried = set()
    for _, sc, tx, ty, used in cands:
        key = (round(sc, 2), round(tx / 3), round(ty / 3), used)
        if key in tried:
            continue
        tried.add(key)
        if len(tried) > 6:
            break
        extra = [pid for i, (pid, _) in enumerate(pts) if i not in used]
        b = _scaled_board(LIBRARY[name], sc, tx, ty)
        model, errs, _ = _parse(b)
        if errs:
            return None
        hidden, _, _ = _check_rings(image, model, skip=[p for p in model["pin"] if p not in extra])
        if hidden:
            continue
        pulled = tuple(sent)
        return (name, b, pulled,
                f"library board {name} recognised after the view moved (zoom {sc:.3f}, shift {tx:+.0f},{ty:+.0f}; "
                f"pins {' '.join(pulled)} pulled in an earlier round; ring{'s' if len(extra) > 1 else ''} "
                f"{' '.join(extra)} seen by the ring check where the view put {'them' if len(extra) > 1 else 'it'})")
    return None


def _match_reframed(rings, mem):
    """The level of the last round when the game zoomed or moved the view after a pull (level 11: after the two
    bombs meet the container grows and every ring moves 6-18 px, 2026-10-04 video of session 005453): one
    zoom and shift must put every ring still expected within 8 px of a ring found, with no ring left over."""
    name, sent = mem.get("entry"), mem.get("sent") or []
    if name not in LIBRARY or not sent or not rings:
        return None
    pts = [(pid, xy) for pid, xy in _lib_points(LIBRARY[name]) if pid not in sent]
    if not pts or len(pts) != len(rings):
        return None
    best = None
    for sc in np.arange(0.92, 1.12, 0.005):
        for _, (x, y) in pts[:2]:
            for rx, ry in rings:
                tx, ty = rx - sc * x, ry - sc * y
                err, used = 0.0, set()
                for _, (px, py) in pts:
                    d, j = min((((qx - (sc * px + tx)) ** 2 + (qy - (sc * py + ty)) ** 2) ** 0.5, j)
                               for j, (qx, qy) in enumerate(rings))
                    if d > 8 or j in used:
                        break
                    used.add(j)
                    err = max(err, d)
                else:
                    if best is None or err < best[0]:
                        best = (err, float(sc), tx, ty)
    if best is None:
        return None
    _, sc, tx, ty = best
    pulled = tuple(sent)
    return (name, _scaled_board(LIBRARY[name], sc, tx, ty), pulled,
            f"library board {name} recognised after the view moved (zoom {sc:.3f}, shift {tx:+.0f},{ty:+.0f}; "
            f"pins {' '.join(pulled)} pulled in an earlier round)")


def _slider_seen(g, ch, swipe):
    """A slider pin still in place: a dark knob near the swipe start and a dotted track (light grey dots ~16 px
    apart on the white wall) running in the swipe direction. Level 19 on 2026-10-05 (235042 shot 40): after
    T only the hook K was left, a pin with no ring, and the run stopped with 'no pin ring on this frame'; the
    swipe was sent by hand. Knob at ~(153,821) g~100, dots g~170 on the 210 wall from x 165 to 285."""
    x1, y1, x2, y2 = swipe
    h, w = g.shape
    d = np.array([x2 - x1, y2 - y1], float)
    d /= max(1e-6, np.hypot(*d))
    win = g[max(0, int(y1) - 10):min(h, int(y1) + 50), max(0, int(x1) - 25):min(w, int(x1) + 25)]
    wch = ch[max(0, int(y1) - 10):min(h, int(y1) + 50), max(0, int(x1) - 25):min(w, int(x1) + 25)]
    if not win.size or not ((win < 130) & (wch < 30)).sum() >= 12:
        return False
    best = 0
    for off in range(0, 46, 2):  # the track runs along the swipe, a little below its start (the hook's loop)
        for slope in (-0.1, 0.0, 0.1):
            vals = []
            for t in range(8, 150):
                x = x1 + d[0] * t
                y = y1 + off + (d[1] + slope) * t
                if not (0 <= int(x) < w and 0 <= int(y) < h):
                    break
                vals.append(float(g[int(y) - 1:int(y) + 2, int(x)].min()))
            v = np.array(vals)
            if len(v) < 60:
                continue
            dots = [i for i in range(2, len(v) - 2) if 140 <= v[i] <= 195 and v[i] == v[i - 2:i + 3].min()
                    and v[i - 2:i + 3].max() >= 198]
            # dots evenly spaced (10-24 px) on a white wall
            gaps = np.diff(dots)
            n = int(((gaps >= 10) & (gaps <= 24)).sum()) if len(dots) > 1 else 0
            best = max(best, n)
    return best >= 4


def _match_remembered(image, rings, mem):
    """The level of the last round, when the frame fits no library board by its rings alone (a pin the circle
    search does not see, a pin that answered late): every pin not yet sent must pass the ring check on this
    frame and every ring found must be one of those pins. The memory then carries the level to its end
    instead of giving up after a partial run (2026-10-04, level 12 after A)."""
    name, sent = mem.get("entry"), list(mem.get("sent") or [])
    if name not in LIBRARY or not sent:
        return None
    b = LIBRARY[name]
    model, errs, _ = _parse(b)
    if errs:
        return None
    left = [p for p in model["pin"] if p not in sent and model["pin"][p]["check"]]
    if not left:
        # only slider pins left (level 19 after T): no ring to check, the knob and the dotted track instead
        sliders = [p for p in model["pin"] if p not in sent and "swipe" in model["pin"][p]]
        if rings or not sliders:
            return None
        g, ch = _small(image)
        if not all(_slider_seen(g, ch, model["pin"][p]["swipe"]) for p in sliders):
            return None
        return (name, b, tuple(sent), f"library board {name} kept from the last round (pins {' '.join(sent)} "
                                      f"sent; only the slider {' '.join(sliders)} left, its knob and dotted track "
                                      "seen on this frame)")
    pts = [xy for pid, xy in _lib_points(b) if pid in left]
    if any(min((((rx - x) ** 2 + (ry - y) ** 2) ** 0.5 for x, y in pts), default=99) > RING_TOL for rx, ry in rings):
        return None
    hidden, _, _ = _check_rings(image, model, skip=sent)
    if hidden:
        return None
    return (name, b, tuple(sent), f"library board {name} kept from the last round (pins {' '.join(sent)} sent; "
                                  f"the rings of {' '.join(left)} checked on this frame)")


# --- scrolling levels (challenge) ------------------------------------------------------------------------
# Challenge 1 (2026-10-06, session 030951, three losses, every pin tapped by hand): the level is about two
# screens tall and the camera follows the coloured pile, so the same pin sits at another y on every frame. The
# board is written once in level pixels (the view at the start = 0, "height"); each frame is placed in the
# level by its rings (one vertical offset for all of them, plus the few px of sideways shake after a blast),
# and the camera must rest where the board's "views" say for the place the colour is in: a frame taken while
# it still moves (the intro pan from the cup up to the top, 4-5 s after a pile falls) gives no moves. In try 2
# the camera moved 1219 -> 1307 between the frame and the tap on TD, and the tap pulled TV (greys out, lost).
VIEW_TOL = 35  # px between the view the frame shows and the view the camera rests at
SCROLL_TOL = 12  # px: a ring found and a pin of the board placed by the frame's offset


def _match_scrolling(image, rings, mem):
    """(name, board, pulled, (dx, view), how) or (None, None, None, None, why not)"""
    if not SCROLLING:
        return None, None, None, None, "no scrolling level in the library"
    why = "no scrolling level fits the rings"
    for name, b in SCROLLING.items():
        pts = _lib_points(b)
        sent = list(mem.get("sent") or []) if mem.get("entry") == name else []
        exp = None
        if sent or mem.get("entry") == name:
            model, errs, _ = _parse(b)
            if not errs:
                st0, _ = _initial(model)
                if st0 is not None:
                    st, _, loss = _replay(model, State(frozenset(), {}, st0, frozenset()), sent)
                    exp = None if loss else _view(model, st)
        best = None
        for rx, ry in rings:
            for _pid, (x, y) in pts:
                dx, view = rx - x, y - ry
                if abs(dx) > 16:
                    continue
                used, ok = {}, 0
                for qx, qy in rings:
                    m = None
                    for pid, (px, py) in pts:
                        d = max(abs(qx - (px + dx)), abs(qy - (py - view)))
                        if pid not in used.values() and d <= SCROLL_TOL and (m is None or d < m[0]):
                            m = (d, pid)
                    if m:
                        used[(qx, qy)] = m[1]
                        ok += 1
                score = (ok, -(abs(view - exp) if exp is not None else 0), -abs(dx))
                if best is None or score > best[0]:
                    best = (score, dx, view, dict(used))
        if best is None:
            continue
        (ok, _, _), dx, view, used = best
        if ok < len(rings):
            why = f"{name}: {len(rings) - ok} of {len(rings)} rings fit no pin at any view"
            continue
        if ok < int(mem.get("min_rings") or 0):
            why = f"{name}: only {ok} ring(s) fit"
            continue
        if ok < 3 and (exp is None or abs(view - exp) > 150):
            why = f"{name}: only {ok} ring(s), too few to place the frame in the level"
            continue
        back = [p for p in used.values() if p in sent]
        if back:
            return (None, None, None, None,
                    f"{name}: pin(s) {' '.join(back)} were tapped in an earlier round but their rings are still there "
                    "(the tap missed, or another pin came out): look at the frame")
        how = (f"scrolling board {name} recognised: {ok} ring(s) place this frame at view {view:.0f} px of the level"
               + (f" (shifted {dx:+.0f} px sideways)" if dx else "")
               + (f"; pins {' '.join(sent)} pulled in earlier rounds" if sent else ""))
        return name, b, tuple(sent), (dx, view), how
    return None, None, None, None, why


def _solve_scrolling(image, board, name, pulled, where, how):
    dx, view = where
    model, errs, warns = _parse(board)
    if errs:
        return {"moves": [], "note": f"{how}. board refused: " + "; ".join(errs[:6]), "rescan": False, "done": False}
    st0, err = _initial(model)
    if err:
        return {"moves": [], "note": f"{how}. board refused: {err}", "rescan": False, "done": False}
    start = State(frozenset(), {}, st0, frozenset())
    head = f"{model['level']}: " if model["level"] else ""
    st, _, loss = _replay(model, start, list(pulled))
    if loss:
        return {"moves": [], "rescan": False, "done": False,
                "note": f"{how}. {head}the pins already pulled ({' '.join(pulled)}) lose in the model: {loss}"}
    if not _balls_left(st):
        return {"moves": [], "rescan": False, "done": True, "note": f"{how}. {head}every pull is done ({' '.join(pulled)})"}
    exp = _view(model, st)
    if exp is not None and abs(view - exp) > VIEW_TOL:
        return {"moves": [], "rescan": True, "done": False,
                "state": {"entry": name, "sent": list(pulled)},
                "note": f"{how}. The camera is still moving: this frame shows view {view:.0f}, it rests at {exp:.0f} "
                        "with the colour where it is (the intro pan, or a pile still falling). Wait 3 s and run "
                        "solve pin-pull --run again (--settle 7 avoids it)."}
    order, source = None, ""
    if model["plan"] and model["plan"][:len(pulled)] == list(pulled):
        rest = model["plan"][len(pulled):]
        steps = _split_steps(model, rest)
        cur, ok = st, steps is not None and len(pulled) + len(rest) <= (model["max_moves"] or 99)
        for s in steps or []:
            cur, _, loss = _step_ok(model, cur, s)
            if cur is None or loss:
                ok = False
                break
        if ok and not _balls_left(cur):
            order, source = rest, "the board's plan (checked by the model, not yet won on the phone)"
    if order is None:
        found, partial, err = _search(model, st)
        if not found:
            msg = f"{head}no order gets every ball into the cup" + (f" within {model['max_moves']} moves" if model["max_moves"] else "")
            if err:
                msg += f" ({err})"
            if partial:
                msg += f"; the best keeps balls in {', '.join(partial[2])} after {' '.join(partial[1])}"
            return {"moves": [], "rescan": False, "done": False, "note": f"{how}. {msg}"}

        def rank(o):
            _, steps_, _ = _replay(model, st, list(o))
            return (sum(s_["timing"] for s_ in steps_), len(o))
        order, source = list(min(found, key=rank)), f"{len(found)} safe order(s) that keep each next ring in the view"
    step = _split_steps(model, order)[0]
    # the step's rings where this frame shows them
    k = image.size[0] / model["fw"]
    out_view = [p for p in step if not _in_view(model, p, view)]
    if out_view:
        return {"moves": [], "rescan": True, "done": False, "state": {"entry": name, "sent": list(pulled)},
                "note": f"{how}. {head}next {' '.join(step)}, but {' '.join(out_view)} is not in this view: wait for "
                        "the camera and run solve pin-pull --run again"}
    cm = {"fw": model["fw"], "pin": {}}
    for pid, p in model["pin"].items():
        if pid in pulled or "swipe" in p or not _in_view(model, pid, view):
            continue
        cm["pin"][pid] = {"at": [p["at"][0] + dx, p["at"][1] - view], "check": p["check"], "gold": p["gold"]}
    missing, off, _ = _check_rings(image, cm, skip=[p for p in cm["pin"] if p not in step])
    if missing:
        return {"moves": [], "rescan": True, "done": False, "state": {"entry": name, "sent": list(pulled)},
                "note": f"{how}. {head}next {' '.join(step)}, but no ring at " + ", ".join(missing)
                        + " on this frame (a popup, an ad, or the camera moved): look, then run again"}
    moves = []
    for pid in step:
        p = model["pin"][pid]
        x, y = p.get("tap") or p["at"]
        moves.append([round((x + dx) * k), round((y - view) * k)])
    _, all_steps, _ = _replay(model, st, order)
    done = len(order) == len(step)
    taps = " ".join(f"{(model['pin'][p].get('tap') or model['pin'][p]['at'])[0] + dx:.0f},"
                    f"{(model['pin'][p].get('tap') or model['pin'][p]['at'])[1] - view:.0f}" for p in step)
    note = (f"{how}. {head}order {' '.join(order)} ({len(order)} pulls left, {source}). This round plays "
            f"{' '.join(step)} at {taps} on this frame"
            + (" (one round: keep --gap under 1 s, the second ring leaves the view once the first pile falls)"
               if len(step) > 1 else "")
            + (f"; {' '.join(p for p in step if 'tap' in model['pin'][p])} tapped beside the ring centre, away from "
               "the neighbour that a centre tap pulls" if any("tap" in model["pin"][p] for p in step) else "")
            + f". Expect: {_describe(all_steps)}."
            + ("" if done else " Solve again on the next frame (solve --run --rounds 12 --settle 7 does it)."))
    if off:
        note += " rings off by >9 px: " + ", ".join(off)
    if warns:
        note += " warn: " + "; ".join(warns)
    return {"moves": moves, "rescan": not done, "done": done, "note": note,
            "state": {"entry": name, "sent": list(pulled) + list(step)}}


# --- the entry point -----------------------------------------------------------------------------------
def _pace(res, mem):
    """Hold this round's pull until the previous round's pull is `_wait` s old. sw.py taps the moves as soon
    as the solver returns and gives no pause of its own between rounds but the --gap the player typed, so
    the pause a pull needs lives here, timed from the moment the previous round's moves were returned
    (`t_sent` in the memory). A memory older than the wait (a recorded frame, a later call) waits nothing."""
    w = float(res.pop("_wait", 0) or 0)
    pin = res.pop("_pin", None)
    t = mem.get("t_sent")
    if res.get("moves") and w > 0 and isinstance(t, (int, float)):
        rest = t + w - time.time()
        if 0 < rest <= 30:
            time.sleep(rest)
            res["note"] = (f"{res.get('note') or ''} Waited {rest:.1f} s before {pin}: it needs {w:g} s after "
                           "the previous pull (balls still running).").strip()
    return res


def _stamp(res):
    if res.get("moves") and isinstance(res.get("state"), dict):
        res["state"]["t_sent"] = time.time()
    return res


def solve(image, board=None, frame_scale=1.0, state=None):
    mem = state if isinstance(state, dict) else {}
    if board is not None:
        res = _solve_board(image, board)
        res.pop("_wait", None), res.pop("_pin", None)
        sent = res.pop("_sent", [])
        res.pop("_stage_done", None)
        if res.get("moves") and not res.get("done"):
            # one pull per round: the next round of `solve --run` comes without --board, so the board rides
            # in the memory
            res["state"] = {"entry": "board", "board": board, "sent": sent}
        return _stamp(res)
    if mem.get("entry") == "board" and isinstance(mem.get("board"), dict):
        pulled = [p for p in mem.get("sent") or []]
        res = _pace(_solve_board(image, mem["board"], pulled=pulled), mem)
        sent = res.pop("_sent", [])
        res.pop("_stage_done", None)
        res["note"] = f"the board of the first round, pins {' '.join(pulled)} pulled. {res.get('note') or ''}"
        if res.get("moves") and not res.get("done"):
            res["state"] = {"entry": "board", "board": mem["board"], "sent": pulled + sent}
        return _stamp(res)
    scroll_why = None
    if mem.get("entry") in SCROLLING:
        # a scrolling level (challenge) in progress: placed in the level by its rings, never as a screen
        g, ch = _small(image)
        sname, sb, spulled, where, scroll_why = _match_scrolling(image, _find_rings(g, ch), mem)
        if sname:
            return _stamp(_solve_scrolling(image, sb, sname, spulled, where, scroll_why))
        return {"moves": [], "rescan": True, "done": False, "state": mem,
                "note": f"no move for the scrolling level {mem['entry']} on this frame ({scroll_why}); a popup, an "
                        "ad, the fail or win screen, or a pin that did not come out: look at it"}
    name, lib, pulled, how = _match_library(image, state)
    if not name and not mem.get("entry"):
        # no level in memory: a scrolling level needs 4 rings or more to be told from a screen-sized one (its
        # frames would otherwise read as a grey stack or match nothing)
        g, ch = _small(image)
        sname, sb, spulled, where, scroll_why = _match_scrolling(image, _find_rings(g, ch), {"min_rings": 4})
        if sname:
            return _stamp(_solve_scrolling(image, sb, sname, spulled, where, scroll_why))
    if name:
        res = _solve_board(image, lib, pulled=pulled, verified=lib.get("verified"))
        if pulled and mem.get("entry") == name:
            res = _pace(res, mem)
        res.pop("_wait", None), res.pop("_pin", None)
        res["note"] = f"{how}. {res.get('note') or ''}"
        res["state"] = {"entry": name, "sent": list(pulled) + res.pop("_sent", []), "stage": lib.get("stage"),
                        "stage_done": bool(res.pop("_stage_done", False))}
        return _stamp(res)
    board, how2 = _read_stack(image)
    if board is not None:
        res = _solve_board(image, board)
        res.pop("_sent", None), res.pop("_stage_done", None), res.pop("_wait", None), res.pop("_pin", None)
        res["note"] = f"{how2}. {res.get('note') or ''}"
        return res
    if mem.get("stage_done"):
        return {"moves": [], "rescan": True, "done": True, "state": mem,
                "note": f"stage {mem.get('stage')} ({mem.get('entry')}) was played; the next stage is not on this "
                        "frame (the stage animation or an ad): look, close an ad if one came, then solve pin-pull "
                        "--run again"}
    return {"moves": [], "rescan": False, "done": False,
            "note": f"no board and the frame is not a known level ({how}) nor a simple stack ({how2}): write "
                    "places (has, exits) and pins (ring positions) as JSON and pass it with --board (the "
                    "playbook, section pin-pull)"}


def _solve_board(image, board, pulled=(), verified=None):
    model, errs, warns = _parse(board)
    if errs:
        return {"moves": [], "note": "board refused: " + "; ".join(errs[:6]), "rescan": False, "done": False}
    start_piles, err = _initial(model)
    if err:
        return {"moves": [], "note": "board refused: " + err, "rescan": False, "done": False}
    start = State(frozenset(), {}, start_piles, frozenset())
    events, passed = [], set()
    loss = _settle(model, start, events, passed)
    if loss or events:
        return {"moves": [], "rescan": False, "done": False,
                "note": "board refused: before any pull something already moves "
                        f"({loss or '; '.join(events)}): an exit marked free should need a pin"}
    head = (f"{model['level']}" + (f" stage {model['stage']}" if model["stage"] and "stage" not in model["level"]
                                   else f" ({model['stage']})" if model["stage"] else "") + ": ") if model["level"] else ""
    stage = str(model["stage"] or "")
    last_stage = not stage or (stage.split("/")[0].strip() == stage.split("/")[-1].strip())
    pulled = tuple(pulled)
    start0 = start
    if pulled:
        st, _, loss = _replay(model, start, list(pulled))
        if loss:
            return {"moves": [], "rescan": False, "done": False,
                    "note": f"{head}the pins already pulled ({' '.join(pulled)}) lose in the model: {loss}"}
        start = st
        if not _balls_left(start):
            return {"moves": [], "rescan": not last_stage, "done": True, "_stage_done": not last_stage,
                    "note": f"{head}every pull of this board is done ({' '.join(pulled)})"
                            + ("" if last_stage else "; the next stage comes after the animation or an ad: "
                               "look, then solve pin-pull --run again")}
    missing, off, k = _check_rings(image, model, skip=pulled)
    if missing:
        return {"moves": [], "rescan": True, "done": False,
                "note": "board refused: no pin ring on this frame at " + ", ".join(missing)
                        + " (a popup, the camera moved, or a misread position; a pin that is not a plain "
                          "ring takes \"check\": false)"}
    tail = []
    if warns:
        tail.append("warn: " + "; ".join(warns))
    if off:
        tail.append("rings off by >9 px: " + ", ".join(off))

    if model["try"]:
        order = [str(p) for p in model["try"]]
        st, steps, loss = _replay(model, start, order)
        left = _balls_left(st)
        verdict = (f"LOST at {steps[-1]['pin']}: {loss}" if loss else
                   "WON: every ball in the cup" if not left else f"no loss, balls left in {', '.join(left)}")
        safe = not loss and not left
        return {"moves": _moves(model, order, k) if safe else [], "rescan": not safe, "done": safe,
                "note": f"{head}try {' '.join(order)} -> {verdict}. {_describe(steps)}"
                        + ("; " + "; ".join(tail) if tail else "")}

    best, source = None, ""
    for v in verified or []:  # an order already won on the phone beats a shorter one only the model knows
        v = [str(p) for p in v]
        if v[:len(pulled)] != list(pulled):
            continue
        rest = v[len(pulled):]
        st, _, loss = _replay(model, start, rest)
        if rest and not loss and not _balls_left(st):
            best, source = tuple(rest), "the order won on the phone"
            break
    if best is None:
        found, partial, err = _search(model, start)
        if err and not found:
            return {"moves": [], "note": f"{head}board refused: {err}", "rescan": False, "done": False}
        if not found:
            msg = f"{head}no order gets every ball into the cup without a loss"
            if partial:
                msg += (f"; the best keeps balls in {', '.join(partial[2])} after {' '.join(partial[1])}: "
                        "check the board (an exit missing or a wrong 'via'), or play that part and look")
            if model["max_moves"]:
                msg += f" (within {model['max_moves']} moves)"
            return {"moves": [], "note": msg, "rescan": False, "done": False}

        def rank(order):
            _, steps, _ = _replay(model, start, order)
            return (sum(s["timing"] for s in steps), order.__len__())

        best = min(found, key=rank)
        source = f"{len(found)} safe order(s) of this length"
    st, steps, _ = _replay(model, start, best)
    gap = model["gap"] + (2 if any(s["timing"] for s in steps) else 0)
    parked = sorted(r for r, p in st.piles.items() if p[2])
    order = list(best)
    # the pause this round's first pull needs after the previous round's pull: the board's "waits", and
    # gap + 2 s for a pull that re-routes a place balls just ran through (timing, judged on the whole order
    # from the start: replayed from the pulled pins alone the run-through is forgotten). 2026-10-05
    # (235042): level 20 B, M, Y as rounds 3.8 s apart lost; M was read on a frame with the blue still
    # running over the M rod (shot 61) and the last blue went to the yellow cup (shot 62).
    wait = 0.0
    if pulled:
        _, fsteps, _ = _replay(model, start0, list(pulled) + order[:1])
        timed = bool(fsteps) and len(fsteps) > len(pulled) and fsteps[len(pulled)]["timing"]
        wait = max(model["waits"].get(order[0], 0.0), model["gap"] + 2 if timed else 0.0)
    note = (f"{head}order {' '.join(order)} ({len(order)} pulls, {source}). "
            f"Play: taps \"{_taps(model, order)}\" --gap {gap:g}. Expect: {_describe(steps)}. "
            f"End: every ball in the cup" + (f", bomb parked in {', '.join(parked)}" if parked else "") + ".")
    if tail:
        note += " " + "; ".join(tail)
    # a pin made of two rings pulled together (level 5 stage 2): the run's gap between moves is too long for
    # it, so the solver plays up to it and hands the pair over
    pair = next((i for i, p in enumerate(order) if "with" in model["pin"][p]), None)
    if pair == 0:
        p = model["pin"][order[0]]
        return {"moves": [], "rescan": True, "done": False, "_sent": [order[0]],
                "note": note + f" FIRST {order[0]}: its two rings must go together, under 0.5 s apart: "
                               f"taps \"{p['at'][0]:.0f},{p['at'][1]:.0f} {p['with'][0]:.0f},{p['with'][1]:.0f}\" "
                               "--gap 0.3, then solve pin-pull --run again for the rest."}
    cut = len(order) if pair is None else pair
    for r in model["reframe"]:
        if r in order[:cut - 1]:
            cut = order.index(r) + 1
    if model["scrolling"]:
        cut = 1
    # One pull per round: every pull must settle before the next (bombs meet, a pile stops running), and a
    # batch takes the run's --gap, 0.35 s when the player leaves it out. 2026-10-04 (session 004411): level 11
    # with the library order E W F B (--gap 5) was lost twice with "Balls fell out of the level": on 241.5.1 a
    # grey stays on the C half after E, so E C W F B is the order (won in 005453). A round (the --gap, the
    # settle, a shot, the solver) is >= 4 s, and each next pull is read on a frame showing the last one's result.
    single = cut > 1
    if single:
        cut = 1
    if cut < len(order):
        why = ("the camera scrolls: pull one pin, take a shot, find the next ring by its name" if model["scrolling"]
               else "each pull settles before the next; the frame shows its result" if single
               else f"the board re-frames after {order[cut - 1]}: the next rings move"
               if order[cut - 1] in model["reframe"] else f"{order[cut]} is a pair of rings pulled together")
        return {"moves": _moves(model, order[:cut], k), "rescan": True, "done": False, "_sent": order[:cut],
                "_wait": wait, "_pin": order[0],
                "note": note + f" This round plays {' '.join(order[:cut])} only ({why}); solve again on the next "
                               "frame (solve --run --rounds 6 does it)."}
    if not last_stage:
        note += f" Stage {stage}: look again when the next stage appears."
    return {"moves": _moves(model, order, k), "rescan": not last_stage, "done": last_stage, "_sent": order,
            "_stage_done": not last_stage, "_wait": wait, "_pin": order[0], "note": note}


# generated from the local state/<game>/solvers/boards/*.json (name: board + verified orders won on the phone;
# IQ1 = Sketchman IQ Test level 1 (the All You Can Play mode), no verified order yet: the search plays it)
LIBRARY_JSON = r'''{
 "L3": {"level":"level 3","places":{"G":{"has":["grey"],"exits":[{"to":"out","via":["L"]},{"to":"cup","via":["S"]}]},"POP":{"has":["colour"],"exits":[{"to":"cup","via":["S"]}]}},"pins":{"D":{"at":[363,300],"joins":[["G","POP"]]},"S":[606,500],"L":[140,794]},"verified":[["D","S"]],"src":"raw/com.maroieqrwlk.unpin/20261003-203702-chrono-2FYKPJ/shots/00007.jpg"},
 "L4": {"level":"level 4","places":{"BOMB":{"has":["bomb"],"exits":[{"to":"POP","via":["A"]}]},"POP":{"has":["colour"],"exits":[{"to":"cup","via":["B"]}]}},"pins":{"A":[118,482],"B":[612,594]},"verified":[["B"]],"src":"raw/com.maroieqrwlk.unpin/20261003-203702-chrono-2FYKPJ/shots/00015.jpg"},
 "L5-s1": {"level":"level 5","stage":"1/4","places":{"BOMB":{"has":["bomb"],"exits":[{"to":"cup","via":["L"]}]},"POP":{"has":["colour"],"exits":[{"to":"cup","via":["R"]}]}},"pins":{"L":[124,612],"R":[606,598]},"verified":[["R"]],"src":"raw/com.maroieqrwlk.unpin/20261003-203702-chrono-2FYKPJ/shots/00021.jpg"},
 "L5-s2": {"level":"level 5","stage":"2/4","places":{"POP":{"has":["colour"],"exits":[{"to":["GL","GR"],"via":["TOP"]}]},"GL":{"has":["grey"],"exits":[{"to":"cup","via":["BL"]}]},"GR":{"has":["grey"],"exits":[{"to":"cup","via":["BR"]}]}},"pins":{"TOP":{"at":[222,310],"with":[508,310]},"BL":[168,772],"BR":[560,772]},"verified":[["TOP","BL","BR"]],"src":"raw/com.maroieqrwlk.unpin/20261003-203702-chrono-2FYKPJ/shots/00023.jpg"},
 "L5-s3": {"level":"level 5","stage":"3/4","places":{"POP":{"has":["colour"],"exits":[{"to":"GL","via":["A"]}]},"GL":{"has":["grey"],"exits":[{"to":"X","via":["B"]}]},"GR":{"has":["grey"],"exits":[{"to":"X","via":["C"]}]},"X":{"exits":[{"to":"cup","via":["XL","XR"]}]}},"pins":{"A":[130,482],"B":[132,620],"C":[558,620],"XL":[122,686],"XR":[606,664]},"verified":[["A","B","C","XL","XR"]],"src":"raw/com.maroieqrwlk.unpin/20261003-203702-chrono-2FYKPJ/shots/00027.jpg"},
 "L5-s4": {"level":"level 5","stage":"4/4","places":{"TL":{"has":["colour"],"exits":[{"to":["LL","LU"],"via":["H"]}]},"TM":{"has":["colour"],"exits":[{"to":"cup","via":["H"]}]},"TR":{"has":["colour"],"exits":[{"to":["RL","RU"],"via":["H"]}]},"LL":{"has":["grey"],"exits":[{"to":"cup","via":["V1"]}]},"LU":{"has":["grey"],"exits":[{"to":"cup","via":["V1"]}]},"RL":{"has":["grey"],"exits":[{"to":"cup","via":["V2"]}]},"RU":{"has":["grey"],"exits":[{"to":"cup","via":["V2"]}]}},"pins":{"V1":[294,311],"V2":[412,311],"H":[608,442]},"verified":[["H","V1","V2"]],"src":"raw/com.maroieqrwlk.unpin/20261003-203702-chrono-2FYKPJ/shots/00031.jpg"},
 "L6": {"level":"level 6","places":{"POP":{"has":["colour"],"exits":[{"to":"cup","via":["V"]},{"to":"G","via":["B1"]}]},"G":{"has":["grey"],"exits":[{"to":"cup","via":["V"]},{"to":"BC","via":["B2"]}]},"BC":{"has":["bomb"],"exits":[{"to":"out","via":["B3"]},{"to":"cup","via":["V"]}]}},"pins":{"B1":[190,386],"B2":[196,506],"B3":[198,622],"V":[392,298]},"verified":[["B3","B1","V"]],"src":"raw/com.maroieqrwlk.unpin/20261003-203702-chrono-2FYKPJ/shots/00041.jpg"},
 "L7": {"level":"level 7","places":{"POPL":{"has":["colour"],"exits":[{"to":"GL","via":["H"]}]},"POPR":{"has":["colour"],"exits":[{"to":"GR","via":["H"]}]},"GL":{"has":["grey"],"exits":[{"to":"cup","via":["DL"]}]},"GR":{"has":["grey"],"exits":[{"to":"cup","via":["DR"]}]}},"pins":{"H":[122,466],"DL":[190,747],"DR":[553,753]},"verified":[["H","DL","DR"]],"src":"raw/com.maroieqrwlk.unpin/20260930-201034-chrono-2FYKPJ/shots/00061.jpg"},
 "L8": {"level":"level 8","reframe":["T"],"places":{"GL":{"has":["grey"],"exits":[{"to":"LOW","via":["T"]}]},"BL":{"has":["bomb"],"exits":[{"to":"U","via":["T"]}]},"BR":{"has":["bomb"],"exits":[{"to":"U","via":["T"]}]},"GR":{"has":["grey"],"exits":[{"to":"MIDR","via":["T"]}]},"U":{"exits":[{"to":"LOW","via":["M"]}]},"MIDR":{"has":["colour"],"exits":[{"to":"LOW","via":["M"]}]},"LOW":{"has":["colour"],"exits":[{"to":"cup","via":["P"]}]}},"pins":{"T":[608,492],"M":[595,735],"P":[186,808]},"verified":[["T","P","M"]],"src":"raw/com.maroieqrwlk.unpin/20261003-203702-chrono-2FYKPJ/shots/00068.jpg"},
 "L8-after-T": {"level":"level 8 (after the top pin)","places":{"MIDR":{"has":["colour"],"exits":[{"to":"LOW","via":["M"]}]},"LOW":{"has":["colour"],"exits":[{"to":"cup","via":["P"]}]}},"pins":{"M":[604,750],"P":[190,822]},"verified":[["P","M"]],"src":"raw/com.maroieqrwlk.unpin/20261003-203702-chrono-2FYKPJ/shots/00070.jpg"},
 "L9": {"level":"level 9","places":{"POP":{"has":["colour"],"exits":[{"to":"G1","via":["A"]}]},"G1":{"has":["grey"],"exits":[{"to":"G2","via":["B"]}]},"G2":{"has":["grey"],"exits":[{"to":"G3","via":["C"]}]},"G3":{"has":["grey"],"exits":[{"to":"cup","via":["D"]}]}},"pins":{"A":[262,347],"B":[445,393],"C":[445,797],"D":[322,830]},"verified":[["A","B","C","D"]],"src":"raw/com.maroieqrwlk.unpin/20261001-054205-chrono-2FYKPJ/shots/00005.jpg"},
 "L10-s1": {"level":"level 10 stage 1","stage":"1/4","places":{"BL1":{"has":["bomb"],"exits":[{"to":"BL2","via":["S"]}]},"PM":{"has":["colour"],"exits":[{"to":"GM","via":["S"]}]},"BR1":{"has":["bomb"],"exits":[{"to":"BR2","via":["S"]}]},"BL2":{"exits":[{"to":"out","via":["F"]}]},"GM":{"has":["grey"],"exits":[{"to":"cup","via":["F"]}]},"BR2":{"exits":[{"to":"out","via":["F"]}]}},"pins":{"S":[608,570],"F":[120,718],"V1":{"at":[262,417],"joins":[["BL1","PM"],["BL2","GM"]]},"V2":{"at":[462,417],"joins":[["PM","BR1"],["GM","BR2"]]}},"verified":[["S","F"]],"src":"raw/com.maroieqrwlk.unpin/20261001-054205-chrono-2FYKPJ/shots/00121.jpg"},
 "L10-s2": {"level":"level 10 stage 2","stage":"2/4","places":{"PO":{"has":["colour"],"exits":[{"to":"LC","via":["P"]}]},"RG":{"has":["grey"],"exits":[{"to":"LC","via":["R"]}]},"LL":{"has":["grey"]},"LC":{"has":["grey"],"exits":[{"to":"cup","via":["F"]}]}},"pins":{"P":[255,442],"R":[592,624],"D":{"at":[222,826],"joins":[["LL","LC"]]},"F":[540,683]},"verified":[["P","R","D","F"]],"src":"raw/com.maroieqrwlk.unpin/20261001-054205-chrono-2FYKPJ/shots/00129.jpg"},
 "L10-s3": {"level":"level 10 stage 3","stage":"3/4","places":{"G":{"has":["grey"]},"P":{"has":["colour"],"exits":[{"to":"FT","via":["C"]}]},"B1":{"has":["bomb"],"exits":[{"to":"FT","via":["Fp"]}]},"FT":{"has":["bomb"],"exits":[{"to":"cup","via":["E"]}]}},"pins":{"D":{"at":[253,765],"joins":[["G","P"]]},"C":[360,597],"Fp":[617,636],"E":[609,725]},"verified":[["D","Fp","C","E"]],"src":"raw/com.maroieqrwlk.unpin/20261001-075644-chrono-2FYKPJ/shots/00003.jpg"},
 "L10-s4": {"level":"level 10 stage 4","stage":"4/4","places":{"TL":{"has":["grey"],"exits":[{"to":"LM","via":["UL"]}]},"TR":{"has":["grey"],"exits":[{"to":"RM","via":["UR"]}]},"LM":{"has":["grey"],"exits":[{"to":"BOT","via":["ML"]}]},"TUBE":{"has":["colour"],"exits":[{"to":"BOT","via":["ML"]}]},"RM":{"has":["grey"],"exits":[{"to":"BOT","via":["ML"]}]},"BOT":{"has":["grey"],"exits":[{"to":"cup","via":["B"]}]}},"pins":{"UL":[132,396],"UR":[608,496],"ML":[122,630],"B":[570,728]},"verified":[["UL","UR","ML","B"]],"src":"raw/com.maroieqrwlk.unpin/20261003-211035-chrono-2FYKPJ/shots/00021.jpg"},
 "L11": {"level":"level 11","places":{"G":{"has":["grey"],"exits":[{"to":"BOX","via":["E"]},{"to":"BOX","via":["C"]}]},"BR":{"has":["bomb"],"exits":[{"to":"CH","via":["E"]}]},"POP":{"has":["colour"],"exits":[{"to":"BR","via":["W"]},{"to":"out","via":["P"]}]},"BOX":{"exits":[{"to":"CH","via":["F"]},{"to":"BR","via":["V"]}]},"CH":{"has":["bomb"],"exits":[{"to":"cup","via":["B"]}]}},"pins":{"E":[570,470],"W":[512,392],"P":[612,530],"C":[105,505],"F":[105,597],"B":[167,821],"V":[420,385]},"verified":[["E","C","W","F","B"]],"src":"raw/com.maroieqrwlk.unpin/20261004-004411-chrono-2FYKPJ/shots/00029.jpg"},
 "L12": {"level":"level 12","places":{"POP":{"has":["colour"],"exits":[{"to":"G","via":["A"]}]},"G":{"has":["grey"],"exits":[{"to":"cup","via":["B"]}]},"BOMB":{"has":["bomb"],"exits":[{"to":"?","via":["D"]},{"to":"?","via":["E"]}]}},"pins":{"A":[143,525],"B":{"at":[221,626],"gold":true},"D":[425,455],"E":[580,690]},"verified":[["A","B"]],"src":"raw/com.maroieqrwlk.unpin/20261004-005453-chrono-2FYKPJ/shots/00018.jpg"},
 "L12-after-A": {"level":"level 12 (after A)","places":{"G":{"has":["colour"],"exits":[{"to":"cup","via":["B"]}]},"BOMB":{"has":["bomb"],"exits":[{"to":"?","via":["D"]},{"to":"?","via":["E"]}]}},"pins":{"B":{"at":[221,626],"gold":true},"D":[425,455],"E":[580,690]},"verified":[["B"]],"src":"raw/com.maroieqrwlk.unpin/20261004-005453-chrono-2FYKPJ/shots/00019.jpg"},
 "L13": {"level":"level 13","places":{"TL":{"has":["colour"],"exits":[{"to":"ML","via":["T"]}]},"TR":{"has":["grey"],"exits":[{"to":"MR","via":["T"]}]},"ML":{"has":["grey"],"exits":[{"to":"CL","via":["M"]}]},"MR":{"has":["grey"],"exits":[{"to":"CR","via":["M"]}]},"CL":{"has":["bomb"],"exits":[{"to":"cup","via":["B"]}]},"CR":{"has":["bomb"],"exits":[{"to":"cup","via":["B"]}]},"PL":{"has":["bomb"],"exits":[{"to":"CL","via":["L"]}]},"PR":{"has":["bomb"],"exits":[{"to":"CR","via":["R"]}]}},"pins":{"V":{"at":[365,432],"joins":[["TL","TR"],["ML","MR"],["CL","CR"]]},"T":[484,517],"M":[267,617],"L":[230,597],"R":[505,597],"B":[481,797]},"verified":[["V","T","M","B"]],"src":"raw/com.maroieqrwlk.unpin/20261001-102608-chrono-2FYKPJ/shots/00038.jpg"},
 "L14": {"level":"level 14","places":{"P":{"has":["colour"],"exits":[{"to":"HL","via":["DL"]}]},"G1":{"has":["grey"],"exits":[{"to":"HL","via":["DL"]}]},"G2":{"has":["grey"],"exits":[{"to":"HR","via":["DR"]}]},"G3":{"has":["grey"],"exits":[{"to":"HR","via":["DR"]}]},"HL":{"has":["grey"],"exits":[{"to":"VF","via":["H"]}]},"HR":{"has":["grey"],"exits":[{"to":"VF","via":["H"]}]},"VF":{"exits":[{"to":"out","via":["LL"]},{"to":"cup","via":["LR"]}]}},"pins":{"DL":[118,422],"DR":[591,402],"V1":{"at":[262,350],"joins":[["P","G1"]]},"V2":{"at":[361,350],"joins":[["G1","G2"],["HL","HR"]]},"V3":{"at":[455,350],"joins":[["G2","G3"]]},"H":[596,609],"LR":[613,622],"LL":[118,630]},"verified":[["DL","DR","V2","LR","H"],["V1","V2","V3","DL","DR","LR","H"]],"src":"raw/com.maroieqrwlk.unpin/20261005-014031-chrono-2FYKPJ/shots/00013.jpg"},
 "L15-s1": {"level":"level 15 stage 1","stage":"1/4","places":{"TOP":{"has":["colour"],"exits":[{"to":"XZ","via":["T"]}]},"XZ":{"has":["bomb"],"exits":[{"to":"BOT","via":["X1","X2"]},{"to":"out","via":["X1"]},{"to":"?","via":["X2"]}]},"BOT":{"has":["grey"],"exits":[{"to":"cup","via":["F"]}]}},"pins":{"T":[160,450],"X1":[185,497],"X2":[557,494],"F":[163,810]},"verified":[["X1","X2","T","F"]],"src":"raw/com.maroieqrwlk.unpin/20261001-102608-chrono-2FYKPJ/shots/00120.jpg"},
 "L15-s2": {"level":"level 15 stage 2","stage":"2/4","places":{"POP":{"has":["colour"],"exits":[{"to":"U","via":["D"]}]},"U":{"has":["grey"],"exits":[{"to":"M","via":["A"]}]},"M":{"has":["grey"],"exits":[{"to":"L","via":["B"]}]},"L":{"has":["grey"],"exits":[{"to":"cup","via":["C"]}]}},"pins":{"D":[383,343],"A":[198,493],"B":[118,775],"C":[582,817]},"verified":[["D","A","B","C"]],"src":"raw/com.maroieqrwlk.unpin/20261001-102608-chrono-2FYKPJ/shots/00128.jpg"},
 "L15-s3": {"level":"level 15 stage 3","stage":"3/4","places":{"BOMB":{"has":["bomb"],"exits":[{"to":"LCOL","via":["H"]}]},"LCOL":{"exits":[{"to":"cup","via":["V1"]}]},"PM":{"has":["colour"],"exits":[{"to":"MG","via":["H"]}]},"PR":{"has":["colour"],"exits":[{"to":"BG","via":["H"]}]},"MG":{"has":["grey"],"exits":[{"to":"cup","via":["V2"]}]},"BG":{"has":["grey"],"exits":[{"to":"cup","via":["V2"]}]}},"pins":{"V1":[262,298],"V2":[377,298],"H":[578,437]},"verified":[["H","V2"]],"src":"raw/com.maroieqrwlk.unpin/20261001-102608-chrono-2FYKPJ/shots/00136.jpg"},
 "L15-s4": {"level":"level 15 stage 4","stage":"4/4","places":{"PO":{"has":["colour"],"exits":[{"to":"GR","via":["P"]}]},"GR":{"has":["grey"],"exits":[{"to":"cup","via":["G","F"]},{"to":"BZ","via":["G"]}]},"BZ":{"has":["bomb"],"exits":[{"to":"out","via":["R","F"]},{"to":"?","via":["F"]}]}},"pins":{"P":[330,385],"G":[440,440],"R":[488,532],"F":[130,645]},"verified":[["R","F","P","G"]],"src":"raw/com.maroieqrwlk.unpin/20261001-145738-chrono-2FYKPJ/shots/00003.jpg"},
 "L16": {"level":"level 16","places":{"PL":{"has":["colour"],"exits":[{"to":"BL","via":["GP"]}]},"BL":{"has":["bomb"],"exits":[{"to":"C","via":["I1"]}]},"BR":{"has":["bomb"],"exits":[{"to":"C","via":["I2"]}]},"GR":{"has":["grey"],"exits":[{"to":"BR","via":["RP"]}]},"C":{"exits":[{"to":"cup","via":["F"]}]}},"pins":{"GP":{"at":[222,408],"gold":true},"I1":[307,456],"I2":[421,463],"RP":[493,420],"F":[209,806]},"verified":[["I1","I2","RP","GP","F"]],"src":"raw/com.maroieqrwlk.unpin/20261005-151039-chrono-2FYKPJ/shots/00032.jpg"},
 "L17": {"level":"level 17","places":{"TL":{"has":["bomb"],"exits":[{"to":"MC","via":["V1"]}]},"TR":{"has":["grey"],"exits":[{"to":"MC","via":["V2"]}]},"MC":{"exits":[{"to":"CTR","via":["H"]}]},"LL":{"has":["colour"],"exits":[{"to":"CTR","via":["DL"]}]},"LR":{"has":["bomb"],"exits":[{"to":"CTR","via":["DR"]}]},"CTR":{"exits":[{"to":"cup","via":["F"]}]}},"pins":{"V1":[317,292],"V2":[452,292],"H":[123,607],"DL":[243,828],"F":[285,838],"DR":[520,823]},"verified":[["H","DL","V2","F"],["V1","DR","H","V2","DL","F"]],"src":"raw/com.maroieqrwlk.unpin/20261005-151039-chrono-2FYKPJ/shots/00046.jpg"},
 "L18": {"level":"level 18","places":{"BOMB":{"has":["bomb"],"exits":[{"to":"?","via":["A"]}]},"POP":{"has":["colour"],"exits":[{"to":"GC","via":["C"]}]},"GL":{"has":["grey"]},"GC":{"has":["grey"],"exits":[{"to":"GB","via":["D"]}]},"GB":{"has":["grey"],"exits":[{"to":"cup","via":["E"]}]}},"pins":{"A":[342,412],"B":{"at":[411,448],"joins":[["GL","GC"]]},"C":[475,448],"D":[152,770],"E":[477,792]},"verified":[["C","B","D","E"]],"src":"raw/com.maroieqrwlk.unpin/20261001-150634-chrono-2FYKPJ/shots/00059.jpg"},
 "L19": {"level":"level 19","places":{"BLUE":{"has":["colour"],"exits":[{"to":"CH","via":["T"]}]},"CH":{"exits":[{"to":"cup","via":["K"]}]}},"pins":{"T":[420,468],"K":{"swipe":[153,790,360,745]}},"waits":{"K":6},"verified":[["T","K"]],"src":"raw/com.maroieqrwlk.unpin/20261001-153137-chrono-2FYKPJ/shots/00009.jpg"},
 "L20": {"level":"level 20","places":{"YB":{"has":["yellow"],"exits":[{"to":"J","via":["Y"]}]},"BB":{"has":["blue"],"exits":[{"to":"J","via":["B"]}]},"J":{"exits":[{"to":"cup:yellow","via":["M"]},{"to":"cup:blue","via":[]}]}},"pins":{"Y":[335,457],"B":[400,458],"M":[229,820]},"waits":{"M":10,"Y":7},"verified":[["B","M","Y"]],"src":"raw/com.maroieqrwlk.unpin/20261006-012240-chrono-2FYKPJ/shots/00024.jpg"},
 "L21": {"level":"level 21","places":{"LPZ":{"has":["colour"],"exits":[{"to":"B1Z","via":["LP"]}]},"B1Z":{"has":["bomb"],"exits":[{"to":"DZ","via":["B1"]}]},"DZ":{"exits":[{"to":"cup","via":["D"]},{"to":"BZ","via":[]}]},"BZ":{"has":["bomb"],"exits":[{"to":"cup","via":["D"]},{"to":"cup","via":[],"only":"balls"}]},"GZ":{"has":["grey"],"exits":[{"to":"RPZ","via":["G"]}]},"RPZ":{"has":["colour"],"exits":[{"to":"BZ","via":["RP"]}]}},"pins":{"LP":[117,513],"B1":[175,632],"D":[131,657],"G":[613,468],"RP":[587,606]},"verified":[["B1","LP","G","RP"]],"src":"raw/com.maroieqrwlk.unpin/20261001-160324-chrono-2FYKPJ/shots/00004.jpg"},
 "L22": {"level":"level 22","places":{"YB":{"has":["yellow"],"exits":[{"to":"J","via":["Y"]}]},"BB":{"has":["blue"],"exits":[{"to":"J","via":["B"]}]},"J":{"exits":[{"to":"cup:blue","via":["D"]},{"to":"cup:yellow","via":[]}]}},"pins":{"Y":[280,490],"B":[360,490],"D":[312,767]},"verified":[["Y","D","B"]],"src":"raw/com.maroieqrwlk.unpin/20261001-160324-chrono-2FYKPJ/shots/00061.jpg"},
 "L23-s1": {"level":"level 23 stage 1","stage":"1/4","places":{"TL":{"has":["grey"],"exits":[{"to":"M","via":["S"]}]},"TR":{"has":["colour"],"exits":[{"to":"M","via":["S"]}]},"M":{"has":["grey"],"exits":[{"to":"cup","via":["XA","XB"]},{"to":"R","via":["XB"]},{"to":"LZ","via":["XA"]}]},"R":{"has":["grey"],"exits":[{"to":"cup","via":["XA"]}]},"LZ":{"exits":[{"to":"cup","via":["XB"]}]}},"pins":{"V":{"at":[365,300],"joins":[["TL","TR"]]},"S":[175,520],"XA":[163,563],"XB":[557,560]},"verified":[["V","S","XB","XA"]],"src":"raw/com.maroieqrwlk.unpin/20261001-160324-chrono-2FYKPJ/shots/00077.jpg"},
 "L23-s2": {"level":"level 23 stage 2","stage":"2/4","places":{"CT":{"has":["colour"],"exits":[{"to":"LEFT","via":["TL"]},{"to":"RIGHT","via":["TR"]}]},"LEFT":{"has":["colour"],"exits":[{"to":"cup","via":["BL"]}]},"RIGHT":{"has":["colour"],"exits":[{"to":"cup","via":["BR"]}]}},"pins":{"TL":[243,405],"TR":[458,405],"BL":[142,772],"BR":[572,772]},"verified":[["TL","TR","BL","BR"]],"src":"raw/com.maroieqrwlk.unpin/20261001-162240-chrono-2FYKPJ/shots/00006.jpg"},
 "L23-s3": {"level":"level 23 stage 3","stage":"3/4","places":{"PL":{"has":["colour"],"exits":[{"to":"G1","via":["V"]}]},"G1":{"has":["grey"],"exits":[{"to":"G3","via":["S"]}]},"G2":{"has":["grey"],"exits":[{"to":"G3","via":["S"]}]},"G3":{"has":["grey"],"exits":[{"to":"BOT","via":["D"]}]},"LB":{"has":["bomb"],"exits":[{"to":"BOT","via":["V"]}]},"BOT":{"has":["bomb"],"exits":[{"to":"cup","via":["F"]}]}},"pins":{"V":[290,392],"T":{"at":[537,397],"joins":[["G1","G2"]]},"S":[603,572],"D":[512,755],"F":[478,828]},"verified":[["V","T","S","D","F"]],"src":"raw/com.maroieqrwlk.unpin/20261001-162240-chrono-2FYKPJ/shots/00008.jpg"},
 "L23-s3-resumed": {"level":"level 23 stage 3 resumed","stage":"3/4","places":{"PL":{"has":["colour"],"exits":[{"to":"G","via":["V"]}]},"G":{"has":["grey"],"exits":[{"to":"BOT","via":["D"]}]},"LB":{"has":["bomb"],"exits":[{"to":"BOT","via":["V"]}]},"BOT":{"has":["bomb"],"exits":[{"to":"cup","via":["F"]}]}},"pins":{"V":[290,392],"T":[537,397],"D":[512,755],"F":[478,828]},"verified":[["V","D","F"]],"src":"raw/com.maroieqrwlk.unpin/20261001-162240-chrono-2FYKPJ/shots/00064.jpg"},
 "L23-s4": {"level":"level 23 stage 4","stage":"4/4","places":{"TOPG":{"has":["grey"],"exits":[{"to":["CL","RP"],"via":["S"]}]},"PLEFT":{"has":["colour"],"exits":[{"to":"CL","via":["DL"]}]},"CL":{"has":["grey"],"exits":[{"to":"cup","via":["L"]}]},"RP":{"has":["colour"],"exits":[{"to":"cup","via":["DR"]}]}},"pins":{"L":[500,445],"S":[618,645],"DL":[203,835],"DR":[498,845]},"verified":[["S","DR","DL","L"],["DL","S","L","DR"]],"src":"raw/com.maroieqrwlk.unpin/20261001-162240-chrono-2FYKPJ/shots/00078.jpg"},
 "L24": {"level":"level 24","places":{"POP":{"has":["colour"],"exits":[{"to":"RG","via":["V"]},{"to":"HL","via":["D"]}]},"RG":{"has":["grey"],"exits":[{"to":"HR","via":["D"]}]},"HL":{"has":["grey"],"exits":[{"to":"BL","via":["H"]}]},"HR":{"exits":[{"to":"BRZ","via":["H"]}]},"BL":{"has":["bomb"],"exits":[{"to":"cup","via":["F"]}]},"BRZ":{"has":["bomb"],"exits":[{"to":"BL","via":["V"]}]}},"pins":{"V":{"at":[385,305],"joins":[["HL","HR"]]},"D":[195,390],"H":[607,622],"F":[162,840]},"verified":[["V","D","H","F"]],"src":"raw/com.maroieqrwlk.unpin/20261001-164104-chrono-2FYKPJ/shots/00027.jpg"},
 "L25": {"level":"level 25","places":{"BALLS":{"has":["colour"],"exits":[{"to":"CH","via":["TOP"]}]},"CH":{"exits":[{"to":"cup","via":["BOT"]}]}},"pins":{"TOP":[400,467],"BOT":[385,908]},"verified":[["BOT","TOP"]],"src":"raw/com.maroieqrwlk.unpin/20261001-164104-chrono-2FYKPJ/shots/00040.jpg"},
 "L26": {"level":"level 26","places":{"BALLS":{"has":["colour"],"exits":[{"to":"cup","via":["P"]}]}},"pins":{"P":[440,545]},"verified":[["P"]],"src":"raw/com.maroieqrwlk.unpin/20261001-164104-chrono-2FYKPJ/shots/00047.jpg"},
 "L27": {"level":"level 27","places":{"TOPB":{"has":["bomb"],"exits":[{"to":"CEN","via":["T"]}]},"CEN":{"has":["bomb"],"exits":[{"to":"cup","via":["F"]}]},"G":{"has":["grey"],"exits":[{"to":"CEN","via":["V"]}]},"COL":{"has":["colour"],"exits":[{"to":"CEN","via":["C"]}]}},"pins":{"T":[515,410],"C":[533,755],"V":[292,843],"F":[500,833]},"verified":[["T","C","V","F"]],"src":"raw/com.maroieqrwlk.unpin/20261006-061608-chrono-2FYKPJ/shots/00044.jpg"},
 "L27-after-T": {"level":"level 27 after T","places":{"CEN":{"exits":[{"to":"cup","via":["F"]}]},"G":{"has":["grey"],"exits":[{"to":"CEN","via":["V"]}]},"COL":{"has":["colour"],"exits":[{"to":"CEN","via":["C"]}]}},"pins":{"C":[539,745],"V":[297,830],"F":[507,823]},"verified":[["C","V","F"]],"src":"raw/com.maroieqrwlk.unpin/20261006-061608-chrono-2FYKPJ/shots/00046.jpg"},
 "L28": {"level":"level 28","places":{"SHL":{"has":["grey"],"exits":[{"to":"MID","via":["S"]}]},"SHR":{"has":["colour"],"exits":[{"to":"MID","via":["S","T"]},{"to":"B1","via":["S"]}]},"B1":{"has":["bomb"],"exits":[{"to":"MID","via":["T"]}]},"MID":{"has":["bomb"],"exits":[{"to":"NECK","via":["L"]}]},"NECK":{"has":["grey"],"exits":[{"to":"cup","via":["F"]}]}},"pins":{"T":[328,412],"S":[618,528],"L":[112,596],"F":[474,770]},"verified":[["T","S","L","F"]],"src":"raw/com.maroieqrwlk.unpin/20261006-091133-chrono-2FYKPJ/shots/00004.jpg"},
 "L29": {"level":"level 29","places":{"TOP":{"has":["colour"],"exits":[{"to":"MAZE","via":["T"]}]},"MAZE":{"exits":[{"to":"cup","via":["B"]}]}},"pins":{"T":[554,498],"B":[470,918]},"waits":{"B":6},"verified":[["T","B"]],"src":"raw/com.maroieqrwlk.unpin/20261006-091133-chrono-2FYKPJ/shots/00051.jpg"},
 "L30": {"level":"level 30","places":{"TL":{"has":["grey"],"exits":[{"to":"ML","via":["H1"]}]},"TM":{"has":["grey"],"exits":[{"to":"MM","via":["H1"]}]},"TR":{"has":["grey"],"exits":[{"to":"RS","via":["H1"]}]},"ML":{"has":["grey"],"exits":[{"to":"BL","via":["H2"]}]},"MM":{"has":["colour"],"exits":[{"to":"BM","via":["H2"]}]},"RS":{"has":["grey"],"exits":[{"to":"CH","via":["DR","H2"]},{"to":"MM","via":["DR"]}]},"BL":{"has":["grey"]},"BM":{"has":["grey"],"exits":[{"to":"CH","via":["DR"]}]},"CH":{"exits":[{"to":"cup","via":[]}]}},"pins":{"H1":[592,462],"H2":[118,618],"DL":{"at":[272,364],"joins":[["TL","TM"],["ML","MM"],["BL","BM"]]},"DR":{"at":[442,362],"joins":[["TM","TR"]]}},"verified":[["H1","H2","DL","DR"]],"src":"raw/com.maroieqrwlk.unpin/20261006-091133-chrono-2FYKPJ/shots/00069.jpg"},
 "L31-s1": {"level":"level 31 stage 1","stage":"1/4","places":{"BOMB":{"has":["bomb"],"exits":[{"to":"COL","via":["TP"]}]},"COL":{"has":["colour"],"exits":[{"to":"G","via":["S"]}]},"G":{"has":["grey"],"exits":[{"to":"cup","via":["F"]}]}},"pins":{"TP":[118,518],"S":[518,720],"F":[230,770]},"verified":[["S","F"]],"src":"raw/com.maroieqrwlk.unpin/20261006-113518-chrono-2FYKPJ/shots/00009.jpg"},
 "L31-s2": {"level":"level 31 stage 2","stage":"2/4","places":{"GT":{"has":["grey"],"exits":[{"to":"CL","via":["D"]}]},"B1":{"has":["bomb"],"exits":[{"to":"B2Z","via":["BP"]}]},"CL":{"has":["colour"],"exits":[{"to":"BOT","via":["H"]}]},"B2Z":{"has":["bomb"],"exits":[{"to":"BRB","via":["H"]}]},"BOT":{"has":["grey"],"exits":[{"to":"cup","via":["F"]}]},"BRB":{"exits":[{"to":"cup","via":["F"]}]}},"pins":{"V":{"at":[370,398],"joins":[["CL","B2Z"],["BOT","BRB"]]},"BP":[426,452],"D":[116,718],"H":[548,678],"F":[476,806]},"verified":[["BP","D","H","F"]],"src":"raw/com.maroieqrwlk.unpin/20261006-113518-chrono-2FYKPJ/shots/00015.jpg"},
 "L31-s3": {"level":"level 31 stage 3","stage":"3/4","places":{"TL":{"has":["grey"],"exits":[{"to":"SH","via":["A"]}]},"TR":{"has":["grey"],"exits":[{"to":"SH","via":["B"]}]},"SH":{"has":["grey"],"exits":[{"to":"COL","via":["C","D"]},{"to":"GL","via":["C"]}]},"GL":{"has":["grey"],"exits":[{"to":"COL","via":["D"]}]},"COL":{"has":["colour"],"exits":[{"to":"cup","via":["F"]}]}},"pins":{"A":[310,388],"B":[562,566],"C":[160,638],"D":[610,594],"F":[516,822]},"verified":[["D","B","A","C","F"]],"src":"raw/com.maroieqrwlk.unpin/20261006-113518-chrono-2FYKPJ/shots/00021.jpg"},
 "L31-s4": {"level":"level 31 stage 4","stage":"4/4","places":{"TB":{"has":["bomb"]},"RB":{"has":["bomb"],"exits":[{"to":"?","via":["T2"]}]},"GR":{"has":["grey"],"exits":[{"to":"BC","via":["X"]}]},"BL":{"has":["grey"],"exits":[{"to":"cup","via":["F"]}]},"BC":{"has":["colour"]}},"pins":{"V":{"at":[346,298],"joins":[["TB","RB"],["BL","BC"]]},"T2":[596,398],"X":[550,814],"F":[130,830]},"verified":[["V","X","F"]],"src":"raw/com.maroieqrwlk.unpin/20261006-113518-chrono-2FYKPJ/shots/00024.jpg"},
 "L32": {"level":"level 32","places":{"COL":{"has":["colour"],"exits":[{"to":"LOW","via":["S","BD"]},{"to":"MID","via":["S"]}]},"MID":{"has":["grey"],"exits":[{"to":"LOW","via":["BD"]}]},"GR":{"has":["grey"]},"LOW":{"has":["grey"],"exits":[{"to":"cup","via":["LD"]}]}},"pins":{"S":[112,552],"V":{"at":[443,390],"joins":[["MID","GR"]]},"BD":[550,798],"LD":[136,818]},"verified":[["S","V","BD","LD"]],"src":"raw/com.maroieqrwlk.unpin/20261006-145232-chrono-2FYKPJ/shots/00003.jpg"},
 "L33": {"level":"level 33","places":{"TOP":{"has":["colour"],"exits":[{"to":["MIDC","RP"],"via":["T"]}]},"MIDC":{"exits":[{"to":"cup","via":["K1"]}]},"RP":{"exits":[{"to":"MIDC","via":["K2"]}]}},"pins":{"T":[286,468],"K1":{"swipe":[330,800,190,835]},"K2":{"swipe":[553,620,350,592]}},"waits":{"K1":5,"K2":4},"verified":[["T","K1","K2"]],"src":"raw/com.maroieqrwlk.unpin/20261006-145232-chrono-2FYKPJ/shots/00024.jpg"},
 "C1": {"level":"challenge 1","scrolling":true,"height":2300,"max_moves":10,"places":{"TOP":{"has":["colour"],"exits":[{"to":"S2Z","via":["T"]}]},"DG":{"has":["grey"],"exits":[{"to":"S2Z","via":["D1"]}]},"S2Z":{"has":["grey"],"exits":[{"to":"S3Z","via":["S2"]}]},"PL":{"has":["bomb"],"exits":[{"to":"?","via":["BL"]}]},"PR":{"has":["bomb"],"exits":[{"to":"?","via":["BR"]}]},"S3Z":{"has":["grey"],"exits":[{"to":"BOT","via":["S3","X","L","M","S4"]},{"to":"?","via":["S3"]}]},"XB":{"has":["bomb"],"exits":[{"to":"MB","via":["X"]}]},"MB":{"has":["bomb"],"exits":[{"to":"BOT","via":["M"]}]},"TRI":{"has":["grey"],"exits":[{"to":"BOT","via":["TD"]},{"to":"out","via":["TV"]}]},"BOT":{"has":["grey"],"exits":[{"to":"cup","via":["J"]}]}},"pins":{"T":[596,503],"D1":[370,652],"S2":[611,1026],"BR":[618,1138],"BL":[132,1162],"S3":[602,1423],"S4":[602,1463],"L":[110,1575],"X":[312,1581],"M":[155,1699],"TD":{"at":[616,1855],"tap":[631,1852]},"TV":[594,1889],"J":[506,2076]},"views":{"TOP":0,"S2Z":474,"S3Z":850,"BOT":1221},"together":[["T","D1"]],"plan":["T","D1","X","S2","S4","L","M","S3","TD","J"],"verified":[],"src":"raw/com.maroieqrwlk.unpin/20261006-030951-chrono-2FYKPJ/shots/00009.jpg"},
 "IQ1": {"level":"Sketchman IQ Test level 1","places":{"TOP":{"has":["colour"],"exits":[{"to":"C00","via":["T"]}]},"C00":{"exits":[{"to":"?","via":["L1","R1"]},{"to":"C10","via":["L1"]},{"to":"C01","via":["R1"]}]},"C01":{"exits":[{"to":"?","via":["L1","R2"]},{"to":"C11","via":["L1"]},{"to":"C02","via":["R2"]}]},"C02":{"exits":[{"to":"out","via":["L1"]},{"to":"out","via":["R3"]}]},"C10":{"exits":[{"to":"?","via":["L2","R1"]},{"to":"C20","via":["L2"]},{"to":"C11","via":["R1"]}]},"C11":{"exits":[{"to":"?","via":["L2","R2"]},{"to":"cup","via":["L2"]},{"to":"out","via":["R2"]}]},"C20":{"exits":[{"to":"?","via":["L3","R1"]},{"to":"out","via":["L3"]},{"to":"cup","via":["R1"]}]}},"pins":{"T":[466,705],"L1":[248,829],"L2":[212,890],"L3":[179,954],"R1":[482,828],"R2":[520,888],"R3":[556,950]},"verified":[],"src":"raw/com.maroieqrwlk.unpin/20261005-230946-chrono-2FYKPJ/shots/00005.jpg"}
}'''
LIBRARY = json.loads(LIBRARY_JSON)
# scrolling levels (taller than the screen, level pixels) are placed in the level frame by frame, never matched
# as a screen
SCROLLING = {k: v for k, v in LIBRARY.items() if v.get("scrolling") and v.get("height")}
LIBRARY = {k: v for k, v in LIBRARY.items() if k not in SCROLLING}
