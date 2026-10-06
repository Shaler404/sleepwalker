---
game: com.vitastudio.mahjong
title: "Leaf counter (home)"
type: feature
feature: leaves
version_seen: 3.40.1
verified_at: 2026-10-05
sources: [20261005-002327-chrono-2FYKPJ, 20261005-073409-chrono-2FYKPJ]
---

# Leaf counter (home)

A leaf icon with a count ("x0") on the home screen's top bar, right of the avatar [^s1]. Tapped, it
opens [Daily Victories](daily-victories.md), whose emblem is the same leaf and whose streak was 0 day
when the counter read "x0" [^s3]. Inferred from that, the counter shows the Daily Victories day streak
rather than a currency to spend; nothing in the game was seen to spend or award leaves.

## Why it appeared

On the home top bar next to the avatar at the first home arrival, on the Level 1 home before Sync Data
and on the Level 19 home after it, always "x0" [^s1].

## Where to find it

Home screen > top bar, right of the avatar [^s2].

![The home screen at level 19: the leaf counter "x0" right of the avatar, top left](../img/20261005-daily-victories-entry-d4fc1f86.webp) [^s2]
*The leaf counter "x0" right of the avatar on the home top bar*

## What it looks like

A dark wooden plate with a leaf and "x0" [^s2]. The screen it opens:

![Daily Victories, opened from the leaf counter: the same leaf as an emblem and "0 day streak!", the 10/2026 calendar and chests at 10, 20 and 30](../img/20261005-daily-victories-screen-d5d6464b.webp) [^s3]
*Daily Victories, opened from the leaf counter: the leaf emblem and the day streak*

## How it works

Version 3.40.1.

- "x0" on the Level 1 home and on the Level 19 home [^s1].
- The tap opens Daily Victories at "0 day streak!" [^s3].
- No price, sink or reward in leaves was seen in the game so far; no level was won in the sessions.

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Home top bar right of the avatar: leaf icon "x0" at Level 1 (before Sync) and at Level 19 (after) <!-- case:chk-balance --> | Arrived on home | ✅ | [^s1] |
| Why it appeared: the trigger that brought it up (the first launch, a level won, a threshold, a timer, a loss): a fact with its frame, or a hypothesis to test <!-- case:chk-appeared --> | Arrived on home | ✅ There from the first home arrival | [^s1] |
| Where to find it: the screen and the button that open it <!-- case:chk-entry --> | Looked at the home top bar | Seen: right of the avatar (frame above); the case is still open in the map | [^s2] |
| What it looks like: its screen <!-- case:chk-screen --> | Tapped the counter | Seen: it opens Daily Victories (frame above); the case is still open in the map | [^s3] |
| What it does: the effect of one unit or one use <!-- case:chk-effect --> | Tapped the counter | Opens Daily Victories; no use of a leaf seen | [^s3] |
| Sources: every way to get it and how much <!-- case:chk-sources --> | — | not verified |  |
| Sinks: every way it is spent and the price <!-- case:chk-sinks --> | — | not verified |  |
| At zero: what happens and the offers to refill it <!-- case:chk-empty --> | — | not verified |  |
| Refill timer, if any <!-- case:chk-refill --> | — | not verified |  |

## Not verified

- Where to find it: seen and shown above, not yet closed in the map <!-- case:chk-entry -->
- What it looks like: seen and shown above, not yet closed in the map <!-- case:chk-screen -->
- What it does: whether the number is only the day streak or also a balance <!-- case:chk-effect -->
- Sources: what raises it (a won day, inferred from Daily Victories) <!-- case:chk-sources -->
- Sinks: nothing seen that costs leaves <!-- case:chk-sinks -->
- At zero: it was at zero; no offer or effect seen <!-- case:chk-empty -->
- Refill timer: none seen <!-- case:chk-refill -->

[^s1]: session 20261005-002327-chrono-2FYKPJ, step 1 — [video at 0:41](https://youtu.be/2aQPmh7YksQ?t=41)
[^s2]: session 20261005-073409-chrono-2FYKPJ, step 1 — [video at 0:40](https://youtu.be/vgVMznU7XG0?t=40)
[^s3]: session 20261005-073409-chrono-2FYKPJ, step 2 — [video at 0:53](https://youtu.be/vgVMznU7XG0?t=53)
