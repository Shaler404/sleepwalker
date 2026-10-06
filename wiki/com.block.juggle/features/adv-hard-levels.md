---
game: com.block.juggle
title: "Adventure hard levels (Next Hard Level)"
type: feature
feature: adv-hard-levels
version_seen: 10.8.1
verified_at: 2026-10-05
sources: [20261005-004506-chrono-2FYKPJ, 20261005-015205-chrono-2FYKPJ]
---

# Adventure hard levels (Next Hard Level)

Some Adventure levels are flagged "hard". The flag is shown in one place only: the win screen of the
level before, whose button reads "Next Hard Level" (purple) instead of "Next Level" (green). The only
hard level seen so far is level 5. It is a [gem-collection level](adv-diamonds.md) with the same rules
as levels 2 to 4, but with larger goals: 28, 26 and 26 gems against 22, 20 and 20 on level 4 [^s1] [^s3].

## Why it appeared

After Adventure level 4 was won, the win screen's button read "Next Hard Level" (purple) instead of the
green "Next Level", which flags level 5 as hard [^s1].

## Where to find it

Home menu > Adventure > the green "Level 5" button at the bottom of the Adventure map. On the map, cell 5
looks like any other current cell, with no hard mark. The button reads "Level 5", not "Hard" [^s2].

![The Adventure map: a 96-cell trophy-shaped grid, cells 1-4 done, cell 5 current, the green Level 5 button at the bottom](../img/20261005-adv-hard-levels-entry-ee13c668.webp) [^s2]
*The green Level 5 button at the bottom of the Adventure map; cell 5 has no hard mark*

## What it looks like

Level 5 opens with the same "Target Collection" banner as the other gem levels. The header then shows
three goals: 28 blue diamonds, 26 yellow stars and 26 red gems. The pre-built layout is a symmetrical
shape of yellow and cyan blocks with six gem tiles in its centre. The first tray held a 2x2 piece and two
3x3 pieces, all with gem cells. There is no "hard" label, colour or icon in the level: the back arrow,
gear and goal counters look the same as on level 4 [^s3].

![Hard level 5 at the start: goals 28, 26 and 26 in the header, the pre-built centre pattern with gem tiles, a 2x2 and two 3x3 pieces in the tray](../img/20261005-adv-hard-levels-screen-cf9e3061.webp) [^s3]

### Result

When the last goal was met, all three counters showed green checks while a 1x2 piece was still in the
tray. A rainbow sweep then ran across the board [^s5].

