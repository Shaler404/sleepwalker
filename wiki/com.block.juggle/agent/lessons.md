---
game: com.block.juggle
title: "Lessons"
type: agent
version_seen: 10.8.1
verified_at: 2026-10-04
---

# Lessons for the agent: Block Blast!

- When an interstitial shows a store header with a top-left >| icon, do not tap it: it opens Google Play. Wait for the ad to end, then `launch`.
  *Confirmed: 20261003-212548-chrono-2FYKPJ, 20261003-235233-chrono-2FYKPJ, 10.8.1.* [s:20261003-212548-chrono-2FYKPJ#27] [s:20261003-212548-chrono-2FYKPJ#43] [s:20261003-235233-chrono-2FYKPJ#44]
- Give the solver its mode on the first `solve --run` with `--board` (e.g. {"mode":"score"} for Adventure): a mode passed on a plain `solve` call is dropped.
  *Confirmed: 20261003-235233-chrono-2FYKPJ, 10.8.1.* [s:20261003-235233-chrono-2FYKPJ#8]
- To reach the home menu, press Back on the classic board; the app opens straight on the board and has no menu button.
  *Confirmed: 20261003-212548-chrono-2FYKPJ, 20261003-235233-chrono-2FYKPJ, 10.8.1.* [s:20261003-212548-chrono-2FYKPJ#29] [s:20261003-235233-chrono-2FYKPJ#5]
