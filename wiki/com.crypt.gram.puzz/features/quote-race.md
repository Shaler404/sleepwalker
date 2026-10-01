---
game: com.crypt.gram.puzz
title: Quote Race
type: feature
feature: quote-race
version_seen: 3.6.1
verified_at: 2026-10-01
sources: [20261001-020937-chrono-2FYKPJ]
---

# Quote Race

A timed race event against four opponents: the first to win 10 levels finishes first. It popped up on
launch at level 9 of a progressed install. Route: [routes](../agent/routes.md#quote-race).

## How it works

- On launch a popup announces the event: "Solve 10 levels faster than your opponents to finish the
  race in 1st place", a timer of 11h 59m and a GO button [s:20261001-020937-chrono-2FYKPJ#0].
- GO opens the race screen with a one-time tutorial overlay ("EVENT … Complete levels / Tap to
  continue") [s:20261001-020937-chrono-2FYKPJ#1].
- The race screen shows five racers on pedestals with their level counts (all 0 at the start) and
  their places 1–5; the player ("Me", marked YOU) started third, so the starting order is preset
  [s:20261001-020937-chrono-2FYKPJ#2]. A chest on the right, an (i) button at the top right, and PLAY at the bottom start the
  next level [s:20261001-020937-chrono-2FYKPJ#2] [s:20261001-020937-chrono-2FYKPJ#3].
- PLAY was followed by an interstitial ad before the level opened [s:20261001-020937-chrono-2FYKPJ#3].

![Quote Race popup on launch: "The event has started!", 11h 59m timer, "Solve 10 levels faster than your opponents to finish the race in 1st place", GO](../img/20261001-quote-race-popup-c1176e3d.webp)

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Event popup | Launched the game at level 9 | Popup with the rule, 11h 59m timer, GO | [s:20261001-020937-chrono-2FYKPJ#0] |
| Join | Tapped GO | Race screen, 5 racers, the player third at 0 levels | [s:20261001-020937-chrono-2FYKPJ#1] |

## Numbers (v3.6.1)

| What | Value | Source |
|---|---|---|
| Levels to finish | 10 | [s:20261001-020937-chrono-2FYKPJ#0] |
| Duration seen at the start | 11h 59m | [s:20261001-020937-chrono-2FYKPJ#0] |
| Opponents | 4 | [s:20261001-020937-chrono-2FYKPJ#2] |

## Not verified

- The (i) rules screen and the chest preview of the reward.
- Whether a won level moves the player's counter to 1, and how the opponents advance.
- The finish, placement and reward; what happens when the timer ends.
- Whether the right-side widget on the main screen (laurel badge "3" with a timer) is the race
  entry point (probable: it matches the race rank and timer) [s:20261001-020937-chrono-2FYKPJ#0].
