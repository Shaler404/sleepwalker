---
game: com.crypt.gram.puzz
title: How to play
type: agent
version_seen: 3.6.1
verified_at: 2026-10-02
sources: [20261001-020937-chrono-2FYKPJ, 20261001-050941-chrono-2FYKPJ, 20261001-071926-chrono-2FYKPJ, 20261001-092740-chrono-2FYKPJ, 20261001-114433-chrono-2FYKPJ, 20261001-190315-chrono-2FYKPJ, 20261001-192245-chrono-2FYKPJ, 20261001-224924-chrono-2FYKPJ]
---

# How to play: Cryptogram: Word Logic Puzzles

The player reads this before every level and works in the local copy `state/com.crypt.gram.puzz/playbook.md`;
the dream merges it here. Level times: `sw.py playbook`. Budget: 5 min per level.

**Never read, decode or write the quote text.** Four sessions on level 16 (071926, 092740, 114433,
192245) ended with the model's output blocked by the content filter right after the level 16 board
loaded, losing their notes and the rest of the plan [s:20261001-071926-chrono-2FYKPJ#69]
[s:20261001-092740-chrono-2FYKPJ#9] [s:20261001-114433-chrono-2FYKPJ#18] [s:20261001-192245-chrono-2FYKPJ#17].
Do not put any word of a quote in plans, `--why`, level notes, marks or the summary; refer to a level
by its number and to letters by counts.

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
- Rules: some letters are given (shown above the cell). Key icons above cells are Chest Hunt keys, not
  locks: the cursor fills them normally [s:20261001-071926-chrono-2FYKPJ#24]. Lock icons hide a cell's
  number. A **one-dot** lock takes the next letter when the cursor reaches it; a **two-dot** ("double
  locker", from level 10) is skipped and opens when the letters on both sides are right, so it is
  filled on the wrap-around [s:20261001-050941-chrono-2FYKPJ#54] [s:20261001-050941-chrono-2FYKPJ#72].
  Restart moves the locks to other cells [s:20261001-050941-chrono-2FYKPJ#74].
- Mistakes: 3 circles at the top; a wrong letter costs one. 3 mistakes end the level: popup "You will
  lose: heart -1" with Home, Restart and REVIVE (rewarded ad); Home and Restart both cost a life, a life
  regenerates in 30 min [s:20261001-050941-chrono-2FYKPJ#44] [s:20261001-050941-chrono-2FYKPJ#47]
  [s:20261001-050941-chrono-2FYKPJ#83]. REVIVE never started an ad on this device (3 taps) — do not count
  on it [s:20261001-050941-chrono-2FYKPJ#73].

  ![3 mistakes on a level: 'You will lose: heart -1', Home, Restart and REVIVE (rewarded ad)](../img/20261002-lives-three-mistakes-d4d47a7a.webp)

- Method (on chrono): solver. `sw.py solve cryptogram --run --rounds 6` — each round reads the board,
  types the letters it is sure of (a tap on the cell, a tap on the key) and stops before a tap that
  would scroll the board; the next round reads the scrolled board. Run it again while it says `rescan`
  and cells are left. The solver's note holds counts only; quote it. The solver was checked on 25
  recorded boards of levels 9-14 (about 340 cells, 0 wrong) but has not won a level on the phone yet,
  so it lives only in `state/com.crypt.gram.puzz/solvers/` on chrono and is not published (task
  cryptogram-solver-phone) [lab 2026-10-01].
- Method (manual, proven on levels 9-15, the Daily Challenge and the secret level, 9 wins out of 10
  tries): decode the whole quote from one sharp shot (given letters, one-letter words, double letters,
  word shapes), keep the number→letter map to yourself, then type in cursor order: single locks in
  order, double locks on the wrap-around. 2-5 batches per level, 0.5-3 min
  [s:20261001-050941-chrono-2FYKPJ#82] [s:20261001-071926-chrono-2FYKPJ#36]. Use it only where the
  solver is missing, and never write the decoded words anywhere (see the warning above).
- Level plan: tap START/CONTINUE/PLAY; if an interstitial starts, tap its skip icon at the top left
  (45,110) as soon as it shows, then Back once, then launch if the screen is blank (the route that
  reached level 16) [s:20261001-192245-chrono-2FYKPJ#15] [s:20261001-192245-chrono-2FYKPJ#17]; dismiss
  popups ("Tap to continue" tutorials dim the board; the solver refuses a dimmed board), take a normal
  shot so the board is settled, count the dots of every lock, then the solver (or the manual batches).
  When the solver returns no moves ("no settled letter to type"): use a hint (the bulb with a count at
  the bottom right; what it reveals is not verified) and run the solver again, or `level end --result quit`;
  never type a letter by hand. After the last letter a card with the quote and its author appears: do
  not read or describe it, tap its button (CLAIM/NEXT) and go on.
- Pitfalls:
  - A one-dot lock treated as two-dot: level 13 lost 3 mistakes in one 29-tap batch [s:20261001-050941-chrono-2FYKPJ#72].
  - A quote longer than the screen (scroll bar on the right): the cursor scrolls the board; read the new
    lines after each batch (Daily Challenge Oct 1: 11 lines, 7 batches) [s:20261001-071926-chrono-2FYKPJ#36].
  - The "+20" hint pack at the bottom left ($2.49 / RSD 399) opens a real purchase sheet: never tap there
    [s:20261001-020937-chrono-2FYKPJ#9].
  - Interstitials appear on PLAY/CONTINUE, after CLAIM and NEXT on win screens, on Secret Level PLAY and
    once mid-level; keep a batch to one line (an ad eats the rest of a long batch)
    [s:20261001-020937-chrono-2FYKPJ#15]. Once a level is won, restart at once if an ad with no close
    follows NEXT: the win stays counted [s:20261001-071926-chrono-2FYKPJ#41] [s:20261001-071926-chrono-2FYKPJ#59].
  - Level times on the win card ("Level Time") are longer than the logged time (01:24 vs 58 s); use the
    logged time [s:20261001-071926-chrono-2FYKPJ#24].

  ![Level 10 tutorial: a double locker (two dots) opens when the letters on both sides are right; single locks and Chest Hunt key cells on the same board](../img/20261002-double-locker-tutorial-c56b3991.webp)

### Level times
| Level | Result | Time | Model | Note |
|---|---|---|---|---|
| 9 | quit | 581 s | opus | typed about 60 letters in about 2 min with 0 mistakes, then an unclosable ad took the rest [s:20261001-020937-chrono-2FYKPJ#32] |
| 9 (resumed) | won | 57 s | opus | 2 batches, 0 mistakes [s:20261001-050941-chrono-2FYKPJ#52] |
| 10 | won | 136 s | opus | first double locks, 1-tap probes, 3 batches [s:20261001-050941-chrono-2FYKPJ#60] |
| 11 | won | 58 s | opus | 2 batches, locks on the wrap [s:20261001-050941-chrono-2FYKPJ#64] |
| 12 | won | 85 s | opus | 3 batches [s:20261001-050941-chrono-2FYKPJ#69] |
| 13 | lost | 73 s | opus | one-dot lock typed as two-dot, 3 mistakes [s:20261001-050941-chrono-2FYKPJ#73] |
| 13 (retry) | won | 138 s | opus | locks moved after Restart; 5 batches, 1 mistake [s:20261001-050941-chrono-2FYKPJ#79] |
| 14 | won | 30 s | opus | one 28-tap batch [s:20261001-050941-chrono-2FYKPJ#82] |
| 15 | won | 58 s | opus | 3 batches, 0 mistakes [s:20261001-071926-chrono-2FYKPJ#24] |
| Daily Challenge Oct 1 | won | 177 s | opus | 11 lines, 7 batches, 0 mistakes [s:20261001-071926-chrono-2FYKPJ#36] |
| Secret level 1 | won | 100 s | opus | 3 batches, 0 mistakes [s:20261001-071926-chrono-2FYKPJ#57] |
| 16 | not played | — | opus, sonnet | board reached 3 times via skip icon + Back, every session then crashed on the output filter (above); 2 sessions never got past the ads |

Typical 1.4 min, best 0.5 min: within the budget (`sw.py playbook`).

## card-cryptogram: Peter Pan event "Special Game"
- Goal: the same number-coded quote, but letters come from a hand of 5 "Available Letters" cards and a
  draw pile instead of a keyboard: tap a cell, then a card [s:20261001-050941-chrono-2FYKPJ#7].
- Controls: the hand refills by itself when empty; tapping the draw pile with cards left deals a new
  hand [s:20261001-050941-chrono-2FYKPJ#41]. Event levels carry 5 picture pieces at levels 1, 3, 5, 7
  and 10 of chapter 1 [s:20261001-092740-chrono-2FYKPJ#1].
- Entry: the first visit is a forced tutorial — Home and Back do nothing until START LEVEL 1
  [s:20261001-050941-chrono-2FYKPJ#6].
- Pitfalls: the board auto-scrolls when the cursor jumps to a low or hidden cell, so the later taps of a
  batch land on the wrong cells. Event level 1 was lost with 3 mistakes after 551 s and about 170 moves
  [s:20261001-050941-chrono-2FYKPJ#14] [s:20261001-050941-chrono-2FYKPJ#44] [s:20261001-050941-chrono-2FYKPJ#46].
  Rule until a solver exists: one cell+card pair per call when the target or the next empty cell is
  below y~800, and a fresh shot after it. The solver refuses this board (6 big keys).
- Method: manual; over the budget (task card-cryptogram-fast). The lab's solver draft for it crashed
  mid-edit on 2026-10-01 and is not verified.

### Level times
| Level | Result | Time | Model | Note |
|---|---|---|---|---|
| event level 1 | lost | 551 s | opus | auto-scroll shifted cells, 3 mistakes [s:20261001-050941-chrono-2FYKPJ#46] |
