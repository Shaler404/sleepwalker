# `skill new` gives every step a 1.5 s wait; the transcript knows the real one

Status: proposed by the dream (chrono, 2026-10-02). Change in `harness/sw.py` (`skill_new`, `skill_run`).

## The problem

`skill_new` sets each step's `wait` to the action's `settle` plus 0.5 s — 1.5 s for every tap, however long
the transcript waited after it. A skill that crosses an ad, a level load or a scene change therefore runs its
next tap into the previous screen, and the editors fix the waits by hand after the fact:

- Pull the Pin `skills/com.maroieqrwlk.unpin/jump-to-level.yaml` and `defeat-skip-video.yaml` (from
  20261001-054205-chrono-2FYKPJ [s:20261001-054205-chrono-2FYKPJ#53]–[s:20261001-054205-chrono-2FYKPJ#56] and
  20261001-220948-chrono-2FYKPJ [s:20261001-220948-chrono-2FYKPJ#3]–[s:20261001-220948-chrono-2FYKPJ#8]): the
  rewarded video steps need 33 s and 40 s; `skill new` recorded 1.5 s, the dream's editors wrote 33 and 40.
- Candy Crush Saga `title-to-level-board.yaml` and `story-path-to-next-board.yaml` (20261001-232021-chrono-2FYKPJ
  [s:20261001-232021-chrono-2FYKPJ#14] [s:20261001-232021-chrono-2FYKPJ#15]): level loads need about 3 s;
  set by hand to 3.0.
- Amaze GO! `next-level.yaml` (20261001-204000-chrono-2FYKPJ [s:20261001-204000-chrono-2FYKPJ#4]–
  [s:20261001-204000-chrono-2FYKPJ#6]): the Next Level button appears after a delay the transcript shows as a
  `wait` step.

Three games, eleven skills written this dream, every wait edited by hand or left wrong. The transcript has the
numbers: the `t` of the next action, and the `wait` steps between actions.

A second, smaller fault from the same command: the precondition is the hash of the whole frame before the
first step. For a skill that starts on a board (Block Blast!: the gear on a board full of pieces), the hash
never matches a later board, and `skill run` refuses with "not the screen the skill starts from" every time
(the Block Blast! editor's note, `skills/com.block.juggle/open-settings.yaml`).

## The change

1. `skill_new`: the wait of step *i* is the time from its action to the next action in the range (the next
   action's `t` minus this one's `t` minus its `settle`), rounded up to 0.5 s, capped at 60 s; the last step
   keeps `settle + 0.5`. `wait` steps inside the range are not steps of the skill: their seconds are already in
   that gap. `--wait "3:33,5:10"` overrides single steps.
2. `skill_run` compares the actual post-frame against `post_hash` as today, but reports `waited_s` so the
   dream can tighten slow skills.
3. Preconditions on a changing screen: `skill new --pre-region X1,Y1,X2,Y2` (fractions of the frame) hashes
   only that region (the control the first step taps and its surroundings) for `pre_hash`; `skill run` hashes
   the same region. Without the option, the whole frame as now.

## How to test

- `sw.py skill new com.maroieqrwlk.unpin jump-to-level-test --session 20261001-054205-chrono-2FYKPJ --steps 53-56
  --desc t --out <tmp>`: the step after the video button has `wait` ≥ 30, the others 2–5 s.
- The same for Candy Crush 20261001-232021-chrono-2FYKPJ steps 14–15: the Play step gets about 3 s.
- `skill new … --pre-region 0.85,0.05,1,0.12` on the Block Blast! gear: `skill run open-settings` on a
  different board passes the precondition and opens Settings.
