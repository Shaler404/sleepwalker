---
game: com.maroieqrwlk.unpin
title: "Level path header"
type: feature
feature: level-path
version_seen: 241.5.1
verified_at: 2026-10-03
sources: [20261003-193015-chrono-2FYKPJ]
---

# Level path header

A row of numbered circles at the top of the level screen showing the previous, the current and the next
level. It is the only progress display on the level screen: the game has no level map [^s1].

## Why it appeared

Level screen header: previous, current, next level circles [^s1].

## Where to find it

The top of the level screen, between the gear (Settings) and the restart button; it is on every level
[^s1] [^s2].

![The level 2 screen: circles 1 (with a green tick), 2 (large) and 3 between the gear and restart](../img/20261003-level-path-entry-e0b44bb6.webp) [^s2]
*The level path between the gear and restart: 1 done, 2 current, 3 next*

## What it looks like

![Level 2 just won: the header still shows 1, 2, 3 with 2 as the current level](../img/20261003-level-path-screen-b3c43bcc.webp) [^s3]
*Level 2 won, before the win screen: the header is unchanged until the next level opens*

The current level is a large circle with a bold number; the next level a smaller circle to its right, the
previous one a smaller circle to its left with a green tick; dotted lines join them [^s2]. On level 1
only two circles show, 1 (current) and 2 (next) [^s4].

## How it works

Version 241.5.1. The circles are not buttons in this session's play (none was tapped). The header moves on
by one level when the next level opens [^s4] [^s2].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Always shown in the level screen header <!-- case:chk-entry --> | Played levels 1 and 2 | ✅ On both levels | [^s1] |
| Previous (checked), current, next level circles between gear and restart <!-- case:chk-screen --> | Played levels 1 and 2 | ✅ 1 → 2 on level 1; 1 ✓ → 2 → 3 on level 2 | [^s1] |
| Why it appeared <!-- case:chk-appeared --> | First launch | ✅ On the level screen from level 1 | [^s1] |
| Every entry point on it <!-- case:chk-entries --> | — | not verified: the circles were not tapped |  |
| Badges, timers and counters on it <!-- case:chk-badges --> | — | not verified: none seen on levels 1–2 |  |
| What changes on it with progress <!-- case:chk-changes --> | Levels 1–2 | not verified: only levels 1–2 seen |  |

## Not verified

- Every entry point on it: whether a circle can be tapped <!-- case:chk-entries -->
- Badges, timers and counters on it <!-- case:chk-badges -->
- What changes on it with progress (special level markers, a theme) <!-- case:chk-changes -->

[^s1]: session 20261003-193015-chrono-2FYKPJ, step 5 — [video at 1:53](https://youtu.be/JjeHh2uiLgE?t=113)
[^s2]: session 20261003-193015-chrono-2FYKPJ, step 4 — [video at 1:43](https://youtu.be/JjeHh2uiLgE?t=103)
[^s3]: session 20261003-193015-chrono-2FYKPJ, step 7 — [video at 2:25](https://youtu.be/JjeHh2uiLgE?t=145)
[^s4]: session 20261003-193015-chrono-2FYKPJ, step 2 — [video at 0:55](https://youtu.be/JjeHh2uiLgE?t=55)
