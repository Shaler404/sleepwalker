# Tasks: MeowTrail

Status: **▶️ active** — ready now: 6

Mode: **advance** — move through the content as fast as possible; register every new feature and write down every branch as a case or task for later, do not test them now

Progress reached: **level 55** · last new feature found at: **tutorial 2**

Screen surveys: level 55 — 3 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **Cat placement (Light Up rules)** — mastered, solver, levels won 56, typical 0.4 min

Google Play version: **1.0.2** (checked 2026-10-01 02:46:28) · analyzed version: **1.0.2** · FTUE from a fresh install: **2026-10-01**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Analyze the game, version 1.0.2 | analysis |  | external | find all features and work through all user cases |
| Read Ad Issues and Settings articles in Help Center for remove-ads / hidden features; try Chat with us | check | [Help Center (Helpshift)](features/help-center.md) | from the game |  |
| Log every level start, Restart and Revive with ad yes/no to find the interstitial rule | check | [Interstitial ads](features/ads-interstitial.md) | knowledge gap | levels 52-54 had no ad on three starts in a row; "every 2nd start" is not the rule |
| Lose 3 hearts on an easy level and tap Restart on the Almost! popup | check | [Hearts (mistakes per level)](features/hearts.md) | knowledge gap |  |
| Use the hint booster down to 0 and refill it with the AD badge | check | [Hint booster (bulb)](features/booster-hint.md) | knowledge gap |  |
| Single tap an empty cell, tap the X again, then double tap an X: what happens | check | X marks (single tap) | knowledge gap |  |

## Waiting

| Task | Not before | Kind | Feature |
|---|---|---|---|
| Next day: open the game and look for daily rewards, offers or a changed Home | 2026-10-02 04:00:00 | daily | Home screen |

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

| Task | What to provide | Feature |
|---|---|---|
| Fresh install: at level 9 pick 1-3 stars and 4-5 stars on rate-us (do not submit a review) | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | [Rate us prompt](features/rate-us.md) |

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Survey every screen: capture all entry points and map them to features | 2026-10-01 04:11:40 | 20261001-035425-chrono-2FYKPJ#61 | Walked Home, Settings (home and in-level), Help Center (Helpshift, categories), Privacy/ToS (Chrome), level screen, fail screen Almost (Revive/Restart), win screen, booster AD badge, rewarded ad, interstitial. New: revive, rewarded-ads, help-center |
| Look for remove-ads offer / shop / any currency beyond level 48 | 2026-10-01 04:11:39 | 20261001-035425-chrono-2FYKPJ#61 | No shop, currency or remove-ads purchase on Home, Settings, win, fail screens through level 55. Help Center Ad Issues articles not read: followup ads-help-articles |
| Open Help Center, toggle sound/vibration, Restart button in settings, Privacy/ToS links | 2026-10-01 04:05:57 | 20261001-035425-chrono-2FYKPJ#43 | Sound/vibration toggles, Help Center (Helpshift in-app), Privacy/ToS (Chrome), Restart (interstitial then fresh board with 3 hearts) all verified |
| Check if a rewarded ad exists to refill boosters (cat/hint at 4 each, never refilled) | 2026-10-01 04:01:17 | 20261001-035425-chrono-2FYKPJ#30 | Rewarded ad refills booster by +1 when count is 0 (AD badge). Revive also rewarded ad. |
| Lose all 3 hearts on an easy level once: document fail/revive screen | 2026-10-01 03:59:56 | 20261001-035425-chrono-2FYKPJ#26 | Fail screen Almost! with Revive(ad)/Restart; revive gives 1 heart and keeps board |
| Measure interstitial frequency (every 2 levels? time-based?) and whether rate-us returns | 2026-10-01 03:16:20 | 20261001-024647-chrono-2FYKPJ#109 | Interstitial (skippable video, Next button top-left ~5s, often followed by a second long end-card/playable ad that needs the top-right corner X which opens the Play Store, then sw.py launch) shown when starting EVERY EVEN level (16,18,20..48 seen in two sessions); none before odd levels. Not time-based. Rate-us did not return in levels 19-48. |
