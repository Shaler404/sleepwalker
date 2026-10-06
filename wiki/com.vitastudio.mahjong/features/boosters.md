---
game: com.vitastudio.mahjong
title: "Boosters: Shuffle, Hint, Undo"
type: feature
feature: boosters
version_seen: 3.40.1
verified_at: 2026-10-05
sources: [20261003-195050-chrono-2FYKPJ, 20261003-231804-chrono-2FYKPJ, 20261005-073804-chrono-2FYKPJ, 20261005-133525-chrono-2FYKPJ]
---

# Boosters: Shuffle, Hint, Undo

Three round buttons under the board of every level: Shuffle, Hint and Undo. Each carries a red badge
with the number of uses the player holds; one use costs one unit [^s1] [^s2]. Hint lights a matching
pair, Undo takes the last tile back out of the tray, Shuffle rearranges the tiles on the board
[^s3] [^s4] [^s5]. At zero a badge shows "+"; Hint at zero offers two Hints for a video [^s7].

## Why it appeared

On the level screen when level 19 was opened, with Shuffle 3, Hint 5 and Undo 10 [^s1]. The level they
first appear on is not known from these sessions.

## Where to find it

<!-- no-entry: no control opens them; they sit on the level screen itself (see "What it looks like") -->
On the level screen, in a row under the board: Shuffle left, Hint centre, Undo right [^s2]. The level
opens from the Level N button on the home screen (see [Tray mahjong level](core-level.md)).

## What it looks like

![The level 19 board, an empty four-slot tray above it, and the three booster buttons along the bottom: Shuffle with a 3 badge, Hint (a light bulb) with 5, Undo (a back arrow) with 10](../img/20261003-boosters-screen-d46f6bb0.webp) [^s2]
*The three boosters under the board: Shuffle 3, Hint 5, Undo 10*

- Shuffle: two crossing arrows; badge 3 [^s2].
- Hint: a light bulb; badge 5 [^s2].
- Undo: a curved back arrow; badge 10 [^s2].

## What you can do

