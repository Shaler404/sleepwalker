---
game: com.block.juggle
title: "Adventure diamond-collection levels"
type: feature
feature: adv-diamonds
version_seen: 10.8.1
verified_at: 2026-10-04
sources: [20261003-235233-chrono-2FYKPJ]
---

# Adventure diamond-collection levels

Adventure levels whose goal is to collect gem tiles instead of reaching a target score. The board, the
tray and the drag are those of [Classic](classic.md); the level starts on a pre-built layout, some board
cells and some cells of the tray pieces carry a gem, and clearing a row or column that holds a gem
collects it. The header counts down the gems left of each kind; the level is won when every count
reaches zero. Seen on Adventure levels 2, 3 and 4 in version 10.8.1 [^s1] [^s3] [^s7].

## Why it appeared

Adventure level 2, the level after the first win: the header shows a diamond with a count (60) instead
of a score bar, with diamond tiles on the board and in tray pieces [^s1].

## Where to find it

Home menu > Adventure > the green "Level N" button at the bottom of the Adventure map. There is no
separate entry: the gem goal belongs to the level, and the current level's cell on the map looks like
any other [^s2].

![The Adventure map with cell 2 current; the green Level 2 button starts the diamond level](../img/20261003-adv-diamonds-entry-f887d068.webp) [^s2]
*The green Level 2 button at the bottom of the Adventure map; cell 2 carries no special icon*

## What it looks like

Level 2: back arrow, gear, and in place of the score bar a blue diamond with the count left (60). The
pre-built layout is a tree of green blocks with diamond tiles in it; two of the three tray pieces carry
diamond cells too [^s1].

![Adventure level 2: the diamond goal 60 in the header, diamond tiles on the tree-shaped layout and on tray pieces](../img/20261003-adventure-tab-diamond-level-ce4b3534.webp) [^s1]

Level 3 has two goals side by side, 56 red gems and 54 orange gems, on a frame-shaped layout of yellow
blocks; tray pieces include diagonal shapes with gem cells [^s3]. Level 4 has three: 22 blue diamonds,
20 orange gems and 20 yellow stars [^s7].

![Adventure level 3: two goals, 56 red and 54 orange gems; gem tiles in the frame-shaped layout and on the tray pieces](../img/20261003-adv-diamonds-screen-b0b94343.webp) [^s3]

When a goal is met its count turns into a green check [^s4].

![All 60 diamonds collected: the counter has turned into a green check and the board has cleared](../img/20261003-adv-diamonds-result-ae2b8184.webp) [^s4]

## How it works

Version 10.8.1.

- A gem is collected when the row or column holding its tile is cleared: the gem flies to the header
  and the count drops by one; the clear also shows "+10" [^s9].
- Gems come both on the pre-built board and on cells of new tray pieces [^s1].
- No move limit, timer, lives or boosters were seen [^s1] [^s8].
- Goals per level so far: L2 60 diamonds; L3 56 red + 54 orange gems; L4 22 blue diamonds + 20 orange
  gems + 20 yellow stars [^s1] [^s3] [^s7].

