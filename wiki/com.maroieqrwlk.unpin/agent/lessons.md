---
game: com.maroieqrwlk.unpin
title: "Lessons"
type: agent
version_seen: 241.3.1
verified_at: 2026-09-30
sources: [20260930-192115-chrono-2FYKPJ, 20260930-201034-chrono-2FYKPJ]
---

# Lessons for the agent: Pull the Pin

- Never tap No ADS: it opens a real Google Play sheet with 1-tap buy. If a payment sheet opens,
  press Back at once.
  *Confirmed: 20260930-192115-chrono-2FYKPJ, 241.3.1 (frame of the sheet, not published).* [s:20260930-192115-chrono-2FYKPJ#22]
- An interstitial with no close button for more than 40 s, or a blank beige screen after Play:
  taps and Back do nothing — closing the game and starting it again worked (then from recents; now
  `sw.py restart --why ...`, not yet tried in this game). Whether level progress survives is not
  verified.
  *Confirmed: 20260930-201034-chrono-2FYKPJ, 241.3.1 (twice); 20260930-192115-chrono-2FYKPJ, 241.3.1.* [s:20260930-201034-chrono-2FYKPJ#34] [s:20260930-201034-chrono-2FYKPJ#46] [s:20260930-192115-chrono-2FYKPJ#97]
- When an ad opens Google Play, press Back once or twice to return to the game.
  *Confirmed: 20260930-201034-chrono-2FYKPJ, 241.3.1 (twice).* [s:20260930-201034-chrono-2FYKPJ#52] [s:20260930-201034-chrono-2FYKPJ#61]
- Rewarded video: wait about 25 s for Skip, then close with the X at the top left (45,110).
  *Confirmed: 20260930-192115-chrono-2FYKPJ, 241.3.1; 20260930-201034-chrono-2FYKPJ, 241.3.1.* [s:20260930-192115-chrono-2FYKPJ#34] [s:20260930-201034-chrono-2FYKPJ#3]
- After a pin that drops colour onto grey balls, wait until the painting ends before opening the
  way to the cup: opening it early loses the level.
  *Confirmed: 20260930-201034-chrono-2FYKPJ, 241.3.1 (defeat and the win after it).* [s:20260930-201034-chrono-2FYKPJ#50] [s:20260930-201034-chrono-2FYKPJ#57]
