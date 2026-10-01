# Failed commands leave no trace, and the CLI trips the player on small slips

Status: proposed by the dream (chrono, 2026-10-01). Change in `harness/sw.py` (`fail`, argument
parsing, `ask`).

## The problem

When `sw.py` refuses a command (argparse error, a timeout, a guard), nothing goes into
`steps.jsonl`: the step costs the player a tool call and ten to twenty seconds of thinking, and the
dream cannot count it. The only trace is the player's own inbox note, when it writes one:

- `launch` takes no `--why`, so `launch --why …` is an argparse error
  [s:20261001-054205-chrono-2FYKPJ#49]; `wait` and `shot` take none either, while every other phone
  action requires it;
- `tap 490,840` fails: `tap` takes `X Y`, `taps` takes `X,Y` [s:20260930-225122-chrono-2FYKPJ#7];
- `tap … --why next level` without quotes breaks the command [s:20261001-060942-chrono-2FYKPJ#28];
- `taps "X,Y X,Y" --gap 0` could not make a double tap, and the player fell back to `adb` directly,
  which the log did not record [s:20261001-003641-chrono-2FYKPJ#3] [s:20261001-003641-chrono-2FYKPJ#4]
  (fixed since by `X,Y:2`, but the failure itself was invisible);
- `ask` timed out at 180 s twice in Pull the Pin, three minutes each with nothing back and no step
  record [s:20261001-081207-chrono-2FYKPJ#18] [s:20261001-102608-chrono-2FYKPJ#1]; the successful
  consultations took 25–120 s (eight across four games), and two answers were wrong or against the rules
  (the green tiles in Vita Mahjong [s:20261001-010125-chrono-2FYKPJ#27]; "play the ad" in Cryptogram
  [s:20261001-020937-chrono-2FYKPJ#17]).

Five games, seven sessions. None of this shows in `stats`.

## The change

1. Every refused or failed invocation inside a session is logged as a step of type `error` with the
   command line (without the `--why` text), the message and, for `ask`, the seconds spent. `stats`
   counts `errors` and `error_minutes` per session; the dream reads them in the inbox-less sessions.
2. Forgiving arguments: `--why` is accepted (optional) on `launch`, `wait` and `shot`; `tap` accepts
   `X,Y` as well as `X Y`; `--why` takes several words without quotes (`nargs="+"`, joined). The help
   text stays as it is.
3. `ask`: the default `consult.timeout_s` drops to 90; on a timeout the reply says how long it waited
   and the step is logged; the consultant's prompt gets the session rules that matter for advice
   ("the agent never plays ads, never opens payment sheets") so the answer does not contradict them.

## How to test

- `sw.py -d <device> tap 10,10 --why test tap` on a test session works and logs a `tap` step.
- `sw.py -d <device> tap 10 --why x` (missing Y) logs an `error` step with the message; `sw.py stats`
  shows `errors: 1`.
- With `consult.timeout_s: 1`, `sw.py ask "x"` fails fast, logs an `error` step with `seconds`.
