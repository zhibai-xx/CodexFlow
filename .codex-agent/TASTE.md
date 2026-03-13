# Taste Standards

- Project: `aiAgnet`
- Root: `/home/zhibai/projects/aiAgnet`
- Created: `2026-03-13`

## Product Standards

- What should feel simple for the user: starting a task, resuming a task, and understanding what the agent is doing next
- What should never be surprising: unnecessary interruptions, hidden state, or mandatory process overhead with no delivery value

## UX Standards

- Primary user path: bootstrap project memory once, create a task, let Codex run in batches, resume from disk when needed
- Error handling expectations: prefer explicit blockers, concrete next actions, and recoverable handoffs over vague failures
- Copy and naming expectations: keep names concrete, operational, and short; avoid theatrical wording

## Code Standards

- Preferred patterns: small deterministic scripts, append-only evidence where possible, markdown templates with clear fields
- Patterns to avoid: speculative abstractions, document sprawl, unclear status transitions, brittle parsing
- Review priorities: task resumability, validation evidence, interruption quality, and correctness of long-run orchestration

## Communication Standards

- How to report progress: summarize intent, current batch, blockers, and verified outcomes rather than narrating every command
- What evidence matters most: exact commands, validation outcome, residual risk, and next action
- What tradeoffs must be surfaced: any extra process burden, missing automation, or quality-vs-speed compromise
