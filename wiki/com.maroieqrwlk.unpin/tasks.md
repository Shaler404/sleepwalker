# Tasks: Pull the Pin

Status: **▶️ active** — ready now: 37

Mode: **goals** — work through the session goals in order; play levels only as far as an unlock or experiment goal needs; register anything new you notice as a feature or a goal, do not pursue it now

Progress reached: **level 15** · last new feature found at: **level 15**

Goals: study 14, unlock 8, experiment 15 · maps: level 3 — 6 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **pin-pull** — mastered, solver, levels won 16, typical 1.2 min

Google Play version: **241.5.2** (checked 2026-10-05 00:13:01) · analyzed version: **241.5.2** · FTUE from a fresh install: **2026-10-03**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Recheck the features on version 241.5.2 | recheck |  | external | a newer version is on Google Play: update the game on the phone, then recheck the documented features and look for new ones |
| Study Settings: open it, walk its screens and tabs, verify its cases | study | [Settings](features/settings.md) | external |  |
| Study Remove Ads: open it, walk its screens and tabs, verify its cases | study | [Remove Ads](features/no-ads.md) | external |  |
| Study Level path header: open it, walk its screens and tabs, verify its cases | study | [Level path header](features/level-path.md) | external |  |
| Study the notification prompt: whether it comes back after Don't allow | study | Notification permission prompt | knowledge gap |  |
| Run each outcome once under Multi Stage Level: Balls fell out | experiment | [Multi Stage Level](features/multi-stage.md) | knowledge gap | every known outcome of the base level was run under Multi Stage Level |
| Open the map chest (OPEN after the 15 min timer) | study | [Map chest with timer](features/map-chest.md) | knowledge gap |  |
| Run each outcome once under Hard levels (skull node): Restart icon opens 'You can do better!' (Restart / Continue); Continue closes it; Restart plays an interstitial (skip control opened the Play Store, launch returned) then reloads only the current stage, earlier stages stay ticked; no coin cost, Back arrow returns to the map at once, no confirmation, no cost; reopening via Play keeps the multi-stage progress (stage 4 of 4), The previous session left L10 at stage 4; after the app was closed and relaunched this session, L10 opened at stage 4 with stages 1-3 ticked | experiment | [Hard levels (skull node)](features/hard-levels.md) | knowledge gap |  |
| Run each outcome once under Bonus levels (character node): Win screen, Restart, Quit, Exit the app | experiment | [Bonus levels (character node)](features/bonus-levels.md) | knowledge gap |  |
| Unlock New Mode (key gate at level 17): 3 keys: the 3-key gate at the level 17 key node, 'Unlock New Mode' | unlock | New Mode (key gate at level 17) | knowledge gap | the lock seen on screen (feature --locked) |
| Study Pull Fest: leaderboard, league cups and their rewards, the period end; record what a tier-up gives (never compete or chat) | study | [Pull Fest Ranking (Bronze League)](features/pull-fest.md) | knowledge gap |  |
| Study puzzle pieces: the map puzzle nodes, the album in Collections, what completing a 3x3 picture gives | study | [Puzzle piece collection](features/puzzle-pieces.md) | knowledge gap |  |
| Study keys: collect the key nodes (L9 done, next ones), watch the 3 slots fill, record what 3 keys open | study | [Keys on the map (key nodes, 3-key gate at L11-12)](features/map-keys.md) | knowledge gap |  |
| Play a bonus level (character node) and record how it differs from a normal level | experiment | [Bonus levels (character node)](features/bonus-levels.md) | knowledge gap |  |
| Study Map tutorial tooltips: open it, walk its screens and tabs, verify its cases | study | [Map tutorial tooltips](features/map-tutorial.md) | external |  |
| Study Multi Stage Level: open it, walk its screens and tabs, verify its cases | study | [Multi Stage Level](features/multi-stage.md) | external |  |
| Unlock Sketchman IQ Test: level 16 | unlock | [Sketchman IQ Test](features/mode-iq-test.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Unlock Challenge: level 21 | unlock | [Challenge](features/mode-challenge.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Unlock Merge Balls: level 22 | unlock | [Merge Balls](features/mode-merge-balls.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Unlock Protect The Balloon: level 30 | unlock | [Protect The Balloon](features/mode-protect-balloon.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Unlock Dark Levels: level 50 | unlock | [Dark Levels](features/mode-dark-levels.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Unlock Bonus levels (character node): reach the node after level 16 | unlock | [Bonus levels (character node)](features/bonus-levels.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Check the multiplier reward is credited after the video and the plain Get N close path | experiment | [Win coin multiplier (video)](features/coin-multiplier.md) | knowledge gap |  |
| Find whether multi stage levels come every 5th level (L15, L20) | experiment | [Multi Stage Level](features/multi-stage.md) | knowledge gap |  |
| Find why Weekly trophy chest appeared: present on the Collections trophies tab from the first Collections visit (L3+); the first trophy tier was already reached at L10, likely by level wins | experiment | [Weekly trophy chest](features/trophies.md) | knowledge gap |  |
| Study the weekly trophy chest: find what earns a trophy tier (check the tab before and after a few level wins), tap the chest and 'Catch up on missed chests', record the reward | study | [Weekly trophy chest](features/trophies.md) | knowledge gap |  |
| Look for a win streak: Trails say 'Unlock by consecutive wins'; find the streak counter (win screen, map, level HUD) and what breaks it | experiment | [Collections](features/collections.md) | knowledge gap |  |
| Look for special events: every skin category has an 'Unlock in special events' section; find whether any event entry shows on the map | experiment | [Collections](features/collections.md) | knowledge gap |  |
| Interstitial skipped after a win shortly after a rewarded ad: is there a cooldown? | experiment | [Interstitial video ad after a win](features/interstitial.md) | knowledge gap |  |
| Run each outcome once under Level race: Win screen, Restart icon opens 'You can do better!' (Restart / Continue); Continue closes it; Restart plays an interstitial (skip control opened the Play Store, launch returned) then reloads only the current stage, earlier stages stay ticked; no coin cost, Back arrow returns to the map at once, no confirmation, no cost; reopening via Play keeps the multi-stage progress (stage 4 of 4), The previous session left L10 at stage 4; after the app was closed and relaunched this session, L10 opened at stage 4 with stages 1-3 ticked, Balls fell out | experiment | [Level race](features/race.md) | knowledge gap |  |
| Study Level race: open it, walk its screens and tabs, verify its cases | study | [Level race](features/race.md) | external |  |
| Lose a level by a grey ball and by a bomb in the cup; register each as a core-level outcome | experiment | [Pin-pull level](features/core-level.md) | knowledge gap |  |
| Find what Skip (video) on the 'Level failed' screen does: skips to the next level or not | experiment | [Pin-pull level](features/core-level.md) | knowledge gap |  |
| Unlock Color Bucket Level: reach the 'Color Bucket Level' node (level 19) | unlock | Color Bucket Level | knowledge gap | the lock seen on screen (feature --locked) |
| Find which levels carry a golden star-wand pin: only skull (hard) levels or others too | experiment | [Golden pins (league score)](features/golden-pins.md) | knowledge gap |  |
| Gumball: coin spin once the balance is 375 or more; does the price rise again? Is there a cap or cooldown on Spin with video? | experiment | [Gumball machine](features/gumball.md) | knowledge gap |  |
| Study Daily tasks: open it, walk its screens and tabs, verify its cases | study | Daily tasks | external |  |

## Waiting

| Task | Not before | Kind | Feature |
|---|---|---|---|
| Skip a day of Daily Rewards and check if the calendar resets | 2026-10-05 21:48:44 | check | [Daily Rewards](features/daily-rewards.md) |
| Pull Fest league: record the end-of-period rewards and reset when Time Left (6d 1h on 2026-10-04 01:00) runs out | 2026-10-10 02:00:00 | check | [Pull Fest Ranking (Bronze League)](features/pull-fest.md) |
| Check whether pins and golden pins reset when the league week ends (5d 1h left on 2026-10-05 01:50) | 2026-10-10 04:00:00 | check | [Golden pins (league score)](features/golden-pins.md) |

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

| Task | What to provide | Feature |
|---|---|---|
| Study the intro comic and tutorial: frame each panel and hand step, test skip and replay | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | Intro comic and tutorial hand |

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| After declining the race: does it come back, and is there a map entry for it? | 2026-10-05 01:53:12 | 20261005-014031-chrono-2FYKPJ#3 | After declining at L11, the 'New race started!' popup came back on leaving L13 (15 levels, 5h58m, +250, shot 7); declined again; no race button on the map |
| Golden pins: what they give in the league and the +5 golden pins video offer | 2026-10-05 01:53:11 | 20261005-014031-chrono-2FYKPJ#19 | After the L14 win: Pins 64, Golden 1, Total 69; the +5 video gave Golden 6, Total 94 (golden = 5 points), rank 458 -> 343; offered once per played win, not after a Jump to Level skip |
| Find how a flame-skull level (L14) differs from a plain skull level (L12) | 2026-10-05 01:53:10 | 20261005-014031-chrono-2FYKPJ#16 | L14 (flame skull) played like L12: a normal pin-pull board, same header with the red ring (flame badge), no popup, no golden pin (Golden stayed 1 until the +5 video), same loss and win flow, +25 coins. Only the board is harder (lost try 1). No difference beyond the badge |
| Walls say 'Unlock with daily tasks': find the daily tasks entry | 2026-10-05 01:52:58 | 20261005-014031-chrono-2FYKPJ#21 | The Daily tasks entry is a map button on the left (clipboard with a star) that appeared after the L14 win, tooltip 'Take a look on Daily tasks!' (shot 38); feature daily-tasks |
| update-241-5-2 | 2026-10-05 01:52:58 | 20261005-014031-chrono-2FYKPJ#0 | Phone on 241.5.2; map entry points as on 241.5.1 (shot 2); only new: Daily tasks button after L14 (feature daily-tasks) |
| First look at the new clipboard-with-star map button (appeared after L14) (cancelled) | 2026-10-05 01:52:57 | 20261005-014031-chrono-2FYKPJ#21 | duplicate: its feature map-quest-list was never created (the session's feature op failed); the button's tooltip reads 'Take a look on Daily tasks!', recorded as feature daily-tasks (type daily), whose study goal the planner makes |
| Study golden pins: record every source (golden pin in a level, the +5 video), any sink, and whether they reset with the league week | 2026-10-05 01:49:43 | 20261005-014031-chrono-2FYKPJ#19 | Sources: golden pin in a level (+1), post-win video (+5, watched after L14: 1->6, total 69->94). No sinks. Week reset not observable now (5d 1h left): followup golden-pins-week-reset |
| Study Jump to Level: tap it once, record the offer screen (video) and where it sends; decline without watching | 2026-10-05 01:43:30 | 20261005-014031-chrono-2FYKPJ#6 | One tap starts a rewarded video directly (no offer screen, so declining was impossible); video counted as an L13 win (+25 coins, league board, map to L14), button moved to L15. Shots 2-11 |
| Find when a win is saved: exit the app on the post-win screens on purpose | 2026-10-05 01:40:54 | 20261005-013818-chrono-2FYKPJ#1 | Two wins cut before the post-win flow ended were not saved: L10 (force-stop on the multiplier ad end card, 20261003-211035-chrono-2FYKPJ#23) and L13 (app left on the league board, map back at 13 next day); league pins kept in both. Not a deliberate force-stop, but both cuts land on the plan's screens |
| Check at session start whether the L13 win was kept: the owner took the phone on the post-win league board | 2026-10-05 01:39:08 | 20261005-013818-chrono-2FYKPJ#1 | Map at 13 = reverted. Win flow cut at league board -> level not saved, but league pins (49) were kept. Case for exp-win-saved-when |
| Claim Daily Rewards day 2 (+50) — day 1 of 1 | 2026-10-05 01:39:07 | 20261005-013818-chrono-2FYKPJ#1 | Day 2 +50 claimed from launch popup, coins 344 |
| Study Hard levels (skull node): open it, walk its screens and tabs, verify its cases | 2026-10-04 01:11:23 | 20261004-005453-chrono-2FYKPJ#9 | Entry, screen, announce, win, differs and frequency closed from L12 (shots 17, 23, 25). The only open items, chk-loss and chk-retry, need a deliberate loss on a skull level; that run is the balls-out cell of outcomes-hard-levels, which stays open |
| Study Interstitial video ad after a win: open it, walk its screens and tabs, verify its cases | 2026-10-04 01:06:59 | 20261004-005453-chrono-2FYKPJ#12 | Marked entry (Tap to continue -> ad-loading logo), screen (video), end card with only the skip icon (opened the Play Store, launch returned to the map with the win kept), a second network's variant with 'Google Play >>' and a playable end card closed by the faint X (683,70). Interstitials after both L11 and L12 wins ~3 min apart (no cooldown between wins) |
| Lose a pin-pull level on purpose and record each loss kind as an outcome of core-level | 2026-10-04 00:55:31 | 20261004-004411-chrono-2FYKPJ#23 | L11 lost twice (not on purpose): fail screen 'Pretty Close! Level failed!', tip 'Balls fell out of the level'; outcome balls-out registered; retry offers Skip (video) / Retry. Other loss kinds (grey or bomb in the cup) left to exp-loss-other-kinds |
| Win L10 stage 4 and reach L12: if the pin-pull solver sees no rings on the Space theme, equip the default theme in Collections > Skins > Themes and retry | 2026-10-04 00:55:30 | 20261004-004411-chrono-2FYKPJ#16 | L10 stage 4 won by the solver on the default theme (25 s); map shows L11. Reaching L12 is left to the pin-pull handoff (L11 lost twice) |
| Study Gumball machine: open it, walk its screens and tabs, verify its cases | 2026-10-04 00:46:50 | 20261004-004411-chrono-2FYKPJ#6 | entry (Collections box on map), screen, video spin result marked; video spin reward confirmed: skin Line; coin price 350->375 |
| Gumball Spin with video: what the reward is after the rewarded ad | 2026-10-04 00:46:49 | 20261004-004411-chrono-2FYKPJ#6 | video spin gives one ball skin (Line), coin price then 375 |
| See what a gumball video spin gives | 2026-10-04 00:46:49 | 20261004-004411-chrono-2FYKPJ#6 | 3rd try: ad ~30 s, Google 'Reward granted' sheet with X; X -> spin -> skin Line (NEW). Earlier failures were the ad end cards, not the feature |
| Find why Gumball machine appeared: present on the Collections gumball tab from the first Collections visit (L3+) | 2026-10-04 00:44:30 | planner | the trigger is recorded as a fact: with Collections on the first visit after L3: the gumball tab opens first with a free Spin! badge [20261003-203702-chrono-2FYKPJ#53] |
| Spin the gumball machine once (video spin) and record the reward (cancelled) | 2026-10-04 00:16:19 | 20261004-001002-chrono-2FYKPJ#2 | duplicate of exp-gumball-video-spin (same video spin, reward still unseen; that goal sits on the gumball feature with the ad timing in its plan) |
| Run restart, quit and exit-app once on a level | 2026-10-03 22:24:05 | 20261003-214021-chrono-2FYKPJ#29 | restart (cancel and confirm), quit and exit-app all run on L10 stage 4 |
| Study Daily Rewards: open it, walk its screens and tabs, verify its cases | 2026-10-03 21:48:45 | 20261003-214021-chrono-2FYKPJ#30 | entry checked: popup-only, no map button; same-day relaunch shows nothing; next day in daily-rewards-d2-d1, missed day in daily-rewards-missed |
| Study Pin-pull level: open it, walk its screens and tabs, verify its cases | 2026-10-03 21:48:07 | 20261003-214021-chrono-2FYKPJ#29 | HUD, restart (cancel and confirm, interstitial), quit, exit-app verified; loss and retry left to exp-loss |
| Study Collections: trophies chest, puzzle albums, every skin category (Themes, Trails, Walls, Pins) | 2026-10-03 21:45:19 | 20261003-214021-chrono-2FYKPJ#20 | 4 tabs and all 5 skin categories marked; space theme equipped |
| Study Bronze League leaderboard: open it, walk its screens and tabs, verify its cases (cancelled) | 2026-10-03 21:26:40 | review-20261003 | Duplicate: Bronze League is the pull-fest league (pull-fest is named 'Pull Fest Ranking (Bronze League)'; same timer and pins score) [20261003-211035-chrono-2FYKPJ#15]; study it under study-pull-fest |
| Study the win coin multiplier: on which win screens it appears, how the moving x2-x5 bar picks the factor, and the close path | 2026-10-03 21:23:50 | 20261003-211035-chrono-2FYKPJ#23 | Seen on the L10 multi stage win after puzzle piece and league screens: base +19, bar x2-x5 sweeps, factor locks on tap (x5=95). Credit after the video not verified: the ad end card hung and the restart reverted the win; exp-multiplier-credit added |
| Study Bonus levels (character node): open it, walk its screens and tabs, verify its cases | 2026-10-03 21:12:23 | 20261003-211035-chrono-2FYKPJ#4 | Not studiable at L10: node after L16 is inert when tapped; lock recorded at 16 so the planner sets the unlock goal; study it after L16 is won |
| Study the jar icon on the map: open it, record what it holds, how it fills and what it gives | 2026-10-03 21:12:08 | 20261003-211035-chrono-2FYKPJ#3 | Jar icon = 'All You Can Play!' modes menu; 5 locked modes registered (L16,21,22,30,50); no filling or reward; tap on locked card does nothing; badge clears on first open |
| Find whether interstitial or rewarded ads come after level wins | 2026-10-03 21:07:51 | 20261003-203702-chrono-2FYKPJ#42 | Interstitial video after every win from L6 on (L6, L7, L8, L9), on Tap to continue; feature interstitial |
| First look at Gift unlock progress bar: open it once, record what it is and decide whether it needs a full study | 2026-10-03 21:07:51 | 20261003-203702-chrono-2FYKPJ#46 | Gift bar filled at L9: gift box opened = cup skin Space, Get Another One (video); a skin-reward bar, study via study-collections |
| Look for a shop, skins or daily rewards (genre checklist) while playing to level 10 | 2026-10-03 21:07:50 | 20261003-203702-chrono-2FYKPJ#60 | By level 10: Daily Rewards (map, 2nd Play after L3), Collections with skins (Themes, Trails, Walls, Pins, Balls) and gumball machine from the map box button; no IAP shop besides No Ads |
| What coins are spent on (no shop seen at level 3) | 2026-10-03 21:03:29 | 20261003-203702-chrono-2FYKPJ#62 | Coins are spent in Collections (map box button): gumball spin 350, ball skins 1000/3000/10000 |
| Study Coins: open it, walk its screens and tabs, verify its cases | 2026-10-03 21:03:05 | 20261003-203702-chrono-2FYKPJ#61 | Coins: sources win 17-24/level, video x2-x5 multiplier, daily rewards 25..500; entry map box button -> Collections (balance header); sinks gumball 350 (first spin free), ball skins 1000/3000/10000; not enough = greyed/no reaction; no coin shop/IAP packs seen |
| Find why Keys on the map (key nodes, 3-key gate at L11-12) appeared: key node on L9 (earlier L6); 3 key slots above L11/L12 | 2026-10-03 20:59:30 | planner | the trigger is recorded as a fact: key node on level 9: winning L9 filled 1 of the 3 key slots above L17 ('Unlock New Mode') [20261003-203702-chrono-2FYKPJ#52] |
| Study the banner ad: where it shows, whether it closes, what a tap opens | 2026-10-03 20:57:33 | 20261003-203702-chrono-2FYKPJ#49 | where: bottom strip on levels, win, league, map, daily rewards; no close (only AdChoices i); tap -> Play Store overlay sheet, launch returns intact |
| Continue FTUE from level 3: record when each feature unlocks (gift at ~L9) | 2026-10-03 20:56:18 | 20261003-203702-chrono-2FYKPJ#46 | Fresh install L3-L9: map first shown after the L3 win (map tutorial tooltips, Daily Rewards on the 2nd Play), Multi Stage L5, coin multiplier on the L5 win screen, Pull Fest (Bronze League) after L5, puzzle piece after L6, interstitials after every win from L6, gift bar full at L9 = cup skin Space. Chest timer and Jump to Level on the map from L3. |
| Unlock Gift unlock progress bar: about level 9, not shown: +11-12% per win | 2026-10-03 20:56:17 | planner | seen open at level 9 |
| Map the game: play until the main menu and every entry point is visible; list each entry point as open (a study goal), locked with its unlock condition (an unlock goal) or unclear (an experiment) | 2026-10-03 19:33:11 | 20261003-193015-chrono-2FYKPJ#7 | Fresh install: intro comic, no main menu, the level screen is the hub (gear, restart, ADS, level path). Win screen: coins + gift bar ~11%/win, gift locked ~L9. Banner ads from L1. |
