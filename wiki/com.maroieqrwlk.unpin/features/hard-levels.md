---
game: com.maroieqrwlk.unpin
title: "Hard levels (skull node)"
type: feature
feature: hard-levels
version_seen: 241.5.1
verified_at: 2026-10-04
sources: [20261003-203702-chrono-2FYKPJ, 20261004-001002-chrono-2FYKPJ, 20261004-005453-chrono-2FYKPJ]
---

# Hard levels (skull node)

Levels marked on the map with a red ring and a skull badge (levels 7, 12, 17; level 14 with a flame skull)
[^s1]. The two played, levels 7 and 12, were pin-pull boards like the others, opened with **Play!**,
level 12 with no warning, and both were won on the first try with the same win screens as any level [^s4] [^s7]. No rule
of their own was seen: no timer, no move limit [^s3] [^s7]. Level 12 carried a golden pin that scores in the
league ([Golden pins](golden-pins.md)) [^s6].

## Why it appeared

Map tutorial after the L3 win: skull badges on L7 and L12 (red ring); L14 has a flame skull [^s1].

## Where to find it

The map: a level node with a red ring and a skull badge at its lower right [^s1] [^s2] [^s5]. It is played like
any level, with **Play!** when it is the next level [^s3]. When the marked level becomes the current one, its
node on the map is the large green current circle with no skull badge (level 12 after the level 11 win) [^s9].

![Map: level 7 node with a red ring and a flame-skull badge (level 12 has a grey skull badge)](../img/20261003-hard-levels-entry-8cb2cb37.webp) [^s2]
*The map before level 7: level 7 with a red ring and a red skull badge; level 12 with a grey skull badge*

![Map at level 10: levels 12 and 17 with a red ring and a grey skull badge, level 14 with a red ring and a flame skull](../img/20261004-hard-levels-entry-95e225ed.webp) [^s5]
*The map at level 10, Play! at the bottom: the next marked nodes are 12 and 17 (grey skull) and 14 (flame skull); the player's name in the league banner blacked out*

## What it looks like

![Level 7 board: the level number in the top bar has a red ring and a flame-skull badge; the board itself looks like a normal level](../img/20261003-hard-levels-screen-ccb548b6.webp) [^s3]
*Level 7: the level number in the top bar has a red ring and the skull badge; the board is a usual pin-pull board*

![Level 12 board: the header circle 12 with a red ring and a skull badge; coloured and grey balls in a slanted tube held by a golden star pin, a bomb on a pin at the right](../img/20261004-hard-levels-screen-d625da21.webp) [^s6]
*Level 12: the header circle 12 has a red ring and the skull badge; a golden star pin holds the grey balls, a bomb sits on the right pin (a banner ad blacked out)*

On the level screen only the level number in the top bar carries the mark: a red ring and the skull badge
[^s3] [^s6]. Level 12 opened straight from Play! with no popup or warning before the board [^s7]. Level 7: four
compartments of coloured balls at the top, grey balls in two funnels under them, pins on the sides and two
crossed pins over the cup [^s3]. Level 12: coloured balls over grey ones in a slanted tube, held by a golden
pin with a star head; a vertical pin and a slanted pin with a bomb on the right [^s6]. No timer, move limit
or other rule was shown on either [^s3] [^s6].

### Result

![Level 12 completed: Phenomenal!, +20 coins (294), gift box at 44%, Tap to continue](../img/20261004-hard-levels-result-be78c6c0.webp) [^s8]
*After the level 12 win: "Phenomenal! Level completed!", +20 coins (294), the gift box at 44%, Tap to continue*

## How it works

Version 241.5.1.

- Marked levels seen on the map: 7, 12, 17 (red ring, skull badge); 14 (flame skull) [^s1]. At level 10 the
  map still shows 12 and 17 with a grey skull and 14 with a flame skull [^s5]. The skull levels are 5 apart
  (7, 12, 17); that the step continues is inferred, not verified [^s7].
- Level 7 was won on the first try in 41 s: the top pin, a pause of about 6 s, then the crossed pins [^s4].
- Level 12 was won on the first try in 97 s with two pulls: a plain pin, then the golden pin [^s7].
- After the level 7 win: the Pull Fest leaderboard (Pins 6), then "Level completed!" with +24 coins and the
  gift bar at 85%, then an interstitial video ad, as after level 6 [^s4].
- After the level 12 win: the Bronze League board (Pins 45, Golden Pins 1, Total Score 50, a video for +5
  golden pins left of Next Level!), then "Phenomenal! Level completed!" with +20 coins (294) and the gift box
  at 44%, then an interstitial [^s7] [^s8]. The normal level 11 just before gave +25 coins and the gift box
  went 32% → 44% over one win [^s8].
