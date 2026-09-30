# Sleepwalker

Agents play mobile games on phones and emulators while you sleep: they find every feature, work
through every user case, learn in the "dream" and keep a wiki for each game with screenshots and
clips.

**[Wiki →](wiki/index.md)** · [Games to analyze](games.yaml) · [Rules](project.yaml) ·
[Knowledge schema](schema/WIKI-SCHEMA.md) · [Guide](docs/guide.md)

## How it works

```
 every hour, on every machine                       once a day, on every machine
┌───────────────── play ─────────────────┐          ┌──────────────── dream ────────────────┐
│ sw.py claim: free phones ← games       │          │ feature journal → game feature map    │
│ with work (one game per device)        │          │ an analyst per session (read-only)    │
│ a player per phone, in parallel:       │ state/   │ feature pages, routes, tactics,       │
│  screenshot → decision → tap, screen   │ raw/ ──▶ │ lessons, skills, speed metrics        │
│  recording, features and cases,        │ local    │ critic (read-only) → pull request     │
│  marks, clips                          │          │                                       │
└────────────────────────────────────────┘          └──────────────────┬────────────────────┘
                 ▲                                                     │ maintainer merges
                 └────── routes, skills, lessons, plan ◀── main ◀──────┘
```

- **Local** (on the machine, not in git): phones, session recordings, journals, working notes, the
  YouTube key — `local.yaml`, `state/`, `raw/`.
- **Global** (the repository): the game list, rules, wiki, feature maps, skills. A machine gets
  anything in here only through the pull request of its "dream", so anyone can analyze games and
  improve the process on their own machine.

The routines are Claude Code scheduled tasks: [`runbooks/play.md`](runbooks/play.md) (orchestrator),
[`runbooks/session.md`](runbooks/session.md) (player), [`runbooks/dream.md`](runbooks/dream.md) ("dream").
The agent's hands and eyes are [`harness/sw.py`](harness/sw.py).

## The job for each game

Find every feature and describe how it works by working through every user case. The work is split
into **tasks**: each game has a `wiki/<game>/tasks.md` page, and the overview of all games is
[`wiki/tasks.md`](wiki/tasks.md). It shows what is in progress, what is waiting for its time, what
is done and **which phone is needed from a human**.

Where tasks come from:
- **External — the planner creates them itself:**
  - "Analyze the game, version X", where X is the version on Google Play;
  - a new version in the store: if the analysis is still in progress, it moves to the new version;
    if it is finished — "Update the docs for version Y";
  - a new version is out and the game was last played from scratch more than six months ago —
    "Check whether FTUE changed in version Y". Without a new version FTUE is not rechecked: it does
    not change on its own.
- **From the game and from knowledge gaps — the player creates them during a session:**
  - a feature behind a timer — "check no earlier than…";
  - a 7-day daily activity — one task per day;
  - what is only visible from a fresh install: FTUE, how a feature unlocks, a route that cannot be
    repeated from the current progress.

**The games on the phones are in different states.** At the start of a session the agent checks
whether the install is fresh:
- **fresh install** — plays the game from the start and records how each feature unlocks;
- **progressed** — harvests: describes everything already unlocked, keeps playing, and for what it
  cannot see (how the game got to this state) creates "needs a fresh install" tasks.

Only a phone with a fresh install of the game gets such tasks: `sw.py` notices a reinstall by
itself. Until there is such a phone, the task stays in the "Needs a human" section.

**How a game is played — advance first.** The goal is complete information as fast as possible:
- while not all features are found, the agent moves through the content as fast as it can and writes
  every branch down as a case or task for later instead of testing it on the spot;
- when advancing is blocked (energy, lives, a timer, a paywall), it slows down on purpose and verifies
  the cases that need no progress; if there are none, the phone goes to another game until the gate
  opens;
- whether new features can still appear is decided by looking, not by grinding levels: regular
  **screen surveys** map every entry point on every screen to a feature, and the dream compares
  surveys with each other and with a genre checklist. Two clean surveys at different progress points
  and a covered checklist close the search, so the agent does not play 700 levels when everything
  appears by level 100.

When there are no open tasks, the game **sleeps until a new version**.

## How memory works

**Who decides what to record.** The player does: it creates features and cases, marks screenshots
and clips, writes notes and lesson candidates. The "dream" selects and formats: it keeps what
repeats or is confirmed by a screenshot.

**Skills.** The "dream" turns a recurring transition (for example, "from the level map to the shop")
into a macro `skills/<game>/*.yaml` straight from the transcript. The player runs it with one
command. A skill fires only if the screen matches its start screen, and counts only if it got where
it should. After three successes it is `verified`, after failures — `broken`.

**How the process gets faster.** Before a session the player reads the routes to features
(`agent/routes.md`), mechanic tactics (`agent/tactics.md`), lessons and skills. Every day the
"dream" measures speed (`agent/metrics.md`: steps per closed case, share of steps without a screen
change, skills) and fixes routes and lessons if speed is not improving.

**Versions and overwrite protection.**
- The global part is git: every change records the author role, and the machine and sessions in
  trailers; roll back with `git revert`.
- `main` is protected: pull requests only.
- If two machines edit the same thing, GitHub catches the conflict at merge.
- Locally, a game runs in only one process at a time and phones are shared under a lock; the feature
  journal is append-only, and a copy of the notes is saved in every session.

