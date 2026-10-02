---
game: com.king.candycrushsaga
title: "Lessons"
type: agent
version_seen: 1.335.1.2
verified_at: 2026-10-02
sources: [20261001-202316-chrono-2FYKPJ, 20261001-232021-chrono-2FYKPJ]
---

# Lessons for the agent: Candy Crush Saga

- After a move, wait before reading the board: the next frame often still shows the old board or the
  cascade (`wait 3`; after a big combo `sleep 6` + `wait 3`). Re-sending a move on a stale frame
  repeated the same swap on level 4.
  confirmed: 20261001-202316-chrono-2FYKPJ, 1.335.1.2; 20261001-232021-chrono-2FYKPJ, 1.335.1.2 [s:20261001-202316-chrono-2FYKPJ#6-8] [s:20261001-232021-chrono-2FYKPJ#16-21]
- The FTUE hides the saga map for more than 6 levels (story path through level 7); a scout of a fresh
  install needs a level budget (about 3 levels per 25-min session), not a menu walk.
  confirmed: 20261001-202316-chrono-2FYKPJ, 1.335.1.2; 20261001-232021-chrono-2FYKPJ, 1.335.1.2 [s:20261001-202316-chrono-2FYKPJ#31] [s:20261001-232021-chrono-2FYKPJ#53]
- King's own windows (the first-launch Terms popup and the Retrieve My Progress panel) are reported as
  app "Panel": `mark` refuses them; describe them in the notes with the shot number so the dream can
  export the frame with `wiki-img`.
  confirmed: 20261001-202316-chrono-2FYKPJ, 1.335.1.2; 20261001-232021-chrono-2FYKPJ, 1.335.1.2 [s:20261001-202316-chrono-2FYKPJ#0] [s:20261001-232021-chrono-2FYKPJ#13]
- The "N / heart-infinity" at the top left of the level HUD is the level number (2 on level 2, 5 on
  level 5), not a life count; lives are unlimited during the FTUE.
  confirmed: 20261001-202316-chrono-2FYKPJ, 1.335.1.2; 20261001-232021-chrono-2FYKPJ, 1.335.1.2 (frames of levels 2 and 5) [s:20261001-202316-chrono-2FYKPJ#12] [s:20261001-232021-chrono-2FYKPJ#33]
- A tap sent on a late frame of the King panel landed on another page (Privacy and security instead of
  the carousel): after opening the panel, shoot again before the next tap.
  confirmed: 20261001-232021-chrono-2FYKPJ, 1.335.1.2 (frame of the wrong page) [s:20261001-232021-chrono-2FYKPJ#1-3]
- A link from the King panel opens Chrome; `launch` returns to the panel, not the title.
  confirmed: 20261001-232021-chrono-2FYKPJ, 1.335.1.2 (frame) [s:20261001-232021-chrono-2FYKPJ#10]
- End the session soon after the last level: both sessions spent 1.5-3 min on bookkeeping after the
  last move without starting the next level; write notes while the cascade settles instead.
  confirmed: 20261001-202316-chrono-2FYKPJ, 1.335.1.2; 20261001-232021-chrono-2FYKPJ, 1.335.1.2 [s:20261001-202316-chrono-2FYKPJ#31] [s:20261001-232021-chrono-2FYKPJ#52-53]
