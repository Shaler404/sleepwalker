---
game: com.vitastudio.mahjong
title: "How to play"
type: agent
version_seen: 3.39.1
verified_at: 2026-10-01
sources: [20260930-211039-chrono-2FYKPJ, 20260930-214524-chrono-2FYKPJ, 20260930-221457-chrono-2FYKPJ, 20260930-225122-chrono-2FYKPJ, 20260930-235817-chrono-2FYKPJ, 20261001-010125-chrono-2FYKPJ, 20261001-031723-chrono-2FYKPJ]
---

# How to play: Vita Mahjong

The player reads this before every level and works in the local copy `state/com.vitastudio.mahjong/playbook.md`;
the dream merges it here. Level times: `sw.py playbook`.

## core-match: tray mahjong
- Goal: clear every tile.
- Controls: tap a free tile → it flies into the 4-slot tray; two identical tiles in the tray vanish
  [s:20260930-211039-chrono-2FYKPJ#80]. Undo returns the last tray tile; Hint lights a pair; Shuffle reshuffles faces in place.
- Rules: a tile is free when nothing lies on it and one side (left or right) is open. Tapping a locked
  tile only shows "Locked by left and right" — harmless [s:20260930-203959-chrono-2FYKPJ#22]. 4 unmatched tiles = Out of space
  (Revive / "-4 to revive" / Restart; every revive returns the 4 tray tiles to the board) [s:20260930-225122-chrono-2FYKPJ#34].
- Reading layers (the time sink):
  - A tile drawn over its neighbours, with full shadow, is on top; a partly hidden tile is covered.
  - Rows of the same layer that overlap vertically only overlap in drawing order: no block [s:20260930-225122-chrono-2FYKPJ#39].
  - A higher tile half a tile off diagonally covers the 2–4 tiles under its corners [s:20260930-225122-chrono-2FYKPJ#76].
  - SIDE RULE: a tile is blocked on a side by any same-layer tile touching that side, even with a
    half-row offset [s:20260930-235817-chrono-2FYKPJ#27].
  - In a closed row only the two ends are free: peel from an end [s:20260930-235817-chrono-2FYKPJ#34].
  - A tile with only 60–90 px visible is covered, even at the board edge [s:20261001-010125-chrono-2FYKPJ#72].
  - Cascades: the lowest drawn tile of a stack is the free one [s:20260930-221457-chrono-2FYKPJ#60].
  - Look-alikes: blue 8-circle vs red/blue 8-circle; 3-bamboo vs 5-bamboo [s:20260930-221457-chrono-2FYKPJ#44] [s:20260930-214524-chrono-2FYKPJ#123].
- Face-down greens (from L11): the tap rule is not settled (see the
  [page](../features/hidden-tiles.md)); treat a tap on a green as information and only when the tray
  can take an unknown single.
- Method: manual, batches. On every frame list ALL certain pairs (both tiles free) and send them in one
  batch of 8–13 taps in peel order; end with at most ONE uncertain tap (a blocker whose removal frees
  the twin of a tray tile) [s:20260930-221457-chrono-2FYKPJ#90] [s:20261001-031723-chrono-2FYKPJ#61].
- Tray discipline: never take a single while 2 are in the tray; never two uncertain pairs in one batch;
  at 3 in the tray with no sure match: Undo at once [s:20260930-225122-chrono-2FYKPJ#33] [s:20260930-225122-chrono-2FYKPJ#46].
- When no certain pair is left: spend a hint (a video gives 2) rather than guess; take the blocker
  the hint hand points at first [s:20261001-010125-chrono-2FYKPJ#47] [s:20261001-031723-chrono-2FYKPJ#5].
- Timing: take one frame after the level opens (the intro eats the first taps) and wait 1 s after a
  match animation before a tray-critical tap; taps sent under a popup are lost [s:20260930-221457-chrono-2FYKPJ#79] [s:20260930-225122-chrono-2FYKPJ#38] [s:20260930-235817-chrono-2FYKPJ#65].
- Ads: a playable with no close button — `sw.py launch` at once; the reward is still granted [s:20261001-031723-chrono-2FYKPJ#82].
- Solver: the player's local draft (board JSON) is untested and models the greens wrongly; it is not
  published.

### Level times
| Level | Result | Minutes | Model | What decided it | Source |
|---|---|---|---|---|---|
| 1 | won | 22.8 | — | ~15 free hints, one pair per step | [s:20260930-211039-chrono-2FYKPJ#117] |
| 2 | won | 17.7 | — | one tap per call | [s:20260930-214524-chrono-2FYKPJ#96] |
| 3 | won | 9.2 | opus | 2–8 tap batches | [s:20260930-221457-chrono-2FYKPJ#39] |
| 4 | won | 7.5 | opus | look-alike tiles, an overloaded batch | [s:20260930-221457-chrono-2FYKPJ#60] |
| 5 | won | 6.5 | opus | 4–9 certain pairs per batch, tray ≤ 2 | [s:20260930-221457-chrono-2FYKPJ#77] |
| 6 | won | 5.8 | opus | 10–12 tap batches after the intro | [s:20260930-221457-chrono-2FYKPJ#90] |
| 7 | won | 7.8 | opus | single taps, 3 locked guesses | [s:20260930-225122-chrono-2FYKPJ#20] |
| 8 | won | 17.6 | opus | dense 3 layers, 2 Out of space | [s:20260930-225122-chrono-2FYKPJ#61] |
| 9 | quit, then won | 8.0 + 9.6 | opus | top-down peeling, then a tray overflow | [s:20260930-225122-chrono-2FYKPJ#76] [s:20260930-235817-chrono-2FYKPJ#20] |
| 10 (Hard) | won | 9.1 | opus | stuck 4 min, Shuffle opened it | [s:20260930-235817-chrono-2FYKPJ#41] |
| 11 | won | 13.8 | opus | a covered hint target, popups | [s:20260930-235817-chrono-2FYKPJ#67] |
| 12 | quit, then won | 28.1 + 14.0 | opus | greens, half-offset tiles, video hints | [s:20261001-010125-chrono-2FYKPJ#72] [s:20261001-031723-chrono-2FYKPJ#52] |
| 13 | won | 18.1 (3.2 of ads) | opus | fast opening batches, slow greens | [s:20261001-031723-chrono-2FYKPJ#95] |

Best 5.8 min (L6); every level from L7 is over the 5-minute budget, so the mechanic is `broken`.
Make it fast: a solver that reads tiles and layers from the screenshot (the hand-written board JSON was
slower than playing).
