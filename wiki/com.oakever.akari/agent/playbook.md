---
game: com.oakever.akari
title: "How to play"
type: agent
version_seen: 1.0.2
verified_at: 2026-10-02
sources: [20261001-003641-chrono-2FYKPJ, 20261001-024647-chrono-2FYKPJ, 20261001-035425-chrono-2FYKPJ, 20261001-091349-chrono-2FYKPJ, 20261001-100940-chrono-2FYKPJ, 20261001-143237-chrono-2FYKPJ, 20261001-171336-chrono-2FYKPJ, 20261001-171804-chrono-2FYKPJ, 20261001-172422-chrono-2FYKPJ, 20261001-173851-chrono-2FYKPJ, 20261001-174614-chrono-2FYKPJ, 20261001-175856-chrono-2FYKPJ, 20261001-221517-chrono-2FYKPJ]
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
- Risks: a misread board = wrong cats = hearts. The solver reads the board itself and refuses (no
  taps) unless the reading is complete and exactly one solution agrees with the counter, so a refusal
  costs time, never a heart.
- Method: solver [`solvers/com.oakever.akari/akari.py`](../../../solvers/com.oakever.akari/akari.py) (local draft
  `state/com.oakever.akari/solvers/akari.py`, which `sw.py` runs first). It reads the board from the
  frame: grid 3x3 to 12x12, numbered walls 0-4 (by digit colour), boxes, cells outside an irregular
  board (walls), cats already placed, red and grey X marks, and the counter "k/N". It solves Light Up
  exactly and double-taps every missing cat. Nothing to type.
  - Run: `sw.py solve akari --run --rounds 3`. Round 1 sends all double taps; round 2 reads the board
    again: "all cats are placed: the level is done" or the win screen ("the win screen: the counter reads
    N/N under the veil"); both end the run as "solved" (from 2026-10-03; before, the win screen was a
    refusal and every won run was logged as given up). A cat lost in round 1 is placed in round 2: one of 13-25 double taps was dropped on
    levels 89, 96, 102 and 109, and round 2 placed it in about 3 s [s:20261001-172422-chrono-2FYKPJ#8]
    [s:20261001-173851-chrono-2FYKPJ#6] [s:20261001-174614-chrono-2FYKPJ#11] [s:20261001-221517-chrono-2FYKPJ#7].
  - Verified on the phone: levels 83-120 (7x7 to 12x12, Hard 19-cat boards, 25-cat 12x12) won with one
    `solve` call each, by haiku, sonnet and opus alike [s:20261001-171804-chrono-2FYKPJ#2]
    [s:20261001-174614-chrono-2FYKPJ#11] [s:20261001-221517-chrono-2FYKPJ#41].
  - Tutorial (fresh install, two scripted boards under a grey veil): `sw.py solve akari --run --rounds 5`
    double-taps the cell(s) the game leaves bright (3x3: (2,2), then (1,1), then (3,3); 4x4: the four
    cells around the "4" at once, then (4,4)) and stops as "solved" on the finished board with "Got it!".
    Tap "Got it!" (364,1425), run it again on the second board, tap "Got it!" (364,1430): level 1 opens.
    It taps only bright cells, never a dimmed one; with no bright cell (a hint still coming) it refuses.
  - It refuses with a note when the frame is not a settled board: an ad, a popup, the home screen, the
    fail screen, the "Hard" banner, the board still appearing (cells growing, boxes dropping), the bulb
    booster's hint (veiled page with an orange "Apply": the note says to tap Apply (364,1348) and run it
    again), the fail screen "Almost!" (the note names the free green Restart (364,1285)), a whole screen
    dimmed evenly by the phone (below), a reading with 0 or 2+ solutions, or a counter that disagrees. Fix what the note says (wait, close the popup,
    skip the ad) and run it again.
  - Fallback when it refuses a settled, clean board twice: write the board as JSON and run
    `sw.py solve akari --board FILE --run`. Rows: '.' empty, '0'-'4' numbered wall, '#' box or cell
    outside the board, 'C' cat already placed; "count" from the counter; cell centres in frame pixels
    (730x1583 frame):
    - 6x6: x 81,195,308,422,535,649; y 545,659,772,886,999,1113
    - 7x7: x 73,170,267,364,461,558,656; y 537,634,731,828,925,1022,1119
    - 8x8: x 66,151,236,321,406,491,576,662; y 530,615,700,785,870,955,1040,1125
    - 9x9: x 62,138,213,289,365,440,516,592,667; y 525,600,676,752,828,903,979,1055,1130
    - 10x10: x 58,126,194,262,330,398,466,534,602,670; y 519,587,655,723,791,859,927,995,1063,1131
- Level plan: tap the orange button at its centre: "Level N+1" on the win screen (364,1285), "Level N"
  on Home (364,1340) [s:20261001-171336-chrono-2FYKPJ#1] [s:20261001-175856-chrono-2FYKPJ#14];
  `sw.py wait 2` and look at the frame (an ad may be up: skip it first, see Ads below);
  `sw.py level start "level N" --mechanic akari --plan "solver"`; `sw.py solve akari --run
  --rounds 3`; on "solved" or the win screen take a shot and confirm the win screen with the counter at
  N/N, `level end won`, then the next level button. On any other stop, read the note, fix it and run
  `solve` again. Every won level needs its own `level end won` before the next `level start`.
- Pitfalls:
  - The win screen's counter is read under its dark veil: "done" needs N/N there. A dimmed screen with
    k/N, k < N (a popup, the fail screen) is a refusal that names the counter
    [s:20261003-200925-chrono-2FYKPJ#10].
  - Run the solver only on a settled board: right after "Level N" or an ad the cells grow in and boxes
    drop [s:20261001-024647-chrono-2FYKPJ#2] [s:20261001-035425-chrono-2FYKPJ#20]
    [s:20261001-024647-chrono-2FYKPJ#86]; the solver then refuses ("none of floor/wall/box", "lit
    cells do not match"): wait 2 s and run it again.
  - A rejected cat plays an animation for about a second (an angry cat, the number next to it flashes
    red, the cell lit without its cat): the solver refuses ("lit cells do not match", "none of
    floor/wall/box"); look again and run it once more [s:20261003-232850-chrono-2FYKPJ#11].
  - The whole screen dimmed evenly, board, bar and ad banner alike, with no popup on it, is the phone, not
    the game: its idle dim or Samsung touch protection (the proximity sensor covered). Game taps, Back and
    `restart` do nothing; level 44 was quit after 433 s of taps on it, read as a "stuck veil after the
    rewarded video". The solver says "the whole screen is dimmed evenly ... not the game" and shows the board
    it reads under the dim; when `sw.py` says touches are blocked, the sensor must be cleared (record the
    session as blocked); do not log the level quit as a solver failure [s:20261006-102842-chrono-2FYKPJ#18].
  - Boosters are not needed with the solver: after the cat booster or the bulb's Apply the solver reads
    the placed cats and places the rest (level 3: 8/9 read, 1 placed) [s:20261003-232850-chrono-2FYKPJ#9].
  - Grey X marks (the bulb's Apply, or a single tap) and red X (a rejected cat) sit on dark cells; the
    solver leaves them alone and lists them in its note [s:20261001-100940-chrono-2FYKPJ#13]
    [s:20261001-091349-chrono-2FYKPJ#13].
  - With the `--board` fallback: every row string must have the grid's length and boxes go by their x
    centre: two misreads put a box in the wrong column ("no solution: board misread?")
    [s:20261001-035425-chrono-2FYKPJ#30] [s:20261001-035425-chrono-2FYKPJ#44].
  - Do not send the ad skip taps blind: on a level without an ad (85,107) is the back arrow and
    (690,107) the gear [s:20261001-035425-chrono-2FYKPJ#46] [s:20261001-035425-chrono-2FYKPJ#47].
  - Log `level end won` only when the counter reads N/N on the win screen: level 63 was logged won at
    11/13 and level 77 after 5 s with 0 moves, before either was solved [s:20261001-091349-chrono-2FYKPJ#13]
    [s:20261001-100940-chrono-2FYKPJ#28].
  - The button misses: Home "Level N" spans about y 1280-1400, the win-screen "Level N+1" about
    y 1225-1345. Taps at y 1430 (Home) and y 1200-1210 (win screen) land just outside and change
    nothing; a session lost 4.3 min and another about 150 s this way. If the frame does not change after
    a tap, compare the tap with the button's bounds before trying anything else
    [s:20261001-171336-chrono-2FYKPJ#11] [s:20261001-175856-chrono-2FYKPJ#13].
  - The win screen is left only by its button: the back arrow, system Back, swipes and taps away do
    nothing; `launch` while the game is in front keeps it; a restart lands on Home
    [s:20261001-175856-chrono-2FYKPJ#11] [s:20261001-175856-chrono-2FYKPJ#14].
  - (364,1290) on a level screen is the empty gap between the two boosters: a tap there does nothing
    [s:20261001-100940-chrono-2FYKPJ#29].
- Ads (see [the ads page](../features/ads-interstitial.md)): an interstitial may come after the level
  button. Look at the frame, then tap the labelled skip: "Next" at the top left (45-85,107), or a
  "Google Play ▸|" pill at the top right (590,120); then `launch` from the Play Store
  [s:20261001-070939-chrono-2FYKPJ#19]. An ad with no skip ends on the Play Store by itself: wait in
  20-30 s blocks, then `launch` [s:20261001-221517-chrono-2FYKPJ#16] [s:20261001-221517-chrono-2FYKPJ#37].
  A playable ad (a colour grid, "tap the lonely square") is not the game: do not play it; skip it or
  restart the app [s:20261001-143237-chrono-2FYKPJ#16]. System Back does not close an interstitial
  [s:20261001-143237-chrono-2FYKPJ#10].
  Hypothesis, not a rule yet: the interstitial has a cooldown of about 50-60 s from the last one
  closing, so a level started within about 45 s of an ad closing gets none
  ([experiment ad-cooldown-timer](../features/ads-interstitial.md#how-it-works)).

### Level times
Seconds from `level start` to `level end`. When the ad comes after `level start`, its time is inside
the level time (marked "ad").

| Levels | Result | Median | Range | Model | Source |
|---|---|---|---|---|---|
| tutorial–18 | 19 won | 22 s | 15–58 s (58 s: booster demo; 41 s: deliberate wrong cat) | opus | [s:20261001-003641-chrono-2FYKPJ#37] |
| 19–48 | 30 won | 20 s | 16–29 s | sonnet | [s:20261001-024647-chrono-2FYKPJ#109] |
| 49–55 | 7 won | 29 s | 22–271 s (49: fail/revive/booster tests; 51: Restart test) | sonnet | [s:20261001-035425-chrono-2FYKPJ#61] |
| 56–61 | 6 won | not logged | the session logged one "level 56 quit 407 s" | sonnet | [s:20261001-070939-chrono-2FYKPJ#27] |
| 62–70 | 9 won | 25 s | 13–41 s (Hard 70: 41 s); 63 about 75 s after a misread, logged 18 s | sonnet | [s:20261001-091349-chrono-2FYKPJ#38] |
| 71–80 | 10 won | 26 s | 17–39 s (Hard 80: 39 s); 73: 197 s of hint tests; 77 logged 5 s before it was solved; 72 not logged | sonnet | [s:20261001-100940-chrono-2FYKPJ#41] |
| 81–82 | 2 won | about 4 min | board typed by hand, corrected by `ask`; logged as quit | haiku | [s:20261001-143237-chrono-2FYKPJ#19] |
| 83–107 | 25 won | 29 s | 19–59 s without an ad; 100–149 s with an ad inside the level time (92, 94, 96, 98, 100, 102) | haiku, sonnet, opus (bench) | [s:20261001-171804-chrono-2FYKPJ#10] [s:20261001-175856-chrono-2FYKPJ#22] |
| 108–120 | 13 won | 20 s | 12–40 s; 115: 136 s with a staged fail and Revive | sonnet | [s:20261001-221517-chrono-2FYKPJ#41] |

Solving is no longer the bottleneck: from level 83 the frame-reading solver takes 12-40 s per level.
Ads take most of the wall time: about 40% of session 2, about half of the bench slots 2-3 and about 45%
of the 108-120 session [s:20261001-024647-chrono-2FYKPJ#109] [s:20261001-172422-chrono-2FYKPJ#11]
[s:20261001-221517-chrono-2FYKPJ#41].

## Boosters and fail (session 20261003-232850)
- Cat booster places one correct cat; bulb shows a hint then Apply (364,1348) places cats; counts 5 each, persist across levels; at 0 badge = AD, rewarded video gives +1.
- 3 wrong double taps: "Almost!" with Revive (video) and Restart (364,1285, free, same board, hearts reset). Back arrow quits with no confirmation; force-stop mid-level returns to Home, progress in level lost.

## Dream 2026-10-04: the fresh install (1.0.2)

- Fresh launch: consent Accept, the Android notification dialog, a 2-board tutorial, then level 1 with no Home in between; Home only by the back arrow [s:20261003-200925-chrono-2FYKPJ#0-12]. The solver gives up on the dimmed tutorial boards: place the cats where the hand points [s:20261003-200925-chrono-2FYKPJ#6-8].
- Boosters: the bulb is charged when the hint opens; Apply places up to 3 sure cats. At 0 a booster shows AD; the video takes about 64-77 s and may end on the Play Store (`launch`) [s:20261003-232850-chrono-2FYKPJ#4-8].
- Loss: "Almost!" with Revive (AD) and a free Restart (same board, 3 hearts) at (364,1285) [s:20261003-232850-chrono-2FYKPJ#18-19]. In an exit-app test reopen the level before recording anything [s:20261003-232850-chrono-2FYKPJ#23].

| Level | Result | Seconds | Source |
|---|---|---|---|
| 1 | won (solve) | 30 | [s:20261003-200925-chrono-2FYKPJ#10] |
| 2 | won (solve) | 29 | [s:20261003-200925-chrono-2FYKPJ#16] |
| 3 | won (boosters, then solve) | 133 | [s:20261003-232850-chrono-2FYKPJ#9] |

## Level times by mechanic (dream 2026-10-07)

```yaml
---
mechanics:
- id: akari
  name: Cat placement (Light Up rules)
  status: mastered
  method: solver
  solver: solvers/com.oakever.akari/akari.py
  levels:
    won: 46
    lost: 3
    quit: 7
  typical_min: 0.6
  best_min: 0.2
  solver_file: solvers/com.oakever.akari/akari.py
level_budget_min: 5
```
