---
game: com.maroieqrwlk.unpin
title: "Golden pins (league score)"
type: feature
feature: golden-pins
version_seen: 241.5.1
verified_at: 2026-10-04
sources: [20261004-005453-chrono-2FYKPJ]
---

# Golden pins (league score)

A second score of the Bronze League (the league of [Pull Fest Ranking](pull-fest.md)): a golden pin with a
star head sits on a level board among the usual grey pins, and pulling it adds one **Golden Pin** to the
player's league score next to the ordinary **Pins** [^s3] [^s2]. One golden pin counted as 5 in the league's
**Total Score** [^s2] [^s5]. After a win the league board offers a video for +5 golden pins [^s2].

## Why it appeared

Golden star-wand pin on hard L12; after the win the Bronze League board showed a Golden Pins counter (1) next
to Pins, Total Score 50, and a video offer +5 golden pins; the map league panel now shows a wand counter [^s1].
The first golden pin seen was on hard level 12 [^s3]; the map's league panel already showed the wand counter
at 0 right before that level, after the level 11 win [^s4].

## Where to find it

It has no button of its own. On the map, the dark panel under the ranking icon at the right edge shows two
counters: a magnifier-pin with the Pins and a golden wand with the Golden Pins [^s1] [^s4]. The full score is
on the Bronze League board that comes after each win [^s2].

