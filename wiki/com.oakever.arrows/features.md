# Features: Amaze GO!

Version: **1.33.0** · features: **25**, documented: **8** · cases closed: **186 / 250** · all sections found: **no**

Generated from [`research.yaml`](research.yaml) by `sw.py render`. Tasks: [tasks.md](tasks.md).

| Feature | Found at | Status | Cases | Open tasks | Version |
|---|---|---|---|---|---|
| [Consent screen](features/consent.md) |  | 🔎 seen | 1 / 6 | Study consent screen on a fresh install: buttons, links, answers |  |
| [Home screen](features/home.md) |  | 🛠 in progress | 6 / 6 |  |  |
| [Bronze League](features/bronze-league.md) |  | 🛠 in progress | 9 / 10 | Find whether gold arrows cleared before a quit or an out-of-lives give league points (points credited only on the win?) |  |
| [Shark Run](features/shark-run.md) |  | 🔎 seen | 1 / 15 | Unlock Shark Run: level 70 |  |
| [Daily Challenge](features/daily-challenge.md) |  | 🛠 in progress | 2 / 9 | Unlock Daily Challenge: level 20 |  |
| [Event Countryside Capers](features/countryside-capers.md) |  | 🛠 in progress | 8 / 16 | Run each outcome once under Event Countryside Capers: Out of lives, Restart from Out of Lives popup resets the board immediately, no confirmation, no life cost, Force-stop and relaunch mid-level, Restart from the in-level gear popup (Restart board); Countryside Caper: is there any reward or end? Hypothesis: a reward appears only when the whole path (~28 levels) is cleared, and the event has no timer; Adapt the arrows solver to the Countryside Caper worm boards (beads, eyed heads, tapered tails; L2 is ~28x28 and zooms out to fit after a resume) |  |
| [Settings](features/settings.md) |  | ✅ documented | 7 / 7 |  | 1.33.0 |
| [Zen Mode toggle](features/zen-mode.md) |  | ✅ documented | 11 / 11 | What does Zen Mode change? Compare timer/score/drop behaviour with zen on vs off on a Hard level | 1.33.0 |
| [Guideline toggle](features/guideline.md) |  | 🛠 in progress | 9 / 9 |  | 1.33.0 |
| [Level (arrows-escape board)](features/level.md) |  | 🛠 in progress | 17 / 17 | Verify the first-time experience from level 1: on a fresh install try to dismiss the cloud-restore popup (back key) and play levels 1-2 with their tutorial; Why was the L17 win of 20261005-233140 not saved? Hypothesis: the session ended on the win card or its interstitial before the game wrote progress |  |
| [Save Your Progress (cloud save)](features/cloud-save.md) |  | ✅ documented | 7 / 7 |  | 1.33.0 |
| [Rate Us](features/rate-us.md) |  | 🛠 in progress | 7 / 7 | Find when the Rate Us popup comes back after wins (every N wins, once per day, or never after one dismissal) |  |
| [Theme picker (palette icon in the level HUD)](features/theme-picker.md) |  | ✅ documented | 6 / 6 | Theme picker: find whether the chosen theme stays after leaving the level and after an app restart | 1.33.0 |
| [Drops (mistake allowance in the level HUD)](features/drops.md) |  | 🛠 in progress | 7 / 8 | Hard levels: does a tap on a red (already blocked) arrow cost a drop or do nothing?; Find when the Out of Lives Continue is free vs needs an ad | 1.33.0 |
| [Daily Streak](features/daily-streak.md) | level 4 | 🛠 in progress | 10 / 17 | Run each outcome once under Daily Streak: Out of lives, Restart from Out of Lives popup resets the board immediately, no confirmation, no life cost, Force-stop and relaunch mid-level, Restart from the in-level gear popup (Restart board); Daily Streak: find what a missed day does to the streak (reset, a save offer and its price); Find whether Daily Streak resets every Monday (calendar week) or only on a missed day | 1.33.0 |
| [Hard level (purple, larger zoomable board)](features/hard-level.md) | level 4 | 🛠 in progress | 18 / 18 | Find whether win stars drop with the level time: 2 stars on a win with no mistake and no hint |  |
| [Hint (bulb button in the level HUD)](features/hint.md) | level 5 | 🛠 in progress | 9 / 12 | Find whether the hint bulb appears on Normal levels after Hard level 5 (level 6) and whether a used hint changes the win screen; Find whether using hints lowers the win result (stars, title, score) against a win without hints |  |
| Notification permission prompt | level 3 | 🛠 in progress | 8 / 8 | Re-mark the notification prompt frame on a fresh install (the permission dialog cannot be re-triggered on a progressed phone); Find when the in-game Notifications popup comes back (every launch, daily, after N launches) and what its X does |  |
| Profile (name, avatar, frame) | level 10 hard | ✅ documented | 6 / 6 |  | 1.33.0 |
| Gold arrows (league tokens on the board) | level 10 hard | 🛠 in progress | 8 / 8 |  |  |
| Red level node (level 20) | level 15 hard retry | 🔎 seen | 0 / 15 | Find why Red level node (level 20) appeared: level 20 node is red on the path after L15 win: probably a harder tier than purple Hard; Run each outcome once under Red level node (level 20): Back arrow top left leaves the level for home at once, no confirmation; drops were full, no cost seen; Play still shows the same level, Win screen, Out of lives, Restart from Out of Lives popup resets the board immediately, no confirmation, no life cost, Force-stop and relaunch mid-level, Restart from the in-level gear popup (Restart board); Study Red level node (level 20): open it, walk its screens and tabs, verify its cases |  |
| Interstitial ad (after a gear-popup restart or a win) | level 15 hard retry | ✅ documented | 9 / 9 | Interstitials skip a win soon after a rewarded ad and start at about L15; Look for a Remove Ads offer, shop or VIP now that interstitials run (from L15) | 1.33.0 |
| Rewarded ad for Continue (Out of Lives) | level 15 hard retry | ✅ documented | 8 / 8 |  | 1.33.0 |
| Rewarded ad on the hint bulb (AD badge) | level 15 hard retry | ✅ documented | 7 / 7 |  | 1.33.0 |
| Silver League | level 17 continue-ad test | 🛠 in progress | 5 / 8 | Finish a league period in the top 3 to see the gift reward; Open the Silver League after its first period ends: end card, rank, promotion or demotion, any reward; and the points a gold arrow gives in Silver; Study Silver League: open it, walk its screens and tabs, verify its cases |  |
