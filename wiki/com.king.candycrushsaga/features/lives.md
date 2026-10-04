---
game: com.king.candycrushsaga
title: "Lives"
type: feature
feature: lives
version_seen: 1.337.0.2
verified_at: 2026-10-03
sources: [20261003-194350-chrono-2FYKPJ, 20261003-230937-chrono-2FYKPJ]
---

# Lives

The number of attempts at levels the player has, shown as a heart in the map's top bar: 5 and "Full" on a
fresh install. A tap opens a Lives popup with the count, the time to the next life and offers of unlimited
lives for gold bars, from friends or for real money [^s1].

## Why it appeared

The heart is in the map's top bar from the first view of the map, after level 1, at 5 Full; the level 1 top
bar also showed "heart 5" [^s2] [^s3].

## Where to find it

The pink heart with 5 and "Full", left of the avatar in the map's top bar; it stays in the top bar on the
Events, Social and Shop tabs [^s2].

![The level map; the heart with 5 and Full is in the top bar, between the envelope and the avatar](../img/20261003-lives-entry-9af4f0af.webp) [^s2]
*Heart with 5 and Full, left of the avatar in the top bar of the map*

## What it looks like

![The Lives popup: 5 lives, Next life Full, 6 hours of unlimited lives for 69 gold bars, Ask friends; below, a real-money offer of 10 minutes of unlimited lives and a 5-minute colour bomb (price blacked out)](../img/20261003-lives-screen-d0d86a6c.webp) [^s1]
*The Lives popup at 5 Full; the real-money price is blacked out (local currency)*

A popup titled "Lives" with a red X. Top left, the gold bar balance (0) with a green plus. A large heart with
5 and "Next life: Full". In the middle, an offer card: a heart with an infinity sign, a stopwatch "6h" and a
green button "69" with a gold bar. Under it a pink "Ask friends" button. Below the popup a second card: an
infinity heart with "10m" and a colour bomb with "5m", for a real-money price. At the bottom the note
"Lives will be fully restored after Unlimited Lives expire" [^s1].

## What you can do

| Tab or button | What it does |
|---|---|
| [Unlimited lives for gold bars](#unlimited-lives-for-gold-bars) | 6 hours for 69 gold bars; not bought |
| [Ask friends](#ask-friends) | Not tapped |
| [Real-money offer](#real-money-offer) | 10 minutes of unlimited lives and a 5-minute colour bomb; not tapped |
| [Gold bar balance](#gold-bar-balance) | 0, with a green plus; not tapped |

The X closes the popup to the screen behind [^s4].

### Unlimited lives for gold bars

<!-- no-frame: the card is on the popup frame above -->
The middle card: an infinity heart, a stopwatch "6h", a green button "69" with a gold bar [^s1]. Not
tapped: the balance was 0.

### Ask friends

<!-- no-frame: the button is on the popup frame above -->
A pink button under the card [^s1]. Not tapped (it acts on other players). See [Friends list](friends.md).

### Real-money offer

<!-- no-frame: the card is on the popup frame above -->
A card hung under the popup: an infinity heart with "10m" and a colour bomb with "5m", and a green price
button in real money (blacked out) [^s1]. Not tapped.

### Gold bar balance

<!-- no-frame: the balance is on the popup frame above -->
Top left of the popup: a gold bar, 0, and a green plus [^s1]. Inferred: the plus opens the
[Shop](shop.md); not tapped.

## How it works

Version 1.337.0.2 [^s1]:

- Maximum shown: 5 lives; at 5 the timer reads "Full".
- Unlimited lives: 6 hours for 69 gold bars; 10 minutes (with a 5-minute colour bomb) in the real-money
  offer; 30 minutes in the Shop's Daily Deal (see [Shop](shop.md)) [^s5].
- After unlimited lives expire, lives are fully restored (the popup's note).

Force-stopping the app in the middle of a level, with no move made, cost one life (4 to 3) and showed a
refill timer in the map's top bar [^s6]. Inferred: a lost level also costs
one life; not verified.

## Cases

| Case | What was done | Result | Source |
|---|---|---|---|
| Why it appeared <!-- case:chk-appeared --> | First map view | ✅ The heart at 5 Full in the top bar | [^s2] |
| Where to find it <!-- case:chk-entry --> | Tapped the heart | ✅ The Lives popup opened | [^s1] |
| What it looks like <!-- case:chk-screen --> | Looked at the popup | ✅ As above | [^s1] |
| What it does <!-- case:chk-effect --> | — | not verified: no life spent |  |
| The balance <!-- case:chk-balance --> | Read the top bar and the popup | ✅ 5, "Full", in the map's top bar and the level's top bar | [^s1] |
| Sources <!-- case:chk-sources --> | Read the popup and the Shop | ✅ partly: unlimited lives for gold bars, real money, the Daily Deal; Ask friends not tried | [^s1] |
| Sinks <!-- case:chk-sinks --> | — | not verified: no level lost |  |
| At zero <!-- case:chk-empty --> | — | not verified |  |
| Leaving the app mid level <!-- case:sink-exit-app --> | Opened level 4, made no move, force-stopped the app and reopened it | ✅ One life spent: the game reopened on the map with 3 lives (was 4) and a refill timer at 24:05; the level was not resumed | [^s6] |
| Refill timer <!-- case:chk-refill --> | — | not verified: lives were full ("Next life: Full") |  |

## Not verified

- What one life does and when it is spent (a lost level, a quit) <!-- case:chk-effect --> <!-- case:chk-sinks -->
- What Ask friends sends, and whether friends' lives arrive <!-- case:chk-sources -->
- The screen and offers at 0 lives <!-- case:chk-empty -->
- The time to regain one life <!-- case:chk-refill -->

[^s1]: session 20261003-194350-chrono-2FYKPJ, step 16 — [video at 3:53](https://youtu.be/OjVVcEHXMyI?t=233)
[^s2]: session 20261003-194350-chrono-2FYKPJ, step 7 — [video at 2:16](https://youtu.be/OjVVcEHXMyI?t=136)
[^s3]: session 20261003-194350-chrono-2FYKPJ, step 3 — [video at 0:29](https://youtu.be/OjVVcEHXMyI?t=29)
[^s4]: session 20261003-194350-chrono-2FYKPJ, step 17 — [video at 4:04](https://youtu.be/OjVVcEHXMyI?t=244)
[^s5]: session 20261003-194350-chrono-2FYKPJ, step 14 — [video at 3:34](https://youtu.be/OjVVcEHXMyI?t=214)

[^s6]: session 20261003-230937-chrono-2FYKPJ, step 12 — [video at 2:12](https://youtu.be/QXlart4AJGo?t=132)
