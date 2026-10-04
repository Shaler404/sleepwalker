---
game: com.king.candycrushsaga
title: "Lessons"
type: agent
version_seen: 1.337.0.2
verified_at: 2026-10-04
---

# Lessons for the agent: Candy Crush Saga

- After the winning move, `shot` every 1-2 s: the Level completed screen falls between frames taken 8-15 s apart.
  *Confirmed: 20261003-194350-chrono-2FYKPJ, 20261003-225003-chrono-2FYKPJ, 1.337.0.2.* [s:20261003-194350-chrono-2FYKPJ#6] [s:20261003-225003-chrono-2FYKPJ#43]
- A quit and a force-stop each cost a life; run exit-app tests right after Play, before any move.
  *Confirmed: 20261003-225003-chrono-2FYKPJ, 20261003-230937-chrono-2FYKPJ, 1.337.0.2.* [s:20261003-225003-chrono-2FYKPJ#50] [s:20261003-230937-chrono-2FYKPJ#12]
- Tap bottom-bar tab centres (73, 218, 365, 510, 655): x=437 is the Social/Pins boundary and opened Pins.
  *Confirmed: 20261003-230937-chrono-2FYKPJ, 1.337.0.2.* [s:20261003-230937-chrono-2FYKPJ#2]
