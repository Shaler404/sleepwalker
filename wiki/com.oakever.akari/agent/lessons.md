---
game: com.oakever.akari
title: "Lessons"
type: agent
version_seen: 1.0.2
verified_at: 2026-10-07
---

# Lessons for the agent: MeowTrail

- The solver gives up on the dimmed tutorial boards: place the cats where the tutorial hand points.
  *Confirmed: 20261003-200925-chrono-2FYKPJ, 1.0.2.* [s:20261003-200925-chrono-2FYKPJ#6] [s:20261003-200925-chrono-2FYKPJ#8]
- A rewarded booster video (about 64-77 s) can end on the Play Store: `launch` returns with the booster refilled.
  *Confirmed: 20261003-232850-chrono-2FYKPJ, 1.0.2.* [s:20261003-232850-chrono-2FYKPJ#7] [s:20261003-232850-chrono-2FYKPJ#8]
- An interstitial comes on every second level start, whatever the route (win button, Home, Restart), and not on a time cooldown: L31 had none 145 s after an ad and L33 none 90 s after one. The 'even level number' rule is refuted (ads at L27 and L29).
  *Confirmed: 20261006-023308-chrono-2FYKPJ, 1.0.2; 20261006-002027-chrono-2FYKPJ, 1.0.2.* [s:20261006-023308-chrono-2FYKPJ#20] [s:20261006-002027-chrono-2FYKPJ#13] [s:20261006-002027-chrono-2FYKPJ#18]
- A bulb hint closes only with Apply (Back and the veil do nothing) and charges a unit when it opens; alternate bulb (482,1305) and Apply (364,1348) about 0.5 s apart to spend units fast.
  *Confirmed: 20261005-221436-chrono-2FYKPJ, 1.0.2.* [s:20261005-221436-chrono-2FYKPJ#4-8] [s:20261005-221436-chrono-2FYKPJ#10-15]
- Run `level start` before `level end`; a level solved with no `level start` has no record, and a tip popup mistaken for a win logs a false L6 win.
  *Confirmed: 20261005-080420-chrono-2FYKPJ, 1.0.2; 20261006-002027-chrono-2FYKPJ, 1.0.2.* [s:20261005-080420-chrono-2FYKPJ#15] [s:20261005-080420-chrono-2FYKPJ#50] [s:20261006-002027-chrono-2FYKPJ#21]
- The system Back key does not close the Home Settings sheet: use its X button.
  *Confirmed: 20261006-002027-chrono-2FYKPJ, 1.0.2.* [s:20261006-002027-chrono-2FYKPJ#43]
- The every-second-start interstitial count survives a force-stop, a 3.5-minute pause on Home and a rewarded video: none of them shifts the alternation.
  *Confirmed: 20261006-080945-chrono-2FYKPJ, 20261006-102842-chrono-2FYKPJ, 20261006-124837-chrono-2FYKPJ, 1.0.2.* [s:20261006-080945-chrono-2FYKPJ#3] [s:20261006-080945-chrono-2FYKPJ#7] [s:20261006-080945-chrono-2FYKPJ#9] [s:20261006-102842-chrono-2FYKPJ#12] [s:20261006-102842-chrono-2FYKPJ#14] [s:20261006-124837-chrono-2FYKPJ#5] [s:20261006-124837-chrono-2FYKPJ#8]
- Do not wait on the win screen: it has no harmless control and the phone blocked touches there after about 3 minutes. Wait on Home with the gear and its close button (665,127 then 648,830) about every 50 s.
  *Confirmed: 20261006-080945-chrono-2FYKPJ, 20261006-102842-chrono-2FYKPJ, 1.0.2.* [s:20261006-080945-chrono-2FYKPJ#11] [s:20261006-102842-chrono-2FYKPJ#6] [s:20261006-102842-chrono-2FYKPJ#11]
- A board dimmed after a rewarded video is the phone (touch protection), not the game: wait 10 s after `launch` and take a frame; both later videos left the board bright and playable.
  *Confirmed: 20261006-102842-chrono-2FYKPJ, 20261006-124837-chrono-2FYKPJ, 1.0.2.* [s:20261006-102842-chrono-2FYKPJ#18] [s:20261006-124837-chrono-2FYKPJ#3] [s:20261006-124837-chrono-2FYKPJ#12]
