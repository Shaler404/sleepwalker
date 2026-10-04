---
game: com.oakever.akari
title: "Hearts (3 per level)"
type: feature
feature: hearts
version_seen: 1.0.2
verified_at: 2026-10-03
sources: [20261003-200925-chrono-2FYKPJ]
---

# Hearts (3 per level)

Three red hearts on the bar above the grid of every level, left of the cat counter. Each level started with three; no heart was lost in this session, so what costs a heart and what happens at zero are not known [^s2] [^s3].

## Why it appeared

Level 1 HUD shows 3 hearts [^s1]. They are on the level screen from Level 1 on; the tutorial does not mention them [^s3].

## Where to find it

On the [Akari level](core-level.md) screen, in the bar under the rule cards, left of the cat counter. They are not a separate screen and no control opens them.

<!-- no-entry: part of the level screen HUD; no control or screen leads to them -->

## What it looks like

Three red hearts in a white bar, with the cat counter on the right of the same bar [^s2].

![Level 2 at the start: three red hearts left of the cat counter 0/6 in the bar above the grid](../img/20261003-hearts-screen-ba46b032.webp) [^s2]
*The hearts: three red hearts in the bar above the grid*

## How it works

- Three hearts at the start of Level 1 and of Level 2 (version 1.0.2) [^s2] [^s3].
- Levels 1 and 2 were won without a wrong move; all three hearts were still drawn on the win screens [^s4].
- Inferred, not verified: a wrong cat placement costs a heart and the level is lost at zero hearts.

## Outcomes

| Outcome of the base level | Under hearts | Source |
|---|---|---|
| Win | The same as the base level; the three hearts stay on the dimmed bar behind the win screen | [^s4] |
| Loss | Not seen: no heart was lost | — |

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Shown from level 1 on the HUD (3 hearts), not mentioned by the tutorial <!-- case:chk-first-level --> | Played the tutorial and Level 1 | Hearts first on Level 1 | ✅ [^s3] |
| Hearts bar above the grid: 3 red hearts, left of the cat counter <!-- case:chk-screen --> | Opened Levels 1 and 2 | Three hearts each time | ✅ [^s3] |
| Why it appeared: the trigger that brought it up <!-- case:chk-appeared --> | Opened Level 1 | Hearts on the HUD | ✅ [^s1] |
| Where to find it <!-- case:chk-entry --> | — | not verified: part of the level HUD, no own entry |  |
| What it does and how it is used <!-- case:chk-rules --> | — | not verified: no heart lost |  |
| How it interacts with the other pieces <!-- case:chk-interactions --> | — | not verified |  |
| Whether it adds a way to lose <!-- case:chk-loss --> | — | not verified |  |

## Not verified

- Where to find it: the hearts have no own entry; they are on the level HUD <!-- case:chk-entry -->
- What costs a heart (a wrong cat, a broken number) <!-- case:chk-rules -->
- How hearts interact with the boosters and the cat counter <!-- case:chk-interactions -->
- Whether zero hearts loses the level, its screen and the retry offer <!-- case:chk-loss -->

[^s1]: session 20261003-200925-chrono-2FYKPJ, step 13 — [video at 1:42](https://youtu.be/JOMuD_cF8gM?t=102)
[^s2]: session 20261003-200925-chrono-2FYKPJ, step 15 — [video at 2:06](https://youtu.be/JOMuD_cF8gM?t=126)
[^s3]: session 20261003-200925-chrono-2FYKPJ, step 9 — [video at 0:36](https://youtu.be/JOMuD_cF8gM?t=36)

[^s4]: session 20261003-200925-chrono-2FYKPJ, step 10 — [video at 0:57](https://youtu.be/JOMuD_cF8gM?t=57)
