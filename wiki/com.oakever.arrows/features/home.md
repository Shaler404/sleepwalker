---
game: com.oakever.arrows
title: "Home screen"
type: feature
feature: home
version_seen: 1.33.0
verified_at: 2026-10-03
sources: [20261003-200141-chrono-2FYKPJ, 20261003-232357-chrono-2FYKPJ]
---

# Home screen

The game's main screen. It has a horizontal carousel of feature cards at the top, the title "Amaze GO!"
in the middle, and a Play button with the next level number at the bottom. A gear icon for Settings is
in the top right corner [^s1]. After the first wins, a Daily Streak badge shows next to the gear, and a
path of the next levels shows above Play [^s7].

## Why it appeared

On launch, after the consent screen and the "Progress updated!" cloud-restore popup [^s1].

## Where to find it

<!-- no-entry: Home is the screen the game opens on; there is no control that leads to it -->
It is the screen the game opens on, after the first-launch flow [^s1]. These return to it:

- the Back key or the arrow in Settings [^s3] [^s9];
- the back arrow inside a level [^s7].

## What it looks like

![Home: card carousel (Bronze League Lv.11, Shark Run Lv.70, a third card cut off), settings gear top right, Play Level 3](../img/20261003-home-screen-ee4e6b91.webp) [^s1]
*Home on a fresh install with progress restored to level 3: Bronze League and Shark Run cards, the gear top right, Play / Level 3*

The carousel holds four cards. Each card has a picture and a button "Unlock Lv.N". Two cards and part of a
third fit on the screen, and swiping left shows the rest [^s1] [^s4] [^s2]. The Play button shows the next
level under the word Play: "Level 1" before the restore, "Level 3" after it [^s5] [^s1].

![The carousel at its end: Daily Challenge (Oct 3) and Event Countryside Capers](../img/20261003-countryside-capers-entry-ea4a3ab5.webp) [^s2]
*The carousel scrolled to its end: Daily Challenge with the date Oct 3, then Event Countryside Capers, the last card*

## What you can do

