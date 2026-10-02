---
game: com.oakever.akari
title: "Lessons"
type: agent
version_seen: 1.0.2
verified_at: 2026-10-02
sources: [20261001-003641-chrono-2FYKPJ, 20261001-024647-chrono-2FYKPJ, 20261001-035425-chrono-2FYKPJ, 20261001-070939-chrono-2FYKPJ, 20261001-091349-chrono-2FYKPJ, 20261001-100940-chrono-2FYKPJ, 20261001-143237-chrono-2FYKPJ, 20261001-171336-chrono-2FYKPJ, 20261001-173851-chrono-2FYKPJ, 20261001-175856-chrono-2FYKPJ, 20261001-221517-chrono-2FYKPJ]
---

# Lessons for the agent: MeowTrail

- After tapping a level button, look at the frame before tapping anything else: an interstitial may
  or may not be up, and blind skip taps hit the level's back arrow and gear.
  *Confirmed: 20261001-035425-chrono-2FYKPJ, 1.0.2; 20261001-024647-chrono-2FYKPJ, 1.0.2 (blind taps landed on Play Store pages).* [s:20261001-035425-chrono-2FYKPJ#46] [s:20261001-024647-chrono-2FYKPJ#64]
- With the `--board` fallback (a hand-typed board), when the solver says "no solution: board
  misread?", re-read the row lengths and the box columns first. Since 2026-10-01 15:29 the solver reads
  the board from the frame and the fallback is rarely needed.
  *Confirmed: 20261001-035425-chrono-2FYKPJ, 1.0.2 (twice).* [s:20261001-035425-chrono-2FYKPJ#30] [s:20261001-035425-chrono-2FYKPJ#44]
- (364,1225) in the Settings popup is Help Center on Home but Restart in a level (Restart costs an
  interstitial): check which popup is open.
  *Confirmed: 20261001-035425-chrono-2FYKPJ, 1.0.2 (frames of both popups).* [s:20261001-035425-chrono-2FYKPJ#5] [s:20261001-035425-chrono-2FYKPJ#42]
- On a level with a tip popup (levels 6 and 11), close it with OK before reading the board.
  *Confirmed: 20261001-003641-chrono-2FYKPJ, 1.0.2 (two levels).* [s:20261001-003641-chrono-2FYKPJ#12] [s:20261001-003641-chrono-2FYKPJ#23]
- Log `level end won` only after the win screen shows the counter at N/N: level 63 was logged won at
  11/13 (Next did nothing) and level 77 after 5 s with no move, before either was solved; both left
  wrong level times.
  *Confirmed: 20261001-091349-chrono-2FYKPJ, 1.0.2; 20261001-100940-chrono-2FYKPJ, 1.0.2.* [s:20261001-091349-chrono-2FYKPJ#13] [s:20261001-100940-chrono-2FYKPJ#28]
- Close every won level with `level end won` before starting the next one: levels 57–61 and 81–82 were
  won but never logged, and the mechanic statistics count them as nothing or as quits.
  *Confirmed: 20261001-070939-chrono-2FYKPJ, 1.0.2; 20261001-143237-chrono-2FYKPJ, 1.0.2.* [s:20261001-070939-chrono-2FYKPJ#27] [s:20261001-143237-chrono-2FYKPJ#19]
- Tap the orange level buttons at their centre (Home "Level N" y 1340, win screen "Level N+1" y 1285);
  if the frame does not change, compare the tap with the button's bounds before retrying, relaunching
  or swiping. Taps at y 1430 cost a whole bench slot (4.3 min, 0 levels); taps at y 1210 cost about
  150 s.
  *Confirmed: 20261001-171336-chrono-2FYKPJ, 1.0.2; 20261001-175856-chrono-2FYKPJ, 1.0.2 (frames of both buttons).* [s:20261001-171336-chrono-2FYKPJ#11] [s:20261001-175856-chrono-2FYKPJ#13]
- An ad can look like a puzzle (a colour grid, "tap the lonely square"): a "Next" button or a Google
  Play bar means it is an ad. Skip it; never play it.
  *Confirmed: 20261001-143237-chrono-2FYKPJ, 1.0.2 (frame of the ad with Next at the top left).* [s:20261001-143237-chrono-2FYKPJ#16]
- An interstitial with no skip button ends on the Play Store by itself: wait in 20–30 s blocks, then
  `launch`; do not tap the video.
  *Confirmed: 20261001-173851-chrono-2FYKPJ, 1.0.2; 20261001-221517-chrono-2FYKPJ, 1.0.2 (levels 113 and 119).* [s:20261001-173851-chrono-2FYKPJ#3] [s:20261001-221517-chrono-2FYKPJ#16] [s:20261001-221517-chrono-2FYKPJ#37]
