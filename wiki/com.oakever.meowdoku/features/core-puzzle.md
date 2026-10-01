---
game: com.oakever.meowdoku
title: "Core puzzle (Queens-like)"
type: feature
feature: core-puzzle
version_seen: 1.18.0
verified_at: 2026-10-01
sources: [20260930-233055-chrono-2FYKPJ, 20261001-013526-chrono-2FYKPJ]
---

# Core puzzle (Queens-like)


An N×N board split into N colour regions; place N cats: one per region, one per row, one per column,
and no two cats touching, diagonals included [s:20260930-233055-chrono-2FYKPJ#9]. The rules strip on the level screen reads
"1 Cat per color", "1 Cat per column and row", "Cats cannot touch".

![Level 1: rules strip, 3 fish, the cat and hint boosters at 5 and a slot locked until level 21](../img/20261001-level-1-board-eac19530.webp)

## How it works
- Board sizes grow from 4x4 (level 1) to 10x10 (from level 12); most levels have one cat already
  placed [s:20260930-233055-chrono-2FYKPJ#59] [s:20261001-013526-chrono-2FYKPJ#3].
- Hard levels from level 30: a flame + "Hard" in the header and a Hard tag on the previous win
  screen's button; the same rules [s:20261001-013526-chrono-2FYKPJ#67].
- A level can open with a toast comparing the player: "Zero mistakes! You're in the top 8.8%", "No
  tools used! ... ahead of 78.5%" [s:20260930-233055-chrono-2FYKPJ#51] [s:20260930-233055-chrono-2FYKPJ#113].
- The score grows with each correct cat (level 1: 2016; level 12: 8640); the formula is unknown
  [s:20260930-233055-chrono-2FYKPJ#14] [s:20260930-233055-chrono-2FYKPJ#59].

## Cases
| Case | What was done | Result | Source |
|---|---|---|---|
| Rules | Tutorial and levels 1–43 | As above | [s:20260930-233055-chrono-2FYKPJ#9] |
| Hard | Level 30 and 40 | Flame + Hard, same rules | [s:20261001-013526-chrono-2FYKPJ#67] |
| Level-start toast | Levels 11 and 21 | Percentile toasts | [s:20260930-233055-chrono-2FYKPJ#51] |

## Not verified
- The score formula; what the toasts depend on.
