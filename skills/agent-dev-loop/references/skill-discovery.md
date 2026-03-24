# Skill Discovery

## Goal

Find the smallest useful set of skills before inventing a custom workflow.

## Discovery Order

1. Check repo-local skills under `skills/`
2. Check Codex-home skills under `~/.codex/skills/`
3. Check reusable scripts already present in the repo
4. Only invent a new workflow if the above do not cover the need

## Command

Use:

```bash
python3 scripts/discover_skills.py --repo-root <repo-root> "<task or domain>"
```

The script ranks skills by overlap between the query and each skill's `name` and `description`.

## Selection Rules

- Prefer the minimal set of skills that covers the task.
- Prefer repo-local skills when they are tailored to the current workflow.
- Add a second skill only when it contributes a genuinely different capability.
- Record chosen and rejected skills in the `Skill Plan` section of `TASK.md`.
- If no good skill exists, note the gap in `BACKLOG.md` instead of hiding it.
