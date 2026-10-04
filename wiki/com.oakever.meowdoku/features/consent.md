---
game: com.oakever.meowdoku
title: "Terms consent popup"
type: feature
feature: consent
version_seen: 1.19.1
verified_at: 2026-10-03
sources: [20261003-200440-chrono-2FYKPJ]
---

# Terms consent popup

A "Welcome" popup that asks the player to accept the Terms of Service and the Privacy Policy before the game
starts. It has one button, Accept; there is no decline button and no close cross [^s1].

## Why it appeared

First launch, Welcome popup with Accept [^s1]. It came up over the loading screen on the first launch of a
fresh install, after the publisher's splash screen [^s1].

## Where to find it

<!-- no-entry: no control opens it; it comes up by itself over the loading screen on the first launch -->

No control opens it: it shows by itself on the first launch, over the loading screen (a loading bar with a
cat and a tip card signed by the game) [^s1]. Whether it can be reopened later (for example from the Terms of
Service and Privacy Policy links in [Settings](settings.md)) was not checked.

## What it looks like

![Accept Terms of Service and Privacy Policy](../img/20261003-consent-screen-95976e6c.webp) [^s1]
*The Welcome popup over the loading screen: the Terms of Service and Privacy Policy links in the text, the orange Accept button*

- Title: "Welcome".
- One line of text with two green underlined links: Terms of Service and Privacy Policy.
- One orange button: Accept.

## How it works

- Accept closes the popup. Right after it, the Android system asked for permission to send notifications
  (a system dialog, not the game's); the player answered "Don't allow", and the game opened on Home with the
  event popup [Fish rank event](fish-event.md) on top [^s2] [^s3].
- Inferred: the notification request is tied to accepting the terms, since it came right after Accept; it
  was seen once only.

Version 1.19.1.

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared: the trigger that brought it up (the first launch, a level won, a threshold, a timer, a loss): a fact with its frame, or a hypothesis to test <!-- case:chk-appeared --> | Fresh install launched: the Welcome popup showed over the loading screen | ✅ | [^s1] |
| What it looks like: its screen (mark --as screen) <!-- case:chk-screen --> | Frame marked on the first launch: title, text with two links, Accept | ✅ | [^s1] |
| Where to find it: the screen and the button that open it (mark --as entry --at X,Y) <!-- case:chk-entry --> | No control opens it; it shows by itself | not verified |  |
| Every option or button and what it changes (each toggle once, set back after) <!-- case:chk-options --> | Accept tapped: the popup closed, a system notification request followed; no other button exists | not verified | [^s2] |
| For a prompt (consent, rate us, notifications): what each answer does and whether it comes back <!-- case:chk-answers --> | Accept tapped once; whether it comes back (a second launch, a reinstall) was not checked | not verified | |
| Links out (privacy, terms, help): where they lead (back to the game at once) <!-- case:chk-links --> | Not tapped | not verified |  |

## Not verified

- Where to find it: whether any screen reopens it <!-- case:chk-entry -->
- Every option or button: Accept is the only one; it was tapped once (see How it works) <!-- case:chk-options -->
- What each answer does and whether the popup comes back on a later launch <!-- case:chk-answers -->
- Where the Terms of Service and Privacy Policy links lead <!-- case:chk-links -->

[^s1]: session 20261003-200440-chrono-2FYKPJ, step 0 — [video at 0:00](https://youtu.be/Pqx4QY-FpBA?t=0)

[^s2]: session 20261003-200440-chrono-2FYKPJ, step 1 — [video at 0:22](https://youtu.be/Pqx4QY-FpBA?t=22)
[^s3]: session 20261003-200440-chrono-2FYKPJ, step 2 — [video at 0:30](https://youtu.be/Pqx4QY-FpBA?t=30)
