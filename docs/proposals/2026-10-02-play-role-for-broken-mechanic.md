# The fast model is sent to a broken mechanic when the session's tasks are follow-ups

Status: proposed by the dream (chrono, 2026-10-02). Change in `harness/sw.py` (`model_role`, `cmd_claim`,
`finish`).

## The problem

`model_role()` picks `play` whenever the ready tasks have no `analyze`, `update`, `scout`, `unlock` or
`experiment` kind ("checks and studies: no gameplay to learn in this session"), and only otherwise looks at the
mechanics' statuses. A `followup` or `ftue` task that needs winning levels of a `broken` mechanic therefore goes
to the fast model, which by the runbook must hand it back at once:

- Vita Mahjong 20261001-204654-chrono-2FYKPJ: sonnet, role `play`, tasks `auto-complete-trigger`,
  `hard-levels-streak`, `interstitials` (all `followup`, all need a level won) while `core-match` was `broken`
  (typical 14 min a level). The solver found no certain pair on L18, the player filled the tray and handed off
  after 3.7 minutes [s:20261001-204654-chrono-2FYKPJ#10].
- 20261001-205148-chrono-2FYKPJ: the owner started opus by hand under a slot reserved as sonnet
  (`start --model opus`) and won L18 in 27.6 minutes [s:20261001-205148-chrono-2FYKPJ#74].
- 20261001-211823-chrono-2FYKPJ: the next `claim` gave the same three follow-ups to sonnet again; handed off
  after 6 taps and 2.5 minutes [s:20261001-211823-chrono-2FYKPJ#6]. The reviewer's blocker note after each of
  these says "route its sessions to the strong model while the mechanic is broken".

Two wasted sessions in one evening on one game, plus the handoff penalty (the game comes back first, with the
strong model, but only for the next `claim`; after the strong model's `ok` session the rule forgets). A
handoff carries no target: `end --status handoff` says nothing about which mechanic the strong model should
take, so the next brief cannot name it either.

## The change

1. `model_role`: the "checks and studies" shortcut applies only when every known mechanic is `mastered`. If
   any mechanic is `studying` or `broken` and any ready task is of a kind that plays levels (`analyze`,
   `update`, `scout`, `unlock`, `experiment`, `ftue`, `replay`, `followup`), the role is `study` with the
   reason "gameplay to learn: <mechanic> (<status>) — the tasks need levels". Pure `study`, `survey` and
   `daily` sessions (menus, no levels) keep the fast model.
2. `end --status handoff --to <mechanic>`: the mechanic goes into `sessions.jsonl` (`handoff_to`) and the next
   assignment's brief carries it in `model_why` ("handoff from <session>: <mechanic> is <status>"). Without
   `--to`, `end` takes the open level's mechanic when there is one.
3. `claim` keeps the handoff priority (the game comes back first), and `stats` counts `handoff` sessions under
   two minutes as `wasted_handoffs` so the dream sees them.

## How to test

- A unit test of `model_role` with a view where `core-match` is `broken` and the ready tasks are three
  `followup` goals → `study`; the same view with all mechanics `mastered` → `play`; a view with a `broken`
  mechanic and only `study` and `daily` tasks → `play`.
- On this machine: `sw.py claim` for Vita Mahjong with `core-match` still `broken` returns a `study`
  assignment with the mechanic in `model_why`.
- `end --status handoff --to core-match` on a test session → `handoff_to` in `sessions.jsonl`.
