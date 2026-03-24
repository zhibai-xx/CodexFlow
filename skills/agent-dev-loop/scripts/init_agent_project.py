#!/usr/bin/env python3
"""Create project-level memory for the agent-dev-loop skill."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize project memory for Codex agent work.",
    )
    parser.add_argument("project_name", help="Human-readable project or subproject name")
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root that should contain .codex-agent/",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    script_dir = Path(__file__).resolve().parent
    template_dir = script_dir.parent / "assets" / "project-template"
    repo_root = Path(args.root).resolve()
    agent_root = repo_root / ".codex-agent"
    tasks_dir = agent_root / "tasks"

    agent_root.mkdir(parents=True, exist_ok=True)
    tasks_dir.mkdir(parents=True, exist_ok=True)

    replacements = {
        "__PROJECT_NAME__": args.project_name.strip(),
        "__REPO_ROOT__": str(repo_root),
        "__DATE__": str(date.today()),
    }

    created = []
    for template_path in sorted(template_dir.glob("*.md")):
        output_path = agent_root / template_path.name
        if output_path.exists():
            continue
        content = template_path.read_text(encoding="utf-8")
        for placeholder, value in replacements.items():
            content = content.replace(placeholder, value)
        output_path.write_text(content, encoding="utf-8")
        created.append(output_path)

    print(agent_root)
    if created:
        print("")
        print("Created:")
        for path in created:
            print(f"  - {path}")
    else:
        print("")
        print("No new project-memory files were needed.")
    roadmap_path = agent_root / "ROADMAP.md"
    if roadmap_path.exists():
        print(f"Roadmap: {roadmap_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
