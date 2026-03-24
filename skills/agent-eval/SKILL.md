---
name: agent-eval
description: Evaluate Codex-driven delivery quality across autonomy, state quality, verification quality, interruption quality, and output quality. Use when a task, milestone, or project phase should be reviewed to determine whether the agent workflow is actually working or needs changes.
---

# Agent Eval

## Overview

Turn a completed or in-progress Codex run into a structured evaluation. Score the run, identify weaknesses, and leave concrete changes that improve the next iteration instead of relying on vague impressions.

## Evaluate the Right Unit

Use this skill on one of these scopes:

- one task directory under `.codex-agent/tasks/`
- one milestone or project phase
- one full delivery conversation, if its artifacts were written to disk

Prefer a bounded unit over “the whole project” unless the project has already been divided into explicit milestones.

## Start an Evaluation Packet

If no evaluation packet exists yet, run:

```bash
python3 scripts/init_eval_packet.py <slug> "<scope summary>" --root <repo-root>
```

Use the packet as the review contract:

- `SUMMARY.md`: scope, reviewed artifacts, and headline judgment
- `SCORES.md`: scored dimensions and rationale
- `FINDINGS.md`: concrete failures, risks, and examples
- `ACTION_ITEMS.md`: changes to the workflow, skills, prompts, or project process

Prefer filling these files over leaving the evaluation only in chat.

## Run the Review

Read these artifacts before judging the run:

- project memory: `.codex-agent/PROJECT.md`, `.codex-agent/TASTE.md`
- task state: `TASK.md`, `STATE.md`, `DECISIONS.md`, `EVIDENCE.md`, `RUNS.md`, `RESULTS.md`
- relevant code or product output if the task produced one

Then score the run using `references/rubric.md`.

## Review Standard

Judge the run on these dimensions:

1. Autonomy: did the agent keep moving without unnecessary interruptions?
2. State quality: could a new session resume safely from disk?
3. Verification quality: is there evidence, not just claims?
4. Interruption quality: did the agent interrupt only for real blockers?
5. Output quality: is the actual result defensible?

Use `references/scoring-guide.md` for how to interpret scores and when a run should be considered “good enough”.

## Output Standard

An evaluation is useful only if it changes future behavior. Every review should leave:

- at least one concrete finding tied to evidence
- at least one concrete workflow improvement
- an explicit judgment on whether the current agent setup is acceptable for the next milestone

## Use the Resources

- `scripts/init_eval_packet.py`: create an evaluation packet under `.codex-agent/evals/`
- `assets/eval-template/`: packet templates

Prefer the script and templates over recreating these files by hand.
