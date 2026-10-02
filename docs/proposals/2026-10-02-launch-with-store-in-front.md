# `launch` and `restart` leave the Play Store in front, and the store never triggers the "not the game" warning

Status: proposed by the dream (chrono, 2026-10-02). Change in `harness/sw.py` (`cmd_launch`, `cmd_restart`,
`take_shot`, `SYSTEM_OVERLAYS`).

## The problem

An interstitial that opens the advertised app's Play Store listing opens it as its own screen, not as a sheet
over the game. `launch` (`adb app_start`) and `restart` (force-stop, then start) bring the game up behind it,
and the store stays in front. `key back` removes it; the players did not know that, because the session
runbook told them "`launch`, not `key back`" (right for a sheet, wrong for a listing):

- Cryptogram 20261001-190315-chrono-2FYKPJ: `launch` at [s:20261001-190315-chrono-2FYKPJ#6],
  [s:20261001-190315-chrono-2FYKPJ#9], [s:20261001-190315-chrono-2FYKPJ#10] and `restart` at
  [s:20261001-190315-chrono-2FYKPJ#7], [s:20261001-190315-chrono-2FYKPJ#11] all came back with
  `app: com.android.vending`; `key back` at [s:20261001-190315-chrono-2FYKPJ#12] left the store and the
  next `launch` worked [s:20261001-190315-chrono-2FYKPJ#13]. About 3.2 minutes.
- Cryptogram 20261001-192245-chrono-2FYKPJ: two launches and two restarts with the store in front
  [s:20261001-192245-chrono-2FYKPJ#2] [s:20261001-192245-chrono-2FYKPJ#3] [s:20261001-192245-chrono-2FYKPJ#4]
  [s:20261001-192245-chrono-2FYKPJ#6] [s:20261001-192245-chrono-2FYKPJ#7]; `key back` went to the launcher
  [s:20261001-192245-chrono-2FYKPJ#8], then `launch` worked [s:20261001-192245-chrono-2FYKPJ#9]. About 100 s.
- Cryptogram 20261001-224924-chrono-2FYKPJ: two launches [s:20261001-224924-chrono-2FYKPJ#5]
  [s:20261001-224924-chrono-2FYKPJ#6], then `key back` returned to the game [s:20261001-224924-chrono-2FYKPJ#7].
- Pull the Pin 20261001-075644-chrono-2FYKPJ: four launches, one back, one X [s:20261001-075644-chrono-2FYKPJ#7]
  … [s:20261001-075644-chrono-2FYKPJ#12] before a `restart` finally worked [s:20261001-075644-chrono-2FYKPJ#13];
  about 90 s and a multi-stage level reset to stage 1.

Two games, four sessions, 6–7 minutes of phone time, and in three of them the whole session was lost to the
loop around one button. A second part of the problem: `com.android.vending` is in `SYSTEM_OVERLAYS` (so a
permission or billing sheet does not count as "another app"), which means a full Play Store listing in front
produces **no** "not the game on screen" warning. The `app` field says `com.android.vending`, the warning the
runbook promises never comes, and the player reads the frame as an ad that will not close.

The same sessions show the loop the runbook already forbids (the same button, the same ad, a restart, again):
Cryptogram ran it 5 times in 190315 and 4 times in 224924 after the rule was merged (15:20 on 2026-10-01).

## The change

1. `launch` and `restart`: after starting the game, wait for the frame and read the focused package. If it is
   the Play Store (any window that is not a billing sheet) or a browser, send `KEYCODE_BACK`, wait 1.5 s and
   start the game again, up to two times. The reply gets `back_pressed: N` and the step record keeps it. If
   the store is still in front after that, the reply says so with the hint "key back by hand, then launch".
2. `take_shot`: the store counts as an overlay only when `focus_window()` matches `PAYMENT_WINDOW`
   (the sheet `sw.py` already closes). A Play Store listing in front gets the "not the game on screen"
   warning with the hint "`launch` (it presses back for you)".
3. An ad-loop counter: the third `restart` in a session within 10 minutes with no `level_start` or
   `level` op in between adds the warning "ad loop: the same button gives the same ad after a restart; do
   the goals that do not need it, set a task for the rest". `stats` counts `restarts` per session.

## How to test

- A test session on the phone; open a listing from the shell (`am start -a android.intent.action.VIEW -d
  market://details?id=com.king.candycrushsaga`), then `sw.py launch`: the reply shows the game in front
  and `back_pressed: 1`; the step record has it.
- With the listing open, `sw.py shot` warns "not the game on screen"; with a billing sheet it still reports
  `payment_sheet_closed` and no "not the game" warning.
- Three `restart` calls in a row on a test session: the third reply carries the ad-loop warning;
  `sw.py stats` shows `restarts: 3`.
