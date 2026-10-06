---
game: com.maroieqrwlk.unpin
title: "Lessons"
type: agent
version_seen: 241.5.1
verified_at: 2026-10-06
---

# Lessons for the agent: Pull the Pin

- Never end a session or restart on a win screen: the win is saved only after the post-win flow (puzzle piece, league board, coin screen) ends.
  *Confirmed: 20261003-193015-chrono-2FYKPJ, 20261003-211035-chrono-2FYKPJ, 241.5.1.* [s:20261003-193015-chrono-2FYKPJ#7] [s:20261003-211035-chrono-2FYKPJ#23]
- On an interstitial end card do not tap the top-left skip (45,108): it opens the Play Store. Use the store sheet's own Close (top left) or `launch` (here `launch` alone returned to the game).
  *Confirmed: 20261003-211035-chrono-2FYKPJ, 20261003-214021-chrono-2FYKPJ, 20261004-004411-chrono-2FYKPJ, 20261004-005453-chrono-2FYKPJ, 241.5.1.* [s:20261003-211035-chrono-2FYKPJ#7] [s:20261003-214021-chrono-2FYKPJ#28] [s:20261004-004411-chrono-2FYKPJ#21] [s:20261004-005453-chrono-2FYKPJ#4]
- When a library order loses, read the end frame before replaying it: the same order loses the same way.
  *Confirmed: 20261004-004411-chrono-2FYKPJ, 20261004-005453-chrono-2FYKPJ, 241.5.1.* [s:20261004-004411-chrono-2FYKPJ#19] [s:20261004-005453-chrono-2FYKPJ#2]
- When the solver finds no pin rings on a dark theme, equip the default theme first; it is one tap away in Collections.
  *Confirmed: 20261004-003223-chrono-2FYKPJ, 20261004-004411-chrono-2FYKPJ, 241.5.1.* [s:20261004-003223-chrono-2FYKPJ#17] [s:20261004-004411-chrono-2FYKPJ#13]
- Three 60 s waits in a row (or a 60 s plus a 45 s wait) dim the screen and the next tap hits Samsung touch protection: keep idle waits under about 90 s with a harmless tap between them.
  *Confirmed: 20261005-145445-chrono-2FYKPJ, 241.5.2; 20261005-151039-chrono-2FYKPJ, 241.5.2; 20261005-141756-chrono-2FYKPJ, 241.5.2.* [s:20261005-145445-chrono-2FYKPJ#0] [s:20261005-151039-chrono-2FYKPJ#37] [s:20261005-141756-chrono-2FYKPJ#23]
- The camera follows falling balls, so pin positions move after each pull: look again after every pull that moves balls; only pulls of empty pins can be batched. Never pull a ring at the triangle tip on Challenge 1.
  *Confirmed: 20261006-030951-chrono-2FYKPJ, 241.5.2; 20261006-033538-chrono-2FYKPJ, 241.5.2.* [s:20261006-030951-chrono-2FYKPJ#19] [s:20261006-030951-chrono-2FYKPJ#26] [s:20261006-033538-chrono-2FYKPJ#66]
- On Color Bucket L20 wait 6 s between the M and Y pulls: the 98% stall came from pulling Y 0.5 s after M.
  *Confirmed: 20261006-012240-chrono-2FYKPJ, 241.5.2; 20261005-235042-chrono-2FYKPJ, 241.5.2.* [s:20261006-012240-chrono-2FYKPJ#16] [s:20261005-235042-chrono-2FYKPJ#36]
- A restart while stuck in a between-stage ad sends a multi-stage level back to stage 1; Back closes the frozen end card and keeps the stage.
  *Confirmed: 20261005-141756-chrono-2FYKPJ, 241.5.2; 20261006-033538-chrono-2FYKPJ, 241.5.2.* [s:20261005-141756-chrono-2FYKPJ#13] [s:20261006-033538-chrono-2FYKPJ#40]
- Sketchman (IQ test) levels cannot be failed: a 0% result still pays IQ 50; the Get button leaves for the next main level, not the mode grid.
  *Confirmed: 20261006-012240-chrono-2FYKPJ, 241.5.2; 20261005-235042-chrono-2FYKPJ, 241.5.2.* [s:20261006-012240-chrono-2FYKPJ#13] [s:20261005-235042-chrono-2FYKPJ#21]
