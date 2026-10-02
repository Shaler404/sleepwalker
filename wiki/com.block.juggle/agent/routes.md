---
game: com.block.juggle
title: "Routes"
type: agent
version_seen: 10.6.5
verified_at: 2026-10-02
sources: [20261001-200952-chrono-2FYKPJ, 20261001-230945-chrono-2FYKPJ]
---

# Routes

Positions in the 730x1583 frame. There is no main menu: the game opens on the classic board, and the
gear is the only entry point.

- Launch, progressed device: straight to a new classic board (score 0, best score kept), no menu and no
  popup [s:20261001-230945-chrono-2FYKPJ#0].
- Launch, fresh install: Terms/Privacy window, Accept (365,1018); Android notification prompt, Don't
  allow (365,1476); the tutorial board; drag the 2x2 (365,1210) → (365,960) [s:20261001-200952-chrono-2FYKPJ#1]
  [s:20261001-200952-chrono-2FYKPJ#2] [s:20261001-200952-chrono-2FYKPJ#5]. Skill: `first-launch-consent`
  (candidate; covers the two taps).
- Settings: gear (660,135) [s:20261001-200952-chrono-2FYKPJ#6] [s:20261001-200952-chrono-2FYKPJ#31]
  [s:20261001-200952-chrono-2FYKPJ#38]. Skill: `open-settings` (candidate; its pre-hash is one board,
  so it matches only that board).
- From Settings: More Games (365,703) [s:20261001-200952-chrono-2FYKPJ#33]; More Settings (365,832)
  [s:20261001-200952-chrono-2FYKPJ#7], close it (609,445) [s:20261001-200952-chrono-2FYKPJ#8]; Replay
  (365,965) → an interstitial [s:20261001-200952-chrono-2FYKPJ#39]; Default Skin (365,1097) does
  nothing [s:20261001-200952-chrono-2FYKPJ#32]. Sound, BGM and Vibration sit in the top row of the
  popup (not tapped yet).
- More Games: scroll the list (365,1100) → (365,550); Sudoku (365,1050) after the scroll; the
  mini-game's back arrow (50,197); close More Games (628,347) [s:20261001-200952-chrono-2FYKPJ#34-37].
  Skill: `more-games-sudoku-roundtrip` (candidate; from the Settings popup back to the board).
- Terms of Service and Privacy Policy (study-consent): Settings → More Settings, rows under the social
  links [s:20261001-200952-chrono-2FYKPJ#7]; not opened yet.
