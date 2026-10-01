---
game: com.crypt.gram.puzz
title: Interstitial ads
type: feature
feature: interstitial-ads
version_seen: 3.6.1
verified_at: 2026-10-01
sources: [20261001-020937-chrono-2FYKPJ, 20261001-050941-chrono-2FYKPJ, 20261001-071926-chrono-2FYKPJ, 20261001-092740-chrono-2FYKPJ, 20261001-114433-chrono-2FYKPJ]
---

# Interstitial ads

Full-screen ads for other games that the game shows on its own, without the player asking: when a
level starts, after a level is won and sometimes in the middle of a level [^s2] [^s10]
[^s11]. They usually start as a video of about 35 s and then turn
into a playable demo of the advertised game [^s8]. Some of them can be
left with the skip icon and the Play Store sheet it opens; others have no working close control at
all, and only restarting the game gets out [^s9] [^s12]. Unlike the
REVIVE and CLAIM ×3 buttons (rewarded ads), they give nothing.

## Where to find it

<!-- no-entry: an interstitial has no button of its own; it is shown when the player taps a button that starts or ends a level. The frames show the buttons after which it appeared. -->

The most common moment is the tap on PLAY on the Quote Race screen (or CONTINUE LEVEL / START LEVEL on
the main screen): the ad plays before the level opens [^s2] [^s13]
[^s14].

![Quote Race screen: PLAY (circled) starts the next level; the interstitial video ad played right after this tap](../img/20261001-interstitial-ads-entry-daf00ba5.webp) [^s1]

It also appeared after:

- CLAIM 5 (keys, the button without a video) on a level's win screen [^s11];
- NEXT on the Daily Challenge win screen [^s7];
- PLAY on the Secret Level offer, both times it was tapped [^s15];
- typing letters in the middle of level 9, about 330 s after the previous ad [^s10].

![Level win screen: CLAIM 5 keys, the button without a video, also led to an interstitial; the quote on the card is blacked out](../img/20261001-interstitial-ads-win-claim-ea95c934.webp) [^s16]

## What it looks like

A full-screen video of another game (here Royal Match). At the top: a "Skip to playable" pill, a strip
with the advertised app's icon and name, Install and a collapse arrow, then sound and pause buttons
[^s2]. Advertisers seen: Royal Match, a Sudoku game (Oakever), Zoodoku, a word game, a crossword and a
Bus Jam parking game [^s2] [^s7] [^s13]
[^s17] [^s18] [^s4].

![Interstitial video ad (Royal Match): 'Skip to playable' pill top left, advertised app with Install and a collapse arrow, sound and pause buttons, the video below](../img/20261001-interstitial-ads-screen-ae4514d4.webp) [^s2]

## What you can do

