# Project Agent Entry

This project uses the external CodexFlow brain at `__BRAIN_ROOT__`.

## Read Order

1. Read `__BRAIN_ROOT__/MASTER_BOOTSTRAP.md`
2. Read `__BRAIN_ROOT__/AGENTS.md`
3. Read local `.codex-agent/PROJECT.md`
4. Read local `.codex-agent/TASTE.md`
5. Read local `.codex-agent/ROADMAP.md`

## Behavior

- Do not scan the external brain repository indiscriminately.
- Use the external brain skills under `__BRAIN_ROOT__/skills/`.
- If there is an active inception packet, continue idea clarification before coding.
- If there is an active task, continue from `.codex-agent/tasks/`.
- If `ROADMAP.md` approves the next task and the autonomy budget remains, continue automatically instead of reporting after every completed task.

## Local Mode

- Project root: `__PROJECT_ROOT__`
- Project name: `__PROJECT_NAME__`
- Bootstrap source: `__BRAIN_ROOT__/codexflow-init`
