---
game: com.maroieqrwlk.unpin
title: "Map chest with timer"
type: feature
feature: map-chest
version_seen: 241.5.1
verified_at: 2026-10-03
sources: [20261003-203702-chrono-2FYKPJ, 20261003-214021-chrono-2FYKPJ]
---

# Map chest with timer

A chest button at the left edge of the map with a countdown under it. The countdown ran out during levels
6-9 and the label changed to **OPEN** [^s1] [^s3]. The chest was not opened, so its contents are unknown.

## Why it appeared

On the map from its first visit after L3, timer 13m36s counting down [^s1].

## Where to find it

The map, left edge, under the top bar: a chest icon in a grey square with a clock and the time left under it
[^s2]. When the time is up the label under it reads **OPEN** in green [^s3]; it still read OPEN at
the start of the next session, at level 10 [^s5].

![Map: the chest button at the left edge with a 13m 36s timer under it](../img/20261003-map-chest-entry-99fc23cc.webp) [^s2]
*The map after the level 3 win: the chest button at the left edge, 13m 36s under it*

## What it looks like

<!-- no-screen: the chest was not tapped; what it opens was not seen -->

Only the button was seen; the chest was not tapped.

### Result

![Map after the L9 win: the chest timer ended, the chest button now reads OPEN](../img/20261003-map-chest-result-cdb2ec35.webp) [^s3]
*The map after the level 9 win: the chest button reads OPEN*

## How it works

Version 241.5.1.

| When | Under the chest |
|---|---|
| Map after the level 3 win | 13m 36s [^s2] |
| Map after the level 5 win | 8m 56s [^s1] |
| Map after the level 6 win | 5m 48s [^s4] |
| Map after the level 9 win | OPEN [^s3] |
| Map at level 10, the next session (21:48) | OPEN [^s5] |

Between the level 3 and level 5 maps the timer fell by 4m 40s in about 4m 48s of session time, so it runs
while levels are played [^s2] [^s1]. Between the level 5 and level 6 maps it fell by only 3m 08s in about
4m 47s, a span that held the first interstitial video ad (about 1.5 minutes) [^s1] [^s4]. Inferred: the
timer stops while an ad is on screen; not verified. Also inferred: a timer of about 15 minutes from the
start of the session.

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared <!-- case:chk-appeared --> | Won level 3, the map appeared | ✅ The chest with its timer on the first map | [^s1] |
| Map, left side: chest icon with a timer; shows a green OPEN label when ready (seen at L10, 21:48) <!-- case:chk-entry --> | Looked at the map | ✅ The chest button at the left edge, OPEN | [^s5] |
| What it looks like <!-- case:chk-screen --> | — | not verified: not tapped |  |
| The progress <!-- case:chk-progress --> | Watched the timer | not verified: the timer ran out to OPEN | [^s3] |
| The items <!-- case:chk-items --> | — | not verified |  |
| How it is earned <!-- case:chk-earn --> | — | not verified |  |
| Using it: opening the chest <!-- case:chk-use --> | — | not verified: OPEN not tapped |  |
| Completing it: the reward <!-- case:chk-complete --> | — | not verified |  |

## Not verified

- What it looks like: the chest's screen <!-- case:chk-screen -->
- The progress: the timer's full length and whether it restarts after opening <!-- case:chk-progress -->
- The items: what the chest holds <!-- case:chk-items -->
- How it is earned: a timer only, or wins too <!-- case:chk-earn -->
- Using it: opening the chest at OPEN <!-- case:chk-use -->
- Completing it: the reward <!-- case:chk-complete -->

[^s1]: session 20261003-203702-chrono-2FYKPJ, step 19 — [video at 6:01](https://youtu.be/cirqlD7KGWI?t=361)
[^s2]: session 20261003-203702-chrono-2FYKPJ, step 5 — [video at 1:43](https://youtu.be/cirqlD7KGWI?t=103)
[^s3]: session 20261003-203702-chrono-2FYKPJ, step 52 — [video at 20:59](https://youtu.be/cirqlD7KGWI?t=1259)
[^s4]: session 20261003-203702-chrono-2FYKPJ, step 30 — [video at 10:39](https://youtu.be/cirqlD7KGWI?t=639)
[^s5]: session 20261003-214021-chrono-2FYKPJ, step 30 — [video at 7:39](https://youtu.be/siJO2QCuGxI?t=459)
