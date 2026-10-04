---
game: com.block.juggle
title: "How to play"
type: agent
version_seen: 10.8.1
verified_at: 2026-10-04
sources: [20261001-200952-chrono-2FYKPJ, 20261001-230945-chrono-2FYKPJ, 20261003-193423-chrono-2FYKPJ, 20261003-212548-chrono-2FYKPJ, 20261003-235233-chrono-2FYKPJ]
---

# How to play: Block Blast!

The player reads this before every level and works in the local copy `state/com.block.juggle/playbook.md`;
the dream merges it here. Level times: `sw.py playbook`. Positions are in the 730x1583 model frame.

## classic: endless 8x8 block placement (the default mode on launch)
- Goal: endless. Points for placed cells and cleared rows/columns; the crown at the top left shows the
  best score and follows the current score live [s:20261001-230945-chrono-2FYKPJ#63]. The game ends
  only when no tray piece fits (game over not reached yet in two games).
- "Level": a classic game is played only for a goal (game over for study-classic, ads-cadence,
  look-monetization). A game played for score does not end within the 5-minute budget
  [s:20261001-200952-chrono-2FYKPJ#42] [s:20261001-230945-chrono-2FYKPJ#63].
- Controls: drag a piece from the tray (3 pieces at y~1210, x 152/365/578) onto the board. Pieces
  cannot be rotated (inferred). The tray refills only when all 3 pieces are placed
  [s:20261001-200952-chrono-2FYKPJ#5].
- Board geometry: 8x8, cells ~81 px, x 42..690, y 372..1020; cell (col c, row r) centre =
  (82+81c, 413+81r) [s:20261001-200952-chrono-2FYKPJ#12].
- Drag model (v10.6.5 fit; for v10.8.1 the lift is 2.4 cells = 195 px, see the next item): the piece moves faster than the finger (gain ~1.46) and floats above the touch point.
  To put the piece's bounding-box centre at board point (X, Y), swipe from a touch point (x0, y0) on a
  block of the tray piece to `finger_x = x0 + (X - x0) / 1.46`, `finger_y = y0 + (Y - y0 + 230) / 1.46`
  (lab fit on 53 placed drags of two sessions: gain 1.44-1.46, lift 2.84 cells = 230 px; most land
  within 0.1 cell; snapping tolerance about half a cell) [s:20261001-200952-chrono-2FYKPJ#12-14]
  [s:20261001-230945-chrono-2FYKPJ#19]. Checked: T to rows 2-3 (finger 365,960), 5-line to row 6
  (finger 244,1150), 3-line to row 4 cols 0-2 (finger 294,1040). The tutorial 2x2, drawn full size in
  the tray, worked with finger (365,960) for rows 3-4 [s:20261001-200952-chrono-2FYKPJ#5].
- Drag model v10.8.1 (lab 2026-10-03, screen recording of session 20261003-212548 + 73 landed drops):
  the lift is 2.4 cells, not 2.84: `finger_y = y0 + (Y - y0 + 195) / 1.46` (195 model px = 2.4 cells),
  gain 1.46 unchanged. A piece held at its tray touch point floats half under the board (centre 8.05
  cells down), so a drop to row 7 needs the finger about 0.55 cell (45 model px) ABOVE the touch point:
  for a 1-row tray piece at y~1210, finger y ~1165 lands it in row 7. The game rejects a drop only when
  the piece is off the board at release; the finger itself may end low (landed with it 1.72 cells under
  the board, row 7, session 20261003-193423). The old "finger more than 1.64 cells under the board is
  ignored" rule was the wrong lift: every row-7 drop the old solver sent held the piece under the board
  [s:20261003-212548-chrono-2FYKPJ#24].
- Where to touch: the lifted piece centres on the touch point wherever you touch it. Touch the middle
  of a filled block of the tray piece, never the bbox centre when it falls on an empty cell or a seam
  between blocks: such touches failed again and again (the same drop 13 times in a row) while every drag
  started on a block worked [s:20261001-230945-chrono-2FYKPJ#14-18] [s:20261001-230945-chrono-2FYKPJ#19]
  [s:20261001-230945-chrono-2FYKPJ#53].
- Vertical misses land a row short (lower): with the 2.4 lift aim 0.2 cell above the target centre (lab,
  2026-10-03; the old 0.3 with the 2.84 lift was in fact aiming 0.14 cell low, hence "one row low 4 times
  in 10"). Sideways it is not symmetric (lab 2026-10-04, replay of 156 solver drops of three sessions):
  leftward drags never missed with the aim 0.2 cell ahead (0 of 60), but rightward drags overshoot - 4 of
  65 landed one column RIGHT of the target with the 0.2 lead, all from slot 1 touched on a left block.
  Aim rightward drags 0.1 cell behind (left of) the target centre, leftward ones up to 0.2 ahead.
- Batches work: the step-9 `taps` batch failed only because its coordinates were wrong (lab replay:
  two drops ended 2+ cells under the board, one above it), not a harness gap
  [s:20261001-200952-chrono-2FYKPJ#9].
- Scoring (v10.6.5): 1 point per placed cell [s:20261001-200952-chrono-2FYKPJ#23]; one line about +10
  (a 3-cell piece clearing a row gave +13) [s:20261001-200952-chrono-2FYKPJ#23]; two lines with one
  piece +60 and "Good!" [s:20261001-200952-chrono-2FYKPJ#30]; the tutorial 2+2 lines gave +6 and
  "Excellent!" [s:20261001-200952-chrono-2FYKPJ#5]. The score probably counts up after a clear (not proven): one frame
  showed 201 with "+60" still on screen [s:20261001-200952-chrono-2FYKPJ#30]; read the
  score only once the count-up has finished. On 10.8.1 the tutorial clear gives +120 and the score counts
  up 4 -> 124 [s:20261003-193423-chrono-2FYKPJ#4].
  > ⚠️ Previously (v10.6.5, 2026-10-02): "the tutorial 2+2 lines gave +6" and "the 6 → 124 jump after the
  > tutorial is probably the same count-up (not proven)" [s:20261001-200952-chrono-2FYKPJ#7].
- Pieces seen: 1x1; lines of 2, 3, 4 and 5 (both directions); 2x2 and 3x3 squares; 3x3 L; small L; T;
  S/Z; 3x3 diagonal; ##/.#/.# [s:20261001-230945-chrono-2FYKPJ#25] [s:20261001-230945-chrono-2FYKPJ#40].
- Method: solver (`solvers/com.block.juggle/classic.py`, published 2026-10-04: Adventure levels 1-3 were
  won with it in score mode within the budget [s:20261003-235233-chrono-2FYKPJ#21] [s:20261003-235233-chrono-2FYKPJ#59]).
  > ⚠️ Previously (2026-10-02): "local draft, not published yet: no classic game has been finished within the budget". `sw.py solve classic` reads the board and the
  tray, searches every order and placement of the tray pieces (clears modelled, droppable placements
  only) and returns one swipe per piece with the drag model built in (touch on a block, aim up, sideways
  ahead on leftward drags and a little behind on rightward ones); `rescan` is always true (the refill is random). After a refill the first swipe is a warm-up
  pull (the piece goes back to the tray), then the real drags. Its memory bars a placement that did not
  drop, so a failed drop is not repeated (note "last round: ... did not drop (barred)"). One round =
  one tray. Since lab 2026-10-03 the default mode is gameover (fill the board, fewest clears; the note
  starts "[mode gameover]"): no `--board` file is needed. It reads the board from its dark frame line
  (the dot ring that appears from score ~319 had shifted the old lattice 0.1-0.2 cell), prefers
  placements that still land if the drop ends one row low, and says "GAME OVER" (done) on the "No Space
  Left" banner. Since lab 2026-10-03 (evening) it reaches row 7 (lift 2.4), refuses the glowing tray
  of a refill ("tray glow: the refill is animating": run again) and, when it retries a barred drop,
  touches another block of the piece; once every block has been tried it also aims 0.2 cell higher
  (0.4 after two cycles). The RETRY note says "slotN missed Kx, touch block B" and, from 4 misses on,
  "place it by hand from a tray block" (lab 2026-10-03, third pass).
- Level plan: start the level, `solve classic` once and open the drawn frame (the red circles must sit
  on tray blocks), then `solve classic --run --rounds 20` with no `--board`; when it stops, read its last
  note and run it again. "GAME OVER" (no tray piece fits, or the No Space Left banner) ends the level:
  `level end lost`, the score is the progress value. Only a task that needs a high score (beat the best,
  the dot ring) plays for score: a file with `{"mode": "score"}` passed once as `--board FILE` on the
  first `--run` of the level (the mode is kept in the solver memory; do not pass it on every call). A
  plain `solve` is a check and never writes the memory: a `--board` given there is lost (session
  20261003-235233: the next `--run` played gameover mode). The note's first word `[mode ...]` shows it.
- Play every placement through `solve --run`. Hand drags are for a piece the solver gives up on (RETRY
  with 4+ misses) only: a level placed by hand counts to the lab as a bypassed solver.
- Pitfalls:
  - Playing for score: game 1 ran 517 s and game 2 489 s with no game over, both quit; 724 points
    after ~45 placements and the board still open [s:20261001-200952-chrono-2FYKPJ#42]
    [s:20261001-230945-chrono-2FYKPJ#63]. Use the gameover mode when the goal is the end screen.
  - Solver retry loops (before the lab fix): the same plan on the same frame was sent 5, 11-12 and 7
    times in a row (~24 of 63 steps, ~2.5 min); only a hand drag started on a tray block broke them
    [s:20261001-230945-chrono-2FYKPJ#14-19] [s:20261001-230945-chrono-2FYKPJ#42-53]
    [s:20261001-230945-chrono-2FYKPJ#57-63]. If the note repeats the same plan twice on an unchanged
    frame, place that piece by hand at once.
  - The "same" flag is often true after a successful placement (a small change under the pHash
    threshold): read the frame, do not resend [s:20261001-200952-chrono-2FYKPJ#16]
    [s:20261001-200952-chrono-2FYKPJ#19] [s:20261001-200952-chrono-2FYKPJ#22].
  - Recompute the bbox of the piece before every hand swipe: a wrong T centre dropped it back
    [s:20261001-200952-chrono-2FYKPJ#29].
  - The solver refuses frames with a popup, "Good!/Excellent!" over the board or a line-clear flash:
    run again. "the moves changed nothing on screen" = every drag missed: run again (now barred).
    "UNTESTED low drop" = a finger near the cutoff: check the result. "RETRY of a barred drop" = nothing
    else fits; a RETRY note with "4+ misses" means place that piece by hand now instead of running
    again. The "half bright" stop of session 230945 was a misread green piece (fixed); whether a
    piece that cannot fit is drawn dimmed is still unknown [s:20261001-230945-chrono-2FYKPJ#32].
  - Past the 5-minute budget `--run` stops after every round ("over its time budget"): call it again.
  - Drops landed one row low about 4 times in 10 (session 20261003-193423: 7 of 17 solver drops, one 2
    rows low; the hand drag aimed 0.3 cell high landed): the lift was wrong (2.84 for 2.4), fixed in lab
    2026-10-03; check whether it still happens. The solver prefers placements that still land one
    row low; "did not drop (barred)" then "RETRY" on the same lone piece: place it by hand from a block,
    aiming 0.3 cell high (hand drag (152,1192) -> (437,1104) put ###/..# at r5c5).
  - Row 7 left empty with only lines in the tray (session 20261003-212548, score 2516): not a game bug,
    the pieces fit in row 7 and the old drag model never reached it (fixed). If a run still stops on
    a row-7 drop, a hand drag from a tray block with the finger ~45 model px above the touch point
    puts a 1-row piece in row 7.
  - Replay of the 90 solver drops of session 20261003-235233 (adventure levels, same board and drag
    model, lift 2.4): 86 landed where planned, 1 a row low, 3 a column right (rightward drags with the old
    0.2 lead, fixed lab 2026-10-04); 0 "did not drop". If "an earlier piece landed on its cells" appears,
    the next round replans by itself: just run again.
  - `solve --run` may crash on an adb hiccup (ConnectionResetError 10054 inside a swipe, session
    20261003-235233 step 35): look at the frame and run `--run` again; the round may replan from scratch.
  - `--board` on every solver call reads to the lab as a bypassed solver (sign of session
    20261003-193423, where `--board` carried only the gameover mode): do not pass it in classic.

- v10.8.1 fresh install (session 20261003-193423): the gameover mode reached "No Space Left" in ~2.2 min
  (score 327, ~205 s with the ad): 11 solver rounds, 39 moves, then one stop "the moves changed nothing"
  on a lone ###/..# piece; a hand drag from a block (152,1192) to finger (437,1104) placed it at r5c5
  (the solver had aimed 0.3 cell lower and 0.3 right: lattice shifted by the dot ring, fixed). Game over flow:
  board fills with colour, "No Space Left" banner with the last piece, an interstitial (skip >> ~10 s,
  end-card X ~8 s later), then "Can you Top that?" + Play -> new board. No revive on the first game.
  The solver refuses the black ad-loading frame ("board block is not square"): look at the frame.
- Tutorial on a fresh install is one board (2x2 into a cross hole, swipe 365,1210 -> 365,960); the
  clear gives +120 and the score counts up to 124 [s:20261003-193423-chrono-2FYKPJ#4].
  > ⚠️ Previously (2026-10-03): "the score then jumped 19 -> 124 with no move" (19 was a mid count-up frame).

### Level times
| Game | Result | Seconds | Model | Method | What decided it | Source |
|---|---|---|---|---|---|---|
| classic game 1 | quit | 517 | opus (study) | manual | drag calibration (5 failed drags), then Settings scouting; 35 moves, no game over | [s:20261001-200952-chrono-2FYKPJ#42] |
| classic game 2 | quit | 489 | sonnet low (play) | solver + hand drags | 724 points, no game over; ~38% of steps in solver retry loops | [s:20261001-230945-chrono-2FYKPJ#63] |
| classic game 1 (v10.8.1) | lost | 205 | opus (scout) | solver, gameover mode via --board + 1 hand drag | 327 points, No Space Left after 41 placements; one stall on a lone piece (lattice shifted by the dot ring) | [s:20261003-193423-chrono-2FYKPJ#31] |

The first two games were played for score and quit over the 5-minute budget; the gameover-mode game ended in 205 s. The mechanic stays `studying`. Next: task
make-classic-fast (lab fixes checked in play + gameover mode).

- Session 20261003-212548 (v10.8.1): a classic game played by the gameover solver reached 2516 and got stuck with only row 7 empty and tray of 1-row lines (5,3,4): drops there are ignored (low-drop cutoff), no game over. Hand drags of a Z piece to r0c5 failed from the top-left block and worked from the bottom-right block (400,1228). Settings gear > Replay = interstitial then fresh board (best kept).
- Block Slide (More Games): drag bars sideways; unsupported blocks fall; full 8-cell row clears (+30); each non-clearing move raises a row (preview bar under the board); game over when the stack reaches the top, then interstitial and Game Over screen (exit / Play).
- Session 20261003-235233 (v10.8.1): row 7 confirmed reachable by hand with the 2.4-lift formula. 1-row
  2-line touched at (347,1210), finger to (415,1186) = 24 px above the touch point, 2.05 cells under the
  board edge -> row 7 cols 4-5. 2x2 rows 6-7 (touch y 1192, finger y 1142/1153) and vertical 2-line
  rows 6-7 (touch y 1228, finger y 1164) landed first try: 4 of 4 drags on target. Finger ends 0.5-1.5
  cells under the board (the old followup plan) would land a piece 1-2 rows too high.
  [s:20261003-235233-chrono-2FYKPJ#2-4]

## adventure: classic board with a goal (Adventure mode, 96 levels)
- Goal per level, shown in the header: L1 a target score (progress bar 0 -> 368); L2 collect 60 diamonds;
  L3 56 red + 54 orange gems; L4 22 blue diamonds + 20 orange + 20 yellow stars. Gem tiles sit on the
  pre-built board and on tray piece cells; a gem counts when its line is cleared (the gem flies to the
  counter). A goal turns into a green check when done.
- Same 8x8 geometry, tray, drag model and scoring as classic. Loss: No Space Left before the goal ->
  "You Can Do It!" + Retry, no revive, nothing spent. No lives, energy or timer.
- Method: the classic solver in score mode, which maximises clears (clears collect the gems):
  `solve classic --run --rounds 30 --board <file with {"mode":"score"}>` on the FIRST `--run` of the
  level; later `--run` calls without `--board` keep score mode (memory). A `--board` on a plain
  `solve` (no --run) did NOT carry over: the next --run played gameover mode (L1 still won by luck).
  The gameover mode loses a gem level fast (L2: 16 moves, 4/60) - use it only for a deliberate loss.
- The run stops on the gem-fly animation ("cells neither empty nor a block") and on the result screen
  ("board block is not square"): rerun / look at the frame. After the goal: the win panel slides in
  (Consecutive Victories xN counts up ~3 s), sometimes an interstitial first (skip icon top left).
- Results (session 20261003-235233): L1 won 2.2 min, L2 lost (deliberate), L2 won 3.1 min (incl. ad),
  L3 won 2.3 min. Mastered.

## Dream 2026-10-04: corrections and level times (v10.8.1)

- Tutorial: the 2x2 clear gives +120 and the score counts up 4 -> 124; read a score only after the count-up ends [s:20261003-193423-chrono-2FYKPJ#4].
- Back on the classic board opens the home menu (Classic, Adventure, More Games, Medal, daily victories) [s:20261003-212548-chrono-2FYKPJ#29]. Settings > Replay restarts and plays an interstitial [s:20261003-212548-chrono-2FYKPJ#26].
- Game over is reached: No Space Left, an interstitial, then "Can you Top that?" with Play and no revive (327 in 205 s) [s:20261003-193423-chrono-2FYKPJ#29-31].
- Row 7 is reachable with a hand drag: `finger_y = y0 + (Y - y0 + 195) / 1.46` (4 of 4 drops landed) [s:20261003-235233-chrono-2FYKPJ#4]. This confirms the v10.8.1 drag model above (lift 2.4 cells = 195 px), which replaces the v10.6.5 fit (230 px).
- Adventure: play with the classic solver in score mode: pass `--board` with `{"mode":"score"}` on the FIRST `--run`; a mode given on a plain `solve` call is dropped [s:20261003-235233-chrono-2FYKPJ#8]. When it stops on "cells neither empty nor a block" in a gem level, rerun: the gems are still flying to their counters [s:20261003-235233-chrono-2FYKPJ#51].
- Interstitial with a store header (Royal Match): never tap its top-left >| icon, it opens Google Play; wait, then `launch`. Tapped three times in two sessions [s:20261003-212548-chrono-2FYKPJ#27] [s:20261003-212548-chrono-2FYKPJ#43] [s:20261003-235233-chrono-2FYKPJ#44].
- Before testing quit or exit-app, make sure the board has a score > 0: on an empty board the case cannot be read [s:20261003-212548-chrono-2FYKPJ#29-30].

| Level | Result | Seconds | Source |
|---|---|---|---|
| classic game 1 | lost on purpose (gameover mode), 327 | 205 | [s:20261003-193423-chrono-2FYKPJ#31] |
| adventure 1 (score 368) | won | 131 | [s:20261003-235233-chrono-2FYKPJ#21] |
| adventure 2 (60 diamonds) | lost on purpose, then won | 62 / 188 | [s:20261003-235233-chrono-2FYKPJ#29] [s:20261003-235233-chrono-2FYKPJ#45] |
| adventure 3 (gems) | won | 137 | [s:20261003-235233-chrono-2FYKPJ#59] |
