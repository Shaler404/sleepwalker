# Tasks: Meowdoku: Brain Puzzle Games

Status: **▶️ active** — ready now: 22

Mode: **goals** — work through the session goals in order; play levels only as far as an unlock or experiment goal needs; register anything new you notice as a feature or a goal, do not pursue it now

Progress reached: **level 129** · last new feature found at: **level 129 home**

Goals: study 13, unlock 1, experiment 8 · maps: level 127 home — 6 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **Cat placement on color regions (Queens-like)** — mastered, solver, levels won 3, typical 2.0 min

Google Play version: **1.18.0** (checked 2026-10-03 19:29:54) · analyzed version: **1.19.1** · FTUE from a fresh install: **never**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Study profile: skins, avatars, frames and how locked skins unlock | study | [Profile (name, avatar, frame, skins)](features/profile.md) | knowledge gap |  |
| Study fish event rewards and rank | study | [Fish rank event (New Session)](features/fish-event.md) | knowledge gap |  |
| Study daily streak rewards and break rule | study | [Daily Streak](features/daily-streak.md) | knowledge gap |  |
| Study Daily Challenge incl. trial skin on 3-fish clear | study | [Daily Challenge](features/daily-challenge.md) | knowledge gap |  |
| Save your progress in Settings: what it offers (do not sign in) | experiment | [Settings](features/settings.md) | knowledge gap |  |
| Study Terms consent popup: open it, walk its screens and tabs, verify its cases | study | [Terms consent popup](features/consent.md) | external |  |
| Study Home screen: open it, walk its screens and tabs, verify its cases | study | [Home screen](features/home.md) | external |  |
| Study Settings: open it, walk its screens and tabs, verify its cases | study | [Settings](features/settings.md) | external |  |
| Study Fish leaderboard: open it, walk its screens and tabs, verify its cases | study | [Fish leaderboard](features/fish-leaderboard.md) | external |  |
| Unlock Cat skins (7 locked): unknown: 7 locked silhouettes, tap shows no hint; Daily Challenge says a 3-fish clear unlocks a trial skin | unlock | [Cat skins (7 locked)](features/cat-skins.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Study Mouse booster: open it, walk its screens and tabs, verify its cases | study | [Mouse booster](features/booster-mouse.md) | external |  |
| Find why Banner ad under the level board appeared: shown on every level from some level on; first seen on level 128 (not checked on level 127) | experiment | [Banner ad under the level board](features/ad-banner.md) | knowledge gap |  |
| Find how often the interstitial and banner show: play three levels in a row and mark which level starts show an interstitial and whether the banner is on every level | experiment | [Interstitial ad at level start](features/ad-interstitial.md) | knowledge gap |  |
| Study the Rate Us popup: what X and Rate Us do (Rate Us leads to the store: back at once, no rating) and after which win it comes back | study | [Rate Us popup](features/rate-us.md) | knowledge gap |  |
| Study rewarded videos: every place that offers one (streak restore, booster at 0, others) and what each gives after a full watch | study | [Rewarded video (streak restore, booster refill)](features/ad-rewarded.md) | knowledge gap |  |
| Study Interstitial ad at level start: open it, walk its screens and tabs, verify its cases | study | [Interstitial ad at level start](features/ad-interstitial.md) | external |  |
| Study Banner ad under the level board: open it, walk its screens and tabs, verify its cases | study | [Banner ad under the level board](features/ad-banner.md) | external |  |
| Watch the Get 3 Fishes ad on Out of Fishes once: confirmed when the level continues with the placed cats kept and 3 fish back | experiment | [Rewarded video (streak restore, booster refill)](features/ad-rewarded.md) | knowledge gap |  |
| Use the hint booster down to 0 and see what refills it: confirmed when the badge at 0 and its refill (video, timer, level win) are marked | experiment | [Hint booster (bulb)](features/booster-hint.md) | knowledge gap |  |
| Toggle Pattern Mode in the in-level settings once: confirmed when the board with Pattern Mode on is marked and the toggle is set back | experiment | [Main level (cat placement board)](features/level.md) | knowledge gap |  |
| What decides the score a placed cat gives (+576 on L128, +672 on L130)? | experiment | [Main level (cat placement board)](features/level.md) | knowledge gap |  |
| Daily Streak interrupted: try Restore (video) once and record the day-7 gift | experiment | [Daily Streak](features/daily-streak.md) | knowledge gap |  |

## Waiting

| Task | Not before | Kind | Feature |
|---|---|---|---|
| Open the fish leaderboard after its 24h timer ends (started 2026-10-03 ~20:05): mark the results screen, the rank and the reward paid, and whether a new period starts | 2026-10-04 20:10:31 | check | [Fish leaderboard](features/fish-leaderboard.md) |

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

| Task | What to provide | Feature |
|---|---|---|
| Play the first-time experience on a fresh install (tutorial, first levels, first popups); the current install keeps progress from earlier sessions (level 127 after the update to 1.19.1) | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone |  |

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Run each outcome once under Daily Streak: Android Back on Home opens Quit popup; X cancels | 2026-10-03 20:38:09 | planner | every known outcome of the base level was run under Daily Streak |
| Run each outcome once under Fish rank event (New Session): Android Back on Home opens Quit popup; X cancels | 2026-10-03 20:38:07 | planner | every known outcome of the base level was run under Fish rank event (New Session) |
| Find whether a main level can be lost: place wrong cats until all 3 fish are grey and one more; confirmed when a fail screen (or the absence of one at 0 fish) is marked | 2026-10-03 20:37:54 | 20261003-202631-chrono-2FYKPJ#17 | L130: wrong cats grey one fish each; the third wrong cat ends the level with an Out of Fishes screen (Remaining 10, Get 3 Fishes AD, Restart) |
| Watch the rewarded video on the cat booster at 0 once: how many cats it gives, and whether the badge returns to a count | 2026-10-03 20:37:54 | 20261003-202631-chrono-2FYKPJ#13 | Cat booster at 0 (green video badge) started a rewarded playable ad (Gossip Harbor); after leaving it via launch the badge showed 1 (shot 27), the next tap placed a correct cat and the badge went back to the video icon |
| Study the main level: play levels 127+ with the solver, mark the win screen and its rewards (fish, score), restart, quit and exit-app; find whether and how a level can be lost | 2026-10-03 20:34:31 | 20261003-202631-chrono-2FYKPJ#23 | L129 won via solve --run (3 fish Immaculate), win flow marked, loss = Out of Fishes after 3 wrong cats, restart same board, quit via back arrow, exit via Back on Home |
| Study Cat booster: open it, walk its screens and tabs, verify its cases | 2026-10-03 20:34:30 | 20261003-202631-chrono-2FYKPJ#23 | cat booster: instant correct cat, ad refill at 0 |
| Study Hint booster (bulb): open it, walk its screens and tabs, verify its cases | 2026-10-03 20:34:30 | 20261003-202631-chrono-2FYKPJ#23 | hint: explained cell + Apply places cat |
| Find what makes the 3 fish on the level HUD drop (time, wrong cats, boosters): play one level fast and clean, one with a deliberate wrong placement; confirmed when the fish count at the win differs and the leaderboard fish rise by it | 2026-10-03 20:25:42 | 20261003-201915-chrono-2FYKPJ#18 | L127 clean: 3 fish, Perfect screen, leaderboard fish 3 (rank 21). L128 one wrong cat (orange X, fish 3->2, other boosters did not cost fish): 2 fish, Brilliant, Beat 91.3%, leaderboard 3->5 (+2). Time not tested separately but both fast. |
| Study the three level boosters (cat, hint, mouse): use each once on a level, mark the effect, then note the balance and where more come from | 2026-10-03 20:25:42 | 20261003-201915-chrono-2FYKPJ#18 | Start: cat 1, hint 4, mouse 1. Cat: places one correct cat (+576 score on L128; a 109 on an earlier frame was the counter mid-animation), count to 0 then a video icon. Hint: two kinds (single-cell Apply places a cat; exclusion Apply makes the crosses solid), 4->3. Mouse: adds three crosses, 1->0, video icon. More come via rewarded video (icon at 0). |
| Look for the shop, offers, no-ads, rewarded videos and interstitials: none seen on Home; check after level wins and at zero boosters | 2026-10-03 20:25:42 | 20261003-201915-chrono-2FYKPJ#18 | No shop/offers/no-ads seen on Home or after wins. Ads: banner at level bottom, interstitial (video/playable, 9s countdown, X) on level start, rewarded video: Restore daily streak popup after win leaderboard (Give up declined), booster badge turns into green video icon at 0. Rate Us popup after L127 win. Nothing bought. |
| Map the game: play until the main menu and every entry point is visible; list each entry point as open (a study goal), locked with its unlock condition (an unlock goal) or unclear (an experiment) | 2026-10-03 20:08:29 | 20261003-200440-chrono-2FYKPJ#20 | Home mapped; install already at level 127 (progress present on first launch). No locked entries seen; skins 7 locked silhouettes with unknown unlock; Save your progress in settings left unexplored |
