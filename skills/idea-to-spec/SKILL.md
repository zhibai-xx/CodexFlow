---
name: idea-to-spec
description: Turn raw product or project ideas into clarified requirements, ambiguity checks, a buildable specification, and a first implementation plan. Use when the user has an initial concept, brainstorm, feature idea, startup idea, or vague project direction that needs sharper thinking before execution starts.
---

# Idea to Spec

## Overview

Convert a rough idea into an inception packet that a future Codex session can build from without re-deriving the problem. Challenge the idea where it is ambiguous, underspecified, contradictory, or too broad, then rewrite it into a concrete first-phase spec.

## Start with Friction, Not Blind Agreement

Do not jump directly from the user's inspiration to implementation. First:

1. Restate the idea in plain terms.
2. Identify what problem it solves, for whom, and how success would be judged.
3. Detect ambiguity, hidden assumptions, overloaded words, and likely misunderstandings.
4. Rewrite the idea into a cleaner version before asking for more details.

Ask only the highest-leverage questions. Prefer proposing an interpretation plus the specific uncertainty, instead of asking broad open-ended questions with no structure.

Read `references/clarification-rubric.md` before shaping the first response.

## Create an Inception Packet

If no inception packet exists yet, run:

```bash
python3 scripts/init_inception_packet.py <slug> "<idea summary>" --root <repo-root>
```

Use the generated files as the contract for the idea-shaping phase:

- `IDEA.md`: original idea, rewritten idea, user, problem, and first boundaries
- `QUESTIONS.md`: critical ambiguities, assumptions, and high-value clarification questions
- `SPEC.md`: scoped first-phase product or project spec
- `PLAN.md`: first implementation slice, risks, and sequencing

Prefer filling these files over keeping the reasoning only in chat.

## Run the Inception Workflow

Follow this order:

1. Capture the raw idea without embellishing it.
2. Rewrite it into a clearer problem statement.
3. Stress-test the statement against user, workflow, data, output, constraints, and failure modes.
4. Surface the most dangerous ambiguities and propose defaults.
5. Define the first version scope and explicit non-goals.
6. Produce the first executable plan.

Do not aim for a perfect master spec. Aim for a spec that is sharp enough to build the first phase safely.

Read these references as needed:

- `references/clarification-rubric.md` for how to critique and rewrite the idea
- `references/spec-shape.md` for what the resulting spec should contain

## Quality Bar

The skill should improve the user's original idea in four ways:

1. Make the objective easier to understand
2. Reduce ambiguity that would cause engineering waste
3. Shrink the first buildable scope to something defensible
4. Leave future implementation with explicit assumptions and acceptance criteria

If the idea is weak, say why. If it is promising but vague, sharpen it. If it is too large, cut it into phases.

## Use the Resources

- `scripts/init_inception_packet.py`: create an inception packet under `.codex-agent/inception/`
- `assets/inception-template/`: markdown templates for the packet

Prefer the script and templates over recreating these files by hand.
