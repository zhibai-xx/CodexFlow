# Workflow

## Activation

Use this workflow when the request is likely to need more than one implementation batch, more than one validation step, a long-running command, or a resumable handoff.

## Startup Order

Before substantial work:

1. Read `.codex-agent/PROJECT.md` if it exists.
2. Read `.codex-agent/TASTE.md` if it exists.
3. Inspect local `AGENTS.md`, available skills, and reusable scripts.
4. Read the current task directory.

Prefer existing skills, scripts, and templates over inventing a new process from scratch.

## Batch Size

Aim for a batch that includes:

1. Enough context gathering to act safely
2. One cohesive code change or investigation result
3. At least one verification step
4. A state update

Avoid the "one shell command, then stop" pattern unless a hard blocker appears.

## Execution Standard

Drive each batch with this order:

1. Read only the files needed to understand the current slice of work.
2. Form or revise a short plan.
3. Make the code or configuration changes.
4. Run the narrowest validation that proves the change.
5. Record what changed, what passed, what failed, and what comes next.

For commands that may take 30 minutes or longer, switch to the long-run protocol in `long-runs.md`.

## State Discipline

Update `STATE.md` whenever the active phase changes or a meaningful batch finishes.

Keep these fields current:

- `Status`
- `Active phase`
- `Completed this session`
- `In progress`
- `Next actions`
- `Blockers`
- `Verification`
- `Files touched`

Update `DECISIONS.md` when you choose between alternatives, accept a tradeoff, or discover a constraint that should survive a session reset.

Update `EVIDENCE.md` when a command, test, or inspection produces evidence.

Update `RUNS.md` when detached commands are launched or completed.

Update `BACKLOG.md` when you discover relevant work that should not be executed in the current task.

Update `RESULTS.md` when the user-facing outcome changes materially.

## Review Standard

Before completion, switch from execution mode to review mode:

1. Re-check the acceptance criteria
2. Review the code and evidence for correctness and regression risk
3. Review product and UX quality against `taste-rubric.md` when relevant
4. Record unresolved risks in `RESULTS.md`

## Completion Standard

Do not mark the task complete until all of these are true:

1. The requested outcome is implemented or the investigation answer is established.
2. Verification evidence is recorded.
3. A review pass has been completed.
4. Remaining risks are explicit.
5. The next Codex session could understand the result by reading the project and task files alone.
