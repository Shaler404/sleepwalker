# Proposal: the arrows-escape solver taps from a simulated board; make it look before each batch

Date: 2026-10-05. Machine: chrono. Status: proposal (the solver is in `state/com.oakever.arrows/solvers/`,
not published; the fix is solver code, which the process PR does not touch, and it needs the lab's recorded
frames to test).

## The problem, with sources

`arrows-escape.py` (Amaze GO!, `com.oakever.arrows`) won Hard L5 in session `20261005-010045-chrono-2FYKPJ`
(step 92, 870 s, no drop lost) and L6-L10 in `20261005-012010-chrono-2FYKPJ` (292 taps, 0 blocked, 3 stars).
The dream's critic read it in full and found three things that the section 6 rule for solvers ("stops with
`rescan` before hidden outcomes") does not allow, and that cost nothing yet only because every board read was
right:

1. **Taps chained from a simulation, one batch, no look between them.** In the solve phase the solver
   takes the arrows free on the current board, marks them gone in a copy (`sim`), takes the arrows that are
   free *after* those, and so on up to `MAX_TAPS = 14` per round (`solve()`, the `while len(moves) < MAX_TAPS`
   loop). In `20261005-012010` 20 of 23 rounds sent 14 taps at once (steps 2-3, 6-8, 11-15, 18-19, 22-26).
   A tap whose ray is blocked costs a drop; three drops are the whole level ("Out of Lives", playbook). One
   misread head direction or one missed edge in the map makes every tap chained behind it blind: a chain of
   14 can spend the three drops in a second, inside one batch, before the harness's `changed` check runs.
2. **A stuck arrow is tapped three times.** `st["tapped"]` counts taps per arrow and stops only at `n >= 3`
   ("tapped 3 times and still there"). An arrow that does not leave was not free: the first retry costs the
   second drop, the second retry the third. Three drops is the level.
3. **The docstring does not match the code.** It says "at most 45% of the viewport" per swipe and "up to 8"
   taps a round; the code has `SWIPE_MAX = 0.3` and `MAX_TAPS = 14`. A reader who tunes by the docstring tunes
   the wrong thing (the pan physics of 2026-10-05, FLING = 2.0, were learned the hard way: about 40 rounds of
   map restarts in `20261005-010045`, steps 2-50, inbox "Agent error").

Why it is not a one-night fix: the chaining is what makes Hard levels fast (L8 168 s, L10 268 s against 863 s
for L5 by the hint loop), so the change trades speed for safety and needs the level times measured again on
the recorded frames, and the solver itself lives in the knowledge zone.

## The change

- **One rank per round.** Tap only the arrows free on the board as read (`free_now(arrows, box)`), never the
  ones freed by the simulation; return `rescan: True` unless the taps empty the board. The next round reads
  the frame after the taps and sees what actually left. Keep the per-round cap, but as a constant that the
  docstring states correctly.
- **No blind retry.** An arrow tapped once and still on the board after the next read is a misread, not bad
  luck: stop with a note (`rescan: False`, no moves) after the first miss, not the third. The player then
  looks at the board and, if needed, restarts the map (a new `level plan`). A sliding animation caught
  mid-flight is the one false positive: treat an arrow whose nodes read as a mix of `A` and `D` as "in
  flight" and skip it this round instead of counting a miss.
- **Docstring = code.** State `MAX_TAPS`, `SWIPE_MAX` and `FLING` in the docstring from the constants, or
  drop the numbers from the prose.

## How to test it

- Offline, on the recorded frames of the two sessions: `sw.py solve arrows-escape --image <frame> --game
  com.oakever.arrows --state <json>` chained through the rounds of L8 and L10 (`raw/com.oakever.arrows/
  20261005-012010-chrono-2FYKPJ/shots/`). The moves per round drop (one rank each), the total taps stay 292,
  no round taps an arrow that the next frame still shows.
- The level times on the phone: L8 and L10 again with the new solver (the lab, `runbooks/lab.md`); the
  budget is 5 min (`play.level_budget_min`). If a Hard level goes over it with one rank per round, allow a
  chain of depth 2 (the free arrows and the ones they free) and no deeper, and measure again.
- A misread injected on purpose (flip one head direction in the state JSON): the old solver taps the
  dependent chain blind; the new one stops after the first arrow that did not leave.
