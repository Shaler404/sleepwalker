---
game: com.oakever.meowdoku
title: "Home screen"
type: feature
feature: home
version_seen: 1.19.1
verified_at: 2026-10-03
sources: [20261003-200440-chrono-2FYKPJ]
---

# Home screen

The game's hub: one static screen with the Meowdoku logo, the button to the next main level, the Daily
Challenge button and five other entry points (profile, daily streak, settings, the event leaderboard).
There is no level map [^s1].

## Why it appeared

After consent on first launch [^s1]. On the first launch it opened right after the consent popup and the
system notification request, with the event popup "New Session" on top of it [^s3].
The install already showed Level 127 on its first launch: no tutorial was seen [^s3].

## Where to find it

The game opens on Home after loading. From a level, the back arrow top left returns to it without a
confirmation (Level 127, no move made) [^s1].

![Level screen: the back arrow top left returns to Home](../img/20261003-home-entry-fa0194d4.webp) [^s2]
*Level screen: the back arrow top left returns to Home*

## What it looks like

![Home: avatar top-left, yarn 0, settings (red dot), event podium with timer, Level 127, Daily Challenge](../img/20261003-home-screen-ad85780f.webp) [^s1]
*Home: the avatar top left, the yarn counter top centre, the gear top right, the podium with its timer on the left, Level 127 and Daily Challenge at the bottom*

## What you can do

| Tab or button | Where | What it opens |
|---|---|---|
| [Avatar](#avatar) | top left | [Profile](profile.md) |
| [Yarn counter](#yarn-counter) | top centre, shows 0 | [Daily Streak](daily-streak.md) |
| [Gear](#gear) | top right, red dot | [Settings](settings.md) |
| [Podium with timer](#podium-with-timer) | left edge, 23:59:28 | [Fish leaderboard](fish-leaderboard.md) of the [Fish rank event](fish-event.md) |
| [Level 127](#level-127) | orange button | the next [main level](level.md) |
| [Daily Challenge](#daily-challenge) | blue button under Level, countdown 03:53:49 | [Daily Challenge](daily-challenge.md) |

### Avatar

![Profile, opened from the avatar (the name field is blacked out)](../img/20261003-profile-screen-84977b68.webp) [^s4]
*Profile, opened from the avatar (the name field is blacked out)*

The player's selected avatar (a corgi) in a red frame; it opens the Profile popup [^s4].

### Yarn counter

![Daily Streak, opened from the yarn counter](../img/20261003-daily-streak-screen-f221995a.webp) [^s5]
*Daily Streak, opened from the yarn counter*

A ball of yarn with a number (0); it opens the Daily Streak screen [^s5].

### Gear

![Settings, opened from the gear](../img/20261003-settings-screen-90663f85.webp) [^s6]
*Settings, opened from the gear*

The gear carries a red dot; it opens the Settings popup, where the music toggle carries the same red dot
[^s6]. Inferred: the dot points at the music toggle being off.

### Podium with timer

![The event leaderboard, opened from the podium (player names blacked out)](../img/20261003-fish-leaderboard-screen-be476195.webp) [^s7]
*The event leaderboard, opened from the podium (player names blacked out)*

A 2-1-3 podium with a countdown under it (23:59:28 at the time of the frame); it opens the event leaderboard
[^s7].

### Level 127

![Level 127, the next main level](../img/20261003-level-screen-fa0194d4.webp) [^s2]
*Level 127, the next main level*

The orange button names the next main level by number and opens it [^s2].

### Daily Challenge

![The Daily Challenge board of 10/03](../img/20261003-daily-challenge-screen-ebd19564.webp) [^s8]
*The Daily Challenge board of 10/03*

The blue button with a cat icon and a countdown (03:53:49 at 20:06 local time) opens today's challenge
board [^s8]. Under it, a line with four avatars reads "4.002M players joined
today" [^s1].

## How it works

- Every entry point on Home was open on this account; no locked button was seen [^s1].
- The two countdowns run independently: the event timer showed about 24 h left, the Daily Challenge timer
  about 3 h 54 min [^s1]. Inferred: the Daily Challenge countdown ends at local midnight (20:06 + 3:53:49).

Version 1.19.1.

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Home: avatar top-left, yarn streak counter top-center, settings gear with red dot top-right, event podium with 24h timer on the left, Level 127 button, Daily Challenge button with reset timer, players-joined-today counter <!-- case:chk-screen --> | Frame marked after the first launch | ✅ | [^s1] |
| Why it appeared: the trigger that brought it up (the first launch, a level won, a threshold, a timer, a loss): a fact with its frame, or a hypothesis to test <!-- case:chk-appeared --> | Opened after the consent popup on the first launch | ✅ | [^s1] |
| Where to find it: the screen and the button that open it (mark --as entry --at X,Y) <!-- case:chk-entry --> | The back arrow of Level 127 returned to Home; frame marked | not verified | [^s2] |
| Every entry point on it: open (a feature), locked (feature --locked with its condition) or unclear (an experiment) <!-- case:chk-entries --> | All six controls opened; none locked | not verified | [^s1] |
| Badges, timers and counters on it and what each points to <!-- case:chk-badges --> | Red dot on the gear, event timer, Daily Challenge timer, yarn counter 0, players-joined counter seen | not verified | [^s1] |
| What changes on it with progress (new buttons, a moving map, a theme) <!-- case:chk-changes --> | Only one state seen (Level 127) | not verified |  |

## Not verified

- Where to find it: the back arrow from a level was seen; other ways back (from Daily Challenge, from Daily Streak) are described on their pages <!-- case:chk-entry -->
- Every entry point: all six opened; whether any entry is added later is unknown <!-- case:chk-entries -->
- Badges: what clears the red dot on the gear, and what the players-joined counter does when tapped <!-- case:chk-badges -->
- What changes on Home with progress <!-- case:chk-changes -->

[^s1]: session 20261003-200440-chrono-2FYKPJ, step 4 — [video at 1:15](https://youtu.be/Pqx4QY-FpBA?t=75)
[^s2]: session 20261003-200440-chrono-2FYKPJ, step 3 — [video at 1:05](https://youtu.be/Pqx4QY-FpBA?t=65)

[^s3]: session 20261003-200440-chrono-2FYKPJ, step 2 — [video at 0:30](https://youtu.be/Pqx4QY-FpBA?t=30)
[^s4]: session 20261003-200440-chrono-2FYKPJ, step 7 — [video at 1:41](https://youtu.be/Pqx4QY-FpBA?t=101)
[^s5]: session 20261003-200440-chrono-2FYKPJ, step 19 — [video at 3:11](https://youtu.be/Pqx4QY-FpBA?t=191)
[^s6]: session 20261003-200440-chrono-2FYKPJ, step 5 — [video at 1:25](https://youtu.be/Pqx4QY-FpBA?t=85)
[^s7]: session 20261003-200440-chrono-2FYKPJ, step 12 — [video at 2:18](https://youtu.be/Pqx4QY-FpBA?t=138)
[^s8]: session 20261003-200440-chrono-2FYKPJ, step 16 — [video at 2:52](https://youtu.be/Pqx4QY-FpBA?t=172)
