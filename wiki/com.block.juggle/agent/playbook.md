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
- Gameover mode ends the game by BLOCKING (lab 2026-10-06 (4)): the game deals a tray that fits the board
  as dealt, so filling the board never ends a game (session 20261006-084209: 84 trays, 10.7 min, 11366, the
  tray turned to 1x1s and diagonals), but it does not check the order of the three pieces. Once a tray
  allows it, the solver places only 1 or 2 pieces so that the rest of the tray fits nowhere; the note
  starts `[mode gameover] BLOCK: after ... no room is left for slotN`. On the 84 recorded trays of that game
  such a line existed from round 5 on (79 of 80; 73 of 110 trays over three sessions), so a game should end
  in about 5-6 rounds (~2 min). Until then it fills the board as before. Not yet seen on the phone: check
  that the game ends with pieces still in the tray (expected: the No Space Left banner); if it does not,
  `--run` again: the next round says "GAME OVER: no tray piece fits" or plays on.
  ⚠️ Superseded: the BLOCK line was seen on the phone, 15 of 15 classic games over in 0.4-1.3 min (sessions 20261006-105231, 20261006-111957, 20261006-133549 below).
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
  - Filling the board is not a way to lose: the tray adapts (small pieces on a crowded board) and forced
    clears follow [s:20261006-084209-chrono-2FYKPJ#103]. The BLOCK line is the way; a BLOCK round leaves
    tray pieces unplaced on purpose: do not place them by hand. If the drop of a BLOCK round missed, the
    next round bars it and finds another block.
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
  - The solver refuses frames with a popup or a dimmed page: run again. "Good!/Excellent!" text, a
    line-clear flash, flying gems or the refill glow give a "WAIT n" round instead (lab 2026-10-06: a
    tray piece pulled down and let go, the run continues; after 3 waits in a row it stops: look at the
    frame). "the moves changed nothing on screen" = every drag missed: run again (now barred).
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
    20261003-235233 step 35; "device not found" / "adb server refused" 5 times in session 20261006-105231):
    `shot` to reconnect, then `--run` again. Since lab 2026-10-06 (5) the solver sees that nothing of the
    crashed round happened (same board, same tray) and plays that plan again once, warm-up included (note
    "last round: nothing changed (the moves were probably not sent: adb drop?): planned again once");
    before, it barred all three placements as "did not drop" and skipped the warm-up (games 3 and 5 of
    105231). A second unchanged round in a row bars them as before.
  - The result screen ends the run: "GAME OVER: the classic result screen (Score, Best Score, Play)"
    (done) on the blue page with the green Play or the purple new-best page with the orange Play (lab
    2026-10-06 (5)). Before, a game over with no interstitial reached that screen during the run and the run
    stopped as "not a classic board" (gave up, game 2 of 105231). A new game whose tray is still growing in
    gives a WAIT round instead of "tray empty".
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
- Method (lab 2026-10-06): `solve classic --run --rounds 30` with NO `--board`. The solver sees the
  Adventure screen itself (back chevron top left instead of the classic crown) and plays score mode,
  which maximises clears (clears collect the gems); the note starts `[mode score]`. Only a deliberate
  loss needs `--board '{"mode":"gameover"}'` on the first `--run` (the gameover mode loses a gem level
  fast: L2, 16 moves, 4/60).
  > Previously (2026-10-04): `--board <file with {"mode":"score"}>` on the first `--run` of every level
  > (an inline `--board {"mode":"score"}` was refused once as "no such file", session 20261005-004506).
- How a run ends: "LEVEL WON: every goal in the header is checked" or "LEVEL WON/LOST: the result
  panel" (done): take a `shot` and `level end won|lost`. A gem-fly animation, a line clear or the refill
  glow now gives a "WAIT n" round (a tray piece pulled down and let go) and the run goes on; up to 3 in
  a row. Before this, 7 of 8 adventure runs of three sessions ended as "gave up" on exactly those
  screens. After the goal: the win panel slides in (Consecutive Victories xN counts up ~3 s; green
  "Next Level" or purple "Next Hard Level"), sometimes an interstitial first (skip icon top left).
