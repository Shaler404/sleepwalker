# Tasks: Block Blast!

Status: **▶️ active** — ready now: 27

Mode: **goals** — work through the session goals in order; play levels only as far as an unlock or experiment goal needs; register anything new you notice as a feature or a goal, do not pursue it now

Progress reached: **Water Sort L2** · last new feature found at: **adventure L4**

Goals: study 2, experiment 27 · maps: classic best 327 — 16 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **classic** — studying, solver, levels won 0; **adventure** — mastered, solver, levels won 5, typical 3.1 min; **fruit-merge** — studying, heuristic, levels won 0; **mahjong-mg** — studying, manual, levels won 1, typical 1.9 min; **one-line** — studying, solver, levels won 0; **onet** — studying, solver, levels won 0; **sudoku** — studying, solver, levels won 1; **water-sort** — studying, solver, levels won 1, typical 1.0 min

Google Play version: **10.8.0** (checked 2026-10-05 22:05:43) · analyzed version: **10.8.1** · FTUE from a fresh install: **never**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| What makes the grey Default Skin button in Settings active (other skins)? | experiment | [Skins (Default Skin button)](features/skins.md) | knowledge gap |  |
| What the red vibration badge on the gear means and when it clears | experiment | [Settings](features/settings.md) | knowledge gap |  |
| What the green dot ring around the classic board means (seen from score ~319 of the first game) | experiment | [Classic mode (endless 8x8)](features/classic.md) | knowledge gap | dream: frames show the ring absent at 187 (193423 shot 24) and present at 223 (shot 25) while the best was already 124, so 'ring = new best' is unlikely; test a threshold near 200 |
| Is a revive / second chance offered at game over in later games? | experiment | [Classic mode (endless 8x8)](features/classic.md) | knowledge gap |  |
| How often the game-over interstitial plays | experiment | [Interstitial ad during classic play](features/ad-interstitial-classic.md) | knowledge gap |  |
| Look for daily rewards, a daily challenge or a timed event after day 1 | experiment |  | knowledge gap |  |
| Look for a shop, a no-ads purchase or any offer popup | experiment |  | knowledge gap |  |
| Run each outcome once under Consecutive Daily Victories: Leaving the app mid-game | experiment | [Consecutive Daily Victories](features/daily-victories.md) | knowledge gap |  |
| Run each outcome once under Adventure diamond-collection levels: Leaving the app mid-game | experiment | [Adventure diamond-collection levels](features/adv-diamonds.md) | knowledge gap |  |
| Run each outcome once under Adventure Consecutive Victories (win streak): Leaving the app mid-game | experiment | [Adventure Consecutive Victories (win streak)](features/adv-win-streak.md) | knowledge gap |  |
| Win 2-3 Adventure levels in a row and watch the Consecutive Victories panel: does anything pay at x2, x3? | experiment | [Adventure Consecutive Victories (win streak)](features/adv-win-streak.md) | knowledge gap |  |
| How often an interstitial follows an Adventure result: seen after the L2 retry win (not after L1, the L2 loss or L3) | experiment | [Adventure mode](features/adventure.md) | knowledge gap |  |
| Classic: press Back with score > 0, then Classic: is the game in progress kept? Also leave the app mid-game and launch | experiment | [Classic mode (endless 8x8)](features/classic.md) | knowledge gap |  |
| Find how to close the Royal Match interstitial with a store header without opening Google Play | experiment | [Interstitial ad during classic play](features/ad-interstitial-classic.md) | knowledge gap |  |
| Adventure: tap Retry on the loss panel and Next Level on the win panel; gear > Replay inside a level | experiment | [Adventure mode](features/adventure.md) | knowledge gap |  |
| Play Adventure levels 5-12 and record which have gem goals | experiment | [Adventure diamond-collection levels](features/adv-diamonds.md) | knowledge gap |  |
| Run each outcome once under Adventure hard levels (Next Hard Level): Settings gear > Replay, No Space Left, Back key mid-game opens the home menu with no confirmation; whether the game in progress is kept is NOT verified, Leaving the app mid-game | experiment | Adventure hard levels (Next Hard Level) | knowledge gap |  |
| Lose Adventure hard level once (replay L5 or next hard) to see its fail screen and cost | experiment | Adventure hard levels (Next Hard Level) | knowledge gap |  |
| Record which Adventure levels L6-L15 are hard (purple Next Hard Level on the previous win) | experiment | Adventure hard levels (Next Hard Level) | knowledge gap |  |
| Find whether Fruit Merge has a win: is making a watermelon an end screen or is the jar endless | experiment | [Mini-game: Fruit Merge](features/mg-fruit-merge.md) | knowledge gap |  |
| Mini-games: reopen One Line, Mahjong and Fruit Merge and record whether each resumes where it was left | experiment | [More Games (mini-game list)](features/more-games.md) | knowledge gap |  |
| Mini-games: count interstitials per win (does every One Line / Mahjong level win play an ad) | experiment | [More Games (mini-game list)](features/more-games.md) | knowledge gap |  |
| See Onet win screen (after the post-win ad; the ad froze twice) and whether any loss exists | experiment | [Mini-game: Onet](features/mg-onet.md) | knowledge gap |  |
| Onet: find when the greyed freeze-time tool becomes usable (timed levels or a level number) | experiment | [Mini-game: Onet](features/mg-onet.md) | knowledge gap |  |
| Sudoku: tap Yes on the leave dialog in L2, reopen Sudoku from More Games and record whether L2 resumes with its filled cells and timer or starts fresh | experiment | [Mini-game: Sudoku](features/mg-sudoku.md) | knowledge gap |  |
| Water Sort: find a loss/stuck state, restart, and limits (later levels with fewer empty tubes; leave with back arrow) | study | [Mini-game: Water Sort](features/mg-water-sort.md) | knowledge gap |  |
| Tic Tac Toe: win a real round against the robot and record the win screen and whether the 0 VS 0 scoreboard changes | experiment | [Mini-game: Tic Tac Toe](features/mg-tic-tac-toe.md) | knowledge gap |  |

