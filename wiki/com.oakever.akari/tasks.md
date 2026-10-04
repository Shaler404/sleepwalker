# Tasks: MeowTrail

Status: **▶️ active** — ready now: 13

Mode: **goals** — work through the session goals in order; play levels only as far as an unlock or experiment goal needs; register anything new you notice as a feature or a goal, do not pursue it now

Progress reached: **level 3** · last new feature found at: **first launch, before level 1**

Goals: study 6, experiment 7 · maps: level 2 — 4 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **Cat placement (Light Up rules)** — mastered, solver, levels won 3, typical 0.5 min

Google Play version: **1.0.2** (checked 2026-10-03 19:29:54) · analyzed version: **1.0.2** · FTUE from a fresh install: **never**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Study Settings (toggles, help center, links) | study | [Settings](features/settings.md) | knowledge gap |  |
| Experiment: home shows only Level button and gear; do shop/daily/map entries appear at later levels? | experiment | [Home screen](features/home.md) | knowledge gap |  |
| Study Tutorial: open it, walk its screens and tabs, verify its cases | study | [Tutorial](features/tutorial.md) | external |  |
| Study Home screen: open it, walk its screens and tabs, verify its cases | study | [Home screen](features/home.md) | external |  |
| Study Help Center: open it, walk its screens and tabs, verify its cases | study | [Help Center](features/help-center.md) | external |  |
| Study Hearts (3 per level): open it, walk its screens and tabs, verify its cases | study | [Hearts (3 per level)](features/hearts.md) | external |  |
| Experiment: find what sets the win title (BRILLIANT on level 1, PERFECT on level 2) | experiment | [Akari level](features/core-level.md) | knowledge gap |  |
| Study the notification prompt: whether it comes back after Don't allow, and any in-game toggle for it | study | [Notification permission prompt](features/notifications.md) | knowledge gap |  |
| Bulb booster at zero: is the refill also a rewarded video, how many units | experiment | [Cat and bulb boosters](features/boosters.md) | knowledge gap |  |
| Experiment: after leaving the app mid-level, is the board kept (placed cats, lost hearts) or reset | experiment | [Akari level](features/core-level.md) | knowledge gap |  |
| Experiment: what Revive on the Almost! screen gives (hearts back, board kept) after its rewarded ad | experiment | [Hearts (3 per level)](features/hearts.md) | knowledge gap |  |
| Open the bulb hint and close it without Apply: is the unit refunded? | experiment | [Cat and bulb boosters](features/boosters.md) | knowledge gap |  |
| Find the first level that shows an interstitial (none through level 4) and register the ad feature | experiment |  | knowledge gap |  |

## Waiting

None.

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

| Task | What to provide | Feature |
|---|---|---|
| Replay first-launch Terms consent screen on a fresh install | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | [Terms consent](features/consent.md) |

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Experiment: find what costs a heart and what happens at zero hearts (a loss outcome, its screen, retry offer and price) | 2026-10-03 23:36:31 | 20261003-232850-chrono-2FYKPJ#18 | Each wrong cat costs a heart (red X); at 0 hearts Almost! shows Revive (rewarded ad) and Restart (free, same board, 3 hearts). No lives meter between levels. |
| Study cat and bulb boosters (count 5 each, refill) | 2026-10-03 23:34:46 | 20261003-232850-chrono-2FYKPJ#26 | Studied; see cases |
| Study Terms consent: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:34:46 | 20261003-232850-chrono-2FYKPJ#26 | Studied; see cases |
| Study Akari level: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:34:46 | 20261003-232850-chrono-2FYKPJ#26 | Studied; see cases |
| Map the game: play until the main menu and every entry point is visible; list each entry point as open (a study goal), locked with its unlock condition (an unlock goal) or unclear (an experiment) | 2026-10-03 20:14:10 | 20261003-200925-chrono-2FYKPJ#16 | Fresh install: consent, notification prompt, 2-board tutorial, level 1 straight away. Home has only the Level N button and settings gear; settings has sound, vibration, Help Center, policy links. No map, shop or daily seen through level 2; boosters and hearts on the level HUD. Remaining entries are open: study-settings, study-boosters, exp-late-entries. |
