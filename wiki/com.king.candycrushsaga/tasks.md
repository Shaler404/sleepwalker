# Tasks: Candy Crush Saga

Status: **▶️ active** — ready now: 12; update the game on the phone in Google Play to recheck on the new version: installed 1.335.1.2, Google Play 1.337.0.2

Mode: **goals** — work through the session goals in order; play levels only as far as an unlock or experiment goal needs; register anything new you notice as a feature or a goal, do not pursue it now

Progress reached: **level 7 open (FTUE story path, no map yet)** · last new feature found at: **first Play on a fresh install**

Goals: map 1, study 6, unlock 2, experiment 3 · maps: none yet

Gameplay (target: a level within 5 min; how to play: [agent/playbook.md](agent/playbook.md)): **core-match** — mastered, manual, levels won 6, typical 4.3 min

Google Play version: **1.337.0.2** (checked 2026-10-01 20:09:25) · analyzed version: **1.335.1.2** · FTUE from a fresh install: **2026-10-01**

Generated from [`research.yaml`](research.yaml) by `sw.py render`; do not edit by hand. Feature map: [features.md](features.md).

## Ready now

| Task | Kind | Feature | Source | Note |
|---|---|---|---|---|
| Map the game: play until the main menu and every entry point is visible; list each entry point as open (a study goal), locked with its unlock condition (an unlock goal) or unclear (an experiment) | map |  | external | the first map of the game |
| Study Settings: General and Accessibility tabs, More Audio, Features, Account & Help | study | [Settings](features/settings.md) | knowledge gap |  |
| Study boosters once unlocked: which level unlocks each of the 5 in-level slots | unlock | [Pre-level and in-level boosters](features/boosters.md) | knowledge gap | Lollipop Hammer unlocked on arrival at level 7 (x3) [s:20261001-232021-chrono-2FYKPJ#53]; the other 4 slots still locked at level 7 |
| Study Level play (match-3 board): open it, walk its screens and tabs, verify its cases | study | [Level play (match-3 board)](features/level-play.md) | external |  |
| Study FTUE story path (forest clue): open it, walk its screens and tabs, verify its cases | study | [FTUE story path (forest clue)](features/ftue-story.md) | external |  |
| Study Golden crown (first-try win): open it, walk its screens and tabs, verify its cases | study | [Golden crown (first-try win)](features/golden-crown.md) | external |  |
| Lives: find when lives stop showing 1/infinity after the FTUE and how a lost level, refill timer and the lives pop-up work | experiment |  | knowledge gap | Correction: the "N / heart-infinity" at the top left of the level HUD shows the level number (2 on level 2, 5 on level 5, 7 on level 7), not a life count; lives are unlimited through level 7 [s:20261001-202316-chrono-2FYKPJ#12] [s:20261001-232021-chrono-2FYKPJ#33] [s:20261001-232021-chrono-2FYKPJ#53] |
| Play levels 7+ on the FTUE path until the saga map appears; then redo scout-1 on the map | unlock | [FTUE story path (forest clue)](features/ftue-story.md) | knowledge gap | Levels 1-6 done; chapter 2/5 follows Dachs, no map yet; level 7 has meringue over jelly; target_value 12 is a guess (no frame says when the map opens) |
| Study Lollipop Hammer booster (unlocked at level 7, count 3): use it on a level, record its effect | study | [Pre-level and in-level boosters](features/boosters.md) | knowledge gap |  |
| Golden crown: after the saga map appears, find whether first-try wins show a crown on map nodes or the profile, or confirm the feature is absent | experiment | [Golden crown (first-try win)](features/golden-crown.md) | knowledge gap |  |
| FTUE story: find where the fancy key from chapter 1 is used (chapter 2 'follow Dachs' 0/5) and what the chapter reward is | experiment | [FTUE story path (forest clue)](features/ftue-story.md) | knowledge gap |  |
| Consent: open SDK List and Manage Preferences on the personalised ads page, see what switching the toggle off and Confirm changes | study | [Terms & privacy consent](features/consent.md) | knowledge gap | Seen but not opened: SDK List, Manage Preferences (toggle on by default) [s:20261001-232021-chrono-2FYKPJ#4] |

## Waiting

None.

## Needs a human

The agent cannot do these tasks until it is given a suitable phone.

| Task | What to provide | Feature |
|---|---|---|
| Recheck the features on version 1.337.0.2 | update the game on the phone in Google Play to recheck on the new version: installed 1.335.1.2, Google Play 1.337.0.2 |  |
| Fresh install: record a game-side frame of the notification permission prompt after the first Play and check whether Allow changes anything in the game | a phone with a fresh install: uninstall the game and install it again (or clear its data), then connect the phone | Notification permission prompt |

## Done

| Task | Closed | By | Note |
|---|---|---|---|
| Study Title screen: open it, walk its screens and tabs, verify its cases | 2026-10-02 12:00:00 | 20261001-232021-chrono-2FYKPJ#13 | All three title buttons walked: Play [s:20261001-202316-chrono-2FYKPJ#4], gear to Settings [s:20261001-202316-chrono-2FYKPJ#2], Retrieve My Progress [s:20261001-232021-chrono-2FYKPJ#13]; page features/title-screen.md |
| Golden crown: win a level on the first try and see where the crown shows (map, profile) | 2026-10-01 23:45:40 | 20261001-232021-chrono-2FYKPJ#32 | Level 4 won on the first try (17 moves, no loss) but no crown appeared: the win screen shows only 'Level complete' and the path node gets the usual orange check (shot 56); levels 5 and 6 also first-try wins with plain checks. No crown during the FTUE; recheck on the saga map in crown-on-map |
| Play the FTUE on from level 4 until the saga map/main menu appears, then finish the scout (cancelled) | 2026-10-01 23:45:40 | 20261001-232021-chrono-2FYKPJ#53 | duplicate of ftue-map-2 (same target: play the FTUE path until the saga map appears, then finish scout-1); ftue-map-2 carries the current state (levels 1-6 done) |
| Study Terms of Use consent: open it, walk its screens and tabs, verify its cases | 2026-10-01 23:23:10 | 20261001-232021-chrono-2FYKPJ#13 | Terms of Use link (Chrome page) and Privacy and security/personalised ads page walked; first-launch consent was seen earlier. |
| Study Retrieve My Progress (account sign-in): open it, walk its screens and tabs, verify its cases | 2026-10-01 23:23:09 | 20261001-232021-chrono-2FYKPJ#13 | Walked panel carousel, login form, Terms link, privacy page; nothing entered. Marks refused: panel frames are app Panel. |
