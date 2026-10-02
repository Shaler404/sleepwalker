# The game's own window is reported as another app when its window title has no package name

Status: proposed by the dream (chrono, 2026-10-02). Change in `harness/sw.py` (`focus`, `focus_window`).

## The problem

`focus()` reads `mCurrentFocus=Window{<hash> u0 <name>}` from `dumpsys window` and returns `<name>`. For an
activity the name is `package/activity`; for a window the app creates with its own title, the name is that
title. The King account panel in Candy Crush Saga is such a window, named "Panel":

- Candy Crush Saga 20261001-232021-chrono-2FYKPJ: ten steps with `app: "Panel"` [s:20261001-232021-chrono-2FYKPJ#1]
  [s:20261001-232021-chrono-2FYKPJ#3] [s:20261001-232021-chrono-2FYKPJ#11] [s:20261001-232021-chrono-2FYKPJ#13];
  `launch` at [s:20261001-232021-chrono-2FYKPJ#2] "returned" to a game that was already in front;
  `mark` refuses frames whose app is not the game, so the account panel (carousel, login form, "Privacy and
  security") could not be marked.
- Candy Crush Saga 20261001-202316-chrono-2FYKPJ: the first-launch Terms popup is the same kind of window; its
  only frame was recorded as not the game [s:20261001-202316-chrono-2FYKPJ#0].

The documenter shipped `account-retrieve` and `consent` without screen frames and described the panel in
words (`state/com.king.candycrushsaga/docs-log.md`); the player wrote the gap into the inbox twice. The wiki
rule is right (frames from other apps carry personal data and do not go to the wiki); the detection is wrong.

## The change

`focus()` returns the **package** of the focused window:

1. If the name has the form `package/activity`, the package as today.
2. Otherwise, the package of `mFocusedApp=ActivityRecord{… u0 <package>/<activity> …}` from the same
   `dumpsys window` output (the activity that owns the focused window), with the window title kept in the step
   record as `window` for debugging. If neither is readable, `None` as now.

`focus_window()` (the billing-sheet check) keeps the raw name: the payment regex matches the activity.

## How to test

- On the phone, open the King panel (title screen → Retrieve My Progress) in a test session: `shot` reports
  `app: com.king.candycrushsaga`, the step has `window: Panel`, `mark` accepts the frame.
- Open a Play Store listing: `app: com.android.vending` as before; open a billing sheet in a test app: the
  sheet is still closed and logged as `payment_sheet_closed`.
- The Android permission dialog still reports `com.google.android.permissioncontroller`.
