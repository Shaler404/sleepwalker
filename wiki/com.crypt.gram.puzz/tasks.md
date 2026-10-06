# Tasks: Cryptogram: Word Logic Puzzles

Status: **▶️ active** — ready now: 24

Mode: **goals** — work through the session goals in order; play levels only as far as an unlock or experiment goal needs; register anything new you notice as a feature or a goal, do not pursue it now

Progress reached: **level 10** · last new feature found at: **level 8**

Goals: study 7, unlock 4, experiment 13 · maps: level 1 (fresh install, no level played) — 9 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **Number-coded quote** — mastered, solver, levels won 10, typical 2.0 min; **card-cryptogram** — studying, manual, levels won 0

Google Play version: **3.6.1** (checked 2026-10-05 22:05:43) · analyzed version: **3.6.1** · FTUE from a fresh install: **never**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Unlock Daily Challenge: complete 15 levels (shown at level 1: 'Complete 15 more levels to unlock') | unlock | [Daily Challenge](features/daily-challenge.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Run the cryptogram solver on the recorded level-1 board after the word-list fix: does the stall at one ambiguous number go away? | experiment |  | knowledge gap | stall at 20261003-234451-chrono-2FYKPJ#13 |
| Loss popup REVIVE: what it costs and gives (a video for undoing the 3rd mistake, a heart kept?) | experiment | [Cryptogram level](features/cryptogram-level.md) | knowledge gap |  |
| Lives at 0: empty-state offers and any ways to get hearts (ad, daily reward) | experiment | [Lives (hearts)](features/lives.md) | knowledge gap |  |
| Mistakes counter and hints: does a hint after a wrong letter change the X count, and does a hint ever count as a mistake | experiment | Mistakes counter | knowledge gap |  |
| Hint video retry: another ad creative, wait up to 3 min for a close X, then read the bulb count | experiment | Hints (bulb) | knowledge gap |  |
| Unlock Leagues: complete 50 levels (47 more after level 3) | unlock | Leagues | knowledge gap | the lock seen on screen (feature --locked) |
| Unlock Collection: complete 15 levels (12 more after level 3) | unlock | Collection | knowledge gap | the lock seen on screen (feature --locked) |
| Unlock Album: complete 99 levels (96 more after level 3) | unlock | Album | knowledge gap | the lock seen on screen (feature --locked) |
| Study Shop: open it, walk its screens and tabs, verify its cases | study | Shop | external |  |
| Study Statistics: open it, walk its screens and tabs, verify its cases | study | Statistics | external |  |
| Run each outcome once under Win streak banner: Home icon in level, Restart only from the loss popup (no restart button on the HUD seen); no confirmation, no ad, same board and cells, mistakes reset, Force-stop (restart) mid-level with a hint used, Lose by 3 mistakes | experiment | Win streak banner | knowledge gap |  |
| Run each outcome once under Chest Hunt event: Home icon in level, Force-stop (restart) mid-level with a hint used | experiment | Chest Hunt event | knowledge gap |  |
| Run each outcome once under Secret Level: Win card, Home icon in level, Restart only from the loss popup (no restart button on the HUD seen); no confirmation, no ad, same board and cells, mistakes reset, Force-stop (restart) mid-level with a hint used, Lose by 3 mistakes | experiment | Secret Level | knowledge gap |  |
| Study Secret Level (Daily Tasks bar reward): play it, note reward | study | Secret Level | knowledge gap |  |
| Playable interstitial (no close) after win/NEXT and on START needs restart; log frequency | experiment | Banner ad | knowledge gap |  |
| Study Rate us popup: open it, walk its screens and tabs, verify its cases | study | Rate us popup | external |  |
| Study Win streak banner: open it, walk its screens and tabs, verify its cases | study | Win streak banner | external |  |
| Study No ADS offer: open it, walk its screens and tabs, verify its cases | study | No ADS offer | external |  |
| Chest Hunt keys per level: free claim against key slots, and keys after a loss | experiment | Chest Hunt event | knowledge gap |  |
| Run each outcome once under Quote Race event: Home icon in level, Force-stop (restart) mid-level with a hint used | experiment | Quote Race event | knowledge gap |  |
| Does the hint pack price discount (RSD 249) follow a timer or level time? note tag price at level start and after 3 min on several boards | experiment | Hint pack offer (+20 hints) | knowledge gap |  |
| Study Quote Race: rewards chest, end results at timer end, quit case | study | Quote Race event | knowledge gap |  |
| Find why a tutorial hand points at the hint bulb after a Restart, and whether it blocks the HUD every time | experiment | Hints (bulb) | knowledge gap |  |

## Waiting

| Task | Not before | Kind | Feature |
|---|---|---|---|
| Quote Race at its 12h end: mark the results screen, the final rank and the reward chest paid, and whether a new race starts | 2026-10-06 14:50:00 | check | Quote Race event |
| Daily Tasks after the day reset: mark the new batch, the bar (reset to 0/9 or kept) and whether an unplayed Secret Level survives | 2026-10-07 00:30:00 | check | [Daily Tasks](features/daily-tasks.md) |
| Chest Hunt at its end: the results screen, the reward for the keys collected, and whether a new event starts | 2026-10-09 00:30:00 | check | Chest Hunt event |

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

None.

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Run Home-icon quit under Quote Race and Chest Hunt (home icon was blocked by a hint tutorial hand on level 11 restart) (cancelled) | 2026-10-06 03:07:17 | 20261006-024420-chrono-2FYKPJ#39 | duplicate: the Home-icon quit cells are already owed by outcomes-quote-race and outcomes-chest-hunt (under-quit); the blocker (hint tutorial hand over Home after a restart) is recorded in the review |
| Study Chest Hunt event | 2026-10-06 03:04:37 | 20261006-024420-chrono-2FYKPJ#39 | Keys on cells, claim 3 or x3 with video, 9->12->17/120, loss and restart done; quit and end remain as tasks |
| Study Hint pack offer (+20 hints): open it, walk its screens and tabs, verify its cases | 2026-10-06 03:04:36 | 20261006-024420-chrono-2FYKPJ#39 | Button on board, tap opens Play payment sheet directly; price 399 vs 249 tag; timer open as task hint-pack-timer |
| Study Lockers (padlocked cells): open it, walk its screens and tabs, verify its cases | 2026-10-06 03:04:36 | 20261006-024420-chrono-2FYKPJ#39 | Lockers documented: single lock (L9), double locker tooltip tutorial (L10), no extra loss, coexist with keys |
| Which home entry points appear after the first levels (earlier installs showed Chest Hunt keys, a secret level, a card event, hints) | 2026-10-06 01:02:43 | 20261006-003220-chrono-2FYKPJ#72 | Levels 4-8 added: No ADS button on home after level 4/5 (#22), Chest Hunt event card after level 6 and relaunch (#33/#36), Daily Tasks card turning into Secret Level PLAY after the 9th task (#72); Daily Challenge counter 12 -> 7 more. Card-cryptogram event still unseen |
| Look for interstitial and rewarded-video ads: after which level wins and after a loss | 2026-10-06 01:02:42 | 20261006-003220-chrono-2FYKPJ#9 | Full-screen ads after NEXT on the level 4, 5, 6, 7 and 8 win cards and once on START (level 7): store pages (Back), a skippable video with a Next skip and 'Not interested', and playable ads with no close that needed a force-stop (#22, #33, #43, #60, #72). Rewarded videos: hint at 0 bulb, REVIVE, Chest Hunt CLAIM x3 |
| Find why Hint pack offer (+20 hints) appeared: in-level button with a price tag 'RSD 399' and '+20' bulb at the bottom left of the board, seen from level 4 (first board this session); probably since the level-3 win that opened the Shop | 2026-10-06 01:02:42 | planner | the trigger is recorded as a fact: from level 4, after the 3rd win (absent on the level-3 board [20261005-221933-chrono-2FYKPJ#23]): bottom-left bulb button '+20' with a green 'RSD 399' price tag [20261006-003220-chrono-2FYKPJ#1] |
| Study IQ score: open it, walk its screens and tabs, verify its cases | 2026-10-06 00:57:47 | 20261006-003220-chrono-2FYKPJ#73 | IQ pill and Daily Tasks info i open one popup: N IQ, smarter than X% players, Complete Daily Tasks to increase IQ, NICE!. 100 -> 118 IQ, 25.33% at 109. |
| Study Daily Tasks: complete its 3 tasks on level 4+ (any level, a 4+ letter word, 20 correct letters), mark each claim and the IQ gain, and what the 9-segment bar's star-wand reward gives | 2026-10-06 00:57:46 | 20261006-003220-chrono-2FYKPJ#73 | Tasks rotate in batches of 3 (any level, words, letters, lockers, letter E counts); each finished task fills one of 9 bar segments and adds IQ (100->118 over levels 4-8); bar full turns card into Secret Level PLAY. Claim is automatic, no button seen; info i opens IQ popup. |
| Look for a shop, a no-ads purchase or a hint pack (genre checklist: monetization) | 2026-10-05 22:33:20 | 20261005-221933-chrono-2FYKPJ#38 | Shop button appears in the home bottom bar after the 3rd level win (red badge 1); registered as feature shop, not opened this session |
| First look at Daily Tasks: open it once, record what it is and decide whether it needs a full study | 2026-10-05 22:32:02 | 20261005-221933-chrono-2FYKPJ#35 | Unlocked after the 3rd level win: home card with day timer, info popup about IQ (100 IQ, smarter than 20%), 2 tasks with IQ rewards. Needs a full study: complete both tasks, see the claim and the IQ gain, check the reset |
| Unlock Daily Tasks: complete 3 levels (shown: 'Complete 3 levels to unlock') | 2026-10-05 22:31:09 | planner | seen open at level 3 |
| Hint video: does the hint reward arrive after watching a rewarded ad to its end | 2026-10-05 22:28:51 | 20261005-221933-chrono-2FYKPJ#28 | Bulb at zero -> rewarded video, then a playable end card with no close X after ~100 s (Back and launch ignored); force restart was the only exit, and after it the bulb still showed the play badge: no hint credited. The ad never finished on its own, so whether a completed ad pays is still unknown; a second ad creative might have a close X |
| Study Support: open it, walk its screens and tabs, verify its cases | 2026-10-05 22:23:35 | 20261005-221933-chrono-2FYKPJ#17 | Need Help? popup: FAQ (Zendesk Help Center, 7 sections, articles, Get in touch chat) and Support (Conversations inbox, Get in touch); all in-app, X back to popup; nothing sent |
| Settings: tap Support, Privacy Policy, Terms of Use and Restore Purchases once each, return at once, record where each leads | 2026-10-05 22:23:35 | 20261005-221933-chrono-2FYKPJ#17 | Support -> in-app Need Help? popup (Zendesk); Privacy Policy and Terms of Use -> Chrome joyteractive.com; Restore Purchases -> in-game success banner; launch returned to Settings each time |
| Study Settings: open it, walk its screens and tabs, verify its cases | 2026-10-05 22:22:02 | 20261005-221933-chrono-2FYKPJ#9 | All rows verified: both toggles in place, Restore Purchases success banner, Support -> Need Help popup, Privacy/Terms -> Chrome joyteractive.com; Promo Code and How to play from earlier sessions |
| Promo Code: APPLY with an empty and an invalid code; record the message | 2026-10-05 14:37:56 | 20261005-143208-chrono-2FYKPJ#8 | Empty APPLY: nothing visible; invalid code TEST123: Oops panel 'You have entered an incorrect code or your promo code has expired' (shot 10) |
| Find whether the notification prompt returns after 'Don't allow' (and what the Settings Notifications toggle does then) | 2026-10-05 14:37:55 | 20261005-143208-chrono-2FYKPJ#11 | No re-prompt on any relaunch after Don't allow (sessions through this one); Settings Notifications toggle OFF then ON raised no system dialog (shots 13-14) |
| Study Quote share (win card): open it, walk its screens and tabs, verify its cases | 2026-10-05 14:36:53 | 20261005-143208-chrono-2FYKPJ#18 | Share arrow on win card opens Android share sheet; Back returns |
| Study Notification permission prompt: open it, walk its screens and tabs, verify its cases | 2026-10-05 14:34:41 | 20261005-143208-chrono-2FYKPJ#11 | answers: Don't allow tapped on first launch; no re-prompt since; Settings toggle ON/OFF shows no system dialog |
| Study Promo Code: open it, walk its screens and tabs, verify its cases | 2026-10-05 14:34:12 | 20261005-143208-chrono-2FYKPJ#8 | Dialog options verified: PASTE clears field with empty clipboard, empty APPLY nothing, invalid code -> Oops panel |
| Mistakes counter with hints and revive (cancelled) | 2026-10-05 12:35:15 | 20261005-123057-chrono-2FYKPJ#11 | plan too vague and its REVIVE half duplicates revive-offer; replaced by hint-vs-mistakes |
| Lives below full: tap the heart's green plus and record the refill offer; record how long one heart takes to regenerate | 2026-10-05 12:35:14 | 20261005-123057-chrono-2FYKPJ#11 | At 4/5 the heart widget and its green plus open nothing (no refill offer below full); timer 29m58s right after the loss, so 30 min per heart (#9-#11) |
| Study Lives (hearts): open it, walk its screens and tabs, verify its cases | 2026-10-05 12:33:58 | 20261005-123057-chrono-2FYKPJ#11 | lives widget, regen timer 30 min, loss cost verified; zero state and sources left as task lives-zero-and-sources |
| Study Mistakes counter: open it, walk its screens and tabs, verify its cases | 2026-10-05 12:33:58 | 20261005-123057-chrono-2FYKPJ#11 | 3 wrong letters to loss popup verified; hint interaction left as task |
| Study Level info button (i): open it, walk its screens and tabs, verify its cases | 2026-10-05 12:32:44 | 20261005-123057-chrono-2FYKPJ#5 | info opens 3-page How to play |
| Use the hint bulb once and find how hints are refilled (what the bulb offers at 0) | 2026-10-05 00:39:44 | 20261005-003245-chrono-2FYKPJ#8 | Bulb (count 1) reveals only the tapped cell (#7); at 0 the badge is an orange play icon and the bulb starts a rewarded playable ad (#8); whether the hint is granted is left to hint-reward-check |
| Study Hints (bulb): open it, walk its screens and tabs, verify its cases | 2026-10-05 00:38:22 | 20261005-003245-chrono-2FYKPJ#13 | Studied: loss popup, restart, force-stop, hint bulb, banner rotation; REVIVE and hint reward not tested (ad never closed); see cases |
| Study Banner ad: open it, walk its screens and tabs, verify its cases | 2026-10-05 00:38:22 | 20261005-003245-chrono-2FYKPJ#13 | Studied: loss popup, restart, force-stop, hint bulb, banner rotation; REVIVE and hint reward not tested (ad never closed); see cases |
| Cryptogram level: lose via 3 mistakes, restart, exit app mid-level, hint bulb | 2026-10-05 00:38:21 | 20261005-003245-chrono-2FYKPJ#13 | Studied: loss popup, restart, force-stop, hint bulb, banner rotation; REVIVE and hint reward not tested (ad never closed); see cases |
| Study Home screen: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:50:09 | 20261003-234451-chrono-2FYKPJ#19 | home on fresh, after level 1 (counters, banner ad), settings entry; lives popup not reachable, locked cards inert |
| Study Cryptogram level: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:50:09 | 20261003-234451-chrono-2FYKPJ#19 | walked L1 tutorial, win card, L2 HUD, quit via home; loss, restart, exit-app, elements left open (lives/mistakes cost needs deliberate loss) |
| Study How to play: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:47:06 | 20261003-234451-chrono-2FYKPJ#7 | 3 pages walked and marked, X closes all |
| Map the game: play until the main menu and every entry point is visible; list each entry point as open (a study goal), locked with its unlock condition (an unlock goal) or unclear (an experiment) | 2026-10-03 20:18:35 | 20261003-201504-chrono-2FYKPJ#13 | Fresh install (level 1). Home: lives 5 FULL (tap does nothing), gear > Settings (Notifications, Vibration, Restore Purchases, Support, Promo Code, How to play 3 pages, Privacy Policy, Terms of Use), Daily Challenge locked 'complete 15 more levels', Daily Tasks locked 'complete 3 levels', START LEVEL 1 with tutorial hand. No shop/currency/event entry on a fresh install; experiment home-after-levels set for entries that appear with progress. |
