---
game: com.oakever.akari
title: "How to play"
type: agent
version_seen: 1.0.2
verified_at: 2026-10-01
sources: [20261001-003641-chrono-2FYKPJ, 20261001-024647-chrono-2FYKPJ, 20261001-035425-chrono-2FYKPJ]
---

# How to play: MeowTrail

The player reads this before every level and works in the local copy `state/com.oakever.akari/playbook.md`;
the dream merges it here. Level times: `sw.py playbook`.

## akari: Cat placement (Light Up rules)
- Goal: every white cell occupied (paw-tinted or holding a cat). The counter "0/N" is the exact number
  of cats in the solution [s:20261001-003641-chrono-2FYKPJ#10].
- Controls: DOUBLE TAP places a cat; a single tap marks an X. `sw.py taps "X,Y:2 ..."` sends real
  double taps. Boosters under the grid: cat (247,1305) places one correct cat; bulb (482,1305) shows
  the next deduction, Apply places it [s:20261001-003641-chrono-2FYKPJ#26] [s:20261001-003641-chrono-2FYKPJ#28].
- Rules: a cat occupies its row and column up to a wall; two cats never see each other. Numbered
  tiles are walls, the number = cats in the 4 neighbours. Boxes (level 11+) are walls without a
  number. The game checks each cat against its own solution: a wrong double tap costs 1 of 3 hearts
  and leaves a red X. Hearts reset every level [s:20261001-003641-chrono-2FYKPJ#29].
- Risks: a misread board = wrong cats = hearts; the solver returns the first solution it finds, so a
  misread board with several solutions is not caught.
- Method: solver [`solvers/com.oakever.akari/akari.py`](../../../solvers/com.oakever.akari/akari.py) (backtracking Light Up
  with the cat count). Read the board by hand into JSON rows: '.' empty, '0'-'4' numbered wall, '#'
  box (and any cell outside an irregular board), 'C' cat already placed; pass "count" from the
  counter and the cell centres in frame pixels (730x1583 frame):
  - 6x6: x 81,195,308,422,535,649; y 545,659,772,886,999,1113
  - 7x7: x 73,170,267,364,461,558,656; y 537,634,731,828,925,1022,1119
  - 8x8: x 66,151,236,321,406,491,576,662; y 530,615,700,785,870,955,1040,1125
  - 9x9: x 62,138,213,289,365,440,516,592,667; y 525,600,676,752,828,903,979,1055,1130
  - 10x10: x 58,126,194,262,330,398,466,534,602,670; y 519,587,655,723,791,859,927,995,1063,1131

  Run `sw.py solve akari --board FILE --run`: it returns `[x, y, 2]` double taps.
- Level plan: tap "Level N" (364,1285), take a frame and look at it (an ad may be up), read the board
  once, solve, send all taps, then "Level N+1".
- Pitfalls:
  - Every row string must have the grid's length and boxes go by their x centre: two misreads put a
    box in the wrong column ("no solution: board misread?") [s:20261001-035425-chrono-2FYKPJ#30] [s:20261001-035425-chrono-2FYKPJ#44].
  - Do not send the ad skip taps blind: on a level without an ad (85,107) is the back arrow and
    (690,107) the gear [s:20261001-035425-chrono-2FYKPJ#46] [s:20261001-035425-chrono-2FYKPJ#47].
  - Interstitials: see [the ads page](../features/ads-interstitial.md); Next at the top left, then
    `launch` from the Play Store.

### Level times
| Levels | Result | Median | Range | Model | Source |
|---|---|---|---|---|---|
| tutorial–18 | 19 won | 22 s | 15–58 s (58 s: booster demo; 41 s: deliberate wrong cat) | opus | [s:20261001-003641-chrono-2FYKPJ#37] |
| 19–48 | 30 won | 20 s | 16–29 s | sonnet | [s:20261001-024647-chrono-2FYKPJ#109] |
| 49–55 | 7 won | 29 s | 22–271 s (49: fail/revive/booster tests; 51: Restart test) | sonnet | [s:20261001-035425-chrono-2FYKPJ#61] |

Ads take most of the wall time: about 40% of session 2 [s:20261001-024647-chrono-2FYKPJ#109].
