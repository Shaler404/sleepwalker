# The same solver plan or the same tap, again and again, on a frame that did not change

Status: proposed by the dream (chrono, 2026-10-02). Change in `harness/sw.py` (`cmd_solve`, `cmd_tap`/`cmd_taps`,
`cmd_stats`). Complements `2026-10-01-screen-change-measure.md` (what "unchanged" means); this one is about what
the harness does when the same action is repeated on an unchanged screen.

## The problem

`solve --run` stops when a round repeats the previous round's moves or the moves change nothing — but only
inside one run. Separate `solve` calls (`--rounds 1`, or a draw followed by a run) have no memory, and `tap`
has none either:

- Block Blast! 20261001-230945-chrono-2FYKPJ: 56 `solve` steps, 16 of them identical to the previous one
  (same frame hash, same moves); three loops [s:20261001-230945-chrono-2FYKPJ#14]–[s:20261001-230945-chrono-2FYKPJ#18],
  [s:20261001-230945-chrono-2FYKPJ#42]–[s:20261001-230945-chrono-2FYKPJ#52],
  [s:20261001-230945-chrono-2FYKPJ#57]–[s:20261001-230945-chrono-2FYKPJ#63], about 24 steps (38 % of the
  session) and 2.5 minutes; each loop ended only when the player dragged by hand. The root cause (the solver
  pressed the tray piece at a seam) was found by the lab afterwards; the session itself never learned that the
  plan was the same plan.
- MeowTrail bench slot 20261001-171336-chrono-2FYKPJ: every tap on "Level 83" landed about 30 px below the
  button [s:20261001-171336-chrono-2FYKPJ#1] … [s:20261001-171336-chrono-2FYKPJ#10]; the player relaunched,
  restarted, pressed Back and swiped instead of looking at the miss; 4.3 minutes, 0 levels, the slot wasted.
- MeowTrail bench slot 20261001-175856-chrono-2FYKPJ: taps at y 1210, above the win button, at
  [s:20261001-175856-chrono-2FYKPJ#4]–[s:20261001-175856-chrono-2FYKPJ#7] and [s:20261001-175856-chrono-2FYKPJ#13]
  with Back, an outside tap and a swipe in between: about 150 s, 37 % of the slot.
- Meowdoku bench slot 20261001-185238-chrono-2FYKPJ: the Home "Level N" button tapped at y 1245 (it is at
  about 1185) [s:20261001-185238-chrono-2FYKPJ#5], then Back opened the Quit dialog and a restart followed —
  about 3 minutes [s:20261001-185238-chrono-2FYKPJ#3]–[s:20261001-185238-chrono-2FYKPJ#9].

Three games, four sessions, about 10 minutes and one benchmark slot. The runbook's "three steps without a
screen change — change strategy" exists; the harness has no way to say *what* repeated.

## The change

1. `solve` (every call, not only inside `--run`) keeps the last `(frame hash, moves)` in the session. A call
   whose moves equal the previous call's on a frame within `HASH_MATCH` of the previous frame is **not sent**:
   the reply is `repeated: true` with "the solver returns the moves of step N on the same frame: they do not
   land. Place one by hand on this frame, or fix the solver" and the drawn frame; `--force` sends them anyway.
   The step is logged as `solve` with `repeated: true`.
2. `tap`/`taps`: a tap within 25 px of the previous tap's point, when both replies were `same_as_prev`, adds
   the warning "same tap twice with no change: the control is probably elsewhere — compare the point with its
   bounds on the frame before another tap". The third such tap is refused with exit 5 unless `--force`; the
   reply carries the frame so the player looks before it acts.
3. `stats`: `repeated_steps` per session (solve repeats plus refused taps), so the dream sees the loops
   without reading the transcripts.

## How to test

- `sw.py solve classic --image <frame> --game com.block.juggle` twice in a test session with the same image:
  the second reply is `repeated: true` and logs no moves; with `--force` it sends them.
- Fake device: `tap 100 100` three times → the second reply warns, the third is refused with exit 5;
  `tap 100 100 --force` goes through.
- `sw.py stats com.block.juggle` on this machine shows `repeated_steps` for 20261001-230945-chrono-2FYKPJ
  when recomputed from `steps.jsonl` (16 identical consecutive solves).
