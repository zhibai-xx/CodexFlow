# Milestone Mode

## Purpose

Prevent the agent from stopping after every clean task boundary.

Use milestone mode when the project already knows a sequence of approved tasks. In this mode, the agent should optimize for completing the current milestone, not merely the current task.

## Required File

Create `.codex-agent/ROADMAP.md` and keep it current.

The roadmap should define:

- current milestone
- approved task sequence
- autonomy budget
- allowed default decisions
- milestone-level stop conditions

## Auto-Continue Rule

When all of these are true, the agent should continue without asking the user:

1. the current task is complete
2. the next task is already approved in `ROADMAP.md`
3. the next task does not require new secrets, permissions, or user-owned product decisions
4. the autonomy budget is not exhausted

In that case, create the next task, update state, and keep working.

## When to Stop

Stop only when one of these happens:

- the milestone is complete
- the autonomy budget is exhausted
- a hard blocker appears
- the roadmap is no longer sufficient to choose the next task safely

## User Updates

Do not report after every task. Report at:

- milestone completion
- budget exhaustion
- hard blockers
- genuinely important outcome changes
