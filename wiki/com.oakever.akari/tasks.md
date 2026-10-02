# Tasks: MeowTrail

Status: **▶️ active** — ready now: 19

Mode: **goals** — work through the session goals in order; play levels only as far as an unlock or experiment goal needs; register anything new you notice as a feature or a goal, do not pursue it now

Progress reached: **level 121 next** · last new feature found at: **tutorial 2**

Goals: study 12, experiment 2 · maps: level 55 — 3 new, level 73 — 0 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **Cat placement (Light Up rules)** — mastered, solver, levels won 112, typical 0.3 min

Google Play version: **1.0.2** (checked 2026-10-01 20:09:25) · analyzed version: **1.0.2** · FTUE from a fresh install: **2026-10-01**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Lose 3 hearts on an easy level and tap Restart on the Almost! popup | check | [Hearts (mistakes per level)](features/hearts.md) | knowledge gap |  |
| Single tap an empty cell, tap the X again, then double tap an X: what happens | check | X marks (single tap) | knowledge gap |  |
| Next day: open the game and look for daily rewards, offers or a changed Home | daily | Home screen | from the game |  |
| Study Level progression: open it, walk its screens and tabs, verify its cases | study | [Level progression](features/levels.md) | external |  |
| Study Hearts (mistakes per level): open it, walk its screens and tabs, verify its cases | study | [Hearts (mistakes per level)](features/hearts.md) | external |  |
| Study Hint booster (bulb): open it, walk its screens and tabs, verify its cases | study | [Hint booster (bulb)](features/booster-hint.md) | external |  |
| Study X marks (single tap): open it, walk its screens and tabs, verify its cases | study | X marks (single tap) | external |  |
| Study Home screen: open it, walk its screens and tabs, verify its cases | study | Home screen | external |  |
| Study Cat characters (per level set): open it, walk its screens and tabs, verify its cases | study | Cat characters (per level set) | external |  |
| Study Rate us prompt: open it, walk its screens and tabs, verify its cases | study | [Rate us prompt](features/rate-us.md) | external |  |
| Study Interstitial ads: open it, walk its screens and tabs, verify its cases | study | [Interstitial ads](features/ads-interstitial.md) | external |  |
| Study Banner ads: open it, walk its screens and tabs, verify its cases | study | Banner ads | external |  |
| Study Rewarded ads (revive, booster refill): open it, walk its screens and tabs, verify its cases | study | Rewarded ads (revive, booster refill) | external |  |
| Study Help Center (Helpshift): open it, walk its screens and tabs, verify its cases | study | [Help Center (Helpshift)](features/help-center.md) | external |  |
| Study Push notifications: open it, walk its screens and tabs, verify its cases | study | Push notifications | external |  |
| Keep advancing past level 121 to find where content ends (12x12 seen at 114, hard every 10th) | check | [Level progression](features/levels.md) | from the game |  |
| Confirm the interstitial is a ~60 s cooldown since the last interstitial closed (rewarded ads do not reset it) | experiment | [Interstitial ads](features/ads-interstitial.md) | knowledge gap | more data fits the hypothesis: 62-70 (no ad 31-45 s, ad 71-92 s), 71-80 (no ad 35-44 s, ad 75-253 s, ad 47 s after a hint rewarded video), bench 83-107 (no ad 33-35 s, ad 78-81 s) [s:20261001-091349-chrono-2FYKPJ#38] [s:20261001-100940-chrono-2FYKPJ#38] [s:20261001-172422-chrono-2FYKPJ#9] |
| Use the cat booster from 1 to 0 in a level and check whether the next level starts with 0 (counts persist) or 1 (refill per level) | experiment | [Cat booster](features/booster-cat.md) | knowledge gap |  |
| Read the two unread Help Center Ad Issues articles ('Why are there so many ads?', 'There is inappropriate content in an ad.') | check | [Help Center (Helpshift)](features/help-center.md) | knowledge gap | ads-help-articles was closed after one of the three Ad Issues articles [s:20261001-070939-chrono-2FYKPJ#5] |

## Waiting

None.

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

| Task | What to provide | Feature |
|---|---|---|
| Fresh install: at level 9 pick 1-3 stars and 4-5 stars on rate-us (do not submit a review) | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | [Rate us prompt](features/rate-us.md) |

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Check whether cat/hint booster counts persist between levels (hint stayed 1 after AD refill at level 73; earlier notes said reset to 4) | 2026-10-01 22:30:41 | 20261001-221517-chrono-2FYKPJ#41 | Cat and hint booster both showed 1 at the start of every level 108-120 (none used). No sign of a carry-over beyond 1; refilled to 1 per level or stays 1. |
| Keep advancing past level 80 to find where content ends or a new feature appears (hard every 10th, 8x8-10x10 boards) | 2026-10-01 22:30:41 | 20261001-221517-chrono-2FYKPJ#41 | Advanced to 120 (hard 7x7, 9 cats); no end of content, no new feature. 12x12 board seen at L114, 10x10 at 115. Still going. |
| Log every level start, Restart and Revive with ad yes/no to find the interstitial rule | 2026-10-01 22:30:40 | 20261001-221517-chrono-2FYKPJ#41 | Starts 108-120: ad on 109,111,113,115,116,119; none on 108,110,112,114,117,118,120. Restart in 114 (after a no-ad start): no ad. Revive is a rewarded video (AD icon), gives 1 heart back, then next start (116) still had an ad. Not strict alternation; ~half of starts, possibly random/time-based. Banner on some levels only. |
| Survey every screen: capture all entry points and map them to features | 2026-10-01 10:16:47 | 20261001-100940-chrono-2FYKPJ#17 | Walked Home, Settings, level screen with tips, hint popup (text reason + Apply), hint AD badge and rewarded video (Mintegral end card), interstitials (Nova Studio Zoodoku video then Play Store), win screen. Nothing new; cat color varies per level (pink 72, blue 73, dark blue 71). |
| Check whether the game has a Remove Ads or subscription (Help Center chat lists 'Subscription issue') | 2026-10-01 10:16:46 | 20261001-100940-chrono-2FYKPJ#17 | No Remove Ads / subscription / restore purchases / shop anywhere: Home (logo, gear, Level button), Settings (sound, vibration, Help Center, Privacy, ToS, version/build 190, User ID), win and fail screens, booster popups. Only 'Subscription issue' category in Help Center chat form. Likely generic Helpshift template. |
| Test hint (bulb) booster at 0 uses: AD refill, and heart-loss revive cases | 2026-10-01 10:16:19 | 20261001-100940-chrono-2FYKPJ#16 | Hint 4->0 after 4 uses (count drops on tap, Apply places cats/X marks with text reason); at 0 badge shows AD; tap runs a ~40s rewarded video (Mintegral end card, close X top-right after ~45s, may chain a 2nd popup close) and gives +1 hint. Heart-loss revive already documented under hearts. |
| Log interstitial cadence over 10 levels (56 none, 57 ad, 58 none, 59 ad, 60 none, 61 ad) and the ad types: playable with Next / Google Play skip | 2026-10-01 09:26:39 | 20261001-091349-chrono-2FYKPJ#38 | Levels 62-70 interstitial before start: 62 none, 63 ad, 64 ad, 65 none, 66 ad, 67 none, 68 ad, 69 none, 70 ad. Mostly alternating but phase shifted at 63/64 (after a heart loss on 63). Types: Colordoku playable-like banner with Next (top-left) which chains to a playable demo with only the corner X (top-right, opens Play Store); Nova Studio video that auto-ends in ~35 s into the Play Store; Royal Match video with skip icon top-left immediately; video with Next then a chained rings-game ad. |
| Open Helpshift Chat with us (read only, do not send) to see the form/fields | 2026-10-01 09:14:42 | 20261001-091349-chrono-2FYKPJ#3 | Chat form: preset categories Ad issue/Bug or Crash/Suggestion/Rules issue/Subscription issue plus free text field; nothing sent. Subscription issue category hints at a subscription (maybe remove ads) not seen in game. |
| Read Ad Issues and Settings articles in Help Center for remove-ads / hidden features; try Chat with us | 2026-10-01 07:10:56 | 20261001-070939-chrono-2FYKPJ#5 | Read skip-ad and more-hints articles; nothing about remove-ads. Chat not used (live-people rule). |
| Survey every screen: capture all entry points and map them to features | 2026-10-01 04:11:40 | 20261001-035425-chrono-2FYKPJ#61 | Walked Home, Settings (home and in-level), Help Center (Helpshift, categories), Privacy/ToS (Chrome), level screen, fail screen Almost (Revive/Restart), win screen, booster AD badge, rewarded ad, interstitial. New: revive, rewarded-ads, help-center |
| Look for remove-ads offer / shop / any currency beyond level 48 | 2026-10-01 04:11:39 | 20261001-035425-chrono-2FYKPJ#61 | No shop, currency or remove-ads purchase on Home, Settings, win, fail screens through level 55. Help Center Ad Issues articles not read: followup ads-help-articles |
| Open Help Center, toggle sound/vibration, Restart button in settings, Privacy/ToS links | 2026-10-01 04:05:57 | 20261001-035425-chrono-2FYKPJ#43 | Sound/vibration toggles, Help Center (Helpshift in-app), Privacy/ToS (Chrome), Restart (interstitial then fresh board with 3 hearts) all verified |
| Check if a rewarded ad exists to refill boosters (cat/hint at 4 each, never refilled) | 2026-10-01 04:01:17 | 20261001-035425-chrono-2FYKPJ#30 | Rewarded ad refills booster by +1 when count is 0 (AD badge). Revive also rewarded ad. |
| Lose all 3 hearts on an easy level once: document fail/revive screen | 2026-10-01 03:59:56 | 20261001-035425-chrono-2FYKPJ#26 | Fail screen Almost! with Revive(ad)/Restart; revive gives 1 heart and keeps board |
| Measure interstitial frequency (every 2 levels? time-based?) and whether rate-us returns | 2026-10-01 03:16:20 | 20261001-024647-chrono-2FYKPJ#109 | Interstitial (skippable video, Next button top-left ~5s, often followed by a second long end-card/playable ad that needs the top-right corner X which opens the Play Store, then sw.py launch) shown when starting EVERY EVEN level (16,18,20..48 seen in two sessions); none before odd levels. Not time-based. Rate-us did not return in levels 19-48. |
| Use the hint booster down to 0 and refill it with the AD badge (cancelled) |  |  | duplicate of hint-booster-refill, done at 20261001-100940-chrono-2FYKPJ#16 |
