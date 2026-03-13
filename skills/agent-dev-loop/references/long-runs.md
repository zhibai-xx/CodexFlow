# Long Runs

## When to Use This Protocol

Use the long-run protocol for tests, builds, benchmarks, migrations, crawls, or data jobs that may run for 30 minutes or longer.

## Goals

- Keep the command detached from the current chat turn
- Preserve stdout, stderr, status, and exit code
- Leave enough evidence for a later Codex session to inspect the run

## Start the Run

Launch the command with:

```bash
python3 scripts/start_long_run.py <task-dir> <label> -- <command ...>
```

The script creates a run directory under `<task-dir>/runs/` and writes:

- `meta.json`
- `command.txt`
- `stdout.log`
- `stderr.log`

It also appends a record to `RUNS.md`.

## Inspect the Run

Inspect progress with:

```bash
python3 scripts/inspect_long_run.py <run-dir>
```

Poll until the run is complete or a failure requires action. Summarize the important findings in `EVIDENCE.md` instead of copying raw logs into the chat.

## Recording Rules

- Record the purpose of the run before launching it.
- Record the outcome in `EVIDENCE.md` after reading the result.
- Record any follow-up work in `BACKLOG.md` if it is outside the current task.

## Stop Conditions

Interrupt the user only if the long run is blocked by missing access, dangerous side effects, or a result that requires a user-owned decision.
