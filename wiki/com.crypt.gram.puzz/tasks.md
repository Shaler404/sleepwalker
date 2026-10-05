# Tasks: Cryptogram: Word Logic Puzzles

Status: **▶️ active** — ready now: 20

Mode: **goals** — work through the session goals in order; play levels only as far as an unlock or experiment goal needs; register anything new you notice as a feature or a goal, do not pursue it now

Progress reached: **level 2 reached, 1 won** · last new feature found at: **level 2 reached, 1 won**

Goals: study 8, unlock 2, experiment 10 · maps: level 1 (fresh install, no level played) — 9 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **Number-coded quote** — studying, solver, levels won 1, typical 1.9 min; **card-cryptogram** — studying, manual, levels won 0

Google Play version: **3.6.1** (checked 2026-10-05 00:13:01) · analyzed version: **3.6.1** · FTUE from a fresh install: **never**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Unlock Daily Challenge: complete 15 levels (shown at level 1: 'Complete 15 more levels to unlock') | unlock | [Daily Challenge](features/daily-challenge.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Unlock Daily Tasks: complete 3 levels (shown: 'Complete 3 levels to unlock') | unlock | [Daily Tasks](features/daily-tasks.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Which home entry points appear after the first levels (earlier installs showed Chest Hunt keys, a secret level, a card event, hints) | experiment | [Home screen](features/home.md) | knowledge gap |  |
| Study Lives (hearts): open it, walk its screens and tabs, verify its cases | study | [Lives (hearts)](features/lives.md) | external |  |
| Study Settings: open it, walk its screens and tabs, verify its cases | study | [Settings](features/settings.md) | external |  |
| Study Promo Code: open it, walk its screens and tabs, verify its cases | study | [Promo Code](features/promo-code.md) | external |  |
| Study Support: open it, walk its screens and tabs, verify its cases | study | [Support](features/support.md) | external |  |
| Find whether the notification prompt returns after 'Don't allow' (and what the Settings Notifications toggle does then) | experiment | Notification permission prompt | knowledge gap |  |
| Study Notification permission prompt: open it, walk its screens and tabs, verify its cases | study | Notification permission prompt | external |  |
| Study Mistakes counter: open it, walk its screens and tabs, verify its cases | study | Mistakes counter | external |  |
| Study Level info button (i): open it, walk its screens and tabs, verify its cases | study | Level info button (i) | external |  |
| Study Quote share (win card): open it, walk its screens and tabs, verify its cases | study | Quote share (win card) | external |  |
| Look for interstitial and rewarded-video ads: after which level wins and after a loss | experiment | Banner ad | knowledge gap |  |
| Look for a shop, a no-ads purchase or a hint pack (genre checklist: monetization) | experiment | [Home screen](features/home.md) | knowledge gap |  |
| Settings: tap Support, Privacy Policy, Terms of Use and Restore Purchases once each, return at once, record where each leads | experiment | [Settings](features/settings.md) | knowledge gap |  |
| Promo Code: APPLY with an empty and an invalid code; record the message | experiment | [Promo Code](features/promo-code.md) | knowledge gap |  |
| Run the cryptogram solver on the recorded level-1 board after the word-list fix: does the stall at one ambiguous number go away? | experiment |  | knowledge gap | stall at 20261003-234451-chrono-2FYKPJ#13 |
| Hint video: does the hint reward arrive after watching a rewarded ad to its end | experiment | Hints (bulb) | knowledge gap |  |
| Lives below full: tap the heart's green plus and record the refill offer; record how long one heart takes to regenerate | experiment | [Lives (hearts)](features/lives.md) | knowledge gap |  |
| Loss popup REVIVE: what it costs and gives (a video for undoing the 3rd mistake, a heart kept?) | experiment | [Cryptogram level](features/cryptogram-level.md) | knowledge gap |  |

## Waiting

None.

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

None.

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Use the hint bulb once and find how hints are refilled (what the bulb offers at 0) | 2026-10-05 00:39:44 | 20261005-003245-chrono-2FYKPJ#8 | Bulb (count 1) reveals only the tapped cell (#7); at 0 the badge is an orange play icon and the bulb starts a rewarded playable ad (#8); whether the hint is granted is left to hint-reward-check |
| Study Hints (bulb): open it, walk its screens and tabs, verify its cases | 2026-10-05 00:38:22 | 20261005-003245-chrono-2FYKPJ#13 | Studied: loss popup, restart, force-stop, hint bulb, banner rotation; REVIVE and hint reward not tested (ad never closed); see cases |
| Study Banner ad: open it, walk its screens and tabs, verify its cases | 2026-10-05 00:38:22 | 20261005-003245-chrono-2FYKPJ#13 | Studied: loss popup, restart, force-stop, hint bulb, banner rotation; REVIVE and hint reward not tested (ad never closed); see cases |
| Cryptogram level: lose via 3 mistakes, restart, exit app mid-level, hint bulb | 2026-10-05 00:38:21 | 20261005-003245-chrono-2FYKPJ#13 | Studied: loss popup, restart, force-stop, hint bulb, banner rotation; REVIVE and hint reward not tested (ad never closed); see cases |
| Study Home screen: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:50:09 | 20261003-234451-chrono-2FYKPJ#19 | home on fresh, after level 1 (counters, banner ad), settings entry; lives popup not reachable, locked cards inert |
| Study Cryptogram level: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:50:09 | 20261003-234451-chrono-2FYKPJ#19 | walked L1 tutorial, win card, L2 HUD, quit via home; loss, restart, exit-app, elements left open (lives/mistakes cost needs deliberate loss) |
| Study How to play: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:47:06 | 20261003-234451-chrono-2FYKPJ#7 | 3 pages walked and marked, X closes all |
| Map the game: play until the main menu and every entry point is visible; list each entry point as open (a study goal), locked with its unlock condition (an unlock goal) or unclear (an experiment) | 2026-10-03 20:18:35 | 20261003-201504-chrono-2FYKPJ#13 | Fresh install (level 1). Home: lives 5 FULL (tap does nothing), gear > Settings (Notifications, Vibration, Restore Purchases, Support, Promo Code, How to play 3 pages, Privacy Policy, Terms of Use), Daily Challenge locked 'complete 15 more levels', Daily Tasks locked 'complete 3 levels', START LEVEL 1 with tutorial hand. No shop/currency/event entry on a fresh install; experiment home-after-levels set for entries that appear with progress. |