- Since lab 2026-10-06 (7) two more endings are "done", not "gave up": "LEVEL OVER: the Adventure result
  panel is coming in" (the page dims to navy, the Consecutive Victories banner slides down or the score
  counts up in a disc; session 20261006-133549 frames 91, 149) and "LEVEL OVER: an interstitial covers the
  screen right after an Adventure round" (the ad plays BEFORE the result panel: frames 100, 142). On either:
  close the ad if there is one, take a `shot` of the result panel and `level end won` (Next Level / Next Hard
  Level) or `lost` (Retry). The score-target "Well Done!" panel (button higher, frame 150) now reads as
  LEVEL WON too. In that session 3 of 4 adventure runs had ended "gave up" on exactly these frames after
  the winning round; nothing was wrong with the play (L6 2.7, L7 0.9, L8 1.6, L9 ~2 min of solver play).
  Also fixed: stars flying over the page under the board (gem-fly, session 20261006-141221 frame 102) made
  the run stop with "page background ... is not the game's blue: popup or dim"; it is now a WAIT round.
- Scoring, read off the Adventure score bar (session 20261006-141221, L11 and L12, 47 rounds, exact): a
  placement scores 1 per cell plus 10 x k(k+1)/2 for k lines cleared at once (1 line 10, 2 lines 30, 3 lines
  60); past ~81% of the target (about 520/641, 595/733) cells stop counting and only clears score. So
  the last fifth of a score-target level is 10 points per single-line round (L12: 599 -> 733 took 11
  rounds). Score-target levels take longer as the target grows (L11 641: 3.6 min of play, L12 733: ~5.8
  min). Weighting multi-line clears in the search was tried offline (96 simulated games): +3% points
  and more game overs, so it stays off. Budget ~6 min for a score target over 700.
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

## More Games mini-games (2026-10-05)
- Fruit Merge: tap drops the current fruit at x; equal fruits merge along 11 steps (blueberry to watermelon); jar rarely overflows with merging (140 drops, none). Boosters shake and bomb x1 each, then rewarded-ad badge. Back arrow leaves at once; restart arrow asks to confirm.
- Mahjong: tap two identical free tiles (+30). L1 guided tutorial, tools undo (free), shuffle x3, hint x3 from L2. Win: interstitial then Level Clear (Home/Continue). Back key asks Are you sure you want to leave.
- One Line: drags must be straight segments via `taps "a>b c>d"`; the line persists between drags. Hint auto-draws squares. No loss state. Win is followed by an interstitial: Back closes the video, the L2 one chained into a playable ad that Back, launch and 40 s did not close (restart fixed it).

## Onet and Fruit Merge (2026-10-05, session 20261005-131038)
- Onet: tap two identical tiles joined by a path of at most 2 turns through empty cells; the path may run outside the board. Clear edge pairs first to open paths. Hint draws the path. After a board clear an interstitial plays then a playable that freezes: only restart gets out (L2 opened, so progress saved).
- Fruit Merge: dropping at the center x only (40+ drops) fills the jar; at overflow an ad covered the screen before the game over screen was seen.

## Sudoku and loss states (2026-10-05, session 20261005-153835)
- Sudoku: 6x6, 2x3 boxes, 3 hearts. Solve by logic (row/col/box elimination), digit then cell via `taps`; tray digits keep fixed x (80,196,308,420,533,645 on a 730 frame). Wrong digit costs a heart and is cleared; 0 hearts: Restore 1 Heart (ad)/New Game/Restart. L1 solved in 1:33.
- Fruit Merge: ~140 center drops (x=365) reach game over; a video ad and a store sheet cover it; launch then Back shows Game Over.
- Mahjong: MATCHES counter = free pairs; playing every pair wins. Win then interstitial then frozen playable: restart.

## Tic Tac Toe, Water Sort, Mahjong loss (2026-10-05, session 20261005-231555)
- Tic Tac Toe: tutorial (block, then win column) then rounds vs robot; bot blocks and takes lines; draw/loss each: ad then Draw/You Lost, Home (to More Games) / Play Again. Back closes the playable.
- Water Sort: tap source tube then target; pour needs same top colour and room; finished tube corks. L1: 3 colours, 2 empty tubes. Win goes straight to next level. Hint auto-pours (3), add tube (3), undo free.
- Mahjong: pairing free twins in any order never dead-ended on L3; no loss found.

