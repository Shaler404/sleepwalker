---
game: com.king.candycrushsaga
title: "Level map"
type: feature
feature: map
version_seen: 1.337.0.2
verified_at: 2026-10-03
sources: [20261003-194350-chrono-2FYKPJ]
---

# Level map

The main screen between levels: a winding path of numbered level nodes, with a top bar of currencies and
icons and a bottom tab bar that switches between the map and four other screens [^s2].

## Why it appeared

After winning level 1: level 1 opened straight from the title screen with no map, and the first frame after
the win showed the Level 2 start popup over the map [^s1] [^s3].

## Where to find it

The map is the screen the game returns to after a level. From the other tabs, the Map tab (a folded map
icon) at the left end of the bottom tab bar brings it back [^s2].

![The level map with the Map tab selected at the left end of the bottom tab bar](../img/20261003-map-entry-9af4f0af.webp) [^s2]
*Map, the first tab of the bottom tab bar*

## What it looks like

![The level map after level 1: the top bar, a path of pink level nodes, the level 2 node with the avatar beside it, the level 1 node with a crown at the bottom, the bottom tab bar](../img/20261003-map-screen-9af4f0af.webp) [^s2]
*The map after level 1: level 2 is the highlighted node, the avatar marks the player's place*

A candy-coloured path climbs up the screen with pink round nodes. The next level (2) is a larger
highlighted node with the player's avatar beside it; level 1 sits below with a crown. Characters and houses
line the path [^s2].

Top bar, left to right: an envelope, a heart with 5 and "Full", the avatar, a gold bar with 0, a gear.
Bottom tab bar: Map, a calendar, two figures, a star badge, a shop stall with a red badge "1"; the selected
tab is lighter and shows its name [^s2].

## What you can do

| Tab or button | What it does |
|---|---|
| [Top bar](#top-bar) | Envelope, lives, avatar, gold bars, gear |
| [Bottom tab bar](#bottom-tab-bar) | Map, Events, Social, Pins, Shop |
| [Level node](#level-node) | The level start popup |

### Top bar

<!-- no-frame: the top bar is on the map frame above -->
Left to right [^s2]:

- Envelope: a tap changed nothing, see [Mailbox icon](mailbox.md).
- Heart with 5 and "Full": opens the [Lives](lives.md) popup.
- Avatar: opens [Profile and inventory](profile.md).
- Gold bar with 0: a tap changed nothing (tried with the Shop tab open) [^s1].
- Gear: opens [Settings](settings.md).

### Bottom tab bar

<!-- no-frame: the tab bar is on the map frame above -->
Left to right; the selected tab is lighter and shows its name [^s2]:

- Map: this screen.
- Calendar: the [Events tab](events-tab.md).
- Two figures: Social, with [Candy Teams](candy-teams.md) and the [Friends list](friends.md).
- Star badge: the [Pins collection](pins.md).
- Shop stall, with a red badge "1": the [Shop](shop.md).

### Level node

<!-- no-frame: the start popup is on the Level page -->
The Level 2 start popup came up by itself after the level 1 win, over the map; its X closed it to the map
[^s3] [^s2]. See [Level](core-level.md#level-start-popup). Tapping a node directly was not tried.

## How it works

Version 1.337.0.2. Only the next level (2) and the won level (1) were seen as reached nodes; the nodes above
level 2 were plain [^s2]. The Shop badge "1" was on the tab from the first map view [^s2].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared <!-- case:chk-appeared --> | Won level 1 | ✅ The map shows for the first time, under the Level 2 popup | [^s1] |
| Where to find it <!-- case:chk-entry --> | Closed the Level 2 popup | ✅ The map; the Map tab at the left of the tab bar | [^s2] |
| What it looks like <!-- case:chk-screen --> | Looked at the map | ✅ Path of nodes, top bar, tab bar | [^s2] |
| Every entry point on it <!-- case:chk-entries --> | Tapped every top bar icon and every tab | ✅ All five tabs and the heart, avatar and gear open screens; envelope and gold bar did nothing | [^s1] |
| Badges, timers and counters on it <!-- case:chk-badges --> | Looked at the bar and tabs | ✅ partly: lives 5 Full, gold bars 0, Shop badge 1; what the badge counts is not verified | [^s2] |
| What changes on it with progress <!-- case:chk-changes --> | — | not verified: only the map at level 2 was seen |  |

## Not verified

- What the Shop tab badge "1" counts, and when it clears <!-- case:chk-badges -->
- What changes on the map with progress (new nodes, episodes, new icons) <!-- case:chk-changes -->
- Tapping a level node directly (the Level 2 popup came up by itself)

[^s1]: session 20261003-194350-chrono-2FYKPJ, step 23 — [video at 4:49](https://youtu.be/OjVVcEHXMyI?t=289)
[^s2]: session 20261003-194350-chrono-2FYKPJ, step 7 — [video at 2:16](https://youtu.be/OjVVcEHXMyI?t=136)
[^s3]: session 20261003-194350-chrono-2FYKPJ, step 6 — [video at 1:33](https://youtu.be/OjVVcEHXMyI?t=93)
