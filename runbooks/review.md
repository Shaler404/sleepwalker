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
- `python harness/sw.py research <game>`: the feature map, the goals, the progress, discovery.

## Decide and record

1. **The session's goals.** For each goal it had: done, partly done, or not started. If the player did
   the work but did not close the goal, close it with the source (`task done <id> --game <game>
   --source <session>#<step> --note …`; experiments with `--result`). If a goal turned out to be wrong
   (the feature does not exist, a duplicate), cancel it with the reason.
2. **New goals** from what the session saw:
   - every locked entry point in the frames → an unlock goal with its target (`--target "level 20"
     --target-value 20`); read the lock icon, the tooltip, the "unlocks at" text;
   - every open feature without a study goal → a study goal;
   - every question the session raised that needs play to answer → an experiment with a `--plan`
     (what to do, what result confirms it);
   - a new area opened (a new map, a new mode) → a scout.
   Give each goal a clear title that says what is done when it is done.
3. **The search for features (discovery).** Close it when all of this holds: the latest scout walked
   every reachable screen; every entry point maps to a feature; no locked entry point is left without
   an unlock goal, and the open unlock goals point at features already known; the genre checklist
   (`schema/WIKI-SCHEMA.md`, section 9) has no typical feature that the game might still have
   unseen — if it does, add an experiment "Look for <feature>" instead. Then
   `sw.py discovery closed --game <game> --why "…"`. Reopen it if a session found a new entry point.
   Do not wait for many levels: if nothing new appeared across the last levels and the map is
   complete, close it.
4. **Order.** If a goal blocks others (the core gameplay is too slow to reach any unlock), say so in the
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
- Blockers: what slowed the session down
```

The last reply is one line: the game, goals closed, goals added, discovery.
