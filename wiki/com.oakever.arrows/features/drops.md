---
game: com.oakever.arrows
title: "Drops (mistake allowance in the level HUD)"
type: feature
feature: drops
version_seen: 1.33.0
verified_at: 2026-10-03
sources: [20261003-232108-chrono-2FYKPJ, 20261003-232357-chrono-2FYKPJ, 20261003-233532-chrono-2FYKPJ]
---

# Drops (mistake allowance in the level HUD)

Three blue water drops at the top left of every level, below the back arrow. A tap on an arrow that
cannot leave the board costs one drop. The drop greys out, and the win card counts the tap as a mistake
[^s2] [^s5] [^s4].

## Why it appeared

There are three blue drops at the top left of the level HUD on level 3, the first level opened on this
install [^s1]. They were on levels 4 and 5 (Hard) too [^s5] [^s6].

## Where to find it

In any level: the three drops at the top left, under the back arrow [^s2]. They are not a button: two
taps on them on level 5 opened nothing [^s8].

![Level 3: the three blue drops top left, under the back arrow](../img/20261003-drops-entry-a61f9f66.webp) [^s2]
*Level 3: three blue drops at the top left, all full*

## What it looks like

![Level 4 after a blocked tap: the third drop greyed out, the blocked arrow red](../img/20261003-drops-screen-b70e0e33.webp) [^s3]
*Level 4 after one blocked tap: two blue drops and a grey one; the arrow that was blocked is red*

Full drops are blue. A spent drop turns grey-beige and stays in its place, the rightmost first [^s3]. The
arrow that was tapped while blocked flashes red, stays on the board, and stays red afterwards [^s3] [^s5].

The drops take the colour of the level theme chosen in the [Theme picker](theme-picker.md): light blue
in the default cream theme, teal in Eye Comfort Mode, bright blue in Dark Mode [^s9] [^s10].

![A tap on the blocked top arrow: it turns red and the third drop greys out; then a free arrow slides off in green](../clips/20261003-level-blocked-tap-loses-drop.webp) [^s5]
*Clip 6.2 s · [original on YouTube from 2:25](https://youtu.be/x9mSZuHgO_4?t=145)*

## How it works

Version 1.33.0.

- Each level starts with three drops, Hard level 5 too [^s2] [^s6].
- A tap on the drops does nothing: no popup or explanation [^s8].
- One blocked tap costs one drop [^s5].
- The spent drop stayed grey to the end of level 4 [^s3], and the mistake shows on the win card [^s4]:

| Mistakes | Title | Accuracy | Source |
|---|---|---|---|
| 0 (level 3) | Flawless! | 100% | [^s7] |
| 1 (level 4) | Perfect! | 87% | [^s4] |

- Quitting with the back arrow with full drops cost nothing seen [^s1].
- Inferred: losing all three drops loses the level. Not verified.

## Outcomes

<!-- the map has no under-<outcome> cases for this feature yet -->
Whether running out of drops is a loss of the base [level](level.md), and what that loss costs, is not
verified (exp-drops).

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared <!-- case:chk-appeared --> | Opened level 3 | ✅ Three blue drops at the top left | [^s1] |
| Where to find it <!-- case:chk-entry --> | — | ✅ Not a button: shown at the top left of every level HUD | [^s1] |
| Its screen <!-- case:chk-screen --> | Made one blocked tap on level 4; tapped the drops twice on level 5 | ✅ Two blue drops and a grey one; the blocked arrow red. A tap on the drops opens nothing | [^s3] [^s8] |
| A blocked tap <!-- case:blocked-tap --> | Tapped an arrow with another in its way on level 4 | ✅ Costs one drop, the arrow flashes red; counted as a mistake on the win card (x1, accuracy 87%), the title drops from Flawless! to Perfect! | [^s5] [^s4] |
| The first level it shows on <!-- case:chk-first-level --> | — | not verified: present on level 3, the first level of this install; levels 1-2 not seen in these sessions | |
| What it does <!-- case:chk-rules --> | — | partly: a blocked tap costs one; what happens at zero not seen | [^s5] |
| How it interacts with other pieces <!-- case:chk-interactions --> | Switched the level theme | partly: the drops follow the theme colour; hints and Zen Mode not tried | [^s9] [^s10] |
| A way to lose <!-- case:chk-loss --> | — | not verified: no drop run-out reached | |

## Not verified

- The first level the drops show on, and whether the game introduces them <!-- case:chk-first-level -->
- What happens at zero drops <!-- case:chk-rules -->
- How drops interact with the hint bulb and with Zen Mode (only the theme colour was seen) <!-- case:chk-interactions -->
- Whether running out is a loss of the level, its screen and cost (exp-drops) <!-- case:chk-loss -->

[^s1]: session 20261003-232108-chrono-2FYKPJ, step 8 — [video at 1:09](https://youtu.be/KL7evNlX6oU?t=69)
[^s2]: session 20261003-232357-chrono-2FYKPJ, step 8 — [video at 1:15](https://youtu.be/x9mSZuHgO_4?t=75)
[^s3]: session 20261003-232357-chrono-2FYKPJ, step 15 — [video at 2:39](https://youtu.be/x9mSZuHgO_4?t=159)
[^s4]: session 20261003-232357-chrono-2FYKPJ, step 17 — [video at 3:08](https://youtu.be/x9mSZuHgO_4?t=188)
[^s5]: session 20261003-232357-chrono-2FYKPJ, step 14 — [video at 2:31](https://youtu.be/x9mSZuHgO_4?t=151)
[^s6]: session 20261003-232357-chrono-2FYKPJ, step 18 — [video at 3:20](https://youtu.be/x9mSZuHgO_4?t=200)
[^s7]: session 20261003-232357-chrono-2FYKPJ, step 11 — [video at 1:41](https://youtu.be/x9mSZuHgO_4?t=101)
[^s8]: session 20261003-233532-chrono-2FYKPJ, step 7 — [video at 1:03](https://youtu.be/RNRDUiKRry4?t=63)
[^s9]: session 20261003-233532-chrono-2FYKPJ, step 3 — [video at 0:34](https://youtu.be/RNRDUiKRry4?t=34)
[^s10]: session 20261003-233532-chrono-2FYKPJ, step 4 — [video at 0:41](https://youtu.be/RNRDUiKRry4?t=41)
