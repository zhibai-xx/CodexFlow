#!/usr/bin/env python3
"""Create a persistent task directory for the agent-dev-loop skill."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path


def normalize_slug(raw: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", raw.strip().lower())
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "task"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize a Codex agent task directory.",
    )
    parser.add_argument("slug", help="Short task identifier")
    parser.add_argument("objective", help="Task objective in one sentence")
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root that should contain .codex-agent/tasks",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    script_dir = Path(__file__).resolve().parent
    template_dir = script_dir.parent / "assets" / "task-template"
    repo_root = Path(args.root).resolve()
    agent_root = repo_root / ".codex-agent"
    tasks_root = agent_root / "tasks"
    task_id = f"{date.today():%Y%m%d}-{normalize_slug(args.slug)}"
    task_dir = tasks_root / task_id

    if task_dir.exists():
        print(f"[ERROR] Task directory already exists: {task_dir}", file=sys.stderr)
        return 1

    tasks_root.mkdir(parents=True, exist_ok=True)
    task_dir.mkdir(parents=True, exist_ok=False)

    replacements = {
        "__TASK_ID__": task_id,
        "__DATE__": str(date.today()),
        "__REPO_ROOT__": str(repo_root),
        "__OBJECTIVE__": args.objective.strip(),
    }

    for template_path in sorted(template_dir.glob("*.md")):
        content = template_path.read_text(encoding="utf-8")
        for placeholder, value in replacements.items():
            content = content.replace(placeholder, value)
        output_path = task_dir / template_path.name
        output_path.write_text(content, encoding="utf-8")

    print(task_dir)
    print("")
    print("Next:")
    print(f"  1. Fill in {task_dir / 'TASK.md'}")
    print(f"  2. Update {task_dir / 'STATE.md'} and {task_dir / 'EVIDENCE.md'} after each work batch")
    print(f"  3. If present, link the task to {agent_root / 'ROADMAP.md'} and set auto-continue rules")
    print(f"  4. Use {script_dir / 'render_resume_prompt.py'} {task_dir} for the next session")
    if not (agent_root / "PROJECT.md").exists():
        print(f"  5. Consider bootstrapping project memory with {script_dir / 'init_agent_project.py'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
