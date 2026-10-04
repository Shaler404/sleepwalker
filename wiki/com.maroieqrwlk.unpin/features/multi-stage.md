---
game: com.maroieqrwlk.unpin
title: "Multi Stage Level"
type: feature
feature: multi-stage
version_seen: 241.5.1
verified_at: 2026-10-03
sources: [20261003-203702-chrono-2FYKPJ, 20261003-211035-chrono-2FYKPJ, 20261003-214021-chrono-2FYKPJ]
---

# Multi Stage Level

A level made of several pin-pull boards in a row. Levels 5 and 10 had four stages each [^s4]
[^s8]; each board is solved on its own,
a "Stage Completed!" banner follows, and the level counts as won after the last stage [^s4] [^s6]. On the map
these levels have a yellow ring, a ! badge and a "Multi Stage Level" label [^s5].

## Why it appeared

Level 5 (4 stages), map label on L5/L6/L10 [^s1].

## Where to find it

The map: a level node with a yellow ring and a purple ! badge, with a "Multi Stage Level" speech bubble beside
it (levels 5, 10, 15, 16) [^s5] [^s2]. It has no entry of its own: it is played with **Play!** like any
level [^s3] [^s10]. At level 10 the map's only "Multi Stage Level" bubble sat by level 16, not level 15 [^s10].

![Map: the Multi Stage Level label next to level 5 (and level 10)](../img/20261003-multi-stage-entry-8cb2cb37.webp) [^s2]
*The map before level 4: levels 5 and 10 with a yellow ring and a ! badge, "Multi Stage Level" labels beside them*

## What it looks like

![Level 5, stage 1: the Stage column at the right edge, one current and three locked stages](../img/20261003-multi-stage-screen-c8b449b3.webp) [^s3]
*Level 5, stage 1: the level number with a yellow ring and ! badge; the Stage column at the right edge*

The level screen of a usual level, plus a **Stage** column at the right edge under the ADS button: one icon
per stage, the current stage as a figure, the next stages with locks [^s3]. The level number in the top bar
carries the same yellow ring and ! badge as on the map [^s3]. Done stages turn into green ticks; the last
stage's box shows a figure, inferred to be a boss stage [^s11].

![Level 5, stage 4: three stages ticked in the Stage column, the last one current](../img/20261003-multi-stage-outcome-win-c3b448b7.webp) [^s7]
*Level 5 after stage 3: "Stage Completed!" over the board, three green ticks in the Stage column, stage 4 next*

## How it works

Version 241.5.1.

- Level 5 had four stages, each a separate board with its own pins and cup [^s4] [^s6].
- When a stage's balls are in the cup the banner "Stage Completed!" shows, the stage's icon turns into a green
  tick and the next board comes [^s7].
- The whole level took 147 s; all four stages were solved on the first try [^s4].
- Level 10 had four stages too, all won on the first try in 306 s, including two interstitial video ads
  that came after stages 1 and 3 [^s8] (see
  [Interstitial video ad](interstitial.md)).
- The number of stages of a level is not fixed: level 10 was known with three stages from an earlier
  play and had four this time, in version 241.5.1
  [^s8]. The Stage column on the level screen shows the count.
- Stage progress is kept: a restart reloads only the current stage, and a quit to the map or an app exit
  keeps the stages already done; level 10 reopened at stage 4 with stages 1-3 ticked each time [^s11] [^s12]
  [^s13].
- No loss was seen, so what a lost stage costs (the stage or the whole level) is unknown.

