# Post-session review: what the session learned, and the next goals

Instructions for the reviewer (`sleepwalker-reviewer`). The orchestrator starts you right after a
player ends a session; you do not touch the phone, so the next session can already be running on it.
The brief gives the repository root, the game and the session id. Run every command from the root:
`cd <root> && python harness/sw.py … --game <game>` (`--game` records ops without a session).

Your job is the game's plan: after you, the next session must have concrete goals, and nobody plays
"the game" without one. You do not write the wiki and you do not change the process: that is the
documenter's and the dream's work.

## Read

- `raw/<game>/<session>/steps.jsonl`: actions with `why`, `mark` frames (open the marked shots in
  `raw/<game>/<session>/shots/`), notes, research ops (features, cases, goals, levels, progress);
- `state/<game>/progress.md` and the session's block in `state/<game>/inbox.md`;
- `python harness/sw.py research <game>`: the feature map, the goals, the progress, discovery;
- `python harness/sw.py audit <game>`: the feature model (JSON): untyped features, unknown triggers, open checklist
  items, locks without an unlock goal, the matrix of outcomes.

## Decide and record

1. **The session's goals.** For each goal it had: done, partly done, or not started. If the player did
   the work but did not close the goal, close it with the source (`task done <id> --game <game>
   --source <session>#<step> --note …`; experiments with `--result`). If a goal turned out to be wrong
   (the feature does not exist, a duplicate), cancel it with the reason.
2. **New goals** from what the session saw:
   - every locked entry point in the frames → its lock as data (step 3); read the lock icon, the tooltip, the
     "unlocks at" text. The planner makes its unlock goal;
   - every open feature without a study goal → a study goal;
   - every question the session raised that needs play to answer → an experiment with a `--plan`
     (what to do, what result confirms it);
   - a new area opened (a new map, a new mode) → a scout.
   Give each goal a clear title that says what is done when it is done.
