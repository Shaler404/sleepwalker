---
game: com.oakever.meowdoku
title: "Fish rank event (New Session)"
type: feature
feature: fish-event
version_seen: 1.19.1
verified_at: 2026-10-04
sources: [20261003-200440-chrono-2FYKPJ, 20261003-201915-chrono-2FYKPJ, 20261003-202631-chrono-2FYKPJ, 20261003-235107-chrono-2FYKPJ]
---

# Fish rank event (New Session)

A timed competition: clearing main levels earns fish, and players are ranked by fish on the
[Fish leaderboard](fish-leaderboard.md); the top ranks win gift boxes and exclusive avatar frames. An event
("session") runs for 24 hours [^s1] [^s4]. A main level pays up to three fish: each wrong cat costs one [^s8]
[^s7].

## Why it appeared

Popup on Home after launch, 23:59:50 timer, collect fish and rank up [^s1]. It showed over Home on the first
launch, right after the consent popup and the system notification request [^s1].

## Where to find it

On [Home](home.md), the podium icon with the event timer on the left edge opens the event's leaderboard [^s2].
On launch, the "New Session" popup announces the event by itself [^s1].

![Home screen: the podium icon with the event timer on the left opens the event leaderboard](../img/20261003-fish-event-entry-ad85780f.webp) [^s2]
*Home screen: the podium icon with the event timer on the left edge*

## What it looks like

On launch, the "New Session" popup:

![New Session popup over Home on launch: event art with a 23:59:50 timer, collect fish and rank up, Got it](../img/20261003-fish-event-popup-917b2e84.webp) [^s1]
*The "New Session" popup: a cat on a podium with a 23:59:50 timer, one line of rules, Got it*

Title "New Session", a cross top right, art of a cat with a medal on a 2-1-3 podium with the timer 23:59:50,
the line "Play games to collect [fish] and rank up during each event. Aim for higher ranks!", and the orange
Got it button [^s1]. Got it opened Level 127 directly, not Home [^s5].

### Leaderboard

![Fish leaderboard, 24h timer, podium gifts, info i, Go to Collect](../img/20261003-fish-event-screen-be476195.webp) [^s3]
*The event leaderboard (player names blacked out): the timer, the top three on a podium with gifts, the ranked list, the player's own row last, Go to Collect*

The event's screen is its leaderboard; it is described on [Fish leaderboard](fish-leaderboard.md) [^s3].

### Rules overlay

![Clear main levels to earn fish, top leaderboard, win frames and rewards](../img/20261003-fish-event-popup-c7c2398d.webp) [^s4]
*The rules overlay from the i button: Clear main levels, fish, Top the Leaderboard, Win exclusive frames and rewards; Tap to Continue*

The i button top right of the leaderboard opens a three-step picture: "Clear main levels" leads to fish,
fish lead to "Top the Leaderboard", the top leads to "Win exclusive frames and rewards" (a gift box and a
framed cat avatar). "Tap to Continue" closes it [^s4] [^s6].

### In a level

![Level 128 after a wrong cat: an orange cross on the top left cell, the fish box at the top right with the third fish grey](../img/20261003-fish-event-wrong-cat-fec38193.webp) [^s8]
*Level 128: the fish box (top right, under the gear) after one wrong cat: two orange fish and a grey one (the banner ad is blacked out)*

The [main level](level.md) shows a box of three fish right of the cat heads [^s5]. A wrong cat greys one
[^s8].

## How it works

- Fish come from clearing main levels [^s4]. A level starts with three fish in its box; each wrong cat greys
  one; the boosters do not [^s8] [^s7]. The fish left at the win are added to the player's leaderboard count:
  3 for a clean Level 127 (0 to 3), 2 for Level 128 with one wrong cat (3 to 5) [^s11] [^s7].
- After each won level the [Fish leaderboard](fish-leaderboard.md) comes up by itself before the win screen,
  showing the player's row move up [^s11] [^s7]. The win screen's title follows the fish kept: "Perfect" with
  3, "Brilliant" with 2 [^s9] [^s10].
- Timer: 23:59:50 on the launch popup at 20:05:50 local time [^s1], 23:59:28 on Home at 20:06:17 [^s2],
  23:58:25 on the leaderboard [^s3]; 23:44:36 and 23:40:27 at the two wins about 15 and 19 minutes later
  [^s11] [^s7]; 20:14:07 on the Home icon at about 23:51:33 [^s16]. All readings put the end at about
  20:05:40 on 4 October, 24 h after the first launch. Inferred: this event started when the app was first
  launched; whether every event is tied to the player's own start or to a global schedule is not verified.
