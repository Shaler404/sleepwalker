---
game: com.oakever.meowdoku
title: "Meowdoku: Brain Puzzle Games"
type: overview
version_seen: 1.18.0
verified_at: 2026-10-02
sources: [20260930-233055-chrono-2FYKPJ, 20261001-013526-chrono-2FYKPJ, 20261001-022624-chrono-2FYKPJ, 20261001-060942-chrono-2FYKPJ, 20261001-082114-chrono-2FYKPJ, 20261001-093348-chrono-2FYKPJ, 20261001-115413-chrono-2FYKPJ, 20261001-223249-chrono-2FYKPJ]
---

# Meowdoku: Brain Puzzle Games


[Google Play](https://play.google.com/store/apps/details?id=com.oakever.meowdoku) · version 1.18.0

A Queens-like logic puzzle with cats on colour regions. Around the core: 3 fish (mistake lives) per
level, three boosters, a daily streak, a Daily Challenge from level 21, a fish leaderboard event from
level 10, a Golden Fish bonus board offered every fourth level from 54, a profile with avatars and
frames, win titles, Hard levels from 30, a Helpshift support center, ads. No shop, currency or
remove-ads purchase seen through level 126.

## Coverage
- 16 sessions on this machine (8 of them bench slots), FTUE from a fresh install and levels 1–126, all
  won with the [solver](../../solvers/com.oakever.meowdoku/queens.py) or its drawn solution placed in one
  batch; surveys 1 and 2 done; discovery is open.
- 21 features, 16 with a page; 46 of 59 cases verified. Waiting: the streak days, the Daily Challenge
  next day, the fish event end, the next-day check of a pending Golden Fish.
- Feature pages: [tutorial](features/tutorial.md), [core puzzle](features/core-puzzle.md),
  [hint](features/hint.md), [cat booster](features/booster-cat.md), [mouse booster](features/booster-lv21.md),
  [fish](features/lives-fish.md), [settings](features/settings.md), [streak](features/streak.md),
  [Daily Challenge](features/daily-challenge.md), [fish event](features/fish-event.md),
  [win titles](features/win-rank.md), [Golden Fish board](features/golden-fish-level.md),
  [level-start banner](features/level-start-banner.md), [ads](features/ads.md),
  [rate us](features/rate-us.md), [home](features/home.md).
- Every level met: [levels.md](levels.md).
- All features and cases: [features.md](features.md); tasks: [tasks.md](tasks.md).

## For the agent
[How to play](agent/playbook.md) · [routes](agent/routes.md) · [tactics](agent/tactics.md) ·
[lessons](agent/lessons.md) · [metrics](agent/metrics.md)