![Level 5, stage 1: the right pin is pulled and the balls run into the cup, 0% to 90%](../clips/20261003-level5-stage1-to-stage2.webp) [^s6]
*Clip 3.7 s · [original on YouTube from 3:37](https://youtu.be/cirqlD7KGWI?t=217); stage 1 solved with one pin*

## Outcomes

| Outcome | As the base or what differs | Frame |
|---|---|---|
| win <!-- case:under-win --> | Differs: the usual "Level completed!" screen after the last stage (+23 coins, gift bar 62%), plus the x2-x5 video coin multiplier, first seen here [^s4]; after level 10 the flow was Puzzle Piece Found, the Bronze League leaderboard, then "Incredible! Level completed!" (+19 coins) with the multiplier again [^s8] [^s9] | ![win](../img/20261003-multi-stage-result-bbb6c2e0.webp) |
| restart <!-- case:under-restart --> | Differs: the base's "You can do better!" popup and interstitial, then only the current stage reloads; earlier stages stay ticked (level 10, stage 4) [^s11] | ![restart: stage 4 reloaded, stages 1-3 ticked](../img/20261003-multi-stage-outcome-restart-891ee138.webp) |
| quit <!-- case:under-quit --> | As the base (the back arrow, map at once, no cost), plus: Play! reopens the level at the same stage, stages done kept [^s12] | ![quit: the map, level 10 still current](../img/20261003-daily-rewards-entry-cdb2ec35.webp) |
| exit app <!-- case:under-exit-app --> | Stage progress survives: level 10, left at stage 4 in the previous session, opened at stage 4 with stages 1-3 ticked after the app was closed and relaunched [^s13] | ![exit app: level 10 at stage 4 after a relaunch](../img/20261003-multi-stage-outcome-exit-app-891ee178.webp) |
| balls fell out <!-- case:under-balls-out --> | not verified: the "Balls fell out of the level!" loss was seen so far only on level 11, an ordinary level (see [Pin-pull level](core-level.md#level-failed)) | — |

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Map node with a yellow ring, a ! badge and a 'Multi Stage Level' speech bubble (L5, L10, L15, L16) <!-- case:chk-announce --> | Looked at the map | ✅ Seen | [^s5] |
| Several boards in a row in one level (L5: 4 stages), each solved separately; the level is won after the last stage <!-- case:chk-differs --> | Played level 5 | ✅ Four stages | [^s4] |
| Same 'Level completed' screen after the last stage; L5 win +23 coins with the x2-x5 video multiplier offer <!-- case:chk-win --> | Won level 5 | ✅ As the base plus the multiplier | [^s4] |
| Why it appeared <!-- case:chk-appeared --> | Won level 4 | ✅ Level 5 | [^s1] |
| No own entry: a map node with a yellow ring and a 'Multi Stage Level' bubble, opened by Play! <!-- case:chk-entry --> | Played levels 5 and 10 from Play! | ✅ The marked node on the map | [^s10] |
| Level screen with a Stage column on the right (ticked stages, the last one a boss) <!-- case:chk-screen --> | Played levels 5 and 10 | ✅ The Stage column, frames above | [^s11] |
| Map tooltip 'Multi Stage Level' next to L16 (not L15) <!-- case:map-label-l16 --> | Looked at the map at level 10 | ✅ The bubble by level 16; the every-5th-level guess may be wrong | [^s10] |
| L10 had 4 stages this time (the board library had 3 for it): the stage count of a level is not fixed between installs or versions <!-- case:stage-count-varies --> | Played level 10 | ✅ Four stages | [^s8] |
| Each loss <!-- case:chk-loss --> | — | not verified: no stage lost |  |
| Retry and continue offers <!-- case:chk-retry --> | — | not verified |  |
| Where and how often it comes up <!-- case:chk-frequency --> | Looked at the map | not verified: levels 5, 10, 15, 16 marked; no rule known |  |

## Not verified

- Each loss: the fail screen and whether a lost stage costs the whole level <!-- case:chk-loss -->
- Retry and continue offers after a lost stage; whether a retry starts at the same stage <!-- case:chk-retry -->
- Where and how often it comes up: levels 5 and 10 so far; the guess "every 5th level" is to be checked at L15, L16 and L20 <!-- case:chk-frequency -->
- Whether the coin multiplier comes with every Multi Stage win (levels 5 and 10: yes).
- What decides a level's stage count (level 10: three stages before, four now).
- Balls fell out under a Multi Stage level: as the base, or what differs <!-- case:under-balls-out -->

[^s1]: session 20261003-203702-chrono-2FYKPJ, step 19 — [video at 6:01](https://youtu.be/cirqlD7KGWI?t=361)
[^s2]: session 20261003-203702-chrono-2FYKPJ, step 7 — [video at 2:10](https://youtu.be/cirqlD7KGWI?t=130)
[^s3]: session 20261003-203702-chrono-2FYKPJ, step 12 — [video at 3:24](https://youtu.be/cirqlD7KGWI?t=204)
[^s4]: session 20261003-203702-chrono-2FYKPJ, step 18 — [video at 5:47](https://youtu.be/cirqlD7KGWI?t=347)
[^s5]: session 20261003-203702-chrono-2FYKPJ, step 5 — [video at 1:43](https://youtu.be/cirqlD7KGWI?t=103)
[^s6]: session 20261003-203702-chrono-2FYKPJ, step 13 — [video at 3:40](https://youtu.be/cirqlD7KGWI?t=220)
[^s7]: session 20261003-203702-chrono-2FYKPJ, step 17 — [video at 5:11](https://youtu.be/cirqlD7KGWI?t=311)

[^s8]: session 20261003-211035-chrono-2FYKPJ, step 14 — [video at 6:19](https://youtu.be/Mpfk4cqdltQ?t=379)
[^s9]: session 20261003-211035-chrono-2FYKPJ, step 16 — [video at 6:59](https://youtu.be/Mpfk4cqdltQ?t=419)
[^s10]: session 20261003-214021-chrono-2FYKPJ, step 30 — [video at 7:39](https://youtu.be/siJO2QCuGxI?t=459)
[^s11]: session 20261003-214021-chrono-2FYKPJ, step 29 — [video at 7:04](https://youtu.be/siJO2QCuGxI?t=424)
[^s12]: session 20261003-214021-chrono-2FYKPJ, step 24 — [video at 5:37](https://youtu.be/siJO2QCuGxI?t=337)
[^s13]: session 20261003-214021-chrono-2FYKPJ, step 21 — [video at 4:51](https://youtu.be/siJO2QCuGxI?t=291)
