---
game: com.oakever.meowdoku
title: "How to play"
type: agent
version_seen: 1.18.0
verified_at: 2026-10-01
sources: [20260930-233055-chrono-2FYKPJ, 20261001-013526-chrono-2FYKPJ, 20261001-022624-chrono-2FYKPJ]
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
  screenshot (saturation bands, colours clustered by hue down to N groups), backtracks, returns at most
  3 double taps ([x, y, 2]) per round with `rescan`. Run `sw.py solve queens --run --rounds 8`. It returns
  no moves (see its note) when the grid size, the regions or the cat count look wrong or the board has
  several solutions: then look at the frame (popup, ad, intro animation) or place the cats by hand.
- `sw.py solve queens` draws the planned cats on the frame:

  ![Solver overlay on level 3: the cells the solver will fill are marked on the board](../img/20261001-solver-overlay-fac1853e.webp)

- Level plan: tap "Level N" (365,1245) → look at the frame (an interstitial may be up: `launch`) →
  wait 2 s (the intro eats taps) → solve → win screen.
- After a win: from level 11 the leaderboard overlay comes first: Tap to Continue (365,1413), then
  look at the frame before "Level N" (365,1245) — the overlay can be late and a blind pair of taps
  drifts by a level [s:20260930-233055-chrono-2FYKPJ#72] [s:20261001-013526-chrono-2FYKPJ#110].
- Pitfalls:
  - The solver misses light colours (light blue, green, yellow) on 10x10 boards: look at the frame
    after the run and place the last cats by hand (10x10: x=54+69c, y=515+69r) [s:20261001-013526-chrono-2FYKPJ#106] [s:20261001-022624-chrono-2FYKPJ#16].
  - A popup or ad over the board reads as a "1x1, 1 colors" board: recover first [s:20260930-233055-chrono-2FYKPJ#47] [s:20261001-013526-chrono-2FYKPJ#24].
  - Record a level as won only after the win screen or the leaderboard: four early records
    mislabelled later levels [s:20261001-013526-chrono-2FYKPJ#20] [s:20261001-013526-chrono-2FYKPJ#110].
  - Daily Challenge boards sit about 22 px lower; the solver still works [s:20261001-013526-chrono-2FYKPJ#106].
  - Back and the arrow do nothing on the win screen; go Home through the next level's back arrow
    [s:20261001-022624-chrono-2FYKPJ#62].

### Level times
| Levels | Result | Median | Range | Model | Source |
|---|---|---|---|---|---|
| tutorial–21 | won | 28 s | 18–123 s (L11: event and profile popups; L2: manual, 95 s) | opus | [s:20260930-233055-chrono-2FYKPJ#116] |
| 22–35 + Daily | won | about 50 s | 32–283 s (L23: a 3-minute playable ad) | sonnet | [s:20261001-013526-chrono-2FYKPJ#144] |
| 36–43 | won | 32 s | 21–165 s (L38: fish thrown away on purpose + ad) | sonnet | [s:20261001-022624-chrono-2FYKPJ#98] |

The mechanic's counter says 47 won; four early records in session 20261001-013526-chrono-2FYKPJ double-count levels, so the
real number is 45 (tutorial, levels 1–43, the Daily Challenge).
