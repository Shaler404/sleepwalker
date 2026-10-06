---
game: com.block.juggle
title: "Lessons"
type: agent
version_seen: 10.8.1
verified_at: 2026-10-06
---

# Lessons for the agent: Block Blast!

- When an interstitial shows a store header with a top-left >| icon, do not tap it: it opens Google Play. If the ad ends on a playable end card with no X, press the Back key: `launch` does nothing while the app is already in front.
  ⚠️ Previously: "Wait for the ad to end, then `launch`." Two sessions saw an end card that never ended (95 s and 88 s of waiting) and was closed by Back.
  *Confirmed: 20261003-212548-chrono-2FYKPJ, 20261003-235233-chrono-2FYKPJ, 20261005-004506-chrono-2FYKPJ, 20261005-015205-chrono-2FYKPJ, 10.8.1.* [s:20261005-004506-chrono-2FYKPJ#12] [s:20261005-004506-chrono-2FYKPJ#13] [s:20261005-015205-chrono-2FYKPJ#21] [s:20261003-212548-chrono-2FYKPJ#27] [s:20261003-212548-chrono-2FYKPJ#43] [s:20261003-235233-chrono-2FYKPJ#44]
- Give the solver its mode on the first `solve --run` with `--board <file>` (a file path, not inline JSON; e.g. a file holding {"mode":"score"} for Adventure): a mode passed on a plain `solve` call is dropped.
  *Confirmed: 20261003-235233-chrono-2FYKPJ, 20261005-004506-chrono-2FYKPJ, 10.8.1.* [s:20261005-004506-chrono-2FYKPJ#13] [s:20261003-235233-chrono-2FYKPJ#8]
- To reach the home menu, press Back on the classic board; the app opens straight on the board and has no menu button.
  *Confirmed: 20261003-212548-chrono-2FYKPJ, 20261003-235233-chrono-2FYKPJ, 10.8.1.* [s:20261003-212548-chrono-2FYKPJ#29] [s:20261003-235233-chrono-2FYKPJ#5]
- After a mini-game ends, an ad plays and a playable ad can follow with no close button: wait about 40-45 s, then press Back; restart only if that fails (a restart during the ad loses the win screen).
  *Confirmed: 20261005-231555-chrono-2FYKPJ, 10.8.1; 20261005-131038-chrono-2FYKPJ, 10.8.1.* [s:20261005-231555-chrono-2FYKPJ#20] [s:20261005-231555-chrono-2FYKPJ#24] [s:20261005-131038-chrono-2FYKPJ#33]
- The harness `taps` command takes two-point swipes only and at most 40 moves per call: draw One Line runs as separate swipes and split large batches.
  *Confirmed: 20261005-125535-chrono-2FYKPJ, 10.8.1; 20261005-131038-chrono-2FYKPJ, 10.8.1.* [s:20261005-125535-chrono-2FYKPJ#33] [s:20261005-131038-chrono-2FYKPJ#5]
- Game Over and result buttons slide in from the bottom: wait until they settle (about y 1220 on Fruit Merge) before tapping.
  *Confirmed: 20261005-153835-chrono-2FYKPJ, 10.8.1.* [s:20261005-153835-chrono-2FYKPJ#13]
- The More Settings button of the classic Settings sits at y 767 (it was 833 in older notes); a tap at the old place leaves the frame unchanged.
  *Confirmed: 20261006-032721-chrono-2FYKPJ, 10.8.1.* [s:20261006-032721-chrono-2FYKPJ#3]