![The map after the level 12 win: the league panel under the ranking icon at the right, Pins 45 and the golden wand at 1](../img/20261004-golden-pins-entry-ccb2ec33.webp) [^s1]
*The map after the level 12 win: the panel under the ranking icon at the right shows Pins 45 and the golden wand counter 1 (the player's name in the league banner blacked out)*

## What it looks like

![The Bronze League board after the level 12 win: Pins 45, Golden Pins 1, Total Score 50; the green +5 video button left of Next Level!](../img/20261004-golden-pins-screen-bf36c1b4.webp) [^s2]
*The Bronze League board after the level 12 win: Pins 45, Golden Pins 1, Total Score 50, the green video button with +5 and a wand left of Next Level! (the leaderboard names blacked out)*

The Bronze League board after a win now has three boxes above the leaderboard: **Pins** (blue, 45),
**Golden Pins** (blue, a wand icon, 1) and **Total Score** (yellow, 50) [^s2]. Under the leaderboard the
single **Next Level!** button became two: a green video button with "+5" and a wand on the left, **Next
Level!** on the right [^s2].

## What you can do

| Tab or button | What it does |
|---|---|
| [Golden pin in a level](#golden-pin-in-a-level) | A pin with a star head; pulling it adds one Golden Pin |
| [Golden pins video](#golden-pins-video) | The green video button on the league board: +5 golden pins for a video; not taken |

### Golden pin in a level

![Level 12: the golden pin with a star head across the grey balls, among the grey pins; the panel at the right shows the wand counter 0](../img/20261004-golden-pins-tab-golden-pin-d625da21.webp) [^s3]
*Level 12 (a hard level): the golden pin with a yellow star head holds the grey balls; the panel at the right shows Pins 44 and the wand 0 (a banner ad blacked out)*

On level 12 one of the three pins was golden with a yellow star for a head; it held the grey balls and the
coloured ones above them [^s3]. It is pulled like any pin [^s2]. After the win the board showed Golden Pins 1
[^s2].

### Golden pins video

![The green video button with +5 and a wand, left of Next Level!](../img/20261004-golden-pins-tab-video-plus-5-bf36c1b4.webp) [^s2]
*The green button with a video icon, +5 and a wand, left of Next Level! on the league board*

A video for +5 golden pins, offered on the league board after the level 12 win and again after level 13
[^s2] [^s5]. It was not taken; Next Level! went on to "Level completed!" [^s7].

## How it works

Version 241.5.1.

| Moment | Pins | Golden Pins | Total Score | Source |
|---|---|---|---|---|
| Before level 12 (map, level panel) | 44 | 0 | — | [^s4] [^s3] |
| After the level 12 win (golden pin pulled) | 45 | 1 | 50 | [^s2] |
| After the last pull of level 13 (no golden pin seen) | 49 | 1 | 54 | [^s5] |

- Total Score = Pins + 5 × Golden Pins on both boards (45 + 5 = 50, 49 + 5 = 54) [^s2] [^s5]. Inferred from
  two boards with one golden pin.
- The golden count stayed at 1 through level 13 [^s5].
- The rank in the league went from 554 before level 12 to 521 after it, and 505 after level 13 [^s4] [^s1]
  [^s5].
- Whether golden pins appear only on hard levels is not known: the only one seen was on hard level 12 [^s3].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| League board after a win offers a video for +5 golden pins (left of Next Level); not taken <!-- case:video-plus-5 --> | Tapped Next Level! instead | not verified: the video's effect not seen | [^s2] |
| League board after a win: Pins / Golden Pins / Total Score row above the leaderboard, a +5 golden pins video button left of Next Level <!-- case:chk-screen --> | Won hard level 12 with the golden pin pulled | ✅ The board above | [^s2] |
| No own entry: shown on the post-win league board and as a wand counter under the pins counter in the map league panel (0 before level 12) <!-- case:chk-entry --> | Looked at the map after the level 11 and 12 wins | ✅ Wand counter 0, then 1 | [^s4] [^s1] |
| One golden pin adds 5 to the league Total Score: 45 pins + 1 golden = 50; after level 13, 49 + 1 golden = 54 <!-- case:chk-effect --> | Won level 12; finished level 13 (its league board seen as the session ended) | ✅ +5 per golden pin | [^s2] [^s5] |
| Shown on the league board (Golden Pins) and the map league panel (wand counter); started at 0, 1 after hard level 12, still 1 after level 13 <!-- case:chk-balance --> | Won level 12; finished level 13 (its league board seen as the session ended) | ✅ 0 → 1 → 1 | [^s5] |
| Why it appeared <!-- case:chk-appeared --> | Played hard level 12 | ✅ The golden pin on level 12, the Golden Pins box after the win | [^s1] |
| Sources <!-- case:chk-sources --> | Pulled one golden pin | not verified: one pulled golden pin gave 1; the +5 video not taken | |
| Sinks <!-- case:chk-sinks --> | — | not verified | |
| At zero <!-- case:chk-empty --> | — | not verified | |
| Refill timer <!-- case:chk-refill --> | — | not verified | |

## Not verified

- What the +5 golden pins video gives: whether the Golden Pins box and the Total Score grow by 5 and 25 <!-- case:video-plus-5 -->
- Sources: every way to get golden pins beyond one pulled golden pin and the +5 video; on which levels golden pins appear <!-- case:chk-sources -->
- Sinks: whether golden pins are ever spent, or only scored in the league <!-- case:chk-sinks -->
- At zero: nothing is lost at 0 as far as seen; what happens when the league week ends <!-- case:chk-empty -->
- Refill timer: none seen <!-- case:chk-refill -->

[^s1]: session 20261004-005453-chrono-2FYKPJ, step 12 — [video at 10:56](https://youtu.be/rH_NzK3D4WA?t=656)
[^s2]: session 20261004-005453-chrono-2FYKPJ, step 9 — [video at 8:17](https://youtu.be/rH_NzK3D4WA?t=497)
[^s3]: session 20261004-005453-chrono-2FYKPJ, step 7 — [video at 6:48](https://youtu.be/rH_NzK3D4WA?t=408)
[^s4]: session 20261004-005453-chrono-2FYKPJ, step 6 — [video at 5:59](https://youtu.be/rH_NzK3D4WA?t=359)
[^s5]: session 20261004-005453-chrono-2FYKPJ, step 17 — [video at 12:15](https://youtu.be/rH_NzK3D4WA?t=735)
[^s2]: session 20261004-005453-chrono-2FYKPJ, step 9 — [video at 8:17](https://youtu.be/rH_NzK3D4WA?t=497)
[^s7]: session 20261004-005453-chrono-2FYKPJ, step 10 — [video at 8:49](https://youtu.be/rH_NzK3D4WA?t=529)
