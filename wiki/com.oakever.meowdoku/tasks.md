# Tasks: Meowdoku: Brain Puzzle Games

Status: **▶️ active** — ready now: 27

Mode: **goals** — work through the session goals in order; play levels only as far as an unlock or experiment goal needs; register anything new you notice as a feature or a goal, do not pursue it now

Progress reached: **level 126** · last new feature found at: **level 66**

Goals: study 15, experiment 3 · maps: level 40 — 6 new, level 67 — 0 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **Cat placement on color regions (Queens-like)** — mastered, solver, levels won 128, typical 1.0 min

Google Play version: **1.18.0** (checked 2026-10-01 20:09:25) · analyzed version: **1.18.0** · FTUE from a fresh install: **2026-10-01**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Win a level to extend the daily streak; record the day's reward — day 1 of 7 | daily | [Daily streak (yarn ball)](features/streak.md) | from the game |  |
| Check the fish leaderboard result and rank rewards after the event ends | check | [Fish leaderboard event (podium on home)](features/fish-event.md) | from the game |  |
| Trigger the Rate Us popup again and test the low-star path, never submit (not seen again on levels 9-127) | check | [Rate Us popup](features/rate-us.md) | from the game |  |
| Next day: play the new Daily Challenge and look for a reward or calendar | daily | [Daily Challenge](features/daily-challenge.md) | from the game |  |
| Collect variants of the level-start banner ('That was a clean solve! Only 18.2% can say the same.', seen L65): when does it show | check | [Level start stat banner](features/level-start-banner.md) | from the game |  |
| Catalog all win titles and subtitle lines by mistakes/board (new: Masterful, Crystal Clear, Persevered, Immaculate) | check | [Win screen titles (Exact, Untouchable, Stellar, Masterclass, Crystal Clear, Unreal)](features/win-rank.md) | from the game | "Masterful" was listed by an agent but no win frame showed it (20261001-115413-chrono-2FYKPJ); confirm before adding it |
| Win a level with exactly 2 fish lost (1 left) done=Brilliant; test win after Restart/Get 3 Fishes ad and win with 3 mistakes across a restart: titles? | check | [Win screen titles (Exact, Untouchable, Stellar, Masterclass, Crystal Clear, Unreal)](features/win-rank.md) | from the game |  |
| Catalog Hard-tagged levels (Hard from L30; tag on the next-level button seen before L90): frequency, reward, win titles | check | [Win screen titles (Exact, Untouchable, Stellar, Masterclass, Crystal Clear, Unreal)](features/win-rank.md) | from the game |  |
| Study Level score: open it, walk its screens and tabs, verify its cases | study | Level score | external |  |
| Study Fish (3 mistake lives per level): open it, walk its screens and tabs, verify its cases | study | [Fish (3 mistake lives per level)](features/lives-fish.md) | external |  |
| Study Settings: open it, walk its screens and tabs, verify its cases | study | [Settings](features/settings.md) | external |  |
| Study Daily streak (yarn ball): open it, walk its screens and tabs, verify its cases | study | [Daily streak (yarn ball)](features/streak.md) | external |  |
| Study Daily Challenge: open it, walk its screens and tabs, verify its cases | study | [Daily Challenge](features/daily-challenge.md) | external |  |
| Study Rate Us popup: open it, walk its screens and tabs, verify its cases | study | [Rate Us popup](features/rate-us.md) | external |  |
| Study Fish leaderboard event (podium on home): open it, walk its screens and tabs, verify its cases | study | [Fish leaderboard event (podium on home)](features/fish-event.md) | external |  |
| Study Profile (avatar, frame, nickname): open it, walk its screens and tabs, verify its cases | study | Profile (avatar, frame, nickname) | external |  |
| Study Save progress (Facebook/Google sign-in, Delete Account): open it, walk its screens and tabs, verify its cases | study | Save progress (Facebook/Google sign-in, Delete Account) | external |  |
| Study Language selection: open it, walk its screens and tabs, verify its cases | study | Language selection | external |  |
| Study Feedback / Helpshift support center: open it, walk its screens and tabs, verify its cases | study | Feedback / Helpshift support center | external |  |
| Study Ads: banner, interstitial, rewarded revive: open it, walk its screens and tabs, verify its cases | study | [Ads: banner, interstitial, rewarded revive](features/ads.md) | external |  |
| Study Win screen titles (Exact, Untouchable, Stellar, Masterclass, Crystal Clear, Unreal): open it, walk its screens and tabs, verify its cases | study | [Win screen titles (Exact, Untouchable, Stellar, Masterclass, Crystal Clear, Unreal)](features/win-rank.md) | external |  |
| Study Golden Fish bonus level (win-screen button after a flawless win): open it, walk its screens and tabs, verify its cases | study | [Golden Fish bonus level (win-screen button after a flawless win)](features/golden-fish-level.md) | external |  |
| Study Level start stat banner: open it, walk its screens and tabs, verify its cases | study | [Level start stat banner](features/level-start-banner.md) | external |  |
| Find out what picks the level-start banner text (hint stat vs clean-solve stat) | experiment | [Level start stat banner](features/level-start-banner.md) | knowledge gap |  |
| Look for a remove-ads purchase, shop or IAP offer (none seen through level 126) | experiment | [Ads: banner, interstitial, rewarded revive](features/ads.md) | knowledge gap |  |
| Does the score follow the number of cats the player places? Compare a golden 8x8 (7296), a normal 8x8 with and without a pre-placed cat (6048 / ?) and a 7x7 (6048) | experiment | [Golden Fish bonus level (win-screen button after a flawless win)](features/golden-fish-level.md) | knowledge gap |  |
| Quit dialog on Home (Back): does Quit close the app and what does the X keep | check | [Home screen](features/home.md) | knowledge gap |  |

