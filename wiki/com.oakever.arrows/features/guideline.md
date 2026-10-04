---
game: com.oakever.arrows
title: "Guideline toggle"
type: feature
feature: guideline
version_seen: 1.33.0
verified_at: 2026-10-03
sources: [20261003-200141-chrono-2FYKPJ, 20261003-232108-chrono-2FYKPJ]
---

# Guideline toggle

A switch in the home screen's Settings named "Guideline", with a grid icon, off by default [^s1]. It
can be switched on and stays on after Settings is closed and reopened [^s6]. It is not in the Settings
popup inside a level [^s4]. With it on, no change was seen on the board of level 3 at rest [^s5]; what it
does is not known yet.

## Why it appeared

In Settings from the first visit after a fresh install, with no lock (progress had been restored from the
cloud to level 3) [^s1]. Hypothesis: it draws a guide on the board, such as the path an arrow will take
when tapped (from the name and the grid icon), not verified; level 3 at rest showed nothing [^s5].

## Where to find it

Home > the gear top right > Settings > "Guideline", the fourth row of the first block, between Music and
Zen Mode [^s1] [^s2]. Only the home screen's Settings has it: the gear inside a level opens a shorter
popup without it [^s4].

![Settings: the Guideline switch (grid icon), fourth row, off](../img/20261003-guideline-entry-9a5a2f35.webp) [^s2]
*Settings: the Guideline switch (grid icon) in the fourth row, between Music and Zen Mode, off*

## What it looks like

The feature has no screen of its own: it is the switch. Off, the switch is grey with the knob on the
left; on, it turns orange with the knob on the right, like Sound, Vibration and Music [^s3].

![Settings with Guideline switched on: the fourth switch orange like the three above it, Zen Mode grey](../img/20261003-guideline-screen-9a5a2fa5.webp) [^s3]
*Settings with Guideline on: the fourth switch orange, Zen Mode still off*

With Guideline on, level 3 at rest: the arrows on a plain background, three blue drops top left; no grid
and no guide lines [^s5].

![Level 3 at rest with Guideline on: arrows on a plain background, no grid or guide lines](../img/20261003-guideline-result-a61f9f66.webp) [^s5]
*Level 3 at rest with Guideline on: no grid or guide lines on the board*

The Settings popup inside a level (the gear top right of the level) lists Sound, Vibration, Music and Zen
Mode and a Restart button; there is no Guideline row [^s4].

![In-level Settings popup: Sound, Vibration, Music, Zen Mode, Restart; no Guideline row](../img/20261003-guideline-popup-c1d13e3e.webp) [^s4]
*The in-level Settings popup: four switches and Restart, no Guideline*

## How it works

Version 1.33.0.

- Off by default [^s1].
- One tap on the switch turns it on; one more tap turns it off. It was switched on, left through Home and
  a level, and found still on when Settings was reopened; then it was set back to off [^s6].
- Only in the home screen's Settings; the in-level Settings popup has no Guideline row, so it cannot be
  changed during a level [^s4].
- Effect on the board: none seen on level 3 at rest, with no arrow tapped [^s5]. Whether it shows anything
  when an arrow is tapped or on larger levels is not verified (experiment exp-guideline-effect).

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Toggle on in home settings persists after reopening; in-level settings popup has no Guideline row <!-- case:toggle-persist --> | Switched Guideline on, went Home, opened level 3 and its Settings popup, came back and reopened Settings | ✅ Still on after reopening; the in-level popup has no Guideline row | [^s6] [^s4] |
| Visible effect on level 3 at idle with Guideline on: none seen <!-- case:visual-effect --> | Opened level 3 with Guideline on and looked at the board without tapping an arrow | ✅ No grid or guide lines seen | [^s5] |
| Why it appeared <!-- case:chk-appeared --> | Opened Settings after a fresh install | ✅ In Settings from the start, no lock; what it does is a hypothesis | [^s1] |
| Where to find it: the screen and the button that open it <!-- case:chk-entry --> | Opened Settings from the gear on Home | ✅ Fourth row, "Guideline", off; not in the in-level popup | [^s2] [^s4] |
| What it looks like: its screen <!-- case:chk-screen --> | Switched it on and opened level 3 | The switch turns orange; no change on the board at rest; its effect not seen yet | [^s3] [^s5] |
| Every option or button and what it changes <!-- case:chk-options --> | Switched on, then back off | Switching works and persists; what "on" changes in play not verified | [^s6] |
| For a prompt: what each answer does <!-- case:chk-answers --> | Switched on and off | No prompt appeared on either tap | [^s6] |
| Links out <!-- case:chk-links --> | — | none: a switch with no link |  |

## Not verified

- What Guideline changes in play: tapping an arrow with it on, larger levels, compared with it off
  (exp-guideline-effect) <!-- case:chk-options -->
- What the board looks like when Guideline shows something <!-- case:chk-screen -->
- Hypothesis: it draws the path an arrow will take <!-- case:chk-appeared -->

[^s1]: session 20261003-200141-chrono-2FYKPJ, step 5 — [video at 1:32](https://youtu.be/l44HK-PZ5-o?t=92)
[^s2]: session 20261003-232108-chrono-2FYKPJ, step 5 — [video at 0:43](https://youtu.be/KL7evNlX6oU?t=43)
[^s3]: session 20261003-232108-chrono-2FYKPJ, step 6 — [video at 0:54](https://youtu.be/KL7evNlX6oU?t=54)
[^s4]: session 20261003-232108-chrono-2FYKPJ, step 9 — [video at 1:26](https://youtu.be/KL7evNlX6oU?t=86)
[^s5]: session 20261003-232108-chrono-2FYKPJ, step 8 — [video at 1:09](https://youtu.be/KL7evNlX6oU?t=69)
[^s6]: session 20261003-232108-chrono-2FYKPJ, step 13 — [video at 1:58](https://youtu.be/KL7evNlX6oU?t=118)
