---
game: com.oakever.arrows
title: "Settings"
type: feature
feature: settings
version_seen: 1.33.0
verified_at: 2026-10-03
sources: [20261003-200141-chrono-2FYKPJ, 20261003-232108-chrono-2FYKPJ, 20261003-232357-chrono-2FYKPJ]
---

# Settings

A full-screen list of options opened from the home screen: five toggles (Sound, Vibration, Music,
Guideline, Zen Mode), an account entry (Save Your Progress), Rate Us and Feedback, and links to the
Privacy Policy and Terms of Service [^s1]. No toggle has been changed for good: Guideline was switched
and set back (see [Guideline](guideline.md)); Save Your Progress ([its page](cloud-save.md)) and Rate Us
are the only rows opened [^s5].

## Why it appeared

Open from the start: the gear icon is on the home screen on the first launch, with no lock [^s1] [^s2].

## Where to find it

Home screen > the gear icon in the top right corner [^s2]. The Back key, or the arrow left of the
"Settings" title, returns to Home [^s3].

![Home screen: the gear icon top right opens Settings](../img/20261003-settings-entry-ee4e6b91.webp) [^s2]
*Home screen: the gear icon top right opens Settings*

## What it looks like

A light screen titled "Settings" with a back arrow, and four white blocks of rows [^s1]:

- toggles: Sound, Vibration, Music (on by default), Guideline, Zen Mode (off by default);
- Save Your Progress, with an arrow;
- Rate Us and Feedback, each with an arrow;
- Privacy Policy and Terms of Service, each with an arrow.

![Settings: Sound, Vibration and Music on; Guideline and Zen Mode off; Save Your Progress, Rate Us, Feedback, Privacy Policy, Terms of Service](../img/20261003-settings-screen-9a5a2f35.webp) [^s1]
*The Settings screen on a fresh install, default values*

## What you can do

| Tab or button | Default | What it does |
|---|---|---|
| [Sound, Vibration and Music](#sound-vibration-and-music) | on | not tested |
| [Guideline](guideline.md) | off | not tested; see its page |
| [Zen Mode](zen-mode.md) | off | not tested; see its page |
| [Save Your Progress](#save-your-progress) | — | opens the Save Progress popup; see [its page](cloud-save.md) |
| [Rate Us and Feedback](#rate-us-and-feedback) | — | Rate Us opens a rating popup, see [its page](rate-us.md); Feedback not opened |
| [Privacy Policy and Terms of Service](#privacy-policy-and-terms-of-service) | — | not opened |
| [In-level Settings popup](#in-level-settings-popup) | — | the gear inside a level: a shorter list with Restart |

All values are from the Settings frame above, version 1.33.0 [^s1].

### Sound, Vibration and Music

<!-- no-frame: the three toggles are on the Settings frame above; none was switched -->
The first three rows, each with an icon and a switch; all three on by default [^s1]. Switching them was not
tried.

### Save Your Progress

<!-- no-frame: the row is on the Settings frame above; it was not opened -->
A row with a person icon and an arrow, alone in the second block [^s1]. It opens the Save Progress popup
(sign in with Facebook or Google, Delete Account), described on the
[Save Your Progress](cloud-save.md) page; the restore seen on the first launch is on the
[Consent screen](consent.md) page.

### Rate Us and Feedback

<!-- no-frame: the rows are on the Settings frame above; the Rate Us popup is on its own page -->
Two rows with arrows in the third block: Rate Us (a thumbs-up icon) and Feedback (a speech-bubble icon)
[^s1]. Rate Us opens a popup over Settings with five empty stars, "Do you like Amaze GO?", a Rate button
and an X; X closes it with nothing changed [^s5] (see [Rate Us](rate-us.md)). Feedback was not opened.

### Privacy Policy and Terms of Service

<!-- no-frame: the rows are on the Settings frame above; neither was opened -->
Two rows with arrows in the last block [^s1]. Not opened; the same two documents are linked from the
[Consent screen](consent.md).

### In-level Settings popup

The gear top right of a level opens a shorter Settings popup over the board: Sound, Vibration, Music and
Zen Mode switches and an orange Restart button, with an X to close; no Guideline and no Save Your Progress
[^s4].

![In-level Settings popup: Sound, Vibration, Music, Zen Mode, Restart](../img/20261003-guideline-popup-c1d13e3e.webp) [^s4]
*The Settings popup inside a level: four switches and Restart*

## How it works

Version 1.33.0. Beyond the defaults shown [^s1], only Guideline (see [its page](guideline.md)), Save
Your Progress (see [its page](cloud-save.md)) and Rate Us (see [its page](rate-us.md)) have been tried
[^s5]. The screen looked the same on a progressed device in the third session [^s5]. Guideline and Save Your Progress are only in the home
screen's Settings, not in the in-level popup [^s4].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared <!-- case:chk-appeared --> | Fresh install, looked at Home | ✅ The gear is on Home from the first launch | [^s1] |
| Where to find it: the screen and the button that open it <!-- case:chk-entry --> | Tapped the gear top right of Home | ✅ Settings opened | [^s2] |
| What it looks like: its screen <!-- case:chk-screen --> | Opened Settings | ✅ Five toggles, Save Your Progress, Rate Us, Feedback, Privacy Policy, Terms of Service | [^s1] |
| Every option or button and what it changes <!-- case:chk-options --> | — | not verified: only the defaults were read |  |
| For a prompt: what each answer does and whether it comes back <!-- case:chk-answers --> | Opened Rate Us, closed it with X | not verified: X returns to Settings; the stars, Rate and Feedback not tried | [^s5] |
| Gear in a level opens a short settings popup <!-- case:in-level-popup --> | Opened level 3 and tapped the gear top right | ✅ Sound, Vibration, Music, Zen Mode and Restart; no Guideline, no Save Progress | [^s4] |
| Links out (privacy, terms, help): where they lead <!-- case:chk-links --> | — | not verified: not opened |  |

## Not verified

- Every option or button and what it changes: Sound, Vibration, Music, Guideline, Zen Mode, Save Your Progress (study-save-progress) <!-- case:chk-options -->
- For a prompt: what Feedback opens, and what the Rate Us stars and Rate do <!-- case:chk-answers -->
- Links out: where Privacy Policy and Terms of Service lead <!-- case:chk-links -->

[^s1]: session 20261003-200141-chrono-2FYKPJ, step 5 — [video at 1:32](https://youtu.be/l44HK-PZ5-o?t=92)
[^s2]: session 20261003-200141-chrono-2FYKPJ, step 2 — [video at 0:39](https://youtu.be/l44HK-PZ5-o?t=39)

[^s3]: session 20261003-200141-chrono-2FYKPJ, step 6 — [video at 1:48](https://youtu.be/l44HK-PZ5-o?t=108)
[^s4]: session 20261003-232108-chrono-2FYKPJ, step 9 — [video at 1:26](https://youtu.be/KL7evNlX6oU?t=86)
[^s5]: session 20261003-232357-chrono-2FYKPJ, step 4 — [video at 0:42](https://youtu.be/x9mSZuHgO_4?t=42)
