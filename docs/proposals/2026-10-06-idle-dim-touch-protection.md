# Proposal: keep the phone from dimming during long waits (off unless local.yaml turns it on)

Date: 2026-10-06. Machine: chrono. Status: proposal (the fix drives the phone during `wait` and needs the
phone to validate: which input keeps the screen awake without touching the game, and whether the dim is
what brings the protection up).

## The problem, with sources

Four sessions ended `blocked` the same way: a run of `wait` calls with no touch in between, the screen
dimmed, the next `tap` refused with exit 3 "touches are blocked by Samsung accidental touch protection"
(the `IgniteTouchProtectionPresenter` window visible), and the session ended.

| Session | Waits before the block | Last touch to the dim | Lost |
|---|---|---|---|
| `20261004-001002-chrono-2FYKPJ#2` (Pull the Pin) | 30+30+20+40+20 s | about 3 min | a rewarded-ad reward never claimed |
| `20261005-141756-chrono-2FYKPJ#23` (Pull the Pin) | 60+60+60+60 s | about 3 min after the `restart` | the map-chest timer experiment |
| `20261005-145445-chrono-2FYKPJ#0` (Pull the Pin) | 60+60+60 s | the session had made no touch at all | the whole session: 0 steps, blocked |
| `20261005-151039-chrono-2FYKPJ#37` (Pull the Pin) | 60+45 s | 2.7-3.6 min after the tap of step 37 | the chest-open follow-up |

What the records say:

- Every block follows a `wait` step with `screen: dimmed`; no block happened without one. The `wait`
  warning said "Tap something harmless now" and the tap was refused each time (the harness guard refuses
  a tap while the protection window is visible, by design: an injected tap would be swallowed by the
  overlay). This dream changes the warning: `wait` now looks for the protection window and says which of
  the two it is (`touch_blocked` in the reply and the step).
- The dim comes about 3 minutes after the last touch, while `start` reports `timeout_s: 600` and
  `stay_awake: true` (`android.stay_awake` keeps the screen on while charging, but a screen kept on
  still dims). The power state at the refusal reads `brightness 87, wakefulness Awake, dimmed False`:
  by then the dim itself is over and only the protection overlay is left.
- Nothing covered the sensor: `145445` started 3 minutes after `141756` ended blocked, took two frames
  and a mark without a touch, waited 3 minutes and was blocked. The protection had cleared by itself
  between 14:58 and 15:10 (`151039` tapped fine from its first step). So the overlay comes with the
  idle dim and goes away on its own, within about 12 minutes.
- `screen_settings` already warns when `settings get system accidental_touch_protection` reads `1`;
  the key is unverified on this phone (an unknown key reads `null` and warns nothing).

Cost: four blocked sessions, one of them empty; the Pull the Pin map-chest experiment (a 10-minute
timer) could not be run in three attempts; the inbox asks for "a keep-awake during wait; a long timer wait
on the map needs periodic harmless taps" (`state/com.maroieqrwlk.unpin/inbox.md`, session 145445).

## The change

`android.keep_awake: <input>` in `local.yaml`, default off (a phone setting or input the owner did not
ask for is never sent by default). When set, `wait` sleeps in slices of at most 50 s and sends the
configured input between slices, so the user-activity timer never reaches the dim. The wait step records
`nudges: N`. Nothing is changed in the phone's settings; the only effect is one input event per slice.

Which input is "harmless" is the open question, to settle on the phone, from the least to the most
intrusive:

1. `input keyevent KEYCODE_SHIFT_LEFT` (a modifier alone: no character, no navigation). Open: whether
   an injected key event resets the activity timer on this phone (Android's `InputDispatcher` pokes
   user activity for dispatched events; injected events included, as far as the sources say, but it
   is not measured here).
2. `input keyevent KEYCODE_WAKEUP` when `power_state` says the screen has dimmed (it brightens a
   dimmed screen; it does nothing when the screen is already awake, so it cannot prevent the dim, only
   cut it short before the protection overlay appears — if the overlay follows the dim with a delay).
3. The owner's switch: Settings > Display > Accidental touch protection off on the phone. The harness
   cannot do this (a phone setting), but `screen_settings` should confirm which key the setting uses so
   its warning fires.

A second, independent step for `guard`: when the overlay is visible and `power_state` says the screen is
dimmed, try `KEYCODE_WAKEUP` once and look again before refusing. This only helps if the overlay goes
away with the dim; `145445`'s timing says it stays longer.

## How to test it

- On the phone, in the lab or a slot the owner gives: `wait 60` eight times with `keep_awake` off, then
  with each candidate input; after every wait, `power_state` and `touch_blocked` (both are one `dumpsys`
  each). The input that keeps `dimmed: false` and `touch_blocked: false` through 8 minutes, with the game
  unchanged on the frames (`same: true` on every wait step), is the one to keep as the default value of
  the option (still off by default).
- The real use: the Pull the Pin map-chest timer (10 minutes on the map, `state/com.maroieqrwlk.unpin/
  research.yaml`, task `chest-open-followup`): one session with the option on ends with the chest opened.
- With the fake phone: `wait 120` with `keep_awake` set sends the input twice and records `nudges: 2`;
  without it, none (the fake device counts its inputs).
