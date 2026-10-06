---
game: com.crypt.gram.puzz
title: "Lessons"
type: agent
version_seen: 3.6.1
verified_at: 2026-10-06
---

# Lessons for the agent: Cryptogram: Word Logic Puzzles

- On level 1 there is no hint bulb and no Mistakes counter: if the solver stalls, quit with the home icon (free) instead of typing letters by hand.
  *Confirmed: 20261003-234451-chrono-2FYKPJ, 3.6.1.* [s:20261003-234451-chrono-2FYKPJ#10] [s:20261003-234451-chrono-2FYKPJ#19]
- After opening a text field, take a fresh shot before the next tap: the keyboard moves the dialog and an old coordinate types a key.
  *Confirmed: 20261003-201504-chrono-2FYKPJ, 3.6.1.* [s:20261003-201504-chrono-2FYKPJ#11]
- The solver stalls on the last cell or two of almost every level (levels 4-10) and refuses a board while a tutorial overlay is up: dismiss the tutorial first, and type the last letter by hand after reading the board.
  *Confirmed: 20261006-003220-chrono-2FYKPJ, 3.6.1; 20261005-221933-chrono-2FYKPJ, 3.6.1; 20261005-143208-chrono-2FYKPJ, 3.6.1.* [s:20261006-003220-chrono-2FYKPJ#6] [s:20261006-003220-chrono-2FYKPJ#57] [s:20261005-221933-chrono-2FYKPJ#28] [s:20261005-143208-chrono-2FYKPJ#15]
- A playable ad with no close button after NEXT, START, CLAIM or the hint bulb ignores Back and `launch`: restart the app; the win and the lives are kept and a hint is not credited.
  *Confirmed: 20261006-003220-chrono-2FYKPJ, 3.6.1; 20261005-221933-chrono-2FYKPJ, 3.6.1; 20261006-024420-chrono-2FYKPJ, 3.6.1.* [s:20261006-003220-chrono-2FYKPJ#22] [s:20261005-221933-chrono-2FYKPJ#25] [s:20261006-024420-chrono-2FYKPJ#20]
- Tap a locked home button to read its 'Complete N more levels' condition instead of guessing the unlock level.
  *Confirmed: 20261005-221933-chrono-2FYKPJ, 3.6.1.* [s:20261005-221933-chrono-2FYKPJ#36]
- The keyboard moves the promo-code dialog: take a frame after focusing the field, or taps land on keyboard keys.
  *Confirmed: 20261005-143208-chrono-2FYKPJ, 3.6.1.* [s:20261005-143208-chrono-2FYKPJ#3]
