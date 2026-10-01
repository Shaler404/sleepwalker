# Tasks: Meowdoku: Brain Puzzle Games

Status: **▶️ active** — ready now: 8

Mode: **advance** — move through the content as fast as possible; register every new feature and write down every branch as a case or task for later, do not test them now

Progress reached: **level 43** · last new feature found at: **level 1**

Screen surveys: level 40 — 6 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **Cat placement on color regions (Queens-like)** — mastered, solver, levels won 47, typical 0.7 min

Google Play version: **1.18.0** (checked 2026-10-01 02:46:28) · analyzed version: **1.18.0** · FTUE from a fresh install: **2026-10-01**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Analyze the game, version 1.18.0 | analysis |  | external | find all features and work through all user cases |
| Trigger Rate Us popup again and test low-star rating path (did not appear in levels 22-35) | check | [Rate Us popup](features/rate-us.md) | from the game |  |
| Scroll language list, document all languages | check | Language selection | from the game |  |
| Determine what decides Exact/Stellar/Unreal win titles | check | [Win screen titles (Exact, Untouchable, Stellar, Masterclass, Crystal Clear, Unreal)](features/win-rank.md) | from the game |  |
| Turn Pattern Mode back OFF (left ON by session 20261001-022624) | check | [Settings](features/settings.md) | knowledge gap |  |
| Lose all fish and tap Restart on the Out of Fishes popup | check | [Fish (3 mistake lives per level)](features/lives-fish.md) | knowledge gap |  |
| Use a booster down to 0 and record the refill offer (rewarded ad?) | check | [Hint (lightbulb)](features/hint.md) | knowledge gap |  |
| Open Terms of Service and Privacy Policy from Home settings | check | [Settings](features/settings.md) | knowledge gap |  |

## Waiting

| Task | Not before | Kind | Feature |
|---|---|---|---|
| Win a level to extend the daily streak; record the day's reward — day 1 of 7 | 2026-10-01 23:34:51 | daily | [Daily streak (yarn ball)](features/streak.md) |
| Check the fish leaderboard result and rank rewards after the event ends | 2026-10-01 23:43:31 | check | [Fish leaderboard event (podium on home)](features/fish-event.md) |
| Next day: play the new Daily Challenge and look for a reward or calendar | 2026-10-02 00:30:00 | daily | [Daily Challenge](features/daily-challenge.md) |
| Win a level to extend the daily streak; record the day's reward — day 2 of 7 | 2026-10-02 23:34:51 | daily | [Daily streak (yarn ball)](features/streak.md) |
| Win a level to extend the daily streak; record the day's reward — day 3 of 7 | 2026-10-03 23:34:51 | daily | [Daily streak (yarn ball)](features/streak.md) |
| Win a level to extend the daily streak; record the day's reward — day 4 of 7 | 2026-10-04 23:34:51 | daily | [Daily streak (yarn ball)](features/streak.md) |
| Win a level to extend the daily streak; record the day's reward — day 5 of 7 | 2026-10-05 23:34:51 | daily | [Daily streak (yarn ball)](features/streak.md) |
| Win a level to extend the daily streak; record the day's reward — day 6 of 7 | 2026-10-06 23:34:51 | daily | [Daily streak (yarn ball)](features/streak.md) |
| Win a level to extend the daily streak; record the day's reward — day 7 of 7 | 2026-10-07 23:34:51 | daily | [Daily streak (yarn ball)](features/streak.md) |

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

| Task | What to provide | Feature |
|---|---|---|
| How the fish ranking event unlocks (seen after level 10) | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | [Fish leaderboard event (podium on home)](features/fish-event.md) |

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Leaderboard event end: collect rank rewards and see next event (cancelled) | 2026-10-01 05:00:00 | dream | duplicate of fish-event-end (leaderboard-event merged into fish-event) |
| Survey every screen: capture all entry points and map them to features | 2026-10-01 02:42:41 | 20261001-022624-chrono-2FYKPJ#74 | Walked home, profile (avatar/frame), streak page, leaderboard + info, level settings, home settings, language, save progress, support center articles, out-of-fishes, ads. New: save-progress, language, support-center, leaderboard-event, ads, pattern-mode, win-rank. |
| Streak day-7 gift contents; streak reset when a day is missed | 2026-10-01 02:42:40 | 20261001-022624-chrono-2FYKPJ#74 | Day-7 gift box on Daily Streak page is not tappable early; support article says 7 days in a row unlocks a mysterious reward; missing a day breaks the streak. Contents verified by streak-day-d7 task. |
| Daily Challenge: check calendar/rewards after repeated days and what Continue gives | 2026-10-01 02:42:40 | 20261001-022624-chrono-2FYKPJ#74 | Daily already done today: button inert after completion, no calendar/reward popup. Next-day check requires new day (case daily-challenge/next-day). |
| Document ad flow: banner from level 23, interstitial on level start/Restart/Daily; check remove-ads or rewarded options | 2026-10-01 02:42:39 | 20261001-022624-chrono-2FYKPJ#74 | Banner at the bottom of levels; interstitials on level start (video with skip icon, or playable without close; 'sw.py launch' dismisses); rewarded 'Get 3 Fishes' on Out of Fishes = ~30s playable, launch returns with reward granted. No remove-ads found in home/level settings. |
| Lose all 3 fish: fail screen and revive options | 2026-10-01 02:36:36 | 20261001-022624-chrono-2FYKPJ#42 | 3 wrong placements -> 'Out of Fishes' popup (Remaining: N cats, Get 3 Fishes [rewarded ad], Restart). Revive via ad restores 3 fish and keeps the board. Restart not tested. |
| Check solver reading with Pattern Mode on (icons on regions) | 2026-10-01 02:33:37 | 20261001-022624-chrono-2FYKPJ#35 | Pattern Mode ON draws distinct icons on each region (stars, leaves, bells, paws, fish, ...) keeping colours; queens solver reads the board correctly and solved 9x9 level 37. First --run right after closing settings misread (animation), re-run OK. |
| Toggle music/sound/voice/vibration in settings and note effects | 2026-10-01 02:32:40 | 20261001-022624-chrono-2FYKPJ#30 | 4 toggles (music/sound/voice/vibration) flip ON/OFF instantly in Settings; music default OFF with red dot (dot disappears after first toggle); audio/vibration effects not observable via screenshots. Restored defaults. |
| Open Settings > Feedback and document the form (do not send) | 2026-10-01 02:32:05 | 20261001-022624-chrono-2FYKPJ#27 | Settings > Feedback opens in-app Helpshift web page 'Meowdoku Support': search, tabs Popular/Get Started/General/Account/Settings, articles (How to play, close an ad, Streak, place cat vs X, Daily Challenge, delete account data), Chat with us button. Not sent. |
| Cases pass from level 22: settings screen, hint/cat/mouse boosters first use, Daily Challenge (now unlocked), profile Frame tab, streak counter tap, Rate Us low stars, wrong placement losing a fish | 2026-10-01 02:04:17 | 20261001-013526-chrono-2FYKPJ#145 | Done: settings, hint/cat/mouse boosters, profile frames, streak tap, wrong placement (fish 3->2), Daily Challenge cleared. Rate Us low stars not reachable: new task. |
| Advance from level 22 with the queens solver; watch for new unlocks/events after level 21 | 2026-10-01 02:04:17 | 20261001-013526-chrono-2FYKPJ#145 | Advanced levels 22-35 with solver, new: banner+interstitial ads from L23, Hard tag at L30; no new unlock seen |
