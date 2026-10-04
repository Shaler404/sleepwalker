---
game: com.oakever.arrows
title: "How to play"
type: agent
version_seen: 1.31.0
verified_at: 2026-10-02
sources: [20261001-204000-chrono-2FYKPJ]
---

# How to play: Amaze GO!

The player reads this before every level and works in the local copy
`state/com.oakever.arrows/playbook.md`; the dream merges it here. Level times: `sw.py playbook`.
Positions are in the 730x1583 frame.

## arrows-escape: Tap arrows so they slide off the board
- Goal: clear every arrow from the board. 0 mistakes gives 3 stars and "Flawless!" [s:20261001-204000-chrono-2FYKPJ#4].
- Controls: tap any segment of an arrow; it slides out along its head direction, the body following
  its own path. The board is a dot grid, about 45 px per cell (levels 1-3: 5x5, centred near y 800)
  [s:20261001-204000-chrono-2FYKPJ#21].
- Rules: an arrow leaves only if no other arrow lies on the straight line from its head to the board
  edge. 3 blue drops at the top left are the mistake allowance; what a blocked tap costs is not
  verified yet (experiment `lives-mistake`) [s:20261001-204000-chrono-2FYKPJ#21].
- Risks: tapping a blocked arrow (probably costs a drop). Taps on free arrows are safe and can be
  batched.
- Method: manual. Levels 1-3 took 0.4-0.7 min. The status "mastered" was set on tutorial-sized boards
  only; for larger boards a solver from the dot grid will probably be worth it [s:20261001-204000-chrono-2FYKPJ#8].
- Level plan: list the arrows whose head faces open space (usually the outer ones) and tap them in one
  batch; take a frame; then tap the arrows they freed [s:20261001-204000-chrono-2FYKPJ#4] [s:20261001-204000-chrono-2FYKPJ#7] [s:20261001-204000-chrono-2FYKPJ#20].
- Pitfalls:
  - A tap sent while the previous arrow is still sliding can be ignored: check the frame after a
    batch and re-tap what is left [s:20261001-204000-chrono-2FYKPJ#7] [s:20261001-204000-chrono-2FYKPJ#8].
  - The hit-box is generous: a tap between two arrows can move the neighbour instead. To hit one
    arrow, tap the middle of a segment with no other arrow within one cell [s:20261001-204000-chrono-2FYKPJ#21].
  - The result screen's Next Level appears about 3 s after the win; a tap before it does nothing
    [s:20261001-204000-chrono-2FYKPJ#5] [s:20261001-204000-chrono-2FYKPJ#6].

### Level times
| Levels | Result | Logged | In-game timer | Model | Source |
|---|---|---|---|---|---|
| 1 (tutorial) | won, Flawless | 24 s | 00:11 | opus | [s:20261001-204000-chrono-2FYKPJ#4] |
| 2 | won, Flawless | 24 s | 00:12 | opus | [s:20261001-204000-chrono-2FYKPJ#8] |
| 3 | won, Flawless | 44 s (includes the lives experiment) | 00:25 | opus | [s:20261001-204000-chrono-2FYKPJ#22] |

Median 0.4 min against a 5 min budget. Boards of levels 1-3: [levels.md](../levels.md).

## Notes 20261003-232357
- L3-L4 normal boards: free arrows first; blocked tap costs 1 drop (3 total) and arrow flashes red; L4 won Perfect with 1 mistake. Win screen: Flawless (0 mistakes)/Perfect.
- L5 is "Hard" (purple, also L8): board larger than screen, "Pinch to zoom" tip, hint bulb button. Not played: needs strong model (zoom/pan handling, solver).
- In-level gear = Sound/Vibration/Music/Zen + Restart. Back arrow quits instantly (no confirm).
- 20261004: Hard L5 won via hint loop (hint=free green free-arrow, tap it). Write real solver later.

## Dream 2026-10-04: Hard levels (1.33.0)

- A blocked tap costs one drop and the arrow turns red; at 0 drops "Out of Lives" offers a free Continue (board kept) or Restart (board reset) [s:20261003-233756-chrono-2FYKPJ#4-5] [s:20261003-233756-chrono-2FYKPJ#23].
- Hard levels (L5, L8, L10; board about 3 screens wide): play the hint loop: bulb (665,212), wait about 2 s for the pan, tap the green arrow. The hint is free (about 55 uses on L5). Never batch blind taps on a Hard board: that gave 4 Out of Lives in one session [s:20261003-233756-chrono-2FYKPJ#6-22] [s:20261004-001551-chrono-2FYKPJ#2-108].
- If a bulb tap leaves the frame unchanged, the green arrow is off-screen: find the green edge pixel and swipe toward it [s:20261004-001551-chrono-2FYKPJ#84-92]. Do not `shot` after a tap that already returns a frame [s:20261004-001551-chrono-2FYKPJ#13].
- To speed up (untested): in each hint frame also tap the other arrows that are visibly free (task make-hard-fast) [s:20261004-001551-chrono-2FYKPJ#61].
- After a win the Daily Streak screen can come before the win card; shoot the card only once Next Level and Home are visible (the score counts up: 895 -> 1194) [s:20261004-001551-chrono-2FYKPJ#110].
- Run destructive outcome cases (Restart, force-stop) after the win or on an early board, never mid-attempt on the progress gate [s:20261003-233756-chrono-2FYKPJ#23-24].

| Level | Result | Seconds | Source |
|---|---|---|---|
| 3 | won, Flawless | 35 | [s:20261003-232357-chrono-2FYKPJ#11] |
| 4 | won, Perfect (1 mistake) | 105 | [s:20261003-232357-chrono-2FYKPJ#17] |
| 5 Hard | won by the hint loop, Great Start! 1194 | 863 (13:15) | [s:20261004-001551-chrono-2FYKPJ#110] |
