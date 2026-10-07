# Knowledge schema

The "constitution" of the global memory. The dream, the analysts and the critic read it; maintainers
change it through a pull request. The rule comes from Karpathy's LLM Wiki pattern: raw data is
immutable, the model writes the knowledge, humans read, ask and edit the rules.

## 1. Local and global

```
Global — the repository shared by all machines (changes only through a pull request)
├── games.yaml                  the games to analyze: the process works only from this list
├── project.yaml                rules: maintainers, budgets per task kind, version checks, when to recheck FTUE
├── runbooks/ schema/ harness/  the process: instructions, schema, code
├── wiki/<game>/                knowledge about a game (section 2)
├── wiki/_common/               shared by all games: agent lessons, patterns
├── skills/<game>/*.yaml        skill macros (section 6)
├── solvers/<game>/*.py         level solvers per mechanic (section 10)
└── dreams/<date>-<machine>.md  dream reports: what was processed and what changed

Local — on each machine, not in git
├── local.yaml                  the machine: phones, working hours, YouTube keys, its own games
├── state/<game>/
│   ├── research.jsonl          journal of tasks and the feature map from sessions and the planner (append-only)
│   ├── progress.md             the player's working notes: where it stopped, the plan
│   ├── inbox.md                candidates for the dream: routes, tactics, lessons, skills
│   ├── playbook.md             how to play: the player's working copy of agent/playbook.md (section 10)
│   ├── solvers/<mechanic>.py   solvers the player wrote, used at once, published by the dream
│   ├── sessions.jsonl          index of this machine's sessions
│   ├── pages/                  the documenter's pages: features/<id>.md, img/, clips/ (the dream publishes them)
│   ├── docs-log.md             the documenters' log: each session documented, its pages and gaps
│   └── skills.jsonl            skill runs: success or failure
├── state/sessions/<device>.json  which session is running on the device (one game — one device)
├── state/devices/<device>.json   the state of each game on the phone: fresh | progressed
├── state/holds/<device>.json     the owner has taken the phone (sw.py stop): it is not given to sessions
└── raw/<game>/<session>/       transcript steps.jsonl, frames, clips, screen recording, session.json
```

A machine writes to the global part in only one way: its dream opens a pull request and a maintainer
merges it. So many people can analyze games on their own machines and send results and process
improvements without getting in each other's way.

## 2. The wiki of one game

```
wiki/<game>/
├── index.md             overview: what the game is, coverage, links
├── research.yaml        tasks, feature map and versions — the plan and progress of the analysis (section 4)
├── tasks.md             tasks for humans: what is in progress, what is waiting, which phone is needed (sw.py render)
├── features.md          feature table (sw.py render)
├── features/<id>.md     feature page: how it works, all cases (section 3)
├── screens/             UI map: one page per screen, _map.md — which screen leads where
├── economy.md           currencies, sources and sinks, prices, timers
├── versions.md          versions and what changed
├── agent/
│   ├── routes.md        routes: how to reach each feature from the main screen (+ skill)
│   ├── playbook.md      how to play: rules, method and level times per mechanic (section 10)
│   ├── tactics.md       tactics: how to beat the game's mechanics
│   ├── lessons.md       lessons for the agent on this game
│   └── metrics.md       analysis speed per dream: is the process learning
├── img/                 frames: YYYYMMDD-<slug>-<hash8>.webp
└── clips/               clips: YYYYMMDD-<slug>.webp (animated WebP)
```

The player reads `agent/` before every session, so each next session goes faster. The overview of
all games is `wiki/tasks.md`: the status of each game and which phone a human needs to provide.

## 3. Pages

Front matter of every page:

```yaml
---
game: com.example.game
title: Daily reward
type: feature           # overview | feature | screen | economy | versions | agent
feature: daily-reward   # feature id from research.yaml (for type: feature)
version_seen: 241.3.1   # the version the page was last verified on
verified_at: 2026-10-01
sources: [20261001-091500-chrono-FYKPJ]
---
```

