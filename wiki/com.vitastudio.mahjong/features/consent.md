---
game: com.vitastudio.mahjong
title: "Terms consent"
type: feature
feature: consent
version_seen: 3.40.1
verified_at: 2026-10-03
sources: [20261003-195050-chrono-2FYKPJ, 20261003-231804-chrono-2FYKPJ]
---

# Terms consent

The first window of a fresh install: the game asks the player to accept its Terms of Service and Privacy
Policy before anything else. It has a single Accept button and no way to decline [^s1].

## Why it appeared

The first launch of a fresh install, before the loading screen [^s1].

## Where to find it

<!-- no-entry: no control opens it; it shows by itself on the first launch of a fresh install -->
No button opens it: it is the first thing on screen after a fresh install [^s1]. The same two documents
stay reachable later from Settings > About (see [Settings](settings.md)).

## What it looks like

![A dark green screen with the tile mascot winking over a card: "Welcome to Vita Mahjong!", "Please read and accept our Terms of Service and Privacy Policy.", one green Accept button](../img/20261003-consent-screen-d1d96a24.webp) [^s1]
*The consent window: two linked documents in the text and one Accept button*

- The title "Welcome to Vita Mahjong!" [^s1].
- One sentence with "Terms of Service" and "Privacy Policy" as links [^s1].
- One green Accept button; no decline and no close button [^s1].

## What you can do

| Tab or button | What it does |
|---|---|
| [Accept](#accept) | Closes the window; the Android notification permission prompt follows, then the loading screen |
| [Terms of Service, Privacy Policy](#terms-of-service-privacy-policy) | Links in the text; not tapped |

### Accept

<!-- no-frame: the button is on the consent frame above; the next screen was the system's -->
After Accept, Android asked whether to allow the game's notifications (a system dialog, not shown here);
the session chose "Don't allow". The loading screen followed (see [Loading screen](loading.md)) [^s2].

### Terms of Service, Privacy Policy

<!-- no-frame: the links are on the consent frame above -->
Not tapped in this session.

## How it works

Version 3.40.1. Shown once, on the first launch of a fresh install [^s1]. A later launch that reopened
the game at Level 1 with the age popup went logo > loading > home without it [^s3]. Accept is the only way on
[^s1]. The notification permission is asked right after it [^s2].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Welcome window: Terms of Service and Privacy Policy links, one Accept button, no decline <!-- case:chk-screen --> | Fresh install, first launch | ✅ | [^s1] |
| No entry: shown by itself on the first launch of a fresh install <!-- case:chk-entry --> | Fresh install | ✅ | [^s1] |
| Why it appeared: the trigger that brought it up (the first launch, a level won, a threshold, a timer, a loss): a fact with its frame, or a hypothesis to test <!-- case:chk-appeared --> | Fresh install | ✅ First launch | [^s1] |
| Every option or button and what it changes (each toggle once, set back after) <!-- case:chk-options --> | Tapped Accept | ✅ The only button: notification prompt, then loading | [^s2] |
| For a prompt (consent, rate us, notifications): what each answer does and whether it comes back <!-- case:chk-answers --> | Tapped Accept; relaunched later | ✅ There is no decline; Accept leads on to the loading screen. The window did not come back on later launches, even one that reopened at Level 1 with the age popup | [^s2] [^s3] |
| Links out (privacy, terms, help): where they lead (back to the game at once) <!-- case:chk-links --> | — | not verified: links not tapped |  |

## Not verified

- Whether the consent comes back after an update or a full reinstall
- Links out: where Terms of Service and Privacy Policy lead <!-- case:chk-links -->

[^s1]: session 20261003-195050-chrono-2FYKPJ, step 0 — [video at 0:00](https://youtu.be/KUKs3cQ-xqY?t=0)
[^s2]: session 20261003-195050-chrono-2FYKPJ, step 2 — [video at 0:35](https://youtu.be/KUKs3cQ-xqY?t=35)
[^s3]: session 20261003-231804-chrono-2FYKPJ, step 0 — [video at 0:00](https://youtu.be/ssTmhwls_uc?t=0)
