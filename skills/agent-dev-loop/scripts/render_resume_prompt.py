#!/usr/bin/env python3
"""Render a compact prompt for resuming an existing agent task."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render a resume prompt for a task directory.",
    )
    parser.add_argument("task_dir", help="Path to the task directory")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    task_dir = Path(args.task_dir).resolve()
    project_dir = task_dir.parent.parent
    print("Continue this task in agent mode:")
    if (project_dir / "PROJECT.md").exists():
        print(f"- Read first: {project_dir / 'PROJECT.md'}")
    if (project_dir / "TASTE.md").exists():
        print(f"- Read first: {project_dir / 'TASTE.md'}")
    print(f"- Task directory: {task_dir}")
    print(f"- Read: {task_dir / 'TASK.md'}")
    print(f"- Read: {task_dir / 'STATE.md'}")
    print(f"- Read if needed: {task_dir / 'DECISIONS.md'}")
    print(f"- Read if needed: {task_dir / 'EVIDENCE.md'}")
    print(f"- Read if needed: {task_dir / 'RUNS.md'}")
    print(f"- Read if needed: {task_dir / 'BACKLOG.md'}")
    print(f"- Read if needed: {task_dir / 'RESULTS.md'}")
    print("- Continue autonomously until the task is complete or a hard blocker appears.")
    print("- Update STATE.md, DECISIONS.md, EVIDENCE.md, and RESULTS.md before stopping.")
    print("- Run an execution pass and then a review pass before declaring completion.")
    print("- Only interrupt for approvals, missing secrets, destructive actions, or user-owned decisions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
