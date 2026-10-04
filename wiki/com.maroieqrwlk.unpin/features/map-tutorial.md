---
game: com.maroieqrwlk.unpin
title: "Map tutorial tooltips"
type: feature
feature: map-tutorial
version_seen: 241.5.1
verified_at: 2026-10-03
sources: [20261003-203702-chrono-2FYKPJ]
---

# Map tutorial tooltips

A one-screen tutorial for the level map: the map is dimmed and four speech-bubble tooltips point at the
map's features — the items collection, rewards in levels, bonus levels and special levels [^s1]. It came once,
on the first map visit, and a tap dismissed it [^s3].

## Why it appeared

First tap on Play! on the map after the L3 win [^s1].

## Where to find it

No control opens it. After the level 3 win the map appears for the first time; the first tap on **Play!**
brings the tooltips instead of level 4 [^s2] [^s1].

![Map after the L3 win: Play!, whose first tap brought the tooltips](../img/20261003-map-tutorial-entry-99fc23cc.webp) [^s2]
*The first map, after the level 3 win: the green Play! button whose first tap brought the tooltips*

## What it looks like

![Dimmed map with tooltips: Check your items collection (shop box, coins 79), Get unique rewards buried in the levels (key on L6), Discover bonus levels (character between L8-9), Find levels with special features (L9); hard L7 and L12 skull](../img/20261003-map-tutorial-screen-9d63ed34.webp) [^s1]
*The dimmed map with four tooltips; the pointed-at controls stay bright*

| Tooltip | Points at |
|---|---|
| "Check your items collection!" | The box button right of Play! (Collections, coin balance 79) |
| "Get unique rewards buried in the levels!" | An orange key node beside a level |
| "Discover bonus levels as you go" | A character node between levels 8 and 9 |
| "Find levels with special features!" | Level 9 |

Source: [^s1]. The rest of the map is dimmed; the level nodes with skull badges (7 and 12) stay visible
[^s1].

## How it works

Version 241.5.1. One overlay with all four tooltips at once, no steps and no hand [^s1]. A tap on Play!
dismissed it; the next tap on Play! opened Daily Rewards [^s3]. No skip button was seen [^s1].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| One dimmed overlay with four tooltips: items collection (box button), unique rewards in levels (key node), bonus levels (character node), levels with special features (L9) <!-- case:chk-steps --> | Tapped Play! on the first map | ✅ Seen | [^s1] |
| No entry: shows by itself on the first Play! tap on the map after the L3 win <!-- case:chk-entry --> | Tapped Play! | ✅ By itself | [^s1] |
| Dimmed map with four speech-bubble tooltips <!-- case:chk-screen --> | Looked at it | ✅ Seen | [^s1] |
| A tap dismisses it; the next Play! tap opens Daily Rewards <!-- case:chk-end --> | Tapped Play! again | ✅ Dismissed; Daily Rewards next | [^s3] |
| Why it appeared <!-- case:chk-appeared --> | Won level 3, tapped Play! | ✅ The first map visit | [^s1] |
| Whether it can be skipped <!-- case:chk-skip --> | — | not verified |  |
| Whether it can be seen again <!-- case:chk-replay --> | — | not verified |  |

## Not verified

- Whether it can be skipped, and what happens when the app is left while it is shown <!-- case:chk-skip -->
- Whether it can be seen again (a help button, Settings) <!-- case:chk-replay -->

[^s1]: session 20261003-203702-chrono-2FYKPJ, step 6 — [video at 1:57](https://youtu.be/cirqlD7KGWI?t=117)
[^s2]: session 20261003-203702-chrono-2FYKPJ, step 5 — [video at 1:43](https://youtu.be/cirqlD7KGWI?t=103)
[^s3]: session 20261003-203702-chrono-2FYKPJ, step 8 — [video at 2:20](https://youtu.be/cirqlD7KGWI?t=140)
