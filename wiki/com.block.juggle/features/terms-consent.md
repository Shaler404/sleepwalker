---
game: com.block.juggle
title: "Terms of Use consent"
type: feature
feature: terms-consent
version_seen: 10.8.1
verified_at: 2026-10-06
sources: [20261003-193423-chrono-2FYKPJ, 20261006-032721-chrono-2FYKPJ]
---

# Terms of Use consent

The first thing a fresh install shows: a welcome window that asks the player to accept the Terms of Use
and read the Privacy Policy, with a single button to accept [^s1].

## Why it appeared

First launch of a fresh install, before anything else [^s1].

## Where to find it

<!-- no-entry: no control opens it; it is shown by itself on the first launch of a fresh install -->
It is shown by itself on the first launch; no button in the game opens it [^s1]. On an install past the
first launch the window did not come back, but the two documents it names open from the gear on the
classic board > More Settings > Terms of Service and Privacy Policy: pages inside the game, with no Accept
button [^s2] [^s4] [^s5].

## What it looks like

![The first-launch window: the Block Blast logo, a pixel emoji, the welcome text with Terms of Use and Privacy Policy links, and the green Accept Terms of Use button](../img/20261003-terms-consent-screen-cc493b33.webp) [^s1]
*The consent window: two links in the text and one green button; there is no decline option*

A blue panel under the game's logo and a pixel-art emoji. The text welcomes the player and asks them to
accept the Terms of Use and read the Privacy Policy; both names are cyan links. One green button, "Accept
Terms of Use". No decline or close button [^s1].

## What you can do

| Tab or button | What it does |
|---|---|
| [Accept Terms of Use](#accept-terms-of-use) | Closes the window and opens the tutorial board |
| [Terms of Use and Privacy Policy links](#terms-of-use-and-privacy-policy-links) | Not tapped in the window; the same documents open from More Settings |

### Accept Terms of Use

<!-- no-frame: the button is on the consent frame above -->
The window closes and the [tutorial board](tutorial.md) appears [^s3].

### Terms of Use and Privacy Policy links

![The Terms of Use page opened from More Settings: the title, Last Updated Aug 5, 2026 and the opening paragraphs naming Hungry Studio and ARETIS LIMITED](../img/20261006-terms-consent-screen-bb917584.webp) [^s4]
*The Terms of Use document, opened from Settings > More Settings > Terms of Service (the phone's navigation bar blacked out)*

Cyan words in the text [^s1]. In the consent window they were not tapped. The documents they name open
from More Settings on a progressed install: Terms of Service opens a white page "Terms of Use" (last
updated Aug 5, 2026; Hungry Studio, operated by ARETIS LIMITED; numbered sections from Definitions), text
only with no Accept button [^s4]; Privacy Policy opens a separate page "Privacy Policy" of the same date
[^s6]. The Back key returns from either to the classic board [^s5]. See [Settings](settings.md#more-settings).

## How it works

Version 10.8.1. Accepting is the only way into the game; after it the window was not seen again, in the
first session nor in later sessions on the same install [^s1] [^s3] [^s5].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Welcome window with Terms of Use and Privacy Policy links and one Accept button; no decline <!-- case:chk-screen --> | Fresh install | ✅ | [^s1] |
| Why it appeared <!-- case:chk-appeared --> | Fresh install | ✅ First launch, before anything else | [^s1] |
| Where to find it <!-- case:chk-entry --> | Fresh install; later gear > More Settings > Terms of Service | ✅ The window has no entry: shown by itself on the first launch; the Terms of Use document reopens from More Settings | [^s1] [^s4] |
| Every option or button and what it changes <!-- case:chk-options --> | Tapped Accept | not verified: Accept opens the tutorial; the rest of the window (links, any way to decline) not walked | [^s3] |
| What each answer does and whether it comes back <!-- case:chk-answers --> | Accepted | not verified: whether it comes back after a reinstall or an update not checked |  |
| Links out (terms, privacy): where they lead <!-- case:chk-links --> | Opened Terms of Service and Privacy Policy from More Settings | ✅ Two pages inside the game, Terms of Use and Privacy Policy, updated Aug 5, 2026; text only; Back returns to the board | [^s4] [^s6] [^s5] |

## Not verified

- Every control of the window on a fresh install: the links tapped inside the window, whether it can be declined or closed <!-- case:chk-options -->
- Whether the window comes back (a reinstall, an updated policy) <!-- case:chk-answers -->

[^s1]: session 20261003-193423-chrono-2FYKPJ, step 0 — [video at 0:00](https://youtu.be/A6Wh-xa4ryg?t=0)

[^s2]: session 20261003-193423-chrono-2FYKPJ, step 6 — [video at 1:21](https://youtu.be/A6Wh-xa4ryg?t=81)
[^s3]: session 20261003-193423-chrono-2FYKPJ, step 1 — [video at 0:13](https://youtu.be/A6Wh-xa4ryg?t=13)
[^s4]: session 20261006-032721-chrono-2FYKPJ, step 17 — [video at 2:15](https://youtu.be/nugMYVUvpqk?t=135)
[^s5]: session 20261006-032721-chrono-2FYKPJ, step 47 — [video at 6:27](https://youtu.be/nugMYVUvpqk?t=387)
[^s6]: session 20261006-032721-chrono-2FYKPJ, step 13 — [video at 1:47](https://youtu.be/nugMYVUvpqk?t=107)
