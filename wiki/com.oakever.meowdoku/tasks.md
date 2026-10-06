# Tasks: Meowdoku: Brain Puzzle Games

Status: **▶️ active** — ready now: 12

Mode: **cases** — all features are found: study goals and checks only; do not advance

Progress reached: **level 139** · last new feature found at: **level 134**

Goals: unlock 1, experiment 12 · maps: level 127 home — 6 new · search for features closed: Golden Fish (the last new entry) was played through at L138: its board, popup and win lead only back to the next main level, no new entry point; Home, Settings, Profile, leaderboard and daily walked earlier; the one lock (cat skins) has its unlock goal; no shop/IAP/no-ads/offer seen across L127-139; onboarding left to ftue

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **Cat placement on color regions (Queens-like)** — mastered, solver, levels won 16, typical 1.0 min

Google Play version: **1.18.0** (checked 2026-10-05 22:05:43) · analyzed version: **1.19.1** · FTUE from a fresh install: **never**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Unlock Cat skins (7 locked): unknown: 7 locked silhouettes, tap shows no hint; Daily Challenge says a 3-fish clear unlocks a trial skin | unlock | [Cat skins (7 locked)](features/cat-skins.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Use the hint booster down to 0 and see what refills it: confirmed when the badge at 0 and its refill (video, timer, level win) are marked | experiment | [Hint booster (bulb)](features/booster-hint.md) | knowledge gap |  |
| Toggle Pattern Mode in the in-level settings once: confirmed when the board with Pattern Mode on is marked and the toggle is set back | experiment | [Main level (cat placement board)](features/level.md) | knowledge gap |  |
| What decides the score a placed cat gives (+576 on L128, +672 on L130)? | experiment | [Main level (cat placement board)](features/level.md) | knowledge gap |  |
| Daily Streak interrupted: try Restore (video) once and record the day-7 gift | experiment | [Daily Streak](features/daily-streak.md) | knowledge gap |  |
| Find what the Daily Streak break popup counts: confirmed when the number in 'N days interrupted' is matched to the current streak, the best streak or the days lost | experiment | [Daily Streak](features/daily-streak.md) | knowledge gap |  |
| Is the trial skin granted only for a 3-fish daily clear, and what happens when its 24h trial ends | experiment | [Daily Challenge](features/daily-challenge.md) | knowledge gap |  |
| What the Daily Streak day-7 gift gives | experiment | [Daily Streak](features/daily-streak.md) | knowledge gap |  |
| Hearts on leaderboard rows: watch after a win what gives hearts and if tapping does anything | experiment | [Fish leaderboard](features/fish-leaderboard.md) | knowledge gap |  |
| Leaderboard frames 5/15/30/50: verify they are given for top-N placement at period end | experiment | [Profile (name, avatar, frame, skins)](features/profile.md) | knowledge gap |  |
| Read the own condition of each Leaderboard frame (5, 15, 30, 50): done when each frame's tooltip is marked | experiment | [Profile (name, avatar, frame, skins)](features/profile.md) | knowledge gap |  |
| Run each outcome once under Golden Fish bonus board: Out of fishes, Settings gear > Restart restarts the SAME board (same layout, cat bar order shuffled), cats cleared, score 0, hint count kept, no confirm, Back arrow in level goes straight Home, no confirm, may trigger interstitial, Android Back on Home opens Quit popup; X cancels | experiment | Golden Fish bonus board | knowledge gap |  |

## Waiting

| Task | Not before | Kind | Feature |
|---|---|---|---|
| Find when the Daily Streak day rolls over: done when the yarn counter is marked before and after the first win of a new calendar day and the jump (or none) is explained | 2026-10-06 08:00:00 | experiment | [Daily Streak](features/daily-streak.md) |
| Watch a fish leaderboard period end with the game open: period ends about 01:09 phone time on 2026-10-07 (timer read 23:55:49 at 01:13 on 10-06); open the leaderboard at 01:05 and stay past 01:09; mark results screen, final rank, reward | 2026-10-07 01:03:00 | check | [Fish leaderboard](features/fish-leaderboard.md) |
| Rate Us: wins of L133 and L134 did not bring it back; keep playing and note after which win it returns, then tap X and Rate Us (back at once) | 2026-10-07 01:16:44 | check | [Rate Us popup](features/rate-us.md) |
| Skip the Daily Challenge on 2026-10-07 entirely, open it on 2026-10-08: done when the Home button and the daily screen after a missed day are marked (what is lost or reset, any streak or calendar effect) | 2026-10-08 08:00:00 | check | [Daily Challenge](features/daily-challenge.md) |

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

| Task | What to provide | Feature |
|---|---|---|
| Play the first-time experience on a fresh install (tutorial, first levels, first popups); the current install keeps progress from earlier sessions (level 127 after the update to 1.19.1) | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone |  |

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Open the Daily Challenge on 2026-10-06: done when the renewed Home button (timer, check gone, skin) and the new dated board are marked; then skip one day and mark what a missed day shows | 2026-10-06 02:27:45 | 20261006-021434-chrono-2FYKPJ#26 | 10/06 renewed Home button (frame 45) and new dated board (frame 46) seen at ~02:22; missed-day part moved to daily-missed-day |
| Watch the Daily Challenge Retry ad once after a clear: done when what Retry gives (the same board or a new one, timer reset, best time kept or replaced, another trial skin or none) is marked | 2026-10-06 02:24:34 | 20261006-021434-chrono-2FYKPJ#33 | Retry (AD): ad ended with Reward granted + X (~8 s); gives the SAME board with cats cleared, timer reset to 00:00, 3 fish. Retry clear with 2 fish: 00:38 beat 98.7% (first 00:22 beat 99.0%), no trial skin popup (skin popup came only on 3-fish first clear, Equip/Later). Retry offered again. Best-time stored not verified. |
| Find how often the interstitial and banner show: play three levels in a row and mark which level starts show an interstitial and whether the banner is on every level | 2026-10-06 02:20:59 | 20261006-021434-chrono-2FYKPJ#22 | L135 no interstitial, L136 yes, L137 no, L138 yes; banner on every level incl golden. Rule: interstitial at every other level start (alternating) |
| Study the Golden Fish bonus board: on the next 4th-level win (L138) tap Golden Fish instead of Skip; done when the entry, the board (one fish, no Level in the header), any ad before it, its win screen and its reward are marked | 2026-10-06 02:20:58 | 20261006-021434-chrono-2FYKPJ#22 | L138 golden: entry, board, popup, result, leaderboard marked; no ad before; 1 golden=5 fish |
| Save your progress in Settings: what it offers (do not sign in) | 2026-10-06 01:19:00 | 20261006-010939-chrono-2FYKPJ#12 | Home gear > Save your progress opens a popup: Sign in with Facebook, Sign in with Google, Delete Account link; nothing tapped, X closes (shot 16) |
| Open Terms of Service and Privacy Policy from Settings: done when each link's destination (browser, in-app page) and the way back are marked | 2026-10-06 01:18:55 | 20261006-010939-chrono-2FYKPJ#17 | ToS (step 17) and Privacy Policy (step 19) open Chrome pages on oakevergames.com; launch brings the game back with Settings open |
| Study the Rate Us popup: what X and Rate Us do (Rate Us leads to the store: back at once, no rating) and after which win it comes back (cancelled) | 2026-10-06 01:16:52 | 20261006-010939-chrono-2FYKPJ#33 | popup did not return after L133/L134; replaced by followup study-rate-us-2 |
| Watch a fish leaderboard period end with the game open: mark the results screen, the final rank and the reward paid (current period ends about 00:40 local on 2026-10-06) (cancelled) | 2026-10-06 01:16:51 | 20261006-010939-chrono-2FYKPJ#33 | period had already ended before the session opened (New Session popup on launch); new followup fish-event-end-open-2 set for 2026-10-07 |
| Study Settings: open it, walk its screens and tabs, verify its cases | 2026-10-06 01:13:46 | 20261006-010939-chrono-2FYKPJ#22 | Walked Home settings (toggles, Save progress, Language 10 langs, Feedback=Helpshift, ToS/Privacy to Chrome) and in-level variant (Pattern Mode, Restart not tapped) |
| Find what the red dot on the Home avatar points to after the trial skin was equipped: done when Profile > Skins is marked with the trial skin (owned/trial state, timer) and the dot's state after opening it | 2026-10-05 22:43:53 | 20261005-223641-chrono-2FYKPJ#13 | The Home avatar dot led to the Profile Skins tab dot (shot 15); opening Skins cleared both (shot 16). But the trial skin (red bow cat, worn on the L133 board, shot 9) is not in the Skins grid and no trial timer is shown, so the dot leads to the tab, not to a trial skin entry |
| Study profile: skins, avatars, frames and how locked skins unlock | 2026-10-05 22:41:05 | 20261005-223641-chrono-2FYKPJ#21 | Walked Avatar, Skins, Frame tabs; locked frames show rank-1 tooltip; skins give no condition. exp-frame-rank-tiers set |
| Study Home screen: open it, walk its screens and tabs, verify its cases | 2026-10-05 22:39:08 | 20261005-223641-chrono-2FYKPJ#11 | Home walked: entries, badges, yarn counter opens Daily Streak, gear opens Settings, podium opens leaderboard |
| Study Fish leaderboard: open it, walk its screens and tabs, verify its cases | 2026-10-05 22:38:32 | 20261005-223641-chrono-2FYKPJ#7 | Walked leaderboard: podium, list scroll, info sheet, row tap (nothing), Go to Collect (opens L133 board), period timer. Hearts and period-end results left open as tasks (exp-heart-cheers, fish-event-end-open) |
| Study fish event rewards and rank | 2026-10-05 14:43:08 | 20261005-143752-chrono-2FYKPJ#20 | leaderboard, +3 fish per clean win, top-3 gift boxes mapped; end results await fish-event-end-open |
| Study daily streak rewards and break rule | 2026-10-05 14:43:07 | 20261005-143752-chrono-2FYKPJ#20 | screen, entry, week row mapped; gift contents and count-shown still open (experiments) |
| Study Daily Challenge incl. trial skin on 3-fish clear | 2026-10-05 14:43:06 | 20261005-143752-chrono-2FYKPJ#20 | entry, board, win with trial skin, cleared state mapped; loss, next-day renewal, missed day open |
| Watch the Get 3 Fishes ad on Out of Fishes once: confirmed when the level continues with the placed cats kept and 3 fish back | 2026-10-05 12:43:00 | 20261005-123456-chrono-2FYKPJ#11 | L132: 3 wrong cats -> Out of Fishes (shot 22); Get 3 Fishes ad ~40 s, 'Reward granted' + X top-left; back on the same board with the 3 wrong-cat X marks kept and 3 fish (shot 26). No correct cat had been placed, so keeping placed cats is inferred from the board being kept, not seen |
| Study Terms consent popup: open it, walk its screens and tabs, verify its cases | 2026-10-05 12:40:49 | 20261005-123456-chrono-2FYKPJ#14 | Popup is first-launch only (fresh install); on this progressed phone only the Settings links remain; marked, links not opened |
| Study rewarded videos: every place that offers one (streak restore, booster at 0, others) and what each gives after a full watch | 2026-10-05 12:40:19 | 20261005-123456-chrono-2FYKPJ#11 | Watched in full: mouse booster at 0 (+1 charge) and Out of Fishes Get 3 Fishes (+3 fish, board kept, Reward granted + X). Streak Restore not reachable today (exp-streak-restore covers) |
| Study Mouse booster: open it, walk its screens and tabs, verify its cases | 2026-10-05 12:37:24 | 20261005-123456-chrono-2FYKPJ#4 | Mouse at 0: tap -> rewarded video, +1 charge, use puts mouse and X on a cell, back to video badge |
| Find why Banner ad under the level board appeared: shown on every level from some level on; first seen on level 128 (not checked on level 127) | 2026-10-05 00:45:58 | planner | the trigger is recorded as a fact: on the first level board played on this install (L127, Gossip Harbor banner under the boosters); on every level board since, never on Home or popups [20261003-201915-chrono-2FYKPJ#2] |
| Study Interstitial ad at level start: open it, walk its screens and tabs, verify its cases | 2026-10-05 00:44:08 | 20261005-003925-chrono-2FYKPJ#14 | Video then end card after win -> next level; none on reopening same level; close via launch |
| Study Banner ad under the level board: open it, walk its screens and tabs, verify its cases | 2026-10-05 00:44:07 | 20261005-003925-chrono-2FYKPJ#14 | Banner Royal Match under boosters on level board, persistent, absent elsewhere |
| Open the fish leaderboard after its 24h timer ends (started 2026-10-03 ~20:05): mark the results screen, the rank and the reward paid, and whether a new period starts | 2026-10-05 00:40:32 | 20261005-003925-chrono-2FYKPJ#3 | Checked 10-05: period ended unseen; New Session popup, new 24h period started, leaderboard reset, own row 0 fish unranked. No results screen/rank/reward seen (game was closed at the end). Follow-up: keep game open at an end to see results. |
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
