---
game: com.block.juggle
title: "Lessons"
type: agent
version_seen: 10.8.1
verified_at: 2026-10-07
---

# Lessons for the agent: Block Blast!

- When an interstitial shows a store header with a top-left >| icon, do not tap it: it opens Google Play. If the ad ends on a playable end card with no X, press the Back key: `launch` does nothing while the app is already in front.
  ⚠️ Previously: "Wait for the ad to end, then `launch`." Two sessions saw an end card that never ended (95 s and 88 s of waiting) and was closed by Back.
  *Confirmed: 20261003-212548-chrono-2FYKPJ, 20261003-235233-chrono-2FYKPJ, 20261005-004506-chrono-2FYKPJ, 20261005-015205-chrono-2FYKPJ, 10.8.1.* [s:20261005-004506-chrono-2FYKPJ#12] [s:20261005-004506-chrono-2FYKPJ#13] [s:20261005-015205-chrono-2FYKPJ#21] [s:20261003-212548-chrono-2FYKPJ#27] [s:20261003-212548-chrono-2FYKPJ#43] [s:20261003-235233-chrono-2FYKPJ#44]
- Give the solver its mode on the first `solve --run` with `--board <file>` (a file path, not inline JSON; e.g. a file holding {"mode":"score"} for Adventure): a mode passed on a plain `solve` call is dropped.
  *Confirmed: 20261003-235233-chrono-2FYKPJ, 20261005-004506-chrono-2FYKPJ, 10.8.1.* [s:20261005-004506-chrono-2FYKPJ#13] [s:20261003-235233-chrono-2FYKPJ#8]
- To reach the home menu, press Back on the classic board; the board has no menu button. The app may open on the home menu instead of the board: look at the first frame.
  ⚠️ Previously: "the app opens straight on the board". After relaunches on 2026-10-06 it opened on the home menu [s:20261006-053412-chrono-2FYKPJ#0] [s:20261006-084209-chrono-2FYKPJ#0].
  *Confirmed: 20261003-212548-chrono-2FYKPJ, 20261003-235233-chrono-2FYKPJ, 10.8.1.* [s:20261003-212548-chrono-2FYKPJ#29] [s:20261003-235233-chrono-2FYKPJ#5]
- After a mini-game ends, an ad plays and a playable ad can follow with no close button: wait about 40-45 s, then press Back; restart only if that fails (a restart during the ad loses the win screen).
  ⚠️ After a Water Sort Restart the playable end card ignored Back twice and 20 s of waiting; only an app restart got out, and the level stayed where it was [s:20261006-053412-chrono-2FYKPJ#10] [s:20261006-053412-chrono-2FYKPJ#11] [s:20261006-053412-chrono-2FYKPJ#12].
  *Confirmed: 20261005-231555-chrono-2FYKPJ, 10.8.1; 20261005-131038-chrono-2FYKPJ, 10.8.1.* [s:20261005-231555-chrono-2FYKPJ#20] [s:20261005-231555-chrono-2FYKPJ#24] [s:20261005-131038-chrono-2FYKPJ#33]
- The harness `taps` command takes two-point swipes only and at most 40 moves per call: draw One Line runs as separate swipes and split large batches.
  *Confirmed: 20261005-125535-chrono-2FYKPJ, 10.8.1; 20261005-131038-chrono-2FYKPJ, 10.8.1.* [s:20261005-125535-chrono-2FYKPJ#33] [s:20261005-131038-chrono-2FYKPJ#5]
- Game Over and result buttons slide in from the bottom: wait until they settle (about y 1220 on Fruit Merge) before tapping.
  *Confirmed: 20261005-153835-chrono-2FYKPJ, 10.8.1.* [s:20261005-153835-chrono-2FYKPJ#13]
- The More Settings button of the classic Settings sits at y 767 (it was 833 in older notes); a tap at the old place leaves the frame unchanged.
  *Confirmed: 20261006-032721-chrono-2FYKPJ, 10.8.1.* [s:20261006-032721-chrono-2FYKPJ#3]
- An ad with a Google Play bar and a top-left "Next" opens a Play Store sheet by itself and ends on a playable that ignores Back, Next and waiting. Close the sheet with its X (677,408) and restart the app at once: the game over, the best score and an Adventure win are kept. Ads with a store header (Royal Match, Match Masters) still close with one Back.
  *Confirmed: 20261006-105231-chrono-2FYKPJ, 20261006-111957-chrono-2FYKPJ, 20261006-133549-chrono-2FYKPJ, 20261006-141221-chrono-2FYKPJ, 10.8.1.* [s:20261006-105231-chrono-2FYKPJ#6] [s:20261006-105231-chrono-2FYKPJ#14] [s:20261006-111957-chrono-2FYKPJ#11] [s:20261006-111957-chrono-2FYKPJ#14] [s:20261006-133549-chrono-2FYKPJ#69] [s:20261006-133549-chrono-2FYKPJ#71] [s:20261006-141221-chrono-2FYKPJ#90] [s:20261006-141221-chrono-2FYKPJ#93] [s:20261006-133549-chrono-2FYKPJ#37] [s:20261006-141221-chrono-2FYKPJ#44]
- Interstitials follow a time cooldown shared by classic game overs and Adventure wins, counted from the previous ad's close (about 3-4.7 min), not a game count. In an ad test, space results in time and log each ad's close minute; the first result after a launch is not ad-free (an early no-ad is the ad not loaded yet).
  *Confirmed: 20261006-105231-chrono-2FYKPJ, 20261006-133549-chrono-2FYKPJ, 20261006-141221-chrono-2FYKPJ, 10.8.1.* [s:20261006-105231-chrono-2FYKPJ#51] [s:20261006-133549-chrono-2FYKPJ#37] [s:20261006-141221-chrono-2FYKPJ#6] [s:20261006-141221-chrono-2FYKPJ#93]
- To end classic games fast (ad or loss tests), run the classic solver in its gameover BLOCK mode: 15 of 15 games ended in 0.4-1.3 min. The fill-fast mode ran 10.7 min with no game over; stop and re-plan when a solver run makes no progress toward the goal for about 5 min.
  *Confirmed: 20261006-084209-chrono-2FYKPJ, 20261006-105231-chrono-2FYKPJ, 20261006-111957-chrono-2FYKPJ, 20261006-133549-chrono-2FYKPJ, 10.8.1.* [s:20261006-084209-chrono-2FYKPJ#58] [s:20261006-084209-chrono-2FYKPJ#103] [s:20261006-105231-chrono-2FYKPJ#49] [s:20261006-111957-chrono-2FYKPJ#23] [s:20261006-133549-chrono-2FYKPJ#36]
- Before forcing a Water Sort loss, search the board (BFS over the pours): boards up to Level 7 have no reachable dead end, so the only loss there is the Restart arrow (counted as a Loss).
  *Confirmed: 20261006-053412-chrono-2FYKPJ, 20261006-084209-chrono-2FYKPJ, 10.8.1.* [s:20261006-053412-chrono-2FYKPJ#7] [s:20261006-053412-chrono-2FYKPJ#16] [s:20261006-084209-chrono-2FYKPJ#18]
