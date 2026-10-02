---
game: com.oakever.meowdoku
title: "Lessons"
type: agent
version_seen: 1.18.0
verified_at: 2026-10-02
sources: [20260930-233055-chrono-2FYKPJ, 20261001-013526-chrono-2FYKPJ, 20261001-022624-chrono-2FYKPJ, 20261001-060942-chrono-2FYKPJ, 20261001-093348-chrono-2FYKPJ, 20261001-115413-chrono-2FYKPJ, 20261001-181422-chrono-2FYKPJ, 20261001-182810-chrono-2FYKPJ, 20261001-183504-chrono-2FYKPJ, 20261001-185238-chrono-2FYKPJ, 20261001-223249-chrono-2FYKPJ]
---

# Lessons for the agent: Meowdoku

- A playable interstitial ignores taps and Back: run `sw.py launch` at once; the level is still
  there.
  *Confirmed: 20261001-013526-chrono-2FYKPJ, 1.18.0; 20261001-022624-chrono-2FYKPJ, 1.18.0; 20261001-182810-chrono-2FYKPJ, 1.18.0.* [s:20261001-013526-chrono-2FYKPJ#15] [s:20261001-022624-chrono-2FYKPJ#42] [s:20261001-182810-chrono-2FYKPJ#5]
- After `launch` from an ad, wait 2 s before solving: the first solve after an overlay misreads the
  board.
  *Confirmed: 20261001-022624-chrono-2FYKPJ, 1.18.0; 20261001-013526-chrono-2FYKPJ, 1.18.0 (a 1x1 read).* [s:20261001-022624-chrono-2FYKPJ#33] [s:20261001-013526-chrono-2FYKPJ#24]
- Record a level as won only when the win screen or the leaderboard is in the frame, and name it from
  the "Level N" header. A golden board (header "Score" only, one fish) is not a level. This lesson was
  broken again: a level recorded won with an ad on screen, a board recorded twice, golden boards
  recorded as levels and two fake wins on the previous win screen.
  *Confirmed: 20260930-233055-chrono-2FYKPJ, 1.18.0; 20261001-013526-chrono-2FYKPJ, 1.18.0; 20261001-060942-chrono-2FYKPJ, 1.18.0; 20261001-185238-chrono-2FYKPJ, 1.18.0.* [s:20260930-233055-chrono-2FYKPJ#59] [s:20261001-013526-chrono-2FYKPJ#110] [s:20261001-060942-chrono-2FYKPJ#20] [s:20261001-181422-chrono-2FYKPJ#13] [s:20261001-185238-chrono-2FYKPJ#19]
- After the solver run on a 10x10 board, check that every light-coloured region has a cat.
  *Confirmed: 20261001-013526-chrono-2FYKPJ, 1.18.0; 20261001-022624-chrono-2FYKPJ, 1.18.0.* [s:20261001-013526-chrono-2FYKPJ#106] [s:20261001-022624-chrono-2FYKPJ#16]
- After toggling settings for a test, restore every toggle and look at the frame: Pattern Mode was left
  ON at level 43 and stayed ON until level 96.
  *Confirmed: 20261001-022624-chrono-2FYKPJ, 1.18.0 (frame of level 43); 20261001-115413-chrono-2FYKPJ, 1.18.0 (frame of level 90).* [s:20261001-022624-chrono-2FYKPJ#95] [s:20261001-115413-chrono-2FYKPJ#43] [s:20261001-115413-chrono-2FYKPJ#75]
- Place the cats with one `taps` batch from the solver's drawn solution (`solve queens`, then the grid
  formula), not with `solve --run`: the batch never failed and is the fastest way through a level.
  *Confirmed: 20261001-115413-chrono-2FYKPJ, 1.18.0; 20261001-182810-chrono-2FYKPJ, 1.18.0; 20261001-223249-chrono-2FYKPJ, 1.18.0.* [s:20261001-115413-chrono-2FYKPJ#62] [s:20261001-182810-chrono-2FYKPJ#2] [s:20261001-223249-chrono-2FYKPJ#2]
- On Home the "Level N" button is at y≈1185, not 1245 (1245 is its place on the win screen only), and
  Android Back on Home opens a Quit popup: take the position from the frame and never press Back there.
  *Confirmed: 20261001-183504-chrono-2FYKPJ, 1.18.0; 20261001-185238-chrono-2FYKPJ, 1.18.0 (frames of the Quit popup and Home).* [s:20261001-183504-chrono-2FYKPJ#1] [s:20261001-185238-chrono-2FYKPJ#7] [s:20261001-185238-chrono-2FYKPJ#10]
- On the win screen of every 4th level the Golden Fish button takes the place of the next-level
  button: look at the frame before the routine (365,1245) tap; "Skip to Level N" is at (365,1475).
  *Confirmed: 20261001-093348-chrono-2FYKPJ, 1.18.0; 20261001-181422-chrono-2FYKPJ, 1.18.0 (frame of the L102 win screen).* [s:20261001-093348-chrono-2FYKPJ#64] [s:20261001-181422-chrono-2FYKPJ#11]
- Look at the frame before a continue tap that follows an ad: an interstitial's "Install" card near
  (365,1413) caught a blind tap and opened the Play Store.
  *Confirmed: 20261001-060942-chrono-2FYKPJ, 1.18.0 (frame of the interstitial).* [s:20261001-060942-chrono-2FYKPJ#20] [s:20261001-060942-chrono-2FYKPJ#21]
- Do not idle-wait inside a session for a timed check: after a few minutes the screen dims and sleeps
  and the next tap fails. Leave a follow-up task with `not_before` instead.
  *Confirmed: 20261001-223249-chrono-2FYKPJ, 1.18.0 (dimmed frame about 6 minutes in).* [s:20261001-223249-chrono-2FYKPJ#8]
