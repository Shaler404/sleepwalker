---
game: com.oakever.akari
title: "Metrics"
type: agent
verified_at: 2026-10-02
---

# Analysis speed

| Date | Machine | Sessions | Steps per closed case | Steps without a screen change | Skills ok/fail | Level time (akari) | Models |
|---|---|---|---|---|---|---|---|
| 2026-10-01 | chrono | 3 | 2.1 / 27.2 / 3.2 | 11% / 9% / 25% | 0/0 | median 0.4 min (best 0.2), 56 won, 0 lost | opus (study) 1, sonnet (play) 2 |
| 2026-10-02 | chrono | 13 (4 research, 9 bench slots of 20261001-1432 and -1531) | 27.0 / 19.0 / 10.2 / 13.7 (research sessions; bench slots close no cases) | 19% / 21% / 15% / 24% / 58% / 0% / 0% / 0% / 0% / 9% / 0% / 47% / 5% | 0/0 | about 25 s of solving per level (62–80 median 25–26 s, 83–107 29 s, 108–120 20 s; `sw.py`: typical 0.3 min, 56 won in these sessions logged); level stats unreliable, see below | sonnet 3, sonnet low 3, sonnet medium 2, haiku 3, opus low 2 |

Level statistics of 2026-10-02 are wrong in `research.yaml` and `sw.py stats`: wins were not logged in
20261001-070939 (levels 56–61, one "level 56 quit 407 s") and 20261001-143237 (81–82, logged as quits),
and early false wins were logged in 20261001-091349 (level 63 at 11/13, 18 s instead of about 75 s) and
20261001-100940 (level 77 after 5 s with 0 moves: the mechanic's best_s 5). The per-level times in
[the playbook](playbook.md#level-times) are read from the steps, not from these counters. Bench level
times include an interstitial whenever `level start` came before the ad (92–102: 100–149 s), so bench
model comparisons depend on which levels drew ads. The same-screen share was high where the agent
missed a button (171336: 58%, 175856: 47%). The akari mechanic is within the 5-minute budget on every
level; the wall time goes to ads.
