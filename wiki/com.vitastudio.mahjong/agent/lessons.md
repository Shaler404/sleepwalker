---
game: com.vitastudio.mahjong
title: "Lessons"
type: agent
version_seen: 3.39.1
verified_at: 2026-10-01
sources: [20260930-211039-chrono-2FYKPJ, 20260930-221457-chrono-2FYKPJ, 20260930-225122-chrono-2FYKPJ, 20260930-235817-chrono-2FYKPJ, 20261001-010125-chrono-2FYKPJ, 20261001-031723-chrono-2FYKPJ]
---

# Lessons for the agent: Vita Mahjong

- Never take a single into the tray while 2 tiles are already there, and never send two uncertain
  pairs in one batch: every Out of space came from this.
  *Confirmed: 20260930-225122-chrono-2FYKPJ, 3.39.1; 20261001-010125-chrono-2FYKPJ, 3.39.1; 20260930-235817-chrono-2FYKPJ, 3.39.1.* [s:20260930-225122-chrono-2FYKPJ#46] [s:20261001-010125-chrono-2FYKPJ#35] [s:20260930-235817-chrono-2FYKPJ#12]
- After a level opens, take one frame (or wait 1 s) before the first batch: the intro eats the first
  taps.
  *Confirmed: 20260930-221457-chrono-2FYKPJ, 3.39.1 (L6); playbook L3.* [s:20260930-221457-chrono-2FYKPJ#79]
- Wait 1 s after a match animation before a tray-critical or booster tap: such taps get lost.
  *Confirmed: 20260930-225122-chrono-2FYKPJ, 3.39.1; 20261001-031723-chrono-2FYKPJ, 3.39.1.* [s:20260930-225122-chrono-2FYKPJ#38] [s:20261001-031723-chrono-2FYKPJ#36]
- A playable ad with no close button: `sw.py launch` at once; the reward is still granted.
  *Confirmed: 20261001-010125-chrono-2FYKPJ, 3.39.1; 20261001-031723-chrono-2FYKPJ, 3.39.1.* [s:20261001-010125-chrono-2FYKPJ#43] [s:20261001-031723-chrono-2FYKPJ#82]
- Read league standings only after the rank animation ends.
  *Confirmed: 20261001-031723-chrono-2FYKPJ, 3.39.1 (frame mid-animation).* [s:20261001-031723-chrono-2FYKPJ#95]
