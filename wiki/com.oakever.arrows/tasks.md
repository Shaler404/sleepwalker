# Tasks: Amaze GO!

Status: **▶️ active** — ready now: 23

Mode: **goals** — work through the session goals in order; play levels only as far as an unlock or experiment goal needs; register anything new you notice as a feature or a goal, do not pursue it now

Progress reached: **level 11** · last new feature found at: **level 10 hard**

Goals: study 6, unlock 3, experiment 15 · maps: ? — 8 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **arrows-escape** — mastered, solver, levels won 9, typical 2.3 min

Google Play version: **1.32.0** (checked 2026-10-05 00:13:01) · analyzed version: **1.33.0** · FTUE from a fresh install: **never**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Unlock Shark Run: level 70 | unlock | [Shark Run](features/shark-run.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Unlock Daily Challenge: level 20 | unlock | [Daily Challenge](features/daily-challenge.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Unlock Event Countryside Capers: level 16 | unlock | [Event Countryside Capers](features/countryside-capers.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Zen Mode: what does the toggle change in a level? | experiment | [Zen Mode toggle](features/zen-mode.md) | knowledge gap |  |
| Study Zen Mode toggle: open it, walk its screens and tabs, verify its cases | study | [Zen Mode toggle](features/zen-mode.md) | external |  |
| Study Settings: each option once (Sound, Vibration, Music, Feedback, Privacy, Terms links), set back after | study | [Settings](features/settings.md) | knowledge gap |  |
| Look for economy and monetization: lives or energy, coins, boosters or hints, shop, no-ads, ads after levels | experiment |  | knowledge gap |  |
| Run each outcome once under Daily Streak: Out of lives, Restart from Out of Lives popup resets the board immediately, no confirmation, no life cost, Force-stop and relaunch mid-level | experiment | [Daily Streak](features/daily-streak.md) | knowledge gap |  |
| Theme picker: find whether the chosen theme stays after leaving the level and after an app restart | experiment | [Theme picker (palette icon in the level HUD)](features/theme-picker.md) | knowledge gap |  |
| Find whether a free Continue after Out of Lives lowers the win result (stars, title, score, accuracy) against a clean win | experiment | [Level (arrows-escape board)](features/level.md) | knowledge gap |  |
| Find whether the hint bulb appears on Normal levels after Hard level 5 (level 6) and whether a used hint changes the win screen | experiment | [Hint (bulb button in the level HUD)](features/hint.md) | knowledge gap |  |
| Find whether using hints lowers the win result (stars, title, score) against a win without hints | experiment | [Hint (bulb button in the level HUD)](features/hint.md) | knowledge gap |  |
| Find which level numbers are Hard up to level 20 (purple nodes on the level path) and whether the pattern is fixed | experiment | [Hard level (purple, larger zoomable board)](features/hard-level.md) | knowledge gap |  |
| Hard levels: does a tap on a red (already blocked) arrow cost a drop or do nothing? | experiment | [Drops (mistake allowance in the level HUD)](features/drops.md) | knowledge gap | 20261003-233756-chrono-2FYKPJ#20 changed nothing |
| Study Notification permission prompt: open it, walk its screens and tabs, verify its cases | study | Notification permission prompt | external |  |
| Find whether Daily Streak resets every Monday (calendar week) or only on a missed day | experiment | [Daily Streak](features/daily-streak.md) | knowledge gap |  |
| Find whether the in-level grid button and the home Settings Guideline toggle are one setting, and whether it stays on across levels and restarts | experiment | [Guideline toggle](features/guideline.md) | knowledge gap |  |
| Study the Profile popup: rename, avatar and frame tabs, which items are locked and how they unlock | study | Profile (name, avatar, frame) | knowledge gap |  |
| Gold arrows on boards after the league starts: do they add league points when cleared, and how many appear per level | experiment | Gold arrows (league tokens on the board) | knowledge gap |  |
| Study the Bronze League: points per gold arrow, the (i) info, rewards per rank, promotion and demotion | study | [Bronze League](features/bronze-league.md) | knowledge gap |  |
| Study Gold arrows (league tokens on the board): open it, walk its screens and tabs, verify its cases | study | Gold arrows (league tokens on the board) | external |  |
| Find when the Rate Us popup comes back after wins (every N wins, once per day, or never after one dismissal) | experiment | [Rate Us](features/rate-us.md) | knowledge gap |  |
| Find whether win stars drop with the level time: 2 stars on a win with no mistake and no hint | experiment | [Hard level (purple, larger zoomable board)](features/hard-level.md) | knowledge gap |  |

## Waiting

| Task | Not before | Kind | Feature |
|---|---|---|---|
| Open the Bronze League after its first period ends: results screen, rank reward, promotion | 2026-10-06 01:35:50 | check | [Bronze League](features/bronze-league.md) |
| Daily Streak: find what a missed day does to the streak (reset, a save offer and its price) | 2026-10-06 09:00:00 | experiment | [Daily Streak](features/daily-streak.md) |

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

| Task | What to provide | Feature |
|---|---|---|
| Verify the first-time experience from level 1: on a fresh install try to dismiss the cloud-restore popup (back key) and play levels 1-2 with their tutorial | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | [Level (arrows-escape board)](features/level.md) |
| Study consent screen on a fresh install: buttons, links, answers | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | [Consent screen](features/consent.md) |

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Make Hard arrows levels fast: tap every visibly free arrow in each hint frame, one batched command per hint pair; measure on Hard L8 (L5 took 863 s) | 2026-10-05 01:39:28 | 20261005-012010-chrono-2FYKPJ#16 | The arrows-escape solver (no hints) won Hard L8 in 168 s and Hard L10 in 268 s, against 863 s for L5 by hint loop |
| Hard win cards give 2 stars and 'Great Start!' even with no drop lost? | 2026-10-05 01:39:28 | 20261005-012010-chrono-2FYKPJ#16 | Hard L8 (0 mistakes, 3 drops, 01:30) gave 3 stars 'Arrow Pro!' 1700, Hard L10 gave 3 stars 'Untouchable!' [#29]; Hard L5 2 stars came with a ~14 min solve, so stars likely drop with time or hints, not capped on Hard |
| Study the core level: rules, HUD, win screen, every loss kind as an outcome, retry, restart, quit, exit-app (play levels 3-10) | 2026-10-05 01:35:51 | 20261005-012010-chrono-2FYKPJ#35 | All core-level cases closed: rules re-verified on L6-L10 (295 solver taps, 0 mistakes), the only loss kind is out-of-lives (free Continue, no timer), no level elements through L10; gold rank arrows start on L11 with the Bronze League (feature gold-arrows). Win cards: normal (stars, title, Difficulty, Time, Score, Today's Levels, accuracy/mistakes/hints) and Hard (purple, Time/Score/Today's Levels); Rate Us popup after the L6 win; Hard L10 opens with a 'beat 74.59% of players' banner. |
| First look at Bronze League: open it once, record what it is and decide whether it needs a full study | 2026-10-05 01:35:41 | 20261005-012010-chrono-2FYKPJ#35 | Opened from Home card Play: how-to overlay (collect rank arrows = gold arrows on boards, rewards, leaderboard), then the board: 24 h event timer, 50+ players, gifts for top 3, next tier locked. Needs a full study: points per gold arrow, rewards, the period end (24 h follow-up). |
| Unlock Bronze League: level 11 | 2026-10-05 01:33:34 | planner | seen open at level 10 hard |
| Write the arrows-escape solver (read arrows and heads from panned frames, free-ray test, ordered removal) and win Hard level 8 with it using no hints | 2026-10-05 01:27:24 | 20261005-012010-chrono-2FYKPJ#16 | Hard L8 won with the solver, no hints, 0 mistakes, 3 stars, 2.6 min logged (01:30 in-game), 6 solve rounds. The L8 board fit the screen at 35 px pitch (no panning); pitch search lowered to 26 px. |
| Make the arrows-escape solver read normal boards (level 6 on): per-level grid pitch (about 61 px at 1080 on L6), arrow heads at the smaller pitch, mask the bottom-right guideline button; then play L6-L7 with solve --run | 2026-10-05 01:24:15 | 20261005-012010-chrono-2FYKPJ#9 | Fixed: pitch refined to 0.05 px (61.15 on L6, ~45 px on L7), head tip probe moved from 0.24 to 0.15 pitch (the triangle tip is only 0.23 pitch ahead of the node), guideline button masked as a white disc (its nodes unobserved). L6: 28 arrows, 2 rounds, 1.8 min, 3 stars. L7: 54 arrows, 4 rounds, 1.5 min, 3 stars, 0 mistakes. |
| Guideline on: find what it draws on a board (nothing visible on idle level 3; try tapping a blocked/free arrow, larger levels) | 2026-10-05 01:20:42 | 20261005-010045-chrono-2FYKPJ#94 | The in-level grid button (bottom right, from level 6) turns the guideline on: a light tan line along every arrow's exit ray from its head to the screen edge; off again on the second tap (#95). Level 3 showed nothing because the in-level button and lines appear only from level 6 |
| Run each outcome once under Hard level (purple, larger zoomable board): Win screen | 2026-10-04 00:33:35 | planner | every known outcome of the base level was run under Hard level (purple, larger zoomable board) |
| Daily Streak day 2: win one level tomorrow and record the streak screen, the counter and any reward | 2026-10-04 00:33:24 | 20261004-001551-chrono-2FYKPJ#109 | Day 2 (Sun 4 Oct, first win of the day = Hard L5): streak screen before the win screen shows 2, SAT and SUN checked, text 'Well done! Your consistency is impressive.', Continue; no reward shown |
| Does Hint run out (count or ad) after N uses? Used 8 on Hard L5 with no limit seen; check on Normal level and on win screen hints-used counter | 2026-10-04 00:33:24 | 20261004-001551-chrono-2FYKPJ#109 | About 55 hint uses on Hard L5 in one level: no counter, price, ad or popup ever; the bulb does not run out on Hard. Normal levels stay with exp-hint-on-normal |
| Win Hard level 5 with pinch-zoom and record how Hard differs from Normal (board, drops, score, win screen), and which levels are Hard (5, 8, ...) | 2026-10-04 00:30:49 | 20261004-001551-chrono-2FYKPJ#110 | Won L5 with hint+pan (no pinch). Hard: purple label, huge board, 3 drops, Great Start result, 895 score, levels 5 and 8 are Hard. |
| Study Hint (bulb button in the level HUD): open it, walk its screens and tabs, verify its cases | 2026-10-04 00:30:49 | 20261004-001551-chrono-2FYKPJ#110 | Hint bulb: free, unlimited in 40+ uses, no popup; highlights a free arrow green, auto-pans; sometimes off-screen so pan by swipe. |
| Write an arrows solver (read dot grid, head directions, free-ray test) and win Hard level 5 via pan-capture; hint can supply free arrows | 2026-10-04 00:30:48 | 20261004-001551-chrono-2FYKPJ#110 | No pixel solver; hint-loop script (tap bulb, find green pixels, tap them) won Hard L5 in ~13 min (2 steps per arrow). A true solver still not written. |
| Drops: find what a blocked-arrow tap costs and what happens at zero drops | 2026-10-03 23:45:50 | 20261003-233756-chrono-2FYKPJ#4 | Each blocked tap costs one drop; at 0 the Out of Lives popup: Continue Free (+3 lives, keeps board) or Restart; registered as level outcome out-of-lives |
| Hint bulb: tap it once on a Hard level and record what it shows, its count or price, and what it offers at zero | 2026-10-03 23:45:50 | 20261003-233756-chrono-2FYKPJ#10 | Bulb pans the view to one free arrow drawn green; tapping it removes it, no mistake; no counter or price over 8 uses |
| Win Normal levels 6-10 (needs L5 Hard won first) (cancelled) | 2026-10-03 23:45:50 | 20261003-233756-chrono-2FYKPJ#24 | duplicate of study-level (play levels 3-10); progress is gated by study-hard-level / solver-hard-arrows |
| Study Daily Streak screen | 2026-10-03 23:37:18 | 20261003-233532-chrono-2FYKPJ#10 | Popup via home badge: description, Current/Best Record, OK. No rewards/milestones visible at streak 1; next-day increment is in exp-streak-next-day |
| Study Drops (mistake allowance in the level HUD): open it, walk its screens and tabs, verify its cases | 2026-10-03 23:37:18 | 20261003-233532-chrono-2FYKPJ#10 | 3 drops in level HUD, not tappable (no popup, verified). Blocked tap costs 1 drop (earlier session L3/L4, arrow flashes red). Drops follow the theme colour. Loss at 0 drops left to exp-drops. |
| Study the theme picker: tap the palette icon in the level HUD, record every theme, which are locked and their condition, equip one and set it back | 2026-10-03 23:36:35 | 20261003-233532-chrono-2FYKPJ#5 | 3 themes: default cream, Eye Comfort green, Dark; none locked; applies instantly to board/HUD; equipped each, restored default; persists across levels unknown |
| Purple level nodes 5 and 8 on win path: what are they? | 2026-10-03 23:30:27 | 20261003-232357-chrono-2FYKPJ#21 | Purple nodes are Hard levels: level 5 opens labelled 'Hard' with a larger zoomable board and a hint bulb; home Play turns purple 'Hard Level 5'. Recorded as feature hard-level. |
| Guideline: what does the toggle show? (cancelled) | 2026-10-03 23:25:23 | review-20261003 | duplicate of exp-guideline-effect (same question, with a sharper plan after nothing showed on idle level 3 [20261003-232108-chrono-2FYKPJ#13]) |
| Study Save Your Progress (account link; look only, never sign in) | 2026-10-03 23:25:23 | 20261003-232108-chrono-2FYKPJ#3 | duplicate of study-cloud-save, done in this session: Settings > Save Your Progress popup (Facebook/Google sign-in, Delete Account, X); looked only |
| Study Home screen: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:25:18 | 20261003-232357-chrono-2FYKPJ#7 | Home: carousel Bronze L11, Shark Run L70, Daily Challenge L20, Countryside L16; locked tap shows tooltip; Play button; settings gear. |
| Study Rate Us: open it from Settings, record the prompt and what each answer does (never submit a rating) | 2026-10-03 23:25:18 | 20261003-232357-chrono-2FYKPJ#7 | Settings > Rate Us opens popup: 5 empty stars, 'Do you like Amaze GO?', Rate button, X. Closed via X, no rating submitted; per-star behaviour not tested to avoid submission. |
| Study Consent screen: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:23:20 | 20261003-232108-chrono-2FYKPJ#13 | Cannot reopen on progressed phone; fresh-install task added |
| Study Guideline toggle: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:23:20 | 20261003-232108-chrono-2FYKPJ#13 | Toggle in home settings only, persists; no visible effect on idle level 3; experiment added |
| Study Save Your Progress (cloud save): open it, walk its screens and tabs, verify its cases | 2026-10-03 23:23:20 | 20261003-232108-chrono-2FYKPJ#13 | Settings > Save Your Progress opens popup with Facebook/Google sign-in, Delete Account, X; observed only |
| Find why Zen Mode toggle appeared: setting toggle, off by default; effect unknown | 2026-10-03 20:05:16 | planner | the trigger is recorded as a fact: present in Settings on the first visit after a fresh install (progress cloud-restored to level 3) [20261003-200141-chrono-2FYKPJ#5] |
| Find why Guideline toggle appeared: setting toggle, off by default; probably grid guide on board | 2026-10-03 20:05:16 | planner | the trigger is recorded as a fact: present in Settings on the first visit after a fresh install (progress cloud-restored to level 3) [20261003-200141-chrono-2FYKPJ#5] |
| Map the game: play until the main menu and every entry point is visible; list each entry point as open (a study goal), locked with its unlock condition (an unlock goal) or unclear (an experiment) | 2026-10-03 20:03:42 | 20261003-200141-chrono-2FYKPJ#6 | Home: carousel of 4 locked cards (Bronze League 11, Countryside Capers 16, Daily Challenge 20, Shark Run 70), Play Level 3 (cloud restored to L3), settings gear. Fresh install with cloud restore. |
