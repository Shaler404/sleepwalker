---
game: com.block.juggle
title: "Tactics"
type: agent
version_seen: 10.6.5
verified_at: 2026-10-02
sources: [20261001-200952-chrono-2FYKPJ, 20261001-230945-chrono-2FYKPJ]
---

# Tactics

The rules and the drag model are in the [playbook](playbook.md); these are the moves that worked.

- Drag with the gain/lift model and touch a filled block of the tray piece: hand drags started on a
  block landed where the model says, drags from the bbox centre on an empty cell or a seam failed over
  and over [s:20261001-230945-chrono-2FYKPJ#19] [s:20261001-230945-chrono-2FYKPJ#53].
- Keep the finger no lower than 1.5 cells under the board; for row 7 use a piece 3+ cells tall
  [s:20261001-200952-chrono-2FYKPJ#13] [s:20261001-200952-chrono-2FYKPJ#25].
- When the solver stalls, place pieces by hand in rows 0-4 with the drag model, then hand back to the
  solver [s:20261001-230945-chrono-2FYKPJ#19] [s:20261001-230945-chrono-2FYKPJ#53].
- To reach game over, fill the board on purpose (solver gameover mode, `{"mode": "gameover"}` via
  `--board`); playing for score keeps the board open past the budget
  [s:20261001-230945-chrono-2FYKPJ#63].
- To end a game quickly without game over: Settings → Replay (costs an interstitial)
  [s:20261001-200952-chrono-2FYKPJ#39] [s:20261001-200952-chrono-2FYKPJ#42].
- Do the cheap Settings tasks (consent links, Sound/BGM/Vibration, More Settings rows) in the first
  minutes, before any long classic game: in one session they were never reached
  [s:20261001-230945-chrono-2FYKPJ#63].
- Big clears come from squares and L pieces: one tray of two 3x3 squares and an L cleared 5 lines
  [s:20261001-230945-chrono-2FYKPJ#40].
