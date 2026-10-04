---
game: com.block.juggle
title: "Consecutive Daily Victories"
type: feature
feature: daily-victories
version_seen: 10.8.1
verified_at: 2026-10-04
sources: [20261003-212548-chrono-2FYKPJ, 20261003-235233-chrono-2FYKPJ]
---

# Consecutive Daily Victories

A panel on the home menu titled "Consecutive Daily Victories" with a crown on a WIN ribbon, a counter
"xN" and a tick. It counts calendar days in a row with at least one [Adventure](adventure.md) level won:
the first win of a day adds one, more wins the same day add nothing, and the tick turns green once the
day's win is in [^s2] [^s3]. It is a different counter from the
[Adventure win streak](adv-win-streak.md) ("Consecutive Victories" on the Adventure result screen), which
counts wins in a row and is reset by a loss [^s4]. No reward was seen for it [^s2].

## Why it appeared

On the home menu showing x0, the first time the menu was opened (the phone's Back key from a classic
game) [^s1].

## Where to find it

Home menu > the panel under the Block Blast logo, above the Adventure button [^s1]. The home menu is
reached with the Back key from the classic board (see [Home menu](home-menu.md)).

![The home menu; the Consecutive Daily Victories panel with the WIN crown and x0 is under the logo](../img/20261003-daily-victories-entry-93112c2c.webp) [^s1]
*The Consecutive Daily Victories panel under the logo: WIN crown and x0*

## What it looks like

![The Consecutive Daily Victories panel at x0: crown with the WIN ribbon, the counter, a grey tick bottom right](../img/20261003-daily-victories-screen-93112c2c.webp) [^s1]
*Before any Adventure win: x0 and a grey tick*

A white panel with a blue title bar "Consecutive Daily Victories". On the left a crown on a green WIN
ribbon, in the middle "xN", bottom right a tick in a circle: grey before the day's first Adventure win,
green after it [^s1] [^s3]. The panel was not tapped.

### Result

![The home menu after two Adventure wins on 2026-10-04: the panel shows x2 with a green tick](../img/20261003-daily-victories-result-93112c2c.webp) [^s2]
*After the second win of the second day: still x2, green tick*

## How it works

Version 10.8.1. The day boundary is the phone's midnight [^s2].

| When | The panel | Source |
|---|---|---|
| Two classic games (classic has no win) | x0, grey tick | [^s1] |
| Adventure level 1 won, 2026-10-03 23:56 | x1, green tick | [^s3] |
| Adventure level 2 lost, same day | x1, green tick | [^s4] |
| Adventure level 2 won just after midnight, 2026-10-04 | x2 | [^s2] |
| Adventure level 3 won, same day | x2, green tick | [^s2] |
| Adventure level 4 quit with gear > Home | x2, green tick | [^s5] |

- Only Adventure wins counted; classic games never moved it [^s1] [^s3].
- A loss on a day already won did not lower it, while the Adventure win streak went from x1 to x0 on
  the same loss [^s4].
- Nothing shows during an Adventure level; the result screen's panel is the Adventure win streak, not
  this counter [^s3].
- No reward came at x1 or x2: no popup and no currency on the home menu or the win screen [^s2].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared <!-- case:chk-appeared --> | Opened the home menu with Back | ✅ The panel with x0 | [^s1] |
| Where to find it <!-- case:chk-entry --> | Looked at the home menu | ✅ The panel at the top of the home menu | [^s1] |
| Its screen <!-- case:chk-screen --> | Looked at the panel | ✅ Crown WIN badge, counter xN, a tick bottom right (grey, green after the day's win) | [^s1] |
| The counter <!-- case:chk-counter --> | Won Adventure levels on 2026-10-03 and 2026-10-04 | ✅ Counts calendar days in a row with an Adventure win: x0 to x1, x2 on the next day, still x2 after a second win that day | [^s2] |
| During a level <!-- case:chk-in-level --> | Played Adventure levels 1 to 4 | ✅ Nothing during the level; the result panel is the Adventure win streak | [^s3] |
| Rewards <!-- case:chk-rewards --> | Reached x1 and x2 | ✅ No reward seen | [^s2] |
| What breaks it <!-- case:chk-break --> | Lost Adventure level 2 on a day already won | partly: a same-day loss does not break it (x1 kept); a missed day not tested |  |
| Offers to keep it <!-- case:chk-save --> | — | not verified: never broken |  |
| Win under the streak <!-- case:under-win --> | Won Adventure levels 1, 2 and 3 | ✅ x1 on the first day's win, x2 on the next day's first win, x2 kept on a second win that day | [^s2] |
| No Space Left under the streak <!-- case:under-no-space-left --> | Lost Adventure level 2 at x1 | ✅ x1 kept with the green tick | [^s4] |
| Quit under the streak <!-- case:under-quit --> | Gear > Home in Adventure level 4 at x2 | ✅ x2 kept with the green tick | [^s5] |
| Restart (Settings > Replay) under the streak <!-- case:under-restart --> | — | not verified |  |
| Leaving the app under the streak <!-- case:under-exit-app --> | — | not verified |  |

## Not verified

- What breaks it: a day with no Adventure win, and what the break costs (task daily-victories-day2) <!-- case:chk-break -->
- Offers to keep it after a break and their price <!-- case:chk-save -->
- Settings gear > Replay in an Adventure level with the streak running <!-- case:under-restart -->
- Leaving the app with the streak running <!-- case:under-exit-app -->
- Whether anything pays at a higher count (x3 and up)
- What a tap on the panel opens

[^s1]: session 20261003-212548-chrono-2FYKPJ, step 29 — [video at 5:55](https://youtu.be/ReMKqt9albk?t=355)
[^s2]: session 20261003-235233-chrono-2FYKPJ, step 60 — [video at 12:34](https://youtu.be/RE70Idi_jrA?t=754)
[^s3]: session 20261003-235233-chrono-2FYKPJ, step 22 — [video at 4:11](https://youtu.be/RE70Idi_jrA?t=251)
[^s4]: session 20261003-235233-chrono-2FYKPJ, step 30 — [video at 6:08](https://youtu.be/RE70Idi_jrA?t=368)
[^s5]: session 20261003-235233-chrono-2FYKPJ, step 64 — [video at 13:28](https://youtu.be/RE70Idi_jrA?t=808)