![A row with a diamond tile is cleared: the diamond flies to the header and the count goes from 60 to 59](../clips/20261003-diamond-line-clear.webp) [^s9]
*Clip 9.8 s · [original on YouTube from 5:30](https://youtu.be/RE70Idi_jrA?t=330)*

## Outcomes

The base level is the 8x8 board of Classic.

| Outcome | As the base or what differs | Frame |
|---|---|---|
| No Space Left: no tray piece fits <!-- case:under-no-space-left --> | Differs: the board dims, the gems still needed are shown (56), "You Can Do It!" and a green Retry button instead of "Can you Top that?" and Play; the Consecutive Victories panel drops in at x0. No ad came after this loss, no revive or price [^s5] | ![The level 2 loss: "You Can Do It!", 56 diamonds left, Retry, Consecutive Victories x0](../img/20261003-adv-diamonds-outcome-no-space-left-d3939392.webp) |
| Win <!-- case:under-win --> | Differs: Classic has no win. Here the counters turn into checks, then the win screen: the Consecutive Victories panel, the trophy grid with one more cell lit and a Next Level button; no coins or other reward. After the level 2 win an interstitial ad came first [^s6] | ![The level 2 win screen: Consecutive Victories x1, two trophy cells lit, Next Level](../img/20261003-adv-diamonds-outcome-win-939393c3.webp) |
| Quit: gear > Home <!-- case:under-quit --> | Differs from Classic's Back key only in the route: the gear's Home button (level 4) goes to the home menu at once with no confirmation and no cost; the level stays the current one [^s7] | ![The home menu after quitting level 4](../img/20261003-adv-diamonds-outcome-quit-93112c2c.webp) |
| Restart: gear > Replay <!-- case:under-restart --> | not verified: Replay is in the level's gear menu but was not tapped | — |
| Leaving the app <!-- case:under-exit-app --> | not verified | — |

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared <!-- case:chk-appeared --> | Won Adventure level 1, opened level 2 | ✅ The level 2 header shows a diamond counter (60) instead of a score bar | [^s1] |
| Where to find it <!-- case:chk-entry --> | Home menu > Adventure > Level N | ✅ No separate entry: the gem goal belongs to the level (2, 3, 4 so far) | [^s1] |
| What it looks like <!-- case:chk-screen --> | Opened levels 2 and 3 | ✅ Back arrow, gear, a counter per gem kind in place of the score bar; gem tiles on the board and on tray pieces | [^s1] |
| How it is announced <!-- case:chk-announce --> | Looked at the map and opened the level | ✅ No announcement: the map cell looks like any other, Level N opens the board straight away; the goal is only in the header | [^s1] |
| What differs from the base level <!-- case:chk-differs --> | Played levels 2 and 3 | ✅ Same board, tray and drag; the goal is to collect gems by clearing their lines; a pre-built layout; several gem kinds from level 3; no move limit or timer | [^s3] |
| Its win <!-- case:chk-win --> | Won levels 2 and 3 | ✅ The counters turn into checks, the board clears; win screen as on the score level: Consecutive Victories, a trophy cell lit, Next Level; no reward currency | [^s6] |
| A loss <!-- case:chk-loss --> | Lost level 2 on purpose | ✅ No Space Left: board dims, the diamonds left, "You Can Do It!", Retry; costs only the Adventure win streak (x1 to x0); the daily counter stayed | [^s5] |
| Retry and continue offers <!-- case:chk-retry --> | Back arrow, then Adventure > Level 2 | ✅ No continue or revive offer, no price; the level restarts with the same pre-built board and goal. The loss screen's Retry button was not tapped | [^s8] |
| Where and how often it comes up <!-- case:chk-frequency --> | — | not verified: levels 2, 3 and 4 are gem levels, level 1 a score level; later levels not opened |  |

## Not verified

- Which levels are gem levels after level 4, and whether score levels come back <!-- case:chk-frequency -->
- Settings gear > Replay in a gem level: as the base, or what differs <!-- case:under-restart -->
- Leaving the app in a gem level and coming back <!-- case:under-exit-app -->
- What the Retry button on the loss screen does (the level was restarted from the map instead)
- How many points or gems a single clear is worth when several gem tiles are in one line

[^s1]: session 20261003-235233-chrono-2FYKPJ, step 25 — [video at 4:57](https://youtu.be/RE70Idi_jrA?t=297)
[^s2]: session 20261003-235233-chrono-2FYKPJ, step 31 — [video at 6:32](https://youtu.be/RE70Idi_jrA?t=392)
[^s3]: session 20261003-235233-chrono-2FYKPJ, step 48 — [video at 10:21](https://youtu.be/RE70Idi_jrA?t=621)
[^s4]: session 20261003-235233-chrono-2FYKPJ, step 43 — [video at 8:34](https://youtu.be/RE70Idi_jrA?t=514)
[^s5]: session 20261003-235233-chrono-2FYKPJ, step 29 — [video at 5:47](https://youtu.be/RE70Idi_jrA?t=347)
[^s6]: session 20261003-235233-chrono-2FYKPJ, step 45 — [video at 9:41](https://youtu.be/RE70Idi_jrA?t=581)
[^s7]: session 20261003-235233-chrono-2FYKPJ, step 64 — [video at 13:28](https://youtu.be/RE70Idi_jrA?t=808)
[^s8]: session 20261003-235233-chrono-2FYKPJ, step 32 — [video at 6:39](https://youtu.be/RE70Idi_jrA?t=399)
[^s9]: session 20261003-235233-chrono-2FYKPJ, step 27 — [video at 5:32](https://youtu.be/RE70Idi_jrA?t=332)