![The last clear on level 5: the red gem counter turns into a check, then a rainbow sweep fills the board from top to bottom](../clips/20261005-hard-level-final-clear.webp) [^s5]
*Clip 7.2 s · [original on YouTube from 3:04](https://youtu.be/a20Ukrexpfs?t=184)*

A full-screen interstitial ad came next: a video for another game, then an end card with no close
button, which the Back key closed. After it came the win screen: the Consecutive Victories panel at x4,
the three gems with checks, "Well Done!" and a green "Next Level" button. Level 6 is therefore not
flagged hard [^s4].

![The level 5 win screen: Consecutive Victories x4, the three gems checked, Well Done!, the green Next Level button](../img/20261005-adv-hard-levels-result-d39392c3.webp) [^s4]

## How it works

Version 10.8.1.

| Level | Hard | Goals |
|---|---|---|
| 4 | no | 22 blue diamonds, 20 orange gems, 20 yellow stars |
| 5 | yes | 28 blue diamonds, 26 yellow stars, 26 red gems |
| 6 | no (offered as "Next Level") | not opened |

[^s1] [^s3]

- Rules seen on level 5 are the gem-level rules: a gem is collected when its row or column is cleared.
  There was no move limit, timer, lives or booster [^s3] [^s4].
- Late in the level, the tray pieces were made only of gem cells (for example a 1x2 piece of two red
  gems) [^s5].
- Level 5 was won in about 1.5 minutes of play over eight trays, plus the ad, by the same placing method
  that won level 4 in about 5 minutes. Inferred: the larger goals did not make it slower to win [^s4].
- No reward for a hard level was seen: the win screen is the same as for other levels [^s4].

## Outcomes

The base level is the Adventure [gem-collection level](adv-diamonds.md) on the 8x8 board of Classic.

| Outcome | As the base or what differs | Frame |
|---|---|---|
| Restart: gear > Replay <!-- case:under-restart --> | not verified | — |
| No Space Left: no tray piece fits <!-- case:under-no-space-left --> | not verified | — |
| Win <!-- case:under-win --> | Same as the base gem level: the counters turn into checks, an interstitial ad, then the win screen with Consecutive Victories (x4) and a green Next Level. No extra reward [^s4] | ![The level 5 win screen](../img/20261005-adv-hard-levels-result-d39392c3.webp) |
| Quit: gear > Home or the back arrow <!-- case:under-quit --> | not verified | — |
| Leaving the app <!-- case:under-exit-app --> | not verified | — |

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared <!-- case:chk-appeared --> | Won Adventure level 4 | ✅ The win screen's button read "Next Hard Level" (purple) in place of the green "Next Level" | [^s1] |
| How it is announced <!-- case:chk-announce --> | Looked at the level 4 win screen and the map | ✅ Only the purple "Next Hard Level" button on the level before; map cell 5 has no hard mark | [^s1] |
| Where to find it <!-- case:chk-entry --> | Home menu > Adventure > Level 5 | ✅ The green Level 5 button on the map, as for any level | [^s2] |
| Its screen <!-- case:chk-screen --> | Opened level 5 | ✅ Target Collection banner, goals 28 blue diamonds, 26 stars, 26 red gems; no hard marker in the level | [^s3] |
| What differs from the base level <!-- case:chk-differs --> | Played level 5 to the win | ✅ Three gem goals with larger counts (28/26/26 against 22/20/20 on level 4), a pre-built centre pattern, 3x3 pieces in the tray; no extra rules | [^s4] |
| Its win <!-- case:chk-win --> | Won level 5 | ✅ "Well Done!", three green checks, Consecutive Victories x4, a green Next Level; an interstitial ad before the win screen | [^s4] |
| Its loss <!-- case:chk-loss --> | — | not verified: level 5 was won on the first try |  |
| Retry and continue offers <!-- case:chk-retry --> | — | not verified: no loss |  |
| Where and how often it comes up <!-- case:chk-frequency --> | — | not verified: of levels 1 to 6, only level 5 is flagged hard |  |

## Not verified

- A loss on a hard level: its fail screen and what it costs <!-- case:chk-loss -->
- Retry and continue offers after a loss on a hard level, and their price <!-- case:chk-retry -->
- Which later levels are hard; so far only level 5 of levels 1 to 6 <!-- case:chk-frequency -->
- Gear > Replay on a hard level <!-- case:under-restart -->
- No Space Left on a hard level <!-- case:under-no-space-left -->
- Quitting a hard level with gear > Home or the back arrow <!-- case:under-quit -->
- Leaving the app in a hard level and coming back <!-- case:under-exit-app -->

[^s1]: session 20261005-004506-chrono-2FYKPJ, step 23 — [video at 6:03](https://youtu.be/pwB69H7MFAc?t=363)
[^s2]: session 20261005-015205-chrono-2FYKPJ, step 10 — [video at 1:42](https://youtu.be/a20Ukrexpfs?t=102)
[^s3]: session 20261005-015205-chrono-2FYKPJ, step 11 — [video at 1:56](https://youtu.be/a20Ukrexpfs?t=116)
[^s4]: session 20261005-015205-chrono-2FYKPJ, step 21 — [video at 5:44](https://youtu.be/a20Ukrexpfs?t=344)
[^s5]: session 20261005-015205-chrono-2FYKPJ, step 18 — [video at 3:06](https://youtu.be/a20Ukrexpfs?t=186)
