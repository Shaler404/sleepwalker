---
game: com.block.juggle
title: "Adventure mode"
type: feature
feature: adventure
version_seen: 10.8.1
verified_at: 2026-10-04
sources: [20261003-212548-chrono-2FYKPJ, 20261003-235233-chrono-2FYKPJ]
---

# Adventure mode

A mode of 96 levels in a row. Each level is the 8x8 board, tray and drag of [Classic](classic.md), but
it starts on a pre-built layout and has a goal: a target score on level 1, gems to collect from level 2
on (see [Adventure diamond-collection levels](adv-diamonds.md)). The levels sit on a map shaped like a
trophy; winning all of them wins the trophy [^s3] [^s4] [^s6]. A win adds one to the
[Adventure win streak](adv-win-streak.md) and counts for the home menu's
[Consecutive Daily Victories](daily-victories.md) [^s9] [^s10]. No energy, lives, timer or currency
was seen [^s11].

## Why it appeared

On the home menu with a red dot, the first time the menu was opened (the phone's Back key from a classic
game) [^s1]. The red dot was gone after the first Adventure win [^s10].

## Where to find it

Home menu > the orange Adventure button, the first of the three mode buttons, with a red dot top right
until the first win [^s2] [^s10]. The home menu is reached with the Back key from the classic board (see
[Home menu](home-menu.md)).

![The home menu; the orange Adventure button with a red dot is the first mode button, under the Consecutive Daily Victories panel](../img/20261003-adventure-entry-83212d2d.webp) [^s2]
*The orange Adventure button with a red dot, above Classic*

## What it looks like

![The Adventure map: back arrow, title, a dark trophy with "Take part in the Adventure and win the trophy", 96 numbered cells in the shape of a trophy, cell 1 yellow with a marker, the green Level 1 button](../img/20261003-adventure-screen-fe83d268.webp) [^s3]
*The Adventure map before the first level: cell 1 is the current one*

The Adventure screen: a back arrow and the title "Adventure"; a dark trophy silhouette with the line
"Take part in the Adventure and win the trophy."; under it 96 numbered cells laid out in the shape of a
trophy, from 1 bottom left to 96 at the top; a green "Level N" button at the bottom. The current level's
cell is yellow with a marker on it; won cells are filled light blue [^s3] [^s5].

## What you can do

