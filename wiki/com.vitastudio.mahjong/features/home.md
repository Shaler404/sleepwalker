---
game: com.vitastudio.mahjong
title: "Home screen"
type: feature
feature: home
version_seen: 3.40.1
verified_at: 2026-10-05
sources: [20261003-195050-chrono-2FYKPJ, 20261003-231804-chrono-2FYKPJ, 20261005-073409-chrono-2FYKPJ]
---

# Home screen

The game's hub: a single screen of closed sliding paper doors under the Vita Mahjong logo, with the
Level N button at the bottom, the avatar and a leaf counter top left and a few round buttons top right.
At level 19 there is no shop, no coin balance, no daily reward and no event button [^s2] [^s6].

## Why it appeared

The first launch, after the consent, the loading screen, the age popup and the saved-game prompt [^s1].

## Where to find it

<!-- no-entry: the hub; the game opens on it after loading, and the level's back arrow returns to it -->
The game opens on it after the loading screen; the back arrow of a level and of Achievements return to it
[^s4] [^s2].

## What it looks like

![The home screen at level 19: the avatar with a red dot and the leaf counter "x0" top left; thumbs-up with a star, palette with a red dot and gear top right; the Vita Mahjong logo; closed sliding doors with a round handle; the orange Level 19 button](../img/20261005-home-screen-d4fc1f86.webp) [^s7]
*Home at level 19: avatar, leaf counter, Achievements, Theme, Settings, Level 19*

- Top left: the player's avatar, which opens [Profile](profile.md) [^s3]; right of it the leaf counter
  "x0", which opens [Daily Victories](daily-victories.md) [^s8].
- Top right: the thumbs-up with a star ([Achievements](achievements.md), only after a level visit), the
  palette ([Theme](theme.md)) and the gear ([Settings](settings.md)) [^s4] [^s3].
- Centre: the logo and the closed doors [^s2].
- Bottom: the orange "Level N" button, which opens the next level ([Tray mahjong level](core-level.md))
  [^s2].

## What you can do

