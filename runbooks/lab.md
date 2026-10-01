# The lab: make gameplay fast without the phone

Instructions for the lab (`sleepwalker-lab`). The orchestrator starts you after a session when
`sw.py lab-check <game> --claim` says a mechanic needs work: it is still being learned, it is broken, or
its levels take longer than the level budget (5 minutes, the time a human needs). You work on recorded
frames, in parallel with the next session on the phone, so speed improves between sessions and fastest
in a game's first sessions.

Run every command from the root: `cd <root> && python harness/sw.py …`.

## Read

- `state/<game>/playbook.md` — the mechanic's rules, risks, method and pitfalls;
- `python harness/sw.py playbook --game <game>` — level times per mechanic;
- `python harness/sw.py level-frames <game> <mechanic>` — past levels with their frames; `start_frames`
  are the boards at the start of each level (look at `…_m.jpg` next to each, 730 px wide);
- the level notes (`level end --note`) in `raw/<game>/<session>/steps.jsonl`. A note that says the
  board was read by hand, the moves were placed by hand or the solver returned no moves means the
  solver is bypassed: the level is fast only because the model did the solver's work. That is lab
  work even when the level times are within the budget (Meowdoku: four sessions of hand-placed cats
  on a `mastered` solver mechanic; MeowTrail: a board typed by hand every level, three misreads).

## Decide the method

- **Solver** — every piece is visible and the rules are exact (a logic puzzle, a tile matcher):
  `state/<game>/solvers/<mechanic>.py` with `solve(image, board=None, frame_scale=1.0)`. It reads the
  board from the image (numpy/OpenCV), models the rules including how a level is lost, searches ahead,
  returns only moves whose outcome it knows (`rescan` before hidden outcomes), double taps as
  `[x, y, 2]`, and refuses implausible boards (schema, section 10).
- **Heuristic** — randomness (refills, cascades): a short ordered list of rules in the playbook.
- **Manual** — physics or reaction: what to look at first and in which order, in the playbook.

## Check, without the phone

For a solver: `python harness/sw.py solve <mechanic> --image <frame> --game <game>` on every start frame
from `level-frames`, and on a few frames that are not boards (menus, popups, the win screen). Open the
drawn frames: the moves must be right on the boards and absent on the rest. Keep a table of frames
tried and results in your log. A heuristic or a manual method: replay three recorded levels in your head
against the frames and write what the method would have done differently.

## Hand over

- The solver file and the playbook's `Method` and `Pitfalls` for the mechanic;
- `python harness/sw.py mechanic <id> --game <game> --method solver|heuristic|manual --note "…"` (a
  solver must exist for `--method solver`); the status stays as it is: levels on the phone decide it;
- `python harness/sw.py lab-done <game> --note "what changed, frames tried, what the next session should check"`.

The next session of the game (the study model) plays the mechanic with the new method; if it is not
faster, the lab runs again with that session's frames.

The last reply is one line: the game, the mechanic, the method, the frames it was checked on.
