---
game: com.oakever.arrows
title: "Levels: Amaze GO!"
type: levels
verified_at: 2026-10-07
---

# Levels: Amaze GO!

Every level the agents met, as its board looked at the start (the ad strips cropped). The notes tell where a new element or rule appears.

| level 3 | level 4 | level 5 | level 6 | level 7 |
|---|---|---|---|---|
| ![level 3](levels/0003.webp) | ![level 4](levels/0004.webp) | ![level 5](levels/0005.webp) | ![level 6](levels/0006.webp) | ![level 7](levels/0007.webp) |

| level 8 hard | level 9 | level 10 hard | level 11 | level 12 |
|---|---|---|---|---|
| ![level 8 hard](levels/0008.webp) | ![level 9](levels/0009.webp) | ![level 10 hard](levels/0010.webp) | ![level 11](levels/0011.webp) | ![level 12](levels/0012.webp) |

| level 13 hard | level 14 continue test | level 15 hard | level 16 | level 17 continue-ad test |
|---|---|---|---|---|
| ![level 13 hard](levels/0013.webp) | ![level 14 continue test](levels/0014.webp) | ![level 15 hard](levels/0015.webp) | ![level 16](levels/0016.webp) | ![level 17 continue-ad test](levels/0017.webp) |

| level 18 hard | level 19 | level 20 super hard | level 21 | level 22 hard |
|---|---|---|---|---|
| ![level 18 hard](levels/0018.webp) | ![level 19](levels/0019.webp) | ![level 20 super hard](levels/0020.webp) | ![level 21](levels/0021.webp) | ![level 22 hard](levels/0022.webp) |

| level 23 | daily challenge Oct 5 (past day) | daily challenge Oct 6 | daily Oct 4 | event countryside L1 |
|---|---|---|---|---|
| ![level 23](levels/0023.webp) | ![daily challenge Oct 5 (past day)](levels/daily-challenge-oct-5-past-day.webp) | ![daily challenge Oct 6](levels/daily-challenge-oct-6.webp) | ![daily Oct 4](levels/daily-oct-4.webp) | ![event countryside L1](levels/event-countryside-l1.webp) |

| event countryside L2 | event countryside L2 resume | level 3 guideline look |
|---|---|---|
| ![event countryside L2](levels/event-countryside-l2.webp) | ![event countryside L2 resume](levels/event-countryside-l2-resume.webp) | no frame |

## Tries

