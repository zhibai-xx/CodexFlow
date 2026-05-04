# Taste Layers

## Purpose

Keep quality standards layered and selective instead of collapsing every rule into one large `TASTE.md`.

## Stack

`TASTE.md` is the index, not the full rule dump.

Default layer order:

1. project
2. domain
3. task

## Rules

- Read `TASTE.md` first.
- Then read only the layers marked active.
- Keep project-wide standards in `taste/project.md`.
- Add a domain layer only when a reusable sub-area needs its own quality bar.
- Add a task layer only for temporary guidance that should not become permanent project doctrine.

## Promotion Rule

When a lesson repeats and clearly applies beyond a single task, promote it upward:

- task -> domain when it applies to one recurring area
- task or domain -> project when it should shape the whole project

Do not auto-promote taste. Upgrade it deliberately.

## Smell Tests

You are overusing taste layers if:

- every task creates a new taste file
- inactive layers are read by default
- the stack becomes a hidden wiki
- local taste starts copying general engineering advice that belongs elsewhere
