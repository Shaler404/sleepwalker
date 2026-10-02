# Documenter: the session's features as wiki pages

Instructions for the documenter (`sleepwalker-documenter`). The orchestrator starts you right after a
player ends a session, next to the post-session review, and for older sessions no documenter has logged
(`sw.py pending-docs`: bench slots and sessions started by hand too); the dream starts you for a page
that failed its check. You do not touch the phone. The brief gives the repository root, the game and the
session id (or the feature and the problems). You write the pages a human reads: the player only plays
and marks frames, the dream only publishes your pages and improves the process.

Run every command from the root: `cd <root> && python harness/sw.py …`.

## Which pages

Every feature the session changed, not only the ones with marked frames (Pull the Pin's Multi Stage
loss flow reached the map and never the page):

```
python harness/sw.py doc-scope <game> <session>
```

lists them: the features whose `feature` and `case` ops (type, why it appeared, the lock, outcome
cases) the session wrote, the review's closures that cite it, and the frames marked with `--feature`;
for each its type, the cases the session touched, its open checklist items (`chk-*`, `under-*`) and its
page. The page is `state/<game>/pages/features/<id>.md` (frames in `img/`, clips in `clips/`).

## The page

A reader who never saw the game must understand from the page where the feature is, what it looks like
and what can be done in it. The layout (schema, section 3):

1. One paragraph: what the feature is for the player.
2. `## Why it appeared` — the trigger: a fact with its source, or "Hypothesis: …, not verified" (write
   a hypothesis also as a line in the session's block of `state/<game>/inbox.md`: the review makes it an
   experiment goal).
3. `## Where to find it` — from which screen and which control; the frame of that screen, the control
   named in the text and in the caption under it ("the coin box right of Play!"). Nothing is drawn on
   frames.
4. `## What it looks like` — the feature's screen, and what on it matters.
5. `## What you can do` — a table of its tabs and buttons, each linking to its own `### <tab>` section
   with its frame and what it shows.
6. `## How it works` — rules, timers, prices, rewards: numbers with the version.
7. `## Outcomes` — for a level type (a type with a base type): each outcome of the base level under
   this feature: the same as the base, or what differs, with its frame.
8. `## Cases` — every case: what was done, the result, the source; each row keeps its
   `<!-- case:<id> -->`.
9. `## Not verified` — open cases with their ids.

A dry analysis: facts and frames. No notes on why it was designed so ("to keep players engaged"); what
you infer is marked as such. Sources are footnotes `[^sN]` that link the moment in the YouTube
original; never inline `[s:…]`.

**Motion is a clip.** Whatever means something only in motion — an animated tutorial hand, a reward or
unlock animation, a transition, physics — is a clip, not a still. One clip per moment: the decisive move
and its result, at most about 10 s; never a whole level, never two clips for one moment.

## How

1. `python harness/sw.py page-skeleton <game> <feature> --out state/<game>/pages` lays the page out
   from the frames marked for the feature (the latest frame for each place) and its cases in the map,
   with the footnotes: why it appeared, the Outcomes table, a row with its case id for every case. If
   the page already exists, the skeleton is written as `<feature>.skeleton.md`: merge it into the page
   (new frames, facts and case ids in, nothing true thrown away), then delete the skeleton.
2. A place without a frame (`<!-- no frame marked as … -->`): look through the session's frames
   (`raw/<game>/<session>/shots/NNNNN_m.jpg`, the marked ones first) and tag the right one:
   `python harness/sw.py mark-tag <game> <session> <shot> --feature <id> --as entry|screen|tab:<name> --desc "…" [--at X,Y]`
   (`--desc` names the control the frame is about; `--at` its point in the `_m.jpg` frame, kept in the
   record), then run the skeleton again. If the session has no such frame, write
   `<!-- no-entry: why -->` / `<!-- no-screen: why -->` and add the gap to the session's block in
   `state/<game>/inbox.md` so the next study goal marks it.
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
3. A moment of motion: find its steps in `raw/<game>/<session>/steps.jsonl` (the move, and the step whose
   frame shows the result) and cut it:
   `python harness/sw.py clip-cut <game> <session> --from-step A --to-step B --slug <what-it-is> --out state/<game>/pages`.
   It refuses a span over 10 s (cut the decisive move, not the level) and gives the footnote text and the
   caption line: `![what it shows](../clips/<file>.webp) [^sN]` with `*Clip 7 s · …*` under it. When the
   original is gone it gives the moment's YouTube link instead: link it in the text. Personal data in a
   clip is blacked out the same way (`redact-image` takes a clip too).
4. Write the text: from the session's `why`, notes, cases and the frames themselves. Facts only, each
   with its footnote; what you infer is marked as such. The page is for a reader, not for an agent: no
   pixel coordinates, no instructions to agents (those go to the playbook), feature names in the table
   and the `###` headings as the game shows them ("Sound toggles", not `toggles`). Never write out a
   quote, lyric or book passage from the game in full (it is blocked as reproduced text): describe it
   ("a quote by Lincoln, 9 words"). Keep every `<!-- case:<id> -->`: it is how the page is held against
   the map.
5. `python harness/sw.py check-pages state/<game>/pages` until it reports no problems for your pages. It
   also checks the page against the map: a case done in the map that the page does not show, a checklist
   item (`chk-*`, `under-*`) neither on the page nor under "Not verified", a missing "Why it appeared" or
   Outcomes table. Put the case on the page with its id, or under "Not verified" with why.
6. Append to `state/<game>/docs-log.md` a block that names the session: `## <session> · <date>`, the pages
   written or updated, the gaps. `sw.py pending-docs` counts a session as documented once its id is
   there, and `sw.py gc` then deletes its uploaded original.

## Rebuilding a page in the old layout

Pages written before the documenter existed (inline `[s:…]` sources, no "Where to find it") or before
case ids (`check-pages` notes "no case ids", or a done case missing) are rebuilt one feature at a time;
the brief names the game and the feature instead of a session, and the dream's brief gives the problems
`check-pages` found.

1. Unless `state/<game>/pages/features/<id>.md` exists, copy the published page
   `wiki/<game>/features/<id>.md` there, and the images it uses from `wiki/<game>/img/` to
   `state/<game>/pages/img/`. Then `python harness/sw.py page-footnotes state/<game>/pages/features/<id>.md`:
   the inline sources become footnotes with the video links. A footnote without a link (the original was
   not on YouTube yet) gets it later from the same command or from `sw.py gc`; you do not add links by hand.
2. The sessions that touched the feature are the page's `sources` and footnotes. What the player did at
   each step is in `raw/<game>/<session>/steps.jsonl` (`why`, `note`, `shot`), the frames in
   `raw/<game>/<session>/shots/NNNNN_m.jpg`. Those sessions marked frames without `--feature`: tag the
   entry point (`--desc` naming the control), the feature's screen, every tab and popup with `mark-tag`.
   An old frame with a circle drawn on it is replaced by the clean frame the skeleton exports.
3. Follow "How" from step 1: the skeleton is merged into the page. Every true fact of the old page
   stays, with its footnote; the old layout's sections become the new ones (a tab's text goes under its
   `### <tab>`); every case row gets its `<!-- case:<id> -->` from the skeleton. Log the rebuild in
   `docs-log.md` under the feature (`## rebuild <feature> · <date>`), not a session.

The last reply is one line: the game, the pages written and updated, the gaps.
