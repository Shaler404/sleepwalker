---
game: com.oakever.akari
title: "MeowTrail"
type: overview
version_seen: 1.0.2
verified_at: 2026-10-02
sources: [20261001-003641-chrono-2FYKPJ, 20261001-024647-chrono-2FYKPJ, 20261001-035425-chrono-2FYKPJ, 20261001-070939-chrono-2FYKPJ, 20261001-091349-chrono-2FYKPJ, 20261001-100940-chrono-2FYKPJ, 20261001-221517-chrono-2FYKPJ]
---

# MeowTrail


[Google Play](https://play.google.com/store/apps/details?id=com.oakever.akari) · version 1.0.2

A Light Up (Akari) logic puzzle with cats: place cats so every white cell is covered by a cat's row or
column, cats never see each other and numbered walls count their neighbouring cats. Around the core:
3 hearts per level, two boosters with rewarded refills, Hard levels every 10th, a rate-us prompt, a
Helpshift help center, interstitial and banner ads. No shop, currency, remove-ads purchase, daily rewards
or events through level 120.

![Home: the MEOW TRAIL logo, the gear and a single "Level N" button](img/20261001-home-be3ed0c1.webp)

## Coverage
- 16 sessions on version 1.0.2 (7 research sessions and 9 bench slots), FTUE from a fresh install and
  levels 1–120, all won with the [solver](../../solvers/com.oakever.akari/akari.py), which reads the board
  from the frame since level 83 (12–40 s a level); content does not end by level 120. Surveys 1 and 2
  done; discovery is open (daily return and push content still unchecked).
- Interstitials: the leading hypothesis is a cooldown of about 50–60 s from the last ad closing
  ([interstitial ads](features/ads-interstitial.md#how-it-works)), under test.
- Every level board the agents met: [levels.md](levels.md).
- Feature pages: [consent](features/consent.md), [tutorial](features/tutorial.md),
  [levels](features/levels.md), [hearts](features/hearts.md), [cat booster](features/booster-cat.md),
  [hint booster](features/booster-hint.md), [settings](features/settings.md),
  [help center](features/help-center.md), [interstitial ads](features/ads-interstitial.md),
  [hard levels](features/hard-levels.md), [rate us](features/rate-us.md).
- All features and cases: [features.md](features.md); tasks: [tasks.md](tasks.md).

## For the agent
[How to play](agent/playbook.md) · [routes](agent/routes.md) · [tactics](agent/tactics.md) ·
[lessons](agent/lessons.md) · [metrics](agent/metrics.md)
