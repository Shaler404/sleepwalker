---
game: _common
title: Common agent lessons
type: agent
verified_at: 2026-10-01
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
  session with the status `blocked`; `sw.py` reports this itself.
  *Confirmed: manual check 2026-09-30, Samsung SM-A276B.*
- A playable ad with no close button ignores taps and Back. Do not play it or wait: `sw.py launch`
  returns to the game (a rewarded ad still pays). In Cryptogram the ad survived home + launch; closing
  the game from recents worked in Pull the Pin, so `sw.py restart --why ...` is the next step (not yet
  verified).
  *Confirmed: 20261001-013526-chrono-2FYKPJ, Meowdoku 1.18.0; 20261001-031723-chrono-2FYKPJ, Vita Mahjong 3.39.1.*
  [s:20261001-013526-chrono-2FYKPJ#15] [s:20261001-031723-chrono-2FYKPJ#82] [s:20260930-201034-chrono-2FYKPJ#46] [s:20261001-020937-chrono-2FYKPJ#21]
- Take tap coordinates only from the frame you are looking at: a `shot --hi` frame is larger than a
  normal one, and coordinates of one sent against the other miss. In Cryptogram that opened a real
  purchase sheet.
  *Confirmed: 20261001-020937-chrono-2FYKPJ, Cryptogram 3.6.1; 20260930-221457-chrono-2FYKPJ, Vita Mahjong 3.39.1.* [s:20261001-020937-chrono-2FYKPJ#9] [s:20260930-221457-chrono-2FYKPJ#12]
- Never tap a remove-ads or price button: in two games it went straight to a Google Play payment sheet
  with 1-tap buy. If a payment sheet opens, press Back at once.
  *Confirmed: 20260930-192115-chrono-2FYKPJ, Pull the Pin 241.3.1; 20261001-020937-chrono-2FYKPJ, Cryptogram 3.6.1.* [s:20260930-192115-chrono-2FYKPJ#22] [s:20261001-020937-chrono-2FYKPJ#9]
- Do not trust `same: true` after a tap during an animation: look at the frame.
  *Confirmed: 20260930-192115-chrono-2FYKPJ, Pull the Pin 241.3.1; 20260930-233055-chrono-2FYKPJ, Meowdoku 1.18.0.* [s:20260930-192115-chrono-2FYKPJ#11] [s:20260930-233055-chrono-2FYKPJ#59]
- After `launch` from a Helpshift help center or an ad, the game may still show the popup that was open
  before: look at the frame before the next tap.
  *Confirmed: 20261001-022624-chrono-2FYKPJ, Meowdoku 1.18.0; MeowTrail 1.0.2 (session 20261001-035425-chrono-2FYKPJ).* [s:20261001-022624-chrono-2FYKPJ#30] [s:20261001-035425-chrono-2FYKPJ#19]
