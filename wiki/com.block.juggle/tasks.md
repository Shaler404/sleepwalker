# Tasks: Block Blast!

Status: **▶️ active** — ready now: 12; update the game on the phone in Google Play to recheck on the new version: installed 10.6.5, Google Play 10.8.0

Mode: **goals** — work through the session goals in order; play levels only as far as an unlock or experiment goal needs; register anything new you notice as a feature or a goal, do not pursue it now

Progress reached: **classic best 724, 2 games** · last new feature found at: **—**

Goals: study 6, experiment 8 · maps: ? — 8 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **classic** — studying, solver, levels won 0

Google Play version: **10.8.0** (checked 2026-10-01 20:09:25) · analyzed version: **10.6.5** · FTUE from a fresh install: **2026-10-01**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Study classic mode: game-over flow, revive offer, scoring and combos | study | [Classic endless mode](features/classic.md) | knowledge gap | two games played for score ran 517 s and 489 s without game over [s:20261001-230945-chrono-2FYKPJ#63]; reach the end screen with the solver gameover mode ({"mode": "gameover"} via --board), do not play for score |
| Study Settings: sound, BGM, vibration, More Settings, contact | study | [Settings](features/settings.md) | knowledge gap |  |
| Study More Games: 8 built-in mini-games (One Line, Tic Tac Toe, Fruit Merge, Water Sort, Onet, Mahjong, Sudoku, Block Slide) | study | [More Games (built-in mini-games)](features/more-games.md) | knowledge gap |  |
| The Default Skin button in Settings is grey and does nothing when tapped: find what unlocks skins (score, games played, days) | experiment | [Skins](features/skins.md) | knowledge gap |  |
| The splash says Adventure Master but only classic is reachable: check whether an Adventure mode appears after some games or a game over | experiment | [Classic endless mode](features/classic.md) | knowledge gap |  |
| When interstitials show: after Replay, after game over, after N moves | experiment | [Interstitial ads](features/ads.md) | knowledge gap | data so far: an interstitial after Settings > Replay [s:20261001-200952-chrono-2FYKPJ#39]; none during play in 724 points / about 45 placements [s:20261001-230945-chrono-2FYKPJ#63] |
| Study Terms and privacy consent: open it, walk its screens and tabs, verify its cases | study | [Terms and privacy consent](features/consent.md) | external |  |
| Study Interstitial ads: open it, walk its screens and tabs, verify its cases | study | [Interstitial ads](features/ads.md) | external |  |
| Study Replay (restart game): open it, walk its screens and tabs, verify its cases | study | [Replay (restart game)](features/replay.md) | external | reopened by the dream of 2026-10-02: Replay was only seen with a stuck ad and an app restart [s:20261001-200952-chrono-2FYKPJ#39-42]; tap Replay and leave the ad without restarting |
| Look for monetization: a shop, a no-ads purchase, rewarded-ad placements (revive, extra pieces) and banners | experiment | [Interstitial ads](features/ads.md) | knowledge gap |  |
| Make classic fast: check the lab fixes in play (touch on a tray block, warm-up pull after a refill, barred-move memory) and reach game over with the gameover mode within the 5-min budget | experiment | [Classic endless mode](features/classic.md) | knowledge gap | session 20261001-230945-chrono-2FYKPJ lost ~24 of 63 steps to the solver repeating one plan on an unchanged frame [s:20261001-230945-chrono-2FYKPJ#14-18] [s:20261001-230945-chrono-2FYKPJ#42-52] [s:20261001-230945-chrono-2FYKPJ#57-63] |
| Is the blue diamond behind the score a "current score = best score" marker? | experiment | [Classic endless mode](features/classic.md) | knowledge gap | seen at 201/201 [s:20261001-200952-chrono-2FYKPJ#30], 403/403 [s:20261001-230945-chrono-2FYKPJ#32], 724/724 [s:20261001-230945-chrono-2FYKPJ#63]; absent at 0 with best 261 [s:20261001-230945-chrono-2FYKPJ#0] |

## Waiting

| Task | Not before | Kind | Feature |
|---|---|---|---|
| Look for retention and LiveOps: daily rewards, daily challenge, streaks, leaderboards or events on the next day's launch | 2026-10-02 16:23:18 | experiment |  |

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

| Task | What to provide | Feature |
|---|---|---|
| Recheck the features on version 10.8.0 | update the game on the phone in Google Play to recheck on the new version: installed 10.6.5, Google Play 10.8.0 |  |
| Explain the score jump from 6 to 124 between the tutorial and the first Settings visit | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | [First-launch tutorial](features/tutorial.md) |

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Study Skins: open it, walk its screens and tabs, verify its cases (cancelled) | 2026-10-02 04:30:00 | dream | nothing to walk yet: the grey Default Skin button opens nothing [s:20261001-200952-chrono-2FYKPJ#32]; covered by skins-unlock, which sets a new study goal once skins open |
| Reach game over in classic: record result screen, revive offer, ads (cancelled) | 2026-10-01 23:20:30 | 20261001-230945-chrono-2FYKPJ#63 | duplicate of study-classic, whose title and its game-over case already cover the result screen, revive offer and ads |
| Map the game: play until the main menu and every entry point is visible; list each entry point as open (a study goal), locked with its unlock condition (an unlock goal) or unclear (an experiment) | 2026-10-01 20:21:06 | 20261001-200952-chrono-2FYKPJ#42 | No main menu: the game opens straight into classic endless 8x8 mode. Only entry: gear -> Settings (Sound, BGM, Vibration slider, More Games with 8 built-in mini-games, More Settings with version/contact/share/social/ToS/privacy/about, Replay which plays an interstitial, Default Skin grey and inactive). Open -> study-classic, study-settings, study-more-games; unclear -> skins-unlock, adventure-mode (splash says Adventure Master), ads-cadence. Game over not reached. |
| Record the first-launch flow: consent, notification prompt, 1-step 2x2 tutorial | 2026-10-01 20:21:00 | 20261001-200952-chrono-2FYKPJ#42 | Seen this session on a fresh install (steps 0-5): Terms/Privacy consent with one Accept button, Android notification prompt, no menu, a scripted board with a 2x2 hole and a hand hint; placing the 2x2 clears 2 rows + 2 columns (+6, Excellent!) and the endless classic game starts |
