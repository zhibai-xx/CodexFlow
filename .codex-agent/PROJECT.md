# Project Memory

- Project: `aiAgnet`
- Root: `/home/zhibai/projects/aiAgnet`
- Created: `2026-03-13`

## Purpose

Build and refine a reusable Codex agent workflow that can be applied inside this repo first, then copied into future project repos after it proves useful.

## Repo Map

- Primary application paths: `skills/agent-dev-loop/`
- Test paths: script-level validation and smoke tests executed manually from the repo root
- Tooling and config: root `AGENTS.md`, skill `references/`, skill `assets/`, skill `scripts/`

## Main Commands

- Install: none yet
- Run: `python3 skills/agent-dev-loop/scripts/<script>.py ...`
- Test: `python3 /home/zhibai/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/agent-dev-loop`
- Lint: none yet
- Build: none yet

## Architecture Notes

- Entry points: [AGENTS.md](/home/zhibai/projects/aiAgnet/AGENTS.md) and [SKILL.md](/home/zhibai/projects/aiAgnet/skills/agent-dev-loop/SKILL.md)
- Data flow: user request -> project memory -> task directory -> implementation batch -> evidence -> review -> resumable handoff
- Integration boundaries: project-level memory under `.codex-agent/`, reusable skill assets under `skills/`, temporary smoke tests under `/tmp`

## Risk Areas

- Fragile modules: task-state schema changes that invalidate older tasks; long-run command orchestration
- Expensive commands: future real-project tests may run for more than 30 minutes and must use detached run logs
- External dependencies: local Codex skill tooling under `/home/zhibai/.codex/skills/.system/skill-creator`

## Delivery Constraints

- Performance: optimize for low-friction operation and short context, not process ceremony
- Security: do not encode secrets in templates or logs
- Compatibility: keep scripts plain Python 3 and file formats simple markdown/json
- Release or rollback concerns: preserve backward compatibility for existing task directories whenever practical
