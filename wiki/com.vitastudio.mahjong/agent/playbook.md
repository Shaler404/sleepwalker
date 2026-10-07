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
- Tile set (3.40.1, session 20261003-195050): the board shows lavender faces with purple side bands and PURPLE
  face-down backs with a flower circle (the "greens" below), although the Theme screen shows "Simple" (green back)
  selected; L19 also has zodiac tiles (Pisces, Gemini, Aries, Capricorn, ...), ordinary pairs. Sessions 231301 and
  231804 (same day, same L19) showed a THIRD set: pink-cream faces, pink and dark red side bands, RED face-down backs
  with a lotus or a lattice medallion; the L19 layout changed between launches. Do NOT switch the theme to get the
  old look: the solver reads all three sets (its note starts "cream", "purple" or "red tile set"). A FOURTH set
  (sessions 20261005-002327, L19, and 073804, L20 Hard): mint faces (234,248,222) with light and mid green side
  bands, GREEN backs with a flower or lattice medallion; the solver reads it too (note "green tile set"). The set
  changes between launches and levels: never assume one. A FIFTH set (session 20261005-133525, Hard L20): white faces
  (230,241,247), light and dark blue side bands, BLUE backs (72,96,222) with corner ornaments; until lab 2026-10-05
  (2nd) the solver took it for purple and read no pair; it now reads it (note "blue tile set"). A SIXTH set (session 20261005-221108, L21):
  warm cream faces (251,244,225) with tan and orange-brown side bands, ORANGE backs with a light flower; until lab
  2026-10-05 (3rd) the solver called it "cream", missed the rabbit pair and took the 8 orange backs for 4 art pairs
  (an 8-tap line of back flips); it now reads it (note "orange tile set"). A set it does not know yet whose backs
  read as one-colour faces is refused ("unknown tile set"): play by hand and leave the frames for the lab.
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
- Method: solver first: `sw.py solve core-match --run --rounds 40 --settle 2` from the level's first frame; it keeps
  its memory (greens seen, last board) between rounds. When it stops, read its note, do what it says (Hint lit pair,
  Shuffle, a video hint) and run it again. The manual loop below is the fallback, per frame:
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
- Solver (`state/com.vitastudio.mahjong/solvers/core-match.py`): reads the screenshot, remembers greens between
  rounds, flips one free green per round, taps Hint when nothing is certain. Lab 2026-10-03: it saw NO tile on the
  purple L19 board (all checks were on cream frames); it now maps the purple set onto the cream colours before
  reading. On 195050/00022 it reads 9 open tiles (2 backs) and plays Gemini pair, Capricorn pair, then flips the
  top-left purple back. Lab 2026-10-03 (2nd): on the red set it read the faces as cream but merged them (5 of 9 open
  tiles, no backs); it now maps the red set too: 231301/00022 9 of 9 open tiles (Scorpio, Capricorn, Pudding pairs),
  231804/00008 14 open tiles with the 4 free red backs, the Hint-lit pair (00009), the lit twin of a tray tile
  (00010) and a Shuffle (00012) read right. Red glyphs (Capricorn, yin-yang) are never taken for backs. In the red
  set a tile beside a picture tile (teapot) may read "side unknown" and wait: harmless, it is free only when it
  pairs anyway. Pitfalls in the purple and red sets, not yet seen on any frame (check them on the phone):
  - the Hint tint on lavender faces and on purple and red backs (on red-set faces it reads): if the round after a
    Hint tap says "no lit pair read after the Hint", tap the lit pair by hand from the frame and run again;
  - a flipped red back (its face shown in place) and the tray match in the red set: not on any frame yet;
  - the grey of a tile tapped while locked ("Locked by left and right") may not read as locked;
  - tray tiles: a tray face that reads "?" is only a single the solver will not pair: look at the tray.
  Earlier: stalled on the L18 resume frame [s:20261001-205148-chrono-2FYKPJ#1]; missed a blank-card pair on the
  cream L19 [s:20261001-211823-chrono-2FYKPJ#3]. Task `core-match-fast`.
  Lab 2026-10-05 (frames of 002327, 073409, 073804), fixed in the solver:
  - the green set read nothing ("no open tile face"): now mapped like the others; L19 and L20 frames read with
    their backs, the flipped back (face-up green) and its twin;
  - purple backs were missed (box 3 px taller than the cream rule), so a tile between two backs read FREE (073804
    step 20: the 八 between two backs, the twin went alone into the tray): backs now read, the 八 reads locked;
  - the purple Hint (cyan faces, BLUE backs) was not read: 5 hand-tapped Hint pairs on L19. Now read, also the
    pale phase and a lit tile showing only its top strip above its lit twin (cascade: the lower drawn one first);
    a lit ART pair (wood frame turns cyan-white) is read by comparing with the frame before the Hint tap;
  - two lions (red set) and two 9-bamboos (purple) were read as different kinds (shade correction, a 2 px box
    offset): fixed, the 9-bamboo pair cost a Hint on L19;
  - the "Watch out! Don't let the holder get full!" bubble (tray at 3, first time after a launch) refused the
    frame: the solver now taps the bubble to close it. A tile tap sent while it shows is lost.
  Run the solver for the whole level: `solve --run --rounds 40 --settle 2`, and run it again after anything you
  tap yourself. Hand taps only for what its note asks (a video offer, Shuffle).
  Lab 2026-10-05 (2nd, frames of 133525, Hard L20 blue set), fixed in the solver:
  - the blue set read as "purple" (its white face lies within 16 of lavender) and no face was mapped: 10 open tiles,
    no pair on a board with the 4-circle pair free. Now its own set (`_blue_to_cream`): 133525/00006 reads 13 open
    tiles and the 4-circle pair; backs read with their 157x195 box, including a back shaded at the top;
  - a back (or face) cut at the bottom by the next row from the right with a deeper notch at the very corner was
    refused (133525/00024, the back over the bird): the notch now counts as part of the cut.
  Not seen on any blue frame: the Hint tint on white faces and blue backs (if "no lit pair read after the Hint",
  tap the lit pair from the frame and run again). Seen on 133525/00006: the top-right tulip, its lower left
  covered in drawing order by the next row, reads as not open (the session played it): harmless, it waits.
  Lab 2026-10-05 (3rd, frames of 221108, L21 orange set): new `_orange_to_cream`; 221108/00010 and 00014 read 15 open
  tiles (7 faces, 8 free backs) and play the rabbit pair, then flip the top-left back. Not on any frame: a back
  shaded by a higher tile (the back rule needs r >= 190: a shaded back may read as nothing and its neighbour as
  free), the Hint tint, the tray in this set, the red "x2" corner badges (read as ordinary faces) and the L21
  spinning tiles ("Clear every tile to stop the spin!"): if the board moves between frames, the solver's taps miss;
  look at two frames 1 s apart before the first batch.
  Still open (check on the phone): the Hint tint in the green and red sets on backs; a lit art tile that is
  also partly covered.
  Lab 2026-10-06 (frames of 073804, 133525, 001538): Hints are at 0 ("+" badge) on every board since 073804/00044
  (L20, L21 too). Before, a dead end tapped Hint, the "Free Hint" video offer came up and `solve --run` stopped
  ("gave up", 073804 step 53, L20 quit). Now the solver reads the booster badges: Hint "+" and a count on Shuffle ->
  it taps SHUFFLE itself (note "Hint at 0: tap Shuffle"); the Free Hint offer on screen -> it taps the X. Both at 0
  or a Shuffle that changed nothing -> no moves, note "Hint at 0 and ...": take the Get Two video by hand (or Undo a
  tray single) and run again. Pitfalls:
  - start `solve --run` from a SETTLED frame: on the very first look the solver cannot tell a match/Combo animation
    from a dead end and may spend the Shuffle on it (133525/00043-45, stateless). Inside a run it compares with the
    last frame and waits ("not spent on a moving board": just run again);
  - it shuffles with 3 in the tray too (073804/00047); the session Undid one first: either works, the next round
    plays only tray matches.
  - L21 (orange set, 001538/00015): the solver plays the fox pair the session tapped by hand, then flips the
    top-left back. Do not tap pairs by hand to "look": `solve --run` does it as fast and the lab counts hand taps.
  Lab 2026-10-06 (2nd, frames of 022624): L21 came back in the PURPLE set with the same layout as the orange one
  (faces dealt differently). The solver reads it (14 open tiles, 8 free backs; red fan pair, then the top-left back),
  but missed the free "book" picture tile (cat in an armchair, wood frame with page edges on its right): such tiles
  are drawn ~6 px wider and ~5 px taller than a face. It now reads them in every set but cream (also the rabbit card
  of the green set, 002327/00009). Pitfalls:
  - a book tile in the TRAY with its twin free on the board is not on any frame: if the note shows the tray as "?"
    while the twin is free, tap the twin by hand and run again;
  - a level opened only to study menus (Options, Theme) is still a level: every Options tap counted as a hand-placed
    move (022624, 24 taps) and kept core-match flagged "bypassed". Open menus from Home where possible, or end the
    level with a note "menus only, no tiles played".
  Lab 2026-10-06 (3rd, frames of 072809, L21 spin, cream faces with green backs): the solver now knows the SPIN ring.
  - It learns per level that the board spins: open faces of the last frame found again whole cells away after a
    take. From then on its note says "SPIN: N open tiles may turn with the ring". It learns which cells hold still
    (a face read in place after a take, or the inner cells once the ring's two rows and two columns have been seen
    moving) and plays a line with at most ONE tile that may move, as its FIRST tap; after it only tiles that hold
    still (higher layer, inner cells, the stacks). A pair whose two tiles both ride the ring: one tile now ("spin: a
    free pair the ring may move"), its twin from the tray next round. After every take it forgets the faces of
    backs that may have turned (they may be another back now) and flips them again. A Hint-lit pair on the ring:
    one tile per round.
  - Backs of the lower row with a green lip under them (232 px tall, 072809/00058-00073) were not read at all: the
    endgame said "no certain pair" with 3 free backs on the board. Read now.
  - Method on L21: `solve --run --rounds 40 --settle 2` from a settled first frame, as everywhere. The ring is
    learnt only once ring faces are open and move: until the first "SPIN" note the solver plays as on any level
    (on 072809 the open faces at the start were all higher-layer, inner or stacks, so that was right).
  Pitfalls (not on any frame yet):
  - a frame taken while the ring still turns: faces between cells are not read; if a round says "fewer open tiles
    ... animation", just run again (a longer --settle helps);
  - a Shuffle on a spinning board (072809 step 17) re-deals everything: the solver forgets the cells and learns
    them again (one or two slower rounds);
  - the free side of an inner tile next to the ring: it is tapped after a take only when the cell beside it is known
    to hold still; a "Locked" tap there is harmless (nothing moves).
  Lab 2026-10-06 (4th, frames of 101909, L22 opened twice, no tiles played): two new looks, both read now.
  - Classic set (Theme > Tiles > Classic, on a RED table): the cream face itself with blue side bands and light blue
    backs with a flower. Before, the solver called it "cream" and took the two free blue backs for an art PAIR (a
    2-tap line of back flips); now note "classic tile set": 101909/00012 plays the rice pair and the 二萬 pair, then
    flips the right blue back. The red table beside a tile read as a neighbour (a board-edge tile read locked on
    that side): it now reads as table, like the dark green one.
  - Red set with BAMBOO backs (on a dark green table, after the relaunch): gold 福 tiles with a red "x2" ribbon on
    the top-right corner were not read at all (the ribbon breaks the tile's outline, its fold looks like a neighbour
    on the right): 101909/00022 said "no certain pair ... take the video". Now it reads both gold tiles and plays the
    gold pair. The bamboo strokes on red backs run off the back's edge; they are filled into the back now.
  - Hint and Shuffle both at "+" (0) on L22: on a real dead end the solver stops ("Hint at 0 and Shuffle at 0"):
    take the Get Two video by hand, then run it again.
  Pitfalls (not on any frame yet): a FREE bamboo back (only covered ones so far: if a tile beside a red bamboo back
  reads free and its tap says "Locked", the back was missed); the Hint tint and a flipped back in the Classic set;
  an x2 gold tile in the tray. A level opened only to look at the board (no tiles) still counts as hand moves: end
  it with "menus only, no tiles played" as 101909 did.
  Lab 2026-10-06 (5th, frames of 122751, L22 red set and L23 purple set): the hand pairs of that session are read now.
  - The red set's dark side band has pixels just outside the mapped red (g/r 0.29): they read as a right neighbour, so
    raised top tiles (the blue vases, the top-row 9-circle) read "locked by left and right". Mapped now: 00009 plays
    the vase pair, 00025 the 9-circle pair.
  - Art cards were compared only at even pixel offsets: the two coffee cards (1 px apart) were two kinds. Now every
    pixel: 00009 plays the coffee pair, 00010-00011 the latte and vase-bird pairs the session tapped by hand.
  - A picture card on a white ground (L23 rabbit with roses) reads as a cream face while its twin reads as art: the
    two could never pair. Now compared in art mode over 5 px: 00071 plays tray twin, rabbit pair, 5-circle and
    9-circle pairs (the session's hand batch plus one pair).
  - A dense face matched only 2 px off (the 9-circles, 0.0% shifted, 12% unshifted) was refused: accepted now when
    the shifted match is near perfect.
  Method on these boards: `solve --run --rounds 40 --settle 2` from the first settled frame, as everywhere; no art
  pairs by eye first. Dead ends with Hint and Shuffle at 0 and two unknown tray singles still stop the run (note
  "Hint at 0 and Shuffle at 0"): take the Free Shuffle video by hand, then run again.
  Pitfalls:
  - a lower tile running on under a top tile (a gold card, a red back) beside its LEFT edge still reads as a
    left neighbour: such a top tile is taken only when its right side is open. A back's deep red band and a lower
    back look alike in the gap; the solver keeps the safe side;
  - `solve --run` dies with a raw `AdbError` traceback when adb loses the phone for a moment (122751 steps 17 and
    45): not a solver fault; wait for the phone (`sw.py` status) and run it again from a fresh frame.

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

## Dream 2026-10-04: corrections (3.40.1)

- Face-down tile backs are not always green: on 3.40.1 L19 showed purple, then red backs (and a different layout after a relaunch) [s:20261003-195050-chrono-2FYKPJ#17] [s:20261003-231301-chrono-2FYKPJ#15] [s:20261003-231804-chrono-2FYKPJ#4]. Re-read the board after every relaunch.
- Every relaunch so far showed Level 1, the age popup and the saved-game offer: Start Over leads to a No/Yes confirm, and Yes may delete the cloud save. Take Sync Data; never tap Start Over [s:20261003-231301-chrono-2FYKPJ#1-4].
- Android Back does nothing in a level and on the medal detail: use the on-screen back arrow (50,110) or tap outside [s:20261003-231301-chrono-2FYKPJ#12-13] [s:20261003-231301-chrono-2FYKPJ#21].
- Boosters at L19: Shuffle 3, Hint 5 (lights a pair in cyan), Undo 10 (returns the tray tile); Shuffle seems to reveal backs [s:20261003-231804-chrono-2FYKPJ#4-8].
## Session 20261005-073409 (sonnet play): L19 opened again: dense red-set board (lotus, scorpio, lion, picture tiles), layout new again. Not played: mechanic is broken. Study core-level (chk-win) and hard-level need a won level: handoff to core-match.

## Session 20261005-073804 (opus study): L19 won in 14.2 min, Hard L20 started
- L19 (purple set) won: solver played 38 moves in 11 rounds (2 min), then stalled on Hint-lit pairs it does not read
  (picture cards, a back lit with its twin, two stacked 3-circles); tapping the lit pair by hand from the frame worked every time.
- Solver errors on the purple set: (1) it took a tile flanked by same-layer purple BACKS as free (八 "Locked by left
  and right") and put singles in the tray; (2) it paired a vertical blue 8-circle with a 9-circle (look-alikes). Fix:
  count backs as same-layer side blockers; separate 8- and 9-circle by the column count.
- Manual loop that was fast on the endgame: one frame, 5-8 taps per batch at row ENDS (left/right edge tiles are free),
  tray twins first; a flipped back + its free twin = one batch ("flip, then twin" clears both, no tray).
- Flipping a back whose twin is already in the tray cleared both at once (bird, step ~38).
- Hint lights a back in cyan together with its twin: flip the back, then tap the twin.
- Shuffle with 2 tray singles gave both twins free at row ends right away.
- Hard L20 (green set, cream faces): solver read it well (13 moves in 3 rounds, 0 errors); it stopped at the Free Hint
  video offer (Hint at 0). The back arrow keeps the board and IQ.

## Session 20261005-133525 (opus study): Hard L20 won by hand (~15 min session time)
- A FIFTH tile set: white faces, BLUE backs with a white scroll border (Hard L20 after the league matchmaking).
  The solver called it "purple" and found no pair on a board with 4+ certain pairs: play by hand (task solver-white-blue).
  Fixed by the lab the same day: the solver reads the blue set; use `solve --run` on it like the others.
- Fast loop that won it: one frame, then batches of 4-12 taps of certain pairs at row ENDS and on top tiles; flip a
  free back as the last tap of a batch, then its twin. All 8 back flips in the endgame were followed by a free twin.
- A seen back (face shown earlier, now down again) + the same kind face up elsewhere: tapping the seen back clears
  both, no tray (red wheel pair, frame 00039).
- Errors that cost two Out of space: (1) a 9-circle at the board edge taken for a 7-circle - count the dot rows;
  (2) a tap on a tile next to a RAISED tile (drawn larger, with a deep shadow) hit the raised one: aim at the far
  side of the lower tile or skip it. "-4 to revive" spends 4 Undos and returns the 4 tray tiles to their places.
- Shuffle with 2 tray singles and no free twin opened 10 pairs at once (again).
- The game clock on the win screen counts the time across sessions (15:31 for L20 across two sessions).
- L21 adds spinning tiles ("Clear every tile to stop the spin!"): unknown mechanic, read its rules before playing.

## Session 20261006-072809 (opus study): L21 won, spin rule found
- SPIN (L21, "Clear every tile to stop the spin!"): a ring of LOWER-layer tiles along the board's edge (top row,
  both side columns, bottom row) turns one place CLOCKWISE after every tile that leaves the board: a tray take
  (single or pair), a match, a flip-and-twin clear. A flip of a back or a locked tap does NOT turn it. Yellow
  chevrons on the ring show the direction (left side up, right side down). Top-layer tiles and the bottom stacks
  never move. Shuffle re-deals the ring with the rest.
- Method on spin boards: in a batch put at most ONE ring tile, as the FIRST tap; the rest of the batch only
  top-layer / stack tiles (they do not move). After a ring take, look before the next ring tap: its twin has moved
  one place. Taps sent while the ring turns hit whatever moved under them (shot 22).
- The solver did not model the ring in this session (stalls: "animation hides some", "no certain pair"). Lab
  2026-10-06 (3rd) taught it the ring and the lipped backs of the lower row: run `solve --run` on L21 too (see the
  Method note above); hand taps only for what its note asks.
- The free Shuffle (badge 1) at a dead end with one tray single gave 6 pairs at once.
- A tap on a seen back flips it face up again (no tray) in this green set; tap it a second time to take it.

## Session 20261006-101909 (opus study): theme vs tile set
- The Theme picker drives the board right after Confirm (Classic = white faces, blue sides and backs; red background).
  After a force-stop relaunch the picker is back to Simple + dark green, and the next board drew the RED-back set on a
  dark green background: the tile set on a board does not follow the picker after a relaunch. Never assume a set; the
  solver reads all of them.

## Session 20261006-122751 (opus study): L22 won in 12.8 min (red set, art tiles)
- Boosters at L22 start: Shuffle 0, Hint 0, Undo 1. All three at 0 open a video offer (Shuffle: 1 per video; Hint, Undo: 2).
- The solver did NOT read the blue-vase pair or the art cards (coffee, latte, vase-bird) on the opening red-set frame
  (shot 9: "no certain pair" with the vase pair free on top). Fixed by lab 2026-10-06 (5th): run `solve --run` from
  the first frame, no art pairs by eye.
- Fast hand loop that worked: 4-6 taps of art/face pairs, uncertain tile first; a flipped back that turns face down
  again is a "seen" back: tap it (goes to the tray) then its twin.
- Dead end with Hint and Shuffle at 0 and 2 tray singles: Free Shuffle video (playable end card with no X: `launch`,
  the Shuffle was granted), then `solve --run` cleared the last ~40% in 38 moves.
- L23 (purple set) is a SPIN board too (the solver's note said "SPIN" after the first takes): take the top-layer
  twin of a tray tile alone, then look before the next ring tile.
- Auto Complete check: run the solver in short runs (`--rounds 3`) near the end so a frame with every tile
  uncovered is left idle for 5 s; a full `--run` clears the rest itself before the game could.

## Level times by mechanic (dream 2026-10-07)

```yaml
---
mechanics:
- id: core-match
  name: core-match
  status: broken
  method: solver
  solver: solvers/com.vitastudio.mahjong/core-match.py
  levels:
    won: 4
    lost: 1
    quit: 11
  typical_min: 17.5
  best_min: 13.3
  solver_file: solvers/com.vitastudio.mahjong/core-match.py
  solver_sign: 'solver bypassed: 2 of 5 levels placed by hand; solver gave up in 3
    of 5 levels (no moves, the same moves, or no change on screen)'
level_budget_min: 5
```
