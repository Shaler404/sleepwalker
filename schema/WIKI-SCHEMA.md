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

Feature page: what it is and where to find it (with a link to the route) → how it works → **case
table** (case, what was done, result, source) → numbers in tables with the version → media →
`## Not verified`.

- Every non-trivial fact ends with a source `[s:<session>#<step>]`.
- Frame: `![what the frame shows and what matters](../img/<file>.webp)`. The caption is not "shop
  screenshot" but "shop: 6 packs, prices 0.99–49.99 $, offer timer 23:59:12".
- Clip: `![what it shows](../clips/<file>.webp)` and the line
  `*Clip 14 s · [original on YouTube from 3:05](https://youtu.be/<id>?t=185)*` if the original is uploaded.
- A contradiction is not overwritten: the old statement moves into a block `> ⚠️ Previously (v1.41, 2026-09-20): …`.
- Links between pages are relative. External links go only to Google Play and YouTube.

## 4. Tasks and the feature map: `research.yaml`

```yaml
game: com.maroieqrwlk.unpin
play_version: 241.5.1     # the Google Play version at the last check
play_checked: '2026-10-01T10:00:00'
version: 241.5.1          # the version the analysis is running for or was finished for
discovery: closed         # open — not all sections found yet; closed — all are registered as features
discovery_note: two clean surveys at level 60 and level 95, checklist covered   # set by the dream
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
  recent:                 # the last 10 levels
  - {level: level 14, result: won, seconds: 95, model: sonnet}
features:
- id: daily-reward
  name: Daily reward
  status: documented      # seen | in_progress | documented | recheck (new version)
  found_at: {text: level 5, value: 5}   # progress when the feature first showed up
  page: features/daily-reward.md
  version_seen: 241.5.1
  cases:
  - id: claim-day-1
    text: Claim the day 1 reward
    done: true
    source: 20261001-091500-chrono-FYKPJ#14
tasks:
- id: analyze
  title: Analyze the game, version 241.5.1
  kind: analyze           # analyze | update | survey | ftue | replay | followup | daily
  version: 241.5.1
  requires: any           # any | fresh — needs a fresh install of the game
  source: external        # external (Google Play version) | game (timers, schedule) | session (knowledge gap)
  status: done            # open | done | cancelled
  closed: '2026-10-01T12:00:00'
  closed_by: planner
- id: survey-3
  title: Survey every screen: capture all entry points and map them to features
  kind: survey
  status: done
  new_entries: 0          # entry points that did not map to known features
  at_progress: level 95
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

**Where tasks come from.**
- **External tasks — set by the planner** (`sw.py claim`):
  - for a new game — "Analyze the game, version X", where X is the Google Play version (checked every
    `version_check_hours`);
  - a new version is out while the analysis is still running — the analysis moves to the new version;
  - the analysis is already finished — "Update the docs for version Y", features go to `recheck`;
  - "Survey every screen…" after every `survey_every_sessions` analysis sessions, and when
    advancing is blocked by a gate and there is nothing else to verify;
  - the analysis is finished but FTUE has never been played from a fresh install — "Play from
    scratch: FTUE and how features unlock";
  - a new version is out and the game was last played from scratch more than `ftue_refresh_days`
    ago — "Check whether FTUE changed in version Y". Without a new version FTUE is not rechecked: it
    does not change on its own.
- **From the game and from knowledge gaps — set by the player** (`sw.py task add`):
  - a timer — `followup` with `not_before`;
  - a daily activity — `daily`, one task per day;
  - what can only be seen from a fresh install (FTUE, how a feature unlocks, a route that cannot be
    repeated from the current progress) — `ftue` or `replay` with `requires: fresh`.

**When a task gets done.** A session gets the game's tasks that can be done on this device right
now:
- `not_before` has passed;
- for `requires: fresh`, the game on the phone is fresh;
- for analysis and update, the phone has the required version installed.

Analysis and update close by themselves when all sections are found and all features are documented.
The player closes the other tasks (`task done`, `task cancel`).

**How a game is played — advance first.** While `discovery` is open the analysis runs in the
`advance` mode: move through the content as fast as possible, register features as they appear and
write every branch down as a case or a task for later. When a gate blocks advancing (energy, lives,
timer, content, paywall — `sw.py gate`), the mode becomes `cases`: verify what needs no progress; if
nothing, the game gives the phone up until the gate opens. Surveys and the genre checklist decide when
the search is over; after that the game is played in `cases` mode until every feature is documented.

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
  A clip is an animated WebP up to 20 s, 720 px, 12 fps, up to 8 MB; a long moment becomes several
  clips. A frame is a WebP up to 1080 px.
- The original recording goes to YouTube and never enters the repository.
- Media are added, not rewritten: git keeps the history. No more than 5 new clips per game per
  dream. GitHub recommends keeping a repository under 1 GB.
- Personal data — nicknames, email, avatars, notifications, other apps, payment windows — never goes
  into the wiki. `sw.py mark` refuses to mark a frame that is not from the game.
- `sw.py check-zones` rejects MP4 and files over the limits.

## 6. Skills

`skills/<game>/<name>.yaml` is a macro for moving between screens. It is created from a transcript
with `sw.py skill new`: steps in screen fractions, pHash of the screen before and after.

```yaml
name: open-shop
description: Open the shop from the level map
status: candidate        # candidate → verified (3 successes in a row) → broken (2 failures or a version change)
version: 241.3.1
pre_hash: b699809d63993ecc
post_hash: 8f9df0487398269d
steps:
- tap: [0.934, 0.052]
  wait: 1.5
source: 20261001-091500-chrono-FYKPJ#12-15
```

`sw.py skill run` runs a skill only if the screen matches `pre_hash`, and counts a success only if
the screen matches `post_hash` at the end. Results accumulate in `state/<game>/skills.jsonl`; the
dream promotes and demotes skills based on them.

## 7. How knowledge stays current

- **Game version.** The planner checks the Google Play version. A new version sets an update task
  and moves features to `recheck`; pages get the mark "recheck on vX".
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

  Moves are in pixels of the full-resolution image: `[x, y]` is a tap, `[x1, y1, x2, y2]` a swipe.
  A solver models the rules exactly (including how a level is lost), searches ahead instead of taking
  the first legal move, prefers moves that keep options open, and stops at the first move that depends
  on something hidden. `sw.py solve <mechanic>` draws its moves on a fresh frame; `--image FRAME`
  does the same on a saved frame without the phone; `--run --rounds N` plays rounds of frame → solver
  → moves until the level is done, the solver has no moves, the moves change nothing or the level runs
  over its time. A solver only
  computes: it may import numpy, OpenCV, PIL and the standard library for math, but code that opens
  files, touches the network, starts processes or runs dynamic code is refused by `sw.py solve` and
  by `check-zones`, and the critic reads every solver. It runs on every machine that merges it.
- **Models by role** (`models` in `project.yaml`, overridable in `local.yaml`): `study` learns new or
  broken mechanics (the strong model), `play` plays mastered mechanics and verifies cases (the fast
  model), `consult` answers `sw.py ask`. `claim` picks the role per session; a `play` session that
  meets gameplay to learn ends with `handoff` and the game goes back to the `study` model at once.
  `sw.py stats --by-model` compares models: levels and features per hour, level times, the share of
  session time the model spends thinking.