## More Games mini-games: method per mechanic (lab 2026-10-06)
Each solver is `solve <mechanic> --run` with no `--board`; open the drawn frame of a plain `solve` once
per new mini-game. They were checked only on the recorded frames of one session each: watch the first
level played with them.
- water-sort: solver `solvers/com.block.juggle/water-sort.py`. Reads tubes and 4-layer colours, finds the
  fewest pours, taps source then target. A pour whose source took part in the pour just before is never
  next (that tap is lost while the tube is still moving: session 20261005-231555 step 32 lost the tap of
  3>4 and only selected tube 4); since lab 2026-10-06 (5) a later pour on other tubes (sharing no tube with
  any unplayed pour before it, so the result is the same) is played in its place, and the round ends only
  when none is ready. L5 of session 20261006-084209 took 10 rounds for 14 pours; the same line now takes 6
  (124 boards offline: 764 rounds -> 560). The note lists the pours in the order played. Two pours into the
  same tube in a row land (084209 step 10). A raised tube is a selection: the
  solver taps it first to put it down (frames 48-53 of that session: the bottom-left tube of L2 sat
  selected through the whole level). The small add-tube tube is planned only when nothing else works
  (its capacity is a guess). Refuses the win glow and tilted (pouring) tubes: run again. A corked
  (finished) tube mid-level is read as a full tube (lab 2026-10-06 (3): its cork split the outline and
  the solver saw a phantom tube, "colour counts [4, 4, 5]", session 20261006-053412 frame 7; fixed).
  Its BFS line is the shortest one: on L2-L4 of that session it gave exactly the lines the player
  worked out by hand (L4: 11 pours 1>5 3>6 1>3 4>3 ...). Play every level by `solve water-sort --run`;
  do not write the tubes and a BFS by hand (that counts as a bypassed solver).
- sudoku: solver `solvers/com.block.juggle/sudoku.py`. Reads the grid (N and the box shape from the thick
  lines) and the digits (matched against the tray glyphs and kept 1-6 bitmaps), solves, then taps a tray
  digit and every cell that takes it, digit by digit (the whole board in one round on L1-L2). Refuses a
  red-outlined (wrong) cell, the hearts sheet and the Pass Level panel.
- onet: solver `solvers/com.block.juggle/onet.py`. Groups equal pictures, searches a clearing order (paths
  of at most 2 turns, outside the board allowed), taps 6 pairs per round. If the board after a round is
  not the expected one (tiles sliding at later levels) it plays one pair per round and says so. A hint
  path over the board makes it refuse (odd picture counts): run again after the path fades. If it says
  "no order clears": shuffle.
- one-line: solver `solvers/com.block.juggle/one-line.py`. Finds the path from the coloured start square
  over every square and sends one swipe per straight run (the line stays between swipes). Since lab
  2026-10-06 (6) it also finishes a line already drawn (by an earlier run, by hand or by the hint): it
  reads the drawn chain from the start disc to its head and swipes the rest from the head (note "line
  drawn ...; continue from the head rXcY"). Do not restart a half-drawn level: run the solver. It says
  "dead end ... restart the level" only when no path covers the open squares from the head, and
  "solved" (done) when every square is drawn or the crown shows. Pitfall: session 20261005-125535 called
  an 8/11 line a dead end and spent a hint, but the head r3c1 could still go r2c1 r2c0 r1c0.
- mahjong-mg: manual. Tiles are stacked (half-hidden lower layers), so the free test needs the eye: a
  tile is free when nothing lies on it and its left or right side is open. Pair free twins, buried twins
  last; three of a kind free: keep the one that frees the most. MATCHES N at the top = free pairs now;
  0 means shuffle. L1 won and L2-L3 played (sessions 20261005-125535, -231555): pairing free twins in
  any order never dead-ended.
- fruit-merge: heuristic (random next fruit, physics). Endless; a "level" is played for a goal only. To
  lose fast (game over study): drop every fruit at the centre x=365 (~140 drops). To play for score:
  1) drop the current fruit onto the same fruit when one sits on top of the pile; 2) else drop small
  fruits at the side where the smallest fruits are, keep the largest in one corner; 3) never drop
  a large fruit on top of small ones. Past the 5-minute budget: quit.

## Water Sort L2-L4 (2026-10-06, session 20261006-053412)
- Boards are fixed per level: Restart and an app restart deal the identical layout. L3: 4 colours, 4 full tubes, 2 empties; L4: 4 colours mixed.
- Method that worked: write the tubes as strings (bottom->top), run a BFS for the shortest line, then send pours by tube centres (730 frame: top row x 177/365/553 y 520; bottom row with 3 tubes x 103/277/452 y 990; with 2 tubes + small tube x 177/365 y 990). Never two pours in a row from the same source in one batch; keep the BFS order (an interleave I made broke a pour, the game just ignored it).
  ⚠️ Superseded: play Water Sort with `solve water-sort --run` (its BFS gives the same lines); since lab 2026-10-06 (5) the solver plays a later pour early only when it shares no tube with an unplayed pour before it and its source was not in the previous pour.
