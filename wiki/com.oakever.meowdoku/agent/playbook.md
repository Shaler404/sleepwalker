---
game: com.oakever.meowdoku
title: "How to play"
type: agent
version_seen: 1.18.0
verified_at: 2026-10-02
sources: [20260930-233055-chrono-2FYKPJ, 20261001-013526-chrono-2FYKPJ, 20261001-022624-chrono-2FYKPJ, 20261001-060942-chrono-2FYKPJ, 20261001-082114-chrono-2FYKPJ, 20261001-093348-chrono-2FYKPJ, 20261001-115413-chrono-2FYKPJ, 20261001-181422-chrono-2FYKPJ, 20261001-182015-chrono-2FYKPJ, 20261001-182810-chrono-2FYKPJ, 20261001-183504-chrono-2FYKPJ, 20261001-184038-chrono-2FYKPJ, 20261001-185238-chrono-2FYKPJ, 20261001-223249-chrono-2FYKPJ]
---

# How to play: Meowdoku

The player reads this before every level and works in the local copy `state/com.oakever.meowdoku/playbook.md`;
the dream merges it here. Level times: `sw.py playbook`.

## queens: Cat placement on color regions (Queens-like)
- Goal: N×N board with N colour regions; place N cats: one per region, row and column, no two cats
  touching (diagonals included) [s:20260930-233055-chrono-2FYKPJ#9].
- Controls: DOUBLE TAP places a cat (`sw.py taps "X,Y:2"`); a single tap or a swipe marks X (notes
  only). Boosters: cat (180,1357), hint (367,1357) → Apply, mouse (553,1357) [s:20261001-013526-chrono-2FYKPJ#77] [s:20261001-013526-chrono-2FYKPJ#80].
- Rules: a wrong cat costs 1 of 3 fish (orange X); at 0 fish "Out of Fishes" [s:20261001-013526-chrono-2FYKPJ#81] [s:20261001-022624-chrono-2FYKPJ#40].
- Method: solver [`solvers/com.oakever.meowdoku/queens.py`](../../../solvers/com.oakever.meowdoku/queens.py): reads the board from the
  screenshot (saturation bands, colours clustered by hue down to N groups), backtracks, and since the lab of
  2026-10-03 returns a double tap ([x, y, 2]) for EVERY missing cat in one round. Since the lab of
  2026-10-06 that round also says `done` (the board has one solution and the moves place every missing
  cat), so the run stops after it: "the solver says these moves finish the level". It
  skips cats already on the board (hint/cat booster cats too). It returns no moves (see its note) when
  the grid size, the regions or the cat count look wrong or the board has several solutions.
- **Play every level with `solve queens --run --rounds 3`** (after `launch` has closed the interstitial):
  one round places all cats and the run ends with "these moves finish the level". Then take a `shot`: the
  win screen, the leaderboard or a Daily popup ("New trial skin", "Pure logic. No hesitation.") means won;
  if the board is still there with a cat missing (a lost double tap), run `solve --run` again, it places
  only the missing cats. Before 2026-10-06 a second round looked at the screen after the last cat and, on
  the Daily popups, ended the run as "no moves" (the lab counted 3 of 5 winning runs as given up). Do NOT
  copy the solution into a hand `taps` batch:
  that was the old work-around for the 3-cats-per-round limit (`solve --run` needed 4-5 rounds, L129 111 s)
  and the lab counts it as a bypassed solver. Lab check 2026-10-03: L127 9x9, L128/L129/L130 10x10 and the
  Daily 10/03 board each get all 9-10 cats in one round, the same cells as the winning hand batches.
- Fallback only when `solve` refuses a frame that IS a board: cell centres in the 730x1583 frame
  (normal levels; c = column, r = row, from 0) for a hand `taps` batch:

  | Board | x | y | Source |
  |---|---|---|---|
  | 10x10 | 54 + 69c | 515 + 69r | [s:20261001-182810-chrono-2FYKPJ#2] |
  | 9x9 | 59 + 77c | 520 + 76.5r | [s:20261001-183504-chrono-2FYKPJ#8] |
  | 8x8 | 65 + 86c | 525 + 86r | [s:20261001-182810-chrono-2FYKPJ#10] |
  | 7x7 | 84 + 93.7c | 547 + 94r | [s:20261001-082114-chrono-2FYKPJ#30] |

  Skip the cell of a cat that is already on the board (a double tap there may remove it). Write in the
  level note why the solver refused (its note), so the lab can fix the reading.
- When the solver reads the board wrong (it merged two similar colours on L84, left 1-5 cats out on
  L49-55, read nothing on L56), read the grid by hand into one letter per region and solve it with a
  short row-by-row search (one cat per row, column and region, no touching); each board has one
  solution [s:20261001-115413-chrono-2FYKPJ#9] [s:20261001-060942-chrono-2FYKPJ#60] [s:20261001-082114-chrono-2FYKPJ#4].
- `sw.py solve queens` draws the planned cats on the frame:

  ![Solver overlay on level 3: the cells the solver will fill are marked on the board](../img/20261001-solver-overlay-fac1853e.webp)

- Level plan: on Home tap "Level N" at **(365,1185)**; on the win screen the next-level button is at
  (365,1245). An interstitial follows almost every level start: `launch`, wait 3-4 s, `solve queens
  --run --rounds 3`, wait about 6 s, win screen [s:20261001-185238-chrono-2FYKPJ#10] [s:20261001-182810-chrono-2FYKPJ#9].

  > ⚠️ Previously (v1.18.0, 2026-10-01): "Level plan: tap Level N (365,1245)". That holds on the win
  > screen only; on Home (365,1245) does nothing [s:20261001-183504-chrono-2FYKPJ#1].
- After a win: from level 11 the leaderboard overlay comes first: Tap to Continue (365,1413), then
  look at the frame before the next-level button (365,1245) - the overlay can be late and a blind pair
  of taps drifts by a level [s:20260930-233055-chrono-2FYKPJ#72] [s:20261001-013526-chrono-2FYKPJ#110].
- **Golden-offer pitfall:** on the win screen of every 4th level (54, 58 ... 126) the next-level button
  is replaced by **Golden Fish** at the same place, so the routine tap (365,1245) starts the golden bonus
  board (one fish, about a minute, sometimes after an ad). Look at the frame first; to go on, tap "Skip
  to Level N" at (365,1475) [s:20261001-093348-chrono-2FYKPJ#64] [s:20261001-181422-chrono-2FYKPJ#11]
  [s:20261001-182015-chrono-2FYKPJ#20]. A golden board has no "Level" in its header (only "Score") and
  one fish: never record it as a level [s:20261001-181422-chrono-2FYKPJ#13].

  ![Win screen of level 74: Golden Fish stands where Level 75 would be; Skip to Level 75 at the bottom](../img/20261002-golden-fish-level-offer-on-win-93936e64.webp)

- Out of Fishes (3 wrong cats): Restart (365,1398) is free and deals a NEW board for the same level;
  Get 3 Fishes is a rewarded ad that keeps the board [s:20261001-115413-chrono-2FYKPJ#43]
  [s:20261001-022624-chrono-2FYKPJ#42]. A booster at 0 offers a rewarded ad (2 ads, about 40 s) for
  1 charge [s:20261001-115413-chrono-2FYKPJ#57].
- Pitfalls:
  - The solver refuses frames that are not a clean board: the fade-in of a Daily board (squares still
    growing), the hint popup (reads "35 cats"), Home, ads ("1x1"/"2x2"/"3x3" or "list index out of
    range"). Wait 1-2 s and run `solve` again before reading the board by hand (lab 2026-10-03).
  - Golden Fish board: it opens under a dark veil with the tooltip "Only Golden Fish - Be careful!"; the
    solver says "the board is dimmed by an overlay" (before 2026-10-06: "read 49 cats"). Tap a neutral
    area (365,1250), then "tap to continue" (365,1394) if a card shows, look at the frame, then `solve --run`
    [s:20261006-021434-chrono-2FYKPJ#19] [s:20261006-021434-chrono-2FYKPJ#21].
  - Never press Android Back on Home: it opens a Quit popup; close it with the X (621,535)
    [s:20261001-185238-chrono-2FYKPJ#7] [s:20261001-185238-chrono-2FYKPJ#9].
  - A "1x1" solver read means a popup, an ad or Home is on screen, not a board: look at the frame and
    record nothing until the header shows the next "Level N" [s:20261001-185238-chrono-2FYKPJ#5]
    [s:20260930-233055-chrono-2FYKPJ#47].
  - Look at the frame before a continue tap after an ad: the "Install" card of an interstitial sits
    near (365,1413) and opened the Play Store once [s:20261001-060942-chrono-2FYKPJ#21].
  - The solver missed light colours (light blue, green, yellow) on 10x10 boards: check that every
    region has a cat [s:20261001-013526-chrono-2FYKPJ#106] [s:20261001-022624-chrono-2FYKPJ#16].
  - Record a level as won only after the win screen or the leaderboard, and name it from the "Level N"
    header, not from your own count: labels drifted by one in several sessions
    [s:20261001-013526-chrono-2FYKPJ#110] [s:20261001-060942-chrono-2FYKPJ#59] [s:20261001-184038-chrono-2FYKPJ#19].
  - Pattern Mode ON (icons on regions) does not change the rules. The solver from 2026-10-06 reads a
    Pattern Mode board correctly (lab: L139 frame 071212/00007, 10 moves, the winning cats); the L85/L86
    "no cats" came from the older solver. OFF is still the default [s:20261006-071212-chrono-2FYKPJ#7].
  - Hint Apply leaves X marks on the board; `solve` ignores them and still returns every cat
    (071212/00012, 00014). The hint popup itself reads as "dimmed by an overlay": close it first.
  - Research taps inside a level (settings, boosters, ads) count as hand moves in the lab's
    "placed by hand" sign (L139: 12 taps vs 10 solver cats). When a level is a booster/settings test,
    say so in the level note so the lab does not read it as a bypassed solver.
  - A toast "Only N% of players solved the last level without hints" covers rows 4-6 of the next board
    for a second or two after the level opens; `solve` refuses it ("a colour region is not connected").
    Wait 2 s and run it again (lab 2026-10-06: 101030/00031 refused, 00032 the same L143 board, 10 moves, done).
  - Record keeping (the lab reads only recorded levels): `level start "level N" ... --mechanic queens`
    BEFORE `solve --run`, and `level end won` on the first `shot` that shows the leaderboard or the win
    screen, BEFORE the Continue tap (365,1413). `level end won` right after a tap is refused ("take a frame
    of the win screen first"); if you already tapped on, use `level end won --shot N` with the frame that
    showed the win. Session 101030: L140 and L142 were refused once each, `level start "level 141"` was
    refused while L140 was still open, so L141 (8x8, won in 1 round) was never recorded and its run
    counted toward nothing; a recorded clean level would have cleared the lab's stale "gave up" sign.
  - Do not idle-wait on a screen for minutes: the phone dims and sleeps, and the next tap fails
    [s:20261001-223249-chrono-2FYKPJ#8].
  - Daily Challenge boards sit about 22 px lower; the solver still works [s:20261001-013526-chrono-2FYKPJ#106].
  - Back and the arrow do nothing on the win screen; go Home through the next level's back arrow
    [s:20261001-022624-chrono-2FYKPJ#62].

### Level times
| Levels | Result | Median | Range | Model | Source |
|---|---|---|---|---|---|
| tutorial–21 | won | 28 s | 18–123 s (L11: event and profile popups; L2: manual, 95 s) | opus | [s:20260930-233055-chrono-2FYKPJ#116] |
| 22–35 + Daily | won | about 50 s | 32–283 s (L23: a 3-minute playable ad) | sonnet | [s:20261001-013526-chrono-2FYKPJ#144] |
| 36–43 | won | 32 s | 21–165 s (L38: fish thrown away on purpose + ad) | sonnet | [s:20261001-022624-chrono-2FYKPJ#98] |
| 44–55 + golden | won (13 real) | about 50 s | 37–75 s; golden 7x7 by hand search 19 s | sonnet | [s:20261001-060942-chrono-2FYKPJ#116] |
| 56–66 + golden | won | 15 s from the board read | 14–17 s one hand batch; 22–27 s with deliberate mistakes; golden 53 s with a planned fail | sonnet | [s:20261001-082114-chrono-2FYKPJ#52] |
| 67–83 + 4 golden | won | about 55 s with the ad | only 3 level records written: times from the transcript | sonnet | [s:20261001-093348-chrono-2FYKPJ#113] |
| 84–96 + golden | won | about 25 s (one batch) | 23–39 s solve + one batch (L91–96); 63–100 s `solve --run` (L85–86, Pattern Mode ON) | sonnet | [s:20261001-115413-chrono-2FYKPJ#79] |
| 97–124 (bench, 8 slots) | won | about 50 s from the Level tap | 43–95 s, of it 9–30 s interstitial | haiku, sonnet, opus | [s:20261001-182810-chrono-2FYKPJ#15] [s:20261001-185238-chrono-2FYKPJ#26] |
| 125–126 | won | about 75 s | two levels in 2.5 min | sonnet | [s:20261001-223249-chrono-2FYKPJ#7] |

The mechanic's counter (`sw.py playbook`: 128 won, 3 quit, typical 1.0 min, best 0.2 min) overstates the
levels: four early records in 20261001-013526-chrono-2FYKPJ double-count levels, and in the bench slots
20261001-180616 to 185238 golden boards were recorded as levels, two wins were fake (185238: the frame was
the previous win screen) and one slot logged `level start` after the solve, so its 23–26 s are too low.
The times above come from the transcripts. Every level is far under the 5-minute budget.

## Session 20261003 notes (v1.19.1)
- Fish: wrong cat = 1 fish lost (orange X); win with 3 fish = "Perfect", 2 = "Brilliant, Beat 91.3%"; leaderboard fish rise by the fish earned. Boosters do not cost fish.
- Boosters at start: cat 1, hint 4, mouse 1; at 0 the badge becomes a green video icon (rewarded ad). Cat = one correct cat (+109 score), hint = Apply puts X on row/col/neighbours, mouse = mouse on a cell + X.
- After a win: leaderboard -> (Daily Streak Restore/Give up popup, yarn ball screen, Continue) -> win screen; a Rate Us popup may follow (X at 621,555). Level start: playable/video interstitial, `launch` leaves it.
- Solver mislabelled regions on L127 but cat positions were right.

## Session 20261003-202631 (L129-130)
- L129: solve queens --run --rounds 8 solved in one call (10x10). Win: leaderboard -> Tap to Continue (365,1413) -> praise screen (Immaculate = 3 fish) with next Level button (365,1245).
- Hint Apply places the cat on the explained cell (not an X). Cat booster places a correct cat at once. Ad at 0 charges: launch leaves it, charge granted.
- In-level gear > Restart keeps the SAME board; Out of Fishes Restart too. Back arrow = Home, no confirm. Android Back on Home = Quit popup.

## Dream 2026-10-04: corrections (1.19.1)

- Out of Fishes > Restart plays an interstitial and then deals the SAME board with 3 fish and score 0 [s:20261003-202631-chrono-2FYKPJ#18-20] (the "NEW board" above was seen on 1.18.0).
- The solver may return the missing cats over several rounds (L129: 4 rounds of up to 3): use `solve queens --run` [s:20261003-202631-chrono-2FYKPJ#2-5].
- Win flow: leaderboard (Tap to Continue), on the day's first win the Daily Streak popup (Give up at 365,1117 unless Restore is the goal) and screen, the praise screen, then Rate Us after the Level tap (X at 621,555) [s:20261003-201915-chrono-2FYKPJ#3-9]. Shoot the win screen before `level end won` (refused twice) [s:20261003-201915-chrono-2FYKPJ#7] [s:20261003-202631-chrono-2FYKPJ#6].
- After a level start or Restart take a shot before tapping the top-left back arrow: an ad under it opened the Play Store [s:20261003-202631-chrono-2FYKPJ#19-20].
- The cat booster at 0 shows a video icon; leaving the ad with `launch` after 60-100 s still granted the charge [s:20261003-202631-chrono-2FYKPJ#11-12].

| Level | Result | Seconds | Source |
|---|---|---|---|
| 127 | won, 3 fish | 121 | [s:20261003-201915-chrono-2FYKPJ#3] |
| 128 | won, 2 fish (booster study, includes about 80 s of popups and ad) | 194 | [s:20261003-201915-chrono-2FYKPJ#17] |
| 129 | won, Immaculate (solve about 36 s) | 111 | [s:20261003-202631-chrono-2FYKPJ#5] |

## Level times by mechanic (dream 2026-10-07)

```yaml
---
mechanics:
- id: queens
  name: Cat placement on color regions (Queens-like)
  status: mastered
  method: solver
  solver: solvers/com.oakever.meowdoku/queens.py
  levels:
    won: 22
    lost: 1
    quit: 2
  typical_min: 1.0
  best_min: 0.5
  solver_file: solvers/com.oakever.meowdoku/queens.py
level_budget_min: 5
```
