# Agent Workflow

Prefer [MASTER_BOOTSTRAP.md](/home/zhibai/projects/aiAgnet/MASTER_BOOTSTRAP.md) as the single external-brain entrypoint for new projects. Do not tell a new project Codex session to “read everything” in this repository.

Use [skills/agent-dev-loop/SKILL.md](/home/zhibai/projects/aiAgnet/skills/agent-dev-loop/SKILL.md) for multi-step development work that should continue with minimal user interruption.
Use [skills/idea-to-spec/SKILL.md](/home/zhibai/projects/aiAgnet/skills/idea-to-spec/SKILL.md) when a new project starts from a rough concept and needs clarification before execution.
Use [skills/agent-eval/SKILL.md](/home/zhibai/projects/aiAgnet/skills/agent-eval/SKILL.md) when a task, milestone, or project phase should be evaluated for agent quality.

## External Brain

To attach a fresh project to CodexFlow, run:

```bash
codexflow-init --project-root . --idea "<rough idea>"
```

Or, for an already-defined project:

```bash
codexflow-init --project-root .
```

For the lowest-friction startup, just enter the new project directory and run:

```bash
codexflow-init
```

It will prompt for the project name and whether to start from a rough idea.

This creates:

- a thin local `AGENTS.md` that points back to CodexFlow
- a `START_Codex.md` file containing the exact first message for a new Codex chat
- `.codex-agent/PROJECT.md`
- `.codex-agent/TASTE.md`
- `.codex-agent/ROADMAP.md`
- an inception packet if `--idea` is supplied

After that, start Codex in the project root and either:

- paste the message from `START_Codex.md`, or
- tell it to read the local `AGENTS.md`

## Default Contract

- Create project memory under `.codex-agent/` before substantial work in a new repo or subproject.
- Fill in `.codex-agent/ROADMAP.md` before substantial delivery so the agent knows the approved task sequence and autonomy budget.
- Create or reuse a task directory under `.codex-agent/tasks/` for any substantial coding task.
- Keep `TASK.md`, `STATE.md`, `DECISIONS.md`, `EVIDENCE.md`, `RUNS.md`, `BACKLOG.md`, and `RESULTS.md` updated as the handoff contract.
- Put future product or experiment codebases under `workspaces/` unless they belong in this agent repo itself.
- Treat `workspaces/` as local-only by default; it is reserved for projects like `NovelMatrix` that should not be pushed to this repository's remote.
- Continue through multiple implementation batches by default; do not stop after a single micro-step.
- When `ROADMAP.md` approves the next task and the autonomy budget remains, continue automatically instead of reporting after every completed task.
- Interrupt the user only for hard blockers: approvals, missing secrets or access, destructive actions, conflicting user changes, or user-owned product decisions.
- Run an execution pass and then a review pass before declaring completion.
- Before ending a turn, leave `STATE.md` with a concrete next action and record verification evidence.

## Project Bootstrap

Run this once per repo or subproject:

```bash
python3 skills/agent-dev-loop/scripts/init_agent_project.py "<project-name>" --root .
```

Then fill in `.codex-agent/ROADMAP.md` with:
- current milestone
- approved task sequence
- autonomy budget
- allowed default decisions

If the project starts from a rough idea, create an inception packet first:

```bash
python3 skills/idea-to-spec/scripts/init_inception_packet.py <slug> "<idea summary>" --root .
```

Before inventing a new workflow for a task, discover available skills with:

```bash
python3 skills/agent-dev-loop/scripts/discover_skills.py --repo-root . "<task or domain>"
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

To evaluate whether the current agent workflow is actually performing well:

```bash
python3 skills/agent-eval/scripts/init_eval_packet.py <slug> "<task or milestone summary>" --root .
```