- The solver misread a corked tube after round 1 (colour counts not multiples of 4) and L2-L4 were then finished by hand. Fixed in lab 2026-10-06 (3) (the cork split the tube outline in two); now it reads that frame (`ABB | CCCC | BBA | AA`, 3 pours). If a count error still appears, run `--run` again once the confetti is gone, and place by hand only if it repeats.
- Dead ends: BFS over all 5132 reachable L4 states found none; L2-L3 cannot dead-end either (a colour on top of another colour in a full tube only comes from the initial layout). Look for a loss on later levels with more colours.

## Water Sort L4-L7 and classic gameover mode (2026-10-06, session 20261006-084209)
- Water Sort: solver `--run` won L4 (resumed mid-board), L5, L6 in 1-2 calls each (0.7-2 min). L5 4 colours mixed, L6 3 colours, L7 4 colours; all keep 2 empties. BFS (scratch script: tubes as strings, pour = top run up to free space) found no dead end on L4, L5, L7: losing by pouring is impossible this early.
- Water Sort: the L6 win played a store-header video interstitial; wait ~35 s for the end card, then one `key back` returns to the next level. Back arrow leaves to More Games over the classic board.
- Classic gameover mode does NOT reach game over: 84 trays, 10.7 min, score 11366; when the board is crowded the tray deals small pieces (1x1, 2-cell diagonals, 2x1) and placements force clears. Do not start a classic game for a game-over goal with less than 15 min left. Fixed in lab 2026-10-06 (4): the gameover mode now blocks the rest of the tray (see "Gameover mode ends the game by BLOCKING" under classic); budget ~3 min for a game over until that is seen on the phone.
  ⚠️ Superseded: that was the fill-fast mode; the BLOCK line added by lab 2026-10-06 (4) ends games in 0.4-1.3 min (sessions 20261006-105231, 20261006-111957, 20261006-133549 below).

## Classic gameover mode on the phone (2026-10-06, session 20261006-105231)
- The BLOCK line works on the phone: 6 of 6 classic games ended in No Space Left with pieces left in the
  tray, 0.5-1.3 min each from an empty board (5-6 solver rounds; the resumed 11366 board ended on round 1).
  Plan for any game-over goal: `level start`, `solve classic --run --rounds 15` (no `--board`), read the
  "GAME OVER" note, `level end lost`. To push the game over later (a timing test), first run score mode
  with a `--board` file holding {"mode":"score"}, then pass a file with {"mode":"gameover"} on the next
  `--run`: the mode switched as asked.
  ⚠️ A `--board` mode file counts as a bypassed solver (see the classic pitfall above): use it only for a timing experiment and say "experiment" in `level end --note`.
- Game-over interstitial: a time cooldown, not every game over.
  ⚠️ Previously "~5 min from the previous ad's start": sessions 20261006-133549 and 20261006-141221 showed it counts from the previous ad's close (about 3-4.7 min), shared with Adventure wins.
  Several end cards: (1) the ad auto-opens a Play Store sheet: close it with the sheet's X (677,408); if the
  Play Store home stays behind, `launch` (it pressed Back for you); (2) a playable end card with no X that
  ignores Back and 40 s of waiting: `restart` (game over and best are already saved); (3) an end card with
  an X top left (59,97): tap it; (4) Royal Match store-header video: wait ~50 s, one Back.
- The result screen title rotates (Can you Top that?, Your Best is Next, Your High Score is Calling!,
  Unbeaten? Try Again!, Just One More!) and counts the score up before the Play button is drawn.
- A Rating popup can cover the result screen: close it with its X (628,500), never the thumbs-up.
- adb dropped 4 times inside `solve --run` this session (traceback "device not found" / "adb server
  refused"): a plain `shot` reconnects; then re-run the solver (pass the `--board` mode again if the
  first round never ran).

## Classic game-over timing (2026-10-06, session 20261006-111957)
- BLOCK mode: 4 of 4 classic games over in 0.4-0.6 min (scores 37-41) from an empty board.
- Interstitials: none at the first game over 1.7 min after an app launch; ads at 5.6 min after the previous ad's start. An ad held open untouched for 3.5 min let the screen dim (session blocked): never hold an ad longer than ~2.5 min.
- New end card: coloring-game video -> auto Play Store sheet (close its X 677,408) -> playable with no X that ignores Back: restart.

