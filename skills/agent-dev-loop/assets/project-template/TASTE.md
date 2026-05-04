# Taste Stack

- Project: `__PROJECT_NAME__`
- Root: `__REPO_ROOT__`
- Created: `__DATE__`

## Purpose

- This file is the index for quality and judgment rules.
- Read this file first, then read only the taste layers marked `active`.
- Keep the stack small. Do not create more than one or two extra layers without a strong reason.

## Current Active Layers

1. `project` -> `.codex-agent/taste/project.md` (`active`)
2. `domain` -> `.codex-agent/taste/domain.md` (`inactive` by default; create only when a reusable domain-specific standard is needed)
3. `task` -> `.codex-agent/taste/task-current.md` (`inactive` by default; create only for short-lived local guidance)

## Load Rules

- Always read active layers in the order listed above.
- Do not read inactive layers unless this file says they are active.
- Promote repeated project-wide lessons into `taste/project.md`.
- Use a domain layer for reusable product, workflow, or interface standards that are narrower than the whole project.
- Use a task layer only for temporary constraints that should not permanently shape the project.

## Activation Notes

- Project layer focus:
- Domain layer activation reason:
- Task layer activation reason:

## Review Reminders

- Product quality priorities:
- UX quality priorities:
- Code quality priorities:
- Communication and reporting priorities:
