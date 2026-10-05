# Tasks: Vita Mahjong

Status: **▶️ active** — ready now: 33

Mode: **goals** — work through the session goals in order; play levels only as far as an unlock or experiment goal needs; register anything new you notice as a feature or a goal, do not pursue it now

Progress reached: **level 19 (restored from the cloud save on a fresh install)** · last new feature found at: **level 19 (restored from the cloud save on a fresh install)**

Goals: study 13, unlock 3, experiment 17 · maps: level 19 (restored by Sync Data) — 11 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **core-match** — broken, solver, levels won 0

Google Play version: **3.40.1** (checked 2026-10-05 00:13:01) · analyzed version: **3.40.1** · FTUE from a fresh install: **never**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Find why Level avatar frames appeared: earned at level milestones: a frame badged 10 is owned at level 19, so likely one frame per 10 levels | experiment | [Level avatar frames](features/level-frames.md) | knowledge gap |  |
| What Auto Complete does at the end of a level | experiment | [Auto Complete](features/auto-complete.md) | knowledge gap |  |
| Find why Leagues appeared: not seen on the home screen at level 19; the Achievements screen lists League Reached and 1st-place finishes, so leagues open later, probably at a level threshold | experiment | [Leagues](features/leagues.md) | knowledge gap |  |
| Unlock Name colors: 8 achievement points for color 2 | unlock | [Name colors](features/name-colors.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Unlock Leagues: not shown; guess about level 30 | unlock | [Leagues](features/leagues.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Run each outcome once under Hard level: Back arrow in the level goes straight to the home screen, no confirmation, no cost seen (board kept, per earlier sessions), Win, Restart in the Out of space window, Force-stop after one pair cleared (IQ 40.4), Out of space | experiment | [Hard level](features/hard-level.md) | knowledge gap |  |
| Which home buttons appear as levels go up (shop, daily, events)? | experiment | [Home screen](features/home.md) | knowledge gap |  |
| Study Loading screen: open it, walk its screens and tabs, verify its cases | study | [Loading screen](features/loading.md) | external |  |
| Study Home screen: open it, walk its screens and tabs, verify its cases | study | [Home screen](features/home.md) | external |  |
| Study Profile: open it, walk its screens and tabs, verify its cases | study | [Profile](features/profile.md) | external |  |
| Study Level avatar frames: open it, walk its screens and tabs, verify its cases | study | [Level avatar frames](features/level-frames.md) | external |  |
| Study Theme (tiles and background): open it, walk its screens and tabs, verify its cases | study | [Theme (tiles and background)](features/theme.md) | external |  |
| Study Settings: open it, walk its screens and tabs, verify its cases | study | [Settings](features/settings.md) | external |  |
| Study Tray mahjong level: open it, walk its screens and tabs, verify its cases | study | [Tray mahjong level](features/core-level.md) | external |  |
| Study IQ score: open it, walk its screens and tabs, verify its cases | study | [IQ score](features/iq-score.md) | external |  |
| Study In-level Options: open it, walk its screens and tabs, verify its cases | study | [In-level Options](features/level-options.md) | external |  |
| Study No Ads purchase: open it, walk its screens and tabs, verify its cases | study | [No Ads purchase](features/no-ads.md) | external |  |
| Study How to Play: open it, walk its screens and tabs, verify its cases | study | [How to Play](features/how-to-play.md) | external |  |
| Study Hard level: open it, walk its screens and tabs, verify its cases | study | [Hard level](features/hard-level.md) | external |  |
| Tile set vs board: find whether the chosen tile set or the level decides the board's faces and face-down color | experiment | [Theme (tiles and background)](features/theme.md) | knowledge gap |  |
| Look for the booster refill: what Shuffle, Hint or Undo offer when a count is 0 (rewarded ad, coins, shop) | experiment | [Boosters: Shuffle, Hint, Undo](features/boosters.md) | knowledge gap |  |
| Look for daily rewards or a daily challenge: open the game on a new day and check the home and launch popups | experiment | [Home screen](features/home.md) | knowledge gap |  |
| Find what an age bracket changes: pick 55+ on the age popup when it shows on a relaunch and compare the home and the next level to the X-closed runs | experiment | [Age selection](features/age-select.md) | knowledge gap |  |
| Find whether Shuffle turns face-down tiles face up (count the backs before and after one Shuffle) | experiment | [Boosters: Shuffle, Hint, Undo](features/boosters.md) | knowledge gap |  |
| Find what set the board's tiles on L19: purple backs in 195050, cream faces with red backs in 231804, no theme change in between | experiment | [Theme (tiles and background)](features/theme.md) | knowledge gap |  |
| Find why Hard level appeared: level 10 was marked Hard in earlier sessions on 3.39.1; not reseen on 3.40.1 | experiment | [Hard level](features/hard-level.md) | knowledge gap |  |
| Reach and study a Hard level (L10 was Hard on 3.39.1; reach L20+ on 3.40.1) | unlock | [Hard level](features/hard-level.md) | knowledge gap |  |
| Win a level: win screen, rewards (needs solver for core-match) | experiment | [Tray mahjong level](features/core-level.md) | knowledge gap |  |
| Find why IQ bonus tiles appeared: tiles with a blue IQ+N banner (IQ+6, IQ+9 on L19, frames 6, 19); seen from level 8 in 20260930-225122 (IQ+10), first level not seen | experiment | IQ bonus tiles | knowledge gap |  |
| Study the home leaf counter: tap it, mark what opens, and record what leaves are for | study | Leaf counter (home) | knowledge gap |  |
| Study IQ bonus tiles: match an IQ+N tile pair and record how much the IQ score grows | experiment | IQ bonus tiles | knowledge gap |  |
| Find what Revive in the Out of space window costs (badge 5: a rewarded video or free revives) | experiment | [Tray mahjong level](features/core-level.md) | knowledge gap |  |
| Find what earns leaves: compare the home leaf counter (x0) before and after a won level | experiment | Leaf counter (home) | knowledge gap |  |

## Waiting

None.

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

| Task | What to provide | Feature |
|---|---|---|
| Check Terms/Privacy links on the consent window | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | [Terms consent](features/consent.md) |
| Replay the 3.40.1 FTUE on a fresh install with the cloud restore declined (levels 1-18 were skipped by Sync Data) | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone |  |

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Find whether every relaunch starts the game at Level 1 with the age and saved-game prompts, and whether Sync always restores the current level | 2026-10-05 00:31:23 | 20261005-002327-chrono-2FYKPJ#10 | Both launches of 002327 (frames 3 and 15) opened on Level 1 with the saved-game popup and Sync Data returned Level 19; the age popup did NOT show on either launch (it did in earlier sessions) |
| Reach a level loss on purpose and record the lose screen (tray full), its continue offer and retry cost | 2026-10-05 00:31:22 | 20261005-002327-chrono-2FYKPJ#13 | Out of space at 4 distinct tiles in the tray (frames 8-10): Revive (badge 5), -4 to revive (4 Undo), Restart free; chk-loss, chk-retry closed, out-of-space is an outcome |
| Does a relaunch or restore regenerate the L19 board (layout and back art changed between 231301 shot 22 and 231804 shot 8)? | 2026-10-05 00:31:22 | 20261005-002327-chrono-2FYKPJ#13 | Restart from Out of space (frame 12) and force-stop + Sync (frame 19) both open a new L19 layout with a different tile/back set; board progress not kept |
| Study Face-down tiles: open it, walk its screens and tabs, verify its cases | 2026-10-05 00:28:31 | 20261005-002327-chrono-2FYKPJ#13 | 6/7 cases; entry, rules, interactions, loss verified on L19 green set |
| Study Terms consent: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:20:26 | 20261003-231804-chrono-2FYKPJ#8 | Consent not shown this launch (only on first launch); cannot reverify now, needs a fresh install |
| Study Saved game sync: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:20:26 | 20261003-231804-chrono-2FYKPJ#8 | Prompt reappeared on a reset install; Start Over shows confirm, No kept level 19 (restored) |
| Study Boosters: Shuffle, Hint, Undo: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:20:25 | 20261003-231804-chrono-2FYKPJ#8 | Hint/Undo/Shuffle each used once, counts drop by 1; empty/refill left to booster-refill |
| Does the chosen age bracket change anything (tile size, difficulty, ads)? (cancelled) | 2026-10-03 23:19:16 | 20261003-231301-chrono-2FYKPJ#1 | superseded by age-bracket-effect: the age popup returns on relaunch of the progressed phone, so the test does not need a fresh install |
| How many achievement points one achievement gives | 2026-10-03 23:19:06 | 20261003-231301-chrono-2FYKPJ#11 | Medal detail reads '+1 Achievement Points' (First-Try Wins 30); the bar is empty, next name color at 8 points, so color 2 needs 8 medals. The bar's fill after a first medal is left to unlock-name-colors |
| Study Age selection: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:17:29 | 20261003-231301-chrono-2FYKPJ#21 | Popup appeared again on a relaunch of the progressed phone (home showed Level 1) before the sync offer; close X verified; bracket choice effect left to age-select-effect (fresh) |
| Study Auto Complete: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:17:11 | 20261003-231301-chrono-2FYKPJ#20 | Toggle verified ON/OFF/ON; actual auto-clear behavior left to auto-complete-check |
| Study Achievements: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:16:07 | 20261003-231301-chrono-2FYKPJ#14 | Walked the screen, both scroll pages, info (Name Colors) popup, medal detail; marked all |
| A new avatar frame at level 20 or 30? (cancelled) | 2026-10-03 20:02:44 | review-20261003 | duplicate of appeared-level-frames (same hypothesis: a level frame per 10 levels, check after L20/L30) |
| Leagues open at some level after 19 (Achievements list League Reached)? (cancelled) | 2026-10-03 20:02:44 | review-20261003 | duplicate of appeared-leagues and unlock-leagues (same question: the level where Leagues opens) |
| Study Rate us button: open it, walk its screens and tabs, verify its cases (cancelled) | 2026-10-03 20:02:43 | review-20261003 | rate-us was registered by mistake: the thumbs-up/star button opens Achievements (feature achievements, entry marked at 20261003-195050-chrono-2FYKPJ#23); duplicate to merge |
| Map the game: play until the main menu and every entry point is visible; list each entry point as open (a study goal), locked with its unlock condition (an unlock goal) or unclear (an experiment) | 2026-10-03 19:59:36 | 20261003-195050-chrono-2FYKPJ#28 | Fresh reinstall; Sync Data restored level 19 with no account. Home at L19: avatar/Profile (Avatar, Frame tabs), Achievements (appears after leaving a level), Theme (6 tile sets, 5 backgrounds, all free), Settings (Save progress sign-in, About 3.40.1), Level 19. In level: IQ score, 4-slot tray, Shuffle 3/Hint 5/Undo 10, Options (Auto Complete, Colorful Effects, How to Play 2 pages, No Ads, Restart). Locked: Name colors (8 achievement points), Leagues (guess, not shown). No shop/daily/events at L19. |
