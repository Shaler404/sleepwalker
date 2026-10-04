---
game: com.oakever.meowdoku
title: "Daily Challenge"
type: feature
feature: daily-challenge
version_seen: 1.19.1
verified_at: 2026-10-04
sources: [20261003-200440-chrono-2FYKPJ, 20261003-235107-chrono-2FYKPJ]
---

# Daily Challenge

One extra board per day, named by its date, with the same rules as the [main level](level.md) on a larger
board and a stopwatch. A countdown on its Home button shows the time until the next day's board [^s1] [^s2].

## Why it appeared

Button under Level on Home, timer 03:5x until reset; opens a dated 10x10 board with timer [^s1].

## Where to find it

On [Home](home.md), the blue Daily Challenge button under the Level button, with a countdown (03:53:49 at the
time of the frame) [^s2].

![Home screen: the blue Daily Challenge button under the Level button, with a countdown](../img/20261003-daily-challenge-entry-ad85780f.webp) [^s2]
*Home screen: the blue Daily Challenge button under the Level button, with a countdown*

## What it looks like

![Daily Challenge board 10/03: three fish, stopwatch 00:00, ten cat colour icons, rules strip, 10x10 board, three boosters](../img/20261003-daily-challenge-screen-ebd19564.webp) [^s3]
*The board of 3 October: "Level 10/03", three fish, the stopwatch at 00:00, ten cat heads, the rules strip, the 10x10 board, the three boosters*

The screen is laid out like a main level, with these differences [^s3]:

- The level label is the date: "10/03" (month/day, inferred from the session date, 3 October).
- A stopwatch next to the three fish, at 00:00.
- A 10x10 board in ten colour regions, and ten cat heads above the rules strip (nine on the main level).
- The same rules strip and the same three boosters with the same counters (cat 1, bulb 4, mouse 1): inferred,
  the booster stock is shared with the main levels.

### Trial skin tooltip

![Daily Challenge opening: the tooltip under the three fish says a 3-fish clear unlocks a trial skin](../img/20261003-daily-challenge-popup-e785944a.webp) [^s1]
*As the board opens, a tooltip under the three fish: a 3-fish clear unlocks a trial skin*

When the board opens, a tooltip with a cat icon points at the three fish: "3-Fish clear unlocks a trial
skin." [^s1]. The board was still appearing behind it. The first tap on the back arrow closed the tooltip;
the board stayed [^s3].

## How it works

- One board per date; the label carries the date [^s3].
- The countdown on the Home button read 03:53:49 at 20:06:17 local time [^s2] and 00:08:28 at about
  23:51:33 the same day [^s5]: both readings put its end at local midnight. What renews then (a new board)
  was not seen.
- The stopwatch still read 00:00 about nine seconds after the board opened, with no move made [^s3]. Inferred:
  it starts with the first move.
- A 3-fish clear unlocks a trial skin (see [Cat skins](cat-skins.md)) [^s1].
- Leaving: the second tap on the back arrow returned to Home with no confirmation
  [^s4].
- The board was not played.

Version 1.19.1.

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| The countdown runs out at local midnight <!-- case:reset-time --> | Home countdown read twice: 03:53:49 at 20:06:17, 00:08:28 at about 23:51:33 | ✅ | [^s5] |
| Dated board (10/03), 10x10, stopwatch from 00:00, 3 fish, same three rules and boosters as the main level <!-- case:chk-screen --> | Opened from Home, frames marked | ✅ | [^s3] |
| Why it appeared: the trigger that brought it up (the first launch, a level won, a threshold, a timer, a loss): a fact with its frame, or a hypothesis to test <!-- case:chk-appeared --> | The Daily Challenge button on Home | ✅ | [^s1] |
| Where to find it: the screen and the button that open it (mark --as entry --at X,Y) <!-- case:chk-entry --> | Daily Challenge button tapped; frame marked | not verified | [^s2] |
| Today's claim, task list or challenge: what it gives <!-- case:chk-today --> | Tooltip read: a 3-fish clear unlocks a trial skin | not verified | [^s1] |
| The calendar or the task list: every day or task and its reward <!-- case:chk-calendar --> | No calendar seen: the button opens today's board directly | not verified |  |
| The next day: what renews and when (a daily follow-up) <!-- case:chk-next-day --> | Countdown read twice: it ends at local midnight; the day after not seen | not verified | [^s5] |
| A missed day: what is lost or reset <!-- case:chk-missed --> | Not seen | not verified |  |
| If it is a board: play it once, its win and its loss <!-- case:chk-play --> | Not played | not verified |  |

## Not verified

- Where to find it: any other entry (a calendar of past days) <!-- case:chk-entry -->
- Today's reward: what a clear pays with fewer than three fish, and what the trial skin is and for how long <!-- case:chk-today -->
- A calendar of past or missed boards <!-- case:chk-calendar -->
- The next day: whether a new board comes when the countdown ends at midnight, and what happens to an unplayed one <!-- case:chk-next-day -->
- A missed day: what is lost <!-- case:chk-missed -->
- Playing the board: its win, its loss, what the stopwatch does <!-- case:chk-play -->

[^s1]: session 20261003-200440-chrono-2FYKPJ, step 16 — [video at 2:52](https://youtu.be/Pqx4QY-FpBA?t=172)
[^s2]: session 20261003-200440-chrono-2FYKPJ, step 4 — [video at 1:15](https://youtu.be/Pqx4QY-FpBA?t=75)
[^s3]: session 20261003-200440-chrono-2FYKPJ, step 17 — [video at 3:06](https://youtu.be/Pqx4QY-FpBA?t=186)

[^s4]: session 20261003-200440-chrono-2FYKPJ, step 18 — [video at 3:08](https://youtu.be/Pqx4QY-FpBA?t=188)
[^s5]: session 20261003-235107-chrono-2FYKPJ, step 0
