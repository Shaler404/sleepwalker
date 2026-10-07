---
game: com.oakever.arrows
title: "Lessons"
type: agent
version_seen: 1.33.0
verified_at: 2026-10-07
---

# Lessons for the agent: Amaze GO!

- On a Hard board never batch blind taps: use the free hint loop (bulb, wait about 2 s, tap the green arrow).
  *Confirmed: 20261003-233756-chrono-2FYKPJ, 20261004-001551-chrono-2FYKPJ, 1.33.0.* [s:20261003-233756-chrono-2FYKPJ#16] [s:20261004-001551-chrono-2FYKPJ#69]
- Read the win card only once Next Level and Home are drawn: the score counts up (895 -> 1194).
  *Confirmed: 20261004-001551-chrono-2FYKPJ, 1.33.0.* [s:20261004-001551-chrono-2FYKPJ#110]
- Restart and force-stop wipe a Hard board: run those outcome cases after the win, not mid-attempt.
  *Confirmed: 20261003-233756-chrono-2FYKPJ, 1.33.0.* [s:20261003-233756-chrono-2FYKPJ#23] [s:20261003-233756-chrono-2FYKPJ#24]
- Send deliberate blocked taps one per call: the second tap of a two-tap batch is ignored. The game also sometimes ignores a free-arrow tap, so every tap chained behind it hits a blocked arrow and costs a drop: re-read the board between taps.
  *Confirmed: 20261005-224323-chrono-2FYKPJ, 1.33.0; 20261005-233140-chrono-2FYKPJ, 1.33.0.* [s:20261005-224323-chrono-2FYKPJ#26] [s:20261005-233140-chrono-2FYKPJ#25] [s:20261005-233140-chrono-2FYKPJ#8]
- After a win the League card comes first: Continue, then take the frame of the win card and run `level end won`.
  *Confirmed: 20261005-124219-chrono-2FYKPJ, 1.33.0; 20261005-233140-chrono-2FYKPJ, 1.33.0.* [s:20261005-124219-chrono-2FYKPJ#12] [s:20261005-233140-chrono-2FYKPJ#21]
- Do not end a session on a win card: the win and its league points are lost if the level is not closed (the L12 and L17 wins were lost this way).
  *Confirmed: 20261005-124219-chrono-2FYKPJ, 1.33.0; 20261006-013740-chrono-2FYKPJ, 1.33.0.* [s:20261005-124219-chrono-2FYKPJ#21] [s:20261006-013740-chrono-2FYKPJ#2]
- An interstitial end card with no X is closed by Back and the win is kept.
  *Confirmed: 20261005-233140-chrono-2FYKPJ, 1.33.0; 20261006-013740-chrono-2FYKPJ, 1.33.0.* [s:20261005-233140-chrono-2FYKPJ#23] [s:20261006-013740-chrono-2FYKPJ#31]
- The interstitial after a win jumps to the Play Store by itself after about 25-35 s: plan a `launch` then; it returns to the win card.
  *Confirmed: 20261006-064018-chrono-2FYKPJ, 20261006-093640-chrono-2FYKPJ, 20261006-114946-chrono-2FYKPJ, 1.33.0.* [s:20261006-064018-chrono-2FYKPJ#40] [s:20261006-064018-chrono-2FYKPJ#81] [s:20261006-093640-chrono-2FYKPJ#21] [s:20261006-093640-chrono-2FYKPJ#22] [s:20261006-114946-chrono-2FYKPJ#24]
- Re-tapping an arrow that is already red costs no drop; a blocked tap on another arrow does. For a deliberate loss, tap three different blocked arrows.
  *Confirmed: 20261006-114946-chrono-2FYKPJ, 1.33.0.* [s:20261006-114946-chrono-2FYKPJ#36] [s:20261006-114946-chrono-2FYKPJ#37] [s:20261006-114946-chrono-2FYKPJ#38]
