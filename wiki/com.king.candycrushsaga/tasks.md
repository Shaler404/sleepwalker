# Tasks: Candy Crush Saga

Status: **▶️ active** — ready now: 31

Mode: **goals** — work through the session goals in order; play levels only as far as an unlock or experiment goal needs; register anything new you notice as a feature or a goal, do not pursue it now

Progress reached: **level 4 reached, on map** · last new feature found at: **level 4 reached, on map**

Goals: study 15, unlock 2, experiment 13 · maps: level 1 won, on map before level 2 — 11 new

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **core-match** — mastered, manual, levels won 3, typical 4.9 min

Google Play version: **1.337.0.2** (checked 2026-10-05 00:13:01) · analyzed version: **1.337.0.2** · FTUE from a fresh install: **never**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Unlock Candy Teams: level 20 | unlock | [Candy Teams](features/candy-teams.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Unlock Boosters (hand, lollipop hammer etc.): not shown, about level 3-10 | unlock | [Boosters (hand, lollipop hammer etc.)](features/boosters.md) | knowledge gap | the lock seen on screen (feature --locked) |
| Find what unlocks boosters: locks seen in level bottom bar and profile inventory, level not shown | experiment | [Boosters (hand, lollipop hammer etc.)](features/boosters.md) | knowledge gap |  |
| Find why Mailbox icon appeared: envelope icon in the top bar of the map from the start; tap did nothing (inbox empty or needs account) | experiment | [Mailbox icon](features/mailbox.md) | knowledge gap |  |
| Mailbox envelope tap does nothing: test again after a few levels or when it shows a badge | experiment | [Mailbox icon](features/mailbox.md) | knowledge gap |  |
| Study Pins collection: open it, walk its screens and tabs, verify its cases | study | [Pins collection](features/pins.md) | external |  |
| Study Shop: open it, walk its screens and tabs, verify its cases | study | [Shop](features/shop.md) | external |  |
| Study Lives: open it, walk its screens and tabs, verify its cases | study | [Lives](features/lives.md) | external |  |
| Study Profile and inventory: open it, walk its screens and tabs, verify its cases | study | [Profile and inventory](features/profile.md) | external |  |
| Study Settings: open it, walk its screens and tabs, verify its cases | study | [Settings](features/settings.md) | external |  |
| Study Mailbox icon: open it, walk its screens and tabs, verify its cases | study | [Mailbox icon](features/mailbox.md) | external |  |
| Study Level map: open it, walk its screens and tabs, verify its cases | study | [Level map](features/map.md) | external |  |
| Run each outcome once under Events tab: Order done, Gear > Settings > Quit level > confirm 'Play on' / 'Quit -1 heart'; shows Level failed with Score and Retry, X goes to map; life 5->4, Out of moves, Force-stop mid level, No Restart button in the in-level settings (sound, Audio, Save progress, Quit level); restart only by quit and replay from map popup | experiment | [Events tab](features/events-tab.md) | knowledge gap |  |
| Study Gold bars: open it, walk its screens and tabs, verify its cases | study | Gold bars | external |  |
| Study Striped candy: open it, walk its screens and tabs, verify its cases | study | Striped candy | external |  |
| Study Terms of Use consent: open it, walk its screens and tabs, verify its cases | study | Terms of Use consent | external |  |
| Study Notification permission prompt: open it, walk its screens and tabs, verify its cases | study | Notification permission prompt | external |  |
| Find what the 3 Select boosters slots in the level start popup do at 0 balance (free trial, gold bars, or locked) | experiment | [Boosters (hand, lollipop hammer etc.)](features/boosters.md) | knowledge gap |  |
| Look for typical features not seen yet: daily reward or login calendar, starter or limited-time offer popups, rewarded ads, piggy bank, season pass, language option | experiment |  | knowledge gap |  |
| Colour bomb combined with striped, wrapped and another colour bomb | experiment | [Colour bomb](features/color-bomb.md) | knowledge gap |  |
| Lose a level by running out of moves and record the fail screen, retry and life cost | experiment | [Level (core match-3)](features/core-level.md) | knowledge gap |  |
| Record the full win sequence: Sugar Crush with moves left, final stars, score and any reward on Level completed | experiment | [Level (core match-3)](features/core-level.md) | knowledge gap |  |
| Find why Fish candy appeared: made by a 2x2 square match; first seen on level 3 board (shot 80) | experiment | Fish candy | knowledge gap |  |
| Study Wrapped candy: make or meet it in a level, mark it, verify its cases | study | Wrapped candy | knowledge gap |  |
| Study Fish candy: make or meet it in a level, mark it, verify its cases | study | Fish candy | knowledge gap |  |
| Study Meringue blocker: make or meet it in a level, mark it, verify its cases | study | Meringue blocker | knowledge gap |  |
| Tap the mail and gold-bar icons from the Map tab (not the Shop tab) and record what opens | experiment | Gold bars | knowledge gap |  |
| Watch lives refill after the 2h unlimited gift ends (lose lives to 3, time per life, cap) | check | [Lives](features/lives.md) | from the game |  |
| Find why Sweet gift (launch gift) appeared: popup on the first launch after about 25 h away (last session 2026-10-03 23:09, this launch 2026-10-05 00:19): a daily or comeback gift; not seen at the earlier launches of 2026-10-03 | experiment | Sweet gift (launch gift) | knowledge gap |  |
| Find what the level 4 cap (colour-bomb icon) releases and when | experiment | Candy dispenser | knowledge gap |  |
| Study Sweet gift (launch gift): open it, walk its screens and tabs, verify its cases | study | Sweet gift (launch gift) | external |  |

## Waiting

| Task | Not before | Kind | Feature |
|---|---|---|---|
| Sweet gift: launch the next day and note whether the gift comes again, what it gives and at what hour (calendar or one-off) | 2026-10-06 00:30:00 | check | Sweet gift (launch gift) |

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

None.

## Done

| Task | Closed | By | Note |
|---|---|---|---|
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
