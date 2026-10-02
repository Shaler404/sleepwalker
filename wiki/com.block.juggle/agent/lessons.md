---
game: com.block.juggle
title: "Lessons"
type: agent
version_seen: 10.6.5
verified_at: 2026-10-02
sources: [20261001-200952-chrono-2FYKPJ, 20261001-230945-chrono-2FYKPJ]
---

# Lessons for the agent: Block Blast!

- An interstitial end card (after Replay) with no close control after 30+ s ignores Back: restart the
  app at once (`sw.py restart --why ...`). The best score survives; the Android notification prompt
  comes back after the restart (Don't allow at (365,1476)).
  confirmed: 20261001-200952-chrono-2FYKPJ, 10.6.5 (frames #40-42) [s:20261001-200952-chrono-2FYKPJ#40] [s:20261001-200952-chrono-2FYKPJ#41] [s:20261001-200952-chrono-2FYKPJ#42]
- When the goal is game over, do not play for score: an endless classic game with good play outlasts the
  5-minute budget (517 s and 489 s, no game over). Fill the board on purpose.
  confirmed: 20261001-200952-chrono-2FYKPJ, 10.6.5; 20261001-230945-chrono-2FYKPJ, 10.6.5 [s:20261001-200952-chrono-2FYKPJ#42] [s:20261001-230945-chrono-2FYKPJ#63]
- If the solver returns the same plan twice on an unchanged frame, stop calling it and make that drag
  by hand, starting on a filled block of the piece; repeating never helped.
  confirmed: 20261001-230945-chrono-2FYKPJ, 10.6.5 (three loops, identical board in the notes) [s:20261001-230945-chrono-2FYKPJ#14-19] [s:20261001-230945-chrono-2FYKPJ#42-53]
- Read the score only after it has settled: one frame showed 201 with "+60" still on screen and the best
  later read 261, which looks like a count-up caught mid-way (a hypothesis, not proven).
  confirmed: 20261001-200952-chrono-2FYKPJ, 10.6.5 (frame #30) [s:20261001-200952-chrono-2FYKPJ#30]
- After a drag, read the frame even when the "same" flag is true: small placements stay under the
  pHash threshold.
  confirmed: 20261001-200952-chrono-2FYKPJ, 10.6.5 (frames #16, #19, #22) [s:20261001-200952-chrono-2FYKPJ#16] [s:20261001-200952-chrono-2FYKPJ#22]