| Tab or button | Where | State in these sessions |
|---|---|---|
| [Settings](settings.md) (the gear) | top right | open |
| [Drop counter and level path](#drop-counter-and-level-path) | left of the gear; above Play | appear after the first wins |
| [Bronze League](bronze-league.md) card | carousel, 1st | locked: Unlock Lv.11 |
| [Shark Run](shark-run.md) card | carousel, 2nd | locked: Unlock Lv.70 |
| [Daily Challenge](daily-challenge.md) card | carousel, 3rd | locked: Unlock Lv.20; shows the date "Oct 3" |
| [Event Countryside Capers](countryside-capers.md) card | carousel, 4th (last) | locked: Unlock Lv.16 |
| [Locked card tooltip](#locked-card-tooltip) | under a tapped locked card | shows the unlock level |
| [Play](#play) | bottom | opens the next [level](level.md) |

### Drop counter and level path

![Home after level 4: drop counter 1 left of the gear, level path 5-9 with purple 5 and 8, purple Hard Level 5 button](../img/20261003-home-tab-drop-counter-and-level-path-ee4c6b91.webp) [^s7]
*Home after two wins: the drop badge "1" left of the gear, the path 5-9 (5 and 8 purple), and the purple Hard / Level 5 button*

After level 4 was won and level 5 was quit, Home had changed in three ways [^s7]:

- a light pill with a blue drop and "1" was left of the gear. This is the [Daily Streak](daily-streak.md)
  count. It was not there before the session's wins [^s6];
- a path of five numbered nodes (5 to 9) was above Play. The next level is ringed, and Hard levels
  (5 and 8) are purple;
- the Play button was purple and read "Hard / Level 5" (see [Hard level](hard-level.md)).

Tapping the badge was not tried.

### Locked card tooltip

![Tapping the locked Daily Challenge card shows the tooltip Unlock Daily Challenge at Level 20](../img/20261003-home-popup-ff1f8f80.webp) [^s8]
*A tap on the locked Daily Challenge card: the tooltip "Unlock Daily Challenge at Level 20"*

A tap on a locked card shows a tooltip under it that names the feature and its unlock level. For Daily
Challenge it reads "Unlock Daily Challenge at Level 20". The card does not open [^s8].

### Play

<!-- no-frame: the button is on the Home frames above; it leads to the level page -->
A wide button at the bottom. It reads "Play" with the next level under it, for example "Level 3" after
the restore [^s1]. It turns purple with "Hard" when the next level is Hard [^s7]. A tap opens the level
[^s9]: see [Level](level.md).

## How it works

Version 1.33.0.

- The cards are not in unlock order: 11, 70, 20, 16 from left to right [^s1] [^s2].
- The Daily Challenge card shows the current date (Oct 3 on the session day) [^s2].
- At level 3 no badge, timer or counter was on the screen [^s1] [^s6].
- After level 4 the streak badge, the level path and the Hard Play button showed [^s7].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared <!-- case:chk-appeared --> | Fresh install: Accept, then Update on the restore popup | ✅ Home opened | [^s1] |
| Where to find it <!-- case:chk-entry --> | Launched the app; left Settings and a level | ✅ The launch screen of the app; the level back arrow and the Settings back arrow return to it | [^s1] [^s7] |
| Its screen <!-- case:chk-screen --> | Looked at Home | ✅ Carousel, title, Play, gear | [^s1] |
| Every entry point on it <!-- case:chk-entries --> | Swiped the carousel to its end, opened the gear, tapped Play | ✅ Four locked cards (Lv.11, 70, 20, 16), Settings, Play | [^s2] [^s9] |
| Badges, timers and counters <!-- case:chk-badges --> | Looked at Home before and after two wins; tapped a locked card | ✅ The drop badge with the Daily Streak count left of the gear (after the first wins). Locked cards show "Unlock Lv.N", and a tap shows "Unlock <mode> at Level N". The Daily Challenge card shows today's date | [^s7] [^s8] [^s2] |
| What changes with progress <!-- case:chk-changes --> | Back on Home after level 4 | ✅ The level path (next five levels, Hard ones purple) above Play, Play turning purple "Hard" before a Hard level, and the streak badge | [^s7] |

## Not verified

- What the drop badge does when tapped
- What changes when a carousel feature unlocks (level 11 and on)

[^s1]: session 20261003-200141-chrono-2FYKPJ, step 2 — [video at 0:39](https://youtu.be/l44HK-PZ5-o?t=39)
[^s2]: session 20261003-200141-chrono-2FYKPJ, step 4 — [video at 1:21](https://youtu.be/l44HK-PZ5-o?t=81)

[^s3]: session 20261003-200141-chrono-2FYKPJ, step 6 — [video at 1:48](https://youtu.be/l44HK-PZ5-o?t=108)
[^s4]: session 20261003-200141-chrono-2FYKPJ, step 3 — [video at 1:11](https://youtu.be/l44HK-PZ5-o?t=71)
[^s5]: session 20261003-200141-chrono-2FYKPJ, step 1 — [video at 0:12](https://youtu.be/l44HK-PZ5-o?t=12)
[^s6]: session 20261003-232357-chrono-2FYKPJ, step 1 — [video at 0:14](https://youtu.be/x9mSZuHgO_4?t=14)
[^s7]: session 20261003-232357-chrono-2FYKPJ, step 21 — [video at 3:56](https://youtu.be/x9mSZuHgO_4?t=236)
[^s8]: session 20261003-232357-chrono-2FYKPJ, step 4 — [video at 0:42](https://youtu.be/x9mSZuHgO_4?t=42)
[^s9]: session 20261003-232357-chrono-2FYKPJ, step 7 — [video at 1:09](https://youtu.be/x9mSZuHgO_4?t=69)
