---
game: com.maroieqrwlk.unpin
title: "Bonus levels (character node)"
type: feature
feature: bonus-levels
version_seen: 241.5.2
verified_at: 2026-10-06
sources: [20261003-203702-chrono-2FYKPJ, 20261003-211035-chrono-2FYKPJ, 20261005-151039-chrono-2FYKPJ, 20261006-012240-chrono-2FYKPJ]
---

# Bonus levels (character node)

A node on the map with a cartoon character's portrait, set beside the level path and joined to it by a short
line; the game's map tutorial calls these bonus levels [^s1]. At level 10 the next such node sat between
levels 16 and 17 and could not be opened yet [^s2]. On version 241.5.2 that node turned out to be the face
of the Sketchman IQ Test mode: it left the map when the mode unlocked after the level 15 win, and no bonus
level was offered [^s3] [^s4]. The next node, a grandmother's portrait between levels 21 and 22, went the same way when the Challenge mode unlocked with the level 20 win [^s5] [^s6]. No bonus level was played, so what one is like is not known.

## Why it appeared

The map tutorial after the level 3 win: a tooltip "Discover bonus levels as you go" at a character node
between levels 8 and 9 [^s1]. Later a node was seen between levels 16 and 17 [^s2].

## Where to find it

The map: a round portrait of an angry stick-figure character at the left of the level path, linked to the
path between level 16 and level 17 [^s2]. At level 10 a tap on it did nothing [^s2]. Inferred from the
node's place: it opens once the path reaches it, after level 16; not verified.

![The map at level 10: the character node left of the path between levels 16 and 17](../img/20261003-bonus-levels-entry-cdb6e924.webp) [^s2]
*The map at level 10: the character portrait left of the path, between levels 16 and 17; a tap on it did nothing*

## What it looks like

<!-- no-screen: the node could not be opened at level 10; no bonus level was played -->

Not seen: the node was not reachable [^s2].

## How it works

Version 241.5.1.

- Nodes seen: between levels 8 and 9 (the tutorial) [^s1], between levels 16 and 17 [^s2].
- Before the path reaches it the node gives no reaction to a tap and no tooltip [^s2].
- Whether the node between levels 8 and 9 was played, skipped or left behind on the way to level 10 is not
  known.

Version 241.5.2.

- The node between levels 16 and 17 shows the angry stick figure of the [Sketchman IQ Test](mode-iq-test.md)
  card. It was on the map at level 15 and gone after the level 15 win, when the mode unlocked; the
  Jump to Level button took its place beside level 17 [^s3] [^s4].
- The next character node, a grandmother's portrait, is linked to the path between levels 21 and 22, where the
  map's "Unlock New Mode" labels sit; Challenge unlocks at level 21 and Merge Balls at level 22 [^s3] [^s4].
  Inferred: character nodes mark mode unlocks, not bonus levels; not verified, and what the tutorial's
  "bonus levels" are stays open.
- The grandmother's node was on the map at level 20 and gone after the level 20 win, when the Challenge mode
  unlocked (the jar showed NEW); no bonus level was offered [^s5] [^s6] [^s7]. The next character
  node is an angry stick figure linked to the path between levels 26 and 27 [^s6]. Inferred from two nodes
  out of two: character nodes are mode markers; not verified for the next one.

## Outcomes

