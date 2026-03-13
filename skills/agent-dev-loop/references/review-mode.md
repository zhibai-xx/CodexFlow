# Review Mode

## Default Model

Use a two-stage quality gate:

1. Execution stage: implement the change and gather evidence.
2. Review stage: inspect the result for correctness, regression risk, and quality.

The same Codex session may perform both stages. A second Codex session or window is optional and should be reserved for risky work, large refactors, or release-critical tasks.

## Execution Stage

Focus on delivery:

- understand the code
- make the change
- run the narrowest validation that proves the change
- record evidence and state

## Review Stage

Switch mindset and search for defects:

- mismatched acceptance criteria
- missing tests or weak validation
- edge cases and rollback risks
- code-quality regressions
- product and UX rough edges

When reviewing UI or product-facing work, also read `taste-rubric.md`.

## Completion Rule

Do not mark the task complete until the review stage either:

- finds no blocking issues, or
- records the remaining issues explicitly in `RESULTS.md`
