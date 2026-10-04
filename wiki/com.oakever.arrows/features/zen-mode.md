---
game: com.oakever.arrows
title: "Zen Mode toggle"
type: feature
feature: zen-mode
version_seen: 1.33.0
verified_at: 2026-10-03
sources: [20261003-200141-chrono-2FYKPJ]
---

# Zen Mode toggle

A toggle in Settings named "Zen Mode", with a lotus icon, off by default [^s1]. It is a mode switch for
the levels, not a separate screen (inferred: it sits among the Settings toggles). Its effect was not tested
in this session.

## Why it appeared

In Settings from the first launch, with no lock [^s1]. Hypothesis: it changes how levels are played (the
name suggests a relaxed variant, for example without a fail condition), not verified.

## Where to find it

Home > the gear top right > Settings > the fifth row of the first block, "Zen Mode" [^s1].

![Settings: the Zen Mode toggle (lotus icon), fifth row, off by default](../img/20261003-zen-mode-entry-9a5a2f35.webp) [^s1]
*Settings: the Zen Mode toggle (lotus icon), fifth row, off by default*

## What it looks like

<!-- no-screen: the toggle was not switched on and no level was played -->
Only the toggle was seen: a grey switch, off, next to a lotus icon [^s1].

## How it works

Version 1.33.0. Off by default [^s1]. What it changes in a level is not verified (experiment exp-zen:
switch it on, play a level, compare mistakes, timer and stars with normal play).

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared <!-- case:chk-appeared --> | Opened Settings | in Settings from the start; what it does is a hypothesis | [^s1] |
| Where to find it: the screen and the button that open it <!-- case:chk-entry --> | Opened Settings | ✅ Fifth row, "Zen Mode", off | [^s1] |
| What it looks like: its screen <!-- case:chk-screen --> | — | not verified: not switched on |  |
| Rules: the goal and how it differs from the core game <!-- case:chk-rules --> | — | not verified |  |
| A win: its screen and what it pays <!-- case:chk-win --> | — | not verified |  |
| A loss: its screen, what it costs and the retry offers <!-- case:chk-loss --> | — | not verified |  |
| Progression inside the mode <!-- case:chk-progression --> | — | not verified |  |
| Limits <!-- case:chk-limits --> | — | not verified: the toggle shows no lock or price | [^s1] |

## Not verified

- Why it appeared: what the toggle does <!-- case:chk-appeared -->
- A level with Zen Mode on <!-- case:chk-screen -->
- Rules: how a level differs with Zen Mode on (exp-zen) <!-- case:chk-rules -->
- A win with Zen Mode on <!-- case:chk-win -->
- A loss with Zen Mode on, or whether a loss is possible <!-- case:chk-loss -->
- Progression with Zen Mode on: whether levels and stars count <!-- case:chk-progression -->
- Limits: attempts, a timer or a price <!-- case:chk-limits -->

[^s1]: session 20261003-200141-chrono-2FYKPJ, step 5 — [video at 1:32](https://youtu.be/l44HK-PZ5-o?t=92)
