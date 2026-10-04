---
game: com.oakever.meowdoku
title: "Interstitial ad at level start"
type: feature
feature: ad-interstitial
version_seen: 1.19.1
verified_at: 2026-10-03
sources: [20261003-201915-chrono-2FYKPJ, 20261003-202631-chrono-2FYKPJ]
---

# Interstitial ad at level start

A full-screen ad the player does not choose. It played when a [main level](level.md) was started from the
win screen's next-level button, and when the level was restarted from the Out of Fishes loss screen. It gives
nothing [^s1] [^s3] [^s5].

## Why it appeared

Tapping Level 128 after the L127 win: full-screen video/playable ad, 9s countdown then X [^s1].

## Where to find it

It is not opened by the player. It came after these taps:

- The next-level button on the win screen: Level 128 after Level 127, Level 130 after Level 129 [^s1] [^s3].
- Restart on the Out of Fishes screen, on Level 130 [^s5].

![Win screen of Level 129: "Immaculate", the orange Level 130 button with a Hard tag](../img/20261003-ad-interstitial-entry-91916e66.webp) [^s2]
*The win screen of Level 129: a tap on the Level 130 button played the interstitial before the level opened*

## What it looks like

![Interstitial after tapping Level 130: a full-screen video ad for another game, a skip control and mute top left, ratings on the right, an install bar at the bottom](../img/20261003-ad-interstitial-screen-a5f3dd6d.webp) [^s3]
*The interstitial after Level 129's win: a third-party game's video, a skip control and mute top left, an install bar at the bottom*

A full-screen video for another game, with a skip control and mute top left, ratings on the right and an
install bar at the bottom [^s3]. After Level 127 the video showed a 9 s countdown, then a close cross top
right, and then a playable ad [^s1].

## How it works

- When it showed (version 1.19.1, one account):
  - Win screen > next level: 2 of 2 times [^s1] [^s3].
  - Out of Fishes > Restart: 1 of 1 [^s5].
  - Not seen: Level 129 opened from the Home button with no ad [^s6]. Settings > Restart reopened the board
    with no ad [^s7]. The back arrow went straight to Home with no ad [^s8].
- Closing: after Level 127, the cross came after a 9 s countdown, but the playable part that followed did not
  close cleanly. Both times the player relaunched the app, and the next level was open with an empty board
  [^s4] [^s9].
- A tap at the top left (where the level's back arrow is) while the ad after Restart was on screen opened a
  Play Store sheet for the advertised game [^s5].
- Reward: none [^s1].

Version 1.19.1.

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Full-screen video ad, then a playable ad; 9 s countdown before the cross top right <!-- case:chk-screen --> | Level 128 started from the win screen | ✅ | [^s1] |
| Interstitial (video, then a playable end card) shown when the next level starts <!-- case:chk-kind --> | Levels 128 and 130 started from the win screen | ✅ | [^s1] [^s3] |
| 9 s countdown, then the cross; the playable part did not close cleanly, the app was relaunched to get out <!-- case:chk-close --> | App relaunched | ✅ | [^s4] |
| Not a rewarded placement: gives nothing <!-- case:chk-reward --> | Nothing given after it | ✅ | [^s1] |
| An interstitial video also plays after Out of Fishes > Restart; a tap at the top left hit the ad and opened a Play Store sheet <!-- case:after-retry --> | Restart on Out of Fishes, then the back arrow's spot tapped | ✅ | [^s5] |
| Why it appeared: the trigger that brought it up (the first launch, a level won, a threshold, a timer, a loss): a fact with its frame, or a hypothesis to test <!-- case:chk-appeared --> | After tapping Level 128 on the win screen | ✅ | [^s1] |

## Not verified

- Where to find it: every action that triggers it; seen after the win screen's next-level button and Out of Fishes > Restart, not after the Home Level button, Settings > Restart or the back arrow <!-- case:chk-entry -->
- How often it shows: every win, every Nth level or a cooldown; three levels in a row were not played to test it <!-- case:chk-frequency -->

[^s1]: session 20261003-201915-chrono-2FYKPJ, step 10 — [video at 3:16](https://youtu.be/ffhYgQE4LvU?t=196)
[^s2]: session 20261003-202631-chrono-2FYKPJ, step 6 — [video at 1:30](https://youtu.be/3-USmjAyOV8?t=90)
[^s3]: session 20261003-202631-chrono-2FYKPJ, step 7 — [video at 1:41](https://youtu.be/3-USmjAyOV8?t=101)
[^s4]: session 20261003-201915-chrono-2FYKPJ, step 11 — [video at 4:04](https://youtu.be/ffhYgQE4LvU?t=244)
[^s5]: session 20261003-202631-chrono-2FYKPJ, step 19 — [video at 6:01](https://youtu.be/3-USmjAyOV8?t=361)
[^s6]: session 20261003-202631-chrono-2FYKPJ, step 1 — [video at 0:31](https://youtu.be/3-USmjAyOV8?t=31)
[^s7]: session 20261003-202631-chrono-2FYKPJ, step 15 — [video at 5:05](https://youtu.be/3-USmjAyOV8?t=305)
[^s8]: session 20261003-202631-chrono-2FYKPJ, step 21 — [video at 6:40](https://youtu.be/3-USmjAyOV8?t=400)
[^s9]: session 20261003-202631-chrono-2FYKPJ, step 8 — [video at 2:06](https://youtu.be/3-USmjAyOV8?t=126)
