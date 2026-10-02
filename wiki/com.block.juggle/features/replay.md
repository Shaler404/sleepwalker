---
game: com.block.juggle
title: "Replay (restart game)"
type: feature
feature: replay
version_seen: 10.6.5
verified_at: 2026-10-01
sources: [20261001-200952-chrono-2FYKPJ]
---

# Replay (restart game)

Replay throws away the current classic game and starts a new one on an empty board. It is the only way
to start over without filling the board, and the best score survives it [^s2].

## Where to find it

From the classic board: the gear at the top right, then the green Replay button, third in the Settings
popup [^s1].

![Settings popup: the Replay button restarts the classic game](../img/20261001-replay-entry-c1b83ec7.webp) [^s1]

## What it looks like

There is no confirmation: tapping Replay goes straight to a full-screen interstitial ad
(see [Interstitial ads](ads.md)) [^s3]. After it, the classic screen
comes back with an empty 8x8 board, a score of 0, a new tray of three pieces and the old best score
(261) next to the crown [^s2].

![After Replay: a fresh empty board with score 0; the best score (crown) is kept](../img/20261001-replay-screen-be69c090.webp) [^s2]

## How it works

- No "are you sure" step: the tap itself ends the game [^s3].
- An interstitial ad plays before the new board [^s3].
- The best score is kept; the current score goes back to 0 [^s2].
- In this session the ad could not be closed, so the app was restarted; the new board after the restart
  is what Replay had started (version 10.6.5) [^s4] [^s2]. Whether the new
  board appears without a restart when the ad closes normally is not verified.

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Replay from settings restarts the game after an interstitial ad; best score kept | Gear, Replay, waited out the ad, restarted the app | ⏳ Not verified: the empty board (score 0, best 261 kept) was seen only after an app restart | [^s2] |

## Not verified

- Whether the board restarts by itself once the ad is closed, without restarting the app.
- Whether Replay always shows an ad or only sometimes.

[^s1]: session 20261001-200952-chrono-2FYKPJ, step 38 — [video at 8:08](https://youtu.be/1AkjzicKdRM?t=488)
[^s2]: session 20261001-200952-chrono-2FYKPJ, step 42 — [video at 10:02](https://youtu.be/1AkjzicKdRM?t=602)
[^s3]: session 20261001-200952-chrono-2FYKPJ, step 39 — [video at 8:12](https://youtu.be/1AkjzicKdRM?t=492)
[^s4]: session 20261001-200952-chrono-2FYKPJ, step 41 — [video at 9:55](https://youtu.be/1AkjzicKdRM?t=595)