| Tab or button | What it does |
|---|---|
| [Level N](#level-n) | Plays the current level |
| [Level cells](#level-cells) | Show progress; a tap on a future cell does nothing |
| [Gear in a level](#gear-in-a-level) | Settings with Home and Replay |
| [Win screen](#win-screen) | Next Level, or the back arrow to the home menu |
| [Loss screen](#loss-screen) | Retry, or the back arrow to the home menu |

### Level N

![Adventure level 1: back arrow, gear, a score bar from 0 to the target 368, the 8x8 board with pre-placed green blocks, three tray pieces](../img/20261003-adventure-tab-level-fe72818d.webp) [^s4]
*Level 1: a score bar to 368 in place of Classic's score*

The green button at the bottom of the map opens the current level straight away, with no intro or
goal popup [^s4]. The level screen has a back arrow, the gear and the goal at the top, the board and
the tray [^s4]. Level 1's goal is a score bar from 0 to 368; from level 2 the goal is a counter for each
gem kind [^s4] [^s6].

![Adventure level 2: a diamond with the count 60 in place of the score bar; diamond tiles on the tree-shaped layout and on two tray pieces](../img/20261003-adventure-tab-diamond-level-ce4b3534.webp) [^s6]
*Level 2: the goal is 60 diamonds*

### Level cells

![The Adventure map after the level 1 win: cell 1 light blue, cell 2 yellow with the marker, the button reads Level 2](../img/20261003-adventure-tab-map-progress-f887d068.webp) [^s5]
*After the first win: cell 1 lit, cell 2 current, Level 2 button*

The cells show progress only. A tap on a future cell (5) changed nothing; only the Level N button plays,
and only the current level [^s11].

### Gear in a level

![The gear in Adventure level 4: Settings with Sound, BGM, Vibration and a slider, More Settings, Home and Replay; the level's three goals, 22, 20 and 20, behind it](../img/20261003-adventure-popup-c1b93ece.webp) [^s7]
*The in-level Settings: Home and Replay instead of More Games and Default Skin*

The gear opens a Settings popup with Sound, BGM, Vibration with a slider, More Settings, Home and Replay
[^s7] (see [Settings](settings.md)). Home leaves for the home menu at once, with no confirmation and no
cost; the level stays the current one [^s12]. Replay was not tapped.

### Win screen

![The level 3 win screen: the Consecutive Victories panel at x2 at the top, the trophy grid with three cells lit, a green Next Level button](../img/20261003-adv-win-streak-screen-939393c3.webp) [^s16]
*The win screen after level 3: win streak x2, three cells lit, Next Level*

When the goal is met the board dims, a "Consecutive Victories xN" panel drops in from the top, the
trophy grid shows the won cell lit, and a green Next Level button is at the bottom; the back arrow stays
top left [^s9] [^s16]. No coins or other currency were paid [^s9]. The back arrow goes to the home menu
[^s10]; Next Level was not tapped (the next level was opened from the map) [^s15].

![The last clears of level 3, then the win screen: the Consecutive Victories panel drops in at x2 above the trophy grid and Next Level](../clips/20261003-adventure-win-streak-panel.webp) [^s16]
*Clip 3 s · [original on YouTube from 12:04](https://youtu.be/RE70Idi_jrA?t=724)*

### Loss screen

![Adventure level 2 lost on No Space Left: the dimmed board, the diamond goal with 56 left, "You Can Do It!", a green Retry button; the Consecutive Victories panel at x0](../img/20261003-adventure-result-d3939392.webp) [^s8]
*The loss screen: the gems still needed, "You Can Do It!" and Retry; the win streak back to x0*

When no tray piece fits before the goal is met: the board dims, the goal shows what is left (56 of 60
diamonds), "You Can Do It!" and a green Retry button; the "Consecutive Victories" panel drops in at x0
(it was x1). No revive or continue offer, no price, no lives spent [^s8]. The back arrow goes to the
home menu [^s10]. Retry was not tapped: the level was restarted from the map instead [^s13].

## How it works

Version 10.8.1.

- Levels are played in order: only the current one can be opened, from the Level N button [^s11].
- Each level has a pre-built board and a goal. Goals so far: level 1 a score of 368; level 2 60
  diamonds; level 3 56 red and 54 orange gems; level 4 22 blue diamonds, 20 orange gems and 20 yellow
  stars [^s4] [^s6] [^s15] [^s12]. Gems are collected by clearing the row or column that holds the gem
  tile (see [Adventure diamond-collection levels](adv-diamonds.md)) [^s17].
- No move limit, timer, boosters, energy or lives [^s6] [^s11].
- A lost level restarts with the same pre-built board and goal: level 2 opened again with the same
  60-diamond tree layout [^s13].
- A win pays no currency; it lights the level's cell on the trophy map, adds one to the
  [Adventure win streak](adv-win-streak.md) and counts for the day on
  [Consecutive Daily Victories](daily-victories.md) [^s9] [^s10] [^s16].
- An interstitial ad came once in four results: after the level 2 win on the second try, before the win
  screen [^s14]. Its top-left icon opened the Play Store (see
  [Interstitial ad](ad-interstitial-classic.md)).
- Levels 1 to 3 each took about 2 to 3 minutes of play [^s9] [^s14] [^s16].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared <!-- case:chk-appeared --> | Opened the home menu with Back | ✅ On the menu with a red dot; the dot was gone after the first win | [^s1] |
| Where to find it <!-- case:chk-entry --> | Home menu > Adventure | ✅ The orange Adventure button opens the Adventure map | [^s2] |
| Its screen <!-- case:chk-screen --> | Opened Adventure | ✅ Back arrow, title, trophy silhouette, 96-cell trophy-shaped grid, green Level N button | [^s3] |
| Rules <!-- case:chk-rules --> | Played levels 1 and 2 | ✅ Classic's board, tray and drag with a goal and a pre-built board: level 1 a score of 368, level 2 60 diamonds; no boosters | [^s6] |
| Different goals per level <!-- case:goals --> | Opened levels 1 to 4 | ✅ Score 368; 60 diamonds; 56 red + 54 orange; 22 blue + 20 orange + 20 yellow stars | [^s12] |
| A win <!-- case:chk-win --> | Won level 1 | ✅ Board dims, Consecutive Victories x1, the won cell lit, Next Level; no currency | [^s9] |
| A loss <!-- case:chk-loss --> | Lost level 2 on No Space Left | ✅ The goal left (56), "You Can Do It!", Retry, back arrow; win streak x1 to x0; no revive, no cost | [^s8] |
| Retry after a loss <!-- case:retry --> | Back arrow, then Adventure > Level 2 | ✅ The same level with the same pre-built board and goal | [^s13] |
| Quit a level <!-- case:quit --> | Gear > Home in level 4 | ✅ Home menu at once, no confirmation, no cost; level 4 stays current | [^s12] |
| Progression inside the mode <!-- case:chk-progression --> | Looked at the map before and after wins | ✅ 96 levels in a trophy-shaped grid; the current cell yellow with a marker, won cells lit | [^s3] |
| Limits <!-- case:chk-limits --> | Looked at the map and levels; tapped a future cell | ✅ No energy, lives, timer or attempt counter; future cells do nothing | [^s11] |

## Not verified

- What the loss screen's Retry button does (the level was restarted from the map)
- What Next Level on the win screen does (the next level was opened from the map)
- Settings gear > Replay inside a level
- Leaving the app in a level and coming back
- How often an interstitial ad comes after a result (once in four results here)
- What winning all 96 levels pays

[^s1]: session 20261003-212548-chrono-2FYKPJ, step 29 — [video at 5:55](https://youtu.be/ReMKqt9albk?t=355)
[^s2]: session 20261003-235233-chrono-2FYKPJ, step 5 — [video at 1:28](https://youtu.be/RE70Idi_jrA?t=88)
[^s3]: session 20261003-235233-chrono-2FYKPJ, step 6 — [video at 1:36](https://youtu.be/RE70Idi_jrA?t=96)
[^s4]: session 20261003-235233-chrono-2FYKPJ, step 7 — [video at 1:49](https://youtu.be/RE70Idi_jrA?t=109)
[^s5]: session 20261003-235233-chrono-2FYKPJ, step 23 — [video at 4:35](https://youtu.be/RE70Idi_jrA?t=275)
[^s6]: session 20261003-235233-chrono-2FYKPJ, step 25 — [video at 4:57](https://youtu.be/RE70Idi_jrA?t=297)
[^s7]: session 20261003-235233-chrono-2FYKPJ, step 63 — [video at 13:13](https://youtu.be/RE70Idi_jrA?t=793)
[^s8]: session 20261003-235233-chrono-2FYKPJ, step 29 — [video at 5:47](https://youtu.be/RE70Idi_jrA?t=347)
[^s9]: session 20261003-235233-chrono-2FYKPJ, step 21 — [video at 3:47](https://youtu.be/RE70Idi_jrA?t=227)
[^s10]: session 20261003-235233-chrono-2FYKPJ, step 22 — [video at 4:11](https://youtu.be/RE70Idi_jrA?t=251)
[^s11]: session 20261003-235233-chrono-2FYKPJ, step 24 — [video at 4:46](https://youtu.be/RE70Idi_jrA?t=286)
[^s12]: session 20261003-235233-chrono-2FYKPJ, step 64 — [video at 13:28](https://youtu.be/RE70Idi_jrA?t=808)
[^s13]: session 20261003-235233-chrono-2FYKPJ, step 32 — [video at 6:39](https://youtu.be/RE70Idi_jrA?t=399)
[^s14]: session 20261003-235233-chrono-2FYKPJ, step 45 — [video at 9:41](https://youtu.be/RE70Idi_jrA?t=581)
[^s15]: session 20261003-235233-chrono-2FYKPJ, step 48 — [video at 10:21](https://youtu.be/RE70Idi_jrA?t=621)
[^s16]: session 20261003-235233-chrono-2FYKPJ, step 59 — [video at 12:07](https://youtu.be/RE70Idi_jrA?t=727)
[^s17]: session 20261003-235233-chrono-2FYKPJ, step 27 — [video at 5:32](https://youtu.be/RE70Idi_jrA?t=332)
