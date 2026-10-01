---
game: com.oakever.meowdoku
title: "Lessons"
type: agent
version_seen: 1.18.0
verified_at: 2026-10-01
sources: [20260930-233055-chrono-2FYKPJ, 20261001-013526-chrono-2FYKPJ, 20261001-022624-chrono-2FYKPJ]
---

# Lessons for the agent: Meowdoku

- A playable interstitial ignores taps and Back: run `sw.py launch` at once; the level is still
  there.
  *Confirmed: 20261001-013526-chrono-2FYKPJ, 1.18.0; 20261001-022624-chrono-2FYKPJ, 1.18.0.* [s:20261001-013526-chrono-2FYKPJ#15] [s:20261001-022624-chrono-2FYKPJ#42]
- After `launch` from an ad, wait 2 s before solving: the first solve after an overlay misreads the
  board.
  *Confirmed: 20261001-022624-chrono-2FYKPJ, 1.18.0; 20261001-013526-chrono-2FYKPJ, 1.18.0 (a 1x1 read).* [s:20261001-022624-chrono-2FYKPJ#33] [s:20261001-013526-chrono-2FYKPJ#24]
- Record a level as won only when the win screen or the leaderboard is in the frame.
  *Confirmed: 20260930-233055-chrono-2FYKPJ, 1.18.0; 20261001-013526-chrono-2FYKPJ, 1.18.0 (four early records).* [s:20260930-233055-chrono-2FYKPJ#59] [s:20261001-013526-chrono-2FYKPJ#110]
- After the solver run on a 10x10 board, check that every light-coloured region has a cat.
  *Confirmed: 20261001-013526-chrono-2FYKPJ, 1.18.0; 20261001-022624-chrono-2FYKPJ, 1.18.0.* [s:20261001-013526-chrono-2FYKPJ#106] [s:20261001-022624-chrono-2FYKPJ#16]
- After toggling settings for a test, restore every toggle and look at the frame (Pattern Mode was
  left ON).
  *Confirmed: 20261001-022624-chrono-2FYKPJ, 1.18.0 (frame of level 43).* [s:20261001-022624-chrono-2FYKPJ#95]
