# Rubric

Score each dimension from 1 to 5.

## 1. Autonomy

- `1`: stops constantly, requires frequent user steering, cannot finish meaningful batches
- `3`: can progress through some batches but still pauses too often or loses momentum
- `5`: sustains progress through multiple meaningful batches and only stops for real blockers

## 2. State Quality

- `1`: new session would need the user to restate context
- `3`: basic resumption is possible, but important assumptions or next actions are missing
- `5`: a new session could resume safely from disk with minimal friction

## 3. Verification Quality

- `1`: claims completion with little or no evidence
- `3`: some checks ran, but important gaps or weak evidence remain
- `5`: evidence is clear, narrow, relevant, and recorded where future sessions can find it

## 4. Interruption Quality

- `1`: interrupts for routine steps or unclear reasons
- `3`: mostly reasonable, but still asks questions it could have answered locally
- `5`: interrupts only for approvals, missing access, destructive actions, or true user-owned decisions

## 5. Output Quality

- `1`: result is unreliable, weakly reasoned, or poor quality
- `3`: result is usable but rough, incomplete, or risky
- `5`: result is defensible, well-scoped, and aligned with project standards

## Passing Heuristic

- `22-25`: strong run
- `18-21`: acceptable but should improve
- `13-17`: weak run; fix process before trusting bigger scopes
- `5-12`: failing run; do not scale the current workflow
