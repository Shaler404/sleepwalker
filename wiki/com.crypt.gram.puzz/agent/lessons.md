---
game: com.crypt.gram.puzz
title: Lessons
type: agent
version_seen: 3.6.1
verified_at: 2026-10-01
sources: [20261001-020937-chrono-2FYKPJ]
---

# Lessons for the agent: Cryptogram

- Take tap coordinates only from the frame you are looking at. On level 9 keyboard coordinates of
  the 730-px frame were sent after a `shot --hi` (918x1988) frame, the tap landed on the "+20 /
  RSD 399" hint pack and opened a real Google Play sheet with 1-tap buy (backed out, nothing bought).
  The cause was the frame mix-up, not an ad overlay.
  *Confirmed: 20261001-020937-chrono-2FYKPJ, 3.6.1 (frame of the payment sheet, not published).* [s:20261001-020937-chrono-2FYKPJ#9]
- A video ad with a skip icon at the top left: tap it, then Back from the Play Store overlay. Look
  at the frame after that before "recovering": the level was already loaded.
  *Confirmed: 20261001-020937-chrono-2FYKPJ, 3.6.1.* [s:20261001-020937-chrono-2FYKPJ#5] [s:20261001-020937-chrono-2FYKPJ#8]
- A playable ad (Bus Jam) that ignores Back and home + launch: do not spend more than 2 minutes on
  it. `sw.py restart --why ...` (force-stop and start, added after this session) is the next thing to
  try — not yet verified here.
  *Confirmed: 20261001-020937-chrono-2FYKPJ, 3.6.1.* [s:20261001-020937-chrono-2FYKPJ#16] [s:20261001-020937-chrono-2FYKPJ#32]
