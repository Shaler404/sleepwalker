---
game: com.oakever.arrows
title: "How to play"
type: agent
version_seen: 1.31.0
verified_at: 2026-10-02
sources: [20261001-204000-chrono-2FYKPJ]
---

# How to play: Amaze GO!

The player reads this before every level and works in the local copy
`state/com.oakever.arrows/playbook.md`; the dream merges it here. Level times: `sw.py playbook`.
Positions are in the 730x1583 frame.

## arrows-escape: Tap arrows so they slide off the board
- Goal: clear every arrow from the board. 0 mistakes gives 3 stars and "Flawless!" [s:20261001-204000-chrono-2FYKPJ#4].
- Controls: tap any segment of an arrow; it slides out along its head direction, the body following
  its own path. The board is a dot grid, about 45 px per cell (levels 1-3: 5x5, centred near y 800)
  [s:20261001-204000-chrono-2FYKPJ#21].
- Rules: an arrow leaves only if no other arrow lies on the straight line from its head to the board
  edge. 3 blue drops at the top left are the mistake allowance; what a blocked tap costs is not
  verified yet (experiment `lives-mistake`) [s:20261001-204000-chrono-2FYKPJ#21].
- Risks: tapping a blocked arrow (probably costs a drop). Taps on free arrows are safe and can be
  batched.
- Method: manual. Levels 1-3 took 0.4-0.7 min. The status "mastered" was set on tutorial-sized boards
  only; for larger boards a solver from the dot grid will probably be worth it [s:20261001-204000-chrono-2FYKPJ#8].
- Level plan: list the arrows whose head faces open space (usually the outer ones) and tap them in one
  batch; take a frame; then tap the arrows they freed [s:20261001-204000-chrono-2FYKPJ#4] [s:20261001-204000-chrono-2FYKPJ#7] [s:20261001-204000-chrono-2FYKPJ#20].
- Pitfalls:
  - A tap sent while the previous arrow is still sliding can be ignored: check the frame after a
    batch and re-tap what is left [s:20261001-204000-chrono-2FYKPJ#7] [s:20261001-204000-chrono-2FYKPJ#8].
  - The hit-box is generous: a tap between two arrows can move the neighbour instead. To hit one
    arrow, tap the middle of a segment with no other arrow within one cell [s:20261001-204000-chrono-2FYKPJ#21].
  - The result screen's Next Level appears about 3 s after the win; a tap before it does nothing
    [s:20261001-204000-chrono-2FYKPJ#5] [s:20261001-204000-chrono-2FYKPJ#6].

### Level times
| Levels | Result | Logged | In-game timer | Model | Source |
|---|---|---|---|---|---|
| 1 (tutorial) | won, Flawless | 24 s | 00:11 | opus | [s:20261001-204000-chrono-2FYKPJ#4] |
| 2 | won, Flawless | 24 s | 00:12 | opus | [s:20261001-204000-chrono-2FYKPJ#8] |
| 3 | won, Flawless | 44 s (includes the lives experiment) | 00:25 | opus | [s:20261001-204000-chrono-2FYKPJ#22] |

Median 0.4 min against a 5 min budget. Boards of levels 1-3: [levels.md](../levels.md).

## Notes 20261003-232357
- L3-L4 normal boards: free arrows first; blocked tap costs 1 drop (3 total) and arrow flashes red; L4 won Perfect with 1 mistake. Win screen: Flawless (0 mistakes)/Perfect.
- L5 is "Hard" (purple, also L8): board larger than screen, "Pinch to zoom" tip, hint bulb button. Not played: needs strong model (zoom/pan handling, solver).
- In-level gear = Sound/Vibration/Music/Zen + Restart. Back arrow quits instantly (no confirm).
- 20261004: Hard L5 won via hint loop (hint=free green free-arrow, tap it). Write real solver later.

## Dream 2026-10-04: Hard levels (1.33.0)

- A blocked tap costs one drop and the arrow turns red; at 0 drops "Out of Lives" offers a free Continue (board kept) or Restart (board reset) [s:20261003-233756-chrono-2FYKPJ#4-5] [s:20261003-233756-chrono-2FYKPJ#23].
- Hard levels (L5, L8, L10; L5 is about 3 screens wide, but L8 and L10 fit the screen at 35 px and 23.6 px pitch [s:20261005-012010-chrono-2FYKPJ#16] [s:20261005-012010-chrono-2FYKPJ#21]): play the hint loop: bulb (665,212), wait about 2 s for the pan, tap the green arrow. The hint is free (about 55 uses on L5). ⚠️ Previously: "never batch blind taps on a Hard board" (that gave 4 Out of Lives in one session); the solver now sends up to 14 free-ray taps per round on Hard boards, see the dream report's solver note [s:20261003-233756-chrono-2FYKPJ#6-22] [s:20261004-001551-chrono-2FYKPJ#2-108].
- If a bulb tap leaves the frame unchanged, the green arrow is off-screen: find the green edge pixel and swipe toward it [s:20261004-001551-chrono-2FYKPJ#84-92]. Do not `shot` after a tap that already returns a frame [s:20261004-001551-chrono-2FYKPJ#13].
- To speed up (untested): in each hint frame also tap the other arrows that are visibly free (task make-hard-fast) [s:20261004-001551-chrono-2FYKPJ#61].
- After a win the Daily Streak screen can come before the win card; shoot the card only once Next Level and Home are visible (the score counts up: 895 -> 1194) [s:20261004-001551-chrono-2FYKPJ#110].
- Run destructive outcome cases (Restart, force-stop) after the win or on an early board, never mid-attempt on the progress gate [s:20261003-233756-chrono-2FYKPJ#23-24].

| Level | Result | Seconds | Source |
|---|---|---|---|
| 3 | won, Flawless | 35 | [s:20261003-232357-chrono-2FYKPJ#11] |
| 4 | won, Perfect (1 mistake) | 105 | [s:20261003-232357-chrono-2FYKPJ#17] |
| 5 Hard | won by the hint loop, Great Start! 1194 | 863 (13:15) | [s:20261004-001551-chrono-2FYKPJ#110] |

## Solver 20261005-010045 (arrows-escape, Hard)
- `state/com.oakever.arrows/solvers/arrows-escape.py` won Hard L5 with no hints and no drop lost (3 drops at the end), 2 stars, 05:54 in-game, score 1300 [s:20261005-010045-chrono-2FYKPJ#91].
- Run it as `solve arrows-escape --run --rounds 1 --settle 2.0`, one round per call once the level is over 5 min (the harness stops `--run` after each round then). `--settle 2.0` is needed: a 1 s frame catches the fling still moving.
- How it works: phase 1 maps the board by swipes (solver memory: nodes A/D/E, edges, heads in global node coords; every frame is registered by the integer node offset with the best agreement; cells that ever held an arrow never change, arrows only turn into dots). Phase 2 extracts the arrows (paths with one head), checks the whole board clears by ordered removal, then taps the free arrows in view plus the ones they free (up to 14 per round), or pans toward the nearest free arrow.
- Board physics: a 300 ms swipe moves the board about 2x its length (FLING = 2); pushing the view far past the board's end snaps it back to the start view, so exploration aims the unseen edge at 30% of the screen, not the centre.
- Cost on Hard L5: ~47 explore rounds (many lost to map restarts while the fling and snap-back were learned) + ~38 tap/pan rounds. With the fixes, expect about 10 explore pans on a 50-column board.
- ⚠️ Previously (superseded: the solver won L6, L7, Hard L8, L9 and Hard L10 with 3 stars in 20261005-012010 [s:20261005-012010-chrono-2FYKPJ#3] [s:20261005-012010-chrono-2FYKPJ#9] [s:20261005-012010-chrono-2FYKPJ#16] [s:20261005-012010-chrono-2FYKPJ#20] [s:20261005-012010-chrono-2FYKPJ#29]): not working yet on normal boards from level 6: the pitch differs per level (about 61 px on L6; the solver now searches it), several heads are missed at that pitch, and the new bottom-right grid button (guideline toggle) reads as arrow nodes (task solver-normal-levels).
- Hard win card: 2 stars, "Great Start!" even with 3 drops left (exp-hard-stars).
- Level 6 adds a bottom-right grid button: the guideline, light tan lines along every arrow's exit ray. Turn it off before solving (the solver would read the lines as dots).

## Lab 2026-10-05 (arrows-escape, normal boards)
- Method: solver on every level, normal and Hard. Normal boards (L6 on) fit the screen: `solve arrows-escape --run --rounds 3` with no hand taps; the solver reads the whole board in one frame (pitch searched and refined per frame, guideline button masked) and taps up to 14 free arrows per round. L6 (28 arrows) cleared in 2 rounds, 3 stars [s:20261005-012010-chrono-2FYKPJ#2-3]. Hard boards: as in the Solver section above (`--rounds 1 --settle 2.0`).
- The solver now returns no moves unless the level header's divider line is on screen (`header line` < 0.9 in its note): home, settings, the theme popup, Rate Us, the win card, Daily Streak and Out of Lives. Before, the home screen passed its background test and got an explore swipe.
- Pitfalls:
  - Do not place moves by hand when the solver gives none: read its note. "not a level board" means a popup is on top (close it, then solve); "misread components" or "can never leave" means a reading problem: take `shot`, run `solve` once more, and if it repeats, note the shot number for the lab instead of tapping by hand.
  - The "Pinch to zoom" tip on Hard starts sits over the board and reads as dots: the first explore swipe is still safe (no taps are sent while exploring).

## Solver 20261005-012010 (normal and Hard boards)
- `solve arrows-escape --run --rounds 10 --settle 2.0` now wins normal boards and a Hard board that fits the screen: L6 (28 arrows, 2 rounds, 1.8 min), L7 (54 arrows, 4 rounds, 1.7 min), Hard L8 (78 arrows, 6 rounds, 2.8 min), all 3 stars, 0 mistakes, no hints.
- Fixes: pitch searched from 26 px (⚠️ the solver code searches from 16 px; L10 needed 23.6 px [s:20261005-012010-chrono-2FYKPJ#21]) (L8 Hard fit the screen at 35 px, L7 46 px, L6 61 px at 1080) and refined to 0.05 px (a 0.25 px error drifts 3-4 px across the board and loses head tips); head tip probe at 0.15 pitch (the triangle tip is only ~0.23 pitch ahead of the head node, its base ~0.28 behind); the guideline button (white disc bottom right) is masked and its nodes left unobserved.
- Leave the guideline off. Wait ~4 s after the run before reading the win card; after the L6 win a Rate Us popup covered it (close X at 609,483).

## Lab 2026-10-05 (2): chain limit and sparse-board pitch (after 20261005-224323)
- Method: solver, `solve arrows-escape --run --rounds 20` on every level (Hard boards that do not fit: `--rounds 1 --settle 2.0` as above). Expect about twice the rounds of before with the same taps (Hard L13 replay: 15 rounds instead of 6, about 3 min); a round now taps 3-14 arrows.
- What changed: a round no longer taps a long chain hanging on one free arrow. Each tap may have at most (drops left - 1) taps depending on it in the same round. Before, L16 tapped 1 free arrow plus 13 it freed, and lost all 3 drops twice on the same plan [s:20261005-224323-chrono-2FYKPJ#53] [s:20261005-224323-chrono-2FYKPJ#56]. The note shows `(N chained, drops D, chain budget B, H held for the next round)`.
- Why L16 failed is not known: the board was read right, and in the recorded rounds a chained tap works even 0.35 s after its blocker. If a drop is lost, the note says `DROP LOST (a -> b)` and lists the arrows tapped that did not leave (head node); chains then stay off for the level.
- Pitch: the solver keeps the first frame's pitch in its memory, and halves a pitch whose halfway points carry dots. Hard L15 resumed with a fresh memory on a half-cleared board now reads 39 arrows (before: pitch 52.55 instead of 26.3, "misread components") [s:20261005-224323-chrono-2FYKPJ#38].
- Pitfalls:
  - On `DROP LOST`, keep going with `solve --run`; write the shot number and the listed head nodes in the level note for the lab (the frame before that round shows the plan).
  - The second Out of Lives in a session wants an ad for Continue [s:20261005-224323-chrono-2FYKPJ#53]: do not let a drop go on experiments when a level is still to be played.

## Session 20261005-233140 (opus): chained taps off
- L16 (55 arrows, normal, gold league arrows) lost 2 drops in round 4 with the chain budget 2: the first tap of the round, on an arrow that WAS free, was ignored by the game (no red, no drop), and the two taps chained behind it hit blocked arrows (red, -1 drop each) [s:20261005-233140-chrono-2FYKPJ#8-9]. An ignored free tap is harmless; a chained tap behind it is not.
- Solver change: chain budget is always 0 (only arrows free on the current frame are tapped, re-checked every round). L16 rounds 5-17 lost nothing; ~17 rounds for 55 arrows, 3.6 min.
- After a normal win: Bronze League jump screen (Continue), then the win card, then an interstitial can start by itself ~3 s later; Android Back on its end card returns to the win card (no X after 45 s).
- L17 (normal, ~60 arrows) with chains off: 19 rounds, 0 drops lost by the solver [s:20261005-233140-chrono-2FYKPJ#40-48]. Ignored taps confirmed again: in a 2-tap batch the second tap was dropped while the first arrow flashed red.
- Deliberate Out of Lives for tests: 3 single taps on blocked arrows, one per call. The Continue is a 2-ad rewarded pod (~35 s), close with "X Reward granted" top left.

## Lab 2026-10-06 (3): toasts over the board (after 20261005-233140)
- Method: unchanged, solver on every level: `solve arrows-escape --run --rounds 20` (Hard boards that do not fit:
  `--rounds 1 --settle 2.0`). No hand taps, no wait before the first solve: the solver now handles the start toast.
- What changed: the game draws arrow-coloured toasts over the board: "65.16% players fail this level!" / "Pass this
  level and beat 74.59% of players!" for ~2 s at level start, and "Fastest today: N seconds!" with a confetti badge
  mid-level [s:20261005-233140-chrono-2FYKPJ#5] [s:20261005-224323-chrono-2FYKPJ#65]. They were read as arrows: a
  solve on the start toast stuck on "misread components" for every later call, and a mid-level toast left ~45 false
  nodes in the map ("mismatch 44-45" in every later note). The solver now masks them (note: `overlay masked`), and
  while a toast hides board nodes it sends one tap on empty page (note: `a toast covers N board nodes ... tap on
  empty page to wait for it`) instead of a swipe. That tap is on blank page far from every arrow and costs nothing.
- Pitfalls:
  - A note `map dropped: the next call reads the board afresh` after "misread components" (nothing tapped yet):
    just run `solve --run` again once the screen is still; if it repeats on a still board, note the shot for the lab.
  - The lab sign "solver gave up" also counts a `solve --run` stopped by Out of Lives or a menu ("not a level
    board"): close the popup before the next solve, and never solve on the win card.

## worms-escape: Countryside Caper event levels (session 20261006-013740)
- Board: the arrows-escape rules in a worm skin. Each worm is a chain of round beads (~23 px apart, cell ~46 px at 730 px)
  with an eyed head; it leaves along the direction neck -> head. Tapered ends are tails. 3 red hearts replace the drops;
  the hint bulb carries an AD badge. Green leafy background, no palette button.
- Method (lab 2026-10-06): solver. `solve worms-escape --run --rounds 20 --settle 1.5` on every event level, no
  hand taps. `arrows-escape` refuses worm boards ("not a level board") and `worms-escape` refuses arrow boards: pick
  the solver by the skin. The worms solver is the arrows solver with a worm reader: beads on nodes and halfway
  between connected nodes, eyes mark the head, vacated nodes show dots; pitch searched per level (L1 67.2 px at 1080,
  L2 zoomed out 46 px) and kept for the level. It taps only worms free on the current frame (L1 replay: 13 rounds,
  the same worms the hand play freed, mismatch 0 on every round). A board wider than the screen (L2 on first open)
  is mapped by pans first, like Hard boards: then use `--rounds 1 --settle 2.0` per call once the level is over 5 min.
- Manual fallback only if the note repeats "misread components" on a still board: for each head, look along its ray
  to the board edge; tap free worms in the middle of a long body segment, away from other worms.
- Pitfalls (solver):
  - Do not use the AD hint: its green exit line is read as a worm and gives "misread components" until it fades.
  - Event L2 is saved half-cleared after a quit: `Continue Level 2` opens it zoomed out to fit (whole board in one
    frame, 34 worms read); the solver needs no memory from before.
- Event L1 won by hand in 4.5 min (13 reads, 0 mistakes, 2 stars at 04:12). Grid: dots at x 70 + 46k, y 450 + 46k
  (14 x 17). Taps that worked: middle of a body bead run. Worms are long and wind across the board; one tap often
  frees a whole region. Send only worms free on the current frame; a worm freed by another tap goes in the next call.
- After the win: Daily Streak screen (event wins count), green win card, then an interstitial by itself.
- Event L2 is a big board (~28 x 28, wider than the screen on first open; after a quit and Continue it opens zoomed
  out to fit, beads ~16 px; the solver reads 20 x 23 nodes, 34 worms). Not attempted by hand: play it with the solver.
- Quit from an event level keeps the board (Continue Level N), so a long event board can be split across sessions.
- Hint on event boards: AD bulb only (each use = one rewarded ad, ~30-45 s); the hint pans to a free worm and draws
  a green exit line.

## Session 20261006-041006 (opus): L17-L19, Super Hard L20 seen
- L17 (normal): 21 rounds, 2.8 min; Hard L18 (fits the screen, ~21 px pitch): 52 rounds, 5.5 min, most rounds had only 1 free arrow; L19 (normal): 28 rounds, 3.1 min. All 0 mistakes, `solve arrows-escape --run --rounds 25 --settle 1.2`.
- Cost: every solver round is one session step. Hard L18 alone took 52 of 140 steps. Plan a session as about 25 steps per normal level and 55 per Hard level (task solver-step-cost).
- Super Hard L20 (red): a shaped (paw/mitten) board, ~17 px pitch at 730, ~150+ arrows, fits the screen. Not attempted yet: expect over 100 rounds at the current 1-free-per-round rate. Give it a session of its own.
- After every win this session: Silver League jump card (Continue) -> win card -> interstitial. Back closes some end cards; a Trivia playable ignored Back for 90 s, and `restart --after-win` kept the L19 win.

## Level times by mechanic (dream 2026-10-06)

```yaml
---
mechanics:
- id: arrows-escape
  name: arrows-escape
  status: broken
  method: solver
  solver: solvers/com.oakever.arrows/arrows-escape.py
  levels:
    won: 20
    lost: 2
    quit: 5
  typical_min: 5.0
  best_min: 0.6
  solver_file: solvers/com.oakever.arrows/arrows-escape.py
- id: worms-escape
  name: worms-escape
  status: studying
  method: solver
  solver: solvers/com.oakever.arrows/worms-escape.py
  levels:
    won: 1
    lost: 0
    quit: 2
  typical_min: 4.5
  best_min: 4.5
  solver_file: solvers/com.oakever.arrows/worms-escape.py
  solver_sign: 'solver bypassed: 3 of 3 levels placed by hand'
level_budget_min: 5
```
