---
game: com.king.candycrushsaga
title: "How to play"
type: agent
version_seen: 1.335.1.2
verified_at: 2026-10-02
sources: [20261001-202316-chrono-2FYKPJ, 20261001-232021-chrono-2FYKPJ]
---

# How to play: Candy Crush Saga

The player reads this before every level and works in the local copy
`state/com.king.candycrushsaga/playbook.md`; the dream merges it here. Level times: `sw.py playbook`.
Every board seen so far is in the [level catalog](../levels.md).

## core-match: classic match-3 (swap adjacent candies)

- Goal: the order in the top panel (level 1: collect 40 blue; levels 2-4: meringue, level 4 also 50
  green; levels 5-6: jelly). The big number top left is the moves left; the small "N / heart-infinity"
  next to it is the level number, not a life count [s:20261001-202316-chrono-2FYKPJ#5] [s:20261001-232021-chrono-2FYKPJ#33].
- Controls: swipe a candy into an adjacent cell. A swap that makes no line of 3+ is undone, also for a
  fish or striped candy swapped with a plain candy [s:20261001-232021-chrono-2FYKPJ#32].
- Rules:
  - Specials: 4 in a line = striped, L/T = wrapped, 5 in a line = colour bomb, 2x2 square = fish
    [s:20261001-202316-chrono-2FYKPJ#27].
  - Meringue (white 1 layer, pink 2 layers) loses a layer from a match next to it and from a
    neighbour cleared by a colour bomb; cells under meringue do not refill until it is gone
    [s:20261001-202316-chrono-2FYKPJ#31].
  - Jelly clears only under a candy that is matched or blasted; double jelly needs two hits
    [s:20261001-232021-chrono-2FYKPJ#42] [s:20261001-232021-chrono-2FYKPJ#52].
  - When the order is done with moves left, Sugar Crush spends the rest by itself (~10 s)
    [s:20261001-202316-chrono-2FYKPJ#11].
- Risks: every move is risky (random cascade and refill): one move per frame.
- Method: manual (heuristic). Prefer, in order: a colour bomb swapped with the order colour (or with
  the colour sitting on the remaining jelly); moves that make a 5-line, an L/T, a 4-line; moves that
  hit the order; moves low on the board (more cascades). Fire specials together by matching them with
  same-colour candies [s:20261001-202316-chrono-2FYKPJ#18] [s:20261001-232021-chrono-2FYKPJ#52].
- Level plan:
  - Meringue: clear from the top edge of a block downwards; a 3-match on the row right above the
    meringue hits three tiles [s:20261001-202316-chrono-2FYKPJ#13-17].
  - Jelly: look for swaps that bring a same-colour neighbour into a jelly row or column; save the
    bomb for the colour on the leftover jelly cells [s:20261001-232021-chrono-2FYKPJ#42].
  - Level 4: bombs come from the dispenser on the top row; swap each with green
    [s:20261001-232021-chrono-2FYKPJ#32].
- Frame grids (730x1583 frame): level 1 (8 wide) x = 92+78c, y = 512+85r; levels 3 and 5 (7 wide)
  x = 130+78c (level 5 y = 555+85r); levels 4 and 6 (9 wide) x = 52+78c (level 6 y = 467+85r).
- Pitfalls:
  - The frame right after a move shows the old board or a cascade: `taps "!move"`, then `wait 3`
    (after big combos `sleep 6` + `wait 3`) before reading. Re-sending a move on a stale frame
    repeated the same swap twice on level 4 [s:20261001-202316-chrono-2FYKPJ#8] [s:20261001-232021-chrono-2FYKPJ#16-21].
  - Level 4 lost ~4.5 min to repeated and no-change moves and an `ask` (47 s); when a move "changes
    nothing", re-read the board once instead of asking [s:20261001-232021-chrono-2FYKPJ#21-22].
- Move cost: ~20-30 s per move with the wait and one frame read; a level needing more than ~12 moves
  goes over the 5-min budget, so look for specials first to cut the move count.

### Level times (sw.py playbook, 2026-10-02)

Status mastered, method manual, 6 won / 0 lost; typical 4.3 min, best 2.6 min (budget 5 min).

| Level | Order | Moves used | Time | Model | Source |
|---|---|---|---|---|---|
| 1 | 40 blue / 28 | 6 | 156 s | opus | [s:20261001-202316-chrono-2FYKPJ#11] |
| 2 | 25 meringue / 25 | 6 | 183 s | opus | [s:20261001-202316-chrono-2FYKPJ#18] |
| 3 | 50 meringue layers / 25 | 13 | 383 s | opus | [s:20261001-202316-chrono-2FYKPJ#31] |
| 4 | 65 meringue + 50 green / 25 | 17 | 526 s | sonnet | [s:20261001-232021-chrono-2FYKPJ#32] |
| 5 | 21 jelly / 15 | 10 | 256 s | sonnet | [s:20261001-232021-chrono-2FYKPJ#42] |
| 6 | 58 jelly / 25 | ~8 | 258 s | sonnet | [s:20261001-232021-chrono-2FYKPJ#52] |

What made levels fast: an early colour bomb on the order colour (levels 1, 2, 6). What made them slow:
many plain matches on meringue (level 3) and repeated moves on stale frames (level 4).

## Dream 2026-10-04: corrections (1.337.0.2)

- The HUD "N/♥M" shows the level and the LIVES ("1/♥5", "4/♥4"), not unlimited lives; quitting and force-stopping each cost a life [s:20261003-194350-chrono-2FYKPJ#3] [s:20261003-225003-chrono-2FYKPJ#50] [s:20261003-230937-chrono-2FYKPJ#12].
- There IS a win screen ("Level completed", crown, stars): after the winning move `shot` every 1-2 s; a `wait 15` misses it [s:20261003-225003-chrono-2FYKPJ#43].
- No Restart inside a level: Quit level (costs a life and the starting boosters) and replay from the map [s:20261003-230937-chrono-2FYKPJ#10] [s:20261003-225003-chrono-2FYKPJ#48].
- Colour bomb: make a 5-line of the order colour, then swap the bomb with that colour (L1 in 3 moves; L4 65 -> 24 meringue in one move) [s:20261003-194350-chrono-2FYKPJ#6] [s:20261003-225003-chrono-2FYKPJ#46].
- Test top-bar icons from the Map tab, not from the Shop tab [s:20261003-194350-chrono-2FYKPJ#23]. Bottom bar at y about 1500: Map 73, Events 218, Social 365, Pins 510, Shop 655 (x=437 is a boundary) [s:20261003-230937-chrono-2FYKPJ#2].

| Level | Result | Seconds | Source |
|---|---|---|---|
| 1 | won (3 moves) | 92 | [s:20261003-194350-chrono-2FYKPJ#6] |
| 2 | won | 294 | [s:20261003-225003-chrono-2FYKPJ#25] |
| 3 | won (one `ask`) | 500 | [s:20261003-225003-chrono-2FYKPJ#43] |