| Outcome | As the base or what differs | Frame |
|---|---|---|
| win <!-- case:under-win --> | not verified: no bonus level played | — |
| restart <!-- case:under-restart --> | not verified | — |
| quit <!-- case:under-quit --> | not verified | — |
| exit app <!-- case:under-exit-app --> | not verified | — |
| balls fell out <!-- case:under-balls-out --> | not verified: the "Balls fell out of the level!" loss was seen so far only on level 11, an ordinary level (see [Pin-pull level](core-level.md#level-failed)) | — |

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Tapping the character node before reaching it (progress L10): no reaction, no tooltip <!-- case:tap-before-reached --> | Tapped the node between levels 16 and 17 at level 10 | ✅ Nothing happened | [^s2] |
| The character node between L16 and L17 was the Sketchman face of the Sketchman IQ Test mode: it vanished from the map when the mode unlocked after the L15 win, no bonus level was offered <!-- case:sketchman-node-was-mode --> | Won level 15, back to the map | ✅ The node gone, the mode unlocked, no bonus level | [^s4] |
| The grandmother's node between levels 21 and 22 <!-- case:granny-node-was-mode --> | Won level 20, back to the map | ✅ The node gone when Challenge unlocked, no bonus level offered; the next node, a stick figure, between levels 26 and 27 | [^s6] |
| Why it appeared <!-- case:chk-appeared --> | Won level 3 | ✅ The map tutorial's tooltip | [^s1] |
| Where to find it <!-- case:chk-entry --> | Tapped the node at level 10 | not verified: the node is on the map, but it did not open |  |
| What it looks like <!-- case:chk-screen --> | — | not verified: not opened |  |
| How it is announced <!-- case:chk-announce --> | — | not verified: the tutorial tooltip only; no popup when the node is reached |  |
| What differs in play from the base level <!-- case:chk-differs --> | — | not verified |  |
| Its win <!-- case:chk-win --> | — | not verified |  |
| Each loss <!-- case:chk-loss --> | — | not verified |  |
| Retry and continue offers <!-- case:chk-retry --> | — | not verified |  |
| Where and how often it comes up <!-- case:chk-frequency --> | Looked at the map | not verified: nodes after levels 8 and 16 seen |  |

## Not verified

- Colours mixed (the Color Bucket fail) under a bonus level, if one has colour cups: as the base, or what differs <!-- case:under-colour-mix -->
- Where to find it: what opens the node (reaching it on the path, after level 16) <!-- case:chk-entry -->
- What it looks like: the bonus level's screen <!-- case:chk-screen -->
- How it is announced when the path reaches the node <!-- case:chk-announce -->
- What differs in play from the base level: the board, the rules, the limits, stages, a timer <!-- case:chk-differs -->
- Its win: the win screen and the reward, against the base level's <!-- case:chk-win -->
- Each loss: its fail screen and what the loss costs <!-- case:chk-loss -->
- Retry and continue offers after a loss and their price <!-- case:chk-retry -->
- Where and how often it comes up beyond the nodes after levels 8 and 16; whether any character node is a bonus level and not a mode marker <!-- case:chk-frequency -->
- Win screen under Bonus levels: as the base, or what differs <!-- case:under-win -->
- Restart under Bonus levels: as the base, or what differs <!-- case:under-restart -->
- Quit under Bonus levels: as the base, or what differs <!-- case:under-quit -->
- Exit the app under Bonus levels: as the base, or what differs <!-- case:under-exit-app -->
- Balls fell out under Bonus levels: as the base, or what differs <!-- case:under-balls-out -->

[^s1]: session 20261003-203702-chrono-2FYKPJ, step 6 — [video at 1:57](https://youtu.be/cirqlD7KGWI?t=117)
[^s2]: session 20261003-211035-chrono-2FYKPJ, step 4 — [video at 1:22](https://youtu.be/Mpfk4cqdltQ?t=82)
[^s3]: session 20261005-151039-chrono-2FYKPJ, step 0 — [video at 0:00](https://youtu.be/r5lFTdFC8_s?t=0)
[^s4]: session 20261005-151039-chrono-2FYKPJ, step 17 — [video at 5:51](https://youtu.be/r5lFTdFC8_s?t=351)

[^s5]: session 20261006-012240-chrono-2FYKPJ, step 0 — [video at 0:00](https://youtu.be/jf_j5LiHuRs?t=0)
[^s6]: session 20261006-012240-chrono-2FYKPJ, step 18 — [video at 10:17](https://youtu.be/jf_j5LiHuRs?t=617)
[^s7]: session 20261006-012240-chrono-2FYKPJ, step 19 — [video at 11:16](https://youtu.be/jf_j5LiHuRs?t=676)
