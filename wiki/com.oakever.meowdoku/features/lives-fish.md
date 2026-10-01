---
game: com.oakever.meowdoku
title: "Fish (3 mistake lives per level)"
type: feature
feature: lives-fish
version_seen: 1.18.0
verified_at: 2026-10-01
sources: [20261001-013526-chrono-2FYKPJ, 20261001-022624-chrono-2FYKPJ]
---

# Fish (3 mistake lives per level)


Three fish in the header of every level; a flawless win adds the fish left to the
[leaderboard event](fish-event.md) score [s:20260930-233055-chrono-2FYKPJ#53].

![Out of Fishes: "Remaining: N" cats to place, Get 3 Fishes (AD) and Restart](../img/20261001-out-of-fishes-9179e626.webp)

## Cases
| Case | What was done | Result | Source |
|---|---|---|---|
| Wrong cat | Double tap on a wrong cell | Orange X on the cell, fish 3 → 2, placed cats close their eyes | [s:20261001-013526-chrono-2FYKPJ#81] |
| Zero fish | Three wrong cats | "Out of Fishes": Remaining N, Get 3 Fishes (AD), Restart | [s:20261001-022624-chrono-2FYKPJ#40] |
| Refill | Get 3 Fishes | A ~30 s rewarded playable; after `launch`: 3 fish, the board and score kept | [s:20261001-022624-chrono-2FYKPJ#42] |

## Not verified
- Restart on the Out of Fishes popup.
