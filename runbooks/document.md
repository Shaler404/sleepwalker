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
   Never tag a frame that shows personal data: the account's nickname or player ID (profile cards,
   name lists, privacy and account screens), a real player's handle or photo, an e-mail, the phone's
   status bar or notifications, or another app (a store, a browser, a system dialog; `mark-tag` refuses
   frames that were not the game's). Inside the game's own frames, black the spot out on the page's
   image: `python harness/sw.py redact-image state/<game>/pages/img/<name>.webp --box X1,Y1,X2,Y2` (pixels
   of that image, or fractions like `0,0,1,0.04` for the status bar); do the same for a banner ad in a
   local language (it tells the phone's country) and for a copyrighted quote, lyric or film line on a
   quote card. When the spot is the point of the frame, pick another frame of the same place, or write the
   place's note (`<!-- no-entry: personal data -->`, `no-screen:`, or `no-frame:` under a tab) and describe
   it in words.
3. Write the text: from the session's `why`, notes, cases and the frames themselves. Facts only, each
   with its footnote; what you infer is marked as such. The page is for a reader, not for an agent: no
   pixel coordinates, no instructions to agents (those go to the playbook), feature names in the table
   and the `###` headings as the game shows them ("Sound toggles", not `toggles`). Never write out a
   quote, lyric or book passage from the game in full (it is blocked as reproduced text): describe it
   ("a quote by Lincoln, 9 words").
4. `python harness/sw.py check-pages state/<game>/pages` until it reports no problems for your pages.
5. Append to `state/<game>/docs-log.md`: the session, the pages written or updated, the gaps.

## Rebuilding a page in the old layout

Pages written before the documenter existed (inline `[s:…]` sources, no "Where to find it") are rebuilt
one feature at a time; the brief names the game and the feature instead of a session.

1. Unless `state/<game>/pages/features/<id>.md` exists, copy the published page
   `wiki/<game>/features/<id>.md` there, and the images it uses from `wiki/<game>/img/` to
   `state/<game>/pages/img/`. Then `python harness/sw.py page-footnotes state/<game>/pages/features/<id>.md`:
   the inline sources become footnotes with the video links. A footnote without a link (the original was
   not on YouTube yet) gets it later from the same command or from `sw.py gc`; you do not add links by hand.
2. The sessions that touched the feature are the page's `sources` and footnotes. What the player did at
   each step is in `raw/<game>/<session>/steps.jsonl` (`why`, `note`, `shot`), the frames in
   `raw/<game>/<session>/shots/NNNNN_m.jpg`. Those sessions marked frames without `--feature`: tag the
   entry point (with `--at` on the button), the feature's screen, every tab and popup with `mark-tag`.
3. Follow "How" from step 1: the skeleton is merged into the page. Every true fact of the old page
   stays, with its footnote; the old layout's sections become the new ones (a tab's text goes under its
   `### <tab>`).

The last reply is one line: the game, the pages written and updated, the gaps.