Feature page — written by the documenter after each session (`runbooks/document.md`) for every
feature the session changed (`sw.py doc-scope`), laid out by `sw.py page-skeleton` from the frames
marked for the feature and its cases in the map, checked by `sw.py check-pages` against the layout and
the map:

1. one paragraph: what the feature is for the player;
2. `## Why it appeared` — the trigger (the map's `appeared`): a fact with its source ("after winning
   level 20 [^s3]"), or "Hypothesis: …, not verified";
3. `## Where to find it` — from which screen and which control, with that screen's frame; the control
   is named in the text and in the caption under the frame (`mark --as entry --at X,Y` keeps the point
   in the record; nothing is drawn on frames);
4. `## What it looks like` — the feature's screen (`--as screen`);
5. `## What you can do` — a table of its tabs and buttons; every row has its own `### <name>` section
   with its frame (`--as tab:<name>`);
6. `## How it works` — rules, timers, prices, rewards, with the version;
7. `## Outcomes` — only for a feature whose type has a base type (a level type over `core-level`):
   one row per `under-<outcome>` case — outcome | as the base or what differs | frame;
8. `## Cases` — case, what was done, result, source; each row carries its case id
   `<!-- case:<id> -->`;
9. `## Not verified` — open cases, each with its id too.

A page without an entry or screen frame says why in `<!-- no-entry: … -->` / `<!-- no-screen: … -->`.

**Held against the map.** Every case done in the map is on the page (its `case:<id>`) or under
"Not verified", and so is every checklist item of the feature's type (`chk-<item>`, `under-<outcome>`):
a page that misses one fails `check-pages` and does not get published. A page written before case
ids is matched by its rows' text and gets the note "no case ids"; checklist items count only by their
ids.

**A dry analysis.** Facts and frames: what is there, what was done, what happened. No notes on why the
game was designed so ("designed to keep players…" fails the check); what is inferred is marked as such.

- Every non-trivial fact ends with a footnote `[^sN]`; the footnote names the session and step and
  links the moment in the YouTube original (`sw.py page-skeleton` writes them). No inline `[s:…]`.
- Frame: `![what the frame shows and what matters](../img/<file>.webp)`. The caption is not "shop
  screenshot" but "shop: 6 packs, prices 0.99–49.99 $, offer timer 23:59:12". Frames are clean: no
  circles or arrows drawn on them.
- Clip: anything whose meaning is motion — an animated tutorial hand, a reward or unlock animation, a
  transition, physics — is a clip, not a still. One clip per moment: the decisive move and its result,
  at most about 10 s (`sw.py clip-cut` cuts it from the session's recording), never a whole level and
  never two clips for one moment. `![what it shows](../clips/<file>.webp)` and the line
  `*Clip 7 s · [original on YouTube from 3:05](https://youtu.be/<id>?t=185)*` if the original is uploaded.
- A contradiction is not overwritten: the old statement moves into a block `> ⚠️ Previously (v1.41, 2026-09-20): …`.
- Links between pages are relative. External links go only to Google Play and YouTube.

## 4. Tasks and the feature map: `research.yaml`

```yaml
game: com.maroieqrwlk.unpin
play_version: 241.5.1     # the Google Play version at the last check
play_checked: '2026-10-01T10:00:00'
version: 241.5.1          # the version the analysis is running for or was finished for
discovery: closed         # open — not all sections found yet; closed — all are registered as features
discovery_note: map at level 40 complete, every locked entry point has an unlock goal, checklist covered   # set by the post-session review
progress: {text: level 95, value: 95, at: '2026-10-02T11:00:00'}   # progress reached
gate: null               # while advancing is blocked: {type: lives, until: ..., note: ...}
ftue_verified: '2026-10-01'   # when the game was last played from scratch
synced:                   # up to which moment each machine's journals are included
  chrono: '2026-10-01T04:31:00'
mechanics:                # kinds of levels and how the agent plays them (section 10)
- id: core-match
  name: Match free tile pairs
  status: mastered        # studying | mastered (2 levels in a row within the budget) | broken
  method: solver          # manual | heuristic | solver
  solver: solvers/com.vitastudio.mahjong/core-match.py
  levels: {won: 14, lost: 1, quit: 1}
  best_s: 71
  recent:                 # the last 10 levels (skipped: true / moves_before: N — not timed, section 10)
  - {level: level 14, result: won, seconds: 95, model: sonnet}
features:
- id: daily-reward
  name: Daily reward
  type: daily             # from the type catalog (schema/feature-types.yaml), or unknown
  appeared: {text: on the first launch after level 5, certainty: fact, source: 20261001-091500-chrono-FYKPJ#12}
  status: documented      # seen | in_progress | documented | recheck (new version)
  found_at: {text: level 5, value: 5}   # progress when the feature first showed up
  page: features/daily-reward.md
  version_seen: 241.5.1
  cases:
  - id: claim-day-1
    text: Claim the day 1 reward
    done: true
    source: 20261001-091500-chrono-FYKPJ#14
  - id: chk-calendar      # an item of the type's checklist
    text: "The calendar or the task list: every day or task and its reward"
    done: false
- id: leagues
  name: Leagues
  type: social
  appeared: {text: the league button shows from level 10, certainty: hypothesis, source: 20261001-091500-chrono-FYKPJ#30}
  locked: {text: level 20, value: 20}   # a lock seen on screen; once seen open: unlocked_at {text, value, source, lock}
  status: seen
tasks:
- id: analyze
  title: Analyze the game
  kind: analyze           # analyze (the container) | scout | study | unlock | experiment | update | ftue | replay | followup | daily
  requires: any           # any | fresh — needs a fresh install of the game
  source: external        # external (Google Play version) | game (timers, schedule) | session (knowledge gap)
  status: done            # open | done | cancelled
  closed: '2026-10-01T12:00:00'
  closed_by: planner
- id: scout-2
  title: "Map the game: ..."
  kind: scout
  status: done
  new_entries: 0          # entry points that did not map to known features
  at_progress: level 40
- id: unlock-leagues
  title: Reach level 20 to unlock Leagues
  kind: unlock
  feature: leagues
  target_text: level 20
  target_value: 20
  status: open
- id: race-win-flow
  title: Winning the race needs about 10 level wins
  kind: experiment
  feature: race
  plan: play levels while the race runs; the race score after each win; confirmed if a win flow shows by 10 wins
  status: done
  result: confirmed       # confirmed | refuted | inconclusive
  note: the race was won at 9 wins; win flow — podium, chest, league points [s:...]
- id: daily-reward-d2
  title: Claim the daily reward — day 2 of 7
  kind: daily
  feature: daily-reward
  not_before: '2026-10-02T09:15:00'
  source: game
  status: open
- id: unlock-shop
  title: How the shop unlocks
  kind: replay
  feature: shop
  requires: fresh
  source: session
  status: open
```

**The feature model.** Every feature has a type, so nothing about it is forgotten (`sw.py audit <game>` shows
what is left):
- **Types** — `schema/feature-types.yaml` (published) merged with `state/feature-types.local.yaml` (this machine's
  new types, from the type designer, used at once; the dream's process PR moves them into the schema). A type is
  `{id, name, description, base, affects_level_flow, checklist: [{id, text, kind: look|outcome|experiment}]}`;
  `sw.py types` lists them. The view gives every typed feature an open case `chk-<item>` per checklist item: the
  universal `chk-appeared` (why it appeared), `chk-entry` (where to find it), `chk-screen` (what it looks like),
  then the type's own. `unknown` has the universal items only; an untyped feature has none.
- **Why it appeared** — `appeared` is a fact (it closes `chk-appeared`) or a hypothesis; for every typed feature
  without a fact the planner keeps the experiment "Find why <feature> appeared: <hypothesis or unknown>".
- **Outcomes and the matrix** — on the base level's feature (type `core-level`) a case with `outcome: true` is one
  way a level ends: its checklist's `chk-win`, `chk-restart`, `chk-quit`, `chk-exit-app`, and each loss kind
  (`case … --outcome`). Every feature whose type has `affects_level_flow` (a level type, an event, a streak) gets
  `under-<outcome>` for every known outcome of the game ("<outcome> under <feature>: as the base, or what
  differs"), whichever side appeared first, and one goal "Run each outcome once under <feature>: …" that waits
  behind the unlock and study goals.
- **Locks** — a lock seen on screen is data (`locked`); the planner makes `unlock-<feature>`, and the moment the
  progress passes its value (or the feature is seen open, `unlocked_at`) a first look goes to the top of the
  game's goals: "First look at <feature>: open it once, record what it is and decide whether it needs a full study".

**Where tasks come from.**
- **External tasks — set by the planner** (`sw.py claim`):
  - for a new game — "Analyze the game" (the container; sessions never get it, they get its goals)
    and the first map ("scout");
  - a study goal for every open feature that has none; a new map when the analysis is open and no
    goal is left;
  - a newer version — "Recheck the features on version Y" (see section 7);
  - the analysis is finished but FTUE has never been played from a fresh install — "Play from
    scratch: FTUE and how features unlock";
  - a new version is out and the game was last played from scratch more than `ftue_refresh_days`
    ago — "Check whether FTUE changed in version Y". Without a new version FTUE is not rechecked: it
    does not change on its own.
- **Goals from the session — set by the player and the post-session review** (`sw.py task add`,
  `--game` outside a session): unlock goals with their target, study goals, experiments with their
  plan, a new map for a new area.
- **From the game and from knowledge gaps — set by the player** (`sw.py task add`):
  - a timer — `followup` with `not_before`;
  - a daily activity — `daily`, one task per day;
  - what can only be seen from a fresh install (FTUE, how a feature unlocks, a route that cannot be
    repeated from the current progress) — `ftue` or `replay` with `requires: fresh`.

**When a task gets done.** A session gets up to `session.max_goals` of the game's goals and tasks
that can be done on this device right now, in order: time-bound checks, rechecks, fresh-install work,
maps, studies, experiments, and unlock goals (nearest target first):
- `not_before` has passed;
- for `requires: fresh`, the game on the phone is fresh;
- for a recheck, the phone has the newer version installed;
- unlock goals wait while a gate (energy, lives, a timer — `sw.py gate`) blocks progress.

The analysis closes by itself when no goal is left, the search for features is closed and every
feature is documented. The player and the post-session review close the goals (`task done`, an
experiment with `--result`); a done unlock goal creates the feature's study goal.

**How a game is played — toward goals.** No level is played without a goal: levels are played only
for an unlock goal or an experiment. The post-session review (`runbooks/review.md`) closes the search
for features (`discovery`) as soon as the map is complete, every entry point maps to a feature, every
locked entry point has an unlock goal and the genre checklist has no unexplained gap.

**The game's state on the phone** — `state/devices/<device>.json`, local.
- The player records it at the start of a session (`sw.py device-state fresh|progressed`); a human
  records it with `sw.py -d <serial> device-state fresh --game <id>`.
- `sw.py` detects a reinstall by itself from the install time.
- After a session the game counts as `progressed`.

**Game status** in `tasks.md`:
- ▶️ active — there are tasks that can be done now;
- ⏳ waiting — the tasks wait for their time;
- 🙋 needs a human — the remaining tasks need a phone with a fresh install;
- 💤 sleeping until a new version — no open tasks.

During sessions only the journal `state/<game>/research.jsonl` changes. The dream moves it into the
global `research.yaml` (`sw.py snapshot`), and `sw.py render` rebuilds `tasks.md`, `features.md` and
`wiki/tasks.md`.

## 5. Images and clips

- No Git LFS and no MP4: GitHub does not play `<video>` from a repository (verified 2026-09-30).
  A clip is an animated WebP up to 20 s, 720 px, 12 fps, up to 8 MB; a page's clip is one moment of
  about 10 s (section 3). A frame is a WebP up to 1080 px.
- The original recording goes to YouTube and never enters the repository. It stays on the machine
  until the session is documented (the documenter cuts its clips from it), then `sw.py gc` deletes it;
  an original never uploaded goes after `raw.keep_originals_days`.
- Media are added, not rewritten: git keeps the history. No more than 5 new clips per game per
  dream. GitHub recommends keeping a repository under 1 GB.
- Personal data — nicknames, email, avatars, notifications, other apps, payment windows — never goes
  into the wiki. `sw.py mark` refuses to mark a frame that is not from the game. The account's
  auto-assigned player name or id is personal data too: a text names it as `[auto-assigned id]`
  (`local.yaml` `privacy.names` makes `sw.py case`, `mark` and `task add` refuse it and `snapshot`
  redact it).
- `sw.py check-zones` rejects MP4 and files over the limits.

## 6. Skills

`skills/<game>/<name>.yaml` is a macro for moving between screens. It is created from a transcript
with `sw.py skill new`: steps in screen fractions, pHash of the screen before and after. Each step's
`wait` is the time the transcript took before its next action (at most 60 s; the last step: its settle
+ 0.5 s); `--wait STEP:SECONDS` sets single steps.

```yaml
name: open-shop
description: Open the shop from the level map
status: candidate        # candidate → verified (3 successes in a row) → broken (2 failures or a version change)
version: 241.3.1
pre_hash: b699809d63993ecc
pre_region: [0.85, 0.03, 1.0, 0.12]   # optional: pre_hash is of this part of the frame (a control on a changing screen)
post_hash: 8f9df0487398269d
steps:
- tap: [0.934, 0.052]
  wait: 3.5
source: 20261001-091500-chrono-FYKPJ#12-15
```

`sw.py skill run` runs a skill only if the screen (or its `pre_region`) matches `pre_hash`, and counts
a success only if the screen matches `post_hash` at the end. Results accumulate in
`state/<game>/skills.jsonl` with `waited_s`, the sum of the waits; the dream promotes and demotes
skills based on them and shortens the waits of slow ones.

## 7. How knowledge stays current

- **Game version.** The analysis runs on the version installed on the phone; every feature keeps
  `version_seen` and every verified case its `version`. A newer version on Google Play adds a task
  "Recheck the features on version Y" that waits for the game to be updated on the phone (it shows under
  "Needs a human"); nothing else is blocked. When the phone has the newer version, documented features
  move to `recheck`; pages get the mark "recheck on vY".
- **FTUE.** It is rechecked only with a new version and only if the game was last played from
  scratch more than `ftue_refresh_days` ago.
- **Tasks.** The dream closes unneeded tasks as `cancelled` with a reason instead of deleting them.
- **Time.** Pages and features have `version_seen`. A lesson carries the line "confirmed: <session>,
  <version>"; a lesson not confirmed on two versions in a row is deleted.
- **Skills** drop to `broken` after failures and are no longer run.
- **Contradictions** go into a "⚠️ Previously" block, never a silent replacement.
- **Size.** `lessons.md` has at most 60 items; duplicates are merged.
- **Local data.** `sw.py gc` cleans raw records by the retention periods in `local.yaml`; journals
  already moved into the global `research.yaml` are ignored thanks to the `synced` mark.

## 8. Who writes and reads what

| Who | Reads | Writes | How it is enforced |
|---|---|---|---|
| Player (`sleepwalker-player`) | global knowledge, its own `state/<game>/` | `state/<game>/progress.md`, `inbox.md`, `playbook.md`, `solvers/`; the task and feature journal, the game's state on the phone and `raw/` — through `sw.py` | one game — one device (lock in `sw.py`); commits nothing |
| The "play" orchestrator | `sw.py claim` responses | nothing (`sw.py claim` writes the planner's tasks to the journal) | does not commit or push |
| Lab (`sleepwalker-lab`) | recorded level frames, the playbook | `state/<game>/solvers/`, `playbook.md`, `lab-log.md`; the mechanic's method | after a session whose mechanic is slow or unlearned, or whose solver the player works around; never touches the phone |
| Documenter (`sleepwalker-documenter`) | the finished session's `raw/`, `state/<game>/` | `state/<game>/pages/` (frames, clips), `docs-log.md` | runs right after each session, and for sessions `pending-docs` lists; `check-pages` against the map |
| Reviewer (`sleepwalker-reviewer`) | the finished session's `raw/`, `state/<game>/` | goals, discovery, types, triggers, locks and case closures through `sw.py … --game`; `state/<game>/reviews.md` | runs right after each session, never touches the phone |
| Type designer (`sleepwalker-typist`) | the type catalog, one feature's frames and notes | a new type through `sw.py type-add` (`state/feature-types.local.yaml`); the feature's type through `sw.py feature --type --game` | when a feature fits no type; never touches the phone |
| Analyst (`sleepwalker-analyst`) | its machine's `raw/` and `state/`, the worktree | nothing | tools: Read, Grep, Glob |
| The dream | everything on its machine | `wiki/`, `skills/`, `solvers/`, `dreams/` in the branch `dream/<machine>/<date>` | `sw.py check-zones` before committing |
| Critic (`sleepwalker-critic`) | the diff and the worktree | nothing | tools: Read, Grep, Glob |
| Maintainer | everything; what is needed from people — `wiki/tasks.md` | merges PRs; `games.yaml`, `project.yaml`, the process; feedback — `feedback` issues and PR comments; a fresh phone — `sw.py device-state` | branch protection on `main` on GitHub: changes only through a PR |
| Anyone | the public repository | pull requests, issues | only maintainers are taken into account |

## 9. Genre checklist

Typical features of free-to-play mobile games. The dream checks each game against this list: a
typical feature that is not found yet becomes a task "Look for <feature>", or the report explains why
the game does not have it.

- **Onboarding:** tutorial (FTUE), consent and permission prompts, account or login, language.
- **Core loop:** levels or stages and their types, win and lose flow, retry and continue, boosters,
  difficulty spikes.
- **Meta:** map or progression, chapters or worlds, stars, keys, chests, collections, customization and
  skins, story, decor or renovation, character upgrades.
- **Economy:** soft currency, hard currency, energy or lives, timers, sources and sinks.
- **Monetization:** shop and IAP packs, starter pack and first offer, limited-time offers and popups,
  no-ads purchase, subscription or VIP, battle or season pass, piggy bank, rewarded ads and their
  placements, interstitials, banners.
- **Retention:** daily rewards or login calendar, daily quests or missions, achievements, streaks,
  push-notification prompts, offline or idle rewards.
- **LiveOps:** timed events, tournaments, leagues and leaderboards, seasonal content, collection events.
- **Social:** friends, teams or clans, gifting, chat, PvP (record it; the agent does not play against
  people).
- **Settings and support:** settings, sound, language, privacy and legal, help and support, restore
  purchases, cloud save.

## 10. Mechanics, levels and solvers

How to play is learned in the session that meets the gameplay, not in the dream: the dream only
consolidates it.

- **Mechanic** — a kind of level with its own rules (`core-match`, `ice-tiles`, `boss-level`). The
  player registers it with the first `sw.py level start --mechanic <id>`; it lives in `research.yaml`
  → `mechanics`. Status: `studying` → `mastered` after two levels in a row within
  `play.level_budget_min` (5 minutes, the time a human needs) → `broken` after two levels in a row
  lost or over the budget. `sw.py` changes the status itself.
- **Level cycle** — `level start --plan` (plan from the playbook and one look at the board), safe
  moves in batches and a risky one (`!X,Y`) last (`taps`), `level plan` when the plan has not worked for `play.level_rethink_min` minutes,
  `level end --note` (what worked, what to change) and a playbook update right after.
- **Level records** — a level op (`research.jsonl`) is `{name, value, mechanic, result, seconds, solve_s,
  moves, decisions, replans, model, note, shot}`: `solve_s` from its first move to its end, `shot` the frame
  it was ended on. `level end won` needs a frame after the last move, of the game, and is refused for a
  win with no moves under 15 s unless `--skipped` (a skip for a video: `skipped: true`). A start after
  moves with no level open keeps `moves_before: N`; skipped and late-started levels are left out of
  `best_s`, the typical time and the mastered/broken rule. `--bonus` boards (`bonus: true`) move no
  progress and are filed under their name in the level catalog. `level end lost --retry` records the loss
  and opens the same level again. `session.json` and `sw.py stats` count `moves_outside_level` (moves of
  `taps` and `solve` with no level open in a game with mechanics) and `repeated_steps` (the same tap or
  solver plan again on a screen it did not change: warned, then held back unless `--force`).
- **Playbook** — `wiki/<game>/agent/playbook.md`, one section per mechanic: goal, controls, rules,
  method, level plan, pitfalls, level times. The player works in the local copy
  `state/<game>/playbook.md` (`sw.py playbook`); the dream merges it into the wiki. When a newer
  global playbook arrives (a merged dream), the local copy is replaced and the old one is kept as
  `playbook.prev.md`.
- **Solver** — `solvers/<game>/<mechanic>.py` (the local draft: `state/<game>/solvers/`). The contract:

  ```python
  def solve(image, board=None, frame_scale=1.0):
      # image: PIL.Image, the full-resolution screenshot; board: the JSON the model wrote (--board) or None;
      # frame_scale: full-resolution pixels per pixel of the frame the model sees
      return {"moves": [[x, y], [x1, y1, x2, y2]],  # only the moves whose outcome is known
              "note": "what the solver read and why it chose this line",
              "rescan": True,   # the next move depends on what these moves reveal: look again
              "done": False}    # these moves finish the level
  ```

  Moves are in pixels of the full-resolution image: `[x, y]` is a tap, `[x, y, 2]` a double tap,
  `[x1, y1, x2, y2]` a swipe.
  A solver that declares `state=None` in `solve(...)` gets a memory between the rounds of a level: what it
  returns as `"state"` (JSON, up to 200 KB) comes back in the next round of the same level and
  mechanic, and is `None` at a new level. It keeps what it has seen (face-down tiles turned over, the
  last board) so it recomputes only what changed and verifies that its last moves did what it expected
  (the right tiles gone) before the next ones. `--image FRAME --state FILE` chains recorded frames the same
  way without the phone.
  A solver models the rules exactly (including how a level is lost), searches ahead instead of taking
  the first legal move, prefers moves that keep options open, and stops at the first move that depends
  on something hidden. It checks that what it read is plausible (board size, number of regions or
  pieces) and returns no moves when it is not. Rounds also stop when the solver repeats the moves of
  the previous round. `sw.py solve <mechanic>` draws its moves on a fresh frame; `--image FRAME`
  does the same on a saved frame without the phone; `--run --rounds N` plays rounds of frame → solver
  → moves until the level is done, the solver has no moves, the moves change nothing or the level runs
  over its time. A solver only
  computes: it may import numpy, OpenCV, PIL and the standard library for math, but code that opens
  files, touches the network, starts processes or runs dynamic code is refused by `sw.py solve` and
  by `check-zones`, and the critic reads every solver. It runs on every machine that merges it.
- **Level catalog** — `wiki/<game>/levels.md` and `levels/<level>.webp`: for games whose design lives in
  the levels, the board of every level the agents met at its start, with the tries and the player's
  note (`sw.py level-catalog`, refreshed by the dream).
- **Models by role** (`models` in `project.yaml`, overridable in `local.yaml` and per game in
  `games.yaml`): `study` learns new or broken mechanics (the strong model), `play` plays mastered
  mechanics and verifies cases (the fast model), `consult` answers `sw.py ask`. `claim` picks the role
  per session: `study` while a mechanic is `studying` or `broken` and the session's tasks play levels
  (follow-ups, replays and FTUE checks too), `play` once every mechanic is mastered and for menu-only
  work (studies, surveys, dailies). A `play` session that meets gameplay to learn ends with
  `handoff --to <mechanic>`; the game goes back to the `study` model at once, and the brief's
  `model_why` names the mechanic.
  `sw.py stats --by-model` compares models: levels and features per hour, level times, the share of
  session time the model spends thinking, the share of actions after which nothing changed
  (`same_screen_rate`: the hash and the pixels agree) or only a small part of the frame did
  (`small_change_rate`: a board in play), restarts, refused commands per hour (`errors_per_hour`) and
  `wasted_handoffs` (handoffs that did nothing).

