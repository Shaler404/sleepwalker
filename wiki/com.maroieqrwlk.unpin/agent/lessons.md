---
game: com.maroieqrwlk.unpin
title: "Lessons"
type: agent
version_seen: 241.5.1
verified_at: 2026-10-02
sources: [20260930-192115-chrono-2FYKPJ, 20260930-201034-chrono-2FYKPJ, 20261001-054205-chrono-2FYKPJ, 20261001-075644-chrono-2FYKPJ, 20261001-102608-chrono-2FYKPJ, 20261001-153137-chrono-2FYKPJ, 20261001-154701-chrono-2FYKPJ, 20261001-160324-chrono-2FYKPJ, 20261001-162240-chrono-2FYKPJ, 20261001-164104-chrono-2FYKPJ, 20261001-165538-chrono-2FYKPJ, 20261001-220948-chrono-2FYKPJ]
---

# Lessons for the agent: Pull the Pin

- Never tap No ADS: it opens a real Google Play sheet with 1-tap buy. If a payment sheet opens,
  press Back at once.
  *Confirmed: 20260930-192115-chrono-2FYKPJ, 241.3.1 (frame of the sheet, not published).* [s:20260930-192115-chrono-2FYKPJ#22]
- An ad with no close button right after a WIN: do not `restart` — it reverts the level on the map (the
  coins, keys, league pins and gift % stay), and the level must be replayed. Try `launch` first; if the
  ad stays, budget the replay (a known order takes under a minute). Mid-level and after a loss
  `restart` is safe. Lost this way: level 9 four times, levels 14, 19 and 21.
  [s:20261001-054205-chrono-2FYKPJ#12] [s:20261001-102608-chrono-2FYKPJ#29] [s:20261001-153137-chrono-2FYKPJ#15]
  [s:20261001-160324-chrono-2FYKPJ#16] [s:20261001-075644-chrono-2FYKPJ#13]
  > ⚠️ Previously (241.3.1, 2026-09-30): "closing the game and starting it again worked … `sw.py restart`
  > not yet tried in this game. Whether level progress survives is not verified." — now verified: after
  > a win it does not survive [s:20260930-201034-chrono-2FYKPJ#34] [s:20260930-201034-chrono-2FYKPJ#46].

  *Confirmed: 20261001-054205-chrono-2FYKPJ, 241.5.1; 20261001-102608-chrono-2FYKPJ, 241.5.1; 20261001-153137-chrono-2FYKPJ, 241.5.1; 20261001-160324-chrono-2FYKPJ, 241.5.1.*
- When an ad opens Google Play, use `launch` to come back. On 241.5.1 Back from the Store can land on
  an ad end card with no close [s:20261001-054205-chrono-2FYKPJ#23] [s:20261001-054205-chrono-2FYKPJ#25];
  `launch` returned to the game [s:20261001-102608-chrono-2FYKPJ#7] [s:20261001-164104-chrono-2FYKPJ#22].
  Waiting for a close button that never comes cost 84-100 s per ad [s:20261001-153137-chrono-2FYKPJ#22]
  [s:20261001-162240-chrono-2FYKPJ#11].
  > ⚠️ Previously (241.3.1): "press Back once or twice to return to the game" [s:20260930-201034-chrono-2FYKPJ#52]
  > [s:20260930-201034-chrono-2FYKPJ#61].

  *Confirmed: 20261001-054205-chrono-2FYKPJ, 241.5.1; 20261001-102608-chrono-2FYKPJ, 241.5.1; 20261001-164104-chrono-2FYKPJ, 241.5.1.*
- Rewarded video: wait about 25 s for Skip, then close with the X at the top left (45,110).
  *Confirmed: 20260930-192115-chrono-2FYKPJ, 241.3.1; 20261001-054205-chrono-2FYKPJ, 241.5.1; 20261001-220948-chrono-2FYKPJ, 241.5.1.* [s:20260930-192115-chrono-2FYKPJ#34] [s:20261001-054205-chrono-2FYKPJ#54] [s:20261001-220948-chrono-2FYKPJ#6]
- Keep the gap between pulls (`--gap 5`, 7 when a pin steers a channel balls just ran through): pulls
  closer together lost level 7 (floor opened before the painting ended), level 14, level 20 and the
  challenge (pins 0.5-0.7 s apart).
  *Confirmed: 20260930-201034-chrono-2FYKPJ, 241.3.1; 20261001-102608-chrono-2FYKPJ, 241.5.1; 20261001-154701-chrono-2FYKPJ, 241.5.1.* [s:20260930-201034-chrono-2FYKPJ#50] [s:20261001-102608-chrono-2FYKPJ#42] [s:20261001-154701-chrono-2FYKPJ#4] [s:20261001-154701-chrono-2FYKPJ#28]
- Multi Stage: after Play or a restart, look at the frame before sending a stored stage batch — the level
  resumes at the first unfinished stage (the stage cleared just before a stuck ad is not kept); a blind
  stage-1 batch on a level resumed at stage 3 did nothing useful.
  *Confirmed: 20261001-162240-chrono-2FYKPJ, 241.5.1 (frame: stages 1-2 checked); 20261001-075644-chrono-2FYKPJ, 241.5.1.* [s:20261001-162240-chrono-2FYKPJ#31] [s:20261001-162240-chrono-2FYKPJ#32] [s:20261001-075644-chrono-2FYKPJ#15]
- A hard board is not solved by guessing: write the board and solve it, or follow the advisor's
  (`sw.py ask`) order once you paid for it (49-180 s each). Ignoring the answer cost two losses on
  level 11 and the challenge; on the boss the advisor's coordinates were for the zoomed-out frame and
  had to be re-read after the camera moved.
  *Confirmed: 20261001-075644-chrono-2FYKPJ, 241.5.1; 20261001-154701-chrono-2FYKPJ, 241.5.1; 20261001-165538-chrono-2FYKPJ, 241.5.1.* [s:20261001-075644-chrono-2FYKPJ#36] [s:20261001-154701-chrono-2FYKPJ#12] [s:20261001-165538-chrono-2FYKPJ#46]
- Read where the tap lands on reward screens: on the puzzle-piece screen continue is at y about 1280; a
  tap at y 1200 hits "Get Another" and plays a video.
  *Confirmed: 20261001-102608-chrono-2FYKPJ, 241.5.1 (frame).* [s:20261001-102608-chrono-2FYKPJ#51]
- A boss level that costs more than 2 tries: lose and Skip for a video — it pays the full win and
  opens the next level; only the win streak is lost.
  *Confirmed: 20261001-220948-chrono-2FYKPJ, 241.5.1 (frames of the league and win screens).* [s:20261001-220948-chrono-2FYKPJ#8]
