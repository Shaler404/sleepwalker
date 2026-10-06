---
game: com.oakever.akari
title: "Interstitial ads"
type: feature
feature: interstitial-ad
version_seen: 1.0.2
verified_at: 2026-10-06
sources: [20261005-080420-chrono-2FYKPJ, 20261005-141041-chrono-2FYKPJ, 20261006-002027-chrono-2FYKPJ, 20261006-023308-chrono-2FYKPJ]
---

# Interstitial ads

A full-screen video ad for another app that plays by itself between the win screen and the next level. From Level 16 on it came on every second level start, counting starts from the win screen, from Home and the Restart button in a level's Settings; it has no close cross, ends on its own in the Play Store, and gives nothing (version 1.0.2) [^s1] [^s5] [^s11].

## Why it appeared

First on tapping Level 16 on the win screen of Level 15; the level starts of Levels 4 to 15 had none. That first one was a Flyfox Game video ad with an Open Store button, after which Level 16 opened [^s1].

## Where to find it

No control opens it on purpose. It plays when a level starts, on every second start (from Level 16 on): after the orange Level N button on a win screen, the Level N button on Home, or Restart in the Settings sheet opened from a level ([Akari level](core-level.md)); it was also seen after Restart on the Almost! screen (see [Hearts](hearts.md)) [^s1] [^s5] [^s10] [^s11].

![Win screen of Level 21: PERFECT! over the solved board, the orange Level 22 button below](../img/20261005-interstitial-ad-entry-c3683c97.webp) [^s2]
*The win screen's Level 22 button: tapping it played an interstitial before Level 22*

## What it looks like

A full-screen video of another game (here a ring puzzle). An "Open Store" button sits at the top right; at the bottom are a sound icon, an "i", a Google Play badge, the app's icon with a blue Install Now button, and a thin blue progress bar along the very bottom [^s3].

![Interstitial before Level 22: a ring-puzzle video with Open Store at the top right, Install Now and a Google Play badge at the bottom, the progress bar under them](../img/20261005-interstitial-ad-screen-ac2611c3.webp) [^s3]
*The ad a few seconds in; Open Store at the top right, the progress bar at the bottom. The phone's navigation bar is blacked out*

The ad before Level 24 was the same advertiser with a different video ("IQ = ?" over coloured rings) and a full-width Google Play / Install strip at the bottom [^s5].

## What you can do

