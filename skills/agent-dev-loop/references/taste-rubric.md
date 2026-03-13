# Taste Rubric

Use this rubric when making judgment calls or reviewing output quality. Good taste is not decoration; it is disciplined choice.

## Product Taste

- Solve the user problem directly instead of adding ornamental behavior.
- Prefer clear defaults and fewer decisions on the happy path.
- Keep edge cases explicit rather than silently ignored.

## UX Taste

- Make the primary path obvious.
- Preserve user trust with clear states, errors, and recovery paths.
- Avoid clutter, inconsistent labels, and redundant options.

## Code Taste

- Prefer simple boundaries over clever abstraction.
- Keep names concrete and directional.
- Make the easiest path the safest path.
- Remove dead branches and speculative scaffolding.

## Communication Taste

- Report outcomes, evidence, and risks instead of narrating every micro-step.
- Be specific about what was validated and what remains uncertain.
- Record assumptions where future sessions will need them.

## Scoring Prompt

When the output feels weak, ask:

1. Is this the simplest solution that still respects the real constraints?
2. Did we optimize for the important path instead of the flashy path?
3. Would a strong reviewer see clear intent and acceptable tradeoffs?
