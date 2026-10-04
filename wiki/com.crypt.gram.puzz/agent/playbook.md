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
  cryptogram-solver-phone) [lab 2026-10-01]. Level 1 of the 2026-10-03 install stalled with "no settled
  letter to type" and 2 cells of one number left (one letter typed by hand): the word list lacked about 12 000
  common words (its source drops every word that is also a common password). The lab added them; the same
  frames now type every cell, 0 wrong, the last number one cell per round ("single") [lab 2026-10-04].
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
  - The solver stops with "no settled letter to type" on a finished board too (0 numbered cells): the level
    is won, look for the win card. Run it only after the "Tap to continue" tutorial boxes of levels 1-2 are
    gone: it does not see them and would type under the box [lab 2026-10-04].
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
- Availability: the event was seen only on the 2026-10-01 install; a fresh install (2026-10-03, level 1)
  shows no event icon on home [s:20261003-201504-chrono-2FYKPJ#8]. Play it only when its entry appears.
- Pitfalls:
  - The board auto-scrolls when the cursor jumps to a low or hidden cell, so the later taps of a batch
    land on the wrong cells. Event level 1 was lost with 3 mistakes after 551 s and about 170 moves
    [s:20261001-050941-chrono-2FYKPJ#14] [s:20261001-050941-chrono-2FYKPJ#44] [s:20261001-050941-chrono-2FYKPJ#46].
    Keep one cell+card pair per call when the target or the next empty cell is below y~800 (730 px
    frame), and take a fresh shot after it.
  - The keyboard solver (`cryptogram`) refuses this board (no keyboard): use `card-cryptogram`, never
    `cryptogram`, here.
  - The frames of the only event level (session 20261001-050941) are no longer on disk: the
    `card-cryptogram` solver has never been checked on a real event board.
- Method: manual until the solver is checked; over the budget (task card-cryptogram-fast).
  `solvers/card-cryptogram.py` is a complete draft (same word list as `cryptogram`, with the 12 000 added
  words of lab 2026-10-04; reads word cards, thin digits, the 5-card hand and
  the draw pile; types at most one hand, 5 pairs, per round; deals a new hand at most 2 times in a row
  when no card has a settled letter; refuses any frame without the card panel: 12 of 12 menu frames of
  20261003-201504 refused). On the first event board of a session:
  1. dismiss tutorials, take a normal shot, then `sw.py solve card-cryptogram` WITHOUT `--run`: it only
     draws the moves. Check on the drawn frame that every cell tap is on an empty box and every card tap
     is on a card of the hand; mark the frame (counts only, never the letters).
  2. If the drawing is right: `sw.py solve card-cryptogram --run --rounds 6`, and again while it says
     `rescan`; note in `level end --note` how many pairs it placed and how many mistakes.
  3. If the drawing is wrong or it returns no moves: say which in the level note (the lab needs it) and
     play by hand with the pitfall rule above; the lab fixes the reading from those frames.

### Level times
| Level | Result | Time | Model | Note |
|---|---|---|---|---|
| event level 1 | lost | 551 s | opus | auto-scroll shifted cells, 3 mistakes [s:20261001-050941-chrono-2FYKPJ#46] |

## Dream 2026-10-04: corrections on the fresh install (3.6.1)

- The fresh install has no shop, currency or event entry at levels 1-2; the Chest Hunt, +20 hint pack and card event notes above come from the earlier install and are not verified here [s:20261003-201504-chrono-2FYKPJ#8].
- Level 1 is a tutorial with no Mistakes counter and no hint bulb; both arrive on level 2 (3 mistakes, bulb with 1) [s:20261003-234451-chrono-2FYKPJ#10] [s:20261003-234451-chrono-2FYKPJ#17]. So "use a hint when the solver stalls" does not apply on level 1.
- No interstitial after NEXT on the level-1 win card and none on START of level 2 [s:20261003-234451-chrono-2FYKPJ#16-17]. The in-level home icon quits for free [s:20261003-234451-chrono-2FYKPJ#19].
- Level 1: the solver stopped with "no settled letter to type" on one ambiguous number; two letters were then typed by hand [s:20261003-234451-chrono-2FYKPJ#13-15]. The lab's word-list fix is to be checked (task solver-l1-recheck).
- After opening a text field (Promo Code), take a fresh shot: the keyboard moves the dialog [s:20261003-201504-chrono-2FYKPJ#11].

| Level | Result | Seconds (win card) | Source |
|---|---|---|---|
| 1 | won (two letters by hand) | 113 (01:30) | [s:20261003-234451-chrono-2FYKPJ#15] |