## Ads and Adventure (2026-10-06, session 20261006-133549)
- Classic interstitial cooldown counts from the previous ad's CLOSE (~3 min): game over 3.3 min after a close (4.4 after its start) got an ad. The first game over after a cold launch had no ad at 3.2 and 3.9 min after the launch (hypothesis: the first game over after a launch is exempt).
- Holding the board for a timing test: `wait 55` + a harmless tap at (365,1500) below the tray, repeated; the screen never dimmed.
- Store-header ads: never tap the top-left ">| Next" / "Open Store"; the video auto-opens a Play Store sheet (X at 677,408); if the Play Store home is left, `launch` (presses Back for you). Then either an end card with X top right (670,97), a frozen end frame closed by Back, or a playable with no X that ignores Back: restart (classic game over and Adventure wins are saved before the ad: L7 kept after a restart).
- Adventure L6 (gems 40/40/40), L7 (gems 22/22/20), L8 (gems) and L9 hard (score bar to 687) all won by the solver in score mode, 0.9-2.7 min of play each. In Adventure the win interstitial plays before the win panel. The solver stops with "board block is not square (1080x2340)" on the win panel or a black ad-loading frame: take a shot. (Lab 2026-10-06 (7): these frames now end the run as "LEVEL OVER ..." (done), see "How a run ends" under adventure.)

## Ad timing in Adventure and classic (2026-10-06, session 20261006-141221)
- Adventure L10-L13 won by `solve classic --run` (score mode, no --board): L10 score 395 in ~1.1 min of play, L11 641 ~3.6 min, L12 733 ~5.8 min (hit the over-budget stop once: just run again), L13 gems 34+34 ~2 min of play.
- To time a result, run the solver in short bursts (`--rounds 4-6`), read the goal counter, and hold with `wait` (<=60 s at a time) before the last clear.
- Classic BLOCK mode: game overs in 0.5-0.8 min (scores ~40). The first game over after a cold launch can get an ad.

## Level times by mechanic (dream 2026-10-07)

```yaml
---
mechanics:
- id: classic
  name: classic
  status: studying
  method: solver
  solver: solvers/com.block.juggle/classic.py
  levels:
    won: 0
    lost: 19
    quit: 3
  typical_min: null
  best_min: null
  solver_file: solvers/com.block.juggle/classic.py
- id: adventure
  name: adventure
  status: broken
  method: solver
  solver: solvers/com.block.juggle/classic.py
  levels:
    won: 13
    lost: 1
    quit: 1
  typical_min: 4.8
  best_min: 1.9
  solver_file: ''
  solver_sign: solver gave up in 2 of 5 levels (no moves, the same moves, or no change
    on screen)
- id: fruit-merge
  name: fruit-merge
  status: studying
  method: heuristic
  levels:
    won: 0
    lost: 0
    quit: 2
  typical_min: null
  best_min: null
  solver_file: ''
- id: mahjong-mg
  name: mahjong-mg
  status: studying
  method: manual
  levels:
    won: 1
    lost: 0
    quit: 2
  typical_min: 1.9
  best_min: 1.9
  solver_file: ''
- id: one-line
  name: one-line
  status: studying
  method: solver
  solver: solvers/com.block.juggle/one-line.py
  levels:
    won: 0
    lost: 0
    quit: 1
  typical_min: null
  best_min: null
  solver_file: solvers/com.block.juggle/one-line.py
- id: onet
  name: onet
  status: studying
  method: solver
  solver: solvers/com.block.juggle/onet.py
  levels:
    won: 0
    lost: 0
    quit: 1
  typical_min: null
  best_min: null
  solver_file: solvers/com.block.juggle/onet.py
- id: sudoku
  name: sudoku
  status: studying
  method: solver
  solver: solvers/com.block.juggle/sudoku.py
  levels:
    won: 1
    lost: 0
    quit: 0
  typical_min: null
  best_min: null
  solver_file: solvers/com.block.juggle/sudoku.py
- id: water-sort
  name: water-sort
  status: mastered
  method: solver
  solver: solvers/com.block.juggle/water-sort.py
  levels:
    won: 6
    lost: 1
    quit: 1
  typical_min: 1.0
  best_min: 0.7
  solver_file: solvers/com.block.juggle/water-sort.py
  solver_sign: 'solver bypassed: 2 of 5 levels placed by hand'
level_budget_min: 5
```
