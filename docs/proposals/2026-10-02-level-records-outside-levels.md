# Levels played outside a `level start … level end` pair leave no record, and late starts shorten the times

Status: proposed by the dream (chrono, 2026-10-02). Change in `harness/sw.py` (`cmd_taps`/`cmd_tap`/`cmd_solve`,
`cmd_level`, `finish`, `cmd_stats`, `level_spans`, `bench_rows`). Extends
`2026-10-01-level-end-evidence.md` (a won level needs a frame): that proposal guards the end of a level, this
one guards its start and the moves that happen with no level open.

## The problem

The level record is the player's claim: `level start` and `level end` are optional, nothing ties the moves to
them, and the harness never says "you are playing with no level open". The counters that everything else
reads (`research.yaml` mechanics, `sw.py playbook`, `stats`, the lab's `level-frames`, `level-catalog`, the
benchmark report) are wrong in three games:

- **Wins never recorded.** MeowTrail 20261001-070939-chrono-2FYKPJ: one `level_start` ("level 56") at
  [s:20261001-070939-chrono-2FYKPJ#9], six `progress` ops for the wins of 56–61, and one level op "level 56
  quit 407 s" at [s:20261001-070939-chrono-2FYKPJ#27]: `session.json` says 0 won. MeowTrail
  20261001-143237-chrono-2FYKPJ: L81 and L82 won [s:20261001-143237-chrono-2FYKPJ#7]
  [s:20261001-143237-chrono-2FYKPJ#14], both recorded `quit`. Meowdoku 20261001-093348-chrono-2FYKPJ: 3 level
  ops for 28 `taps`/`solve` steps — 17 levels and 4 golden boards played, 3 recorded
  [s:20261001-093348-chrono-2FYKPJ#6] [s:20261001-093348-chrono-2FYKPJ#13] [s:20261001-093348-chrono-2FYKPJ#31].
- **Wins with no moves.** MeowTrail 20261001-100940-chrono-2FYKPJ: `level_start` "level 77" and `level end
  won` in the same step, 5 s, 0 moves [s:20261001-100940-chrono-2FYKPJ#28]; the level was solved at
  [s:20261001-100940-chrono-2FYKPJ#30]. The mechanic's `best_s` is this 5 s. Meowdoku
  20261001-060942-chrono-2FYKPJ: L46 won after 10 s and 0 moves on an ad frame [s:20261001-060942-chrono-2FYKPJ#20].
- **Start after the reading.** Meowdoku bench slot 20261001-184651-chrono-2FYKPJ: `level_start` at
  [s:20261001-184651-chrono-2FYKPJ#3], the only move batch and the win at [s:20261001-184651-chrono-2FYKPJ#4]
  — the board was read before the start, so the slot reads 23–26 s a level against 47–52 s from the Level tap,
  and the benchmark compares it with slots that started the clock before the solver.
- **Bonus boards named as levels.** Meowdoku bench slots 20261001-180616-chrono-2FYKPJ (a golden board
  recorded as "L99" [s:20261001-180616-chrono-2FYKPJ#19], the real L99 as "L100"
  [s:20261001-180616-chrono-2FYKPJ#26]), 20261001-181422-chrono-2FYKPJ [s:20261001-181422-chrono-2FYKPJ#13],
  20261001-182810-chrono-2FYKPJ [s:20261001-182810-chrono-2FYKPJ#10] [s:20261001-182810-chrono-2FYKPJ#15]:
  every later label in the slot is off by one, and `level-catalog` shows the wrong board under the number.
- **Losses fixed by a retry are invisible.** Pull the Pin 20261001-164104-chrono-2FYKPJ: L23 stage 4 lost at
  [s:20261001-164104-chrono-2FYKPJ#3], won after Retry Stage [s:20261001-164104-chrono-2FYKPJ#9]; the
  session records 4 won, 0 lost.

Three games, nine sessions; the editors marked the level statistics of MeowTrail, Meowdoku and Pull the Pin as
unreliable in `agent/metrics.md`. The session runbook gets the rules in this PR; the harness should make the
gaps visible instead of trusting the claim.

## The change

1. **Moves with no level open.** `tap`, `taps`, `swipe`, `solve` and `skill run` on a game that has
   mechanics with levels (`research.yaml` → `mechanics` not empty) and no open level add the warning
   "no level is open: these moves are in no level's time (`level start` first)" and count
   `moves_outside_level` in the session. `finish` writes it into `session.json`; `stats` shows it per session
   and per game; the dream's metrics line gets it.
2. **Late start.** `level start` records `moves_before`: the moves and `solve` calls since the last level op
   (or the session start). When it is more than zero, the reply says "N moves since the last level end are
   not in this level; the clock starts now" and the step keeps the number; `level_spans` and `level-catalog`
   take the start frame from the first frame after the previous level op, not after the late start, so the
   catalog shows boards, not win screens.
3. **Zero-move wins.** `level end won` with `moves == 0` and under 15 s is refused with "a win with no moves
   in 15 s is the previous win screen, a bonus offer or a skip: look at the frame; if it is a skip for a video,
   `--skipped`". `--skipped` records `result: won, skipped: true`; `stats` and the mechanic's counters leave
   skipped wins out of `best_s` and the typical time.
4. **Retries.** `level end lost --retry` records the loss and opens the same level again in one call (the
   name and mechanic kept, a new clock) so a stage retry is one command instead of two.
5. **Bonus boards.** `level start` takes `--bonus` for a board without a level number (a golden board, a
   challenge, a daily); the record keeps `bonus: true`, `progress` is not written on its win, and
   `level-catalog` files it under the bonus name, not a number.
6. **Benchmark.** `bench_rows` adds `solve_s`: from the first move of the level to its end, next to the level
   time, so slots that drew an ad at the level start (MeowTrail: ads ~6.3 of 13.4 min in slots 2–3,
   [s:20261001-172422-chrono-2FYKPJ#3]) and slots that started the clock late compare on the same footing.

## How to test

- A test session with a mechanic in `research.yaml`: `taps "10,10"` with no level open → the warning;
  `sw.py stats` shows `moves_outside_level: 1`.
- `taps`, then `level start "level 2" --mechanic x --plan p` → `moves_before: 1` in the reply and the step.
- `level start`, `wait 1`, `level end won` → refused; `level end won --skipped` → recorded with `skipped`.
- Replay: `sw.py level-catalog com.oakever.meowdoku` after the change shows no win screens as start frames for
  the bench sessions of 2026-10-01 (slots 180616, 181422, 182810).
