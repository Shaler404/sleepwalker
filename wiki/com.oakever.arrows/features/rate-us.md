---
game: com.oakever.arrows
title: "Rate Us"
type: feature
feature: rate-us
version_seen: 1.33.0
verified_at: 2026-10-05
sources: [20261003-200141-chrono-2FYKPJ, 20261003-232357-chrono-2FYKPJ, 20261005-012010-chrono-2FYKPJ]
---

# Rate Us

A popup that asks the player to rate the game from one to five stars. It is opened from a row in
Settings, and it also came up by itself over the win card of level 6 [^s2] [^s3] [^s5]. Only closing it
was tried. No rating was given, because the project's rule is never to
submit a rating.

## Why it appeared

The Rate Us row is in Settings from the first visit, with no lock [^s1]. The popup did not come up by
itself after levels 3 and 4 [^s4], nor after the wins of Hard level 5. It came up by itself over the win
card of level 6 [^s5]. Hypothesis: it comes at a set level (6) or after a set number of wins; not
verified.

## Where to find it

Home > the gear top right > Settings > the Rate Us row (thumbs-up icon) in the third block, above
Feedback [^s2].

![Settings: the Rate Us row in the third block opens the popup](../img/20261003-rate-us-entry-9a5a2fa5.webp) [^s2]
*Settings: the Rate Us row, third block, above Feedback*

## What it looks like

![Rate Us popup: five empty stars, Do you like Amaze GO?, Rate button, X](../img/20261003-rate-us-screen-90d03e3f.webp) [^s3]
*The Rate Us popup over the dimmed Settings screen*

A cream popup over the dimmed Settings screen [^s3]. From top to bottom it has:

- the title "Rate Us" and an X at the top right;
- five empty stars;
- the question "Do you like Amaze GO?";
- an orange Rate button.

### Popup after a win

The same popup, unasked, over the three-star win card of level 6 [^s5]. X closed it and left the win
card, with Next Level, as it was [^s6].

![The Rate Us popup over the dimmed level 6 win card: five empty stars, Do you like Amaze GO?, Rate, X](../img/20261005-rate-us-popup-91d17f2f.webp) [^s5]
*After the level 6 win: Rate Us over the win card*

## What you can do

| Tab or button | What it does |
|---|---|
| [X](#x) | closes the popup back to Settings |
| [Stars and Rate](#stars-and-rate) | not tapped (no rating is submitted) |

### X

<!-- no-frame: the result is the Settings screen, on the Settings page -->
Closes the popup. Settings shows again with nothing changed [^s4].

### Stars and Rate

<!-- no-frame: the controls are on the popup frame above; not tapped -->
Five stars and the Rate button [^s3]. Not tapped, so whether a low rating stays in the game and a high one
goes to the store is not known. Inferred: Rate leads out to the store.

## How it works

Version 1.33.0. The popup opens from Settings at any time [^s3]. Unasked, it was seen once: after the
level 6 win, not after the wins of levels 3, 4 and 5 [^s4] [^s5]. It did not come again after the wins
of levels 7 to 10 in the same session [^s7].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared <!-- case:chk-appeared --> | Opened Settings on the first launch | ✅ The row is there from the start | [^s1] |
| Where to find it <!-- case:chk-entry --> | Home gear > Settings > Rate Us row | ✅ The popup opened | [^s2] |
| Its screen <!-- case:chk-screen --> | Looked at the popup | ✅ "Rate Us", five empty stars, "Do you like Amaze GO?", Rate, X at the top right | [^s3] |
| Every option <!-- case:chk-options --> | Tapped X | ✅ Back to Settings, nothing changed; stars and Rate not tapped by policy | [^s4] |
| What each answer does <!-- case:chk-answers --> | Dismissed with X | ✅ Only dismiss exercised: back to Settings; rating answers not exercised by policy. The unasked popup after the level 6 win was closed with X: the win card stayed, and the popup did not return in four more wins | [^s4] [^s6] [^s7] |
| Unasked popup <!-- case:chk-auto-prompt --> | Won level 6, the first win after Hard level 5 (Today's Levels 2) | ✅ Rate Us came up over the win card by itself; X closed it back to the win card | [^s5] [^s6] |
| Links out <!-- case:chk-links --> | — | ✅ Rate likely leads out to the store (inferred); not followed by policy | [^s4] |

## Not verified

- What the stars and Rate do (a store page, an in-game thank-you, a feedback form for low ratings):
  not exercised by policy
- What brings the unasked popup after the level 6 win (a count of wins, a level number) and whether it
  comes again later

[^s1]: session 20261003-200141-chrono-2FYKPJ, step 5 — [video at 1:32](https://youtu.be/l44HK-PZ5-o?t=92)
[^s2]: session 20261003-232357-chrono-2FYKPJ, step 4 — [video at 0:42](https://youtu.be/x9mSZuHgO_4?t=42)
[^s3]: session 20261003-232357-chrono-2FYKPJ, step 5 — [video at 0:51](https://youtu.be/x9mSZuHgO_4?t=51)
[^s4]: session 20261003-232357-chrono-2FYKPJ, step 6 — [video at 1:02](https://youtu.be/x9mSZuHgO_4?t=62)

[^s5]: session 20261005-012010-chrono-2FYKPJ, step 3 — [video at 1:43](https://youtu.be/BaXAJZAR4vk?t=103)
[^s6]: session 20261005-012010-chrono-2FYKPJ, step 4 — [video at 2:05](https://youtu.be/BaXAJZAR4vk?t=125)
[^s7]: session 20261005-012010-chrono-2FYKPJ, step 29 — [video at 12:18](https://youtu.be/BaXAJZAR4vk?t=738)
