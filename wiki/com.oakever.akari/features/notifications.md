---
game: com.oakever.akari
title: "Notification permission prompt"
type: feature
feature: notifications
version_seen: 1.0.2
verified_at: 2026-10-05
sources: [20261003-200925-chrono-2FYKPJ, 20261005-080420-chrono-2FYKPJ]
---

# Notification permission prompt

On the first launch, right after the [Terms consent](consent.md), the game asks Android for permission to send notifications. It is the standard Android permission dialog with two answers, Allow and Don't allow [^s1]. After Don't allow it did not come back on a later launch, and the game has no notification setting of its own (version 1.0.2) [^s4].

## Why it appeared

First launch, right after accepting the Terms consent: the Android permission dialog over the game's loading screen [^s1].

## Where to find it

It opens by itself after Accept on the Welcome card and the Oakever Games splash screen [^s1]. No control in the game leads to it: the [Settings](settings.md) sheet has only the sound and vibration toggles, Help Center, Privacy Policy and Terms of Service [^s4].

<!-- no-entry: shown by itself on the first launch, after the Terms consent; no control leads to it -->

## What it looks like

<!-- no-screen: an Android system dialog, not the game's own screen; system dialogs are not shown on pages -->

The Android system dialog asking whether to allow MeowTrail to send notifications, with two buttons: Allow and Don't allow. It is drawn over the game's loading screen [^s1].

## What you can do

| Tab or button | What it does |
|---|---|
| [Don't allow](#dont-allow) | Closes the dialog; the tutorial starts |
| [Allow](#allow) | Not tried in the game; in Android it grants the permission |

### Don't allow

<!-- no-frame: a system dialog -->

The session answered Don't allow; the dialog closed and the first tutorial board opened ([Tutorial](tutorial.md)) [^s2]. On a later session the game was force-stopped and launched again: after 6 s it showed Home with no prompt, and the game played on without the permission [^s4].

### Allow

<!-- no-frame: not tried in this session -->

Not tried on this install (the dialog was answered Don't allow and did not come back) [^s4].

## How it works

- Shown once on the first launch, after the Terms consent and before the tutorial (version 1.0.2) [^s1].
- Not shown again after Don't allow: a force-stop and relaunch on 1.0.2 brought no prompt [^s4].
- No notification toggle in [Settings](settings.md): it has sound and vibration toggles only, and no link to the permission [^s3] [^s4].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Android dialog 'Allow MeowTrail to send you notifications?' Allow / Don't allow, over the loading tip screen <!-- case:chk-screen --> | Accepted the Terms consent on a fresh install | The Android dialog with Allow and Don't allow | ✅ [^s1] |
| Why it appeared: the trigger that brought it up <!-- case:chk-appeared --> | First launch, after Accept | Shown before the tutorial | ✅ [^s1] |
| Where to find it: the screen and the button that open it <!-- case:chk-entry --> | Looked through the Settings sheet | No in-game entry: a system dialog on the first launch only | ✅ [^s4] |
| Every option or button and what it changes <!-- case:chk-options --> | Tapped Don't allow; looked for a toggle in Settings | Only the system dialog's Allow and Don't allow; no notification toggle in the game | ✅ [^s4] |
| For a prompt: what each answer does and whether it comes back <!-- case:chk-answers --> | Tapped Don't allow; later force-stopped and relaunched | The tutorial starts; after the relaunch no prompt, and the game works without the permission | ✅ [^s4] |
| Links out: where they lead <!-- case:chk-links --> | — | Does not apply: the dialog has no links | ✅ [^s4] |

## Not verified

- What Allow changes in the game (not tried on this install; no notification was seen)

[^s1]: session 20261003-200925-chrono-2FYKPJ, step 1 — [video at 0:00](https://youtu.be/JOMuD_cF8gM?t=0)

[^s2]: session 20261003-200925-chrono-2FYKPJ, step 2 — [video at 0:00](https://youtu.be/JOMuD_cF8gM?t=0)
[^s3]: session 20261003-200925-chrono-2FYKPJ, step 13 — [video at 1:42](https://youtu.be/JOMuD_cF8gM?t=102)
[^s4]: session 20261005-080420-chrono-2FYKPJ, step 9 — [video at 1:42](https://youtu.be/bJ144EFaJEE?t=102)
