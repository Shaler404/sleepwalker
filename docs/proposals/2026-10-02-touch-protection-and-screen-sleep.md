# Touch protection and screen sleep end sessions with no record of the failed tap

Status: proposed by the dream (chrono, 2026-10-02). Change in `harness/sw.py` (`cmd_start`, `guard`, `cmd_wait`,
`finish`) and `local.yaml` (`android.stay_awake`). The missing step record is done: every refused command,
exit 3 included, is an `error` step now (`log_refusal` in `sw.py`); this proposal adds what the harness should
do about the phone, and the touch-protection details of point 2 on top of that step.

## The problem

Samsung's accidental touch protection swallows every tap while the proximity sensor is covered or the screen
has dimmed. `guard()` detects it and refuses with exit 3, which is right — but the refusal leaves no step in
`steps.jsonl`, the session has nothing to say about *why* it ended `blocked`, and nothing keeps the screen
awake in the first place:

- Pull the Pin 20261001-081207-chrono-2FYKPJ: L11 opened, the first pull was refused with exit 3; the level
  was recorded `quit` after 6 s with 0 moves [s:20261001-081207-chrono-2FYKPJ#18]; the cause is only in the end
  summary. 8.4 minutes, three goals untouched.
- MeowTrail bench slot 20261001-175320-chrono-2FYKPJ: L104 opened, every touch ignored, `blocked`
  [s:20261001-175320-chrono-2FYKPJ#4]; the slot lost to the benchmark.
- Meowdoku 20261001-223249-chrono-2FYKPJ: 13 `wait` calls on Home over 12 minutes
  [s:20261001-223249-chrono-2FYKPJ#8]; the frame dimmed about 6 minutes in (shot 20 against shot 15), every
  wait came back `same: true`, and the next tap failed with exit 3. 78 % of the session; the Hard-level catalog
  goal never started.

Three games, three sessions, about 25 minutes and a bench slot. `phone_status()` checks the protection at
`claim`, so a phone that is covered at the start is refused; the phone that dims mid-session is not caught,
and the owner cannot see from the records how often it happens.

## The change

1. `start` reads `settings get system screen_off_timeout` and `settings get global stay_on_while_plugged_in`
   and reports both in its reply (`screen: {timeout_s: 30, stay_awake: false}`). With `android.stay_awake:
   true` in `local.yaml` (default true), `start` sets `stay_on_while_plugged_in` to 3 (AC and USB) for the
   session and `end` restores the previous value, the way Do Not Disturb is handled today.
2. The exit-3 refusal is logged as an `error` step with `touch_blocked: true`, the current brightness
   (`settings get system screen_brightness`) and `mWakefulness`, so the dream can tell a covered sensor from
   a dimmed screen. `finish` writes `blocked_reason` into `session.json` for `blocked` sessions.
3. `wait` adds `screen: dimmed` to its reply when the brightness dropped since the previous frame, with the
   hint "the next tap will fail: tap something harmless now, or end and set a task with --after-hours".
4. The `start` reply, when the device is a Samsung and the protection setting is on
   (`settings get system accidental_touch_protection`, to be verified on the device), warns the orchestrator:
   "Settings > Display > Accidental touch protection is on: the owner should turn it off on this phone".

## How to test

- Set the phone's screen timeout to 30 s, run a test session with three `wait 60` calls: the screen stays on,
  `start` shows `stay_awake: true`, `end` restores the previous value.
- Cover the proximity sensor and `tap 10 10`: exit 3, and `steps.jsonl` has an `error` step with
  `touch_blocked: true`; `end --status blocked` writes `blocked_reason`.
- With `android.stay_awake: false`, let the screen dim during a `wait`: the reply says `screen: dimmed`.
