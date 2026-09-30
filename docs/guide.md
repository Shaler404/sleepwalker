# Guide: playing games 24/7 while building knowledge and a wiki

> **This is a research guide: rationale and reference on devices, perception, cost and risks.**
> For how the system works today, see the [README](../README.md), the [knowledge schema](../schema/WIKI-SCHEMA.md) and
> the [routine instructions](../runbooks/). The Anthropic API path code (`explorer.py`, `reflect.py`,
> `compile_wiki.py`, `scheduler.py`) and the role prompts were removed on 2026-09-30, replaced by Claude Code
> routines and `sw.py`. Sections 7, 9.2, 11 and 12 describe that path; the code is in commit `09d48d1`.

A guide to building a system that plays through a list of mobile games around the clock
(exploring new ones, rechecking known ones after updates and during limited-time events),
remembers lessons, accumulates knowledge and publishes an illustrated wiki for each game.

Companion files:

- [`schema/WIKI-SCHEMA.md`](../schema/WIKI-SCHEMA.md) — the wiki schema: data layers, catalog, page format, image rules, lint.
- [`runbooks/`](../runbooks/) — Claude Code routine instructions: "play" (hourly) and "dream" (nightly).
- [`harness/`](../harness/) — code: `sw.py` (the agent's hands and eyes on the phone), the phone driver, perception, the API path.

Contents: [0. Sources](#0-sources) · [1. Result](#1-expected-result) ·
[2. Idea](#2-main-idea-the-agent-plays-memory-learns) · [3. Architecture](#3-architecture) ·
[4. Hardware](#4-devices-and-environment) · [5. Devices](#5-device-layer) · [6. Perception](#6-perception) ·
[7. Explorer](#7-explorer-agent) · [8. Memory](#8-memory-and-learning) · [9. Wiki](#9-wiki) ·
[10. Updates and events](#10-updates-and-events) · [11. 24/7](#11-247-orchestration) · [12. Cost](#12-cost) ·
[13. Risks](#13-risks-rules-and-ethics) · [14. Metrics](#14-metrics-and-evaluation) · [15. Roadmap](#15-roadmap) ·
[Appendices](#appendix-a-phone-checklist-for-247-operation)

---

## 0. Sources

The guide draws on three sources and on hands-on practice with game-playing agents.

1. **Lamis Mukta's (Anthropic) talk "Learning while you Sleep: Beyond Memory to Dreaming"**,
   AI DevCon, 2026: the video from the post `x.com/HeyShobhan/status/2103472783598764525`, 31 minutes,
   watched in full. What matters for us:
   - memory is markdown files; the agent searches them with grep and loads them progressively (frontmatter,
     as with skills); the agent itself is better at deciding what to record;
   - production memory needs versioning (author, session, time, rollback), a hash check before writing,
     permissions (shared rules read-only, own memory writable) and portability ("it's just
     files"). These primitives are worth building into the harness rather than reinventing;
   - in-session memory hits three walls: the agent splits its attention between the task and memory, it
     cannot see patterns across sessions and agents, and notes go stale;
   - the way out is the dream: a separate batch process outside sessions. The memory store is cloned, a
     subagent runs on each session transcript, the orchestrator keeps the patterns that occur
     often enough and proposes edits with example transcripts and frequencies, and a human accepts
     or rejects them. Three actions: verify, organize, enrich;
   - the dream is given only transcripts with the same permission set as the store.
2. **Khairallah AL-Awady's article "How to Build Your First Team of AI Agents Using Claude Opus 5.5"**:
   a team is an orchestrator, narrow specialists and a read-only critic; a subagent needs a full
   brief because it does not see the conversation; each role gets minimal permissions; set limits on depth,
   parallelism, money and time; anything irreversible goes through a human; start with one agent and
   make every next one "earn" its place.
3. Research on memory patterns and game-playing agents — see the table below.

How this maps onto the system: the play routine writes a transcript and working memory, the dream routine
analyzes the transcripts with subagents once a day and opens a pull request, the critic checks it, the owner
merges (sections 8.4 and 11).

What comes from where (the full list of links is in [Appendix C](#appendix-c-sources)):

| Source | What we take |
|---|---|
| Karpathy, *LLM Wiki* (gist) | three layers (raw → wiki → schema), `index.md` + `log.md`, ingest/query/lint, "the model keeps the books, the human reads" |
| *LLM Wiki v2* (rohitg00) | confidence and supersession of facts, consolidation levels (working → episodic → semantic → procedural memory), "the schema is the main product" |
| Google Research + Virginia Tech, *WikiSkill* (arXiv 2608.27454, Aug 2026) | raw traces → a wiki of success/failure patterns → skill rebuild; a skill is accepted only if validation improved |
| *ACE: Agentic Context Engineering* (ICLR 2026) | Generator / Reflector / Curator roles; lessons are appended incrementally ("grow-and-refine") rather than rewritten wholesale |
| Reflexion, ExpeL, Agent Workflow Memory | verbal reflection after an episode; extracting insights from successful and failed traces; inducing workflows from repeated actions |
| Anthropic, *Claude Plays Pokémon* | a deliberately simple harness: screenshot → model → button; a knowledge base the model maintains itself; summarization every ~30 steps; "navigation guide" and "lessons from failures" files |
| Cradle (ICML 2025), Voyager | six agent modules (information gathering, self-reflection, task selection, skill curation, action planning, memory); skills as code with verification |
| Anthropic docs: memory tool, context editing, vision/coordinates, computer use, Dreams | the tools the scaffold in `harness/` is built on |
| Mobile agents 2026: MobileUse, Mobilerun (ex-DroidRun), Ghost in the Droid, Open-AutoGLM | hierarchical reflection, proactive exploration, ADB + screenshots, skills as YAML/Python |
| Game autotesting with LLM agents (TITAN, Lap, SMART, GBQA) | screen coverage metrics, bug detection, vision limits on Unity games |
| Google: Play Games on PC Developer Emulator / FAQ | `adb connect localhost:6520`, sideload only, one instance and one game, x86-64 or ARM via Intel Bridge |

---

## 1. Expected result

**Input.** A list of games (package ids from Google Play), a device pool (phones over USB, PCs with Google
Play Games), a daily model budget.

**Output.**

- For each game, a wiki in git (markdown + images): overview, tutorial, a screen map with
  screenshots, mechanics, economy, monetization, progression, event calendar, version history,
  open questions. The wiki is updated after every night and after every game update.
- For each session, a raw trace (screenshots, actions, notes) and a reflection (facts, lessons).
- For the agent, files of lessons and verified skills that make the next sessions
  faster and cheaper.
- For humans, a wiki site (MkDocs) and a chat over the wiki ("how does the battle pass work in game X?").

**v1 done criterion.** One device, three games, the system runs for a week without manual
intervention, each game has a wiki of ≥ 15 pages with ≥ 30 screenshots, an update to one of the games
is detected and documented automatically, cost stays within budget.

---

## 2. Main idea: the agent plays, memory "learns"

You say you are "building a neural network that will play games by itself". For the task "open any
game, figure it out and describe it", the practical 2026 answer is not to train a network's weights but
to take a ready-made multimodal model (VLM) as the agent's "brain" and make **learning happen in
memory**: in traces, lessons, skills and the wiki. Reasons:

- Reinforcement learning on a single game takes weeks and produces no wiki; a VLM agent plays an
  unfamiliar game from the first launch and explains what it sees.
- Lessons as text and skills carry over between games and versions; they can be read,
  checked and rolled back. Weights cannot.
- Once enough traces pile up, they can be used to fine-tune *small* models for narrow tasks
  (a button detector, a screen classifier) — a cheap "neural network" inside the pipeline, but it
  arrives at stage 5, not stage 1.

The loop that makes the system self-improving:

```
      ┌───────────── play (Explorer) ─────────────┐
      │  screenshot → decide → act → verify       │  writes raw/: screenshots, actions, notes
      └───────────────────┬───────────────────────┘
                          ▼
      ┌─────────── reflect (Reflector) ───────────┐
      │  facts + lessons + wiki requests + skills │  writes reflection.json, lesson candidates
      └───────────────────┬───────────────────────┘
                          ▼
      ┌───── consolidate ("dream", at night) ─────┐
      │  wiki is compiled, lessons merged,        │  edits wiki/, agent/lessons.md, skills/
      │  skills are tested on the device          │
      └───────────────────┬───────────────────────┘
                          ▼
      the next session gets: lessons in the prompt, skills as fast actions,
      open questions as goals  ────────────────────────────────────────────▶ play better
```

Three data layers (as in LLM Wiki and WikiSkill): **raw** is immutable, **wiki** is written only by the
compiler, **skills** are rebuilt from the wiki and accepted only after a check on the device.

---

## 3. Architecture

```
┌────────────────────────────────────── HOST ("brain", Linux or Windows) ──────────────────────────────────────┐
│                                                                                                              │
│  24/7 planner ──▶ task queue (SQLite): onboard / update_diff / event_scan / deep_revisit                     │
│        │                                                                                                     │
│        ▼  one worker per device                                                                              │
│  ┌──────────────┐   Device API    ┌────────────┐   frames   ┌──────────────┐  tool calls  ┌───────────────┐  │
│  │  Driver      │◀───────────────▶│ Perception │──────────▶ │   Explorer   │◀────────────▶│  Claude API   │  │
│  │ ADB / window │  tap/swipe/…    │ resize,    │            │ (tool runner │  memory tool │  Opus 5.5 /   │  │
│  │ GPG on PC    │                 │ pHash, OCR │            │  + memory)   │              │  Sonnet 5.5   │  │
│  └──────────────┘                 └────────────┘            └──────┬───────┘              └───────────────┘  │
│                                                                    │ raw/<game>/<session>/                   │
│                                                                    ▼                                         │
│                                         ┌──────────────┐  reflection.json  ┌──────────────────────────────┐  │
│                                         │  Reflector   │─────────────────▶ │ Nightly consolidation:       │  │
│                                         │ (structured  │                   │ wiki compiler, linter,       │  │
│                                         │  output)     │                   │ skill proposer + tests       │  │
│                                         └──────────────┘                   └──────────────┬───────────────┘  │
│                                                                                           ▼                  │
│                                              wiki/<game>/*.md + img/  ──▶  git  ──▶  MkDocs site / chat      │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
        ▲ USB / adb tcpip                     ▲ Windows window                     ▲ adb connect localhost:6520
   Android phones                      Google Play Games on PC                  GPG Developer Emulator
```

| Component | Role | Implementation in `harness/` |
|---|---|---|
| Device driver | a single interface: screenshot, tap, swipe, text, keys, launch, version, install from the store | `device.py` (ADB) |
| Perception | downscaling the screenshot for the model while keeping the scale, screen signature (pHash), OCR, annotations | `perception.py` |
| Explorer | the "observe → decide → act" loop, tools, memory across sessions, trace recording | `explorer.py` |
| Reflector | trace → facts, lessons, wiki requests, skill candidates (structured output) | `reflect.py` |
| Wiki compiler + linter | targeted page edits via the memory tool, image import, `index.md`/`log.md`, lint | `compile_wiki.py` |
| Planner, watchdog | queue, priorities, workers, recovery, store version checks, nightly jobs | `scheduler.py` |
| Publishing | a static wiki site | MkDocs Material (section 9) |

The main way to run it is Claude Code routines on a PC with a phone connected over USB: `runbooks/play.md`
plays one session every hour through `harness/sw.py`, and `runbooks/dream.md` analyzes the sessions at night
(section 11). `sw.py` has been tested on a real phone: game launch, screenshots, taps, screen recording, clip
cutting. The `explorer.py`, `reflect.py`, `compile_wiki.py` and `scheduler.py` modules are the Anthropic API
path for scale (an API key is required); they were checked for compilation and a run against a fake device.

---

## 4. Devices and environment

### 4.1 Where to play

| Option | ADB | Install from Play Store | Architecture | Emulator detection risk | Good for |
|---|---|---|---|---|---|
| **Phone over USB** (developer mode) | yes | yes, via the store UI | ARM, everything works | none | the main option: new games, events, updates |
| **Google Play Games on PC** (consumer client) | **no** | via the GPG client UI | x86-64 or ARM via Intel Bridge | it is an official platform, but the catalog only has games the developer enabled for PC | games that have a PC version; handy for large screens |
| **GPG Developer Emulator** | yes, `adb connect localhost:6520` | **no, APK sideload only** | as above | as above | your own builds, partner APKs |
| Android Emulator (AVD, Google Play image) | yes | yes | x86-64 + ARM translation | medium: Play Integrity and anti-cheats often block it | fast mass runs where the game does not check the device |
| Redroid / docker-android on a Linux server | yes | limited | x86-64 + translation | high | a headless farm for games without checks |

Facts about Google Play Games on PC that affect the design: only one emulator instance and one game
at a time; the consumer client does not expose ADB, so its driver is window capture and mouse events
(the client itself turns clicks into taps); the Developer Emulator installs games only via
`adb install`, and sideloaded games targeting API 30+ do not see Play Services unless the manifest
has `<queries><package android:name="com.android.vending"/></queries>`.

Recommendation: **a phone over USB** is the main and, so far, the only path in `sw.py`. Google Play Games
on PC was tested on 2026-09-30 and dropped: games launch via the `googleplaygames://launch/?id=<package>` link,
but the client window covers the game, Esc does not work as "back", and, most importantly, the agent has to
move the real mouse. On a phone, the game, the controls and screen recording are all in one place.

### 4.2 Host and peripherals

- The "brain" host: any Linux/Windows PC or mini PC; the load is Python plus network. A GPU is only needed
  for OCR/OmniParser, and even then it is optional (RapidOCR runs on the CPU).
- A USB hub with **power on every port** (industrial, 2–2.4 A per port); otherwise phones under
  load drain their batteries. Backup channel: `adb tcpip 5555` over Wi-Fi.
- Cooling: stands with fans; a phone running a game for days heats up and throttles.
- Battery: turn on the 80 % charge limit (Pixel "Adaptive/limit", Samsung "Protect battery"),
  otherwise the battery swells within a year or two.
- Screen: keep it on while charging, at minimum brightness (see Appendix A).
- Separate Google accounts for the lab, a separate network; no VPN needed.

---

## 5. Device layer

### 5.1 Interface

The agent does not know where it is playing. Everything it needs is described by the `Device` protocol in
`harness/device.py`: `screenshot`, `tap`, `long_press`, `swipe`, `type_text`, `key`, `launch`,
`stop`, `current_app`, `app_version`, `install_from_store`, `healthy`. Coordinates are physical
screen pixels; the Explorer converts them from model coordinates.

### 5.2 Android via ADB (`AndroidDevice`)

- `adbutils`: `screenshot()` (0.2–0.5 s), `click`, `swipe`, `keyevent`, `app_start/app_stop/app_current`,
  `list_packages`, `window_size`, `get_state`. With several devices, address them by serial number.
- Game version: `dumpsys package <pkg>` → `versionName`.
- **Installing and updating from the Play Store** goes through `uiautomator2`: the Play Store has a UI tree,
  and the "Install/Update/Open" buttons can be found by text. Unity games cannot be automated this way
  (the tree is empty); for them only vision works.
- Unicode input: `adb shell input text` cannot type Cyrillic; install ADBKeyboard and send the text
  as a broadcast (see `type_text`).
- Fast screenshots (shooters, rhythm games): `ScrcpyScreen` on top of `scrcpy-client` gives 15–60 fps; remember
  that the frame is downscaled to `max_width`, and scale the coordinates.

Tested on a Samsung SM-A276B (Android 16) on 2026-09-30:

- `pm list packages` fails without `--user 0`: Samsung has a second user (Secure Folder).
- `screenrecord` at the full 1080×2340 resolution does not start ("Encoder failed"); at 720×1560 it records.
  Frames are produced only when the screen changes, and the file may lack a duration, so
  `sw.py` tracks segment times by the clock.
- On first launch the game asks for notification permission: this is the
  `com.google.android.permissioncontroller` window, and the agent answers "Don't allow".
- Samsung's "Accidental touch protection" dims the screen and swallows touches when the proximity sensor
  is covered (the `IgniteTouchProtectionPresenter` window). `sw.py` detects this and does not start a session.

### 5.3 Google Play Games on PC (not used)

The window driver has been removed from `harness/`; this section is kept for reference.

The game is a Windows window titled with the game's name. Driver: `win32gui` (client area), `mss` (capture),
`pyautogui` (mouse; Unicode goes through the clipboard). Run it in the user's interactive session, and keep
the window in the foreground and unobstructed. Games are installed and launched in the client through its
own UI: either manually when a game is added to the list, or by the same agent equipped with
desktop tools (for the Windows desktop the official `computer_toolset_20260801` fits, but you have to
implement the actions for Windows yourself; it does not fit phones — it is desktop-only).

For your own builds, the alternative is the Developer Emulator: `adb connect localhost:6520`, after which it is
a regular `AndroidDevice("localhost:6520")`.

### 5.4 Device hygiene

The full checklist is in Appendix A. The minimum: the screen stays on while charging, auto-rotate is off,
notifications are on Do Not Disturb, app auto-update is **off** (the planner installs updates
once it has detected them itself and recorded the old version), screen lock is disabled,
Play Protect does not interfere.

---

## 6. Perception

### 6.1 Unity games can only be seen

`uiautomator dump` for Unity/Unreal games returns a single `SurfaceView` with no elements. So:
screenshot → model, and everything that can be computed locally (text, numbers, timers, "is this the same
screen") is computed locally and cheaply.

### 6.2 Screenshots for the model and coordinates

From the Claude docs (Vision / Coordinates):

- an image costs `ceil(w/28) × ceil(h/28)` visual tokens; a 1080×2400 phone screenshot is
  3354 tokens, 720×1600 is 1508, 540×1200 is 860;
- Opus/Sonnet 5.x do not downscale images up to 2576 px / 4784 tokens; Haiku 4.5, up to 1568 px / 1568;
- the model returns coordinates **in pixels of the image it sees**. So we downscale the screenshot
  ourselves (`prepare_for_model`), store the scale and multiply by it when tapping. Ask for
  "pixel coordinates `[x, y]`", not normalized ones;
- for small text, use `zoom_crop`: cut out a region at full resolution and show it separately
  (coordinates on the crop + offset).

Practical budget: 1500 tokens per screenshot for the Explorer, 700 for screenshots in reflection.

### 6.3 Screen signature and screen graph

A screenshot's pHash (64 bits) barely changes with timers and counters but does change when the screen changes.
It powers the "screen has not changed" detector (loop protection), screenshot deduplication for the wiki,
and the **screen graph** (a node is a cluster of hashes named via `mark_screen`, an edge is an action).
The graph yields a coverage metric ("how many nodes have unexplored edges"), a list of
goals for the next sessions, and the `screens/_map.png` picture for the wiki (Graphviz).

### 6.4 Local perception levels

| Level | What | Cost | When |
|---|---|---|---|
| 0 | pHash: "same screen / known screen / new" | ~0 | every screenshot |
| 1 | OCR (RapidOCR / PaddleOCR): prices, timers, names, buttons by text | CPU, ~0.1–0.3 s | every screenshot; needed for skills and wiki tables |
| 2 | Templates (OpenCV `matchTemplate`): "close X", currency icons | ~0 | inside skills |
| 3 | OmniParser v2: boxes of interactive elements + labels (Set-of-Mark) | GPU preferred, ~0.5–1 s | if the model misses small elements |
| 4 | VLM (Claude): understanding, decision, description | tokens | a new screen or a decision is needed |

The rule of a cheap system: levels 0–2 decide whether level 4 is needed. Known screen + an existing skill →
the model is not called at all.

---

## 7. Explorer agent

### 7.1 Anatomy of a session

1. The planner picks a game and a task type, launches the game and starts the watchdog.
2. The Explorer receives the system prompt (cached) and a first message with the goal, the budget,
   lessons from `agent/lessons.md` and open questions from the wiki.
3. The model reads `/memories` (memory tool; directory `memory/<game>`), takes a `screenshot`
   and runs the tool loop. Every action returns a fresh screenshot.
4. Stop conditions: `finish`, the minutes/steps budget is exhausted, 20 steps without a screen change, or a
   classifier refusal. Before ending, the model updates `/memories/progress.md`.
5. The trace lives in `raw/<game>/<session>/`: `steps.jsonl`, `shots/*.png`, `marked.json`.

### 7.2 Tools

| Tool | Purpose | Note |
|---|---|---|
| `screenshot` | a screenshot | always the first step |
| `tap`, `long_press`, `swipe` | actions with a `why` parameter (the expectation) | `why` goes into the trace — the Reflector compares expectation and result |
| `type_text`, `press` | text input and system keys | `back` is the most common way out of a loop |
| `wait` | animations, loading, timers | 30 s at most |
| `note` | a typed fact (economy, mechanic, ui, event, bug, question) | written right away, not "at the end" |
| `mark_screen` | mark a screenshot for the wiki | only marked screenshots end up in `img/` |
| `finish` | summary and goal status | mandatory |
| `memory` | `/memories` — notes across sessions | Anthropic itself adds "read memory first" to the prompt |
| (later) `run_skill` | run a verified skill from `skills/<game>/` | one call instead of 3–6 steps |

### 7.3 Prompt rules

See `PROMPTS.md`, section 1. The main ones: one action per step, then check the expectation; three steps without
change mean a change of strategy; popups and offers are content, so `mark_screen` them first; facts go in right
away via `note`; no purchases, no account setting changes, no talking to other players.

### 7.4 Context, cache, models

- **Context.** Screenshots are the heaviest part. `context_management` with `clear_tool_uses_20250919`
  clears old tool results and keeps the last 8 screenshots (in the example, with an 80 k token
  threshold). Notes and memory are excluded from clearing. On top of that there is a hard step limit per session
  (150): long tasks are split into sessions linked through `/memories/progress.md` — the same job that
  "summarization every ~30 steps" did in Claude Plays Pokémon.
- **Cache.** The system prompt uses `cache_control`, the conversation tail uses automatic caching
  (top-level `cache_control`). Check `usage.cache_read_input_tokens`: if it is zero,
  something is breaking the prefix (a date in the prompt, a changing tool list).
- **Models.** `claude-opus-5-5` for decisions and reflection (thinking is always on; depth is set
  via `output_config.effort`: `medium` in the loop, `high` in reflection and compilation).
  `claude-sonnet-5-5` for routine steps when the screen is known; `claude-haiku-4-5` for
  screen classification and OCR post-processing. The examples enable the server-side fallback
  (`fallbacks="default"`): if the classifier refuses, a fallback model finishes the request;
  if you don't need that, remove the parameter and the beta header.
- **Hierarchy.** Start with a single loop (Anthropic deliberately "under-engineered" the Pokémon
  harness). When sessions get long, add a Planner (once per session it sets 3–5 goals from
  open questions and the screen graph) and a Critic (it confirms goal completion from screenshots).

### 7.5 Loops and getting stuck

Three levels of protection: text in the tool result ("the screen has not changed for N steps"), stopping
the session after 20 steps without change, and the planner's watchdog (game not in the foreground → restart).
Typical traps: rewarded ads (wait up to 60 s, then look for the close X), Android permission
requests (their buttons are visible to uiautomator — handle them outside the model), a store update on launch.

---

## 8. Memory and learning

### 8.1 Four kinds of memory

| Memory | What it stores | Where | Who writes | Lifetime |
|---|---|---|---|---|
| Working | the current conversation, the latest screenshots | model context | Explorer | a session |
| Episodic | traces, screenshots, reflections | `raw/<game>/<session>/` | Explorer, Reflector | forever, immutable |
| Semantic | facts about the game, screen map, economy, events | `wiki/<game>/` | compiler | until contradicted (the old fact is marked, not deleted) |
| Procedural | lessons and skills | `wiki/<game>/agent/lessons.md`, `skills/<game>/` | Reflector → compiler; skill proposer | a skill lives as long as it passes its test |

Continuity between sessions comes from `/memories` (the model's own notes: where it stopped, what didn't work)
and `agent/lessons.md` (verified rules that go into the prompt).

### 8.2 Lessons

Format: "in situation X do Y because Z", with confidence, source and scope
(`game` / `general`). The Reflector **appends** candidates to the end of the file; at night the compiler
**merges** them: it combines duplicates, raises confidence for recurring ones, marks outdated ones
(`deprecated: v1.42`), keeps ≤ 60 items and sorts by (confidence, freshness). This is the ACE
principle: incremental deltas instead of rewrites, otherwise memory "collapses" into generic phrases.
General lessons (`general`) are promoted to `wiki/_common/agent-lessons.md` and go into the prompt for
all games.

### 8.3 Skills

A skill is a deterministic macro: a screen precondition (OCR text and/or a template), steps in
relative coordinates, a postcondition. The source is `skill_candidates` from reflections
(sequences repeated ≥ 2 times with the expected result); the format is the YAML from
`PROMPTS.md`, section 6. Acceptance works as in WikiSkill: **a skill is enabled only after a test on the
device** (postcondition met ≥ 3 times in a row) and **disabled** as soon as the test
fails after a game update. The index with the date of the last check is `agent/skills.md`.
Economics: a "close the daily offer" skill replaces 3–6 model calls every session.

### 8.4 Consolidation (the dream)

The dream is a separate process that runs once a day (`runbooks/dream.md`), built as in the Anthropic talk:

1. Memory clone: a `git worktree` on a `dream/<date>` branch. `main` is not touched.
2. A subagent per new session: it reads the `steps.jsonl` transcript, screenshots, clips, `progress.md` and
   `inbox.md`, and returns facts, lessons, agent mistakes, questions, media and outdated items.
3. The orchestrator counts frequency: a game lesson is kept if two sessions or an explicit screenshot confirm it,
   a general lesson if it appeared in two games. It edits the wiki according to the schema.
4. The critic (read-only) checks sources, media and personal data: PASS or FAIL, up to three rounds.
5. A pull request with example sessions and pattern frequencies. The owner merges or closes it; the next dream
   reads the owner's comments and takes them into account (`dreams/feedback.md`).

A merged dream is rolled back with `git revert`. If you later move to Claude Managed Agents with their memory
stores, dreams can be run by Anthropic, but the phone still lives with you, so the main
option is your own process.

### 8.5 What not to do

- Don't let the Explorer write to the wiki: it sees one session, while the compiler sees them all.
- Don't store every screenshot in the wiki: only marked ones, deduplicated by pHash.
- Don't trust a fact without a source screenshot/step: the linter flags such facts and the compiler doesn't insert them.
- Don't rewrite `lessons.md` wholesale and don't let the model "simplify" it.
- Don't update games automatically through the Play Store: an update is an event that is first
  recorded (old version, date), then installed, then described.

---

## 9. Wiki

The schema is in [`WIKI-SCHEMA.md`](WIKI-SCHEMA.md); it is fed in full to the compiler and the linter, and
it is the main document you will keep editing as the system grows.

### 9.1 Images and clips

The rules are in `schema/WIKI-SCHEMA.md`, section 4. In short:

1. While playing, the agent marks screenshots (`sw.py mark`) and segments for clips (`sw.py clip begin/end`).
   The screen is recorded for the whole session (`screenrecord` in 3-minute segments).
2. At the end of the session `sw.py` cuts the clips: animated WebP up to 20 s, 720 px, up to 8 MB. GitHub does not
   play `<video>` from the repository, but WebP plays right in the article.
3. The original recording goes to YouTube (`harness/youtube.py`) and is deleted from disk; clips link to
   it with a timestamp. Until the Google project passes an audit, videos uploaded through the API are private.
4. The dream moves media into the wiki (`sw.py wiki-img`, `sw.py wiki-clip`); screenshots are WebP up to 1080 px.
5. A screenshot that is not from the game (a notification, another app) cannot be marked; personal data never goes into the wiki.

### 9.2 Compilation

The compiler (API path) edits `wiki/<game>/` through the **memory tool** (the `/memories` directory is mapped to the
wiki folder): `view`, `create`, `str_replace`, `insert`, `delete`, `rename` — exactly what is
needed for targeted edits, and the SDK provides a ready-made file-based implementation. Input: the schema (cached),
the reflection JSON of new sessions, an image manifest. Output: changed pages, `index.md`,
`log.md`, merged lessons and a report of unresolved contradictions. Then `git commit`.

Mass rebuilds (for example, rewriting all screen pages for a new schema) are best run
through the Batches API (50 % of the price), one page per request.

### 9.3 Lint and queries

The linter runs once a week (and after a big compilation), fixes mechanical issues and writes `agent/lint.md`
with tasks for sessions: "recheck the price of bundle X on the shop screen". These tasks go into
`open-questions.md`, and from there into `deep_revisit` goals. Human queries ("how does monetization
in game A differ from B?") are a separate mode of the same compiler: an answer that cites pages;
valuable answers are saved as `analysis/` pages.

### 9.4 Publishing

The repository is public: the wiki is read directly on GitHub, and images and clips show up in the articles. MkDocs
Material or Obsidian are optional; the frontmatter is compatible with both.

---

## 10. Updates and events

### 10.1 Detecting updates

- Hourly: `google_play_scraper.app(pkg, lang, country)` → `version`, `updated`,
  `lastUpdatedOn`. The current library version (1.2.7) does not extract the `recentChanges` field, so
  the agent reads "what's new" in the game itself.
- Installed version: `dumpsys package` → `versionName`. A mismatch → an `update_diff` task.
- Order: record the old version and the date → install the update (the "Update" button in the store)
  → an `update_diff` session over all known screens from the graph → "before/after" screenshot pairs through
  the change detector prompt (`PROMPTS.md`, section 7) → an entry in `versions.md` with screenshots →
  recheck the skills.

### 10.2 Events (LiveOps)

A short daily `event_scan` session (≤ 10 minutes): login popups, the
news/events/promotions section, the shop. For each event: name, conditions, rewards, timer
(OCR gives an exact "2d 13:05:12 left", from which the end date is computed). Everything goes into
`events.md` as a calendar; before an event ends, the planner schedules a revisit
(did the rewards change, did a "last chance" offer appear). Past events stay in the history —
that is exactly what makes the wiki valuable six months later.

### 10.3 Default schedule

| Session type | When | Budget | Goal |
|---|---|---|---|
| `onboard` | the game is new | 40 min (in batches of 15) | FTUE, menus, shop, 3–5 rounds |
| `update_diff` | store version ≠ installed version | 25 min | diff over the known screens |
| `event_scan` | every 24 h | 10 min | popups, events, shop |
| `deep_revisit` | every 7 days or on linter tasks | 30 min | open questions, progression |
| compilation | nightly, if there are new reflections | — | wiki, lessons |
| lint + skill tests | once a week | — | wiki health, skills |

---

## 11. 24/7 orchestration

The main path is two scheduled Claude Code tasks in the app on the PC that the phone is
connected to:

- **"play"** — every hour: `runbooks/play.md`. `sw.py next` picks a game and a session kind based on
  `games.yaml` and the state in `memory/<game>/state.json`; if the phone is busy, locked or hot, or there is
  nothing to play, the run ends within seconds;
- **"dream"** — once a day: `runbooks/dream.md`; the result is a pull request.

The tasks run while the Claude app is open; a missed run executes the next time it is
opened. The API path (`harness/scheduler.py`) remains for scale, once there are several
phones. How that planner works is described below.

- **Queue** in SQLite (`scheduler.py`): tables `games` and `sessions`; tasks are picked by
  priority (new > update > event > scheduled deep dive). One worker per device;
  devices are independent.
- **Watchdog**: game not in the foreground → restart; ADB dropped → `recover` (reconnect,
  wait); screen not changing → the session ends by itself and the next one starts from memory.
- **Every session ends with reflection** right away (while the screenshots are still on disk); compilation happens at night.
- **Fault tolerance**: a session error does not crash the worker but is written to `games.last_error`;
  the same package is not picked again for at least a minute; after three errors in a row the game
  should be moved to the `paused` state and a notification sent (add a counter).
- **Deployment**: a host service (`systemd` on Linux, NSSM/Task Scheduler on Windows), logs to a file,
  Telegram notifications about crashes and finished compilations, a simple status page
  (the latest screenshot from each device, the queue, the daily cost). Back up `raw/` and `wiki/`.
- **Scheduling for GPG on PC**: one game at a time, so before a session the `gpg-pc` worker
  closes the previous game and launches the needed one through the client UI.

Typical failures and responses:

| Failure | Sign | Response |
|---|---|---|
| The game crashed | `current_app` ≠ package | restart, a note in the trace (it is a bug for the wiki) |
| An ad/external browser | package `com.android.chrome` etc. | `back`, then restart the game |
| A Play Store update over a session | an "Update" popup | auto-update is off; queue an `update_diff` |
| The phone overheated | `dumpsys battery` temperature > 45 °C | pause the worker for 15 min |
| USB dropped | `get_state` ≠ `device` | `recover`, then Wi-Fi ADB |
| Model refusal (`refusal`) | `stop_reason` | the session ends, the task is flagged, a human takes a look |
| API limits (429) | an SDK exception | the SDK retries; if it repeats, pause the worker |

---

## 12. Cost

Tokens per screenshot: `ceil(w/28)×ceil(h/28)`. Prices (first party, September 2026): Opus 5.5
$4/$20 per million (cache read $0.20), Sonnet 5.5 $2/$10 (cache $0.20), Haiku 4.5 $1/$5.

An estimate of one Explorer step on Opus 5.5 (a 720×1600 screenshot ≈ 1.5 k tokens + ~1 k tokens of new
text, ~30 k of history from the cache, ~300 response tokens): ≈ $0.006 + $0.004 + $0.006 + $0.006 ≈
**$0.02**. This is a rough estimate; take the real numbers from each session's `usage` (they are written
to the trace).

| Configuration | Steps/hour per device | $/hour | $/day per device |
|---|---|---|---|
| Naive: every step on Opus 5.5, full history | ~400 | ~9 | ~210 |
| Sonnet 5.5 in the loop, Opus for reflection/compilation | ~400 | ~5 | ~120 |
| + clearing old screenshots (last 8 kept), 720 px screenshots | ~400 | ~3.5 | ~85 |
| + local levels 0–2 and skills handle ~60 % of steps | ~400 (160 go to the model) | ~1.5 | ~35 |

Add reflections (≈ 80 sessions/day × ~$0.2 ≈ $15 on Opus) and the nightly compilation (≈ $1–2 per game).
Levers in order of decreasing effect: don't call the model on known screens; clear screenshots from the context;
downscale screenshots; cache the system prompt and the tail; use Batches for mass rebuilds; effort
`low/medium` in the loop; Sonnet/Haiku where the decision is simple. Judge by the cost
**per new fact in the wiki**, not per step.

---

## 13. Risks, rules and ethics

- **Game terms of service.** Almost all online games ban bots and third-party software,
  and many ban emulators; Play Integrity and anti-cheats can detect automation and abnormal
  activity. The consequence is an account or device ban. To lower the risk: separate accounts and
  devices, a human-like pace (1–3 s pauses, not 24 hours straight in one game),
  no impact on other players (no PvP, no chat, no guilds); your own games have no
  restrictions. For competitive analysis, consult a lawyer: where you are, which games,
  what you publish.
- **Money.** A purchase ban in the prompt plus an account with no payment method. If you want to
  document purchases, use gift cards with a limit and an explicit list of allowed actions.
- **Data and publicity.** The repository is public. Screenshots can contain nicknames, email addresses, avatars,
  notifications: such screenshots do not go into the wiki, and the dream's critic checks this. Screenshots and clips
  of other people's games in a public wiki are review use, but this is a copyright question; if a publisher asks,
  remove the game. The originals on YouTube may trigger Content ID.
- **Personal phone.** If the phone is your personal one, the agent plays on your accounts and spends soft
  currency and lives. For the duration of a session `sw.py` turns on "Do Not Disturb: alarms only" and afterwards
  restores the previous mode; a session will not start while you are using the phone.
- **Model safety.** A game may show text that looks like an instruction ("send the code
  here"); the agent's tools are limited to the device and the wiki files, and it has no network access and no
  payment methods — keep it that way.
- **Emergency stop.** A single flag file or a Telegram command that stops all workers.

---

## 14. Metrics and evaluation

| Metric | How to compute | Why |
|---|---|---|
| New screens/hour | screen graph nodes seen for the first time | exploration efficiency |
| Share of steps without a screen change | from the trace | looping, coordinate quality |
| Share of steps handled by skills/locally | from the trace | cost |
| Wiki accuracy | a human checks 20 random claims every week | trust in the wiki |
| Update/event detection latency | time from `updated` in the store to the entry in `versions.md` | freshness |
| Lint issues | from `agent/lint.md` | wiki health |
| $ per new fact | session cost / accepted facts | economics |

**Reference test.** Take a game you know inside out and compare the agent's wiki with your own
knowledge: which mechanics, screens and rules it found, which it missed, where it got things wrong. Use it as a
regression test for every change to the instructions and the schema.

---

## 15. Roadmap

| Stage | What we do | Done when |
|---|---|---|
| 0. Manual loop (2–3 days) | a phone over USB, the play routine on one game, reviewing traces | the agent gets through the tutorial and menus on its own, the trace is readable |
| 1. Memory and reflection (a week) | `/memories`, `reflect.py`, lessons in the prompt, `mark_screen` | the second session picks up where the first left off; lessons are visible and useful |
| 2. Wiki (a week) | `compile_wiki.py`, schema, image import, MkDocs, lint | the first game has ≥ 10 pages with screenshots, checked by a human |
| 3. 24/7 (1–2 weeks) | `scheduler.py`, watchdog, store versions, `event_scan`, three games | a week without manual intervention, one update documented |
| 4. Skills and savings | OCR, pHash graph, skill proposer + tests, Sonnet/Haiku in the loop | cost per step down ≥ 3×, share of steps without the model ≥ 50 % |
| 5. Scale | several phones, a dashboard, cross-game patterns, fine-tuning an element detector on our own traces | 10+ games, cost within budget, wiki accuracy ≥ 90 % |

---

## Appendix A. Phone checklist for 24/7 operation

- Developer mode, USB debugging, "Stay awake while charging" (`settings put global stay_on_while_plugged_in 7`).
- Screen lock: none; minimum brightness; auto-rotate off; Do Not Disturb always on.
- Play Store: app auto-update **off**; Play Protect stays on but does not interfere.
- 80 % charge limit; a cooling fan; temperature via `dumpsys battery`.
- A separate Google account; device language and region matching the game's target audience.
- For Cyrillic input, ADBKeyboard set as the current keyboard.
- Samsung: "Accidental touch protection" blocks touches when the proximity sensor is covered. Keep the phone face up with the top edge uncovered, or turn the feature off.
- Wi-Fi ADB as a backup: `adb tcpip 5555`, then `adb connect <ip>:5555`.
- Notifications from other apps are off, so the only popups come from the game.

## Appendix B. Useful commands

```bash
adb devices -l                                   # serials and models
adb -s SERIAL exec-out screencap -p > shot.png    # screenshot without adbutils
adb -s SERIAL shell dumpsys package PKG | grep versionName
adb -s SERIAL shell dumpsys window | grep mCurrentFocus   # what is in the foreground
adb -s SERIAL shell am start -a android.intent.action.VIEW -d market://details?id=PKG
adb -s SERIAL shell monkey -p PKG 1              # launch the game
adb -s SERIAL shell am force-stop PKG
adb -s SERIAL logcat -d | grep -i "FATAL\|ANR"   # crashes during the session
adb -s SERIAL shell dumpsys battery | grep temperature
adb connect localhost:6520                       # GPG Developer Emulator
```

## Appendix C. Sources

Memory and self-improvement patterns

- Karpathy, *LLM Wiki* — https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- *LLM Wiki v2* (rohitg00) — https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2
- *WikiSkill: Compiling Agent Experience into Persistent Knowledge* (Google Research, Virginia Tech, 2026) — https://arxiv.org/abs/2608.27454; reference implementation — https://github.com/kenhuangus/wikiskill
- *Agentic Context Engineering* (ICLR 2026) — https://arxiv.org/abs/2510.04618
- *Hindsight* (agent memory that learns from experience) — https://github.com/vectorize-io/hindsight
- Anthropic, Dreams for Managed Agents — https://platform.claude.com/docs/en/managed-agents/dreams
- Anthropic, memory tool — https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
- Anthropic, context editing — https://platform.claude.com/docs/en/build-with-claude/context-editing
- Anthropic, vision and coordinates — https://platform.claude.com/docs/en/build-with-claude/vision, https://platform.claude.com/docs/en/build-with-claude/vision-coordinates
- Anthropic, computer use tool — https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool

Game agents

- Claude Plays Pokémon: a breakdown of the harness — https://michaelyliu6.github.io/posts/claude-plays-pokemon/; an interview with the author — https://www.latent.space/p/how-claude-plays-pokemon-was-made
- Cradle: General Computer Control — https://arxiv.org/abs/2403.03186, https://github.com/cuddIle/Cradle
- Voyager, JARVIS-1, Reflexion and others — survey at https://github.com/git-disl/awesome-LLM-game-agent-papers
- DeepMind SIMA 2 — https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/
- LLM agents as game testers (TITAN, Lap, SMART, GBQA) — https://arxiv.org/abs/2512.12706, https://arxiv.org/abs/2604.02648

Mobile automation

- MobileUse — https://github.com/MadeAgents/mobile-use
- Mobilerun (ex-DroidRun) — https://github.com/droidrun/droidrun
- Ghost in the Droid — https://github.com/ghost-in-the-droid/android-agent
- Open-AutoGLM — https://sourceforge.net/projects/open-autoglm.mirror/
- uiautomator2 — https://github.com/openatx/uiautomator2
- scrcpy — https://github.com/Genymobile/scrcpy; py-scrcpy-client — https://github.com/leng-yue/py-scrcpy-client
- OmniParser v2 — https://github.com/microsoft/OmniParser
- google-play-scraper — https://github.com/JoMingyu/google-play-scraper
- Redroid — https://hub.docker.com/r/redroid/redroid

Google Play Games on PC

- Developer Emulator — https://developer.android.com/games/playgames/pg-emulator
- FAQ (one instance, one game, sideload and Play Services) — https://developer.android.com/games/playgames/faq
- Start (ABI, Intel Bridge) — https://developer.android.com/games/playgames/start
- PlayBridge (ADB emulation for the consumer client) — https://github.com/ACK72/PlayBridge
- Integrity protection for Google Play Games on PC — https://developer.android.com/games/playgames/integrity

Risks

- Play Integrity API — https://developer.android.com/google/play/integrity/overview
- Emulators in games: threats and detection — https://docs.talsec.app/appsec-articles/articles/emulators-in-gaming-threats-and-detections
