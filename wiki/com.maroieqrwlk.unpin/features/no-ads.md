---
game: com.maroieqrwlk.unpin
title: "Remove ads (No ADS)"
type: feature
feature: no-ads
version_seen: 241.3.1
verified_at: 2026-09-30
sources: [20260930-192115-chrono-2FYKPJ]
---

# Remove ads (No ADS)

> Recheck on v241.5.1: documented on 241.3.1; Google Play has 241.5.1.


No ADS button at the top right of the level screen (670,268 in the 730-px frame) [s:20260930-192115-chrono-2FYKPJ#21].

## Cases
| Case | What was done | Result | Source |
|---|---|---|---|
| Open the offer | Tapped No ADS | Straight to the Google Play payment sheet "Remove Ads", RSD 999, with 1-tap buy; no in-game screen first | [s:20260930-192115-chrono-2FYKPJ#22] |
| Cancel | Backed out of the sheet | Popup "Purchase Failed! Error: user_cancelled" (the raw error code is shown to the player); nothing bought | [s:20260930-192115-chrono-2FYKPJ#22] |

**Agent: never tap No ADS** — it opens a real purchase sheet.
