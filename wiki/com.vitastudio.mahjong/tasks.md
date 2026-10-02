# Tasks: Vita Mahjong

Status: **▶️ active** — ready now: 29

Mode: **goals** — work through the session goals in order; play levels only as far as an unlock or experiment goal needs; register anything new you notice as a feature or a goal, do not pursue it now

Progress reached: **level 18 won, at Level 19** · last new feature found at: **level 12**

Goals: study 16, experiment 1 · maps: level 3 — 0 new, level 12 — 0 new, level 15 (open) — 0 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **core-match** — broken, solver, levels won 16, typical 14.1 min

Google Play version: **3.39.1** (checked 2026-10-01 20:09:25) · analyzed version: **3.39.1** · FTUE from a fresh install: **2026-10-01**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Auto Complete: find the trigger condition (tile count / all tiles uncovered) on a later level; compare a level end with Auto Complete OFF | check | [Auto Complete option](features/auto-complete.md) | from the game |  |
| League event end: open the game after the Bronze League timer ends and record the rank, promotion and rewards | check | [Leagues](features/leagues.md) | from the game |  |
| Find the next Hard level (after L11) and check whether a win-streak banner or reward appears; record the Hard level interval | check | [Hard levels](features/hard-levels.md) | from the game |  |
| League board: the own-row chevron, a tap on another player, the league names above Gold | check | [Leagues](features/leagues.md) | knowledge gap |  |
| Look for interstitial ads between levels and record when they appear | check | [Rewarded ads (video Revive and other placements)](features/rewarded-ads.md) | knowledge gap |  |
| Find what decides the win title (Intelligent, Brilliant, Perceptive, Genius): IQ, combo or time | check | [Core loop: tile matching](features/core-match.md) | knowledge gap |  |
| Look for a shop, starter or limited offers and a language setting (genre checklist) | check | [Settings](features/settings.md) | knowledge gap |  |
| Study Main screen: open it, walk its screens and tabs, verify its cases | study | Main screen | external |  |
| Study Profile / avatar: open it, walk its screens and tabs, verify its cases | study | Profile / avatar | external |  |
| Study Save progress / account sign-in: open it, walk its screens and tabs, verify its cases | study | Save progress / account sign-in | external |  |
| Study Core loop: tile matching: open it, walk its screens and tabs, verify its cases | study | [Core loop: tile matching](features/core-match.md) | external |  |
| Study Combo tiers (shown by the tray border): open it, walk its screens and tabs, verify its cases | study | [Combo tiers (shown by the tray border)](features/combo.md) | external |  |
| Study No Ads purchase: open it, walk its screens and tabs, verify its cases | study | [No Ads purchase](features/no-ads.md) | external |  |
| Study Auto Complete option: open it, walk its screens and tabs, verify its cases | study | [Auto Complete option](features/auto-complete.md) | external |  |
| Study Leagues: open it, walk its screens and tabs, verify its cases | study | [Leagues](features/leagues.md) | external |  |
| Study Level milestone chest (Reach Level 10): open it, walk its screens and tabs, verify its cases | study | [Level milestone chest (Reach Level 10)](features/level-chest.md) | external |  |
| Study Level button badge (panda tile + padlock): open it, walk its screens and tabs, verify its cases | study | Level button badge (panda tile + padlock) | external |  |
| Study Hard levels: open it, walk its screens and tabs, verify its cases | study | [Hard levels](features/hard-levels.md) | external |  |
| Study Live player ticker banner: open it, walk its screens and tabs, verify its cases | study | Live player ticker banner | external |  |
| Study Daily Victories (daily win streak calendar): open it, walk its screens and tabs, verify its cases | study | [Daily Victories (daily win streak calendar)](features/daily-victories.md) | external |  |
| Study Face-down green tiles (flip on tap): open it, walk its screens and tabs, verify its cases | study | [Face-down green tiles (flip on tap)](features/hidden-tiles.md) | external |  |
| Study Notification opt-in prompt: open it, walk its screens and tabs, verify its cases | study | Notification opt-in prompt | external |  |
| Study Rewarded ads (video Revive and other placements): open it, walk its screens and tabs, verify its cases | study | [Rewarded ads (video Revive and other placements)](features/rewarded-ads.md) | external |  |
| Look for timed events, daily quests and social features (friends, teams, gifting) on the main screen at L18-L25; done when each is seen or recorded as absent at L25 | experiment | Main screen | knowledge gap |  |
| Win L19 and L20 (L19 is a dense board, not Hard): open the level chest at L20 and record its reward, check the Profile Frame tab for a level-20 frame, and note whether L20 is Hard and whether an interstitial shows between levels | from scratch | [Level milestone chest (Reach Level 10)](features/level-chest.md) | knowledge gap | Progress: L18 won, at Level 19; chest 8/10 toward L20 [#72]. Session 20261001-211823 already handed off on L19 after 6 solver taps. |
| Make core-match fast: the solver reads blank cards, golden/framed faces and every tray tile, flips one free green per round with a rescan, and sends each certain pair as one call (target under 5 min a level) | check | [Core loop: tile matching](features/core-match.md) | knowledge gap | Typical level 14 min (L14-L18), budget 5. L18 at one tap per call: ~10.5 s per tap+wait, about 2x slower per tile than batches [s:20261001-205148-chrono-2FYKPJ#29]. The solver misses blank cards [s:20261001-211823-chrono-2FYKPJ#3] and read the tray blender as "?" [s:20261001-205148-chrono-2FYKPJ#1]. |
| Check whether quitting a level from Out of space always restores the last saved board, and when the save is written | check | [Core loop: tile matching](features/core-match.md) | knowledge gap |  |
| Re-test a tile whose bottom edge is cut by a higher neighbour in the next row: does a tap take it into the tray or show Locked? Record the frame | check | [Core loop: tile matching](features/core-match.md) | knowledge gap |  |
| League board: tap a heart on another player's row and on the own row; record what the count means | check | [Leagues](features/leagues.md) | knowledge gap |  |

## Waiting

| Task | Not before | Kind | Feature |
|---|---|---|---|
| Win a level on the 4th day of the Daily Victories week (Saturday) and record the gift | 2026-10-03 10:00:00 | check | [Daily Victories (daily win streak calendar)](features/daily-victories.md) |
| Win a level on the 7th day of the Daily Victories week (Tuesday) and record the gift | 2026-10-06 10:00:00 | check | [Daily Victories (daily win streak calendar)](features/daily-victories.md) |
| Daily Victories: open the 10-won-days chest | 2026-10-10 10:00:00 | daily | [Daily Victories (daily win streak calendar)](features/daily-victories.md) |

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

| Task | What to provide | Feature |
|---|---|---|
| How Daily Victories starts: is it shown from day 1 on a fresh install? | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | [Daily Victories (daily win streak calendar)](features/daily-victories.md) |

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Make core-match fast: test the board-JSON solver (the local draft) on a simple board or add image tile detection; L12 took 28 min by eye (cancelled) | 2026-10-02 00:00:00 |  | Obsolete: the board-JSON draft was replaced by a screenshot solver (lab 2026-10-01) that still stalled on L18 and L19 [s:20261001-204654-chrono-2FYKPJ#10] [s:20261001-211823-chrono-2FYKPJ#6]; superseded by core-match-fast. |
| Win L18 (now on Out of space with a full tray: take Restart, or Revive by video) and continue to L20: level chest at L20, next Hard level, Elite x2 source, Auto Complete trigger | 2026-10-01 21:17:18 | 20261001-205148-chrono-2FYKPJ#74 | L18 won (resumed at ~45%, about 22 min incl. 2 video ads; title Intelligent!, IQ 134.1, combo 31). Now at Level 19. |
| Resume L18 (open ~45%, tray blender + 4-circle, all boosters 0; the 4-circle twin sits between two face-down greens) and continue to L20: level chest at L20, Hard interval, Elite x2 source (cancelled) | 2026-10-01 20:51:35 | 20261001-204654-chrono-2FYKPJ#10 | Superseded: the app relaunch restarted L18 from scratch, so the described ~45% board no longer exists; the replay ended at Out of space (tray blender, 4-circle, mixer, cat). Replaced by continue-ftue-lv18b. Correction (dream 2026-10-02): the ~45% board was not gone; 204654 opened on it [s:20261001-204654-chrono-2FYKPJ#2] and lost it to Out of space, and the quit restored it for 205148 [s:20261001-205148-chrono-2FYKPJ#1]; the goal was carried out by continue-ftue-lv18b. |
| Settle the face-down green rule: with an empty tray tap one clearly free green once and take a frame | 2026-10-01 11:42:28 | 20261001-110957-chrono-2FYKPJ#71 | Settled on L17 with an empty tray: a tap on a free green flips it face-up in place, no tray slot. Only one green is face-up at a time (flipping another turns the previous one back). A tap on a green whose face was already seen sends it straight into the tray (and matches if its twin is there). |
| Resume L17 (open ~45%, tray ring-bamboo, all boosters 0) and continue to L20: level chest at L20, Hard interval, Elite x2 source | 2026-10-01 11:42:28 | 20261001-110957-chrono-2FYKPJ#71 | L17 restarted from scratch on launch (half-played board not kept after relaunch); won in 13.9 min (Brilliant, IQ 137.2, combo 27). L18 is not Hard; played to ~45% and left open (board kept on back-arrow exit). Level chest 7/10 toward L20. |
| Resume L15 (open at ~60%, tray chips + 2-bamboo) and continue to L20: level chest at L20, Hard interval, Elite x2 source | 2026-10-01 09:13:06 | 20261001-083725-chrono-2FYKPJ#83 | L15 won on resume (9.2 min), L16 won (13.7 min, 2nd place in Bronze League, 26 pts), L17 left open at ~45%. L15-L17 are not Hard (last Hard: L10). No Elite x2 tag. Level chest 7/10 toward L20. Auto Complete did not fire on L15/L16. |
| Survey every screen: capture all entry points and map them to features | 2026-10-01 08:41:40 | 20261001-083725-chrono-2FYKPJ#17 | Walked: launch reward popup, main, Daily Victories (leaf x2 banner), Profile (Avatar/Frame), Achievements (thumbs-up; 5 sections), Theme (Tiles/Background), Settings, Bronze League. All entries map to known features; nothing new. Theme shows face-down green tiles are the Simple theme tile back. |
| Rewarded ads: check Undo and Shuffle '+' with stock 0 (video offer? how many), and whether Free Hint videos have a daily cap | 2026-10-01 07:03:53 | 20261001-063226-chrono-2FYKPJ#64 | Undo '+' at stock 0: Free Undo, 1 video = 2 Undos. Shuffle '+' at stock 0: Free Shuffle, 1 video = 1 Shuffle. Hint: 9th Free Hint video on 2026-10-01 still gave 2 Hints - no daily cap up to 9/day. |
| Continue L14+: Hard level interval, what grants Elite x2, Auto Complete trigger, level chest at L20 | 2026-10-01 07:03:53 | 20261001-063226-chrono-2FYKPJ#64 | L14 won (12:26, IQ 156.6, combo 32, no Hard, no Elite x2, +4 league for one 福 pair, chest 4/10). L15 not Hard either, left open at ~60% (resumes). Auto Complete did not fire on L14. |
| Finish level 12 (resume or restart) and continue L13+: Elite x2 tag, Hard level interval, league rank, Auto Complete trigger | 2026-10-01 03:52:34 | 20261001-031723-chrono-2FYKPJ#96 | L12 resumed after restart and won (30:29 total), L13 won (15:04). Elite x2 tag on L12-L13, gone on L14. No Hard levels at L12-13. League: 16 points, rank 48 -> 42, 'You're 38 away from ranking up'. Auto Complete did not fire on either level. |
| Continue from level 12: play L12+ with the x2 Elite tag, watch for shop/events/new tile types, record league rank changes | 2026-10-01 01:34:21 | 20261001-010125-chrono-2FYKPJ#72 | L12 played but not won (quit at 27.7 min, ~60% cleared). Seen: many face-down green tiles (free = straight into tray, locked = peek face), IQ+5 strawberry, golden Elite tile, Revive via video, Free Hint videos (2 hints each). League rank 46/50 with 4 points before L12. No shop/events on main at L12. Continue in continue-ftue-lv12b |
| Survey every screen: capture all entry points and map them to features | 2026-10-01 01:05:02 | 20261001-010125-chrono-2FYKPJ#14 | Walked main at L12 (leaf x2 pill = Daily Victories monthly calendar with 10/20/30-day chests; league badge -> Bronze board rank 46, info 2 pages incl. Glory star tiers, ladder Bronze/Silver/Gold/...; profile Frame tab has a new Level-10 frame). No new features, all entries map to daily-victories, leagues, profile, rate-us, themes, settings |
| Find when leagues / 1st-place competition unlock and document them | 2026-10-01 00:35:35 | 20260930-235817-chrono-2FYKPJ#67 | Leagues unlock after winning L10 (the first Hard level): Bronze League intro popup on the Level 11 tap, matchmaking into a group of 50, mid-level tutorial after the first Elite Tile pair, leaderboard with a ~24 h timer, Top 10 promoted. 5 tiers shown (bronze, gold, jade, amethyst, crowned king) |
| Read the full 'Hard levels' streak banner and document Hard levels / win streak | 2026-10-01 00:35:35 | 20260930-235817-chrono-2FYKPJ#67 | Hard levels: L10 is the first Hard level. The previous win screen shows a red 'Level 10 / Hard' button; the level opens with a red flame 'Hard' banner; win text 'This HARD level was no match for your skills.' and the next Level button gets an x2 Elite Tile tag. No separate win-streak banner appeared this session (L9-L11) |
| Continue FTUE from level 9: win L9-L10, open the level-10 chest, find what the panda+padlock badge unlocks, watch for leagues/shop/events/Hard levels | 2026-10-01 00:35:34 | 20260930-235817-chrono-2FYKPJ#67 | L9 won (10.4 min), L10 (first Hard level: red 'Level 10 / Hard' button, flame 'Hard' intro banner) won 9.6 min, L11 won 12.3 min. Level-10 chest opened: +1 Hint, +1 Undo; next chest at L20. The panda+padlock badge was the locked league Elite Tile: after L10 the badge became a golden tile, Bronze League joined (group of 50, ~24 h event, top 10 promoted), Elite Tiles are golden tiles on the board; Hard win gives an x2 tag. New at L9: Daily Victories popup (first win of a calendar day). New at L11: face-down green tiles, notification prompt. No shop or events seen through L11 |
| IQ+N bonus tiles: record IQ before/after matching an IQ+8 pair | 2026-09-30 23:28:08 | 20260930-225122-chrono-2FYKPJ#76 | IQ+N is a blue badge on both tiles of one pair (IQ+5 on L7, IQ+10 on L8). Matching it moved the IQ bar by ~N IQ (IQ+5: ~12 px, IQ+10: ~27 px on the 918-px frame between the 40 and 90 marks, 2.56 px/IQ); normal pairs move it ~1 px. Final IQ L7 119.3, L8 101.7 |
| Continue FTUE from level 7: find what the panda-padlock badge on Level 7 means, open the level-10 chest, watch for leagues/shop/events/Hard levels | 2026-09-30 23:28:08 | 20260930-225122-chrono-2FYKPJ#76 | Levels 7 and 8 won, 9 quit mid-level. The panda+padlock badge stays on the Level 8 and Level 9 buttons and its meaning is still unknown: no tile, popup or unlock was tied to it on L7-L8. L7 brought golden carved tiles, 'official' face tiles and IQ+5 tiles; L8 had IQ+10; new win title 'Perceptive!' for a slow level. Chest bar is 8/10. No leagues, shop, events or Hard levels seen through L9 |
| Continue FTUE from level 2 (Classic tile set active): play to level 10, record shuffle unlock at Lv 6, level-10 chest reward, leagues/shop/events unlocks | 2026-09-30 22:49:56 | 20260930-221457-chrono-2FYKPJ#93 | Levels 3-6 won this session. Shuffle unlocks silently at level 6 (stock 3). No shop/leagues/events on main through level 6. After level 6 the Level 7 button shows a panda-tile + padlock badge. Chest 6/10; level-10 chest continues in continue-ftue-lv7. |
| Survey every screen: capture all entry points and map them to features | 2026-09-30 22:18:04 | 20260930-221457-chrono-2FYKPJ#11 | Walked main (avatar/profile incl. FB Connect tile, achievements full list, themes, settings, decorative medallion), level board HUD. Main screen at level 3 has only 4 icons + Level button; no shop, leagues, events, daily, currency. No new entry points. |
| Auto Complete: finish a level with Auto Complete ON and observe the auto finish; compare with OFF | 2026-09-30 22:13:35 | 20260930-214524-chrono-2FYKPJ#144 | Level 2 with Auto Complete ON: no auto finish with 4 free tiles and an empty tray (waited 8 s); finished by hand. Trigger condition unknown - follow-up task auto-complete-trigger |
| Colorful Effects OFF vs ON: compare combo tray colors and match effects | 2026-09-30 22:13:34 | 20260930-214524-chrono-2FYKPJ#144 | OFF on level 2, ON on level 3: shards white in both, combo tray blue/purple/gold in both; no visible difference in screenshots |
| Continue FTUE from level 1 (board half cleared): finish level 1, record win screen and what unlocks up to level 10 (shuffle at Lv 6, leagues, events, shop) (cancelled) | 2026-09-30 21:43:48 | 20260930-211039-chrono-2FYKPJ#148 | Level 1 part done (win screen recorded); superseded by continue-ftue-lv2 which starts from level 2 |
| Settings: toggles, Feedback, About, Share, How to Play, Auto Complete, tile set switch | 2026-09-30 21:43:47 | 20260930-211039-chrono-2FYKPJ#148 | Music toggle ON/OFF verified; About (v3.39.1, ToS, Privacy); Share opens Android share sheet; How to Play 2 pages; tile set Simple->Classic applied in level. Feedback/Facebook/social icons open external apps - not opened. Auto Complete left for a level end (new task) |
| Recheck Undo booster behaviour after a match | 2026-09-30 21:25:44 | 20260930-211039-chrono-2FYKPJ#80 | Undo returns the last tray tile to the board; with an empty tray (right after a completed pair) it is a no-op, which explains the earlier 'no effect' observations |