| Tab or button | What it does |
|---|---|
| [Skip to playable](#skip-to-playable) | Ends the video; the ad becomes a playable demo with a small skip icon top left |
| [Skip icon](#skip-icon) | Opens a Google Play overlay or sheet for the advertised game |
| [Playable with no close](#playable-with-no-close) | Some playables have no control that closes them; only a game restart leaves |
| [Play Store sheet](#play-store-sheet) | Its X or Back returns to the game with the ad gone |
| [End card](#end-card) | Back or the X top left closes it |
| [Next pill](#next-pill) | On some playables it does nothing |

### Skip to playable

The pill is shown during the video. After the video (about 35 s), the ad switched to a playable demo by
itself: a Royal Match level with "No Ads and Free DOWNLOAD", and the pill shrank to a skip icon at the
top left [^s2] [^s8].

![After the video: the ad turned into a playable Royal Match level with a 'No Ads and Free DOWNLOAD' button; the pill shrank to a skip icon (circled)](../img/20261001-interstitial-ads-tab-skip-to-playable-94744c57.webp) [^s2]

### Skip icon

Tapping the skip icon of the playable did not close the ad: it opened a Google Play overlay for the
advertised game [^s3]. Back from there returned to the level with the ad gone (the screen first stayed
frozen for a few seconds) [^s9]. The overlay (the app's icon, name, Install and Close at the top left)
has no frame here: it is another app [^s3]. The same route worked in later sessions [^s8]
[^s19] [^s20].

<!-- no-frame: other app (Google Play) -->

### Playable with no close

A Bus Jam playable took over level 9 in the middle of typing. It had no close control: Back (several
times), the edge swipe, the "Google Play" pill painted in the ad, taps in the corners and the black top
bar, playing the ad itself, and going Home and reopening the game (the ad came back) all failed; the session ended stuck
after about 9 minutes [^s4] [^s21] [^s22].
In later sessions the same kind of playable (Bus Jam, Sudoku, Zoodoku, a word game, a crossword) was
left by restarting the game (closing it fully and starting it again) [^s23]
[^s18] [^s24].

![Bus Jam playable ad that took over level 9 mid-input: no close control; Back, edge swipe, corners and reopening the game did not leave it](../img/20261001-interstitial-ads-tab-playable-with-no-cl-ee17425f.webp) [^s4]

### Play Store sheet

Some ads open a Google Play sheet for the advertised game (from the skip icon, or by themselves after
the video). The sheet shows the app with an Install button and an X at the top right; the X closed it and returned
to the game [^s5] [^s8]. The player never tapped Install. The sheet has no frame here: it is another app.

<!-- no-frame: other app (Google Play) -->

### End card

At the end, some ads show an end card: the app's icon, its name and Install. Back closed it and went to
the main screen [^s11]; another time the X at the top left closed it and
the level started [^s25].

![Ad end card after CLAIM on a win screen: app icon, name and Install over a dimmed background; Back closed it and went to the main screen](../img/20261001-interstitial-ads-tab-end-card-c8dd2217.webp) [^s6]

### Next pill

Some playables (a Sudoku game, a word game, Zoodoku) show a "Next" pill instead of the skip icon. Next
and Back did nothing for 60–70 s, and the word game looped between Next and Back; a restart was the way
out [^s7] [^s12] [^s17]
[^s26].

![Playable Sudoku ad with a 'Next' pill (circled): Next and Back did nothing for 60+ s; only a game restart left it](../img/20261001-interstitial-ads-tab-next-pill-81036f7f.webp) [^s7]

## How it works

Version 3.6.1.

- When: on starting a level (PLAY on the race screen, CONTINUE LEVEL), after CLAIM on a win screen,
  after NEXT on the Daily Challenge win screen, on Secret Level PLAY, and once in the middle of a level
  [^s2] [^s11] [^s7]
  [^s15] [^s10].
- No cooldown across restarts: CONTINUE LEVEL 16 right after a restart (that had ended an ad) showed
  another interstitial at once [^s14].
- Progress after a restart: level 9, interrupted by the ad, resumed with the letters of the quote's first
  words in place; the letters typed later were empty again. No life was lost, mistakes stayed 0/3
  [^s27]. A Daily Challenge already won before the ad stayed counted
  (progress 1/31) [^s12].
- Removing ads: the Shop sells "Remove ads" for RSD 649, which keeps the optional rewarded ads
  [^s28]. The No ADS button on the main screen and the ADS toggle in
  Settings both open the Google Play payment sheet directly [^s29]
  [^s30].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Ad on PLAY | Tapped PLAY on the race screen | Video ad with a "Skip to playable" pill, then a playable | [^s2] |
| Skip a video ad | Tapped the skip icon at the top left | A Play Store overlay opened; Back returned to the game with the ad gone | [^s3] [^s9] |
| Ad in the middle of a level | Typed letters on level 9 | A Bus Jam playable ad took over about 330 s after the previous ad | [^s10] |
| Close the playable | Back (twice), edge swipe, the "Google Play" pill, corners, Home and reopening the game, playing the ad | Nothing closed it in about 9 minutes; the session ended stuck | [^s4] [^s22] |
| Close the playable, next session | Skip icon on a Royal Match playable, then X on the Play Store sheet | ✅ Back in the game | [^s8] |
| Playable with no close | Restarting the game | ✅ The game started again on the main screen; the ad was gone | [^s12] |
| Level kept after the ad | Resumed level 9 after the stuck ad | ✅ Letters up to the last save kept, later ones lost; no life lost | [^s27] |
| Ad right after a restart | CONTINUE LEVEL 16 just after a restart | ✅ Another interstitial at once | [^s14] |
| End card | Back on the end card | ✅ Closed, main screen | [^s11] |

## Not verified

- What triggers the mid-level ad (time since the last ad?) and the minimum gap between ads.
- Whether every level start shows an interstitial or only some of them.
- Whether "Remove ads" (RSD 649) removes interstitials as well as banners (not bought).
- Exactly when the game saves the letters of a level (the unsaved tail was lost after the restart).

[^s1]: session 20261001-020937-chrono-2FYKPJ, step 2 — [video at 0:48](https://youtu.be/UqLGP_sLnX8?t=48)
[^s2]: session 20261001-020937-chrono-2FYKPJ, step 3 — [video at 0:57](https://youtu.be/UqLGP_sLnX8?t=57)
[^s3]: session 20261001-020937-chrono-2FYKPJ, step 4 — [video at 2:24](https://youtu.be/UqLGP_sLnX8?t=144)
[^s4]: session 20261001-020937-chrono-2FYKPJ, step 16 — [video at 7:01](https://youtu.be/UqLGP_sLnX8?t=421)
[^s5]: session 20261001-071926-chrono-2FYKPJ, step 20 — [video at 5:46](https://youtu.be/TiPdn57GNJY?t=346)
[^s6]: session 20261001-071926-chrono-2FYKPJ, step 25 — [video at 7:45](https://youtu.be/TiPdn57GNJY?t=465)
[^s7]: session 20261001-071926-chrono-2FYKPJ, step 40 — [video at 15:24](https://youtu.be/TiPdn57GNJY?t=924)
[^s8]: session 20261001-071926-chrono-2FYKPJ, step 21 — [video at 5:57](https://youtu.be/TiPdn57GNJY?t=357)
[^s9]: session 20261001-020937-chrono-2FYKPJ, step 5 — [video at 2:31](https://youtu.be/UqLGP_sLnX8?t=151)
[^s10]: session 20261001-020937-chrono-2FYKPJ, step 15 — [video at 6:22](https://youtu.be/UqLGP_sLnX8?t=382)
[^s11]: session 20261001-071926-chrono-2FYKPJ, step 26 — [video at 9:02](https://youtu.be/TiPdn57GNJY?t=542)
[^s12]: session 20261001-071926-chrono-2FYKPJ, step 41 — [video at 16:14](https://youtu.be/TiPdn57GNJY?t=974)
[^s13]: session 20261001-114433-chrono-2FYKPJ, step 2
[^s14]: session 20261001-114433-chrono-2FYKPJ, step 7
[^s15]: session 20261001-071926-chrono-2FYKPJ, step 48 — [video at 21:03](https://youtu.be/TiPdn57GNJY?t=1263)
[^s16]: session 20261001-071926-chrono-2FYKPJ, step 24 — [video at 7:19](https://youtu.be/TiPdn57GNJY?t=439)
[^s17]: session 20261001-071926-chrono-2FYKPJ, step 46 — [video at 19:20](https://youtu.be/TiPdn57GNJY?t=1160)
[^s18]: session 20261001-071926-chrono-2FYKPJ, step 62 — [video at 30:04](https://youtu.be/TiPdn57GNJY?t=1804)
[^s19]: session 20261001-092740-chrono-2FYKPJ, step 9
[^s20]: session 20261001-114433-chrono-2FYKPJ, step 18
[^s21]: session 20261001-020937-chrono-2FYKPJ, step 31 — [video at 12:29](https://youtu.be/UqLGP_sLnX8?t=749)
[^s22]: session 20261001-020937-chrono-2FYKPJ, step 32 — [video at 13:38](https://youtu.be/UqLGP_sLnX8?t=818)
[^s23]: session 20261001-071926-chrono-2FYKPJ, step 49 — [video at 21:25](https://youtu.be/TiPdn57GNJY?t=1285)
[^s24]: session 20261001-114433-chrono-2FYKPJ, step 6
[^s25]: session 20261001-071926-chrono-2FYKPJ, step 54 — [video at 23:39](https://youtu.be/TiPdn57GNJY?t=1419)
[^s26]: session 20261001-114433-chrono-2FYKPJ, step 10
[^s27]: session 20261001-050941-chrono-2FYKPJ, step 50 — [video at 12:34](https://youtu.be/0QFSEGBnZG8?t=754)
[^s28]: session 20261001-071926-chrono-2FYKPJ, step 4 — [video at 1:12](https://youtu.be/TiPdn57GNJY?t=72)
[^s29]: session 20261001-071926-chrono-2FYKPJ, step 27 — [video at 9:18](https://youtu.be/TiPdn57GNJY?t=558)
[^s30]: session 20261001-071926-chrono-2FYKPJ, step 51 — [video at 22:08](https://youtu.be/TiPdn57GNJY?t=1328)
