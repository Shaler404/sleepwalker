# Onboarding a game: first study and choosing its models

A local procedure, run by hand (by the owner, or by a Claude Code session the owner asks), never on a
schedule. A game enters `games.yaml` — and the hourly routine — only once it has been studied and its
models are chosen; existing games without `models` in `games.yaml` go through steps 4–6.

Models are chosen per role, each with its effort level (low, medium, high, xhigh, max; haiku takes
none):
- `study` — learns gameplay: the first sessions, new or broken mechanics;
- `play` — plays mastered gameplay toward the goals.
The wiki writer and the process improver (the dream) are chosen once for the whole repository with
their own benchmark (section "Writers").

## 1. Stop the routines

Pause "Sleepwalker: play" and "Sleepwalker: dream" in the app (Routines). The phone is the test bench:
nothing else may use it until the benchmark is done.

## 2. Add the game locally

Install the game on the phone. Add it to `local.yaml`:

```yaml
onboarding:
  - id: com.example.game
    title: Example Game
```

`claim` never hands an onboarding game out; `start`, `plan` and `bench` work with it.
`python harness/sw.py plan com.example.game` sets its first goals (the map).

## 3. First study, with the strongest configuration

Play the first sessions with the strongest model and effort (`fable`, `xhigh` or `max`), so that what
is learned is learned well: the map, the core mechanic's rules in the playbook, a solver if every piece
is visible, until the mechanic is `mastered` (two levels in a row within the level budget). Start each
session like the routine does, with the model and effort named: a `sleepwalker-player-fable-xhigh`
subagent, or
`claude -p "<the brief from play.md>" --model fable --effort xhigh --permission-mode bypassPermissions`.
Run the post-session review after each session (`runbooks/review.md`).

## 4. Benchmark the play role

```
python harness/sw.py bench new <game> --variants "opus:low,sonnet:low,sonnet:medium,haiku" --rounds 2 --levels 4 --mechanic <id>
python harness/sw.py bench run <bench id>          (long: start it in the background; --max N to run a few slots)
python harness/sw.py bench report <bench id>
```

Slots are interleaved and rotated, so no variant always plays first or last. Every slot is a session
played through `claude -p --model … --effort …` with the same brief: play N levels of the mechanic
with the level cycle, nothing else. The report gives per variant: levels won and lost, levels won per
hour, the median level time, the median decision time, moves per won level and the cost (from the
CLI's result), and `model_ids`: the models the CLI really ran. `claude` on PATH resolves `opus`, `sonnet`
and `fable` by its own version, and an old one runs older models without an error: before a benchmark,
`claude update`, and check `model_ids` in the report.

## 5. Choose

- `play`: the fastest variant with no lost levels; a cheaper one if it is within about 10 % of it.
- `study`: keep the strongest configuration unless a benchmark on learning (step 3 repeated with
  another variant on a new mechanic) shows a cheaper one learns as well.

## 6. Pull request

Move the game from `local.yaml` `onboarding` to `games.yaml` with its models, and add the benchmark
report as `docs/bench/<bench id>.md` (the report's table and the choice with its reason):

```yaml
  - id: com.example.game
    title: Example Game
    models:
      study: fable:xhigh
      play: sonnet:low
```

Unpause the routines.

## Writers

The wiki writer and the dream are chosen on recorded material, without the phone: give the same
sessions to each candidate (model × effort), score the output against the schema's checklist (pages:
entry point and screen frames, every tab with its frame, sources; process: concrete, sourced
proposals) and pick the cheapest one that scores like the best. Record the choice in `project.yaml`
`models` with a short report in `docs/bench/`.
