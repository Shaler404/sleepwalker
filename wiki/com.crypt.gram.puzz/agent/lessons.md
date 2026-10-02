---
game: com.crypt.gram.puzz
title: Lessons
type: agent
version_seen: 3.6.1
verified_at: 2026-10-02
sources: [20261001-020937-chrono-2FYKPJ, 20261001-050941-chrono-2FYKPJ, 20261001-071926-chrono-2FYKPJ, 20261001-092740-chrono-2FYKPJ, 20261001-114433-chrono-2FYKPJ, 20261001-190315-chrono-2FYKPJ, 20261001-192245-chrono-2FYKPJ, 20261001-224924-chrono-2FYKPJ]
---

# Lessons for the agent: Cryptogram

- Never read, decode or write the quote text of a board (plans, `--why`, notes, marks, summary). Four
  sessions ended with the model's output blocked by the content filter right after the level 16 board
  loaded, losing the notes, the race finish and the rest of the plan. Refer to levels by number and to
  letters by counts; let the solver read the board.
  *Confirmed: 20261001-071926-chrono-2FYKPJ, 20261001-092740-chrono-2FYKPJ, 20261001-114433-chrono-2FYKPJ, 20261001-192245-chrono-2FYKPJ, 3.6.1.*
  [s:20261001-071926-chrono-2FYKPJ#69] [s:20261001-092740-chrono-2FYKPJ#9] [s:20261001-114433-chrono-2FYKPJ#18] [s:20261001-192245-chrono-2FYKPJ#17]
- Take tap coordinates only from the frame you are looking at. On level 9 keyboard coordinates of
  the 730-px frame were sent after a `shot --hi` (918x1988) frame, the tap landed on the "+20 /
  RSD 399" hint pack and opened a real Google Play sheet with 1-tap buy (backed out, nothing bought).
  *Confirmed: 20261001-020937-chrono-2FYKPJ, 3.6.1 (frame of the payment sheet, not published).* [s:20261001-020937-chrono-2FYKPJ#9]
- Never tap No ADS on the main screen or the ADS toggle in Settings: both open the Google Play payment
  sheet at once. The second tap came after the player's own note about the first.
  *Confirmed: 20261001-071926-chrono-2FYKPJ, 3.6.1 (payment sheets closed by sw.py).* [s:20261001-071926-chrono-2FYKPJ#27] [s:20261001-071926-chrono-2FYKPJ#51]
- An interstitial on a level start: tap its skip icon at the top left as soon as it shows, then Back
  once, then launch if the screen is blank. Waiting lets the ad open the store and end on a card with no
  close.
  *Confirmed: 20261001-092740-chrono-2FYKPJ, 20261001-114433-chrono-2FYKPJ, 20261001-192245-chrono-2FYKPJ, 3.6.1.*
  [s:20261001-092740-chrono-2FYKPJ#9] [s:20261001-114433-chrono-2FYKPJ#18] [s:20261001-192245-chrono-2FYKPJ#17]
- A playable or end card with no working close: `sw.py restart --why ...` (force-stop and start) leaves
  it within seconds and keeps the progress; do not wait 60-90 s first (waiting never helped and cost
  about 7 min in one session).
  *Confirmed: 20261001-071926-chrono-2FYKPJ, 20261001-114433-chrono-2FYKPJ, 20261001-224924-chrono-2FYKPJ, 3.6.1.*
  [s:20261001-071926-chrono-2FYKPJ#41] [s:20261001-071926-chrono-2FYKPJ#66] [s:20261001-114433-chrono-2FYKPJ#6] [s:20261001-224924-chrono-2FYKPJ#3]

  > ⚠️ Previously (v3.6.1, 2026-10-01): "`sw.py restart` … is the next thing to try — not yet verified
  > here." Verified since: it worked every time it was used.

- Do not repeat restart + CONTINUE: after two ad loops on the same entry, change the approach (skip
  early, another entry such as the Daily Challenge card). Two sessions spent their whole budget on 5
  and 4 identical loops.
  *Confirmed: 20261001-190315-chrono-2FYKPJ, 20261001-224924-chrono-2FYKPJ, 3.6.1.* [s:20261001-190315-chrono-2FYKPJ#25] [s:20261001-224924-chrono-2FYKPJ#16]
- When an ad's Play Store listing is in front, press Back first: launch and restart leave the store in
  front (about 1.5-3 min lost per session).
  *Confirmed: 20261001-190315-chrono-2FYKPJ, 20261001-192245-chrono-2FYKPJ, 20261001-224924-chrono-2FYKPJ, 3.6.1.*
  [s:20261001-190315-chrono-2FYKPJ#12] [s:20261001-192245-chrono-2FYKPJ#8] [s:20261001-224924-chrono-2FYKPJ#7]
- Once a level is won, an ad with no close after NEXT costs nothing: restart at once, the win stays.
  *Confirmed: 20261001-071926-chrono-2FYKPJ, 3.6.1 (twice: Daily Challenge 1/31 kept, secret level kept).* [s:20261001-071926-chrono-2FYKPJ#41] [s:20261001-071926-chrono-2FYKPJ#59]
- Count the dots of every lock before a batch (one dot: typed in order; two dots: on the wrap-around),
  and re-read the board after a Restart because the locks move.
  *Confirmed: 20261001-050941-chrono-2FYKPJ, 3.6.1 (lost level 13 frame).* [s:20261001-050941-chrono-2FYKPJ#72] [s:20261001-050941-chrono-2FYKPJ#74]
- On card levels the board scrolls by itself: one pair per call when the target is low, a fresh shot
  after it. Stale coordinates cost 9 min, about 170 moves and a life on event level 1.
  *Confirmed: 20261001-050941-chrono-2FYKPJ, 3.6.1 (lost event level frame).* [s:20261001-050941-chrono-2FYKPJ#44] [s:20261001-050941-chrono-2FYKPJ#46]