| Tab or button | What it does |
|---|---|
| [Open Store](#open-store) | Not tapped |
| [Install Now](#install-now) | Not tapped |

### Open Store

<!-- no-frame: the button is on the frame above -->

The button at the top right with a skip-like arrow. Not tapped; the ad reached the Play Store by itself anyway (see How it works) [^s5].

### Install Now

<!-- no-frame: the button is on the frame above -->

The blue button next to the advertised app's icon. Not tapped.

## How it works

- Starts from the win screen's Level N button, in session 20261005-141041 and the one before: Levels 16, 18, 20, 22 and 24 had an ad; Levels 17, 19, 21 and 23 had none. Every even level, over five pairs (version 1.0.2) [^s5].
- Level 21 started from Home's Level 21 button had no ad [^s5]; Level 21 is odd, so this does not show whether Home starts are exempt.
- A later session started Level 26 from Home, then Levels 27 to 30 from the win screens: Levels 27 and 29 (odd) had an ad, Levels 28 and 30 none [^s6] [^s7] [^s8] [^s9]. So the rule is not the level's parity.
- Restart in a level's Settings sheet counts as a start: on Level 30 (opened from Home without an ad) the Restart tap went straight to an interstitial, with no confirmation before it [^s10].
- After that Restart ad, the next starts went: Level 31 from the win screen, no ad; Level 32, ad; Level 33, none; Level 34, ad; Level 34 again from Home (after the back arrow), none; Level 35 from the win screen, ad [^s11]. The Home start took a place in the alternation: had only win-screen starts counted, Level 35 would have had no ad. Rule seen: an ad on every second level start of any route, never two in a row (version 1.0.2).
- The starts in that run were 1 to 2 minutes apart; a time cooldown was not separated from the start count [^s11].
- No close cross appeared in about 20 to 28 s on either of the two ads watched (before Levels 22 and 24) [^s5].
- Both times the ad ended by itself in the Play Store, outside the game; opening the game again returned to the level that was about to start [^s5].
- One earlier ad (the Level 20 start) also ended in the Play Store and needed the game to be opened again [^s4].
- Not rewarded and no offer before it; the game's rewarded videos are the AD badge on the [Boosters](boosters.md) and Revive on the Almost! screen [^s1].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared <!-- case:chk-appeared --> | Played Levels 4 to 16 | First on tapping Level 16 after winning Level 15; none on level starts 4-15 | ✅ [^s1] |
| Where to find it <!-- case:chk-entry --> | — | No entry: it plays on its own when a level opens from the win screen's Level N button (16, 18, 20) and after Restart on the Almost! screen | ✅ [^s1] |
| What it looks like <!-- case:chk-screen --> | Watched the ad | Full-screen video ad, Open Store top right, Install Now and Google Play badges, progress bar at the bottom | ✅ [^s1] [^s3] |
| Kind of placement <!-- case:chk-kind --> | Watched the Level 20 start | Interstitial video before a level starts; this one ended in the Play Store and needed the game opened again | ✅ [^s4] |
| Reward <!-- case:chk-reward --> | — | Does not apply: not rewarded, no offer screen before it | ✅ [^s1] |
| How often <!-- case:chk-frequency --> | Started Levels 16 to 24 from the win screen; later Levels 27 to 30; then a Restart from Settings on Level 30, Levels 31 to 35 from the win screen and Level 34 once more from Home | Ad before 16, 18, 20, 22, 24, 27, 29; none before 17, 19, 21, 23, 28, 30. After the Restart ad: 31 none, 32 ad, 33 none, 34 ad, 34 from Home none, 35 ad. Every second level start of any route (win screen, Home, in-level Restart); not the level's parity | ✅ [^s5] [^s6] [^s7] [^s10] [^s11] |
| Close <!-- case:chk-close --> | Waited through the ads before Levels 22 and 24 | No close cross in about 20-28 s; the ad ends by itself in the Play Store; opening the game returns to the level | ✅ [^s5] |

## Not verified

- Open Store and Install Now were not tapped.
- Whether a time cooldown also plays a part (the starts seen were 1 to 2 minutes apart).

[^s1]: session 20261005-080420-chrono-2FYKPJ, step 41 — [video at 13:08](https://youtu.be/bJ144EFaJEE?t=788)
[^s2]: session 20261005-141041-chrono-2FYKPJ, step 2 — [video at 0:51](https://youtu.be/Bb-2kjuzPgA?t=51)
[^s3]: session 20261005-141041-chrono-2FYKPJ, step 3 — [video at 1:12](https://youtu.be/Bb-2kjuzPgA?t=72)
[^s4]: session 20261005-080420-chrono-2FYKPJ, step 51 — [video at 17:08](https://youtu.be/bJ144EFaJEE?t=1028)
[^s5]: session 20261005-141041-chrono-2FYKPJ, step 9 — [video at 4:36](https://youtu.be/Bb-2kjuzPgA?t=276)

[^s6]: session 20261006-002027-chrono-2FYKPJ, step 12 — [video at 3:00](https://youtu.be/u0n3VnemzrQ?t=180)
[^s7]: session 20261006-002027-chrono-2FYKPJ, step 17 — [video at 4:57](https://youtu.be/u0n3VnemzrQ?t=297)
[^s8]: session 20261006-002027-chrono-2FYKPJ, step 15 — [video at 4:19](https://youtu.be/u0n3VnemzrQ?t=259)
[^s9]: session 20261006-002027-chrono-2FYKPJ, step 20 — [video at 6:15](https://youtu.be/u0n3VnemzrQ?t=375)
[^s10]: session 20261006-023308-chrono-2FYKPJ, step 4 — [video at 1:01](https://youtu.be/bbcco3ENaxU?t=61)
[^s11]: session 20261006-023308-chrono-2FYKPJ, step 20 — [video at 8:59](https://youtu.be/bbcco3ENaxU?t=539)
