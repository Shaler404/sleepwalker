---
game: com.oakever.akari
title: "Hearts (3 per level)"
type: feature
feature: hearts
version_seen: 1.0.2
verified_at: 2026-10-05
sources: [20261003-200925-chrono-2FYKPJ, 20261003-232850-chrono-2FYKPJ, 20261005-002947-chrono-2FYKPJ]
---

# Hearts (3 per level)

Three red hearts on the bar above the grid of every level, left of the cat counter. Each wrong cat costs one heart; when the third is lost the level ends on the "Almost!" screen, where Revive (with an ad) or Restart (free) are offered. Every level and every restart begins with three hearts again [^s3] [^s5] [^s2].

## Why it appeared

Level 1 HUD shows 3 hearts [^s1]. They are on the level screen from Level 1 on; the tutorial does not mention them [^s3].

## Where to find it

On the [Akari level](core-level.md) screen, in the white bar under the two rule cards, left of the cat counter. The hearts are not a separate screen and no control opens them [^s4].

<!-- no-entry: part of the level screen HUD; no control or screen leads to them -->

## What it looks like

Three red hearts on the left of a white bar; the cat counter ("0/6") is on the right of the same bar. Under the grid are the two boosters, the cat (count 1) and the bulb (count 4) [^s2].

![Level 4 at the start: three red hearts left of the cat counter 0/6, the grid below and the cat and bulb boosters under it](../img/20261005-hearts-screen-b946d033.webp) [^s2]
*The hearts bar on Level 4: three hearts, then the cat counter*

A lost heart turns grey; the cat counter does not change for a wrong cat (see the [Akari level](core-level.md) page for the frame with all three hearts grey) [^s5].

## How it works

- Three hearts at the start of every level seen (Levels 1, 2 and 4) and after Restart (version 1.0.2) [^s3] [^s5] [^s2].
- Each wrong cat (a double tap on a cell that is not in the solution) costs one heart and leaves a red X on the cell; correct cats cost nothing [^s5].
- Losing the third heart ends the level on "Almost!": a broken heart over the hearts bar, the cat counter as it stood, an orange Revive button with an AD icon and a green Restart button [^s5].
- Restart is free and reopens the same board with three hearts [^s5].
- Revive: the game's Help Center says that after a failed level, Revive plays a reward video ad, restores a life and continues the level with its progress kept; if the ad is not ready, a toast message is shown [^s8]. This is the game's own help text; Revive itself was not tapped.
- Levels 1 and 2 were won without a wrong move; all three hearts were still drawn on the win screens [^s7].

![The third wrong cat: the last heart goes grey and the Almost! screen comes up with Revive and Restart](../clips/20261003-out-of-hearts-almost.webp) [^s5]
*Clip 4 s · Level 4: the third heart is lost and "Almost!" appears*

## Outcomes

| Outcome of the base level | Under hearts | Source |
|---|---|---|
| Win | The same as the base level; the hearts left stay on the dimmed bar behind the win screen | [^s7] |
| Loss (out of hearts) | The hearts are the loss: the third wrong cat ends the level on "Almost!" with Revive (ad) and Restart (free, 3 hearts again) | [^s5] |

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Shown from level 1 on the HUD (3 hearts), not mentioned by the tutorial <!-- case:chk-first-level --> | Played the tutorial and Level 1 | Hearts first on Level 1 | ✅ [^s3] |
| Hearts bar above the grid: 3 red hearts, left of the cat counter <!-- case:chk-screen --> | Opened Levels 1, 2 and 4 | Three hearts each time | ✅ [^s3] |
| Not a screen: the hearts bar on the level HUD, left of the cat counter; no button opens it <!-- case:chk-entry --> | Looked for a control that opens the hearts | None; they are part of the level HUD | ✅ [^s4] |
| Each wrong cat costs one heart and leaves a red X; correct cats cost nothing; 3 hearts per level, refilled on Restart and on a new level <!-- case:chk-rules --> | Deliberate wrong double taps on Level 4, then Restart | One heart per wrong cat; 3 hearts after Restart | ✅ [^s5] |
| Losing the 3rd heart ends the level with Almost! (broken heart, Revive with an ad, Restart) <!-- case:chk-loss --> | Three wrong cats on Level 4 | "Almost!" with Revive and Restart | ✅ [^s5] |
| Why it appeared: the trigger that brought it up <!-- case:chk-appeared --> | Opened Level 1 | Hearts on the HUD | ✅ [^s1] |
| How it interacts with the other pieces: Revive restores a life (Help Center article); bar beside the cat counter, above the boosters; Level 4 starts at 3/3 again <!-- case:chk-interactions --> | Read the Help Center's Revive article; opened Level 4 | As described | ✅ [^s2] [^s8] |

## Not verified

- What Revive actually gives in play (one heart or all three, the board kept) and the ad it plays: known only from the Help Center text.
- Whether the boosters (cat, bulb) can place a wrong cat or cost a heart.

[^s1]: session 20261003-200925-chrono-2FYKPJ, step 13 — [video at 1:39](https://youtu.be/JOMuD_cF8gM?t=99)
[^s2]: session 20261005-002947-chrono-2FYKPJ, step 10 — [video at 1:22](https://youtu.be/5odRuC4Mzak?t=82)
[^s3]: session 20261003-200925-chrono-2FYKPJ, step 9 — [video at 0:36](https://youtu.be/JOMuD_cF8gM?t=36)
[^s4]: session 20261003-232850-chrono-2FYKPJ, step 11 — [video at 3:06](https://youtu.be/94hgW4CXmbg?t=186)
[^s5]: session 20261003-232850-chrono-2FYKPJ, step 18 — [video at 3:47](https://youtu.be/94hgW4CXmbg?t=227)
[^s7]: session 20261003-200925-chrono-2FYKPJ, step 10 — [video at 0:57](https://youtu.be/JOMuD_cF8gM?t=57)

[^s8]: session 20261005-002947-chrono-2FYKPJ, step 3 — [video at 0:34](https://youtu.be/5odRuC4Mzak?t=34)
