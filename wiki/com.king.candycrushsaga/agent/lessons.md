---
game: com.king.candycrushsaga
title: "Lessons"
type: agent
version_seen: 1.337.0.2
verified_at: 2026-10-06
---

# Lessons for the agent: Candy Crush Saga

- After the winning move, `shot` every 1-2 s: the Level completed screen falls between frames taken 8-15 s apart.
  *Confirmed: 20261003-194350-chrono-2FYKPJ, 20261003-225003-chrono-2FYKPJ, 1.337.0.2.* [s:20261003-194350-chrono-2FYKPJ#6] [s:20261003-225003-chrono-2FYKPJ#43]
- A quit and a force-stop each cost a life; run exit-app tests right after Play, before any move.
  *Confirmed: 20261003-225003-chrono-2FYKPJ, 20261003-230937-chrono-2FYKPJ, 1.337.0.2.* [s:20261003-225003-chrono-2FYKPJ#50] [s:20261003-230937-chrono-2FYKPJ#12]
- Tap bottom-bar tab centres (73, 218, 365, 510, 655): x=437 is the Social/Pins boundary and opened Pins.
  *Confirmed: 20261003-230937-chrono-2FYKPJ, 1.337.0.2.* [s:20261003-230937-chrono-2FYKPJ#2]
- Replay level 1 for experiments on plain candies: the meringue on levels 3 and 4 blocks 2x2 squares and lowers the chance of a fish.
  *Confirmed: 20261005-072135-chrono-2FYKPJ, 1.337.0.2; 20261006-020945-chrono-2FYKPJ, 1.337.0.2.* [s:20261005-072135-chrono-2FYKPJ#18] [s:20261006-020945-chrono-2FYKPJ#8]
- A quit costs one life (5 to 4 to 3) and a life comes back about every 30 min; do not burn lives on purpose.
  *Confirmed: 20261005-072135-chrono-2FYKPJ, 1.337.0.2; 20261005-220615-chrono-2FYKPJ, 1.337.0.2.* [s:20261005-072135-chrono-2FYKPJ#12] [s:20261005-220615-chrono-2FYKPJ#11]
- A force-stop relaunch on a progressed install does not bring the notification prompt back: leave that case for a fresh install.
  *Confirmed: 20261005-220615-chrono-2FYKPJ, 1.337.0.2.* [s:20261005-220615-chrono-2FYKPJ#12]
- A `mark` role with a space (for example tab:Profile card) must be quoted or written with an underscore, or the call fails with exit code 2.
  *Confirmed: 20261006-000939-chrono-2FYKPJ, 1.337.0.2.* [s:20261006-000939-chrono-2FYKPJ#11]
