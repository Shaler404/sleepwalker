---
game: com.block.juggle
title: "Lessons"
type: agent
version_seen: 10.8.1
verified_at: 2026-10-04
---

# Lessons for the agent: Block Blast!

- When an interstitial shows a store header with a top-left >| icon, do not tap it: it opens Google Play. If the ad ends on a playable end card with no X, press the Back key: `launch` does nothing while the app is already in front.
  ⚠️ Previously: "Wait for the ad to end, then `launch`." Two sessions saw an end card that never ended (95 s and 88 s of waiting) and was closed by Back.
  *Confirmed: 20261003-212548-chrono-2FYKPJ, 20261003-235233-chrono-2FYKPJ, 20261005-004506-chrono-2FYKPJ, 20261005-015205-chrono-2FYKPJ, 10.8.1.* [s:20261005-004506-chrono-2FYKPJ#12] [s:20261005-004506-chrono-2FYKPJ#13] [s:20261005-015205-chrono-2FYKPJ#21] [s:20261003-212548-chrono-2FYKPJ#27] [s:20261003-212548-chrono-2FYKPJ#43] [s:20261003-235233-chrono-2FYKPJ#44]
- Give the solver its mode on the first `solve --run` with `--board <file>` (a file path, not inline JSON; e.g. a file holding {"mode":"score"} for Adventure): a mode passed on a plain `solve` call is dropped.
  *Confirmed: 20261003-235233-chrono-2FYKPJ, 20261005-004506-chrono-2FYKPJ, 10.8.1.* [s:20261005-004506-chrono-2FYKPJ#13] [s:20261003-235233-chrono-2FYKPJ#8]
- To reach the home menu, press Back on the classic board; the app opens straight on the board and has no menu button.
  *Confirmed: 20261003-212548-chrono-2FYKPJ, 20261003-235233-chrono-2FYKPJ, 10.8.1.* [s:20261003-212548-chrono-2FYKPJ#29] [s:20261003-235233-chrono-2FYKPJ#5]