3. **The feature model.** Every feature has a type, and the type's checklist is open cases `chk-<item>` so nothing
   is forgotten. The planner turns what you record into goals at once (the reply's `planned`); `audit` shows what
   is left:
   - **Types.** Type every untyped feature the session touched, and a few older ones each review (those with open
     goals first): `feature <id> --type <type> --game <game>`, a type from `sw.py types` (its description says
     what fits). When no type fits: `--type unknown`, and ask for the type designer: name the feature in your last
     reply (`typist: <id> <session>#<step of its best frame>`), and the orchestrator starts it (below).
   - **Why it appeared.** For a feature without `appeared`, read the frames before its first mark: what brought it
     up (the first launch, a level won, a threshold, a loss, a timer). Seen → `feature <id> --appeared "after
     winning level 20" --source <session>#<step> --game <game>`; not certain → `--appeared-guess "..."`. The
     planner makes the experiment "Find why <feature> appeared: <hypothesis>" for every typed feature without a
     fact, and closes it when the fact is recorded.
   - **Locks.** Each locked entry point is its own feature with its lock: `feature <id> "Name" --type <type>
     --locked "level 30" --locked-value 30 --game <game>` (a modes menu that lists five locked modes is five
     features, five locks). The planner makes the unlock goal; when the progress passes the value, a first look
     comes at once. `locks_without_unlock_goal` stays empty.
   - **Outcomes and the matrix.** The base level's feature is typed `core-level`: win, restart, quit and exit come
     from its checklist; every other way a level ended in the session is an outcome: `case <base> <kind> "Out of
     moves: ..." --outcome --source <session>#<step> --game <game>`. Every feature whose type affects the level
     flow (a level type, an event, a streak) then owes one run of each outcome under it (`under-<outcome>`), and
     the planner keeps one goal per such feature ("Run each outcome once under …"). Close the cells the session
     ran, with their source: `case <feature> under-<outcome> "<what differed, or: as the base>" --done --source …`.
   - **Checklists.** A feature is `documented` only when its `chk-*` items are closed (`checklist_open`); an item
     that does not apply is closed with a text that says so.
4. **The search for features (discovery).** Close it when all of this holds: the latest scout walked
   every reachable screen; every entry point maps to a feature; no locked entry point is left without
   an unlock goal, and the open unlock goals point at features already known; the genre checklist
   (`schema/WIKI-SCHEMA.md`, section 9) has no typical feature that the game might still have
   unseen — if it does, add an experiment "Look for <feature>" instead. Then
   `sw.py discovery closed --game <game> --why "…"`. Reopen it if a session found a new entry point.
   Do not wait for many levels: if nothing new appeared across the last levels and the map is
   complete, close it.
5. **Order.** If a goal blocks others (the core gameplay is too slow to reach any unlock), say so in the
   review note: the lab and the dream read it. You do not need to ask for the strong model while a
   mechanic is studying or broken: `claim` gives it every session whose goals play levels (follow-ups
   too), and a handoff names its mechanic for the next brief.

## Write

Append a block to `state/<game>/reviews.md`:

```
## <session-id> · <date>
- Goals of the session: <id> — done / partly (what is left) / not started
- New goals: <id> — why
- Closed or cancelled: <id> — evidence [<session>#<step>]
- Discovery: open | closed — why
- Feature model: typed <ids>; triggers recorded; locks; outcomes and matrix cells closed; typist: <feature → type>
- Blockers: what slowed the session down
```

Last, publish the game's live tables to the Wiki tab (the players plan from this live view; the
repository's copy comes with the nightly dream): `python harness/sw.py wiki-live <game>`.

The last reply is one line: the game, goals closed, goals added, features typed, discovery; and, when a feature
fits no type, `typist: <feature> <session>#<step>` for each.

## The type designer

A feature that fits no type gets `--type unknown`, and the reviewer names it in its last reply. The orchestrator
(`runbooks/play.md`, step 5) then starts a `sleepwalker-typist` subagent for each named feature (its model and
effort are in its definition, from `project.yaml` `models.typist`: pass no model), one at a time per game. Brief:

```
Repository root: <path>. Do not change the working directory: every command is cd <path> && python harness/sw.py ...
Instructions: <path>/runbooks/review.md, section "The type designer" — read it in full and follow it.
game: <game>  feature: <id> (<name>)  session: <session id>  best frame: step <step>
```

What the type designer does:

1. Read the catalog (`python harness/sw.py types`: every type with its description and checklist), the feature
   (`sw.py research <game>`: its cases and goals), its marked frames (the `mark` steps with `"feature": "<id>"` in
   `raw/<game>/<session>/steps.jsonl` and the shots they name) and the session's notes on it.
2. If a type fits after all, set it (`feature <id> --type <type> --game <game>`) and stop. A new type is for a kind
   of feature that other games will have too.
3. Define the new type in words that fit every game:
   - an id for the kind (`collection-event`, `merge-board`), never the game's own name for it;
   - `--description`: what makes a feature this type;
   - `--base`: the type it is a variant of, if any (a kind of level: `level-type`);
   - `--affects-level-flow` when a level is played, won or lost differently while the feature is on: every
     outcome of the base level is then run once under it;
   - 3 to 8 `--item ID:TEXT:KIND` beyond the universal three (appeared, entry, screen: they come by themselves),
     each a check a player can make with the phone: `look` (a screen to see and mark), `outcome` (an ending to
     reach), `experiment` (something to test by play). No item asks to pay or to spend premium currency.

   ```
   python harness/sw.py type-add <id> --name "..." --description "..." [--base T] [--affects-level-flow] --item "board:The board: ...:look" --item ...
   python harness/sw.py feature <feature> --type <id> --game <game>
   ```

   The type is used at once on this machine (`state/feature-types.local.yaml`); the dream's process improver moves
   it into `schema/feature-types.yaml`.
4. The last reply is one line: the feature, its type (new or existing) and why.