| Tab or button | What it does |
|---|---|
| [Hint](#hint) | Lights two matching free tiles in blue; badge 5 to 4 |
| [Undo](#undo) | Returns the last tile from the tray to its place on the board; badge 10 to 9 |
| [Shuffle](#shuffle) | Rearranges the tiles on the board; badge 3 to 2 |
| [Hint at zero](#hint-at-zero) | The "+" badge; a tap offers 2 Hints for a video |

### Hint

![The board after one Hint: two matching tiles, at the left and right edges of the board, lit in blue; the Hint badge reads 4](../img/20261003-boosters-tab-hint-d46b7bb0.webp) [^s3]
*Hint: the pair lit in blue, badge 5 to 4*

One tap lit two matching free tiles in blue and the badge went from 5 to 4 [^s3]. The light stayed on:
after one of the two was tapped into the tray, the tile in the tray and its partner on the board were
both still blue [^s6].

### Undo

![The board after one Undo: the tray empty again, both lit tiles back on the board, the Undo badge reads 9](../img/20261003-boosters-tab-undo-d46b7bb0.webp) [^s4]
*Undo: the tray tile is back on the board, badge 10 to 9*

With one tile in the tray, one tap put it back in its place on the board and emptied the tray; the
badge went from 10 to 9 [^s4]. The board looked as before the move, the Hint light included [^s4].

![One tile flies from the board into the tray, then Undo sends it back to its place](../clips/20261003-booster-undo.webp) [^s6]
*Clip 8 s · [original on YouTube from 1:40](https://youtu.be/ssTmhwls_uc?t=100)*

### Hint at zero

![The Free Hint window over level 20: a light-bulb icon, "Watch a video to get 2 Hints.", a green "Get Two" button with a video icon, a close X; the Hint button below has a "+" badge](../img/20261005-boosters-popup-c1d67f7c.webp) [^s7]
*Hint at zero: the "+" badge and the Free Hint offer*

After level 19 the Hint badge showed "+" instead of a number [^s8]. A tap on Hint then opened a "Free
Hint" window: "Watch a video to get 2 Hints.", a green "Get Two" button with a video icon and a close X
[^s7]. Get Two was not tapped; the X closed the window [^s7].

### Shuffle

![The board after one Shuffle: the same layout with different faces in the slots, several face-down red tiles now face-up and others moved; the Shuffle badge reads 2](../img/20261003-boosters-tab-shuffle-c4ee7bf0.webp) [^s5]
*Shuffle: the tiles rearranged, badge 3 to 2*

One tap kept the shape of the layout and changed which tile lies in each place: the faces changed and
the face-down red tiles moved to other places; the badge went from 3 to 2 [^s5]. The Hint light was
gone after the shuffle [^s5].

![The tiles of the level 19 board rearrange after a tap on Shuffle](../clips/20261003-booster-shuffle.webp) [^s5]
*Clip 5.4 s · [original on YouTube from 1:53](https://youtu.be/ssTmhwls_uc?t=113)*

## How it works

Version 3.40.1.

- Counts at the start of level 19 on a restored save: Shuffle 3, Hint 5, Undo 10 [^s1] [^s2].
- Each use costs one unit from its own badge; no coins or other price was asked [^s3] [^s4] [^s5].
- Hint, Undo and Shuffle were each used once in one level; none of them refilled during the level
  (Shuffle 2, Hint 4, Undo 9 at the end) [^s5].
- The counts carry over from level to level: level 19 ended at Shuffle 2, Hint 0 ("+"), Undo 9, and level
  20 opened with the same; the level 19 win added none [^s8].
- Hint at zero: a video for 2 Hints (not watched) [^s7].
- The level chest is a source: the one at level 20 gave Hint x1 and Undo x1; "Collect x2" with a video
  would double them [^s9] [^s10].
- "-4 to revive" in the Out of space window spends 4 Undos: 9 to 5 on the Hard level 20
  [^s11].
- What Shuffle and Undo do at zero, other sources and whether units refill over time are not verified.

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared: the trigger that brought it up (the first launch, a level won, a threshold, a timer, a loss): a fact with its frame, or a hypothesis to test <!-- case:chk-appeared --> | Opened level 19 | ✅ On the level screen | [^s1] |
| Where to find it: the bottom bar of the level screen, Shuffle, Hint, Undo left to right <!-- case:chk-entry --> | Opened level 19 | ✅ The row under the board | [^s2] |
| What it looks like: three round buttons with count badges <!-- case:chk-screen --> | Opened level 19 | ✅ | [^s2] |
| What it does: the effect of one use <!-- case:chk-effect --> | Hint, Undo, Shuffle once each | ✅ Hint lights a pair in blue; Undo returns the tray tile to the board; Shuffle rearranges the board | [^s3] [^s4] [^s5] |
| The balance: badges on each button <!-- case:chk-balance --> | Opened level 19 | ✅ Shuffle 3, Hint 5, Undo 10 at level 19; the amount on level 1 not seen | [^s2] |
| Hint, then a tap on a lit tile, then Undo <!-- case:hint-tint --> | Hint, one lit tile into the tray, Undo | ✅ The pair lit blue; the tile kept the blue in the tray; Undo returned it to the board, still blue | [^s3] [^s6] [^s4] |
| Sources: every way to get more <!-- case:chk-sources --> | Won level 19; tapped Hint at zero | Partly: the win added none; Hint at zero offers 2 for a video (not watched) | [^s8] [^s7] |
| Sinks: one unit per use, no price <!-- case:chk-sinks --> | Hint, Undo, Shuffle once each | ✅ Hint 5 to 4, Undo 10 to 9, Shuffle 3 to 2 | [^s3] [^s4] [^s5] |
| At zero: what happens and the offers to refill it <!-- case:chk-empty --> | Spent Hint to zero, tapped it | Partly: the badge shows "+"; the Free Hint window offers 2 Hints for a video; Shuffle and Undo at zero not seen | [^s7] |
| Refill timer, if any <!-- case:chk-refill --> | — | not verified: no refill seen during a level or between levels 19 and 20 | [^s8] |
| Shuffle turned face-down tiles up: about 13 red backs before, about 7 after <!-- case:shuffle-reveals --> | One Shuffle on level 19 | not verified: one observation | [^s5] |
| The level chest as a source <!-- case:source-level-chest --> | Won level 20, opened the level chest, Collect | ✅ Hint x1 and Undo x1 (with an avatar frame); the boosters then read Shuffle 1, Hint 1, Undo 2 (see [Level progress chest](level-chest.md)) | [^s10] |

## Not verified

- The balance: the starting amount on level 1 and the level the boosters first appear on <!-- case:chk-balance -->
- Sources: every way to get more (a daily reward, a pack, the chests) and how much; the Free Hint video not watched <!-- case:chk-sources -->
- At zero: Shuffle and Undo at zero, and what Get Two gives in the level <!-- case:chk-empty -->
- Refill timer, if any: how long one unit takes and the maximum <!-- case:chk-refill -->
- Whether Shuffle also turns face-down tiles up <!-- case:shuffle-reveals -->

[^s1]: session 20261003-195050-chrono-2FYKPJ, step 17 — [video at 4:17](https://youtu.be/KUKs3cQ-xqY?t=257)
[^s2]: session 20261003-231804-chrono-2FYKPJ, step 4 — [video at 1:11](https://youtu.be/ssTmhwls_uc?t=71)
[^s3]: session 20261003-231804-chrono-2FYKPJ, step 5 — [video at 1:33](https://youtu.be/ssTmhwls_uc?t=93)
[^s4]: session 20261003-231804-chrono-2FYKPJ, step 7 — [video at 1:47](https://youtu.be/ssTmhwls_uc?t=107)
[^s5]: session 20261003-231804-chrono-2FYKPJ, step 8 — [video at 1:58](https://youtu.be/ssTmhwls_uc?t=118)
[^s6]: session 20261003-231804-chrono-2FYKPJ, step 6 — [video at 1:42](https://youtu.be/ssTmhwls_uc?t=102)
[^s7]: session 20261005-073804-chrono-2FYKPJ, step 53 — [video at 18:10](https://youtu.be/nmXrQmoLWlU?t=1090)
[^s8]: session 20261005-073804-chrono-2FYKPJ, step 49 — [video at 16:19](https://youtu.be/nmXrQmoLWlU?t=979)

[^s9]: session 20261005-133525-chrono-2FYKPJ, step 46 — [video at 18:23](https://youtu.be/D10jI230Oks?t=1103)
[^s10]: session 20261005-133525-chrono-2FYKPJ, step 47 — [video at 18:42](https://youtu.be/D10jI230Oks?t=1122)
[^s11]: session 20261005-133525-chrono-2FYKPJ, step 10 — [video at 3:37](https://youtu.be/D10jI230Oks?t=217)
