---
game: com.crypt.gram.puzz
title: "Secret Level"
type: feature
feature: secret-level
version_seen: 3.6.1
verified_at: 2026-10-06
sources: [20261006-003220-chrono-2FYKPJ, 20261006-024420-chrono-2FYKPJ]
---

# Secret Level

A level offered as the reward of the Daily Tasks bar: when the ninth task of the day is done, the Daily Tasks card on home turns into a "Secret Level" card with a PLAY button [^s1]. How it differs from a regular level was not seen: the session ended on its loading screen [^s2].

## Why it appeared

The ninth segment of the Daily Tasks bar filled when the last task of the third batch was done (level 8 won); back on home the Daily Tasks card had become the Secret Level card, with the day's timer still above it (23h 2m) [^s1]. See [Daily Tasks](daily-tasks.md).

## Where to find it

Home screen > the Daily Tasks place under the Daily Challenge and Chest Hunt cards: once the bar is full, the task tiles and the bar are replaced by a lilac card with a star-wand icon, "Secret Level" and a purple PLAY button [^s1].

![Home after the ninth task: the Daily Tasks card turned into Secret Level with a PLAY button](../img/20261006-secret-level-entry-e9cd01b5.webp) [^s1]
*The Secret Level card in place of the Daily Tasks list; PLAY on the right*

After PLAY had been tapped once (the session ended on the loading screen), the card on the next session's home read "Secret Level" with CONTINUE instead of PLAY, before and after level 9, with the day's timer at 21h 11m and then 21h 4m [^s3] [^s4]. CONTINUE was not tapped.

## What it looks like

<!-- no-screen: PLAY led to the game's "Crafting Your Quote" loading screen and the session ended there; the level itself was not seen -->
PLAY opened the game's loading screen ("Crafting Your Quote", "preparing new quote ...") and the session ended before the level showed [^s2].

## How it works

- Unlocked by filling the 9-segment Daily Tasks bar (nine tasks in three batches of three, levels 4-8 in this session, 3.6.1) [^s1].
- The star-wand icon at the end of the Daily Tasks bar is this level [^s1].
- Its board, rules and reward were not seen.

## Outcomes

| Outcome | As the base or what differs | Frame |
|---|---|---|
| win <!-- case:under-win --> | not verified | — |
| quit <!-- case:under-quit --> | not verified | — |
| restart <!-- case:under-restart --> | not verified | — |
| exit app <!-- case:under-exit-app --> | not verified | — |
| Lose by 3 mistakes: popup with heart -1, Home/Restart/REVIVE <!-- case:under-loss-3-mistakes --> | not verified | — |

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared <!-- case:chk-appeared --> | Finished the ninth Daily Task (level 8 won) | The Daily Tasks card turned into Secret Level PLAY | [^s1] |
| Where to find it <!-- case:chk-entry --> | Looked at home | The Secret Level card in the Daily Tasks place, PLAY on the right | [^s1] |
| What it looks like <!-- case:chk-screen --> | Tapped PLAY | The loading screen; the session ended before the level | [^s2] |
| The card after PLAY <!-- case:card-continue --> | Came back to home the next session, at level 9 and level 10 | The card reads Secret Level with CONTINUE (was PLAY); the day's timer runs on | [^s4] |
| How it is announced <!-- case:chk-announce --> | Back on home after level 8 | No popup was seen: the card itself changed | [^s1] |
| What differs in play <!-- case:chk-differs --> | — | not verified |  |
| Its win <!-- case:chk-win --> | — | not verified |  |
| Each loss <!-- case:chk-loss --> | — | not verified |  |
| Retry and continue offers <!-- case:chk-retry --> | — | not verified |  |
| Where and how often it comes up <!-- case:chk-frequency --> | Filled the Daily Tasks bar | Once a day at most, as the bar's reward (inferred from the bar's place on the daily card) | [^s1] |

## Not verified

- Where to find it: whether the card stays until the day's reset if the level is not played <!-- case:chk-entry -->
- What it looks like: the Secret Level board <!-- case:chk-screen -->
- How it is announced: whether a popup announces it <!-- case:chk-announce -->
- What differs in play from the base level <!-- case:chk-differs -->
- Its win: the win screen and the reward <!-- case:chk-win -->
- Each loss: its fail screen and what it costs <!-- case:chk-loss -->
- Retry and continue offers after a loss <!-- case:chk-retry -->
- Where and how often it comes up: once per day's bar (inferred) <!-- case:chk-frequency -->
- Win card under Secret Level <!-- case:under-win -->
- Home icon in level under Secret Level <!-- case:under-quit -->
- Restart from the loss popup under Secret Level <!-- case:under-restart -->
- Force-stop mid-level under Secret Level <!-- case:under-exit-app -->
- Lose by 3 mistakes under Secret Level <!-- case:under-loss-3-mistakes -->

[^s1]: session 20261006-003220-chrono-2FYKPJ, step 72 — [video at 23:31](https://youtu.be/W0PeVNo113E?t=1411)

[^s2]: session 20261006-003220-chrono-2FYKPJ, step 73 — [video at 23:59](https://youtu.be/W0PeVNo113E?t=1439)

[^s3]: session 20261006-024420-chrono-2FYKPJ, step 6 — [video at 3:14](https://youtu.be/ZmbMZC7iP0E?t=194)
[^s4]: session 20261006-024420-chrono-2FYKPJ, step 20 — [video at 9:46](https://youtu.be/ZmbMZC7iP0E?t=586)
