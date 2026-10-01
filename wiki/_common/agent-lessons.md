---
game: _common
title: Common agent lessons
type: agent
verified_at: 2026-09-30
---

# Common agent lessons

Rules confirmed in two or more games or checked manually. The player reads this file before every
session; the "dream" adds to it. Each lesson says where and on what it was confirmed. A lesson not
confirmed on two versions in a row is deleted.

- On the first launch of a game, Android shows a system permission request (notifications, etc.) —
  a `com.google.android.permissioncontroller` window on top of the game. Tap "Don't allow" (or the same button
  in the phone's language); it is not part of the game.
  *Confirmed: manual check 2026-09-30, Pull the Pin 241.3.1, Samsung SM-A276B.*
- If the whole screen in the screenshot is dimmed and taps change nothing, this is Samsung's
  accidental touch protection (the proximity sensor is covered). Do not repeat the taps: end the
  session with the status `blocked`; `sw.py` reports this itself.
  *Confirmed: manual check 2026-09-30, Samsung SM-A276B.*
