---
game: com.oakever.akari
title: "Tactics"
type: agent
version_seen: 1.0.2
verified_at: 2026-10-02
sources: [20261001-003641-chrono-2FYKPJ, 20261001-024647-chrono-2FYKPJ, 20261001-035425-chrono-2FYKPJ, 20261001-100940-chrono-2FYKPJ, 20261001-171804-chrono-2FYKPJ, 20261001-175856-chrono-2FYKPJ, 20261001-221517-chrono-2FYKPJ]
---

# Tactics

- Solve the whole board before placing anything: each wrong cat costs a heart at once [s:20261001-003641-chrono-2FYKPJ#29].
- One board read + the solver + one batch of double taps wins a level in about 20 s; Hard 10x10
  boards need nothing extra [s:20261001-024647-chrono-2FYKPJ#109].
- From level 83 the solver reads the board itself: one `sw.py solve akari --run --rounds 3` per level,
  12–40 s, nothing typed; it also finishes a board that already has cats and the X marks of hints
  [s:20261001-171804-chrono-2FYKPJ#2] [s:20261001-221517-chrono-2FYKPJ#41] [s:20261001-100940-chrono-2FYKPJ#17].
- Ads, not solving, set the pace (about half of the wall time). Hypothesis to use while the experiment
  `ad-cooldown-timer` runs: start the next level within about 45 s of an interstitial closing (it had no
  ad every time so far), and the first level after an app launch had no ad either
  [s:20261001-221517-chrono-2FYKPJ#41] [s:20261001-175856-chrono-2FYKPJ#21]. Do not stretch levels to
  test this outside the experiment.
- To reach the fail screen on purpose: double tap cells next to 0 walls — they are always wrong
  [s:20261001-035425-chrono-2FYKPJ#21].
