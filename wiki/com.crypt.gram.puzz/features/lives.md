---
game: com.crypt.gram.puzz
title: "Lives (hearts)"
type: feature
feature: lives
version_seen: 3.6.1
verified_at: 2026-10-03
sources: [20261003-201504-chrono-2FYKPJ]
---

# Lives (hearts)

Lives shown as a heart with a number on the home screen. A fresh install of 3.6.1 starts with 5 lives, marked FULL [^s1]. What spends a life and how lives come back was not seen.

## Why it appeared

The counter is at the top left of the home screen from the first launch, showing 5 and FULL [^s1].

## Where to find it

Home screen > the lives counter at the top left: a red heart with the number of lives and the word FULL [^s2].

![The home screen with the lives counter at the top left: a heart with 5 and FULL](../img/20261003-lives-entry-a5930d29.webp) [^s2]
*The lives counter at the top left of home: a heart with 5 and FULL*

## What it looks like

<!-- no-screen: a tap on the counter with 5/5 lives opens nothing; no lives screen or refill offer was seen -->

Only the counter was seen; with full lives a tap opens no screen [^s2].

## How it works

- Starting balance on a fresh install: 5, shown as FULL (3.6.1) [^s1].
- Inferred from FULL at 5, not verified: 5 is the maximum.

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Tap the counter with full lives <!-- case:tap-full --> | Tapped the lives counter with 5/5 FULL | Nothing opens | [^s2] |
| Why it appeared <!-- case:chk-appeared --> | First launch of a fresh install | The counter shows 5 FULL | [^s1] |
| Where to find it <!-- case:chk-entry --> | — | not verified |  |
| What it looks like <!-- case:chk-screen --> | — | not verified |  |
| What one life does <!-- case:chk-effect --> | — | not verified |  |
| The balance <!-- case:chk-balance --> | — | not verified |  |
| Sources <!-- case:chk-sources --> | — | not verified |  |
| Sinks <!-- case:chk-sinks --> | — | not verified |  |
| At zero <!-- case:chk-empty --> | — | not verified |  |
| Refill timer <!-- case:chk-refill --> | — | not verified |  |

## Not verified

- Where to find it: whether the counter opens anything when lives are not full <!-- case:chk-entry -->
- What it looks like: a lives screen or refill popup <!-- case:chk-screen -->
- What one life does (inferred: spent on a lost level; not seen) <!-- case:chk-effect -->
- The balance: the starting 5 was seen; whether it also shows in a level <!-- case:chk-balance -->
- Sources: every way to get lives <!-- case:chk-sources -->
- Sinks: what spends a life <!-- case:chk-sinks -->
- At zero: what happens and the refill offers <!-- case:chk-empty -->
- Refill timer: time per life and the maximum <!-- case:chk-refill -->

[^s1]: session 20261003-201504-chrono-2FYKPJ, step 1 — [video at 0:12](https://youtu.be/D5rsIC9WNT8?t=12)
[^s2]: session 20261003-201504-chrono-2FYKPJ, step 8 — [video at 2:11](https://youtu.be/D5rsIC9WNT8?t=131)
