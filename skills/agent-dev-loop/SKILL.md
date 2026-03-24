---
name: agent-dev-loop
description: Run longer autonomous software-development loops with persistent project memory, task state, verification evidence, and low-interruption handoffs. Use when Codex should drive a multi-step coding task across onboarding, implementation, testing, long-running commands, review, and resumable checkpoints instead of stopping after a short exchange.
---

# Agent Dev Loop

## Overview

Turn a request into a resumable project and task workflow. Keep working in meaningful batches until the objective is complete or a hard blocker requires user input.

## Bootstrap the Project

If the repo does not already have project memory, run:

```bash
python3 scripts/init_agent_project.py "<project-name>" --root <repo-root>
```

Fill in `.codex-agent/PROJECT.md` with architecture, commands, risks, and delivery constraints. Fill in `.codex-agent/TASTE.md` with the product, UX, and code-quality standards that should shape future decisions.
Fill in `.codex-agent/ROADMAP.md` with the approved milestone sequence, autonomy budget, allowed decisions, and milestone stop conditions.

Read `references/project-bootstrap.md` for the startup sequence and `references/taste-rubric.md` before defining quality standards.

Before inventing a new workflow, discover available skills:

```bash
python3 scripts/discover_skills.py --repo-root <repo-root> "<task or domain>"
```

## Start the Task

Use this skill for feature work, bug investigations, refactors, migrations, long test runs, and any task that is likely to span multiple edits or validations. Skip it for trivial one-shot questions or tiny edits that do not need state.

If no task directory exists yet, run:

```bash
python3 scripts/init_agent_task.py <slug> "<objective>" --root <repo-root>
```

Write the concrete task brief into `TASK.md` before substantial execution. Include the user objective, constraints, acceptance criteria, the narrowest practical validation plan, and any explicit stop conditions.
If `ROADMAP.md` exists, link the task to the current milestone and inherit its autonomy budget and auto-continue rules.

## Run the Loop

Follow this cycle:

1. Gather context from the repo, project memory, and the existing task files.
2. Convert the objective into a short executable plan.
3. Execute a meaningful batch of work instead of a single micro-step.
4. Verify the batch with the narrowest command, test, lint, or direct inspection that proves the change.
5. Update the task files before continuing or stopping.
6. Run a review pass before marking the task complete.

Continue into the next batch by default. Do not stop merely because one implementation step finished.
If the current task completes and `ROADMAP.md` already approves the next task in the milestone sequence, create the next task and continue without asking the user again.

Read these references as needed:

- `references/workflow.md` for batching, state discipline, and skill/tool discovery
- `references/milestone-mode.md` for milestone-driven execution and auto-continue behavior
- `references/skill-discovery.md` for how to search, rank, and record skill choices
- `references/long-runs.md` for commands that may run for 30 minutes or longer
- `references/review-mode.md` for execution vs review stages
- `references/interrupt-rules.md` for the conditions that justify interrupting the user

## Keep the Task Resumable

Treat the project and task directories as the handoff contract for the next Codex session.

Project-level memory:

- `.codex-agent/PROJECT.md`: architecture, commands, repo map, and risk areas
- `.codex-agent/TASTE.md`: product, UX, code, and communication standards
- `.codex-agent/ROADMAP.md`: approved task sequence, autonomy budget, and milestone stop rules

Task-level state:

- `TASK.md`: stable problem statement and acceptance criteria
- `STATE.md`: current phase, completed work, next actions, blockers, and verification status
- `DECISIONS.md`: decisions made, rationale, tradeoffs, and reversals
- `EVIDENCE.md`: test evidence, command results, and inspection findings
- `RUNS.md`: append-only log of long-running commands
- `BACKLOG.md`: discovered follow-up work that is out of scope for the current task
- `RESULTS.md`: user-facing outcome and remaining risks

Before ending a turn, leave `STATE.md` with a concrete next action. If the task is complete, record the review outcome and completion evidence in `RESULTS.md`.

## Use the Resources

- `scripts/init_agent_project.py`: create project-level memory under `.codex-agent/`
- `scripts/init_agent_task.py`: create a new task directory from templates
- `scripts/discover_skills.py`: discover and rank available repo-local and Codex-home skills
- `scripts/start_long_run.py`: launch a long-running command with logs and metadata
- `scripts/inspect_long_run.py`: inspect a long-running command and tail its logs
- `scripts/render_resume_prompt.py`: print a compact resume prompt for a future Codex session
- `assets/project-template/`: project-memory templates
- `assets/task-template/`: task-state templates

Prefer the scripts and templates over recreating these files by hand.
