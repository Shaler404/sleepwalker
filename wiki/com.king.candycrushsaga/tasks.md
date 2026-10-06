# Tasks: Candy Crush Saga

Status: **▶️ active** — ready now: 28

Mode: **goals** — work through the session goals in order; play levels only as far as an unlock or experiment goal needs; register anything new you notice as a feature or a goal, do not pursue it now

Progress reached: **level 1** · last new feature found at: **level 1**

Goals: study 3, unlock 6, experiment 19 · maps: level 1 won, on map before level 2 — 11 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **core-match** — mastered, manual, levels won 4, typical 4.9 min

Google Play version: **1.337.0.2** (checked 2026-10-05 22:05:43) · analyzed version: **1.337.0.2** · FTUE from a fresh install: **never**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Unlock Candy Teams: level 20 | unlock | [Candy Teams](features/candy-teams.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Unlock Boosters (hand, lollipop hammer etc.): not shown, about level 3-10 | unlock | [Boosters (hand, lollipop hammer etc.)](features/boosters.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Find why Mailbox icon appeared: envelope icon in the top bar of the map from the start; tap did nothing (inbox empty or needs account) | experiment | [Mailbox icon](features/mailbox.md) | knowledge gap |  |
| Mailbox envelope tap does nothing: test again after a few levels or when it shows a badge | experiment | [Mailbox icon](features/mailbox.md) | knowledge gap |  |
| Run each outcome once under Events tab: Order done, Gear > Settings > Quit level > confirm 'Play on' / 'Quit -1 heart'; shows Level failed with Score and Retry, X goes to map; life 5->4, Out of moves, Force-stop mid level, No Restart button in the in-level settings (sound, Audio, Save progress, Quit level); restart only by quit and replay from map popup | experiment | [Events tab](features/events-tab.md) | knowledge gap |  |
| Study Terms of Use consent: open it, walk its screens and tabs, verify its cases | study | Terms of Use consent | external |  |
| Find what the 3 Select boosters slots in the level start popup do at 0 balance (free trial, gold bars, or locked) | experiment | [Boosters (hand, lollipop hammer etc.)](features/boosters.md) | knowledge gap |  |
| Look for typical features not seen yet: daily reward or login calendar, starter or limited-time offer popups, rewarded ads, piggy bank, season pass, language option | experiment |  | knowledge gap |  |
| Colour bomb combined with striped, wrapped and another colour bomb | experiment | [Colour bomb](features/color-bomb.md) | knowledge gap |  |
| Lose a level by running out of moves and record the fail screen, retry and life cost | experiment | [Level (core match-3)](features/core-level.md) | knowledge gap |  |
| Record the full win sequence: Sugar Crush with moves left, final stars, score and any reward on Level completed | experiment | [Level (core match-3)](features/core-level.md) | knowledge gap |  |
| Study Wrapped candy: make or meet it in a level, mark it, verify its cases | study | Wrapped candy | knowledge gap |  |
| Tap the mail and gold-bar icons from the Map tab (not the Shop tab) and record what opens | experiment | Gold bars | knowledge gap |  |
| Find why Sweet gift (launch gift) appeared: comeback gift on the first launch after a long absence (about 25 h away before the 10-05 00:19 gift); not shown at 10-06 02:09 when the previous session ended about 2 h earlier, so not a fixed daily calendar | experiment | Sweet gift (launch gift) | knowledge gap |  |
| Find what the level 4 cap (colour-bomb icon) releases and when | experiment | Candy dispenser | knowledge gap |  |
| Study Sweet gift (launch gift): open it, walk its screens and tabs, verify its cases | study | Sweet gift (launch gift) | external |  |
| Fish combos: swap fish with striped/wrapped/colour bomb, fish as an order, fish in a loss | experiment | Fish candy | knowledge gap |  |
| Reach 0 lives and record the out-of-lives screen and its refill offers | experiment | [Lives](features/lives.md) | knowledge gap |  |
| Win level 4 and keep winning up to level 10: progress recorded past level 3, boosters lock watched | experiment | [Level (core match-3)](features/core-level.md) | knowledge gap | Progress stuck: 6 quits on L4 across sessions 20261003-225003..20261005-220615, no win since L3; unlock-candy-teams (L20), unlock-boosters, boosters-lock-exp, lives-zero and look-genre-features all wait on it |
| Pins: win more levels and re-open Pins to see when the first pin appears and what earns it | experiment | [Pins collection](features/pins.md) | knowledge gap |  |
| Profile inventory slots unlock at levels 7, 10, 20: re-check profile after reaching them | experiment | [Profile and inventory](features/profile.md) | knowledge gap |  |
| Settings > Account & Help: open Help center and Forum links and see where they lead (launch back at once) | experiment | [Settings](features/settings.md) | knowledge gap |  |
| Unlock Lollipop hammer booster: level 7 | unlock | Lollipop hammer booster | knowledge gap | the lock seen on screen (feature --locked) |
| Unlock Colour bomb booster (inventory): level 10 | unlock | Colour bomb booster (inventory) | knowledge gap | the lock seen on screen (feature --locked) |
| Unlock Striped + wrapped booster: level 20 | unlock | Striped + wrapped booster | knowledge gap | the lock seen on screen (feature --locked) |
| Unlock Round candy booster (inventory row 2 #1): level 65 | unlock | Round candy booster (inventory row 2 #1) | knowledge gap | the lock seen on screen (feature --locked) |
| Profile inventory: read the Unlocks at level N tooltip of the 6 slots not tapped yet (row 2 #2-4, row 3 #1-3) | experiment | [Profile and inventory](features/profile.md) | knowledge gap |  |
| Profile Edit > Frames: find what the locked frame with the 20000 badge needs (tap it and read the tooltip) | experiment | [Profile and inventory](features/profile.md) | knowledge gap |  |

## Waiting

None.

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

| Task | What to provide | Feature |
|---|---|---|
| Study the notification permission prompt on a fresh install: screen, both answers, whether it returns | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | Notification permission prompt |

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Study Striped candy: open it, walk its screens and tabs, verify its cases | 2026-10-06 02:13:23 | 20261006-020945-chrono-2FYKPJ#9 | Made striped via 4-line swap on L1, fired by matching with 2 blue: row cleared (32->18). Combos untested. |
| Study Shop: open it, walk its screens and tabs, verify its cases | 2026-10-06 02:11:05 | 20261006-020945-chrono-2FYKPJ#3 | Walked tab, More Offers; frequency, close, timer closed. chk-buy-path left open: price buttons open a payment sheet, never tapped. |
| Sweet gift: launch the next day and note whether the gift comes again, what it gives and at what hour (calendar or one-off) | 2026-10-06 02:10:33 | 20261006-020945-chrono-2FYKPJ#1 | Launch 2026-10-06 02:09: no Sweet gift popup (frames 1-2), lives 5 Full. Not a daily calendar at this hour; trigger likely a comeback after a long absence or lives not full. Gift at 10-05 was 00:19. |
| Find what unlocks boosters: locks seen in level bottom bar and profile inventory, level not shown | 2026-10-06 00:17:13 | 20261006-000939-chrono-2FYKPJ#10 | Profile inventory tooltips give the unlock levels: lollipop hammer 7, colour bomb 10, striped+wrapped 20, row 2 #1 round candy 65; 6 slots not tapped (inventory-tooltips-rest). Each slot is its own feature with an unlock goal |
| Study Settings: open it, walk its screens and tabs, verify its cases | 2026-10-06 00:14:24 | 20261006-000939-chrono-2FYKPJ#31 | General, More Audio, Features, Accessibility, Account & Help walked; links left to settings-links |
| Study Pins collection: open it, walk its screens and tabs, verify its cases | 2026-10-06 00:14:23 | 20261006-000939-chrono-2FYKPJ#31 | Collection empty (keep passing levels), Awards coming soon; items/earn/use/complete need later levels (task pins-unlock-items) |
| Study Profile and inventory: open it, walk its screens and tabs, verify its cases | 2026-10-06 00:14:23 | 20261006-000939-chrono-2FYKPJ#31 | Profile popup, name prompt, avatar card, Edit Avatars/Frames, inventory lock tooltips levels 7/10/20 checked |
| Study Notification permission prompt: open it, walk its screens and tabs, verify its cases | 2026-10-05 22:10:07 | 20261005-220615-chrono-2FYKPJ#12 | Prompt cannot be opened on a progressed install (no return after relaunch); cases left open, moved to fresh-install task notif-prompt-fresh |
| Study Meringue blocker: make or meet it in a level, mark it, verify its cases | 2026-10-05 22:10:07 | 20261005-220615-chrono-2FYKPJ#12 | L4 meringue: bomb+green took 59 to 21 layers; cases closed |
| Study Level map: open it, walk its screens and tabs, verify its cases | 2026-10-05 22:10:06 | 20261005-220615-chrono-2FYKPJ#12 | Map walked: scrolled both ends, node popup, lives timer; all 5 cases closed |
| Study Mailbox icon: open it, walk its screens and tabs, verify its cases | 2026-10-05 13:32:56 | 20261005-133157-chrono-2FYKPJ#3 | Envelope inert and greyed on map at L4; no screens |
| Study Lives: open it, walk its screens and tabs, verify its cases | 2026-10-05 13:32:39 | 20261005-133157-chrono-2FYKPJ#2 | Popup walked at 5/Full; all cases closed except chk-empty (task lives-zero) |
| Check lives at 5 again: 3 lives at 07:26 with timer 30 min per life; expect 5/Full about 08:30 | 2026-10-05 13:32:15 | 20261005-133157-chrono-2FYKPJ#0 | Lives 5/Full on map at 13:32 (frame 1), cap is 5 |
| Find why Fish candy appeared: made by a 2x2 square match; first seen on level 3 board (shot 80) | 2026-10-05 07:34:28 | planner | the trigger is recorded as a fact: made by the player: one swap that puts 4 same-colour candies in a 2x2 square with no 3-line (L1 replay, frame 35) [20261005-072135-chrono-2FYKPJ#26] |
| Study Fish candy: make or meet it in a level, mark it, verify its cases | 2026-10-05 07:31:53 | 20261005-072135-chrono-2FYKPJ#31 | Made fish on L1 (2x2 swap), activated via match; rules recorded; interactions/loss left as experiment fish-interactions |
| Watch lives refill after the 2h unlimited gift ends (lose lives to 3, time per life, cap) | 2026-10-05 07:31:53 | 20261005-072135-chrono-2FYKPJ#31 | Gift ended: lives 5 Full. Two quits: 5->4->3, timer starts 29:07 (about 30 min per life, counts to next life only). 07:31 timer 22:50 on 3 lives. Full refill to 5 not watched (needs about 1h): task lives-cap-check |
| Study Gold bars: open it, walk its screens and tabs, verify its cases | 2026-10-05 07:23:50 | 20261005-072135-chrono-2FYKPJ#5 | Gold counter opens Shop; packs, bundles, 69-gold sink marked |
| Study Candy dispenser: make or meet it in a level, mark it, verify its cases | 2026-10-05 00:22:13 | 20261005-001914-chrono-2FYKPJ#8 | Dispenser on L4 top row: drops a colour bomb sometimes (once in 3 refills seen), otherwise plain candies |
| Watch the map heart from 3 lives to Full: time per life and the cap (timer read 26:10 -> 24:05 across a life loss) (cancelled) | 2026-10-05 00:20:07 | 20261005-001914-chrono-2FYKPJ#2 | Lives Full and unlimited (2h gift) at session; replaced by lives-refill-after-gift |
| Shop: after the Daily Deal timer (06h12m at 2026-10-03 19:50) runs out, does the deal rotate? What does the Shop tab badge 1 count? | 2026-10-05 00:20:02 | 20261005-001914-chrono-2FYKPJ#2 | Deal rotated: timer now 01h40m, not a continuation of 06h12m. Badge 1 gone on this visit (not identified what it counted). |
| Lose a level on purpose and walk the Retry/out-of-moves flow (cancelled) | 2026-10-03 23:14:03 | review-20261003 | Duplicate of loss-oom (lose by running out of moves, fail screen, Retry and life cost) |
| Capture the level win screen: score, stars, rewards and what follows it (level 1 went straight from Sugar Crush to the level 2 popup) | 2026-10-03 23:13:14 | 20261003-225003-chrono-2FYKPJ#43 | Shot 81: 'Level completed' with crown, level badge and three stars (one filling), then map with 'Sweet!' tag (shot 82), then Level 4 popup (shot 83). Score, Sugar Crush and rewards not captured |
| Core level: Retry button flow, restart and exit-app mid level | 2026-10-03 23:12:26 | 20261003-230937-chrono-2FYKPJ#12 | Restart: none in-level; exit-app costs a life; Retry flow needs a loss, set as retry-flow task |
| Study Events tab: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:11:02 | 20261003-230937-chrono-2FYKPJ#6 | Events tab shows only 'Sweet events coming soon!' on a curtain stage; no tabs or events at level 4 |
| Study Friends list: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:11:02 | 20261003-230937-chrono-2FYKPJ#6 | Social tab: Team (locked, level 20), Invites (empty), Friends with List (empty, Find friends) and Add (Invite, Facebook, suggested players with Add). Add/Invite/Facebook not pressed (social) |
| Study Level (core match-3): open it, walk its screens and tabs, verify its cases | 2026-10-03 23:09:04 | 20261003-225003-chrono-2FYKPJ#50 | Played levels 2-3 won, 4 quit via gear. The win flow does have a 'Level completed' screen (20261003-225003-chrono-2FYKPJ#43, shot 81): it falls between frames 8 s apart; quit costs a life. Left: out-of-moves loss, Retry, exit-app |
| Study Colour bomb: open it, walk its screens and tabs, verify its cases | 2026-10-03 23:07:49 | 20261003-225003-chrono-2FYKPJ#46 | Made a 5-line (L4 top row), bomb swapped with green cleared all greens plus adjacent meringue in one move; bomb+striped/wrapped combos not tested |
| Study Account and Retrieve My Progress: open it, walk its screens and tabs, verify its cases | 2026-10-03 22:51:49 | 20261003-225003-chrono-2FYKPJ#9 | Walked Account & Help and King My Account panel, login and signup forms observed without credentials. Panel frames cannot be marked. |
| Map the game: play until the main menu and every entry point is visible; list each entry point as open (a study goal), locked with its unlock condition (an unlock goal) or unclear (an experiment) | 2026-10-03 19:49:18 | 20261003-194350-chrono-2FYKPJ#23 | Map appears after level 1 (win then level 2 popup). 5 tabs: map, events (coming soon), social (Candy Teams locked to 20), pins (collection empty, awards coming soon), shop (paid). Top bar: mail (inert), lives popup, profile inventory (boosters locked), gold bars (inert on shop), settings. |
