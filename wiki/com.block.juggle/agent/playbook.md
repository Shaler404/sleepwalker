---
game: com.block.juggle
title: "How to play"
type: agent
version_seen: 10.6.5
verified_at: 2026-10-02
sources: [20261001-200952-chrono-2FYKPJ, 20261001-230945-chrono-2FYKPJ]
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
- Drag model: the piece moves faster than the finger (gain ~1.46) and floats above the touch point.
  To put the piece's bounding-box centre at board point (X, Y), swipe from a touch point (x0, y0) on a
  block of the tray piece to `finger_x = x0 + (X - x0) / 1.46`, `finger_y = y0 + (Y - y0 + 230) / 1.46`
  (lab fit on 53 placed drags of two sessions: gain 1.44-1.46, lift 2.84 cells = 230 px; most land
  within 0.1 cell; snapping tolerance about half a cell) [s:20261001-200952-chrono-2FYKPJ#12-14]
  [s:20261001-230945-chrono-2FYKPJ#19]. Checked: T to rows 2-3 (finger 365,960), 5-line to row 6
  (finger 244,1150), 3-line to row 4 cols 0-2 (finger 294,1040). The tutorial 2x2, drawn full size in
  the tray, worked with finger (365,960) for rows 3-4 [s:20261001-200952-chrono-2FYKPJ#5].
- Low drops are ignored: when the finger ends more than ~1.64 cells under the board (y > ~1150) the
  piece flies back whatever the sideways travel (lab: 1.60-1.63 cells placed 3 of 3, 1.65 ignored 7 of
  7). Keep the finger within 1.5 cells. A 1-row piece reaches row 6 at best; row 7 only with pieces 3+
  cells tall [s:20261001-200952-chrono-2FYKPJ#13] [s:20261001-200952-chrono-2FYKPJ#25].
- Where to touch: the lifted piece centres on the touch point wherever you touch it. Touch the middle
  of a filled block of the tray piece, never the bbox centre when it falls on an empty cell or a seam
  between blocks: such touches failed again and again (the same drop 13 times in a row) while every drag
  started on a block worked [s:20261001-230945-chrono-2FYKPJ#14-18] [s:20261001-230945-chrono-2FYKPJ#19]
  [s:20261001-230945-chrono-2FYKPJ#53].
- Drops land short, not long: a missed drop lands 1-2 cells short along the drag, mostly on the first
  drag after a tray refill. Aim 0.3 cell above the target centre and up to 0.2 cell ahead sideways
  (lab, 2026-10-01).
- Batches work: the step-9 `taps` batch failed only because its coordinates were wrong (lab replay:
  two drops ended 2+ cells under the board, one above it), not a harness gap
  [s:20261001-200952-chrono-2FYKPJ#9].
- Scoring (v10.6.5): 1 point per placed cell [s:20261001-200952-chrono-2FYKPJ#23]; one line about +10
  (a 3-cell piece clearing a row gave +13) [s:20261001-200952-chrono-2FYKPJ#23]; two lines with one
  piece +60 and "Good!" [s:20261001-200952-chrono-2FYKPJ#30]; the tutorial 2+2 lines gave +6 and
  "Excellent!" [s:20261001-200952-chrono-2FYKPJ#5]. The score probably counts up after a clear (not proven): one frame
  showed 201 with "+60" still on screen [s:20261001-200952-chrono-2FYKPJ#30]; read the
  score only once the count-up has finished. The 6 → 124 jump after the tutorial is probably the same
  count-up (not proven; task tutorial-score-jump) [s:20261001-200952-chrono-2FYKPJ#7].
- Pieces seen: 1x1; lines of 2, 3, 4 and 5 (both directions); 2x2 and 3x3 squares; 3x3 L; small L; T;
  S/Z; 3x3 diagonal; ##/.#/.# [s:20261001-230945-chrono-2FYKPJ#25] [s:20261001-230945-chrono-2FYKPJ#40].
- Method: solver (`state/com.block.juggle/solvers/classic.py`, local draft, not published yet: no
  classic game has been finished within the budget). `sw.py solve classic` reads the board and the
  tray, searches every order and placement of the tray pieces (clears modelled, droppable placements
  only) and returns one swipe per piece with the drag model built in (touch on a block, aim up and
  ahead); `rescan` is always true (the refill is random). After a refill the first swipe is a warm-up
  pull (the piece goes back to the tray), then the real drags. Its memory bars a placement that did not
  drop, so a failed drop is not repeated (note "last round: ... did not drop (barred)"). One round =
  one tray.
- Level plan: start the level, `solve classic` once and open the drawn frame (the red circles must sit
  on tray blocks), then `solve classic --run --rounds 20`; when it stops, read its last note and run it
  again. "GAME OVER: no tray piece fits" or a game-over screen ends the level (`level end --result
  lost`, the score is the progress value). For the end screen (study-classic, revive, ads) write a file
  with `{"mode": "gameover"}` and run `solve classic --run --rounds 20 --board FILE`: the solver fills
  the board instead of clearing lines for the rest of the level.
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
    else fits. The "half bright" stop of session 230945 was a misread green piece (fixed); whether a
    piece that cannot fit is drawn dimmed is still unknown [s:20261001-230945-chrono-2FYKPJ#32].
  - Past the 5-minute budget `--run` stops after every round ("over its time budget"): call it again,
    or switch to the gameover mode.

### Level times
| Game | Result | Seconds | Model | Method | What decided it | Source |
|---|---|---|---|---|---|---|
| classic game 1 | quit | 517 | opus (study) | manual | drag calibration (5 failed drags), then Settings scouting; 35 moves, no game over | [s:20261001-200952-chrono-2FYKPJ#42] |
| classic game 2 | quit | 489 | sonnet low (play) | solver + hand drags | 724 points, no game over; ~38% of steps in solver retry loops | [s:20261001-230945-chrono-2FYKPJ#63] |

No game finished; both over the 5-minute budget. The mechanic stays `studying`. Next: task
make-classic-fast (lab fixes checked in play + gameover mode).
