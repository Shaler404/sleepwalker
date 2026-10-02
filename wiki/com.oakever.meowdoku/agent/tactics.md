---
game: com.oakever.meowdoku
title: "Tactics"
type: agent
version_seen: 1.18.0
verified_at: 2026-10-02
sources: [20260930-233055-chrono-2FYKPJ, 20261001-022624-chrono-2FYKPJ, 20261001-060942-chrono-2FYKPJ, 20261001-082114-chrono-2FYKPJ, 20261001-115413-chrono-2FYKPJ, 20261001-182810-chrono-2FYKPJ, 20261001-223249-chrono-2FYKPJ]
---

# Tactics

- Start manual boards from single-cell regions (forced), then eliminate by row, column and
  adjacency [s:20260930-233055-chrono-2FYKPJ#10] [s:20260930-233055-chrono-2FYKPJ#17].
- Fastest way through a level: one `solve queens` read (no `--run`), check the drawn solution, then all
  cats in one `taps` batch of double taps from the grid formula (see the playbook). It won L91–96 in
  23–39 s and every bench and late board after that [s:20261001-115413-chrono-2FYKPJ#62]
  [s:20261001-182810-chrono-2FYKPJ#2] [s:20261001-223249-chrono-2FYKPJ#6].

  > ⚠️ Previously (v1.18.0, 2026-10-01): "The solver with 3 cats per round and a rescan wins levels in
  > about 30 s." `solve --run` still works but took 43–100 s on later boards
  > [s:20261001-115413-chrono-2FYKPJ#14] [s:20261001-182015-chrono-2FYKPJ#11].
- When the solver's read is wrong or empty: read the grid into one letter per region (rows as
  strings) and run a row-by-row search with one cat per row, column and region and no touching
  columns between neighbouring rows. It solved L49–66 and the golden boards in 15–75 s
  [s:20261001-060942-chrono-2FYKPJ#60] [s:20261001-060942-chrono-2FYKPJ#108] [s:20261001-082114-chrono-2FYKPJ#4].
- To lose fish on purpose: double tap cells in the row of a given cat [s:20261001-022624-chrono-2FYKPJ#38]
  [s:20261001-115413-chrono-2FYKPJ#42].
- To get a different board for the same level: lose all fish and tap Restart on Out of Fishes — free,
  a new board [s:20261001-115413-chrono-2FYKPJ#43].
