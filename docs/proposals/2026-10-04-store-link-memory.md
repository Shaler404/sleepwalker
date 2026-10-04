# Proposal: a per-game memory of ad controls that open the store

Date: 2026-10-04. Machine: chrono. Status: proposal (too wide for one night: it needs a new state file, a
decision on how to key it, and a few sessions to see whether it misfires).

## The problem, with sources

An interstitial's top-left "skip" icon or a store-header icon opened the Play Store eight times in six sessions
of two games, 15-90 s lost each time (the ad's timer runs again, `launch`, sometimes a relaunch):

- Pull the Pin, the top-left control at about (45,108) of the model frame: [s:20261003-211035-chrono-2FYKPJ#7],
  [s:20261003-211035-chrono-2FYKPJ#12], [s:20261003-214021-chrono-2FYKPJ#28], [s:20261004-004411-chrono-2FYKPJ#21],
  [s:20261004-005453-chrono-2FYKPJ#4];
- Block Blast!, the top-left >| icon of the store-header interstitial: [s:20261003-212548-chrono-2FYKPJ#27],
  [s:20261003-212548-chrono-2FYKPJ#43], [s:20261003-235233-chrono-2FYKPJ#44] (the third time despite a warning
  in the game's inbox).

The process PR of this date adds a **session** memory: a tap that put `com.android.vending` in front is remembered
by its place on the frame, and the same place is refused for the rest of the session (exit 5, `--force` sends it).
That stops the second tap within a session (211035 #12, 212548 #43) and nothing across sessions: five of the eight
taps were the first of their session.

## The change

1. `state/<game>/store-links.jsonl`: one line per tap that opened the store, written by `note_store_tap`:
   `{t, session, step, fx, fy, hash}` — the place as fractions of the frame and the perceptual hash of the frame
   before the tap (`cur["last_hash"]`).
2. `refuse_store_tap` reads the file at the first tap of a session (cached in `cur["store_links"]`) and refuses a tap
   within `STORE_TAP_NEAR` of a remembered place **when the frame before the tap is the same screen by hash**
   (`is_same_screen`), so a game button that sits where an ad's store icon sat is not blocked: the ad frame and the
   game frame hash differently. Without the hash condition a corner that is a legitimate control on another screen
   (the back arrow of a level, a gear) would be refused.
3. The dream reads the file in `sw.py stats` (a `store_taps` count per session) and the knowledge PR turns a place
   seen in two sessions into a lesson in `wiki/<game>/agent/lessons.md`, as it did by hand this time.
4. `gc` drops lines older than 30 days (ad formats change).

## How to test it

- Fake phone (`tests/`): a session with `fake_app: com.android.vending` set before a tap writes the line; a new
  session of the same game, same frame hash (the fake frames cycle, so the same frame comes back), tap at the same
  place → exit 5 with the earlier session and step in the message; a different frame hash → the tap goes through;
  `--force` goes through.
- On the phone: two Pull the Pin sessions with an interstitial after a win; the second must refuse (45,108) on the
  ad's end card and still allow the back arrow of a level, which is in the same corner.

## Risks

- A false refusal on a game control in the ad's corner when the hash happens to match (a static end card of the
  game itself): `--force` is the way out, and the error step counts it so the dream sees how often it happens.
- Ads are drawn by the game, so the "frame before the tap" is the ad's frame: the hash matches only the same ad
  format, which is the point.
