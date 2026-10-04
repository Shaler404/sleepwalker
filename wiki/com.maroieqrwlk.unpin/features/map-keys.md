---
game: com.maroieqrwlk.unpin
title: "Keys on the map (key nodes, 3-key gate at L11-12)"
type: feature
feature: map-keys
version_seen: 241.5.1
verified_at: 2026-10-03
sources: [20261003-203702-chrono-2FYKPJ]
---

# Keys on the map (key nodes, 3-key gate at L11-12)

Keys are collected on the map: some level nodes have an orange key badge beside them, and three key slots
near the top of the map fill as these levels are won. Winning level 9, the first key level, filled the
first slot [^s1] [^s2]. The slots sit at a node labelled "Unlock New Mode" (level 17) [^s1]; what the new mode
is was not seen.

## Why it appeared

Key node on level 9: winning L9 filled 1 of the 3 key slots above L17 ('Unlock New Mode') [^s1].

## Where to find it

The map: the round orange key badge beside level 9, and the row of three keyhole slots in a dark box under
the top bar [^s2]. On the first map a tutorial tooltip points at a key node: "Get unique rewards buried in
the levels!" [^s3].

![Key slots 1/3 filled (gold), 'Unlock New Mode' at L17 key node; chest timer ended -> OPEN; new jar icon with ! top left; Pull Fest 13 pins rank 868](../img/20261003-map-keys-entry-cdb2ec35.webp) [^s1]
*The map after the level 9 win: the first of three key slots gold; the key node at level 17 with "Unlock New Mode"*

## What it looks like

![Map before L4: the orange key node on level 9 and the three empty key slots near the top](../img/20261003-map-keys-screen-8cb2cb37.webp) [^s2]
*The map before level 4: the orange key node beside level 9; three empty key slots at the top*

Before level 9 the three slots are grey outlines of keys [^s2]. After the level 9 win the first slot is a
gold key [^s1]. There is no key counter elsewhere and no key screen [^s1].

## How it works

Version 241.5.1.

| Moment | Key slots |
|---|---|
| Map after the level 3 win | 0 of 3 [^s2] |
| Map after the level 9 win (key node level) | 1 of 3 [^s1] |

- The slots are at the level 17 node, labelled "Unlock New Mode" [^s1].
- Inferred: each level with a key badge gives one key when won, and three keys open the new mode at level 17;
  only the first key was seen.

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared <!-- case:chk-appeared --> | Won level 9 | ✅ The first slot filled | [^s1] |
| Where to find it <!-- case:chk-entry --> | Looked at the map | not verified: the slots and key nodes are seen, not tapped | [^s2] |
| What it looks like <!-- case:chk-screen --> | — | not verified: no key screen seen |  |
| What it does <!-- case:chk-effect --> | — | not verified: the new mode is not open yet |  |
| The balance <!-- case:chk-balance --> | Won level 9 | not verified: 1 of 3 in the slots | [^s1] |
| Sources <!-- case:chk-sources --> | Won level 9 | not verified: one key from the level 9 key node | [^s1] |
| Sinks <!-- case:chk-sinks --> | — | not verified: inferred to be the level 17 gate |  |
| At zero <!-- case:chk-empty --> | — | not verified |  |
| Refill timer <!-- case:chk-refill --> | — | not verified |  |

## Not verified

- Where to find it: whether tapping the slots or a key node opens anything <!-- case:chk-entry -->
- What it looks like: a key screen, if any <!-- case:chk-screen -->
- What it does: what "Unlock New Mode" opens at three keys <!-- case:chk-effect -->
- The balance: where the key count shows besides the slots <!-- case:chk-balance -->
- Sources: which levels carry keys after level 9 <!-- case:chk-sources -->
- Sinks: whether the gate takes the keys <!-- case:chk-sinks -->
- At zero: what the gate shows with fewer than three keys <!-- case:chk-empty -->
- Refill timer: none expected (keys come from levels) <!-- case:chk-refill -->

[^s1]: session 20261003-203702-chrono-2FYKPJ, step 52 — [video at 20:59](https://youtu.be/cirqlD7KGWI?t=1259)
[^s2]: session 20261003-203702-chrono-2FYKPJ, step 7 — [video at 2:10](https://youtu.be/cirqlD7KGWI?t=130)
[^s3]: session 20261003-203702-chrono-2FYKPJ, step 6 — [video at 1:57](https://youtu.be/cirqlD7KGWI?t=117)
