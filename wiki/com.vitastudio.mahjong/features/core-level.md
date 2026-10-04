---
game: com.vitastudio.mahjong
title: "Tray mahjong level"
type: feature
feature: core-level
version_seen: 3.40.1
verified_at: 2026-10-03
sources: [20261003-195050-chrono-2FYKPJ]
---

# Tray mahjong level

The game's core: a numbered level with a pile of mahjong tiles. The player taps free tiles to move them
into a 4-slot tray above the board; identical tiles in the tray match and leave it. Tiles on top block the
ones they cover, and the ends of a row free the inner tiles [^s2]. One level at a time is played, from
the Level N button on the home screen [^s1].

## Why it appeared

The Level N button on the home screen, there from the first launch [^s1].

## Where to find it

Home screen > the large orange "Level N" button at the bottom (Level 19 in this session) [^s1].

![The home screen at level 19: the orange "Level 19" button at the bottom, under the closed sliding doors](../img/20261003-core-level-entry-c1fb4fc5.webp) [^s1]
*The "Level 19" button at the bottom of the home screen opens the level*

Tapping it slides the doors of the home screen apart with a beam of light, then the board appears [^s1]:

![The Level 19 tap on the home screen: the two sliding doors open apart, a beam of light, then the level 19 board](../clips/20261003-level-door-transition.webp) [^s1]
*Clip 5.6 s · [original on YouTube from 4:16](https://youtu.be/KUKs3cQ-xqY?t=256)*

## What it looks like

![Level 19: back arrow top left, "IQ: 40" top centre, menu button top right, an empty 4-slot tray, the board of white tiles (dots, bamboo, characters and zodiac signs) with purple face-down tiles, and Shuffle 3, Hint 5, Undo 10 at the bottom](../img/20261003-core-level-screen-d06a7bf0.webp) [^s1]
*The level screen: HUD on top, the 4-slot tray, the board, three boosters at the bottom*

- Top left: a back arrow to the home screen [^s3].
- Top centre: "IQ: 40" (see [IQ score](iq-score.md)) [^s1].
- Top right: the menu button (three lines) for Options (see [In-level Options](level-options.md)) [^s1].
- Under the HUD: an empty tray of 4 slots [^s1].
- The board: stacked tiles of the Simple tile set; level 19 has zodiac-sign tiles besides dots, bamboo
  and characters, and purple face-down tiles (see [Face-down tiles](face-down-tiles.md)) [^s1].
- Bottom: Shuffle 3, Hint 5, Undo 10 (see [Boosters](boosters.md)) [^s1].

No level number is shown on the level screen itself; it is on the home button [^s1].

## What you can do

| Tab or button | What it does |
|---|---|
| [Tiles](#tiles) | Tap a free tile to move it into the tray |
| [Back arrow](#back-arrow) | Leaves to the home screen at once |
| [Menu](#menu) | Opens the in-level Options |

### Tiles

<!-- no-frame: the board is on the level frame above; the rules are on the How to Play frames -->
The rules as the game's How to Play shows them: match identical tiles in the tray; tiles need not be
adjacent on the board to match; tap the top tiles to free the ones below; tap the left or right end of a
row to free the inner tiles [^s2]. See [How to Play](how-to-play.md). No tile was played in this session.

### Back arrow

<!-- no-frame: the arrow is on the level frame above -->
Goes straight to the home screen: no confirmation popup and no cost shown [^s3]. That the board is kept
for the next visit was seen in earlier sessions, not in this one [^s3].

### Menu

![The in-level Options popup over the board](../img/20261003-level-options-screen-c16e3ed0.webp) [^s4]
*The menu button opens Options: sound toggles, Auto Complete, Colorful Effects, Theme, How to Play, No Ads, Restart*

## How it works

Version 3.40.1.

- Tray of 4 slots [^s1] [^s2].
- Tiles of the active tile set: Simple in this save; it can be changed in [Theme](theme.md) [^s1].
- Leaving a level with the back arrow made a new button (Achievements) appear on the home screen (see
  [Achievements](achievements.md)) [^s3].

## Outcomes

| Outcome | What happens | Source |
|---|---|---|
| Quit with the back arrow <!-- case:chk-quit --> | Home screen at once, no confirmation, no cost seen | [^s3] |
| Win | not verified: no level finished in this session | |
| Loss | not verified | |

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| How to Play (Options): match identical tiles via the 4-slot tray; top tiles unlock covered ones; row ends unlock inner tiles <!-- case:chk-rules --> | Read How to Play from the level's Options | ✅ | [^s2] |
| Back arrow in the level goes straight to the home screen, no confirmation, no cost seen (board kept, per earlier sessions) <!-- case:chk-quit --> | Tapped the back arrow on level 19 | ✅ | [^s3] |
| Level N button on the home screen <!-- case:chk-entry --> | Tapped Level 19 | ✅ Door transition, then the board | [^s1] |
| Board with a 4-slot tray above it <!-- case:chk-screen --> | Opened level 19 | ✅ | [^s1] |
| Back arrow, IQ score, menu; 4-slot tray; Shuffle 3, Hint 5, Undo 10 at level 19 <!-- case:chk-hud --> | Opened level 19 | ✅ | [^s1] |
| Why it appeared: the trigger that brought it up (the first launch, a level won, a threshold, a timer, a loss): a fact with its frame, or a hypothesis to test <!-- case:chk-appeared --> | — | ✅ The Level N button, from the first launch | [^s1] |
| Win: the win screen, its rewards and what comes next <!-- case:chk-win --> | — | not verified |  |
| Each loss: lose the level every way it can be lost: its screen and what the loss costs <!-- case:chk-loss --> | — | not verified |  |
| After a loss: the retry and continue offers (extra moves, a revive) and their price (a video, coins, a life) <!-- case:chk-retry --> | — | not verified |  |
| Restart: restart the level from inside it: the confirmation and what it costs <!-- case:chk-restart --> | — | not verified: the Restart button in Options not tapped |  |
| Exit the app: leave the app in the middle of the level and come back: is the level kept, restarted or lost <!-- case:chk-exit-app --> | — | not verified |  |
| Level elements: each obstacle or special piece the levels introduce, with the level it first shows on <!-- case:chk-elements --> | — | partly: face-down tiles seen on level 19; zodiac tiles are a tile kind (not verified as an element) | [^s1] |

## Not verified

- Win: the win screen, its rewards and what comes next <!-- case:chk-win -->
- Each loss: the full tray and what it costs <!-- case:chk-loss -->
- After a loss: the retry and continue offers and their price <!-- case:chk-retry -->
- Restart: the Restart button in Options, its confirmation and cost <!-- case:chk-restart -->
- Exit the app in the middle of a level and come back <!-- case:chk-exit-app -->
- Level elements: the first level of each element <!-- case:chk-elements -->

[^s1]: session 20261003-195050-chrono-2FYKPJ, step 17 — [video at 4:21](https://youtu.be/KUKs3cQ-xqY?t=261)
[^s2]: session 20261003-195050-chrono-2FYKPJ, step 20 — [video at 5:29](https://youtu.be/KUKs3cQ-xqY?t=329)
[^s3]: session 20261003-195050-chrono-2FYKPJ, step 22 — [video at 6:03](https://youtu.be/KUKs3cQ-xqY?t=363)
[^s4]: session 20261003-195050-chrono-2FYKPJ, step 18 — [video at 4:55](https://youtu.be/KUKs3cQ-xqY?t=295)
