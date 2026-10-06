# Tasks: MeowTrail

Status: **▶️ active** — ready now: 4

Mode: **cases** — all features are found: study goals and checks only; do not advance

Progress reached: **level 34** · last new feature found at: **level 21**

Goals: experiment 5 · maps: level 2 — 4 new · search for features closed: Home through level 30 has only the Level N button and the gear (shot 68); Settings (Home and in-level, incl. Restart), Help Center (all 12 tabs read, nothing unseen named), level HUD, win/fail screens and ads all mapped; no locked entry points; genre checklist: no shop/IAP, no-ads, daily, events, collection or currency entry exists (exp-late-entries and exp-no-ads refuted); timed refill is under exp-booster-refill

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **Cat placement (Light Up rules)** — mastered, solver, levels won 34, typical 0.4 min

Google Play version: **1.0.2** (checked 2026-10-05 22:05:43) · analyzed version: **1.0.2** · FTUE from a fresh install: **never**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Experiment: find what sets the win title (BRILLIANT on level 1, PERFECT on level 2) | experiment | [Akari level](features/core-level.md) | knowledge gap |  |
| Experiment: what Revive on the Almost! screen gives (hearts back, board kept) after its rewarded ad | experiment | [Hearts (3 per level)](features/hearts.md) | knowledge gap |  |
| Run each outcome once under Hard levels: Force-stop and relaunch mid-level lands on Home with the same Level N button; reopening gives a RESET board | experiment | Hard levels | knowledge gap |  |
| Experiment: does the every-2nd-start interstitial counter survive an app relaunch | experiment | Interstitial ads | knowledge gap |  |

## Waiting

| Task | Not before | Kind | Feature |
|---|---|---|---|
| Experiment: do the cat and bulb boosters refill by themselves over time (timer or daily) | 2026-10-06 10:19:33 | experiment | [Cat and bulb boosters](features/boosters.md) |

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

