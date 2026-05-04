# CodexFlow Bootstrap

This file is the single entrypoint for projects that use `/home/zhibai/projects/aiAgnet` as an external brain.

Do not scan this repository indiscriminately. Read this file first, then only the specific referenced files needed for the current mode.

## Read Order

1. Read the local project `AGENTS.md`
2. Read the local `.codex-agent/PROJECT.md`
3. Read the local `.codex-agent/TASTE.md`
4. Read only the local taste layer files that `TASTE.md` marks active
5. Read the local `.codex-agent/ROADMAP.md`
6. If the project has an active inception packet, use `idea-to-spec`
7. If the project has an active task, use `agent-dev-loop`
8. If the user asks to evaluate a task or milestone, use `agent-eval`

## Startup Algorithm

### If the project is not initialized

- Ask the user to run `/home/zhibai/projects/aiAgnet/codexflow-init` in the project root, or run it yourself if the project already trusts this external brain.
- Do not invent local process files manually if the bootstrap tool is available.

### If the user starts with a rough idea

- Use `idea-to-spec`
- Ask only high-leverage clarification questions
- Rewrite the idea into a cleaner problem statement
- Produce or update the inception packet before implementation

### If the project already has an active task

- Use `agent-dev-loop`
- Resume from `.codex-agent/tasks/...`
- Obey `ROADMAP.md` for milestone sequence and autonomy budget
- Use `.codex-agent/events/project-events.jsonl` or task `EVENTS.jsonl` only when recent history is unclear
- Continue into the next approved task when allowed; do not stop after every clean slice

### If the user asks whether the agent process is good enough

- Use `agent-eval`
- Score the run against autonomy, state, verification, interruption, and output quality

## Core Files

- `/home/zhibai/projects/aiAgnet/AGENTS.md`
- `/home/zhibai/projects/aiAgnet/skills/agent-dev-loop/SKILL.md`
- `/home/zhibai/projects/aiAgnet/skills/idea-to-spec/SKILL.md`
- `/home/zhibai/projects/aiAgnet/skills/agent-eval/SKILL.md`

Read only the specific skill needed for the current phase.

## Design Rules

- Prefer a thin local project entrypoint plus this central bootstrap over “read all external files”.
- Keep state on disk, not in the chat history.
- Keep snapshots as the human entrypoint and use append-only events only for factual history.
- Keep taste layered; do not load inactive taste files by default.
- Treat `ROADMAP.md` as the authority for milestone-level auto-continue behavior.
- Stop only for hard blockers, budget exhaustion, or milestone boundaries.
