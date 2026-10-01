# `same_as_prev` by perceptual hash alone: false "stuck" on board games, and batches that run into ads

Status: proposed by the dream (chrono, 2026-10-01). Change in `harness/sw.py` and `harness/perception.py`.

## The problem

`take_shot` sets `same_as_prev` when the 64-bit perceptual hash of the new frame is within 10 bits of
the previous one. A batch that removes two to six mahjong tiles, places a cat or types a line of letters
moves the hash by 2–10 bits, so the harness reports an unchanged screen while the board changes:

- Vita Mahjong 20261001-110957-chrono-2FYKPJ: `same: true` on 62 of 107 actions; from step 11 to step
  36 every batch (2–6 moves each, all of them played) came back `same: true` with hash distances of
  2–10 bits, the streak reached 15 and the reply said "stuck: end the session, end --status stuck" on a
  level that was being won [s:20261001-110957-chrono-2FYKPJ#14] [s:20261001-110957-chrono-2FYKPJ#37].
- Vita Mahjong 20260930-214524-chrono-2FYKPJ: 20 "unchanged" steps while the board changed
  [s:20260930-214524-chrono-2FYKPJ#106] [s:20260930-214524-chrono-2FYKPJ#131]; 95 of 179 actions `same`.
- Vita Mahjong 20260930-203959-chrono-2FYKPJ: `same` after popup selections and matches
  [s:20260930-203959-chrono-2FYKPJ#9] [s:20260930-203959-chrono-2FYKPJ#17].
- Pull the Pin 20260930-192115-chrono-2FYKPJ: `same` on visible changes [s:20260930-192115-chrono-2FYKPJ#6]
  [s:20260930-192115-chrono-2FYKPJ#11] [s:20260930-192115-chrono-2FYKPJ#18].
- Meowdoku 20260930-233055-chrono-2FYKPJ: `same` stays true while cats are placed
  [s:20260930-233055-chrono-2FYKPJ#21] [s:20260930-233055-chrono-2FYKPJ#24].
- Cryptogram 20261001-050941-chrono-2FYKPJ: `same` true for card swaps and typed letters that were real
  [s:20261001-050941-chrono-2FYKPJ#16] [s:20261001-050941-chrono-2FYKPJ#40].

Six sessions in four games; the player reported it as a harness gap three times. The cost: a wiki lesson
"do not trust `same: true`" exists, so the players ignore the flag — which makes the warning useless
exactly when a session really is stuck; `stats --by-model` reports `same_screen_rate` 0.40 for opus
(the Mahjong sessions) against 0.20 for sonnet (solver games), a difference of games, not of models.

The second half of the problem is the opposite case inside a batch: `run_moves` checks between moves
only which app is in the foreground. An interstitial drawn by the game's own ad SDK is the game, so a
30-tap keyboard batch kept typing into a playable ad [s:20261001-020937-chrono-2FYKPJ#15], and a batch
kept tapping cells after the board auto-scrolled [s:20261001-050941-chrono-2FYKPJ#44]; three mistakes
in one 29-tap batch cost a level [s:20261001-050941-chrono-2FYKPJ#72].

## The change

1. A second measure next to the hash: the share of changed pixels between the previous and the new
   frame (`changed_px` already exists for `solve --run`; make it a share of the frame, computed on the
   game area without the status bar). The reply gets `changed: 0.034`; `same_as_prev` is true only when
   the hash is within the threshold **and** the change share is under 0.5 %. The step record keeps both.
2. The "screen unchanged for N steps" warning counts only steps that are `same` by both measures; the
   "stuck: end the session" line fires at 15 such steps, as now. A streak that the hash calls same but
   the pixels call changed is reported as `small change: N steps` and never as stuck.
3. `stats`: `same_screen_rate` uses the new flag; add `small_change_rate` so board games stay comparable.
4. Long batches: in `run_moves`, for a batch of more than 10 moves, every 5 moves take a cheap frame
   (a downscaled screencap, about 0.5 s) and stop the batch when the change share against the batch's
   first frame exceeds 40 % — an ad, a popup or a scrolled board — with `stopped: "the screen changed a
   lot after move N: look before the rest"`. Inside a level a batch of certain moves changes a few per
   cent of the frame; an interstitial or a win screen changes most of it.

## How to test

- Replay: for every recorded session, recompute both measures over consecutive frames
  (`raw/<game>/<session>/shots/NNNNN.jpg` with the `same` flags in `steps.jsonl`). Target: in
  20261001-110957-chrono-2FYKPJ no step between 11 and 37 is `same` by both measures; in a session that
  really idled (a frozen ad: 20261001-020937-chrono-2FYKPJ steps 16–32) the steps stay `same`.
- Batch guard, without the phone: feed `run_moves` a stub device whose frames switch from a board to
  an ad frame after move 6; the batch stops at the next check with the `stopped` text.
- `sw.py stats --by-model` shows the two rates; the opus/sonnet gap in `same_screen_rate` shrinks.
