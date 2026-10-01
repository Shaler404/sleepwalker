---
game: com.crypt.gram.puzz
title: How to play
type: agent
version_seen: 3.6.1
verified_at: 2026-10-01
sources: [20261001-020937-chrono-2FYKPJ]
---

# How to play: Cryptogram: Word Logic Puzzles

The player reads this before every level and works in the local copy `state/com.crypt.gram.puzz/playbook.md`;
the dream merges it here. Level times: `sw.py playbook`.

## cryptogram: Number-coded quote
- Goal: fill every blank of a famous quote; each number is one letter (same number = same letter
  everywhere) [s:20261001-020937-chrono-2FYKPJ#8].
- Controls: the selected cell is green; tap a keyboard letter to fill it. A letter fills ONLY the
  selected cell, then the cursor jumps to the next empty cell and skips given letters. Arrows at the
  keyboard edges move to the previous/next cell [s:20261001-020937-chrono-2FYKPJ#11] [s:20261001-020937-chrono-2FYKPJ#14].
- Keyboard (730x1583 frame only — never use these on a `shot --hi` frame): row 1 y=1155 Q42 W114
  E186 R257 T329 Y400 U472 I543 O615 P687; row 2 y=1250 A74 S146 D218 F290 G363 H436 J508 K580
  L653; row 3 y=1345 Z150 X221 C293 V364 B436 N508 M580. A key turns grey when its letter is
  complete everywhere [s:20261001-020937-chrono-2FYKPJ#14].
- Rules: some letters are given (shown above the cell). Lock icons hide a cell's number; a lock opens
  once the cursor reaches it, so typing straight through works (level 9: 4 locks, 0 mistakes).
  Mistakes: 3 circles at the top; a wrong letter costs one. What 3 mistakes cost is not verified
  [s:20261001-020937-chrono-2FYKPJ#12] [s:20261001-020937-chrono-2FYKPJ#14].
- Risks: every typed letter is a guess that can cost a mistake; only type letters you are sure of.
  The "+20 / RSD 399" hint pack is just left of the board's bottom row: a tap there opens a real
  purchase sheet [s:20261001-020937-chrono-2FYKPJ#9].
- Method: manual. Decode the whole quote from one sharp shot (given letters, one-letter words,
  double letters, word shapes, famous quotes), write the number→letter map, then type in cursor
  order in batches of one line.
- Level plan: sharp shot, scroll if the quote continues below, decode, then one batch per line; take a
  fresh normal shot before the first batch and use its coordinates.
- Pitfalls: interstitials appear on PLAY and in the middle of a level; a playable ad (Bus Jam) had no
  close control — after 2 minutes try `sw.py restart` (not yet verified in this game) [s:20261001-020937-chrono-2FYKPJ#15] [s:20261001-020937-chrono-2FYKPJ#32].

### Level times
| Level | Result | Time | Model | Note |
|---|---|---|---|---|
| 9 | quit | 581 s | opus | decoded in about 1 min, typed about 60 letters in about 2 min with 0 mistakes, then an unclosable ad took the rest [s:20261001-020937-chrono-2FYKPJ#32] |
