# Project Bootstrap

## Startup Sequence

Use this sequence when entering a new repo or subproject:

1. Create project memory with `init_agent_project.py` if `.codex-agent/PROJECT.md` does not exist.
2. Fill in `ROADMAP.md` with the current milestone, approved task sequence, autonomy budget, and allowed default decisions.
3. Read `PROJECT.md`, `TASTE.md`, and `ROADMAP.md` before substantial work.
4. Inspect local `AGENTS.md`, available skills, and reusable scripts before inventing a new workflow.
5. Run `discover_skills.py --repo-root <repo-root> "<task or domain>"` to rank applicable skills.
6. Start a task directory with `init_agent_task.py`.
7. Fill in acceptance criteria and validation commands before implementation.

## Project Memory Standard

Keep project memory short but useful:

- architecture map
- main commands
- test entrypoints
- risky areas
- coding and product standards
- milestone sequence and autonomy policy

Do not turn project memory into a wiki. Update it only when the information would help a future Codex session act correctly.
