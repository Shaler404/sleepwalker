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
