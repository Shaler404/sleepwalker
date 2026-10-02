# Tasks: Amaze GO!

Status: **▶️ active** — ready now: 24; update the game on the phone in Google Play to recheck on the new version: installed 1.31.0, Google Play 1.32.0

Mode: **goals** — work through the session goals in order; play levels only as far as an unlock or experiment goal needs; register anything new you notice as a feature or a goal, do not pursue it now

Progress reached: **level 4** · last new feature found at: **level 3**

Goals: study 12, unlock 3, experiment 8 · maps: level 4 — 12 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **arrows-escape** — mastered, manual, levels won 3, typical 0.4 min

Google Play version: **1.32.0** (checked 2026-10-01 20:09:25) · analyzed version: **1.31.0** · FTUE from a fresh install: **2026-10-01**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Study the main menu: Play button, card carousel, lock tooltips | study | [Main menu](features/main-menu.md) | knowledge gap |  |
| Study Settings: sound/vibration/music toggles, Guideline toggle, Privacy/ToS rows | study | [Settings](features/settings.md) | knowledge gap |  |
| Study color themes: Eye Comfort and Dark Mode on the board | study | [Color themes (Eye Comfort / Dark Mode)](features/themes.md) | knowledge gap |  |
| Study the level result screen: stars vs mistakes, score, time arrow, Today's Levels | study | [Level result screen](features/level-result.md) | knowledge gap |  |
| Study the Save Your Progress screen (look only, never sign in) | study | [Save Your Progress (cloud save)](features/save-progress.md) | knowledge gap |  |
| Study Rate Us and Feedback (look only, back out of store/email) | study | [Rate Us / Feedback](features/rate-feedback.md) | knowledge gap |  |
| Reach level 11 to unlock Bronze League | unlock | [Leagues (Bronze League)](features/leagues.md) | knowledge gap |  |
| Reach level 16 to unlock the Countryside Caper event | unlock | [Event (Countryside Caper)](features/event.md) | knowledge gap |  |
| Reach level 20 to unlock Daily Challenge | unlock | [Daily Challenge](features/daily-challenge.md) | knowledge gap |  |
| Tapping a blocked arrow costs one blue drop; losing all 3 fails the level | experiment | [Lives (blue drops) and mistakes](features/lives.md) | knowledge gap |  |
| A hint button appears on later levels (result screen counts hints used) | experiment | [Hints (lightbulb)](features/hints.md) | knowledge gap |  |
| Study the level HUD: back arrow, in-level settings gear, drops, guideline toggle effect on the board | study | [Level screen HUD (lives, theme, settings)](features/level-hud.md) | knowledge gap |  |
| Study Leagues (Bronze League): open it, walk its screens and tabs, verify its cases | study | [Leagues (Bronze League)](features/leagues.md) | external |  |
| Study Daily Challenge: open it, walk its screens and tabs, verify its cases | study | [Daily Challenge](features/daily-challenge.md) | external |  |
| Study Event (Countryside Caper): open it, walk its screens and tabs, verify its cases | study | [Event (Countryside Caper)](features/event.md) | external |  |
| Study Lives (blue drops) and mistakes: open it, walk its screens and tabs, verify its cases | study | [Lives (blue drops) and mistakes](features/lives.md) | external |  |
| Study Hints (lightbulb): open it, walk its screens and tabs, verify its cases | study | [Hints (lightbulb)](features/hints.md) | external |  |
| Look for ads: record any interstitial after a level, a rewarded-ad offer (extra drops, hint) and a banner, with the level where each first appears | experiment | [Level result screen](features/level-result.md) | knowledge gap |  |
| Look for a shop, IAP packs or a Remove Ads purchase and where they are reached (none seen on the main menu or settings by level 4) | experiment | [Main menu](features/main-menu.md) | knowledge gap |  |
| Look for daily rewards, streaks or a login calendar (a typical retention feature not seen yet) | experiment | [Main menu](features/main-menu.md) | knowledge gap |  |
| Day-2 launch: notification prompt again?, Daily Challenge card date, Today's Levels reset | check | [Level result screen](features/level-result.md) | from the game | On the first launch of a new day: does the Android notification prompt come back [s:20261001-204000-chrono-2FYKPJ#2]; does the locked Daily Challenge card change from 'Oct 1' [s:20261001-204000-chrono-2FYKPJ#10]; does Today's Levels on the next result restart at 1 [s:20261001-204000-chrono-2FYKPJ#4] |
| Find the first level whose Difficulty is not Normal | experiment | [Level result screen](features/level-result.md) | knowledge gap |  |
| What the green up arrow next to Time on the result screen means | experiment | [Level result screen](features/level-result.md) | knowledge gap |  |
| Is the splash quote shown on every launch or only after a fresh install | experiment | [Consent screen (ToS / Privacy)](features/consent.md) | knowledge gap |  |

## Waiting

None.

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

| Task | What to provide | Feature |
|---|---|---|
| Recheck the features on version 1.32.0 | update the game on the phone in Google Play to recheck on the new version: installed 1.31.0, Google Play 1.32.0 |  |

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Map the game: play until the main menu and every entry point is visible; list each entry point as open (a study goal), locked with its unlock condition (an unlock goal) or unclear (an experiment) | 2026-10-01 20:45:28 | 20261001-204000-chrono-2FYKPJ#22 | Main menu (via back arrow in a level): settings gear + carousel of 3 cards: Bronze League (Unlock Lv.11), Daily Challenge Oct 1 (Unlock Lv.20), Event Countryside Caper (Unlock Lv.16, tooltip confirms) + Play Level N. Settings: Sound/Vibration/Music/Guideline toggles, Save Your Progress, Rate Us, Feedback, Privacy, ToS. Level HUD: back, palette (themes: default, Eye Comfort, Dark Mode), gear, 3 drops. Result screen: stars, difficulty, time, score, Today's Levels, accuracy, mistakes, hints. Unclear: drops penalty, hint button (not shown by level 3). |
| Record the FTUE: consent, notification prompt, tutorial level 1 'Tap an arrow' | 2026-10-01 20:45:22 | 20261001-204000-chrono-2FYKPJ#22 | Fresh install played this session: Welcome/consent (Accept) -> splash quote -> Android notification prompt (Don't allow) -> tutorial level 1 'Tap an arrow' with a hand on the down arrow, no HUD -> Flawless result -> level 2 shows full HUD (back, Level N, palette, gear, 3 drops). Main menu is reached only via the back arrow in a level (game opens straight into levels). |
