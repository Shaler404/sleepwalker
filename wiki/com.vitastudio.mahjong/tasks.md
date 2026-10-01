# Tasks: Vita Mahjong

Status: **▶️ active** — ready now: 11

Mode: **advance** — move through the content as fast as possible; register every new feature and write down every branch as a case or task for later, do not test them now

Progress reached: **level 14** · last new feature found at: **level 12**

Screen surveys: level 3 — 0 new, level 12 — 0 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **core-match** — broken, manual, levels won 11, typical 11.7 min

Google Play version: **3.39.1** (checked 2026-10-01 02:46:28) · analyzed version: **3.39.1** · FTUE from a fresh install: **2026-10-01**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Analyze the game, version 3.39.1 | analysis |  | external | find all features and work through all user cases |
| Auto Complete: find the trigger condition (tile count / all tiles uncovered) on a later level; compare a level end with Auto Complete OFF | check | [Auto Complete option](features/auto-complete.md) | from the game |  |
| Find the next Hard level (after L11) and check whether a win-streak banner or reward appears; record the Hard level interval | check | [Hard levels](features/hard-levels.md) | from the game |  |
| Rewarded ads: check Undo and Shuffle '+' with stock 0 (video offer? how many), and whether Free Hint videos have a daily cap | check | [Rewarded ads (video Revive and other placements)](features/rewarded-ads.md) | from the game |  |
| Make core-match fast: test the board-JSON solver (the local draft) on a simple board or add image tile detection; L12 took 28 min by eye | check | [Core loop: tile matching](features/core-match.md) | from the game |  |
| Continue L14+: Hard level interval, what grants Elite x2, Auto Complete trigger, level chest at L20 | check | [FTUE / tutorial levels](features/ftue.md) | knowledge gap |  |
| Settle the face-down green rule: with an empty tray tap one clearly free green once and take a frame | check | [Face-down green tiles (flip on tap)](features/hidden-tiles.md) | knowledge gap |  |
| League board: the own-row chevron, a tap on another player, the league names above Gold | check | [Leagues](features/leagues.md) | knowledge gap |  |
| Look for interstitial ads between levels and record when they appear | check | [Rewarded ads (video Revive and other placements)](features/rewarded-ads.md) | knowledge gap |  |
| Find what decides the win title (Intelligent, Brilliant, Perceptive, Genius): IQ, combo or time | check | [Core loop: tile matching](features/core-match.md) | knowledge gap |  |
| Look for a shop, starter or limited offers and a language setting (genre checklist) | check | [Settings](features/settings.md) | knowledge gap |  |

## Waiting

| Task | Not before | Kind | Feature |
|---|---|---|---|
| League event end: open the game after the Bronze League timer ends and record the rank, promotion and rewards | 2026-10-02 00:34:13 | check | [Leagues](features/leagues.md) |
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
