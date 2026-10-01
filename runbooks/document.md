# Documenter: the session's features as wiki pages

Instructions for the documenter (`sleepwalker-documenter`). The orchestrator starts you right after a
player ends a session, next to the post-session review; you do not touch the phone. The brief gives
the repository root, the game and the session id. You write the pages a human reads: the player only
plays and marks frames, the dream only publishes your pages and improves the process.

Run every command from the root: `cd <root> && python harness/sw.py …`.

## Which pages

The features the session touched: the `feature` and `case` ops and the frames marked with
`--feature` in `raw/<game>/<session>/steps.jsonl`. For each of them, the page is
`state/<game>/pages/features/<id>.md` (frames in `state/<game>/pages/img/`).

## The page

A reader who never saw the game must understand from the page where the feature is, what it looks like
and what can be done in it. The layout (schema, section 3):

1. One paragraph: what the feature is for the player.
2. `## Where to find it` — from which screen and which button; the frame of that screen with the button
   circled.
3. `## What it looks like` — the feature's screen, and what on it matters.
4. `## What you can do` — a table of its tabs and buttons, each linking to its own `### <tab>` section
   with its frame and what it shows.
5. `## How it works` — rules, timers, prices, rewards: numbers with the version.
6. `## Cases` — every case: what was done, the result, the source.
7. `## Not verified`.

Sources are footnotes `[^sN]` that link the moment in the YouTube original; never inline `[s:…]`.

## How

1. `python harness/sw.py page-skeleton <game> <feature> --out state/<game>/pages` lays the page out
   from the frames marked for the feature (the latest frame for each place) with the footnotes. If the
   page already exists, the skeleton is written as `<feature>.skeleton.md`: merge it into the page
   (new frames and facts in, nothing true thrown away), then delete the skeleton.
2. A place without a frame (`<!-- no frame marked as … -->`): look through the session's frames
   (`raw/<game>/<session>/shots/NNNNN_m.jpg`, the marked ones first) and tag the right one:
   `python harness/sw.py mark-tag <game> <session> <shot> --feature <id> --as entry|screen|tab:<name> --desc "…" [--at X,Y]`
   (`--at` — the button to circle, in pixels of the `_m.jpg` frame), then run the skeleton again. If
   the session has no such frame, write `<!-- no-entry: why -->` / `<!-- no-screen: why -->` and add the
   gap to the session's block in `state/<game>/inbox.md` so the next study goal marks it.
3. Write the text: from the session's `why`, notes, cases and the frames themselves. Facts only, each
   with its footnote; what you infer is marked as such.
4. `python harness/sw.py check-pages state/<game>/pages` until it reports no problems for your pages.
5. Append to `state/<game>/docs-log.md`: the session, the pages written or updated, the gaps.

The last reply is one line: the game, the pages written and updated, the gaps.