## Waiting

| Task | Not before | Kind | Feature |
|---|---|---|---|
| After a day with no Adventure win, read the Consecutive Daily Victories counter: does a missed day reset it to x0 (and is a save offered)? | 2026-10-06 10:00:00 | daily | [Consecutive Daily Victories](features/daily-victories.md) |

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

| Task | What to provide | Feature |
|---|---|---|
| Tap Skip on the first-launch tutorial board and record what follows | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | [First-launch tutorial board](features/tutorial.md) |
| On a fresh install walk the consent window: Accept, links, whether it can be declined or comes back | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | [Terms of Use consent](features/terms-consent.md) |

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Study First-launch tutorial board: open it, walk its screens and tabs, verify its cases | 2026-10-06 03:34:28 | 20261006-032721-chrono-2FYKPJ#47 | Tutorial board appears only on a fresh install and cannot be opened on this progressed phone; chk-skip stays open under existing tutorial-skip (requires fresh). |
| Study Terms of Use consent: open it, walk its screens and tabs, verify its cases | 2026-10-06 03:34:27 | 20261006-032721-chrono-2FYKPJ#47 | Consent window itself shows only on first launch of a fresh install; studied what is reachable now: Terms of Use page via More Settings > Terms of Service (webview, no accept button). chk-options and chk-answers left for fresh install task terms-consent-fresh. |
| Open Privacy Policy, About Us, Contact Us, Share with Friends, social icons in More Settings and note where each leads | 2026-10-06 03:34:17 | 20261006-032721-chrono-2FYKPJ#47 | Contact Us: in-app Block Blast Support webview. Share: Android share sheet with onelink link. Privacy Policy and Terms of Service: in-app webviews (Hungry Studio/ARETIS, updated Aug 5 2026). About Us and Official icon: Chrome, official site share.blockblast.com. TikTok, Discord, X, Facebook: Chrome profile pages with login walls. YouTube: YouTube app. Back key closes webview and settings together. |
| Study Settings: open it, walk its screens and tabs, verify its cases | 2026-10-06 01:21:13 | 20261006-011754-chrono-2FYKPJ#17 | Toggles, slider, More Settings and Terms link checked; rest of links set as settings-links-rest |
| Study Skins (Default Skin button): open it, walk its screens and tabs, verify its cases | 2026-10-06 01:21:12 | 20261006-011754-chrono-2FYKPJ#17 | Default Skin is a disabled grey button in Settings; tap does nothing; no skin screen exists; unlock rule left to skins-unlock |
| Study More Games (mini-game list): open it, walk its screens and tabs, verify its cases | 2026-10-06 01:18:53 | 20261006-011754-chrono-2FYKPJ#3 | List of 8 open mini-games walked from the home menu, scrolled to Block Slide; unchanged with progress |
| Find a way out of the frozen playable ad after a mini-game ends (without a restart) so the win or game over screen behind it is seen | 2026-10-05 23:32:29 | 20261005-231555-chrono-2FYKPJ#25 | Tic Tac Toe: after the round the video ad turns into a Royal Match playable; Back at once does nothing, but after about 40-45 s Back closes it and the Draw / You Lost screen is shown (steps 20-21, 24-25). No restart needed |
| Study Mini-game: Tic Tac Toe: open it, walk its screens and tabs, verify its cases | 2026-10-05 23:29:11 | 20261005-231555-chrono-2FYKPJ#38 | tutorial, board, draw, loss with ad, Home/Play Again; real win not played |
| Study Mini-game: Water Sort: open it, walk its screens and tabs, verify its cases | 2026-10-05 23:29:11 | 20261005-231555-chrono-2FYKPJ#38 | tutorial, L1 won, L2 seen, add-tube/hint/undo tested; loss and limits open in water-sort-loss-limits |
| Reach Mahjong no-moves state: pair tiles so twins stay buried until MATCHES reads 0, mark the screen | 2026-10-05 23:29:10 | 20261005-231555-chrono-2FYKPJ#38 | L3 played with deliberate pairings (screens 5-10): no dead end, twins always reached; game seems generated solvable; loss unreached, chk-loss stays open |
| Reach Mahjong no-moves loss (or shuffle prompt), mark screen (cancelled) | 2026-10-05 16:00:20 | 20261005-153835-chrono-2FYKPJ#50 | duplicate of mahjong-loss-3 (same goal, set by session 153835 with the method: leave twins buried until MATCHES reads 0); this session won L2 instead |
| Study Mini-game: Sudoku: open it, walk its screens and tabs, verify its cases | 2026-10-05 15:57:15 | 20261005-153835-chrono-2FYKPJ#50 | Walked tutorial, board, mistake, out-of-hearts sheet, win panel, L2 opens |
| Reach Fruit Merge game over again: keep dropping at x=365 until the line is crossed, then Back-key the ad | 2026-10-05 15:44:13 | 20261005-153835-chrono-2FYKPJ#12 | Game over reached after about 140 center drops (score 7680); video ad then store sheet, launch+Back showed Game Over screen |
| Reach Fruit Merge game over: drop mismatched fruits to overflow, mark loss screen (cancelled) | 2026-10-05 13:33:05 | 20261005-131038-chrono-2FYKPJ#18 | superseded by fruit-merge-loss-2 (same goal with the working recipe: drop at x=365 about 50 times, then Back-key the ad); the overflow was reached at step 9 but the ad froze and hid the game over |
| Study Mini-game: Onet: open it, walk its screens and tabs, verify its cases | 2026-10-05 13:33:04 | 20261005-131038-chrono-2FYKPJ#41 | screen, rules, progression and limits closed (steps 25-41, tutorial, L1 cleared, tools, restart prompt counts a Loss); win and loss screens continue in onet-win-loss |
| Study Mini-game: One Line: open it, walk its screens and tabs, verify its cases | 2026-10-05 13:09:43 | 20261005-125535-chrono-2FYKPJ#45 | Walked tutorial, L1 win, L2 dead end and hint, interstitials; playable ad after L2 stuck, restart needed |
| Study Mini-game: Mahjong: open it, walk its screens and tabs, verify its cases | 2026-10-05 13:04:10 | 20261005-125535-chrono-2FYKPJ#32 | Walked tutorial L1 (won), L2 tools hint/shuffle/undo, restart and leave dialogs, win screen with interstitial. Loss (no moves left) not reached: chk-loss open |
| Study Mini-game: Fruit Merge: open it, walk its screens and tabs, verify its cases | 2026-10-05 13:00:35 | 20261005-125535-chrono-2FYKPJ#16 | Walked screen, rules, both boosters, restart confirm, exit. Loss (overflow) and win not reached in 140 drops: merging keeps jar low; chk-win and chk-loss left open |
| Study the home menu (Adventure, Medal, daily victories, cross-promo icons) | 2026-10-05 01:58:57 | 20261005-015205-chrono-2FYKPJ#22 | Walked home menu, entries and badges |
| Study Adventure hard levels: start L5 (Next Hard Level), record its screen, what differs from a normal level, its win and its loss | 2026-10-05 01:58:57 | 20261005-015205-chrono-2FYKPJ#22 | L5 hard won (28/26/26 gems), no visible marker or extra rules; loss not seen, task hard-loss set |
| Study Medal: open it, walk its screens and tabs, verify its cases | 2026-10-05 01:58:56 | 20261005-015205-chrono-2FYKPJ#22 | Achievement screen, 9 tiered awards, award popups, locked Adventurer |
| L5 is offered as Next Hard Level (purple button after L4 win): open it, record what a hard level is (cancelled) | 2026-10-05 00:54:38 | review-20261005 | duplicate: hard levels are now their own feature adv-hard-levels (level-type); its study goal replaces this one |
| Study Adventure diamond-collection levels: open it, walk its screens and tabs, verify its cases | 2026-10-05 00:52:33 | 20261005-004506-chrono-2FYKPJ#24 | Banner Target Collection at start, Replay gives interstitial+restart, win gives Next Hard Level for L5; frequency (which levels) left to experiment adv-diamonds-frequency |
| Study Consecutive Daily Victories: open it, walk its screens and tabs, verify its cases | 2026-10-05 00:52:24 | 20261005-004506-chrono-2FYKPJ#24 | x2 grey -> x3 green after Oct 5 win; panel not tappable; missed-day and save offer remain open (task daily-victories-missed-day) |
| Study Cross-promo icons on the home menu (GOGO! Blast, Rotate Rings): open it, walk its screens and tabs, verify its cases | 2026-10-05 00:52:24 | 20261005-004506-chrono-2FYKPJ#24 | Both icons open the Open with store chooser; static, no reward, Back closes |
| Find why the classic score jumped from 19 to 124 with no move right after the tutorial board | 2026-10-04 01:10:05 | dream | Answered: a count-up. The 2x2 clear gives +120 and the score counts 4 -> 124; the 19 was a mid count-up frame [20261003-193423-chrono-2FYKPJ#4] (documenter clip tutorial-2x2-clear) |
| Study Adventure Consecutive Victories (win streak): open it, walk its screens and tabs, verify its cases | 2026-10-04 00:11:41 | 20261003-235233-chrono-2FYKPJ#60 | All checklist items closed this session: counter on the Adventure result panel (x1 L1 win, x0 after L2 loss, x2 after L3), reset by a loss, no save, no reward at x1-x2, no entry (shows by itself). Outcome runs left to outcomes-adv-win-streak; rewards past x2 to adv-win-streak-rewards |
| Study Adventure mode: open it, walk its screens and tabs, verify its cases | 2026-10-04 00:07:04 | 20261003-235233-chrono-2FYKPJ#64 | Adventure: 96-level trophy-shaped map (shot 8), Level N button, no energy/lives/timer. Levels are the classic 8x8 board with a pre-built layout and a goal: L1 score 368, L2 60 diamonds, L3 two gem colours, L4 three. Win: Consecutive Victories panel + lit trophy cell + Next Level, no currency; interstitial seen once (after L2 retry win). Loss: No Space Left -> 'You Can Do It!' + Retry, win streak resets, no revive. Gear: Settings with Home/Replay. Played L1 won, L2 lost (deliberate) then won, L3 won, L4 quit; the classic solver in score mode wins them in ~2-3 min. New features: adv-diamonds (gem-goal levels), adv-win-streak. |
| Win an Adventure level on the next day and check whether the counter goes x1 -> x2 (and whether a second win the same day changes it) (cancelled) | 2026-10-04 00:06:09 | 20261003-235233-chrono-2FYKPJ#60 | answered this session: the session crossed midnight; a win on the next day made x1 -> x2 and a second same-day win kept x2 |
| Find what raises the Consecutive Daily Victories counter (x0) on the home menu | 2026-10-03 23:57:20 | 20261003-235233-chrono-2FYKPJ#22 | One Adventure level win (L1, target 368) raised the home-menu counter from x0 to x1 and turned the check mark green (shot 27); the win screen itself shows a 'Consecutive Victories x1' panel. The Adventure button's red dot disappeared too. Whether a second win the same day adds more, and whether a missed day resets it, is open |
| Land a tray piece on classic row 7 (the bottom row) by drag and record the finger end point that works | 2026-10-03 23:54:02 | 20261003-235233-chrono-2FYKPJ#4 | Row 7 is reachable by drag: 1-row horizontal 2-line touched at its left block (347,1210) and released at finger (415,1186) landed on row 7 cols 4-5 (shot 6). Finger end = 24 px ABOVE the touch point = 166 px (2.05 cells) under the board's bottom edge (1020). The plan's 0.5/1/1.5-cell offsets come from the old 2.84 model and would land the piece 1-2 rows higher; the v10.8.1 formula finger_y = y0 + (Y - y0 + 195)/1.46 is right: also 2x2 rows 6-7 (finger 1142 and 1153 from touch y 1192) and vertical 2-line rows 6-7 (finger 1164 from touch 1228) all landed first try (shots 4-5). |
| Find why Medal appeared: Medal icon with badge on the home menu top right | 2026-10-03 21:41:25 | planner | the trigger is recorded as a fact: on the home menu (top right, with a red badge) the first time it was opened by Back from classic [20261003-212548-chrono-2FYKPJ#29] |
| Does a home screen or another mode (e.g. Adventure) appear after more classic games or days? | 2026-10-03 21:41:16 | 20261003-212548-chrono-2FYKPJ#29 | a home menu exists: Back in a classic game opens it (Adventure, Classic, More Games, Medal, Consecutive Daily Victories, cross-promo icons); no extra games or days needed |
| Experiment: classic board where only row 7 is empty and tray has 1-row lines: is it a real stuck state? (cancelled) | 2026-10-03 21:41:09 | review-20261003 | not a game state: on the frame (shot 32) row 7 is empty and all three tray lines (5,3,4) fit it, so the game rightly declared no game over; the drag cannot reach row 7 (harness low-drop cutoff). Replaced by classic-bottom-row-drop |
| Study Mini-game: Block Slide: open it, walk its screens and tabs, verify its cases | 2026-10-03 21:37:27 | 20261003-212548-chrono-2FYKPJ#45 | rules, clear score 30, game over after stack hits top, ad then Game Over screen |
| Study Classic mode (endless 8x8): open it, walk its screens and tabs, verify its cases | 2026-10-03 21:37:26 | 20261003-212548-chrono-2FYKPJ#45 | Settings popup, Replay, back to home menu, 2516 stuck-board bug, cases done |
| Study Interstitial ad during classic play: open it, walk its screens and tabs, verify its cases | 2026-10-03 21:37:26 | 20261003-212548-chrono-2FYKPJ#45 | Seen after No Space Left and after Replay (settings); skip icon opens store; end card at ~45 s |
| Find why Skins (Default Skin button) appeared: grey Default Skin button in Settings from the first launch; a tap does nothing, other skins probably come with progress or events | 2026-10-03 19:44:34 | planner | the trigger is recorded as a fact: in Settings from the first launch: a grey Default Skin button under Replay [20261003-193423-chrono-2FYKPJ#5] |
| Map the game: play until the main menu and every entry point is visible; list each entry point as open (a study goal), locked with its unlock condition (an unlock goal) or unclear (an experiment) | 2026-10-03 19:41:55 | 20261003-193423-chrono-2FYKPJ#32 | Fresh install v10.8.1: consent -> one tutorial board -> classic board directly; no home/mode menu even after game over (Play restarts classic). HUD: crown best (not a button), gear. Settings: Sound/BGM/Vibration, More Games (8 built-in mini-games, each registered as a mode, open), More Settings (external links), Replay, Default Skin (grey, unclear -> experiment). Game over: No Space Left -> interstitial -> 'Can you Top that?' + Play, no revive. No locked entries seen; experiments added: home-menu-appears, gear-badge, green-dots-ring, revive-check, ad-cadence, skins-unlock. |
