# Features: Amaze GO!

Version: **1.33.0** · features: **18**, documented: **2** · cases closed: **89 / 159** · all sections found: **no**

Generated from [`research.yaml`](research.yaml) by `sw.py render`. Tasks: [tasks.md](tasks.md).

| Feature | Found at | Status | Cases | Open tasks | Version |
|---|---|---|---|---|---|
| [Consent screen](features/consent.md) |  | 🔎 seen | 1 / 6 | Study consent screen on a fresh install: buttons, links, answers |  |
| [Home screen](features/home.md) |  | 🛠 in progress | 6 / 6 |  |  |
| [Bronze League](features/bronze-league.md) |  | 🔎 seen | 1 / 8 | Unlock Bronze League: level 11 |  |
| [Shark Run](features/shark-run.md) |  | 🔎 seen | 1 / 14 | Unlock Shark Run: level 70 |  |
| [Daily Challenge](features/daily-challenge.md) |  | 🛠 in progress | 2 / 9 | Unlock Daily Challenge: level 20 |  |
| [Event Countryside Capers](features/countryside-capers.md) |  | 🔎 seen | 1 / 14 | Unlock Event Countryside Capers: level 16 |  |
| [Settings](features/settings.md) |  | 🛠 in progress | 4 / 7 | Study Settings: each option once (Sound, Vibration, Music, Feedback, Privacy, Terms links), set back after |  |
| [Zen Mode toggle](features/zen-mode.md) |  | 🔎 seen | 1 / 8 | Zen Mode: what does the toggle change in a level?; Study Zen Mode toggle: open it, walk its screens and tabs, verify its cases |  |
| [Guideline toggle](features/guideline.md) |  | 🛠 in progress | 7 / 8 | Guideline on: find what it draws on a board (nothing visible on idle level 3; try tapping a blocked/free arrow, larger levels) | 1.33.0 |
| [Level (arrows-escape board)](features/level.md) |  | 🛠 in progress | 10 / 13 | Study the core level: rules, HUD, win screen, every loss kind as an outcome, retry, restart, quit, exit-app (play levels 3-10); Verify the first-time experience from level 1: on a fresh install try to dismiss the cloud-restore popup (back key) and play levels 1-2 with their tutorial; Find whether a free Continue after Out of Lives lowers the win result (stars, title, score, accuracy) against a clean win |  |
| [Save Your Progress (cloud save)](features/cloud-save.md) |  | ✅ documented | 7 / 7 |  | 1.33.0 |
| [Rate Us](features/rate-us.md) |  | 🛠 in progress | 6 / 6 |  |  |
| [Theme picker (palette icon in the level HUD)](features/theme-picker.md) |  | ✅ documented | 6 / 6 | Theme picker: find whether the chosen theme stays after leaving the level and after an app restart | 1.33.0 |
| [Drops (mistake allowance in the level HUD)](features/drops.md) |  | 🛠 in progress | 7 / 8 | Hard levels: does a tap on a red (already blocked) arrow cost a drop or do nothing? | 1.33.0 |
| [Daily Streak](features/daily-streak.md) | level 4 | 🛠 in progress | 8 / 14 | Run each outcome once under Daily Streak: Out of lives, Restart from Out of Lives popup resets the board immediately, no confirmation, no life cost, Force-stop and relaunch mid-level; Daily Streak: find what a missed day does to the streak (reset, a save offer and its price) | 1.33.0 |
| [Hard level (purple, larger zoomable board)](features/hard-level.md) | level 4 | 🛠 in progress | 13 / 14 | Write the arrows-escape solver (read arrows and heads from panned frames, free-ray test, ordered removal) and win Hard level 8 with it using no hints; Find which level numbers are Hard up to level 20 (purple nodes on the level path) and whether the pattern is fixed; Make Hard arrows levels fast: tap every visibly free arrow in each hint frame, one batched command per hint pair; measure on Hard L8 (L5 took 863 s) |  |
| [Hint (bulb button in the level HUD)](features/hint.md) | level 5 | 🛠 in progress | 7 / 10 | Find whether the hint bulb appears on Normal levels after Hard level 5 (level 6) and whether a used hint changes the win screen; Find whether using hints lowers the win result (stars, title, score) against a win without hints |  |
| Notification permission prompt | level 3 | 🔎 seen | 1 / 1 |  |  |
