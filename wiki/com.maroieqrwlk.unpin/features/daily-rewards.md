---
game: com.maroieqrwlk.unpin
title: "Daily Rewards"
type: feature
feature: daily-rewards
version_seen: 241.5.1
verified_at: 2026-10-03
sources: [20261003-203702-chrono-2FYKPJ, 20261003-214021-chrono-2FYKPJ]
---

# Daily Rewards

A seven-day login calendar: days 1-6 pay coins (+25 up to +500), day 7 gift boxes. It comes up by itself as a
popup over the map, once a day; the player claims the day's reward with **Claim** [^s1] [^s3] [^s4]. There is
no button that opens it [^s4].

## Why it appeared

Popup on the second Play! tap on the map after the L3 win (first map visit) [^s1].

## Where to find it

It opens by itself: after the level 3 win the map appeared; the first tap on **Play!** brought the map
tutorial, the second the Daily Rewards popup instead of level 4 [^s2] [^s1]. The map has no button for it:
at level 10 the map shows the gear, ADS, the league button, the jar, the chest and the Collections box, and
none of them is Daily Rewards [^s4]. On a relaunch the same day (21:40, the first popup was at 20:37) the
popup did not come again, neither at launch nor on a later return to the map [^s4].

![Map after the L3 win: Play!, whose second tap brought the Daily Rewards popup](../img/20261003-daily-rewards-entry-8cb2cb37.webp) [^s2]
*The map after the level 3 win: Play!, whose second tap brought the Daily Rewards popup*

![The map at level 10 on a later visit the same day: no popup, and no Daily Rewards button among the map's buttons](../img/20261003-daily-rewards-entry-cdb2ec35.webp) [^s4]
*The map at level 10, same day: gear and ADS top right, the league button, the jar and the chest on the sides, the Collections box right of Play!; no Daily Rewards button (the player's name in the league banner blacked out)*

## What it looks like

![Daily Rewards: days 1-6 coins +25/+50/+100/+150/+250/+500, day 7 gift boxes, Claim](../img/20261003-daily-rewards-screen-e9b6cab4.webp) [^s1]
*Daily Rewards: a calendar icon, days 1-6 with coins, day 7 with gift boxes, the green Claim button*

A calendar icon and the title **Daily Rewards**, a grid of six coin tiles (Day 1 to Day 6) and a wide pink
Day 7 tile with gift boxes, then a green **Claim** button [^s1]. The day that can be claimed is labelled
**Claim!** instead of its day number [^s1].

### Result

![After Claim: day 1 ticked green, coins fly to the balance 102 at top right](../img/20261003-daily-rewards-result-e9b6cab8.webp) [^s3]
*After Claim: the Day 1 tile turns green with a tick; coins fly to the balance top right (102 mid-count)*

![Claim on day 1: the tile is ticked, coins fly to the balance, the popup gives way to level 4](../clips/20261003-daily-rewards-claim-day1.webp) [^s3]
*Clip 3 s · [original on YouTube from 2:29](https://youtu.be/cirqlD7KGWI?t=149); after Claim the game goes straight to level 4*

## How it works

Version 241.5.1.

| Day | Reward |
|---|---|
| 1 | +25 coins |
| 2 | +50 coins |
| 3 | +100 coins |
| 4 | +150 coins |
| 5 | +250 coins |
| 6 | +500 coins |
| 7 | Gift boxes (contents not shown) |

Source: [^s1]. Claim on day 1 credited +25 (balance 79 before, 102 shown while counting, 122 after the level
4 win of +18) and opened level 4 [^s3]. Inferred: the balance after the claim was 104.

It shows once per day: the first map visit of the day brings it; a relaunch of the app the same day did not
[^s4]. It is a popup, not a board to play [^s4].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Claim day 1: +25 coins (79 -> 102 shown), day 1 ticked <!-- case:claim-day1 --> | Tapped Claim | ✅ +25 coins, Day 1 ticked | [^s3] |
| 7-day calendar: d1 +25, d2 +50, d3 +100, d4 +150, d5 +250, d6 +500 coins, d7 gift boxes <!-- case:chk-calendar --> | Read the popup | ✅ Seen | [^s1] |
| Day 1 claimed with Claim: +25 coins, day ticked <!-- case:chk-today --> | Tapped Claim | ✅ Credited | [^s3] |
| Daily Rewards popup over the map with the 7-day calendar and Claim <!-- case:chk-screen --> | Tapped Play! twice on the first map | ✅ Popup seen | [^s1] |
| Why it appeared <!-- case:chk-appeared --> | Tapped Play! twice on the first map | ✅ Opened by itself on the second tap | [^s1] |
| No button: the popup opens by itself on the first map visit of a day (day 1 at 20:37); a relaunch the same day (21:40) did not show it again <!-- case:chk-entry --> | Relaunched the app the same day, played, returned to the map | ✅ No popup and no button for it | [^s4] |
| The next day <!-- case:chk-next-day --> | — | not verified: needs a session on the next day |  |
| A missed day <!-- case:chk-missed --> | — | not verified |  |
| Not a board: a calendar popup only <!-- case:chk-play --> | Read the popup | ✅ A calendar with Claim, nothing to play | [^s4] |

## Not verified

- The next day: whether day 2 (+50) opens the next calendar day and when (follow-up task daily-rewards-d2-d1) <!-- case:chk-next-day -->
- A missed day: whether the streak resets (follow-up task daily-rewards-missed, not before 5 October) <!-- case:chk-missed -->
- What the day 7 gift boxes hold.

[^s1]: session 20261003-203702-chrono-2FYKPJ, step 8 — [video at 2:20](https://youtu.be/cirqlD7KGWI?t=140)
[^s2]: session 20261003-203702-chrono-2FYKPJ, step 7 — [video at 2:10](https://youtu.be/cirqlD7KGWI?t=130)
[^s3]: session 20261003-203702-chrono-2FYKPJ, step 9 — [video at 2:32](https://youtu.be/cirqlD7KGWI?t=152)
[^s4]: session 20261003-214021-chrono-2FYKPJ, step 30 — [video at 7:39](https://youtu.be/siJO2QCuGxI?t=459)
