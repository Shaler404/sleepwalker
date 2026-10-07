---
game: com.oakever.meowdoku
title: "Lessons"
type: agent
version_seen: 1.19.1
verified_at: 2026-10-07
---

# Lessons for the agent: Meowdoku: Brain Puzzle Games

- Shoot the win screen before `level end won`; on the day's first win the Daily Streak popup and screen come before the praise screen.
  *Confirmed: 20261003-201915-chrono-2FYKPJ, 20261003-202631-chrono-2FYKPJ, 1.19.1.* [s:20261003-201915-chrono-2FYKPJ#7] [s:20261003-202631-chrono-2FYKPJ#6]
- After a level start or a Restart take a shot before tapping the top-left back arrow: an interstitial under it opened the Play Store.
  *Confirmed: 20261003-202631-chrono-2FYKPJ, 1.19.1.* [s:20261003-202631-chrono-2FYKPJ#19] [s:20261003-202631-chrono-2FYKPJ#20]
- Android Back inside a level does nothing: leave with the arrow at (57,110).
  *Confirmed: 20261005-123456-chrono-2FYKPJ, 1.19.1.* [s:20261005-123456-chrono-2FYKPJ#12-13]
- The in-level gear and the Home gear open different popups: Pattern Mode and Restart are in-level only; Language, Save progress and the links are Home only. Closing a popup opened from Options also closes Options, so the next tap lands on the board.
  *Confirmed: 20261006-010939-chrono-2FYKPJ, 1.19.1.* [s:20261006-010939-chrono-2FYKPJ#2] [s:20261006-010939-chrono-2FYKPJ#11]
- Clear the golden-fish tutorial popup and tooltip before running the solver: with the popup up it misreads 49 and 31 cats.
  *Confirmed: 20261006-021434-chrono-2FYKPJ, 1.19.1.* [s:20261006-021434-chrono-2FYKPJ#18] [s:20261006-021434-chrono-2FYKPJ#19]
- The solver reports 'not a board' on a win screen: take it as a won level and photograph the win card, do not retry.
  *Confirmed: 20261005-143752-chrono-2FYKPJ, 1.19.1; 20261006-021434-chrono-2FYKPJ, 1.19.1.* [s:20261005-143752-chrono-2FYKPJ#2] [s:20261006-021434-chrono-2FYKPJ#27]
- Run day-boundary and streak tests before the day's first win: once a win has counted the day, the streak screen cannot change and the test is lost.
  *Confirmed: 20261006-101030-chrono-2FYKPJ, 20261006-122109-chrono-2FYKPJ, 1.19.1.* [s:20261006-101030-chrono-2FYKPJ#1] [s:20261006-101030-chrono-2FYKPJ#16] [s:20261006-122109-chrono-2FYKPJ#1] [s:20261006-122109-chrono-2FYKPJ#16]
- In Profile, an open frame tooltip swallows the next frame tap: tap the Profile title (365,415) to close it first.
  *Confirmed: 20261006-044214-chrono-2FYKPJ, 1.19.1.* [s:20261006-044214-chrono-2FYKPJ#6] [s:20261006-044214-chrono-2FYKPJ#8]