| Task | What to provide | Feature |
|---|---|---|
| Replay first-launch Terms consent screen on a fresh install | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | [Terms consent](features/consent.md) |
| Rate us: test stars, Rate Us and whether it returns on win of level 9 | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | Rate us prompt |
| Tutorial: can it be skipped, what happens when the app is left mid-tutorial | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | [Tutorial](features/tutorial.md) |

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Experiment: find the interstitial rule: every 2nd level start from the win-screen button (a counter), not even level numbers | 2026-10-06 02:42:43 | 20261006-023308-chrono-2FYKPJ#20 | Hypothesis 'counter of win-screen starts only' refuted: Home start shifts the alternation. Rule seen: an ad on every 2nd level start counting any start (win button, Home, in-level Restart), none after an ad. Sequence L31 none, L32 ad, L33 none, L34 ad, L34(Home) none, L35 ad. Not even level numbers (L31..35). Time cooldown not excluded but starts were 1-2 min apart with strict alternation. |
| Experiment: tap Restart in the in-level Settings: is there a confirmation, what it costs, and is the board cleared with 3 hearts | 2026-10-06 02:36:14 | 20261006-023308-chrono-2FYKPJ#5 | Free full reset: no confirmation, empty board, 3 hearts, boosters unchanged; but an interstitial ad plays right after the tap (~50 s, ended in Play Store, launch returned to fresh board). Level 30 was started from Home with no ad, the ad came from Restart. |
| Experiment: home shows only Level button and gear; do shop/daily/map entries appear at later levels? | 2026-10-06 00:33:48 | 20261006-002027-chrono-2FYKPJ#45 | At level 30 Home still shows only the logo, settings gear and the Level 30 button (with a Hard badge), shot 68; no shop, daily, map or collection entry appeared over levels 2-30 |
| Look for a remove-ads offer now that ads run from level 16 (Home, Settings, win screen, after an interstitial) | 2026-10-06 00:33:48 | 20261006-002027-chrono-2FYKPJ#45 | No remove-ads offer: Home at L30 (shot 68), Home Settings (shot 42), in-level Settings (shot 71) and the L29 win screen after an interstitial (shot 38) show none; Help Center Ad Issues article says nothing about ad removal (step 38) |
| Read the unread Help Center tabs (Beginners Guide, Items, Ad Issues, the tab past Items) and the Gameplay articles on exit and restart; every unseen feature they name is recorded | 2026-10-06 00:29:55 | 20261006-002027-chrono-2FYKPJ#41 | Read tabs: Popular, Beginners Guide (list + Why did I lose a life), Gameplay (exit, restart articles), Failure & Revive (list), Items (list + more hints: a few free hints for new players, reward video when out, no timer or daily refill), Settings, Ad Issues (many ads: no ad removal offered), Notifications, Privacy, Updates, Feedbacks, About (tab lists only). Nothing new in the feature map: no daily, no ad removal, no skins. Exit article: back arrow keeps in-level progress (matches exp-exit-app-board). Restart article says the settings panel INSIDE a level has a Restart option that clears progress (Home settings lacks it): to be checked in a level. |
| Experiment: find what sets the cat skin on each level (blue L21, pink L22, grey-blue L23, yellow L24) and whether skins are a collection with an entry | 2026-10-06 00:27:23 | 20261006-002027-chrono-2FYKPJ#20 | Cosmetic rotation, period 5 by level number: L26 blue, L27 pink, L28 grey-blue (light blue/white), L29 yellow, L30 purple (Hard); with L21-24 known, L20/25/30 purple, 21/26 blue, 22/27 pink, 23/28 grey-blue, 24/29 yellow. Skin shows on counter, cat booster, tutorial hints and win-box cats (checked blue L26, pink L27). Restart (force-stop) and reopen L26 kept blue. No collection/album entry on Home (only gear and Level button), level screen, win screens; Settings and Help to be seen in help-center goal. |
| Experiment: after leaving the app mid-level, is the board kept (placed cats, lost hearts) or reset | 2026-10-06 00:23:10 | 20261006-002027-chrono-2FYKPJ#10 | Board is kept for background (30 s, home key + launch: wrong-cat X and 2 hearts intact) and for back arrow to Home and reopen (X and 2 hearts kept). Force-stop restart RESETS: empty board, 3 hearts; cat booster use not refunded (still AD). Only 1 correct cat placed (booster) plus 1 wrong cat, not 2 cats. Help article on exit/restart read in exp-help-articles. |
| Bulb booster at zero: is the refill also a rewarded video, how many units | 2026-10-05 22:17:52 | 20261005-221436-chrono-2FYKPJ#17 | Bulb used 4 times from 4 (badge 4>3>2>1>AD; each hint charged on open). Tapping AD played a rewarded video that ended on the Play Store; launch returned with bulb badge 1 (+1 unit per video, frame 20). |
| Open the bulb hint and close it without Apply: is the unit refunded? | 2026-10-05 22:16:19 | 20261005-221436-chrono-2FYKPJ#8 | Hint cannot be closed without Apply: system Back, taps on the veil and the back arrow all do nothing (frames 7-10); only Apply closes it. The unit is charged on open (badge 4 -> 3 at frame 6), so no cancel/refund path. |
| Study Tutorial: open it, walk its screens and tabs, verify its cases | 2026-10-05 22:15:26 | 20261005-221436-chrono-2FYKPJ#3 | Walked: tutorial only on fresh install (2 scripted boards, Got it -> L1); no replay/How-to-play in Settings or Home; skip/leave-mid-tutorial needs fresh (task tutorial-skip-fresh) |
| Study the Rate us prompt (after level 9): stars, Rate Us, X, whether it returns (cancelled) | 2026-10-05 14:18:12 | 20261005-141041-chrono-2FYKPJ#10 | Duplicate of rate-us-answers: the prompt showed only on the level 9 win and does not come back on this install (no prompt on wins 10-24), so stars/Rate Us/return need a fresh install; chk-screen, chk-entry, chk-appeared already closed |
| Banner ad: on which screens it shows (level, win, Home), whether it has a close cross, and whether it was on levels before 16 | 2026-10-05 14:18:12 | 20261005-141041-chrono-2FYKPJ#9 | Banner on every level screen 21-24 with rotating creatives (shots 4, 12); not on the win screen (shot 7) nor Home (shot 2); only AdChoices i, no cross; absent on levels 15 and earlier (20261005-080420#42) |
| Interstitial ads: which level starts show one from level 21 to 30, and how the ad closes (timer, cross, what follows) | 2026-10-05 14:18:11 | 20261005-141041-chrono-2FYKPJ#9 | Win-screen Level N starts 16,18,20,22,24 had an interstitial, 17,19,21 (Home),23 none: every even level start. No close cross in 20-28 s; both L22 and L24 ads ended in the Play Store, launch returned to the level. Levels 25-30 not checked, the pattern held over 5 pairs |
| Study Interstitial ads: open it, walk its screens and tabs, verify its cases | 2026-10-05 14:16:20 | 20261005-141041-chrono-2FYKPJ#10 | Every even level start from the win screen (16-24); none from Home start of 21 or odd; no close cross, ends in Play Store after ~20-28 s |
| Study Banner ad on the level screen: open it, walk its screens and tabs, verify its cases | 2026-10-05 14:16:20 | 20261005-141041-chrono-2FYKPJ#10 | Banner on level screens from 16, rotating creatives, hidden on win screen, no close control |
| Run quit and exit-app under Hard levels: needs the next Hard level (30) (cancelled) | 2026-10-05 08:32:05 | 20261005-080420-chrono-2FYKPJ#56 | duplicate of outcomes-hard-level (the matrix goal now holds only quit and exit-app; next Hard level is 30) |
| Find the first level that shows an interstitial (none through level 4) and register the ad feature | 2026-10-05 08:32:02 | 20261005-080420-chrono-2FYKPJ#41 | First interstitial on the start of level 16 (none on 4-15); banner on the level screen from 16; registered as interstitial-ad and banner-ad |
| Study Hard levels: open it, walk its screens and tabs, verify its cases | 2026-10-05 08:25:33 | 20261005-080420-chrono-2FYKPJ#56 | Hard every 10th level (10, 20): red Hard badge above the Level button on the previous win screen and a Hard label under the level title; same rules, bigger boards; win and fail screens as base; quit and exit-app cells still open (task hard-quit-exit) |
| Find why Hard levels appeared: Help Center says Hard badge on the level entry; trigger unknown, not yet seen | 2026-10-05 08:12:16 | planner | the trigger is recorded as a fact: level 10 is the first Hard level; announced by a red Hard badge above the Level N button on the win screen of level 9 [20261005-080420-chrono-2FYKPJ#27] |
| Study the notification prompt: whether it comes back after Don't allow, and any in-game toggle for it | 2026-10-05 08:06:35 | 20261005-080420-chrono-2FYKPJ#9 | No prompt after force-stop relaunch on progressed install; no in-game toggle in Settings |
| Study Settings (toggles, help center, links) | 2026-10-05 08:06:01 | 20261005-080420-chrono-2FYKPJ#8 | Sound and vibration toggles tested and restored; Privacy/Terms open Chrome, launch returns; no notification toggle in Settings |
| Find first Hard level (badge on level entry, banner) (cancelled) | 2026-10-05 00:32:41 | review-20261005 | duplicate of appeared-hard-level (finding the first Hard level is its trigger; chk-frequency covers how often) [20261005-002947-chrono-2FYKPJ#6] |
| Study Home screen: open it, walk its screens and tabs, verify its cases | 2026-10-05 00:31:43 | 20261005-002947-chrono-2FYKPJ#11 | walked and verified; see cases |
| Study Help Center: open it, walk its screens and tabs, verify its cases | 2026-10-05 00:31:42 | 20261005-002947-chrono-2FYKPJ#11 | walked and verified; see cases |
| Study Hearts (3 per level): open it, walk its screens and tabs, verify its cases | 2026-10-05 00:31:42 | 20261005-002947-chrono-2FYKPJ#11 | walked and verified; see cases |
| Experiment: find what costs a heart and what happens at zero hearts (a loss outcome, its screen, retry offer and price) | 2026-10-03 23:36:31 | 20261003-232850-chrono-2FYKPJ#18 | Each wrong cat costs a heart (red X); at 0 hearts Almost! shows Revive (rewarded ad) and Restart (free, same board, 3 hearts). No lives meter between levels. |
| Study cat and bulb boosters (count 5 each, refill) | 2026-10-03 23:34:46 | 20261003-232850-chrono-2FYKPJ#26 | Studied; see cases |
| Study Terms consent: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:34:46 | 20261003-232850-chrono-2FYKPJ#26 | Studied; see cases |
| Study Akari level: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:34:46 | 20261003-232850-chrono-2FYKPJ#26 | Studied; see cases |
| Map the game: play until the main menu and every entry point is visible; list each entry point as open (a study goal), locked with its unlock condition (an unlock goal) or unclear (an experiment) | 2026-10-03 20:14:10 | 20261003-200925-chrono-2FYKPJ#16 | Fresh install: consent, notification prompt, 2-board tutorial, level 1 straight away. Home has only the Level N button and settings gear; settings has sound, vibration, Help Center, policy links. No map, shop or daily seen through level 2; boosters and hearts on the level HUD. Remaining entries are open: study-settings, study-boosters, exp-late-entries. |
