# Event Layer

## Purpose

Use a lightweight append-only event stream to record material facts without turning CodexFlow into a heavy state platform.

Markdown snapshots remain the main human entrypoints:

- `PROJECT.md`
- `TASTE.md`
- `ROADMAP.md`
- `TASK.md`
- `STATE.md`

The event layer exists to support auditability, recovery, and short factual history.

## Files

- Project-level events: `.codex-agent/events/project-events.jsonl`
- Task-level events: `.codex-agent/tasks/<task-id>/EVENTS.jsonl`

## Rules

- Append events; do not rewrite old event lines.
- Record only material facts, not every shell command.
- Prefer one meaningful event per batch, boundary, review, blocker, or long-run state change.
- If the snapshots and the events disagree, update the snapshots first, then record an event that explains the change.

## Good Event Types

- `task-created`
- `phase-changed`
- `baseline-locked`
- `validation-passed`
- `validation-failed`
- `review-complete`
- `blocked`
- `long-run-started`
- `long-run-finished`

## When To Read Events

- Recent state is unclear
- The task crossed multiple sessions
- A timeline or audit trail matters
- You need to reconstruct what changed between snapshots

Do not front-load the whole event stream into every new session. Read it only when it is useful.

## Tooling

Use `scripts/append_event.py` for structured event writes:

```bash
python3 scripts/append_event.py .codex-agent review-complete "Locked the current milestone review notes"
python3 scripts/append_event.py .codex-agent/tasks/<task-id> validation-passed "Unit tests passed" --artifact tests --status passed
```
