---
game: com.vitastudio.mahjong
title: "How to play"
type: agent
version_seen: 3.39.1
verified_at: 2026-10-01
sources: [20260930-203959-chrono-2FYKPJ, 20260930-211039-chrono-2FYKPJ, 20260930-214524-chrono-2FYKPJ, 20260930-221457-chrono-2FYKPJ, 20260930-225122-chrono-2FYKPJ, 20260930-235817-chrono-2FYKPJ, 20261001-010125-chrono-2FYKPJ, 20261001-031723-chrono-2FYKPJ, 20261001-063226-chrono-2FYKPJ, 20261001-083725-chrono-2FYKPJ, 20261001-110957-chrono-2FYKPJ, 20261001-204654-chrono-2FYKPJ, 20261001-205148-chrono-2FYKPJ, 20261001-211823-chrono-2FYKPJ]
---

# How to play: Vita Mahjong

The player reads this before every level and works in the local copy `state/com.vitastudio.mahjong/playbook.md`;
the dream merges it here. Level times: `sw.py playbook`.

## core-match: tray mahjong
- Goal: clear every tile.
- Controls: tap a free tile → it flies into the 4-slot tray; two identical tiles in the tray vanish
  [s:20260930-211039-chrono-2FYKPJ#80]. Undo returns the last tray tile; Hint lights a pair; Shuffle
  moves the tiles (greens included) between the same slots, see below.
- Rules: a tile is free when nothing lies on it and one side (left or right) is open. Tapping a locked
  tile only shows "Locked by left and right" — harmless [s:20260930-203959-chrono-2FYKPJ#22]. 4 unmatched tiles = Out of space
  (Revive / "-4 to revive" / Restart; every revive returns the 4 tray tiles to the board) [s:20260930-225122-chrono-2FYKPJ#34].
- Reading layers (the time sink):
  - A tile drawn over its neighbours, with full shadow, is on top; a partly hidden tile is covered.
  - Rows of the same layer that overlap vertically only overlap in drawing order: no block [s:20260930-225122-chrono-2FYKPJ#39].
  - A higher tile half a tile off diagonally covers the 2–4 tiles under its corners [s:20260930-225122-chrono-2FYKPJ#76].
  - SIDE RULE: a tile is blocked on a side by any same-layer tile touching that side, even with a
    half-row offset [s:20260930-235817-chrono-2FYKPJ#27]. Face-down greens count: a tile drawn on top
    but flanked by same-layer greens is "Locked by left and right"; free a row end first [s:20261001-110957-chrono-2FYKPJ#52].
  - Before treating a top-looking tile as free, check BOTH edges for flush same-layer neighbours
    (the source of wrong singles on L15) [s:20261001-063226-chrono-2FYKPJ#56] [s:20261001-063226-chrono-2FYKPJ#62].
  - In a closed row only the two ends are free: peel from an end [s:20260930-235817-chrono-2FYKPJ#34].
  - A tile with only 60–90 px visible is covered, even at the board edge [s:20261001-010125-chrono-2FYKPJ#72].
  - Cascades: the lowest drawn tile of a stack is the free one [s:20260930-221457-chrono-2FYKPJ#60].
  - Look-alikes: blue 8-circle vs red/blue 8-circle; 3-bamboo vs 5-bamboo [s:20260930-221457-chrono-2FYKPJ#44] [s:20260930-214524-chrono-2FYKPJ#123].
- Special tiles are ordinary pairs: the blank card (white face, green frame, red inner border — NOT a
  face-down green) [s:20261001-211823-chrono-2FYKPJ#6], gold 福 tiles, framed pictures (roses, gazebo,
  graffiti), IQ+N tiles [s:20260930-225122-chrono-2FYKPJ#76].
- Face-down greens (from L11) — the rule is settled [s:20261001-110957-chrono-2FYKPJ#32]:
  - a tap on a FREE unseen green flips it face up in place and takes NO tray slot [s:20261001-110957-chrono-2FYKPJ#12];
  - only one green is face up at a time: flipping another turns the earlier one face down again [s:20261001-083725-chrono-2FYKPJ#43];
  - while a green is face up, a tap on a free tile of its kind clears both at once, no tray [s:20261001-205148-chrono-2FYKPJ#73];
    a tap on any other tile turns it face down again [s:20261001-205148-chrono-2FYKPJ#5];
  - a green whose face you have seen goes straight into the tray when tapped (with its twin = a certain pair)
    [s:20261001-110957-chrono-2FYKPJ#36] [s:20261001-205148-chrono-2FYKPJ#44];
  - after a twin clears a face-up green, do NOT tap the green's spot: the tap takes the tile under it [s:20261001-205148-chrono-2FYKPJ#63];
  - a tap on a covered green does nothing (stays face down, nothing to the tray) [s:20261001-205148-chrono-2FYKPJ#18];
  - aim at the centre of a green: a tap near its lower edge hit the tile drawn over it [s:20261001-063226-chrono-2FYKPJ#45];
  - lit by the Hint, greens show teal: tap both (or the one whose twin sits in the tray) [s:20261001-063226-chrono-2FYKPJ#54] [s:20261001-063226-chrono-2FYKPJ#58].
- Shuffle keeps the slots but moves every tile between them, greens included, and every green is unseen
  again; the tray stays [s:20261001-063226-chrono-2FYKPJ#59] [s:20261001-205148-chrono-2FYKPJ#41].
- Method: manual (the local solver is not published, see below). Per frame:
  1. list ALL certain pairs (both tiles free) and the tray twins, and send them in one batch in peel order
     (4–13 taps); a pair whose first tile is uncertain: tap the UNCERTAIN tile first — a locked tap does
     nothing, so the sure tile only follows into the tray if the first one went [s:20261001-083725-chrono-2FYKPJ#46] [s:20261001-063226-chrono-2FYKPJ#56];
  2. a tile whose twin is in the tray is a free tap (locked: nothing; free: a match) [s:20261001-083725-chrono-2FYKPJ#48] [s:20261001-083725-chrono-2FYKPJ#62];
  3. end the batch with ONE green flip (free information, no tray slot), then pair the face in the next
     batch [s:20261001-083725-chrono-2FYKPJ#43] [s:20261001-110957-chrono-2FYKPJ#15]. When a green's twin is
     known, flip that green LAST: any later flip turns it face down [s:20261001-110957-chrono-2FYKPJ#32];
  4. endgame: k pairs of k kinds left with k ≤ 3 → tap them all in one batch [s:20261001-063226-chrono-2FYKPJ#29].
- Taps per call: a certain pair goes as ONE call (`taps`, ~1.3 s apart). One tap per call (205148) gave
  no errors but cost ~10.5 s per tap and ~12 of the 23 L18 minutes [s:20261001-205148-chrono-2FYKPJ#29].
  Frames do not lag; never "probe" by hand-tapping tiles [s:20261001-204654-chrono-2FYKPJ#10].
- Tray discipline: never take a single while 2 are in the tray; never two uncertain pairs in one batch;
  at 3 in the tray with no sure match: Undo at once [s:20260930-225122-chrono-2FYKPJ#33] [s:20260930-225122-chrono-2FYKPJ#46].
- No certain pair: flip free greens first (free), then the Hint — tap it ONCE, wait 1 s and look (two quick
  taps spent both hints on one pair) [s:20261001-083725-chrono-2FYKPJ#21]; in the green phase take a
  Free Hint video at once instead of peeking greens one by one [s:20261001-063226-chrono-2FYKPJ#53].
  Take the blocker the hint hand points at first [s:20261001-031723-chrono-2FYKPJ#5]. A Hint that only makes
  Shuffle glow means no free pair: it is spent anyway [s:20261001-205148-chrono-2FYKPJ#24].
- Shuffle when 2–3 singles wait in the tray with no free twin: it gave 3 tray matches on L14 and L16 and
  a 10-tap certain batch on L17 [s:20261001-063226-chrono-2FYKPJ#20] [s:20261001-083725-chrono-2FYKPJ#55] [s:20261001-083725-chrono-2FYKPJ#81].
- Timing: take one frame after the level opens (the intro eats the first taps) and wait 1 s after a
  match animation before a tray-critical tap; taps sent under a popup are lost [s:20260930-221457-chrono-2FYKPJ#79] [s:20260930-225122-chrono-2FYKPJ#38] [s:20260930-235817-chrono-2FYKPJ#65].
- Leaving: the back arrow keeps the board [s:20261001-110957-chrono-2FYKPJ#70]. Quitting from Out of space
  throws away the lost attempt and restores the last saved board (L18) [s:20261001-205148-chrono-2FYKPJ#1].
- Ads: a playable with no close button — `sw.py launch` at once; the reward is still granted [s:20261001-031723-chrono-2FYKPJ#82].
  Never tap the video's top-left skip arrow: it opened the Play Store (~20 s + relaunch) [s:20261001-063226-chrono-2FYKPJ#51].
- Solver (local draft `state/com.vitastudio.mahjong/solvers/core-match.py`, not published): the lab
  rewrote it on 2026-10-01 to read the screenshot and remember greens between rounds. It stalled on the
  L18 resume frame ("no certain pair", tray tile read as "?") [s:20261001-205148-chrono-2FYKPJ#1] and on L19
  after 3 rounds; it missed a free blank-card pair [s:20261001-211823-chrono-2FYKPJ#3]. Task `core-match-fast`.

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
| 14 | won | 12.4 | opus | first 60% in 4 min (7 batches, 0 wrong taps), last 40% 8 min peeking greens | [s:20261001-063226-chrono-2FYKPJ#30] |
| 15 | quit at ~60%, then won | 15.1 + 9.2 | opus | side-locked tiles, 3 wrong singles; resumed with the flip-then-pair loop | [s:20261001-063226-chrono-2FYKPJ#62] [s:20261001-083725-chrono-2FYKPJ#43] |
| 16 | won | 13.7 | opus | 60% in 4 min / 6 batches, then ~one green reveal per frame | [s:20261001-083725-chrono-2FYKPJ#73] |
| 17 | quit at ~45%, restarted, won | 4.3; 14.4 | opus | 4–6 tap batches, green flips, one Shuffle | [s:20261001-083725-chrono-2FYKPJ#83] [s:20261001-110957-chrono-2FYKPJ#40] |
| 18 | quit at ~45% | 13.8 | opus | tiles flanked by same-layer greens, 2 video hints | [s:20261001-110957-chrono-2FYKPJ#67] |
| 18 | lost to Out of space, quit | 2.4 | sonnet | hand-tapped probes into a full tray | [s:20261001-204654-chrono-2FYKPJ#10] |
| 18 (resumed) | won | 23.4 (~5 of ads) | opus | one tap per call; video Hint + Shuffle at a dead end | [s:20261001-205148-chrono-2FYKPJ#72] |
| 19 | quit at ~10% | 1.3 | sonnet | solver stalled; a blank card taken for a green | [s:20261001-211823-chrono-2FYKPJ#6] |

Best 5.8 min (L6); every level from L7 is over the 5-minute budget (typical 14 min on L14–L18), so the
mechanic is `broken`. Where the time goes on L14–L18: the face-up first 60% takes ~4 min in batches; the
rest is greens opening as the board clears, about one reveal per frame and ~25 s per frame
[s:20261001-083725-chrono-2FYKPJ#73]. Make it fast (task `core-match-fast`): a solver that reads every face
(blank cards, gold, framed) and the tray, flips one green per round with a rescan, and certain pairs sent
as one call.
