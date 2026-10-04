---
game: com.oakever.meowdoku
title: "Mouse booster"
type: feature
feature: booster-mouse
version_seen: 1.19.1
verified_at: 2026-10-03
sources: [20261003-200440-chrono-2FYKPJ, 20261003-201915-chrono-2FYKPJ]
---

# Mouse booster

The last of the three boosters under the board of a [main level](level.md): a mouse hops over the board and
crosses out empty cells that cannot hold a cat. It shows a count badge; at zero the badge turns into a green
video icon [^s3].

## Why it appeared

On the level HUD at level 127, count 1 [^s1].

## Where to find it

Inside a [main level](level.md): the mouse button, last (right) of the three round boosters under the board,
with a red count badge [^s2].

![Level 127 screen: the mouse button, last of the three boosters under the board, count 1](../img/20261003-booster-mouse-entry-fa23b474.webp) [^s2]
*Level 127: the mouse button, right of the three boosters under the board, count 1*

## What it looks like

<!-- no-screen: the booster has no screen of its own; one tap starts the mouse on the board -->

The booster has no screen of its own: one tap set a mouse on the board, with no confirmation [^s3].

![The mouse hops over three cells of the Level 128 board; each cell it leaves gets a white cross](../clips/20261003-mouse-booster-crosses-out.webp) [^s3]
*Clip 3 s · [original on YouTube from 4:56](https://youtu.be/ffhYgQE4LvU?t=296)*

### Result

![Level 128 while the mouse booster runs: the mouse on a cell in the lower right, a new cross on the third row, the mouse button's badge a green video icon](../img/20261003-booster-mouse-result-fab1c1b1.webp) [^s3]
*The mouse on a teal cell in the lower right; the mouse button's badge is now a green video icon (the banner ad at the bottom is an install ad)*

## How it works

- One use crossed out three empty cells, one after another: third row last column, seventh row ninth column,
  ninth row second column [^s3]. All three are cells without a cat in the solved board [^s5]. Inferred: the
  mouse only crosses out cells that cannot hold a cat; how many it crosses per use was seen once only.
- No score or fish change (576 and two fish before and after) [^s3].
- Count: 1 before, a green video icon after the one use [^s3]. Inferred: at zero more can be had for a
  rewarded video; not tapped.

Version 1.19.1.

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| One use adds X marks on cells that cannot hold a cat (frame shows new X at r2c9, r6c8, r8c1); no score or fish change <!-- case:chk-effect --> | Tapped once on Level 128 | ✅ | [^s3] |
| Count badge on the mouse button in the level HUD; 1 at start <!-- case:chk-balance --> | Badge read before and after | ✅ | [^s3] |
| At 0 the badge becomes a green video icon <!-- case:chk-empty --> | Badge seen after the only unit was used | ✅ | [^s3] |
| Why it appeared: the trigger that brought it up (the first launch, a level won, a threshold, a timer, a loss): a fact with its frame, or a hypothesis to test <!-- case:chk-appeared --> | On the level HUD from the first level seen | ✅ | [^s1] |
| Where to find it: the screen and the button that open it (mark --as entry --at X,Y) <!-- case:chk-entry --> | The mouse button under the board tapped | ✅ | [^s2] |
| What it looks like: its screen (mark --as screen) <!-- case:chk-screen --> | No screen: one tap started the mouse | not verified | [^s3] |
| Sources: every way to get it (a level win, a video, a daily reward, a pack) and how much <!-- case:chk-sources --> | Count unchanged by two wins; the video icon not tapped | not verified | [^s4] |
| Sinks: every way it is spent and the price <!-- case:chk-sinks --> | Spent by one tap in a level | not verified | [^s3] |
| Refill timer, if any: how long one unit takes and the maximum <!-- case:chk-refill --> | No timer seen | not verified |  |

## Not verified

- What it looks like: whether the booster has any description (a long press, the first use) <!-- case:chk-screen -->
- Sources: what the video icon gives, and whether wins, the Daily Streak gift or the event rewards pay mice <!-- case:chk-sources -->
- Sinks: any spend other than a tap in a level <!-- case:chk-sinks -->
- Refill timer: whether the count refills by itself over time <!-- case:chk-refill -->

[^s1]: session 20261003-200440-chrono-2FYKPJ, step 3 — [video at 1:05](https://youtu.be/Pqx4QY-FpBA?t=65)
[^s2]: session 20261003-201915-chrono-2FYKPJ, step 3 — [video at 1:28](https://youtu.be/ffhYgQE4LvU?t=88)
[^s3]: session 20261003-201915-chrono-2FYKPJ, step 16 — [video at 4:58](https://youtu.be/ffhYgQE4LvU?t=298)
[^s4]: session 20261003-201915-chrono-2FYKPJ, step 18 — [video at 5:47](https://youtu.be/ffhYgQE4LvU?t=347)
[^s5]: session 20261003-201915-chrono-2FYKPJ, step 17 — [video at 5:31](https://youtu.be/ffhYgQE4LvU?t=331)
