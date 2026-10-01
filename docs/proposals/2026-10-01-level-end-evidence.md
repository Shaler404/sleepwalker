# A won level needs a frame, and a restart after a win needs a warning

Status: proposed by the dream (chrono, 2026-10-01). Change in `harness/sw.py` (`level end`, `restart`,
`solve --run`).

## The problem

**Wins without a win screen.** `level end won` records whatever the player claims; the level op carries
no frame. Levels were recorded as won before they were played:

- Meowdoku 20260930-233055-chrono-2FYKPJ: level 12 ended as won with two cats missing; the record
  labelled "level 13" is level 12 finishing [s:20260930-233055-chrono-2FYKPJ#86] [s:20260930-233055-chrono-2FYKPJ#101].
- Meowdoku 20261001-013526-chrono-2FYKPJ: four early records double-count levels; the mechanic counter
  said 47 won when 45 were [s:20261001-013526-chrono-2FYKPJ#20] [s:20261001-013526-chrono-2FYKPJ#110].
- Meowdoku 20261001-060942-chrono-2FYKPJ: level 46 recorded as won from a stale ad frame on which the
  solver said "solved" [s:20261001-060942-chrono-2FYKPJ#20] [s:20261001-060942-chrono-2FYKPJ#28].
- MeowTrail 20261001-100940-chrono-2FYKPJ: a level ended as won while the solver had reported "no
  solution" on a board with a missing box [s:20261001-100940-chrono-2FYKPJ#65] [s:20261001-100940-chrono-2FYKPJ#66].

The cost is in the numbers everything else trusts: the mechanics' win counters and level times
(`research.yaml`, `sw.py playbook`, `stats`, the lab's `level-frames`, the benchmark) and the progress
value an unlock goal compares with its target.

**Restart right after a win.** `restart` force-stops the game. When the post-win screen or its
interstitial is still up, the win is not saved: Pull the Pin went back to the previous level four times
in two sessions, about ten minutes of replaying [s:20261001-054205-chrono-2FYKPJ#11]
[s:20261001-054205-chrono-2FYKPJ#26] [s:20261001-054205-chrono-2FYKPJ#41] [s:20261001-054205-chrono-2FYKPJ#52]
[s:20261001-102608-chrono-2FYKPJ#29]; Vita Mahjong restarted a half-played level after a relaunch
[s:20261001-110957-chrono-2FYKPJ#1]. The player knew the lesson from the previous session and still
restarted: the command gives no signal at the moment it matters.

## The change

1. `level end won` requires a frame taken after the last move (`shot`, `wait` or the frame a move
   returns) and refuses with "take a frame of the win screen first" when the last action was a move
   with no later frame, or when the app on screen is not the game. The level op records `shot` (the
   frame it was called on) so the review, the lab and the critic can check a win against its frame.
2. `solve --run` reports `solved` only when the solver says `done` **and** the frame after the last
   round differs from the one before it (`changed_px > 0`); otherwise `stopped: "the solver says done
   on a frame that did not change: look at it"`.
3. `restart` warns and asks for `--after-win` when the last level op is `won` less than two minutes
   ago and no `level start` followed: "a win may not be saved yet: `launch`, `wait 30`, then restart
   with --after-win". With an open level it keeps working as now and the reply says the level will be
   recorded as `quit` unless the player ends it first.

## How to test

- A test session: `taps` then `level end won` → refused; `wait 1` then `level end won` → recorded
  with `shot`.
- `level end won` with the Play Store in the foreground → refused.
- `level end won`, then `restart --why x` within two minutes → the warning; `--after-win` → restarts.
- The queens solver on a frame of the win screen returns no moves and `done: false` (it refuses
  non-boards), so `solve --run` must not print `solved` on it.
