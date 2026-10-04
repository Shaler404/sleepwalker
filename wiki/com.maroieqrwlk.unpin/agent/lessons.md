---
game: com.maroieqrwlk.unpin
title: "Lessons"
type: agent
version_seen: 241.5.1
verified_at: 2026-10-04
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
