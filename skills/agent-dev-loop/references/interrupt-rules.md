# Interrupt Rules

Interrupt the user only when continuing would be materially unsafe or likely wrong.

## Interrupt Immediately

- A required secret, credential, or external access is missing.
- A destructive action needs approval.
- The repo contains conflicting user changes that change the task direction.
- The task depends on a product or design choice with no safe default.
- Validation reveals multiple plausible fixes and the tradeoff is user-owned.

## Do Not Interrupt

- A single implementation step is done.
- You can continue by inspecting more code.
- You can choose a conservative local default and record it.
- A non-critical test is flaky but the main validation path is available.
- You need to perform the next obvious batch in the same task.

## What to Record Instead of Asking

When you can continue, write the assumption into `DECISIONS.md` and proceed. Keep the next user message focused on outcomes, blockers, or required decisions rather than step-by-step narration.
