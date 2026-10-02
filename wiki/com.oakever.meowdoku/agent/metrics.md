---
game: com.oakever.meowdoku
title: "Metrics"
type: agent
verified_at: 2026-10-02
---

# Analysis speed

| Date | Machine | Sessions | Steps per closed case | Steps without a screen change | Skills ok/fail | Level time (queens) | Models |
|---|---|---|---|---|---|---|---|
| 2026-10-01 | chrono | 3 | 19.3 / 16.1 / 12.2 | 61% / 39% / 35% | 0/0 | median 0.7 min (best 0.3), 45 won, 0 lost | opus (study) 1, sonnet (play) 2 |
| 2026-10-02 | chrono | 13 (5 play + 8 bench slots of 20261001-1531-meowdoku) | 19.4 play sessions (369 steps / 19 closed); 28.4 with the bench steps (bench closes nothing) | 22% (play 21%, bench 24%) | 0/0 | queens: from transcripts about 50 s from the Level tap (43–95 s, of it 9–30 s ad); one hand batch 15–39 s; `solve --run` 43–100 s; all under the 5-min budget. Logged bench level stats are WRONG (golden boards counted as levels, 2 fake wins in 185238, level start logged after solve_check in 184651): `sw.py playbook` 128 won / typical 1.0 min overstate, real totals not recomputed | sonnet (play) 5; bench: sonnet 4 (low 2, medium 2), haiku 2, opus low 2 |