## Waiting

| Task | Not before | Kind | Feature |
|---|---|---|---|
| Check whether the pending Golden Fish still replaces Level 127 on Home next day | 2026-10-02 10:48:11 | check | [Golden Fish bonus level (win-screen button after a flawless win)](features/golden-fish-level.md) |
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
| Rate Us popup did not appear in L56-66 either: keep watching win screens/level starts; test only low-star path, never submit (cancelled) | 2026-10-02 12:00:00 | dream-2026-10-02-chrono | duplicate of rate-us-low-stars (merged by the dream 2026-10-02): both wait for the Rate Us popup to come back |
| Harness/solver: solve --run places no cats on banner-ad levels though solution is correct; hand taps work. Investigate | 2026-10-02 12:00:00 | 20261001-182015-chrono-2FYKPJ#4 | Not reproduced: solve --run placed every cat with the banner ad up on L104-108 [s:20261001-182015-chrono-2FYKPJ#4] and L97-99 (bench 20261001-180616). The failures in 20261001-115413 (L85, L86) came while Pattern Mode was ON; that is the likely cause, not proven. |
| Keep watching for Rate Us popup in L84+ (not seen L56-83) (cancelled) | 2026-10-01 22:49:43 | review-20261001#None | duplicate of rate-us-trigger-search (same watch for the Rate Us popup) |
| Rate Us popup still not seen through L95; keep watching (cancelled) | 2026-10-01 22:49:43 | review-20261001#None | duplicate of rate-us-trigger-search (same watch for the Rate Us popup) |
| Leave Golden Fish pending on Home for 10+ min / next day: does the button expire or stay? | 2026-10-01 22:48:10 | 20261001-223249-chrono-2FYKPJ#8 | Golden Fish pending on Home since ~3 min; last frame (dimmed screen) at ~15 min still shows Golden Fish replacing Level 127, i.e. no expiry within ~12 min. Next-day expiry not tested. Thin check (12 min, not 10+ min idle with the screen awake); the next-day check is golden-home-expiry-nextday. |
| Turn Pattern Mode back OFF (left ON by session 20261001-022624) | 2026-10-01 12:21:42 | 20261001-115413-chrono-2FYKPJ#79 | Pattern Mode in level Settings was ON; switched OFF at L96 (tile icons disappear) |
| Check what happens if the Golden Fish win button is skipped/ignored: home shows Golden Fish instead of Level N, does it expire? | 2026-10-01 12:19:42 | 20261001-115413-chrono-2FYKPJ#71 | Ignored golden button at L86 + force restart: Home shows Golden Fish instead of Level 87, persists after restart. Expiry over time -> new task golden-home-expiry. |
| Use a booster down to 0 and record the refill offer (rewarded ad?) | 2026-10-01 12:15:27 | 20261001-115413-chrono-2FYKPJ#57 | Cat booster used 4x to 0; 5th tap -> rewarded ad (2 ads, ~40s) -> Reward granted -> counter 1 |
| Lose all fish and tap Restart on the Out of Fishes popup | 2026-10-01 12:10:17 | 20261001-115413-chrono-2FYKPJ#43 | Restart returns to same level (L90) with a freshly generated board, 3 fish. |
| Open Terms of Service and Privacy Policy from Home settings | 2026-10-01 11:55:43 | 20261001-115413-chrono-2FYKPJ#5 | Terms of Service and Privacy Policy open in Chrome (oakevergames.com/tos.html, /p...; ToS updated Jan 1 2026, Privacy Aug 5 2026). launch returns to game with Settings still open. |
| Test 'Skip to Level N' link on the Out of Fish popup in Golden Fish (ad? cost?) | 2026-10-01 09:49:24 | 20261001-093348-chrono-2FYKPJ#67 | Skip to Level N link on Out of Fish popup (L74 golden, 8x8): one tap lands straight on next level (L75), no ad seen, no cost |
| Test 'Get 1 Fish' rewarded ad button in Golden Fish Out of Fish popup: does the board continue | 2026-10-01 09:43:11 | 20261001-093348-chrono-2FYKPJ#45 | Get 1 Fish rewarded ad (~25s, then launch): board continues with 1 fish and the wrong X mark kept |
| Survey every screen: capture all entry points and map them to features | 2026-10-01 09:38:14 | 20261001-093348-chrono-2FYKPJ#26 | Walked home, profile, streak, settings, leaderboard + info, Golden Fish from home, win overlays. New: Golden Fish button replaces Level N on home while golden board is pending; 'Almost flawless' banner. |
| Win a level with 1 and 2 mistakes deliberately and record the title and score for each (flawless titles seen: Untouchable, Masterclass) | 2026-10-01 08:36:22 | 20261001-082114-chrono-2FYKPJ#53 | 1 mistake: Brilliant (9x9 8640); 2 mistakes: Awesome (10x10 10080); score unaffected by mistakes. Flawless: Immaculate, Exceptional(Hard), Surgical, Perfect, Purr-fect, Expert, Masterclass |
| In a Golden Fish Challenge make a deliberate wrong move: record lose popup and options | 2026-10-01 08:31:11 | 20261001-082114-chrono-2FYKPJ#34 | Wrong cat in golden fish = immediate Out of Fish popup: Remaining: 8, 'Get 1 Fish' (rewarded AD), 'Restart', 'Skip to Level N' link. Challenge board can be 8x8 (L62) |
| Find what triggers the Golden Fish button on win screen (seen after L54 flawless 9x9; not on L45-53 flawless wins): check next flawless wins and log levels | 2026-10-01 08:30:02 | 20261001-082114-chrono-2FYKPJ#31 | Appears every 4 levels: L54, L58, L62; independent of mistakes (L58 had 2 mistakes) |
| Test the 'Skip to Level N' link under Golden Fish button on a future win screen: does it show an ad or cost anything | 2026-10-01 08:26:35 | 20261001-082114-chrono-2FYKPJ#17 | Tapping 'Skip to Level N' (L58 win screen) shows a full-screen interstitial ad (Hollywood Merge), after launch you land on Level 59 for free |
| Determine what decides Exact/Stellar/Unreal win titles | 2026-10-01 06:15:15 | 20261001-060942-chrono-2FYKPJ#28 | Title tier follows mistakes (fish lost): flawless gives a rotating title (Untouchable, Masterclass; seen with Exact/Stellar/Unreal earlier), score same 10080 for 10x10. Exact mistake-to-title mapping still to confirm: added task. |
| Scroll language list, document all languages | 2026-10-01 06:10:48 | 20261001-060942-chrono-2FYKPJ#4 | 9 languages, list ends at Turkish |
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