| Level | Mechanic | Result | Time | Note |
|---|---|---|---|---|
| level 3 | arrows-escape | 1 won | 35 s | 4 arrows, order outer->inner |
| level 4 | arrows-escape | 1 won | 105 s | L4 won Perfect (win screen seen, frame 25), 1 mistake: blocked tap = lost drop, arrow flashed red |
| level 5 | arrows-escape | 2 won, 2 quit | 863 s | Won via hint loop: hint highlights a free arrow green, panning the board; script taps green. 1 mistake (drop lost). |
| level 6 | arrows-escape | 1 won | 110 s | solver (fine pitch, button masked) cleared 28 arrows in 2 rounds of 14 taps, 3 stars, no drop lost; Rate Us popup over the win card |
| level 7 | arrows-escape | 1 won | 100 s | solver: 54 arrows on a ~45 px pitch board, 4 rounds, 51 taps (2 extra), 0 mistakes, 3 stars Arrow Pro!, in-game 00:55 |
| level 8 hard | arrows-escape | 1 won | 168 s | solver, no hints: board fit the screen at 35 px pitch (26x34 nodes), 78 arrows, 6 rounds of up to 14 taps, 0 mistakes; 3 stars Arrow Pro!, Time 01:30, Score 1700 |
| level 9 | arrows-escape | 1 won | 71 s | solver: 36 arrows, 3 rounds, 0 mistakes, 3 stars Unstoppable Today!, 00:37, score 1500 |
| level 10 hard | arrows-escape | 1 won | 268 s | solver: board fit at 23.6 px pitch (39x50 nodes), 99 arrows, 8 rounds, 0 mistakes; Untouchable! card behind the Bronze League popup |
| level 11 | arrows-escape | 1 won | 114 s | solver, 3 rounds, 1.6 min, 3 stars Untouchable, 4 gold arrows = 4 league points |
| level 12 | arrows-escape | 2 won | 157 s | solver; one blocked gold tap cost a drop; league +4 |
| level 13 hard | arrows-escape | 1 won | 160 s | Hard L13 solver 6 rounds, 3 stars |
| level 14 continue test | arrows-escape | 1 won | 132 s | after 3 deliberate blocked taps and free Continue: Comeback Win, 2 stars |
| level 15 hard | arrows-escape | 1 won, 2 quit | 455 s | Hard L15 after solver pitch fix; sparse board made pitch search double the pitch (26->52) so registration failed |
| level 16 | arrows-escape | 1 won, 2 lost | 272 s | Last Life Win! 1 star, 02:45, score 743, 96%, 2 mistakes, 0 hints. Round 4 lost 2 drops: the first tap (on a free arrow) was ignored, and the 2 taps chained on it (through a second chained arrow) hit  |
| level 17 continue-ad test | arrows-escape | 2 won | 168 s | Clutch Comeback! 2 stars, 02:49, score 1085, 95%, 3 mistakes (all 3 deliberate, for the rewarded Continue), 0 hints. Solver with chains off: 19 rounds, 0 drops lost by the solver. Level clock includes |
| level 18 hard | arrows-escape | 1 won | 328 s | Hard L18 fit the screen; solver 52 rounds, 0 mistakes; most rounds had 1 free arrow so 1 tap per round = slow (5 min); Arrow Master! 1232, 04:38; Silver jump card first (+4); interstitial after |
| level 19 | arrows-escape | 1 won | 186 s | solver 28 rounds, 0 mistakes, 2 stars Arrow Master 02:28; Silver +4 (8->12, 39th->33rd) |
| level 20 super hard | arrows-escape | 1 won | 300 s | Super Hard L20 (130 arrows, shaped board, fits the screen) by solver: 38 rounds, 04:11 in-game, 3 stars 'Unstoppable Today!', score 1163 (may still count). 1 drop lost right after the first chained ro |
| level 21 | arrows-escape | 1 won | 204 s | solver, 19 rounds, 18 chained rounds (2-6 chained each), drops 3 throughout: 0 drops lost. No Mistakes! 02:14, score 806, 100%, 0 mistakes, 0 hints. Interstitial started by itself ~3 s after the card. |
| level 22 hard | arrows-escape | 1 won, 1 quit | 288 s | Hard L22 (dense, ~25 px pitch at 1080) won by the solver with the half-pitch fix: 21 rounds, 131 moves, chained rounds all the way, 0 drops lost, No Mistakes! 3 stars, 03:29, score 961 (may still coun |
| level 23 | arrows-escape | 1 won | 92 s | L23 normal, 28 arrows: solver 5 rounds, 23 moves, chained rounds (2-3 chained each), 0 drops lost, Lightning Fast! 3 stars, 00:33, 100%, 0 mistakes, 0 hints, score 865 (count-up may be running). |
| daily challenge Oct 5 (past day) | arrows-escape | 1 won | 232 s | Past day Oct 5 (~100 arrows, Normal) by solver, 34 rounds, 03:14 in-game; 1 drop lost right after the first chained round (round 2, re-taps), chains off after; interstitial ~3 s after the card again |
| daily challenge Oct 6 | arrows-escape | 1 won | 335 s | Daily Oct 6 (shaped board, ~200 arrows, Normal difficulty) by solver, 35 rounds; 1 drop lost early (chains turned off), 04:44 in-game, accuracy 99%, 1 mistake, 0 hints. Interstitial came up ~3 s after |
| daily Oct 4 | arrows-escape | 1 lost | — | Deliberate loss on past-day Oct 4: 3 blocked arrows (one per call; a 2nd tap on an already red arrow cost no drop). Out of Lives: Continue (ad) or Restart. |
| event countryside L1 | worms-escape | 1 won | 268 s | Event L1 (worm skin) won manually: 13 decisions, 0 mistakes, 0 hints, in-game 04:12, 2 stars (Well Done!), score 848. Re-read the board after each batch, tap only worms free on that frame; one tap oft |
| event countryside L2 | worms-escape | 1 quit | — | Quit on purpose after the two rewarded hints (event quit outcome); big board, not attempted in full |
| event countryside L2 resume | worms-escape | 1 quit | — | Opened only to verify the saved board after quit; left again |
| level 3 guideline look | arrows-escape | 1 quit | — | look only |
