# Features: Block Blast!

Version: **10.8.1** · features: **24**, documented: **14** · cases closed: **210 / 233** · all sections found: **no**

Generated from [`research.yaml`](research.yaml) by `sw.py render`. Tasks: [tasks.md](tasks.md).

| Feature | Found at | Status | Cases | Open tasks | Version |
|---|---|---|---|---|---|
| [Terms of Use consent](features/terms-consent.md) |  | 🛠 in progress | 4 / 6 | On a fresh install walk the consent window: Accept, links, whether it can be declined or comes back |  |
| [First-launch tutorial board](features/tutorial.md) |  | 🛠 in progress | 6 / 7 | Tap Skip on the first-launch tutorial board and record what follows |  |
| [Classic mode (endless 8x8)](features/classic.md) |  | ✅ documented | 14 / 15 | What the green dot ring around the classic board means (seen from score ~319 of the first game); Classic: press Back with score > 0, then Classic: is the game in progress kept? Also leave the app mid-game and launch | 10.8.1 |
| [Settings](features/settings.md) |  | ✅ documented | 7 / 7 | What the red vibration badge on the gear means and when it clears | 10.8.1 |
| [Skins (Default Skin button)](features/skins.md) |  | ✅ documented | 8 / 8 | What makes the grey Default Skin button in Settings active (other skins)? | 10.8.1 |
| [More Games (mini-game list)](features/more-games.md) |  | ✅ documented | 6 / 6 | Mini-games: reopen One Line, Mahjong and Fruit Merge and record whether each resumes where it was left; Mini-games: count interstitials per win (does every One Line / Mahjong level win play an ad) | 10.8.1 |
| [Mini-game: One Line](features/mg-one-line.md) |  | 🛠 in progress | 8 / 8 |  |  |
| [Mini-game: Tic Tac Toe](features/mg-tic-tac-toe.md) |  | ✅ documented | 8 / 8 | Tic Tac Toe: win a real round against the robot and record the win screen and whether the 0 VS 0 scoreboard changes | 10.8.1 |
| [Mini-game: Fruit Merge](features/mg-fruit-merge.md) |  | 🛠 in progress | 8 / 9 | Find whether Fruit Merge has a win: is making a watermelon an end screen or is the jar endless |  |
| [Mini-game: Water Sort](features/mg-water-sort.md) |  | 🛠 in progress | 13 / 14 | Water Sort: spend the add-tube and hint stocks to 0 and record what tapping them at 0 offers (video, coins, nothing) and what No Thanks on Use Item does; Water Sort: check a later level (L15+) for 1 empty tube or more colours, BFS it for a stuck state and record the loss screen if one exists |  |
| [Mini-game: Onet](features/mg-onet.md) |  | 🛠 in progress | 7 / 9 | See Onet win screen (after the post-win ad; the ad froze twice) and whether any loss exists; Onet: find when the greyed freeze-time tool becomes usable (timed levels or a level number) |  |
| [Mini-game: Mahjong](features/mg-mahjong.md) |  | ✅ documented | 9 / 9 |  | 10.8.1 |
| [Mini-game: Sudoku](features/mg-sudoku.md) |  | ✅ documented | 9 / 9 | Sudoku: tap Yes on the leave dialog in L2, reopen Sudoku from More Games and record whether L2 resumes with its filled cells and timer or starts fresh | 10.8.1 |
| [Mini-game: Block Slide](features/mg-block-slide.md) |  | ✅ documented | 8 / 8 |  | 10.8.1 |
| [Interstitial ad during classic play](features/ad-interstitial-classic.md) |  | ✅ documented | 10 / 10 |  | 10.8.1 |
| [Home menu](features/home-menu.md) | classic best 2516 | ✅ documented | 6 / 6 |  | 10.8.1 |
| [Adventure mode](features/adventure.md) | classic best 2516 | ✅ documented | 13 / 13 | Adventure: tap Retry on the loss panel and Next Level on the win panel; gear > Replay inside a level; Adventure: does a result 4.0-4.3 min after an ad's close get an interstitial (window 3.8 none / 4.7 ad)? | 10.8.1 |
| [Medal](features/medal.md) | classic best 2516 | ✅ documented | 8 / 8 |  | 10.8.1 |
| [Consecutive Daily Victories](features/daily-victories.md) | classic best 2516 | 🛠 in progress | 10 / 13 | Run each outcome once under Consecutive Daily Victories: Leaving the app mid-game keeps the game; Consecutive Daily Victories: settled whether any classic game over or only a new classic best marks the day as won; Missed-day check: read the Consecutive Daily Victories counter the day after a full calendar day with no Classic game and no Adventure win |  |
| [Cross-promo icons on the home menu (GOGO! Blast, Rotate Rings)](features/cross-promo-home.md) | classic best 2516 | ✅ documented | 7 / 7 |  | 10.8.1 |
| [Adventure diamond-collection levels](features/adv-diamonds.md) | adventure 1 | 🛠 in progress | 13 / 15 | Run each outcome once under Adventure diamond-collection levels: Leaving the app mid-game keeps the game; Play Adventure levels 5-12 and record which have gem goals |  |
| [Adventure Consecutive Victories (win streak)](features/adv-win-streak.md) | adventure 1 | ✅ documented | 13 / 14 | Run each outcome once under Adventure Consecutive Victories (win streak): Leaving the app mid-game keeps the game | 10.8.1 |
| Adventure hard levels (Next Hard Level) | adventure L4 | 🛠 in progress | 8 / 16 | Run each outcome once under Adventure hard levels (Next Hard Level): Settings gear > Replay, No Space Left, Back key mid-game opens the home menu with no confirmation; whether the game in progress is kept is NOT verified, Leaving the app mid-game keeps the game; Lose Adventure hard level once (replay L5 or next hard) to see its fail screen and cost; Record which Adventure levels L6-L15 are hard (purple Next Hard Level on the previous win) |  |
| Rating prompt (rate us) | water sort L7 | 🛠 in progress | 7 / 8 | When does the Rating popup come up (first seen after the 6th game over of a session, 2239 points)?; Study Rating prompt (rate us): open it, walk its screens and tabs, verify its cases; Classic: does the Rating popup come back after a high-score game (the only popup followed a 2239-point game; 14 low-score game overs had none)? |  |