- No extra reward for a hard level was seen: level 12 gave fewer coins than the normal level 11 [^s8].

## Outcomes

| Outcome | As the base or what differs | Frame |
|---|---|---|
| win <!-- case:under-win --> | As the base: the league board, then "Level completed!" (level 7: +24 coins, gift bar 85%; level 12: +20 coins, gift box 44%), then the interstitial [^s4] [^s8] | ![win](../img/20261003-hard-levels-outcome-win-bfc75185.webp) |
| restart <!-- case:under-restart --> | not verified | — |
| quit <!-- case:under-quit --> | not verified | — |
| exit app <!-- case:under-exit-app --> | not verified | — |
| balls fell out <!-- case:under-balls-out --> | not verified: the "Balls fell out of the level!" loss was seen so far only on level 11, an ordinary level (see [Pin-pull level](core-level.md#level-failed)) | — |

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Red ring and a skull badge on the map node (L7, L12, L17); L14 and once L7 a flame skull <!-- case:chk-announce --> | Looked at the map | ✅ Seen | [^s1] |
| Why it appeared <!-- case:chk-appeared --> | Won level 3, the map appeared | ✅ Skull badges on the first map | [^s1] |
| Where to find it <!-- case:chk-entry --> | Played level 7 from Play!; looked at the map at level 10 | ✅ The skull node on the map, played with Play! | [^s2] [^s5] |
| What it looks like: level 12 opens straight from Play with no popup or warning; only the header node 12 has a red ring and skull badge; the board looks like a normal level (2 pulls) <!-- case:chk-screen --> | Played levels 7 and 12 | ✅ The level 7 and level 12 screens above | [^s3] [^s7] |
| Level 12 plays like a base level: same pins, cup, no timer or move limit; the difficulty is only the board <!-- case:chk-differs --> | Played levels 7 and 12 | ✅ No rule of its own; both won first try | [^s7] |
| Its win: level 12 won with the same win flow as the base (league board → Next Level); the golden pin added Golden Pins 1 (score 50 = 45 pins + 5) and a video offer +5 golden pins <!-- case:chk-win --> | Won levels 7 and 12 | ✅ The same win screens as a usual level; +24 and +20 coins | [^s4] [^s7] |
| Where and how often it comes up: skull nodes at L7, L12, L17 (every 5 levels from 7); flame skull at L14 <!-- case:chk-frequency --> | Looked at the map | ✅ Levels 7, 12, 17 and 14; the step beyond 17 inferred | [^s1] [^s5] [^s7] |
| Each loss <!-- case:chk-loss --> | — | not verified: no hard level lost |  |
| Retry and continue offers <!-- case:chk-retry --> | — | not verified |  |

## Not verified

- Each loss: the fail screen and what it costs <!-- case:chk-loss -->
- Retry and continue offers after a loss <!-- case:chk-retry -->
- Restart under a hard level: as the base, or what differs <!-- case:under-restart -->
- Quit under a hard level: as the base, or what differs <!-- case:under-quit -->
- Exit the app under a hard level: as the base, or what differs <!-- case:under-exit-app -->
- Balls fell out under a hard level: as the base, or what differs <!-- case:under-balls-out -->
- The difference between the grey skull and the flame skull badges (level 14 not played yet).
- Whether skull levels keep coming every 5 levels after 17.

[^s1]: session 20261003-203702-chrono-2FYKPJ, step 6 — [video at 1:57](https://youtu.be/cirqlD7KGWI?t=117)
[^s2]: session 20261003-203702-chrono-2FYKPJ, step 7 — [video at 2:10](https://youtu.be/cirqlD7KGWI?t=130)
[^s3]: session 20261003-203702-chrono-2FYKPJ, step 31 — [video at 11:17](https://youtu.be/cirqlD7KGWI?t=677)
[^s4]: session 20261003-203702-chrono-2FYKPJ, step 32 — [video at 11:54](https://youtu.be/cirqlD7KGWI?t=714)
[^s5]: session 20261004-001002-chrono-2FYKPJ, step 0 — [video at 0:00](https://youtu.be/el_4Pddjvvk?t=0)
[^s6]: session 20261004-005453-chrono-2FYKPJ, step 7 — [video at 6:48](https://youtu.be/rH_NzK3D4WA?t=408)
[^s7]: session 20261004-005453-chrono-2FYKPJ, step 9 — [video at 8:17](https://youtu.be/rH_NzK3D4WA?t=497)
[^s8]: session 20261004-005453-chrono-2FYKPJ, step 10 — [video at 8:49](https://youtu.be/rH_NzK3D4WA?t=529)
[^s9]: session 20261004-005453-chrono-2FYKPJ, step 6 — [video at 5:59](https://youtu.be/rH_NzK3D4WA?t=359)
