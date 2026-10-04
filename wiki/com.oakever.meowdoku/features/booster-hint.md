---
game: com.oakever.meowdoku
title: "Hint booster (bulb)"
type: feature
feature: booster-hint
version_seen: 1.19.1
verified_at: 2026-10-03
sources: [20261003-200440-chrono-2FYKPJ, 20261003-201915-chrono-2FYKPJ, 20261003-202631-chrono-2FYKPJ]
---

# Hint booster (bulb)

The middle of the three boosters under the board of a [main level](level.md). It explains one deduction on
the board in a single sentence, and Apply carries it out. An exclusion hint crosses out cells; a hint that
finds the only possible cell places the cat there. Each use takes one from its count [^s3] [^s4]
[^s5].

## Why it appeared

On the level HUD at level 127, count 4 [^s1].

## Where to find it

Inside a [main level](level.md): the light-bulb button is the middle one of the three round boosters under
the board, with a red count badge [^s2] [^s6].

![Level 127 screen: the light-bulb button, middle of the three boosters under the board, count 4](../img/20261003-booster-hint-entry-fa23b474.webp) [^s2]
*Level 127: the light-bulb button, middle of the three boosters under the board, count 4*

![Level 130 before the first move: the light-bulb button in the middle under the board, count 3](../img/20261003-booster-hint-entry-ef91b2c0.webp) [^s6]
*Level 130 (Hard) before any move: the light-bulb button in the middle, count 3 (the banner ad at the bottom is blacked out)*

## What it looks like

A tap on the bulb darkens the board except the cells the hint is about. It shows a white tip box above the
board and an orange Apply button over the boosters [^s3] [^s6]. Two kinds of tip
were seen:

- Exclusion (Level 128, one cat on the board): "This cat's row, column and neighbors can't have other cats —
  exclude them". It lights the cat's row, its column and the cells touching it, each with an outlined cross
  [^s3].
- Single cell (Level 130, empty board): "Teal — only one cell left for a cat". It lights one cell, the only
  cell of the region the tip names [^s6]. The game calls this pale grey-blue
  region "Teal".

