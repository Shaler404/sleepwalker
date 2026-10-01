---
game: com.oakever.akari
title: "Interstitial ads"
type: feature
feature: ads-interstitial
version_seen: 1.0.2
verified_at: 2026-10-01
sources: [20261001-003641-chrono-2FYKPJ, 20261001-024647-chrono-2FYKPJ, 20261001-035425-chrono-2FYKPJ]
---

# Interstitial ads


## How it works
- The first interstitial came on tapping "Level 16"; then on "Level 18" [s:20261001-003641-chrono-2FYKPJ#32] [s:20261001-003641-chrono-2FYKPJ#36].
- Levels 19–48: an ad after tapping the button of every even level and never before an odd one
  [s:20261001-024647-chrono-2FYKPJ#109].
- Levels 49–55 broke the pattern: ads before 50, after the Restart on 51, before 53 and 55; none
  before 49, 51, 54, and none on two starts of 52. Restart and Revive shift the phase. The rule is not
  known [s:20261001-035425-chrono-2FYKPJ#45] [s:20261001-035425-chrono-2FYKPJ#52] [s:20261001-035425-chrono-2FYKPJ#58].
- The ad is a video with "Next" at the top left after about 5 s; in levels 20–34 Next led to a second
  playable ad whose corner X opened the Play Store; from level 36 Next opened the Play Store directly;
  `launch` returns to the level [s:20261001-024647-chrono-2FYKPJ#7] [s:20261001-024647-chrono-2FYKPJ#64].
- A bottom banner is shown in levels from level 16 [s:20261001-003641-chrono-2FYKPJ#34] [s:20261001-035425-chrono-2FYKPJ#40].
- No remove-ads purchase, shop or currency anywhere through level 55 [s:20261001-035425-chrono-2FYKPJ#61].

> ⚠️ Previously (v1.0.2, 2026-10-01): "an interstitial before every even level start" (levels 16–48).
> Levels 52–54 showed this is not the rule.

## Cases
| Case | What was done | Result | Source |
|---|---|---|---|
| First ad | Level 15 → 16 | Interstitial, ends on the Play Store | [s:20261001-003641-chrono-2FYKPJ#32] |
| Even levels | Levels 19–48 | An ad before every even level | [s:20261001-024647-chrono-2FYKPJ#109] |
| Skip | Next, then the corner X or the Play Store, then `launch` | Back to the level | [s:20261001-024647-chrono-2FYKPJ#109] |
| Restart | In-level Restart | An interstitial; the phase shifts | [s:20261001-035425-chrono-2FYKPJ#61] |
| No-ads | Looked on every screen | No remove-ads purchase | [s:20261001-035425-chrono-2FYKPJ#61] |

## Not verified
- The real rule (counter, timer, both); whether an ad ever comes after a win.
