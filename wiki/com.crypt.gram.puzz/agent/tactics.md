---
game: com.crypt.gram.puzz
title: Tactics
type: agent
version_seen: 3.6.1
verified_at: 2026-10-02
sources: [20261001-020937-chrono-2FYKPJ, 20261001-050941-chrono-2FYKPJ, 20261001-071926-chrono-2FYKPJ, 20261001-114433-chrono-2FYKPJ, 20261001-192245-chrono-2FYKPJ, 20261001-224924-chrono-2FYKPJ]
---

# Tactics

## Decoding a quote
- Let the solver read the board where it exists; the player never writes the quote's words (see the
  [playbook](playbook.md)). Manually: decode the whole quote before typing, from one sharp shot: given
  letters, one-letter words (A or I), repeated-letter shapes and the shape of famous quotes. Level 9 was
  decoded in about 1 min, level 15 in about 20 s [s:20261001-020937-chrono-2FYKPJ#8]
  [s:20261001-071926-chrono-2FYKPJ#24].
- Keyboard colours are a free check: green = the letter is placed somewhere, grey = the letter is
  complete everywhere [s:20261001-020937-chrono-2FYKPJ#14].
- Count the dots of every lock before a batch: a one-dot lock is filled when the cursor reaches it, a
  two-dot lock is skipped and filled on the wrap-around. Mixing them up cost level 13 three mistakes in
  one batch [s:20261001-050941-chrono-2FYKPJ#72]; the retry with the dots counted was won
  [s:20261001-050941-chrono-2FYKPJ#79].

  > ⚠️ Previously (v3.6.1, 2026-10-01): "Lock icons hide a cell's number until the cursor reaches it;
  > typing straight through in cursor order opened all 4 locks of level 9". True for one-dot locks only
  > [s:20261001-050941-chrono-2FYKPJ#72].

- After a Restart, re-read the board: the locks move to other cells [s:20261001-050941-chrono-2FYKPJ#74].
- Keep a typing batch to one line or word group (5–13 taps): an interstitial can appear in the
  middle of a level and eats the rest of a long batch [s:20261001-020937-chrono-2FYKPJ#15]. On a solved
  short quote one batch is fine (level 14: 28 taps, 30 s) [s:20261001-050941-chrono-2FYKPJ#82].
- The quote can be longer than the screen (scroll bar on the right): the cursor scrolls the board, so
  read the new lines after each batch [s:20261001-071926-chrono-2FYKPJ#36].

## Card levels (Peter Pan event)
- One cell+card pair per call when the target or the next empty cell is low on the screen, and a fresh
  shot after it: the board scrolls by itself and later taps of a batch hit the wrong cells
  [s:20261001-050941-chrono-2FYKPJ#14] [s:20261001-050941-chrono-2FYKPJ#44].

## Interstitials
- Skip early: tap the skip icon at the top left (45,110) as soon as it shows, then Back once, then
  launch if the screen is blank. It reached level 16 three times; every wait of 45 s or more let the ad
  open the store and end on a card with no close [s:20261001-114433-chrono-2FYKPJ#17]
  [s:20261001-192245-chrono-2FYKPJ#15] [s:20261001-192245-chrono-2FYKPJ#10] [s:20261001-224924-chrono-2FYKPJ#11].
- A "Next" pill does not close an ad: the tap only hides the pill [s:20261001-224924-chrono-2FYKPJ#10].
  On a Zoodoku playable Next, skip and Back all failed: restart at once
  [s:20261001-114433-chrono-2FYKPJ#10].
- Daily Challenge from the main-screen card showed no interstitial: a way to play when level starts
  are walled [s:20261001-224924-chrono-2FYKPJ#14].