![Hint overlay on Level 128: the board darkened except the placed cat's row, column and neighbours, outlined crosses on them, a one-line tip above the board and the Apply button below](../img/20261003-booster-hint-screen-99c4663b.webp) [^s3]
*The exclusion hint on Level 128: the cat's row, column and neighbouring cells lit with outlined crosses, the tip above the board, Apply below it*

![Hint overlay on Level 130: the whole board dark except one pale-blue cell, the tip "Teal — only one cell left for a cat" above, Apply below](../img/20261003-booster-hint-screen-84b0936e.webp) [^s6]
*The single-cell hint on Level 130: only the one cell of the region is lit; the tip above the board, Apply over the boosters*

### Result

![After Apply on Level 128: solid white crosses on the row, column and neighbours of the cat; the bulb's badge 3](../img/20261003-booster-hint-result-fab1c1b1.webp) [^s4]
*After Apply on the exclusion hint: the outlined crosses became solid crosses on the board; the bulb's badge went from 4 to 3*

![After Apply on Level 130: a cat on the lit cell, a star flying up to the cat bar where the first head turned black, the bulb's badge 2](../img/20261003-booster-hint-result-ef85904a.webp) [^s5]
*After Apply on the single-cell hint: a cat on the cell, a star flying to the cat bar, the badge 3 to 2 (the banner ad is blacked out)*

![Apply on the single-cell hint: the overlay closes, a cat appears on the lit cell, a star flies to the cat bar, the badge drops to 2](../clips/20261003-hint-apply-places-cat.webp) [^s5]
*Clip 3 s · [original on YouTube from 2:30](https://youtu.be/3-USmjAyOV8?t=150)*

## How it works

- The hint picks a deduction from the current board. On Level 128 its tip was about the only cat on the board
  [^s3]. On the empty Level 130 board it was about a one-cell region [^s6].
  Which deduction it picks when several apply was not verified.
- Apply does what the tip says. An exclusion hint turns the outlined crosses into solid crosses, the same
  marks the player can place [^s4]. A single-cell hint places the cat [^s5].
- Score: the exclusion hint scored nothing (576 before and after) [^s3] [^s4]. The cat a hint placed
  scored +576 (0 to 576) [^s7].
- No fish lost on either use [^s4] [^s5].
- Count: 4 at Levels 127 and 128, 3 after one use [^s4]. It was still 3 at the start of Levels 129 and 130,
  and 2 after one use on Level 130 [^s8] [^s6]
  [^s5]. Inferred: the count carries over between levels, and the wins of
  Levels 128 and 129 added none.
- Restarting the level (Settings > Restart) kept the count at 2: the charge spent before the restart was not
  given back [^s9].

Version 1.19.1.

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| The overlay: the board dimmed, the cells of one deduction lit, a one-line tip, an Apply button <!-- case:chk-screen --> | Bulb tapped on Level 128 and Level 130 | ✅ | [^s3] [^s6] |
| Apply carries the hint out. Two kinds: a single-cell tip whose Apply places the cat (count 3 to 2, score +576, no fish cost), and an exclusion tip whose Apply turns the crosses around a cat solid (count 4 to 3, no score, no fish cost) <!-- case:chk-effect --> | Apply tapped on each kind: Level 130 (single cell), Level 128 (exclusion) | ✅ | [^s5] [^s4] |
| Count on a red badge: 4 at Level 127, 3 at Levels 129 and 130, 2 after the Level 130 use <!-- case:chk-balance --> | Badge read at each level start and after each use | ✅ | [^s5] |
| Where to find it: the middle booster under the board in a level <!-- case:chk-entry --> | The bulb tapped | ✅ | [^s2] [^s6] |
| Sinks: one charge per Apply <!-- case:chk-sinks --> | Two Applies | ✅ | [^s5] |
| Why it appeared: the trigger that brought it up (the first launch, a level won, a threshold, a timer, a loss): a fact with its frame, or a hypothesis to test <!-- case:chk-appeared --> | On the level HUD from the first level seen | ✅ | [^s1] |

## Not verified

- Sources: where hints come from is not seen <!-- case:chk-sources -->. Observed: the wins of Levels 128
  and 129 added none (3 at the start of Levels 129 and 130) [^s8] [^s6]. Not checked: the Daily Streak
  gift, the event rewards, a rewarded ad.
- At zero: not reached, 2 left at the end of the session <!-- case:chk-empty --> [^s10]. Not checked:
  whether the badge turns into a video icon and a tap plays a rewarded ad, as with the
  [Cat booster](booster-cat.md).
- Refill: no refill seen <!-- case:chk-refill -->. Observed: the count only went down with use and carried
  over between levels and a restart [^s6] [^s9]. Not checked: whether it refills by itself over a longer
  time, or what restores it at 0.
- Sinks: whether closing the overlay without Apply still spends one.

[^s1]: session 20261003-200440-chrono-2FYKPJ, step 3 — [video at 1:05](https://youtu.be/Pqx4QY-FpBA?t=65)
[^s2]: session 20261003-201915-chrono-2FYKPJ, step 3 — [video at 1:28](https://youtu.be/ffhYgQE4LvU?t=88)
[^s3]: session 20261003-201915-chrono-2FYKPJ, step 14 — [video at 4:38](https://youtu.be/ffhYgQE4LvU?t=278)
[^s4]: session 20261003-201915-chrono-2FYKPJ, step 15 — [video at 4:48](https://youtu.be/ffhYgQE4LvU?t=288)

[^s5]: session 20261003-202631-chrono-2FYKPJ, step 10 — [video at 2:32](https://youtu.be/3-USmjAyOV8?t=152)
[^s6]: session 20261003-202631-chrono-2FYKPJ, step 9 — [video at 2:23](https://youtu.be/3-USmjAyOV8?t=143)
[^s7]: session 20261003-202631-chrono-2FYKPJ, step 12 — [video at 4:22](https://youtu.be/3-USmjAyOV8?t=262)
[^s8]: session 20261003-202631-chrono-2FYKPJ, step 5 — [video at 1:06](https://youtu.be/3-USmjAyOV8?t=66)
[^s9]: session 20261003-202631-chrono-2FYKPJ, step 15 — [video at 5:05](https://youtu.be/3-USmjAyOV8?t=305)
[^s10]: session 20261003-202631-chrono-2FYKPJ, step 23 — [video at 7:11](https://youtu.be/3-USmjAyOV8?t=431)