| Tab or button | What it does |
|---|---|
| [Avatar](#avatar) | Opens Profile |
| [Leaf counter](#leaf-counter) | Opens Daily Victories |
| [Achievements button](#achievements-button) | Opens Achievements |
| [Palette](#palette) | Opens Theme |
| [Gear](#gear) | Opens Settings |
| [Level button](#level-button) | Opens the current level |

### Avatar

![The home screen right after Sync Data, still at Level 1: a grey placeholder avatar with a red dot top left, palette and gear top right](../img/20261003-profile-entry-d0f85be5.webp) [^s1]
*The avatar button top left, here with its red dot on the first visit*

Opens [Profile](profile.md). Its red dot disappeared once Profile had been opened [^s3].

### Leaf counter

<!-- no-frame: the counter is on the home frame above, right of the avatar -->
The leaf icon with "x0", right of the avatar. Tapping it slid the doors apart (the same door transition as
for a level) onto the [Daily Victories](daily-victories.md) calendar, where the same leaf stands for the
day streak, 0 at the time [^s8]. See also [Leaf counter](leaves.md).

### Achievements button

![The home screen after leaving level 19: the thumbs-up-with-a-star button now stands left of the palette](../img/20261003-achievements-entry-d0fa5fa7.webp) [^s4]
*The thumbs-up-with-a-star button appeared after leaving a level*

Opens [Achievements](achievements.md) [^s4].

### Palette

![The home screen at level 19 with a red dot on the palette button](../img/20261003-theme-entry-c1fb4f47.webp) [^s3]
*The palette button with its red dot, left of the gear*

Opens [Theme](theme.md) [^s3].

### Gear

![The home screen at level 19, gear top right](../img/20261003-settings-entry-d0f94f47.webp) [^s3]
*The gear, top right corner*

Opens [Settings](settings.md) [^s3].

### Level button

![The home screen at level 19, the orange Level 19 button at the bottom](../img/20261003-core-level-entry-c1fb4fc5.webp) [^s4]
*The Level 19 button*

Opens the level with a door-opening transition (see [Tray mahjong level](core-level.md)) [^s4].

## How it works

Version 3.40.1.

- Right after Sync Data the screen showed Level 1 and a grey placeholder avatar; a few seconds later it
  showed Level 19 and the restored avatar (see [Saved game sync](cloud-sync.md)) [^s1].
- Red dots: on the avatar until Profile was opened; on the palette after the sync [^s3]. On a later
  launch that reopened at Level 1, the avatar had a red dot and the palette none; once the save was
  restored both the avatar and the palette had red dots [^s5].
- The leaf counter read "x0" both on the Level 1 home before Sync Data and on the Level 19 home after
  it [^s6].
- On a later launch the home behind the saved-game prompt read Level 1 with the grey placeholder avatar
  (red dot), the leaf counter and all three buttons top right, the Achievements button included; after
  Sync Data it showed the restored avatar, Level 19 and red dots on the avatar and the palette [^s6].
- On arrival at level 19 the top right had two buttons (palette, gear). After the player opened level 19
  and left it with the back arrow, a third (Achievements) was there [^s3] [^s4].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Home: avatar, theme palette, settings gear, logo, shoji doors, Level N button <!-- case:chk-screen --> | Arrived after the sync | ✅ | [^s3] |
| The hub: the game opens on it after loading; the level back arrow returns to it <!-- case:chk-entry --> | Left level 19 with the back arrow | ✅ | [^s4] |
| Why it appeared: the trigger that brought it up (the first launch, a level won, a threshold, a timer, a loss): a fact with its frame, or a hypothesis to test <!-- case:chk-appeared --> | Fresh install | ✅ After the first-launch prompts | [^s1] |
| Every entry point on it: open (a feature), locked or unclear <!-- case:chk-entries --> | Opened every button; later tapped the leaf counter | ✅ at level 19: avatar (Profile), leaf counter (Daily Victories), thumbs-up (Achievements), palette (Theme), gear (Settings), Level N; all open, nothing locked | [^s2] [^s6] |
| Red dots after a restore <!-- case:badge-theme --> | Restored the save (Start Over > No) on a launch at Level 1 | ✅ The palette had no dot on the Level 1 home; after the restore the palette and the avatar both had red dots | [^s5] |
| Badges, timers and counters on it and what each points to <!-- case:chk-badges --> | Opened the avatar, the palette and the leaf counter | ✅ red dots on the avatar (Profile) and the palette (Theme); the leaf counter "x0" is the Daily Victories day streak; no timers | [^s3] [^s6] |
| What changes on it with progress (new buttons, a moving map, a theme) <!-- case:chk-changes --> | Level visit; a launch at Level 1, then Sync Data | ✅ before Sync: Level 1 and a grey placeholder avatar; after Sync: the restored avatar, Level 19 and a red dot on the palette; Achievements appeared after a level visit in the first session. Changes at levels past 19 not seen | [^s4] [^s6] |

## Not verified

- Buttons that may appear past level 19 (shop, events, leagues): not reached.

[^s1]: session 20261003-195050-chrono-2FYKPJ, step 4 — [video at 1:18](https://youtu.be/KUKs3cQ-xqY?t=78)
[^s2]: session 20261003-195050-chrono-2FYKPJ, step 28 — [video at 7:53](https://youtu.be/KUKs3cQ-xqY?t=473)
[^s3]: session 20261003-195050-chrono-2FYKPJ, step 10 — [video at 3:07](https://youtu.be/KUKs3cQ-xqY?t=187)
[^s4]: session 20261003-195050-chrono-2FYKPJ, step 22 — [video at 6:03](https://youtu.be/KUKs3cQ-xqY?t=363)
[^s5]: session 20261003-231804-chrono-2FYKPJ, step 3 — [video at 0:59](https://youtu.be/ssTmhwls_uc?t=59)
[^s6]: session 20261005-073409-chrono-2FYKPJ, step 6 — [video at 2:24](https://youtu.be/vgVMznU7XG0?t=144)
[^s7]: session 20261005-073409-chrono-2FYKPJ, step 1 — [video at 0:40](https://youtu.be/vgVMznU7XG0?t=40)
[^s8]: session 20261005-073409-chrono-2FYKPJ, step 2 — [video at 0:53](https://youtu.be/vgVMznU7XG0?t=53)