**Permissions.** The table is in [`schema/WIKI-SCHEMA.md`](schema/WIKI-SCHEMA.md), section 8.
- The player commits nothing.
- The analyst and the critic can only read (their tools are restricted in the role definitions).
- The "dream" writes only `wiki/`, `skills/`, `dreams/`, and `sw.py check-zones` checks this.
- Maintainers from `project.yaml` merge; issues and comments from anyone else are just data.

**How stale knowledge is kept from piling up.**
- A new version on Google Play creates an update task and marks features "recheck".
- A new version when the from-scratch playthrough is older than six months creates a task to check
  FTUE.
- Lessons carry a "confirmed on version" mark; unconfirmed ones are deleted.
- Skills drop to `broken`.
- Contradictions go to a "⚠️ Previously" block.
- Raw recordings are cleaned up on schedule.

**The "dream".**
- Once a day on every machine, it moves the task and feature journal into the game's
  `research.yaml`.
- Analyzes sessions with analysts, edits the wiki in a separate branch, checks the result with the
  critic.
- Opens a pull request with a report: which sessions were analyzed, what changed, patterns with
  their frequency, speed.
- You merge or close it; the next "dream" takes your comments into account.

## Watch and suggest changes

- **The result** — the [wiki](wiki/index.md), right on GitHub.
- **What is needed from you** — the [task overview](wiki/tasks.md): the status of each game and
  which phone is needed.
  - If a fresh install is needed, uninstall the game and install it again (or clear its data), then
    connect the phone: `sw.py` notices the reinstall by itself.
  - If you only cleared the data, tell the system:
    `python harness/sw.py -d <serial> device-state fresh --game <id>`.
- **The process live**:
  - in the Claude app: "Scheduled" → the task → a run (you see the player's screenshots and
    decisions);
  - on the machine: `python harness/sw.py status` — what is running on each phone, the latest steps
    and screenshot.
- **Changes** — an issue labeled `feedback` (wiki format, storage, process — anything) or a comment
  on a "dream" pull request. The next "dream" makes the change and links to the issue. Process
  changes can also come as your own pull request.

## Taking a phone

Need a phone? It is free within a minute:

- double-click `harness/stop-phones.cmd` (you can put a shortcut on the desktop);
- or run `python harness/sw.py stop` (`-d <serial>` — only one phone);
- or tell any Claude Code chat opened in the repository folder (`E:\Sleepwalker` on the owner's
  machine) that you are taking the phone — [`CLAUDE.md`](CLAUDE.md) tells it to run the command.
  Do not write to the running "play" routine session.

`stop` restores the previous Do Not Disturb mode, finishes the screen recording, closes the game and
prints that the phone can be disconnected. The player gets a refusal on its next action and ends the
session. Cutting clips and uploading to YouTube continue without the phone.

The phone is back at work if:
- it was disconnected and connected again;
- `harness/resume-phones.cmd` or `python harness/sw.py resume` was run;
- the time set with `sw.py stop --hours N` has run out.

If you unplug the phone without the command, nothing breaks: the session ends at the next step, and
`sw.py` restores the previous Do Not Disturb mode the next time the phone is connected. Until then
the phone stays on "alarms only".

## Connecting a machine

1. You need: Windows, Linux or macOS with the Claude app, Android phones over USB in developer mode
   or emulators, `adb`, `ffmpeg`, Python 3.10+.
2. `git clone`, then `pip install -r harness/requirements.txt`.
3. Copy `local.example.yaml` to `local.yaml`: machine name, phones, your games (to split games with
   other machines), path to ffmpeg.
4. `python harness/sw.py install-agents` — roles with restricted tools.
5. Two scheduled tasks in Claude:
   - "play" every hour — "run runbooks/play.md in <path to the clone>". The task text must say:
     "do not call change_directory, run every command as cd <path> && …". Otherwise the background
     run hangs on the folder confirmation;
   - "dream" once a day — "run runbooks/dream.md".
6. Phones: unlocked, charging, screen up. On Samsung, a covered proximity sensor blocks touches. For
   the duration of a session `sw.py` turns on Do Not Disturb and then restores the previous mode.

If you have no write access to the repository, the "dream" opens a pull request from a fork.

Manual check:

```
python harness/sw.py claim
python harness/sw.py -d <serial> start <game> --budget 5
python harness/sw.py -d <serial> tap 540 1200 --why "the level opens"
python harness/sw.py -d <serial> end --status ok --summary "manual check"
```

## Images and clips

- No Git LFS and no MP4: GitHub does not play `<video>` from the repository, so a clip is an
  animated WebP up to 20 s and 8 MB that plays right in the article. Screenshots are WebP up to
  1080 px.
- The original recordings go to YouTube ([`harness/youtube.py`](harness/youtube.py)); until the
  Google project passes an audit, videos uploaded through the API are private.

## Sources

- Lamis Mukta (Anthropic), "Learning while you Sleep: Beyond Memory to Dreaming", AI DevCon, 2026 —
  memory in files, versions and permissions, a "dream" with subagents and human review.
- Khairallah AL-Awady, "How to Build Your First Team of AI Agents Using Claude Opus 5.5", 2026 —
  orchestrator, narrow roles, critic, full brief, limits, no early stops.
- Details and the other sources are in the [guide](docs/guide.md#0-sources).