- At about 23:51:33 the podium icon on Home carried a small yellow badge reading 27 at its top right [^s16].
  What it counts (inferred: the player's rank) is not verified.
- Rewards: gift boxes for ranks 1 (red), 2 (blue) and 3 (green), and exclusive frames [^s3] [^s4]. Their
  contents were not opened.
- Go to Collect on the leaderboard was not tapped. Inferred: it leads to the next main level.

Version 1.19.1.

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Info: clear main levels to earn fish, top the leaderboard, win exclusive frames and rewards <!-- case:chk-rules --> | The i button on the leaderboard tapped | ✅ | [^s4] |
| Why it appeared: the trigger that brought it up (the first launch, a level won, a threshold, a timer, a loss): a fact with its frame, or a hypothesis to test <!-- case:chk-appeared --> | The New Session popup on the first launch | ✅ | [^s1] |
| Where to find it: the screen and the button that open it (mark --as entry --at X,Y) <!-- case:chk-entry --> | Podium icon on Home tapped; frame marked | not verified | [^s2] |
| What it looks like: its screen (mark --as screen) <!-- case:chk-screen --> | Leaderboard frame marked | not verified | [^s3] |
| The event ends about 20:05:40 on 4 October, 24 h after the first launch <!-- case:end-time --> | Home podium icon read 20:14:07 at about 23:51:33 | ✅ | [^s16] |
| Its timer and schedule: how long it runs and when it comes back <!-- case:chk-timer --> | Timer seen from 23:59:50 down to 20:14:07; end time worked out, the end not reached | not verified | [^s16] |
| What shows during a level while it runs (a bar, a counter, collectibles) <!-- case:chk-in-level --> | Two levels played: the box of three fish; a wrong cat greys one | ✅ | [^s8] |
| Progress per level: the points or items after a win, and after a loss <!-- case:chk-progress --> | Wins: +3 (clean) and +2 (one wrong cat); no loss reached | not verified | [^s7] |
| The rewards per rank or milestone <!-- case:chk-rewards --> | Gift boxes for ranks 1 to 3 seen, not opened | not verified | [^s3] |
| The end: the results screen and the reward paid (a follow-up at the timer's end) <!-- case:chk-end --> | Not reached | not verified |  |
| Win under Fish rank event (New Session): as the base, or what differs <!-- case:under-win --> | Two wins: the leaderboard comes up before the win screen; the title follows the fish kept | ✅ | [^s11] |
| Restart under Fish rank event (New Session): as the base <!-- case:under-restart --> | Settings > Restart on Level 130: the board cleared, no popup from the event or the streak | ✅ | [^s12] |
| Quit under Fish rank event (New Session): as the base <!-- case:under-quit --> | Back arrow on Level 130: straight to Home, no event or streak popup | ✅ | [^s13] |
| Exit the app under Fish rank event (New Session): as the base <!-- case:under-exit-app --> | Android Back on Home: the Quit popup, its cross cancelled | ✅ | [^s14] |
| Out of Fishes under Fish rank event (New Session): as the base <!-- case:under-out-of-fishes --> | Three wrong cats on Level 130: the Out of Fishes screen, no leaderboard or streak popup after the loss | ✅ | [^s15] |

## Not verified

- Whether a loss (Out of Fishes) takes fish from the event total: the total was not checked after the loss
- Where to find it: whether the New Session popup comes back at each new event <!-- case:chk-entry -->
- What it looks like: the screen while the player has fish and a rank <!-- case:chk-screen -->
- What the badge reading 27 on the Home podium icon counts
- Its timer and schedule: what happens at 00:00 and when the next event starts <!-- case:chk-timer -->
- Progress per level: fish after a loss, and whether time costs fish <!-- case:chk-progress -->
- The rewards per rank: the contents of the gift boxes, which ranks get frames <!-- case:chk-rewards -->
- The end: the results screen and the reward paid <!-- case:chk-end -->

[^s1]: session 20261003-200440-chrono-2FYKPJ, step 2 — [video at 0:30](https://youtu.be/Pqx4QY-FpBA?t=30)
[^s2]: session 20261003-200440-chrono-2FYKPJ, step 4 — [video at 1:15](https://youtu.be/Pqx4QY-FpBA?t=75)
[^s3]: session 20261003-200440-chrono-2FYKPJ, step 12 — [video at 2:18](https://youtu.be/Pqx4QY-FpBA?t=138)
[^s4]: session 20261003-200440-chrono-2FYKPJ, step 13 — [video at 2:26](https://youtu.be/Pqx4QY-FpBA?t=146)

[^s5]: session 20261003-200440-chrono-2FYKPJ, step 3 — [video at 1:05](https://youtu.be/Pqx4QY-FpBA?t=65)
[^s6]: session 20261003-200440-chrono-2FYKPJ, step 14 — [video at 2:42](https://youtu.be/Pqx4QY-FpBA?t=162)
[^s7]: session 20261003-201915-chrono-2FYKPJ, step 17 — [video at 5:31](https://youtu.be/ffhYgQE4LvU?t=331)
[^s8]: session 20261003-201915-chrono-2FYKPJ, step 12 — [video at 4:18](https://youtu.be/ffhYgQE4LvU?t=258)
[^s9]: session 20261003-201915-chrono-2FYKPJ, step 7 — [video at 2:27](https://youtu.be/ffhYgQE4LvU?t=147)
[^s10]: session 20261003-201915-chrono-2FYKPJ, step 18 — [video at 5:47](https://youtu.be/ffhYgQE4LvU?t=347)
[^s11]: session 20261003-201915-chrono-2FYKPJ, step 3 — [video at 1:28](https://youtu.be/ffhYgQE4LvU?t=88)

[^s12]: session 20261003-202631-chrono-2FYKPJ, step 15 — [video at 5:05](https://youtu.be/3-USmjAyOV8?t=305)
[^s13]: session 20261003-202631-chrono-2FYKPJ, step 21 — [video at 6:40](https://youtu.be/3-USmjAyOV8?t=400)
[^s14]: session 20261003-202631-chrono-2FYKPJ, step 22 — [video at 6:55](https://youtu.be/3-USmjAyOV8?t=415)
[^s15]: session 20261003-202631-chrono-2FYKPJ, step 17 — [video at 5:40](https://youtu.be/3-USmjAyOV8?t=340)
[^s16]: session 20261003-235107-chrono-2FYKPJ, step 0
