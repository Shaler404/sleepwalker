---
game: com.vitastudio.mahjong
title: "How to Play"
type: feature
feature: how-to-play
version_seen: 3.40.1
verified_at: 2026-10-03
sources: [20261003-195050-chrono-2FYKPJ]
---

# How to Play

A two-page rules popup, opened from the level's Options. Each page has two illustrated panels with one
line of text each: how tiles match in the tray and how covered tiles are freed [^s1] [^s3].

## Why it appeared

A row in the in-level Options menu, present when the menu was first opened at level 19 [^s1].

## Where to find it

Level screen > menu button (three lines, top right) > Options > the "How to Play" row (an "i" icon),
under Theme [^s2].

![The in-level Options popup: How to Play is the second of four rows, under Theme and above No Ads](../img/20261003-how-to-play-entry-c16e3ed0.webp) [^s2]
*The "How to Play" row in the in-level Options*

## What it looks like

![How to Play page 1: a panel with two identical dot tiles in the tray, "Match the same tiles!"; a panel with four tiles above an empty tray, "Non-adjacent tiles can be matched"; a green Next button](../img/20261003-how-to-play-screen-c44e73b1.webp) [^s1]
*Page 1: matching in the tray; Next goes to page 2*

A popup over the level, with a close X top right. Each page: two green panels, each with a caption, and
the buttons at the bottom [^s1].

## What you can do

| Tab or button | What it does |
|---|---|
| [Page 1](#page-1) | Matching; Next opens page 2 |
| [Page 2](#page-2) | Freeing tiles; back arrow to page 1, Get it closes |

### Page 1

<!-- no-frame: page 1 is the frame above -->
- "Match the same tiles!": two identical tiles side by side in the tray [^s1].
- "Non-adjacent tiles can be matched": a row of alternating tiles above an empty tray [^s1].
- Next opens page 2 [^s3].

### Page 2

![How to Play page 2: a tile covered by another with a red no-entry mark, "Tap the top tiles to unlock other tiles"; a row of tiles with one end tile taken, "Tap left or right tiles to unlock inner tiles"; a back arrow and Get it](../img/20261003-how-to-play-tab-page-2-c54e4e91.webp) [^s3]
*Page 2: covered tiles and row ends; Get it closes the popup*

- "Tap the top tiles to unlock other tiles": a covered tile is marked as blocked [^s3].
- "Tap left or right tiles to unlock inner tiles": the end of a row is taken first [^s3].
- A back arrow returns to page 1; Get it closes the popup and returns to the level [^s3].

## How it works

Version 3.40.1. Two pages, no animation; neither page mentions face-down tiles (see
[Face-down tiles](face-down-tiles.md)) [^s3]. It can be opened again at any time from the level's Options
[^s2].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Level Options > How to Play <!-- case:chk-entry --> | Opened from the level 19 Options | ✅ | [^s1] |
| Two pages: matching via the tray; top and row-end tiles unlock others; Get it <!-- case:chk-screen --> | Read both pages | ✅ | [^s3] |
| Why it appeared: the trigger that brought it up (the first launch, a level won, a threshold, a timer, a loss): a fact with its frame, or a hypothesis to test <!-- case:chk-appeared --> | Opened the level's Options | ✅ A row there | [^s1] |
| Each step and what it teaches, with a frame (an animated hand is a clip) <!-- case:chk-steps --> | Next, then Get it | ✅ Two pages, two panels each, no animation | [^s3] |
| Whether it can be skipped, and what happens when the app is left in the middle of it <!-- case:chk-skip --> | — | partly: the close X skips it (not tapped); leaving the app in the middle not tried | [^s1] |
| Where it ends and what opens after it <!-- case:chk-end --> | Tapped Get it | ✅ The popup closes on the level | [^s3] |
| Whether it can be seen again (How to play, a help button) <!-- case:chk-replay --> | — | ✅ Always in the level's Options | [^s2] |

## Not verified

- Whether it can be skipped with the close X, and leaving the app in the middle <!-- case:chk-skip -->
- Whether the same pages are shown as a tutorial on level 1 of a new player

[^s1]: session 20261003-195050-chrono-2FYKPJ, step 19 — [video at 5:15](https://youtu.be/KUKs3cQ-xqY?t=315)
[^s2]: session 20261003-195050-chrono-2FYKPJ, step 18 — [video at 4:55](https://youtu.be/KUKs3cQ-xqY?t=295)
[^s3]: session 20261003-195050-chrono-2FYKPJ, step 20 — [video at 5:29](https://youtu.be/KUKs3cQ-xqY?t=329)
