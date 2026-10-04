---
game: com.oakever.arrows
title: "Daily Challenge"
type: feature
feature: daily-challenge
version_seen: 1.33.0
verified_at: 2026-10-03
sources: [20261003-200141-chrono-2FYKPJ, 20261003-232357-chrono-2FYKPJ]
---

# Daily Challenge

A daily feature shown as the third card of the Home carousel, with the current date on it ("Oct 3" on the
session day); locked until level 20 in this session, so only its card is documented [^s1].

## Why it appeared

On Home from the first launch, as a locked card "Unlock Lv.20" [^s1]. What makes it open is not verified
(Hypothesis: reaching level 20, as the card says, not verified).

## Where to find it

Home > the carousel at the top > swipe left > the third card, "Daily Challenge" [^s2] [^s1].

![Home carousel scrolled left: the Daily Challenge card (date Oct 3), button Unlock Lv.20](../img/20261003-daily-challenge-entry-ea4a3ab5.webp) [^s1]
*Home carousel scrolled left: the Daily Challenge card with the date Oct 3, button Unlock Lv.20*

## What it looks like

<!-- no-screen: locked until level 20; the session was at level 3 -->
Not seen: the feature is locked. The card is terracotta with a trophy of three stars, the title "Daily
Challenge", the date "Oct 3" under it and an "Unlock Lv.20" button [^s1].

### Locked card tooltip

![Tapping the locked Daily Challenge card shows the tooltip Unlock Daily Challenge at Level 20](../img/20261003-daily-challenge-popup-ff1f8f80.webp) [^s3]
*A tap on the locked card: the tooltip "Unlock Daily Challenge at Level 20" under it*

A tap on the locked card does not open it; a brown tooltip under the card reads "Unlock Daily Challenge
at Level 20" [^s3].

## How it works

Version 1.33.0. Locked until level 20 [^s1] [^s3]. The card shows the device's current date, Oct 3 on
the session day, in both sessions of that day [^s1] [^s3]. What a day's challenge is and what it pays was not seen.

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared <!-- case:chk-appeared --> | — | not verified: locked; the card is on Home from the first launch | [^s1] |
| The locked card: date and tooltip <!-- case:card-date --> | Tapped the locked card | ✅ The card shows today's date (Oct 3) and "Unlock Lv.20"; a tap gives the tooltip "Unlock Daily Challenge at Level 20" | [^s3] |
| Where to find it: the screen and the button that open it <!-- case:chk-entry --> | Swiped the Home carousel left | ✅ The third card, "Unlock Lv.20"; not tapped | [^s1] |
| What it looks like: its screen <!-- case:chk-screen --> | — | not verified: locked |  |
| Today's challenge: what it gives <!-- case:chk-today --> | — | not verified |  |
| The calendar: every day and its reward <!-- case:chk-calendar --> | — | not verified |  |
| The next day: what renews and when <!-- case:chk-next-day --> | — | not verified |  |
| A missed day: what is lost or reset <!-- case:chk-missed --> | — | not verified |  |
| If it is a board: play it once, its win and its loss <!-- case:chk-play --> | — | not verified |  |

## Not verified

- Why it appeared: whether reaching level 20 opens it <!-- case:chk-appeared -->
- Its screen <!-- case:chk-screen -->
- Today's challenge and what it gives <!-- case:chk-today -->
- The calendar: every day and its reward <!-- case:chk-calendar -->
- The next day: what renews and when <!-- case:chk-next-day -->
- A missed day: what is lost or reset <!-- case:chk-missed -->
- Playing a challenge: its win and its loss <!-- case:chk-play -->

[^s1]: session 20261003-200141-chrono-2FYKPJ, step 4 — [video at 1:21](https://youtu.be/l44HK-PZ5-o?t=81)

[^s2]: session 20261003-200141-chrono-2FYKPJ, step 3 — [video at 1:11](https://youtu.be/l44HK-PZ5-o?t=71)
[^s3]: session 20261003-232357-chrono-2FYKPJ, step 3 — [video at 0:39](https://youtu.be/x9mSZuHgO_4?t=39)
