# Agent Workflow

Use [skills/agent-dev-loop/SKILL.md](/home/zhibai/projects/aiAgnet/skills/agent-dev-loop/SKILL.md) for multi-step development work that should continue with minimal user interruption.

## Default Contract

- Create project memory under `.codex-agent/` before substantial work in a new repo or subproject.
- Create or reuse a task directory under `.codex-agent/tasks/` for any substantial coding task.
- Keep `TASK.md`, `STATE.md`, `DECISIONS.md`, `EVIDENCE.md`, `RUNS.md`, `BACKLOG.md`, and `RESULTS.md` updated as the handoff contract.
- Continue through multiple implementation batches by default; do not stop after a single micro-step.
- Interrupt the user only for hard blockers: approvals, missing secrets or access, destructive actions, conflicting user changes, or user-owned product decisions.
- Run an execution pass and then a review pass before declaring completion.
- Before ending a turn, leave `STATE.md` with a concrete next action and record verification evidence.

## Project Bootstrap

Run this once per repo or subproject:

```bash
python3 skills/agent-dev-loop/scripts/init_agent_project.py "<project-name>" --root .
```

## Bootstrap

Run:

```bash
python3 skills/agent-dev-loop/scripts/init_agent_task.py <slug> "<objective>" --root .
```

For commands expected to run a long time:

```bash
python3 skills/agent-dev-loop/scripts/start_long_run.py .codex-agent/tasks/<task-id> <label> -- <command ...>
```

To resume a task in a later session, point Codex at the existing task directory or render a compact resume prompt with:

```bash
python3 skills/agent-dev-loop/scripts/render_resume_prompt.py .codex-agent/tasks/<task-id>
```
