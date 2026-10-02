---
game: com.king.candycrushsaga
title: "Routes"
type: agent
version_seen: 1.335.1.2
verified_at: 2026-10-02
sources: [20261001-202316-chrono-2FYKPJ, 20261001-232021-chrono-2FYKPJ]
---

# Routes

Positions in the 730x1583 frame, version 1.335.1.2. The saga map has not appeared yet (FTUE through
level 7), so every route starts from the title screen or the FTUE story path.

![Title screen: Play, Retrieve My Progress, settings gear bottom left](../img/20261001-title-screen-screen-c7973a0b.webp)

- Fresh install to level 1: Terms of Use ACCEPT (364,1147) → title Play (364,1308) → Android
  notification prompt "Don't allow" (364,1477) → level 1 loads directly [s:20261001-202316-chrono-2FYKPJ#1] [s:20261001-202316-chrono-2FYKPJ#4-5].
  See [consent](../features/consent.md).
- Title → next level (skill `title-to-level-board`): Play (365,1310) → story path → Play (365,1418)
  [s:20261001-232021-chrono-2FYKPJ#14-15].
- Story path after a win → next level (skill `story-path-to-next-board`): Play (365,1418), wait 3 s
  [s:20261001-202316-chrono-2FYKPJ#12] [s:20261001-232021-chrono-2FYKPJ#43].
- Booster Unlocked popup at a level start (skill `close-booster-unlocked`): Sweet! (365,1115)
  [s:20261001-232021-chrono-2FYKPJ#53].
- Settings (skill `open-close-settings-from-title`): gear (72,1448) on the title; X (633,70) closes
  [s:20261001-202316-chrono-2FYKPJ#2-3].
- King account panel: title → Retrieve My Progress (365,1446); Log in with email (365,1068); back arrow
  (45,120); X (676,118) back to the title. Nothing is ever entered [s:20261001-232021-chrono-2FYKPJ#11] [s:20261001-232021-chrono-2FYKPJ#13].
  The panel is reported as app "Panel": `mark` refuses its frames.
- Personalised ads: panel → Privacy and security (bottom row) → personalised ads row (365,475)
  [s:20261001-232021-chrono-2FYKPJ#4].
- Terms of Use link in the panel opens Chrome; `launch` returns to the panel, then X
  [s:20261001-232021-chrono-2FYKPJ#9-10].
