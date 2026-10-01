---
game: com.oakever.akari
title: "Lessons"
type: agent
version_seen: 1.0.2
verified_at: 2026-10-01
sources: [20261001-003641-chrono-2FYKPJ, 20261001-024647-chrono-2FYKPJ, 20261001-035425-chrono-2FYKPJ]
---

# Lessons for the agent: MeowTrail

- After tapping a level button, look at the frame before tapping anything else: an interstitial may
  or may not be up, and blind skip taps hit the level's back arrow and gear.
  *Confirmed: 20261001-035425-chrono-2FYKPJ, 1.0.2; 20261001-024647-chrono-2FYKPJ, 1.0.2 (blind taps landed on Play Store pages).* [s:20261001-035425-chrono-2FYKPJ#46] [s:20261001-024647-chrono-2FYKPJ#64]
- When the solver says "no solution: board misread?", re-read the row lengths and the box columns
  first.
  *Confirmed: 20261001-035425-chrono-2FYKPJ, 1.0.2 (twice).* [s:20261001-035425-chrono-2FYKPJ#30] [s:20261001-035425-chrono-2FYKPJ#44]
- (364,1225) in the Settings popup is Help Center on Home but Restart in a level (Restart costs an
  interstitial): check which popup is open.
  *Confirmed: 20261001-035425-chrono-2FYKPJ, 1.0.2 (frames of both popups).* [s:20261001-035425-chrono-2FYKPJ#5] [s:20261001-035425-chrono-2FYKPJ#42]
- On a level with a tip popup (levels 6 and 11), close it with OK before reading the board.
  *Confirmed: 20261001-003641-chrono-2FYKPJ, 1.0.2 (two levels).* [s:20261001-003641-chrono-2FYKPJ#12] [s:20261001-003641-chrono-2FYKPJ#23]
