---
game: com.oakever.meowdoku
title: "Settings"
type: feature
feature: settings
version_seen: 1.18.0
verified_at: 2026-10-02
sources: [20261001-013526-chrono-2FYKPJ, 20261001-022624-chrono-2FYKPJ, 20261001-060942-chrono-2FYKPJ, 20261001-115413-chrono-2FYKPJ]
---

# Settings

Settings is a small popup behind the gear icon. It switches music, sound, voice and vibration on or off.
Opened from Home, it also leads to saving progress with an account, the language choice, the support
centre and the legal links. Opened from a level, it has Pattern Mode (an icon on every colour region)
and Restart for the current level instead [^s2] [^s4].

## Where to find it

The gear at the top right of Home opens the Home version of the
popup [^s2].

![Home: the gear at the top right (circled) opens Settings](../img/20261001-settings-entry-af95700f.webp) [^s1]

The same gear is at the same place in every level. It opens the in-level version (see [Settings in a level](#settings-in-a-level)) [^s4].

## What it looks like

A cream popup titled "Settings" with a close X at the top right. At the top is a row of four toggles:
music, sound, voice and vibration. On version 1.18.0, music is OFF and the other three are ON by default.
Below the toggles are "Save your progress" (with an arrow), the outlined buttons Language and Feedback,
the links Terms of Service and Privacy Policy, and "Version 1.18.0". The Home version has no Pattern Mode
and no Restart [^s2].

![Settings from Home: music OFF; sound, voice and vibration ON; Save your progress; Language; Feedback; Terms of Service and Privacy Policy; Version 1.18.0](../img/20261001-settings-screen-d0163f85.webp) [^s2]

## What you can do

| Tab or button | What it does |
|---|---|
| [Toggles](#toggles) | Music, sound, voice and vibration switch ON/OFF at once (Home and level) |
| [Save your progress](#save-your-progress) | Home only: sign in with Facebook or Google, or delete the account |
| [Language](#language) | Home only: pick the game language and confirm |
| [Feedback](#feedback) | Opens the in-app support centre "Meowdoku Support" (Home and level) |
| [Terms and Privacy](#terms-and-privacy) | Home only: the Terms of Service and Privacy Policy pages open in the browser |
| [Gear in a level](#gear-in-a-level) | The gear inside a level opens the in-level popup |
| [Settings in a level](#settings-in-a-level) | The level version: the toggles, Pattern Mode, Feedback and Restart |
| [Pattern Mode](#pattern-mode) | Level only: draws an icon on every colour region |
| [Restart](#restart) | Level only: an interstitial ad, then the level starts over |

### Toggles

There are four toggles: music (a note), sound (a speaker), voice (a speaking person) and vibration (a
phone). Each one switches ON/OFF as soon as it is tapped, and when it is OFF its icon is crossed out
[^s7] [^s12]. Music is OFF by default and has a red dot. The dot goes away after the first toggle [^s12].
Screenshots cannot show whether the sound or vibration actually changed [^s12].

![All toggles flipped: music ON; sound, voice and vibration OFF; Pattern Mode ON; an OFF toggle's icon is crossed out](../img/20261001-settings-tab-toggles-c1376f3c.webp) [^s7]

### Save your progress

"Save your progress" opens a "Save progress" popup ("Sign in to save your progress!") with "Sign in with
Facebook", "Sign in with Google" and a "Delete Account" link. None of them was tried [^s10].

![Save progress: Sign in with Facebook, Sign in with Google, Delete Account link](../img/20261001-settings-tab-save-your-progress-c12c3f97.webp) [^s10]

### Language

Language opens a list of 9 languages: English (selected, green, with a check mark), Japanese, Spanish,
French, German (Deutsch), Russian, Portuguese, Korean and Turkish, the last one; each shows its own name
with the English name under it. A Confirm button sits under the list [^s9]
[^s15] [^s16]. The player scrolled to the end
and closed it without changing the language [^s17].

> ⚠️ Previously (v1.18.0, 2026-10-01): "Japanese, Spanish, French, Deutsch and more further down" — the
> rest of the list was not seen then.

![Language popup: English selected; Japanese, Spanish, French, Deutsch and more below; Confirm](../img/20261001-settings-tab-language-94276b98.webp) [^s9]

![Language list scrolled to the end: German, Russian, Portuguese, Korean, Turkish (last); Confirm](../img/20261002-settings-language-list-end-94946b2f.webp) [^s16]

### Terms and Privacy

The links **Terms of Service** (222,1120) and **Privacy Policy** (507,1120) at the bottom of the Home
popup leave the game: each opens a page on oakevergames.com in Chrome. The Terms page says "Last
updated: January 1, 2026" [^s18] [^s19]. `sw.py
launch` brought the game back with Settings still open [^s20]
[^s21]. <!-- no-frame: the pages open in another app (Chrome) with its status bar and tabs; not published -->

### Feedback

Feedback opens "Meowdoku Support", an in-app page powered by Helpshift. It has an article search and the tabs
Popular articles, Get Started, General, Account and Settings. Among the articles are How do I play Meowdoku?,
How do I close an ad?, What's the point of the Streak?, How do I place a cat vs. mark an X?, What is the
Daily Challenge? and How do I delete my account data?. At the bottom is a "Chat with us" button. No message
was sent [^s8] [^s13].

![Feedback opens the in-app Helpshift page "Meowdoku Support": article search; tabs Popular articles, Get Started, General, Account, Settings; Chat with us](../img/20261001-settings-tab-feedback-b7916884.webp) [^s8]

### Gear in a level

Every level has the same gear at its top right. It carries a red dot while something inside is new
(Pattern Mode and the music toggle had dots) [^s3] [^s4].

![Level 31: the gear at the top right (circled) of every level, with a red dot while something inside is new](../img/20261001-settings-tab-in-level-eac19571.webp) [^s3]

### Settings in a level

The level version has the same four toggles, then a Pattern Mode switch, Feedback, and an orange Restart
button. It has no Language, no Save your progress and no legal links [^s4].

![Settings in a level: the four toggles; Pattern Mode OFF with a red dot; Feedback; orange Restart; no Language or Save your progress](../img/20261001-settings-tab-in-level-popup-94633e6f.webp) [^s4]

### Pattern Mode

When Pattern Mode is switched ON, a toast says "Pattern Mode On" [^s5]. After that, every colour region
of the board shows its own icon (stars, bells, paws, hearts, yarn, fish bones, sprouts, grass), and the
colours stay [^s11] [^s14]. This is probably meant for colour-blind players (inferred). With Pattern Mode ON the 9×9 level 37 was
played and won as usual [^s14]. Pattern Mode stays ON until it is switched off: it was left ON from
level 43 and was still ON on level 90 [^s22]; it was switched OFF on level 96 (575,758) and the icons went away
[^s23].

![Pattern Mode switched ON: toast "Pattern Mode On"](../img/20261001-settings-tab-pattern-mode-c1356f1f.webp) [^s5]

![Level 31 after Restart with Pattern Mode ON: every colour region carries its own icon (stars, bells, paws, hearts, yarn, fish bones, sprouts, grass); score 0, 3 fish, boosters still 4/4/1](../img/20261001-settings-result-eac395e3.webp) [^s11]

### Restart

Restart first shows an interstitial video ad with a "Next" button at the top left [^s6]. Then the level
starts over: the board is reset, there are 3 fish and the score is 0. Boosters spent in the level are not
refunded (the counters stayed 4/4/1) [^s11]. See [Ads](ads.md).

![Restart first shows an interstitial video ad with a Next button at the top left](../img/20261001-settings-tab-restart-9554396c.webp) [^s6]

## How it works

- Version 1.18.0. The Home popup has the four toggles, Save your progress, Language, Feedback, Terms of
  Service, Privacy Policy and the version line [^s2].
- The in-level popup has the four toggles, Pattern Mode, Feedback and Restart [^s4].
- Defaults: music OFF; sound, voice and vibration ON; Pattern Mode OFF [^s4] [^s12].
- The red dot on a new option disappears after the first toggle [^s12].
- Restart costs an interstitial ad and does not refund spent boosters [^s6] [^s11].

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Open | The gear on Home and in a level | The Home and level versions as above | [^s2] [^s4] |
| Toggles | All four toggles flipped, then restored | They flip at once; the music dot goes away | [^s12] |
| Pattern Mode | Switched ON in level 31 | Toast "Pattern Mode On"; an icon on every region | [^s5] [^s11] |
| Playing with Pattern Mode | Level 37 (9×9) with Pattern Mode ON | Won as usual; the icons do not change the rules | [^s14] |
| Restart | In-level Restart | Interstitial, then a reset board, 3 fish and score 0; boosters not refunded | [^s11] |
| Feedback | Opened from the level popup | The Helpshift "Meowdoku Support" page; nothing sent | [^s13] |
| Language | Opened from Home, scrolled to the end, closed | 9 languages, Turkish last; nothing changed | [^s9] [^s16] |
| Terms and Privacy | Tapped both links in the Home popup | Each opened an oakevergames.com page in Chrome; `launch` came back to Settings | ✅ [^s18] [^s21] |
| Pattern Mode OFF | Switched Pattern Mode OFF on level 96 | The region icons disappeared | ✅ [^s23] |
| Save your progress | Opened from Home, closed | Facebook / Google sign-in, Delete Account; not used | [^s10] |

## Not verified

- Whether the sound, voice and vibration toggles really change the audio and vibration (screenshots cannot
  show it).
- Whether Feedback in the Home popup opens the same page as in a level.

[^s1]: session 20261001-022624-chrono-2FYKPJ, step 66
[^s2]: session 20261001-022624-chrono-2FYKPJ, step 67
[^s3]: session 20261001-013526-chrono-2FYKPJ, step 81 — [video at 16:34](https://youtu.be/T86pLfervRE?t=994)
[^s4]: session 20261001-013526-chrono-2FYKPJ, step 82 — [video at 16:46](https://youtu.be/T86pLfervRE?t=1006)
[^s5]: session 20261001-013526-chrono-2FYKPJ, step 83 — [video at 16:57](https://youtu.be/T86pLfervRE?t=1017)
[^s6]: session 20261001-013526-chrono-2FYKPJ, step 84 — [video at 17:03](https://youtu.be/T86pLfervRE?t=1023)
[^s7]: session 20261001-022624-chrono-2FYKPJ, step 21
[^s8]: session 20261001-022624-chrono-2FYKPJ, step 23
[^s9]: session 20261001-022624-chrono-2FYKPJ, step 68
[^s10]: session 20261001-022624-chrono-2FYKPJ, step 70
[^s11]: session 20261001-013526-chrono-2FYKPJ, step 85 — [video at 17:28](https://youtu.be/T86pLfervRE?t=1048)
[^s12]: session 20261001-022624-chrono-2FYKPJ, step 30
[^s13]: session 20261001-022624-chrono-2FYKPJ, step 27
[^s14]: session 20261001-022624-chrono-2FYKPJ, step 35

[^s15]: session 20261001-060942-chrono-2FYKPJ, step 2 — [video at 0:31](https://youtu.be/hiHOk1whnok?t=31)
[^s16]: session 20261001-060942-chrono-2FYKPJ, step 4 — [video at 0:50](https://youtu.be/hiHOk1whnok?t=50)
[^s17]: session 20261001-060942-chrono-2FYKPJ, step 5 — [video at 1:00](https://youtu.be/hiHOk1whnok?t=60)
[^s18]: session 20261001-115413-chrono-2FYKPJ, step 2 — [video at 0:30](https://youtu.be/ATvMZzri7O8?t=30)
[^s19]: session 20261001-115413-chrono-2FYKPJ, step 4 — [video at 0:58](https://youtu.be/ATvMZzri7O8?t=58)
[^s20]: session 20261001-115413-chrono-2FYKPJ, step 3 — [video at 0:49](https://youtu.be/ATvMZzri7O8?t=49)
[^s21]: session 20261001-115413-chrono-2FYKPJ, step 5 — [video at 1:13](https://youtu.be/ATvMZzri7O8?t=73)
[^s22]: session 20261001-115413-chrono-2FYKPJ, step 43 — [video at 15:13](https://youtu.be/ATvMZzri7O8?t=913)
[^s23]: session 20261001-115413-chrono-2FYKPJ, step 75 — [video at 25:42](https://youtu.be/ATvMZzri7O8?t=1542)
