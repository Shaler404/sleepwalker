---
game: com.maroieqrwlk.unpin
title: "Level race"
type: feature
feature: race
version_seen: 241.5.1
verified_at: 2026-10-04
sources: [20261004-004411-chrono-2FYKPJ]
---

# Level race

A timed event offered in a popup before a level: the player races three other players to be the first to
beat 15 levels, within a time limit (5 h 59 min left when offered); first place shows a reward of +250
coins [^s1]. The player can join with **Go!** or decline with **No, thanks** [^s1]. It was declined in the
only session that saw it, so the race itself was not seen [^s3].

## Why it appeared

The popup "New race started!" came on tapping **Play!** for level 11, right after the level 10 win; it was
the first time the player's progress reached level 11 [^s1]. Inferred: the event unlocks at level 11 (or
after the level 10 win); whether it is tied to the level or to a schedule is not verified.

## Where to find it

The map: **Play!** under the current level. At level 11 the tap opened the race popup before the level
[^s1]. The map before the tap showed no race button [^s2]; whether one appears after joining is not
verified.

![Map at level 11 after the level 10 win: Play! at the bottom, the Collections gift box right of it, no race button](../img/20261004-race-entry-9de2a568.webp) [^s2]
*Map at level 11: the race popup came on Play! (the player's name in the league banner blacked out)*

## What it looks like

<!-- no-screen: the race was declined, its own screen was never opened -->
The race screen was not seen: the offer was declined [^s3]. The offer popup is described below.

### Popup

![New race started!: Time Left 5h 59m, a line on racing other players to beat 15 levels, three trophies, a bar with places 4 to 1 and +250 coins at its end, Go! and No, thanks](../img/20261004-race-popup-eeb548b7.webp) [^s1]
*The race offer: the timer, the goal (15 levels), the bar with the player ("You") at place 4 and +250 coins for place 1*

From top to bottom [^s1]:

- the title "New race started!" and **Time Left** with a green timer (5h 59m);
- a line: race other players to beat 15 levels the fastest, for rewards;
- three trophies: gold 1, silver 2, bronze 3;
- a bar with four markers, places 4, 3, 2 and 1, the player ("You") on place 4 at the left end, and a coin
  pile with **+250** past place 1 at the right end;
- a green **Go!** and a grey **No, thanks** under it.

## What you can do

| Tab or button | What it does |
|---|---|
| [Go!](#go) | Joins the race; not tried |
| [No, thanks](#no-thanks) | Declines: the popup closes and the level opens at once [^s3] |

### Go!

<!-- no-frame: Go! was not tapped -->
Not tried in version 241.5.1 [^s3].

### No, thanks

<!-- no-frame: the next frame is the level itself, shown on the Pin-pull level page -->
**No, thanks** closed the popup and opened level 11 at once, with no other screen between [^s3].

## How it works

Version 241.5.1, from the offer popup only [^s1]:

| Item | Value |
|---|---|
| Racers | 4 (the player and three others) |
| Goal | beat 15 levels the fastest |
| Time limit | 5 h 59 min left when offered |
| Reward shown | +250 coins for place 1; rewards for places 2-4 not shown |

What a race counts (wins only or every level), the rewards for places 2 and 3, and what happens at the end of
the timer were not seen.

## Outcomes

Level race runs over ordinary levels; the outcomes of a level while a race runs were not seen, because the race
was declined [^s3].

| Outcome of the base level | Under Level race | Source |
|---|---|---|
| Win | not verified | — |
| Restart | not verified | — |
| Quit | not verified | — |
| Exit the app | not verified | — |
| Balls fell out | not verified | — |

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Declined <!-- case:declined --> | Tapped No, thanks on the offer popup | ✅ The popup closed and level 11 opened at once | [^s3] |
| The rules <!-- case:chk-rules --> | Read the offer popup | ✅ Race three other players (four racers) to beat 15 levels the fastest; a bar with places 4 to 1, the player on place 4; Go! joins, No, thanks declines | [^s1] |
| Why it appeared <!-- case:chk-appeared --> | Tapped Play! for level 11 right after the level 10 win | ✅ The popup "New race started!" came before the level | [^s1] |
| Where to find it <!-- case:chk-entry --> | — | not verified: only the offer on Play! seen; no race button on the map before it | [^s2] |
| What it looks like <!-- case:chk-screen --> | — | not verified: declined, the race screen not opened |  |
| Its timer and schedule <!-- case:chk-timer --> | — | not verified: 5h 59m left on the offer; the next race not seen | [^s1] |
| During a level <!-- case:chk-in-level --> | — | not verified |  |
| Progress per level <!-- case:chk-progress --> | — | not verified |  |
| The rewards <!-- case:chk-rewards --> | — | not verified: only +250 coins for place 1 shown on the offer | [^s1] |
| The end <!-- case:chk-end --> | — | not verified |  |
| Win under Level race <!-- case:under-win --> | — | not verified |  |
| Restart under Level race <!-- case:under-restart --> | — | not verified |  |
| Quit under Level race <!-- case:under-quit --> | — | not verified |  |
| Exit the app under Level race <!-- case:under-exit-app --> | — | not verified |  |
| Balls fell out under Level race <!-- case:under-balls-out --> | — | not verified |  |

## Not verified

- Where to find it: a race button or screen once joined <!-- case:chk-entry -->
- What it looks like: the race screen <!-- case:chk-screen -->
- Its timer and schedule: what happens when 6 h run out, and when the next race comes <!-- case:chk-timer -->
- What shows during a level while it runs <!-- case:chk-in-level -->
- Progress per level: what a win, and a loss, add <!-- case:chk-progress -->
- The rewards for each place <!-- case:chk-rewards -->
- The end: the results screen and the reward paid <!-- case:chk-end -->
- The win screen under Level race: as the base, or what differs <!-- case:under-win -->
- Restart under Level race: as the base, or what differs <!-- case:under-restart -->
- Quit under Level race: as the base, or what differs <!-- case:under-quit -->
- Exit the app under Level race: as the base, or what differs <!-- case:under-exit-app -->
- Balls fell out under Level race: as the base, or what differs <!-- case:under-balls-out -->
- Whether a declined race is offered again, and whether it unlocks by level or by time.

[^s1]: session 20261004-004411-chrono-2FYKPJ, step 17 — [video at 5:10](https://youtu.be/KwWbRYgzFFk?t=310)
[^s2]: session 20261004-004411-chrono-2FYKPJ, step 16 — [video at 4:39](https://youtu.be/KwWbRYgzFFk?t=279)
[^s3]: session 20261004-004411-chrono-2FYKPJ, step 18 — [video at 5:35](https://youtu.be/KwWbRYgzFFk?t=335)
