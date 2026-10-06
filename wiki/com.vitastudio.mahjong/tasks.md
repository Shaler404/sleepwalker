# Tasks: Vita Mahjong

Status: **▶️ active** — ready now: 29

Mode: **goals** — work through the session goals in order; play levels only as far as an unlock or experiment goal needs; register anything new you notice as a feature or a goal, do not pursue it now

Progress reached: **level 21 (Hard L20 won)** · last new feature found at: **level 21 (Hard L20 won)**

Goals: study 7, unlock 1, experiment 21 · maps: level 19 (restored by Sync Data) — 11 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **core-match** — broken, solver, levels won 2, typical 16.2 min

Google Play version: **3.40.1** (checked 2026-10-05 22:05:43) · analyzed version: **3.40.1** · FTUE from a fresh install: **never**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| What Auto Complete does at the end of a level | experiment | [Auto Complete](features/auto-complete.md) | knowledge gap |  |
| Unlock Name colors: 8 achievement points for color 2 | unlock | [Name colors](features/name-colors.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Run each outcome once under Hard level: Restart in the Out of space window, Force-stop after one pair cleared (IQ 40.4), Restart row in the in-level Options | experiment | [Hard level](features/hard-level.md) | knowledge gap |  |
| Which home buttons appear as levels go up (shop, daily, events)? | experiment | [Home screen](features/home.md) | knowledge gap |  |
| Study Profile: open it, walk its screens and tabs, verify its cases | study | [Profile](features/profile.md) | external |  |
| Study Theme (tiles and background): open it, walk its screens and tabs, verify its cases | study | [Theme (tiles and background)](features/theme.md) | external |  |
| Study Settings: open it, walk its screens and tabs, verify its cases | study | [Settings](features/settings.md) | external |  |
| Study No Ads purchase: open it, walk its screens and tabs, verify its cases | study | [No Ads purchase](features/no-ads.md) | external |  |
| Tile set vs board: find whether the chosen tile set or the level decides the board's faces and face-down color | experiment | [Theme (tiles and background)](features/theme.md) | knowledge gap |  |
| Look for daily rewards or a daily challenge: open the game on a new day and check the home and launch popups | experiment | [Home screen](features/home.md) | knowledge gap |  |
| Find what an age bracket changes: pick 55+ on the age popup when it shows on a relaunch and compare the home and the next level to the X-closed runs | experiment | [Age selection](features/age-select.md) | knowledge gap |  |
| Find whether Shuffle turns face-down tiles face up (count the backs before and after one Shuffle) | experiment | [Boosters: Shuffle, Hint, Undo](features/boosters.md) | knowledge gap |  |
| Find what set the board's tiles on L19: purple backs in 195050, cream faces with red backs in 231804, no theme change in between | experiment | [Theme (tiles and background)](features/theme.md) | knowledge gap |  |
| Find why IQ bonus tiles appeared: tiles with a blue IQ+N banner (IQ+6, IQ+9 on L19, frames 6, 19); seen from level 8 in 20260930-225122 (IQ+10), first level not seen | experiment | IQ bonus tiles | knowledge gap |  |
| Study IQ bonus tiles: match an IQ+N tile pair and record how much the IQ score grows | experiment | IQ bonus tiles | knowledge gap |  |
| Find what Revive in the Out of space window costs (badge 5: a rewarded video or free revives) | experiment | [Tray mahjong level](features/core-level.md) | knowledge gap |  |
| Run each outcome once under Daily Victories streak: Restart in the Out of space window, Force-stop after one pair cleared (IQ 40.4), Restart row in the in-level Options | experiment | Daily Victories streak | knowledge gap |  |
| Daily Victories: see what the 10-day chest gives (a tap on the chest shows nothing) | experiment | Daily Victories streak | knowledge gap |  |
| See what Shuffle and Undo offer at 0 (as Hint: a video for 2?) | experiment | [Boosters: Shuffle, Hint, Undo](features/boosters.md) | knowledge gap |  |
| Find why Picture tiles (framed art, zodiac, blank card) appeared: ordinary pairs among tile faces; framed art first noted on L12-L19 | experiment | Picture tiles (framed art, zodiac, blank card) | knowledge gap |  |
| Study Picture tiles (framed art, zodiac, blank card): open it, walk its screens and tabs, verify its cases | study | Picture tiles (framed art, zodiac, blank card) | external |  |
| Hard every 10 levels: check that Level 30 is Hard (and L22-29 are not) | experiment | [Hard level](features/hard-level.md) | knowledge gap |  |
| Study spinning tiles (L21): how the spin works, what stops it | study | Spinning tiles | knowledge gap |  |
| Solver: read the 5th tile set (white faces, blue backs, Hard L20 of session 133525) - it read 'purple' and found no pair on shots 00005-00045 | experiment | [Tray mahjong level](features/core-level.md) | knowledge gap |  |
| Study Combo: what breaks the streak (a pause, a tray tile), whether a tier gives anything beyond the win-screen number, its first level | experiment | Combo streak | knowledge gap |  |
| Rate Us prompt: after closing it with X, does it come back on later wins (which level)? | experiment | Rate us button | knowledge gap |  |
| Study Notification prompt: open it, walk its screens and tabs, verify its cases | study | Notification prompt | external |  |
| Find what the x2 league tag on a normal Level button means: win L21 and count the 福 league points it adds | experiment | [Leagues](features/leagues.md) | knowledge gap |  |
| Check Level 20 frame in Frame tab and Save of an equipped frame | experiment | [Level avatar frames](features/level-frames.md) | knowledge gap |  |

## Waiting

| Task | Not before | Kind | Feature |
|---|---|---|---|
| Daily Victories: win a level tomorrow and see whether the streak shows 2 and how a missed day looks — day 1 of 2 | 2026-10-06 07:59:09 | daily | Daily Victories streak |
| Leagues: after the period ends (about 24h from 13:56 on 2026-10-05) mark the results screen, the reward and the new league | 2026-10-06 14:00:00 | check | [Leagues](features/leagues.md) |
| Daily Victories: win a level tomorrow and see whether the streak shows 2 and how a missed day looks — day 2 of 2 | 2026-10-07 07:59:09 | daily | Daily Victories streak |

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

| Task | What to provide | Feature |
|---|---|---|
| Check Terms/Privacy links on the consent window | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | [Terms consent](features/consent.md) |
| Replay the 3.40.1 FTUE on a fresh install with the cloud restore declined (levels 1-18 were skipped by Sync Data) | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone |  |

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Study In-level Options: open it, walk its screens and tabs, verify its cases | 2026-10-06 02:31:48 | 20261006-022624-chrono-2FYKPJ#21 | all rows and toggles walked on L21; toggles restored ON |
| Study Level avatar frames: open it, walk its screens and tabs, verify its cases | 2026-10-06 02:28:47 | 20261006-022624-chrono-2FYKPJ#6 | Profile Frame tab walked: Level section (10) and Default 6 colours, preview and X-discard verified; Save and L20 frame left as task |
| Study Loading screen: open it, walk its screens and tabs, verify its cases | 2026-10-06 02:27:18 | 20261006-022624-chrono-2FYKPJ#0 | Loading screen re-verified on 3.40.1: green screen, tagline, bar with tile icon, Games Today and Playing Now counters; all cases were closed earlier, frame marked |
| Study Hard level: open it, walk its screens and tabs, verify its cases | 2026-10-06 00:19:21 | 20261006-001538-chrono-2FYKPJ#13 | Hard L20 screens/cases were already marked earlier; chk-loss, retry, restart, exit-app, frequency need another Hard level (hard-l30 task, outcomes-hard-level). Today: L21 shows x2 tag but is a normal level |
| Study IQ score: open it, walk its screens and tabs, verify its cases | 2026-10-06 00:18:59 | 20261006-001538-chrono-2FYKPJ#12 | IQ counter: tap does nothing, +1.9 for first pair on L21 (40 to 41.9); no tiers/rewards seen |
| Study Leagues: open the home badge, mark the full board and the rewards per rank, promotion and relegation | 2026-10-06 00:17:57 | 20261006-001538-chrono-2FYKPJ#8 | Board, info pages, trophy carousel marked; end-of-period contents left to leagues-period-end |
| Study How to Play: open it, walk its screens and tabs, verify its cases | 2026-10-05 22:13:40 | 20261005-221108-chrono-2FYKPJ#9 | Re-walked on 3.40.1 (L21 Options): 2 pages, X closes to level, matches wiki; marked page 1/2. |
| Study Daily Victories: chests at 10/20/30, earn leaves by winning daily | 2026-10-05 22:12:38 | 20261005-221108-chrono-2FYKPJ#3 | Re-walked screen: streak 1, 10/20/30 chests, chest tap gives no preview, month arrow no change. Rewards/break/save still need days (dv-chest-10, dv-day2). |
| First look at Leagues: open it once, record what it is and decide whether it needs a full study | 2026-10-05 14:02:36 | 20261005-133525-chrono-2FYKPJ#41 | Leagues: Bronze of 5 tiers, groups of 50, 福 tiles = points (Hard x2), ~24h period, home badge entry; needs a full study (rewards, end of period) |
| Find why Level avatar frames appeared: earned at level milestones: a frame badged 10 is owned at level 19, so likely one frame per 10 levels | 2026-10-05 14:02:17 | planner | the trigger is recorded as a fact: the level chest at L20 gave a 'Level 20' avatar frame: frames come from the 10-level chests [20261005-133525-chrono-2FYKPJ#46] |
| Study Level progress chest: open it, walk its screens and tabs, verify its cases | 2026-10-05 14:02:17 | 20261005-133525-chrono-2FYKPJ#47 | All checklist items closed: earned per won level, chest every 10 levels, L20 contents Hint/frame/Undo, Collect x2 by video |
| Open the level progress chest: win Level 20 and mark what the chest gives and how the bar restarts | 2026-10-05 14:02:14 | 20261005-133525-chrono-2FYKPJ#46 | Bar filled on the L20 win (one segment per won level, chest at the 10th); chest gave Hint x1, Level-20 avatar frame, Undo x1 (Collect x2 by rewarded video); bar resets to 'Reach Level 30' [20261005-133525-chrono-2FYKPJ#45-47] |
| Win Hard Level 20: its win screen and reward vs the base; then L21 and whether Hard repeats every 10 levels | 2026-10-05 13:56:50 | 20261005-133525-chrono-2FYKPJ#49 | Hard L20 won (steps ~5-46): post-win order = league standing (rank 18, +8 福 since Hard tag x2) > notification pitch > Daily Victories panel > win screen 'Legendary!' with 'You cleared HARD level so fast' (Time/IQ/Combo) > Rate Us > level chest (Hint, L20 avatar frame, Undo; Collect x2 by video). Next chest 'Reach Level 30'. L21 is a normal level (orange button, no Hard) with a new element: spinning tiles. Hard seen at L10 and L20: every 10 levels is likely, L30 to confirm (task hard-l30). |
| Find why Leagues appeared: not seen on the home screen at level 19; the Achievements screen lists League Reached and 1st-place finishes, so leagues open later, probably at a level threshold | 2026-10-05 13:36:02 | planner | the trigger is recorded as a fact: popup on the first launch after winning L19 (progress level 20 Hard) [20261005-133525-chrono-2FYKPJ#0] |
| Unlock Leagues: not shown; guess about level 30 | 2026-10-05 13:36:02 | planner | seen open at level 20 (Hard), L19 won |
| Study Face-down backs (flip tiles): open it, walk its screens and tabs, verify its cases (cancelled) | 2026-10-05 13:35:54 | review-20261005 | Duplicate: face-down-backs is the face-down-tiles feature (documented) registered again by session 20261005-133404-chrono-2FYKPJ#0 |
| List the level elements of the tray level (face-down backs, picture tiles, IQ+ tiles) as level-element features with their first level | 2026-10-05 13:34:32 | 20261005-133404-chrono-2FYKPJ#0 | Level elements registered: face-down-backs (from L11, flip in place, no tray slot), picture-tiles (framed art, zodiac, blank card; first level unknown, L12-L19 notes), iq-bonus-tiles (already registered, IQ+N). Appeared-why for picture tiles left as a task. |
| Look for the booster refill: what Shuffle, Hint or Undo offer when a count is 0 (rewarded ad, coins, shop) | 2026-10-05 08:05:46 | 20261005-073804-chrono-2FYKPJ#53 | Hint at 0 offers a rewarded video for 2 Hints (Free Hint window); Shuffle and Undo at 0 not reached yet |
| Find whether a Daily Victories chest (10/20/30) shows its reward before it is reached | 2026-10-05 08:05:45 | 20261005-073804-chrono-2FYKPJ#57 | a tap on the 10-day chest at streak 1 (and at 0 earlier) opens nothing; long-press not tried; contents left to dv-chest-10 |
| Find what the bright calendar days in Daily Victories mean (01-05 bright at a 0 day streak) | 2026-10-05 08:05:44 | 20261005-073804-chrono-2FYKPJ#56 | after the win, 05 turns gold (won day) while 01-04 stay bright though no session ran on 01-02: bright = past days of the month, gold = a won day |
| Find what earns leaves: compare the home leaf counter (x0) before and after a won level | 2026-10-05 08:05:43 | 20261005-073804-chrono-2FYKPJ#55 | home leaf counter x0 before, x1 after the first win of the day (L19); the leaf count is the Daily Victories day streak (panel at #46, calendar '1 day streak!' at #56) |
| Find why Hard level appeared: level 10 was marked Hard in earlier sessions on 3.39.1; not reseen on 3.40.1 | 2026-10-05 08:05:42 | planner | the trigger is recorded as a fact: announced on the level 19 win screen: the next-level button turns red 'Level 20 / Hard'; the Hard banner shows when Level 20 opens [20261005-073804-chrono-2FYKPJ#47] |
| Reach and study a Hard level (L10 was Hard on 3.39.1; reach L20+ on 3.40.1) | 2026-10-05 08:05:41 | 20261005-073804-chrono-2FYKPJ#49 | Level 20 is Hard on 3.40.1: red Hard banner 'Even pros sweat here.', board marked |
| Win a level: win screen, rewards (needs solver for core-match) | 2026-10-05 08:05:41 | 20261005-073804-chrono-2FYKPJ#47 | L19 won; win screen marked: Brilliant!, Time/IQ/Combo, holder line, 10-segment chest bar 'Reach Level 20', red Level 20 Hard button; no coins |
| Study Tray mahjong level: open it, walk its screens and tabs, verify its cases | 2026-10-05 08:00:59 | 20261005-073804-chrono-2FYKPJ#60 | chk-win verified: L19 won (14:12, IQ 154.8, combo 23): fade replay, Daily Victories panel (leaf +1), win screen Brilliant! with Time/IQ/Combo, holder line, 10-segment chest bar 'Reach Level 20', next button Level 20 Hard. chk-elements left to task elements-core |
| Study the home leaf counter: tap it, mark what opens, and record what leaves are for | 2026-10-05 07:38:39 | 20261005-073409-chrono-2FYKPJ#2 | Leaf counter tapped: opens Daily Victories, the counter is the day streak (x0 = 0 day streak); sources and sinks stay with leaves-earn and study-daily-victories |
| Study Home screen: open it, walk its screens and tabs, verify its cases | 2026-10-05 07:36:52 | 20261005-073409-chrono-2FYKPJ#6 | Entries, badges, changes verified; found Daily Victories behind the leaf counter (new feature daily-victories) |
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
