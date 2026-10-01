# The lab does not see a solver the player works around

Status: proposed by the dream (chrono, 2026-10-01). Change in `harness/sw.py` (`lab_needed`, `lab-check`).

## The problem

`lab_needed()` claims a mechanic for the lab when its status is `studying` or `broken`, or its recent
won levels have a median over the level budget. A `mastered` solver mechanic whose solver no longer
works stays invisible as long as the model does the solver's job by hand within five minutes:

- Meowdoku `queens` (status `mastered`, method `solver`, typical 0.7 min):
  - levels 44–55: the solver misreads small or similar-hued regions; cats placed by hand or the whole
    board solved by brute force on a hand-read grid, 40–75 s a level
    [s:20261001-060942-chrono-2FYKPJ#11] [s:20261001-060942-chrono-2FYKPJ#76]
    [s:20261001-060942-chrono-2FYKPJ#103] [s:20261001-060942-chrono-2FYKPJ#116];
  - level 56: "solver did nothing, brute force"; levels 59–66 all by brute force
    [s:20261001-082114-chrono-2FYKPJ#4] [s:20261001-082114-chrono-2FYKPJ#52];
  - level 67: "solver placed 1 cat; brute force the rest", and so on
    [s:20261001-093348-chrono-2FYKPJ#13] [s:20261001-093348-chrono-2FYKPJ#31];
  - levels 84–96: five solver rounds changed nothing (a stale local copy, see
    `2026-10-01-stale-local-solver.md`), all cats placed with `taps`, 10x10 boards 60–100 s
    [s:20261001-115413-chrono-2FYKPJ#14] [s:20261001-115413-chrono-2FYKPJ#78].

  Four sessions, about 60 levels played by hand under a `mastered, solver` label; the lab never ran.
- MeowTrail `akari` (`mastered`, `solver`, 0.3 min): the solver takes a board the model types as JSON
  every level. Misreads cost a heart [s:20261001-091349-chrono-2FYKPJ#26], gave "no solution" twice and a
  false win [s:20261001-035425-chrono-2FYKPJ#74] [s:20261001-035425-chrono-2FYKPJ#75]
  [s:20261001-100940-chrono-2FYKPJ#65] [s:20261001-100940-chrono-2FYKPJ#66], and the benchmark slot
  spent two consultations of 41 s and 24 s on reading a board [s:20261001-143237-chrono-2FYKPJ#6]
  [s:20261001-143237-chrono-2FYKPJ#13]. Reading the board from the screenshot is lab work that no
  trigger asks for.

## The change

`lab_needed()` also returns a mechanic with `method: solver` when, over its last five recorded levels,
any of these holds (all of it is in `raw/<game>/<session>/steps.jsonl` between `level_start` and the
level op):

- **moves by hand**: in two or more levels the moves came from `taps`/`tap` steps and not from `solve`
  steps (count moves per source; a level is "by hand" when more than half of its moves are hand moves);
- **board by hand**: every `solve` step of those levels used `--board` (the solver does not read the
  screenshot);
- **solver gave up**: two or more levels had a `solve --run` that stopped with "no moves", "repeats the
  moves" or "changed nothing".

The `why` names the sign (`solver bypassed: 4 of 5 levels placed by hand`). The mechanic's status is
unchanged (levels on the phone decide it); `sw.py playbook` shows the sign next to the mechanic so the
player and the dream see it too.

## How to test

- On this machine, `sw.py lab-check com.oakever.meowdoku` returns `queens` with "placed by hand" and
  `sw.py lab-check com.oakever.akari` returns `akari` with "board by hand"; Vita Mahjong `core-match`
  is still returned for its status.
- A synthetic journal where the last five levels were played by `solve --run` without `--board` and
  within the budget: not returned.
