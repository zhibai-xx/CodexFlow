# Scoring Guide

## How to Judge

Do not average away serious failures. A run with strong output but no resumable state is not healthy.

Treat these as blockers even if the total score looks acceptable:

- state quality `<= 2`
- verification quality `<= 2`
- output quality `<= 2`

## Good Enough for the Next Milestone

The current agent workflow is good enough to continue only if:

1. No blocking dimension is `<= 2`
2. Total score is at least `18`
3. Action items are recorded for the weakest dimensions

## What to Improve First

- Low autonomy: reduce unnecessary check-ins, strengthen task batching
- Low state quality: improve `STATE.md`, `DECISIONS.md`, `RESULTS.md`
- Low verification quality: improve evidence capture and narrower validation
- Low interruption quality: tighten stop conditions
- Low output quality: strengthen review mode, scope control, or domain-specific skills
