---
game: com.oakever.akari
title: "Notification permission prompt"
type: feature
feature: notifications
version_seen: 1.0.2
verified_at: 2026-10-03
sources: [20261003-200925-chrono-2FYKPJ]
---

# Notification permission prompt

On the first launch, right after the [Terms consent](consent.md), the game asks Android for permission to send notifications. It is the standard Android permission dialog with two answers, Allow and Don't allow [^s1].

## Why it appeared

First launch, right after accepting the Terms consent: the Android permission dialog over the game's loading screen [^s1].

## Where to find it

It opens by itself after Accept on the Welcome card and the Oakever Games splash screen; no control leads to it [^s1].

<!-- no-entry: shown by itself on the first launch, after the Terms consent; no control leads to it -->

## What it looks like

<!-- no-screen: an Android system dialog, not the game's own screen; system dialogs are not shown on pages -->

The Android system dialog asking whether to allow MeowTrail to send notifications, with two buttons: Allow and Don't allow. It is drawn over the game's loading screen [^s1].

## What you can do

| Tab or button | What it does |
|---|---|
| [Don't allow](#dont-allow) | Closes the dialog; the tutorial starts |
| [Allow](#allow) | Not tried |

### Don't allow

<!-- no-frame: a system dialog -->

The session answered Don't allow; the dialog closed and the first tutorial board opened ([Tutorial](tutorial.md)) [^s2].

### Allow

<!-- no-frame: not tried in this session -->

Not tried.

## How it works

- Shown once on the first launch, after the Terms consent and before the tutorial (version 1.0.2) [^s1].
- No notification toggle was seen in [Settings](settings.md): it has sound and vibration toggles only [^s3].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Android dialog 'Allow MeowTrail to send you notifications?' Allow / Don't allow, over the loading tip screen <!-- case:chk-screen --> | Accepted the Terms consent on a fresh install | The Android dialog with Allow and Don't allow | ✅ [^s1] |
| Why it appeared: the trigger that brought it up <!-- case:chk-appeared --> | First launch, after Accept | Shown before the tutorial | ✅ [^s1] |
| Where to find it: the screen and the button that open it <!-- case:chk-entry --> | — | not verified: it opens by itself |  |
| Every option or button and what it changes <!-- case:chk-options --> | Tapped Don't allow | not verified: Allow not tried |  |
| For a prompt: what each answer does and whether it comes back <!-- case:chk-answers --> | Tapped Don't allow | Tutorial starts; whether the prompt comes back was not checked |  |
| Links out: where they lead <!-- case:chk-links --> | — | not verified: the dialog has no links seen |  |

## Not verified

- Where to find it: whether the prompt can be reached again from the game <!-- case:chk-entry -->
- What Allow changes (only Don't allow was tried) <!-- case:chk-options -->
- Whether the prompt comes back after Don't allow (a later launch, a later level) <!-- case:chk-answers -->
- Links out: none seen <!-- case:chk-links -->

[^s1]: session 20261003-200925-chrono-2FYKPJ, step 1 — [video at 0:00](https://youtu.be/JOMuD_cF8gM?t=0)

[^s2]: session 20261003-200925-chrono-2FYKPJ, step 2 — [video at 0:00](https://youtu.be/JOMuD_cF8gM?t=0)
[^s3]: session 20261003-200925-chrono-2FYKPJ, step 13 — [video at 1:42](https://youtu.be/JOMuD_cF8gM?t=102)
