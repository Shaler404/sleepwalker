---
game: _common
title: Common agent lessons
type: agent
verified_at: 2026-10-02
---

# Common agent lessons

Rules confirmed in two or more games or checked manually. The player reads this file before every
session; the "dream" adds to it. Each lesson says where and on what it was confirmed. A lesson not
confirmed on two versions in a row is deleted.

- On the first launch of a game, Android shows a system permission request (notifications, etc.) —
  a `com.google.android.permissioncontroller` window on top of the game. Tap "Don't allow" (or the same button
  in the phone's language); it is not part of the game. It can come back on a later launch: answer it
  the same way.
  *Confirmed: manual check 2026-09-30, Pull the Pin 241.3.1, Samsung SM-A276B; 20261001-003641-chrono-2FYKPJ, MeowTrail 1.0.2;
  20260930-233055-chrono-2FYKPJ, Meowdoku 1.18.0; 20260930-203959-chrono-2FYKPJ, Vita Mahjong 3.39.1; came back on relaunch: 20261001-024647-chrono-2FYKPJ, MeowTrail 1.0.2,
  20260930-211039-chrono-2FYKPJ, Vita Mahjong 3.39.1.* [s:20261001-003641-chrono-2FYKPJ#2] [s:20260930-233055-chrono-2FYKPJ#1] [s:20260930-203959-chrono-2FYKPJ#1] [s:20261001-024647-chrono-2FYKPJ#1] [s:20260930-211039-chrono-2FYKPJ#1]
- If the whole screen in the screenshot is dimmed and taps change nothing, this is Samsung's
  accidental touch protection (the proximity sensor is covered). Do not repeat the taps: end the
  session with the status `blocked`; `sw.py` reports this itself. Long idle waits let the screen dim and
  sleep, after which taps fail the same way: wait for timers with a follow-up task, not inside a session.
  *Confirmed: manual check 2026-09-30, Samsung SM-A276B; 20261001-081207-chrono-2FYKPJ, Pull the Pin 241.5.1;
  20261001-175320-chrono-2FYKPJ, MeowTrail 1.0.2; idle wait: 20261001-223249-chrono-2FYKPJ, Meowdoku 1.18.0.*
  [s:20261001-081207-chrono-2FYKPJ#18] [s:20261001-175320-chrono-2FYKPJ#4] [s:20261001-223249-chrono-2FYKPJ#8]
- A playable ad with no close button ignores taps and Back. Do not play it or wait: `sw.py launch`
  returns to the game (a rewarded ad still pays). If `launch` does not, `sw.py restart --why ...` gets out
  (verified in Cryptogram and Pull the Pin). A restart can cost progress: in Pull the Pin it reverts the
  level just won, so there try `launch` (or Jump to Level) first; in Cryptogram a level already won was
  kept. Waiting 60–90 s on such an ad never helped.
  *Confirmed: 20261001-013526-chrono-2FYKPJ, Meowdoku 1.18.0; 20261001-031723-chrono-2FYKPJ, Vita Mahjong 3.39.1;
  restart: 20261001-071926-chrono-2FYKPJ, Cryptogram 3.6.1; 20261001-075644-chrono-2FYKPJ, Pull the Pin 241.5.1;
  revert after a win: 20261001-054205-chrono-2FYKPJ, 20261001-153137-chrono-2FYKPJ, Pull the Pin 241.5.1.*
  [s:20261001-013526-chrono-2FYKPJ#15] [s:20261001-031723-chrono-2FYKPJ#82] [s:20260930-201034-chrono-2FYKPJ#46] [s:20261001-020937-chrono-2FYKPJ#21]
  [s:20261001-071926-chrono-2FYKPJ#41] [s:20261001-075644-chrono-2FYKPJ#13] [s:20261001-054205-chrono-2FYKPJ#11] [s:20261001-153137-chrono-2FYKPJ#15]
- When an ad has opened the Google Play listing and the store is in front, `launch` (and in Cryptogram
  also `restart`) leaves the store on top. Press Back first, then `launch`.
  *Confirmed: 20261001-190315-chrono-2FYKPJ, 20261001-224924-chrono-2FYKPJ, Cryptogram 3.6.1; 20261001-075644-chrono-2FYKPJ, Pull the Pin 241.5.1.*
  [s:20261001-190315-chrono-2FYKPJ#7] [s:20261001-190315-chrono-2FYKPJ#12] [s:20261001-224924-chrono-2FYKPJ#5] [s:20261001-224924-chrono-2FYKPJ#6] [s:20261001-075644-chrono-2FYKPJ#10]
- If the same ad loop comes back twice (enter a level → ad with no close → restart → ad again), change
  the approach — another way into a level, a longer wait on the end card, or the ad's skip icon early —
  instead of repeating it.
  *Confirmed: 20261001-190315-chrono-2FYKPJ, 20261001-224924-chrono-2FYKPJ, Cryptogram 3.6.1 (5 and 4 identical loops); 20261001-054205-chrono-2FYKPJ, Pull the Pin 241.5.1 (4 restarts, ~15 min).*
  [s:20261001-190315-chrono-2FYKPJ#25] [s:20261001-224924-chrono-2FYKPJ#16] [s:20261001-054205-chrono-2FYKPJ#52]
- Take tap coordinates only from the frame you are looking at: a `shot --hi` frame is larger than a
  normal one, and coordinates of one sent against the other miss. In Cryptogram that opened a real
  purchase sheet.
  *Confirmed: 20261001-020937-chrono-2FYKPJ, Cryptogram 3.6.1; 20260930-221457-chrono-2FYKPJ, Vita Mahjong 3.39.1.* [s:20261001-020937-chrono-2FYKPJ#9] [s:20260930-221457-chrono-2FYKPJ#12]
- Never tap a remove-ads or price button: in two games it went straight to a Google Play payment sheet
  with 1-tap buy. If a payment sheet opens, press Back at once.
  *Confirmed: 20260930-192115-chrono-2FYKPJ, Pull the Pin 241.3.1; 20261001-020937-chrono-2FYKPJ, Cryptogram 3.6.1.* [s:20260930-192115-chrono-2FYKPJ#22] [s:20261001-020937-chrono-2FYKPJ#9]
- Do not trust `same: true` after a tap during an animation: look at the frame. It also misses small
  real changes (a piece placed, a tile flipped) and frames taken while a cascade is still running.
  *Confirmed: 20260930-192115-chrono-2FYKPJ, Pull the Pin 241.3.1; 20260930-233055-chrono-2FYKPJ, Meowdoku 1.18.0;
  20261001-200952-chrono-2FYKPJ, Block Blast! 10.6.5; 20261001-232021-chrono-2FYKPJ, Candy Crush Saga 1.335.1.2;
  20261001-205148-chrono-2FYKPJ, Vita Mahjong.* [s:20260930-192115-chrono-2FYKPJ#11] [s:20260930-233055-chrono-2FYKPJ#59]
  [s:20261001-200952-chrono-2FYKPJ#16] [s:20261001-232021-chrono-2FYKPJ#16] [s:20261001-205148-chrono-2FYKPJ#17]
- If a tap on a button leaves the frame unchanged, do not send the same coordinates again: find the
  button's edges in the current frame and tap its centre. Buttons with the same label sit at different
  heights on different screens (home vs win screen).
  *Confirmed: 20261001-171336-chrono-2FYKPJ, 20261001-175856-chrono-2FYKPJ, MeowTrail 1.0.2; 20261001-183504-chrono-2FYKPJ, 20261001-185238-chrono-2FYKPJ, Meowdoku 1.18.0.*
  [s:20261001-171336-chrono-2FYKPJ#1] [s:20261001-171336-chrono-2FYKPJ#10] [s:20261001-175856-chrono-2FYKPJ#4] [s:20261001-183504-chrono-2FYKPJ#1] [s:20261001-185238-chrono-2FYKPJ#5]
- Record `level end won` only when the win screen is in the frame, and take the level number from the
  board's header. Early or blind records made the level statistics wrong.
  *Confirmed: 20261001-091349-chrono-2FYKPJ, 20261001-100940-chrono-2FYKPJ, MeowTrail 1.0.2; 20261001-060942-chrono-2FYKPJ, 20261001-185238-chrono-2FYKPJ, Meowdoku 1.18.0.*
  [s:20261001-091349-chrono-2FYKPJ#13] [s:20261001-100940-chrono-2FYKPJ#28] [s:20261001-060942-chrono-2FYKPJ#20] [s:20261001-060942-chrono-2FYKPJ#55] [s:20261001-185238-chrono-2FYKPJ#19]
- After `launch` from a Helpshift help center or an ad, the game may still show the popup that was open
  before: look at the frame before the next tap.
  *Confirmed: 20261001-022624-chrono-2FYKPJ, Meowdoku 1.18.0; MeowTrail 1.0.2 (session 20261001-035425-chrono-2FYKPJ).* [s:20261001-022624-chrono-2FYKPJ#30] [s:20261001-035425-chrono-2FYKPJ#19]
