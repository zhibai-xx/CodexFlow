#!/usr/bin/env python3
"""Attach a project directory to the CodexFlow external brain."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path


def normalize_slug(raw: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", raw.strip().lower())
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "idea"


def render_template(path: Path, replacements: dict[str, str]) -> str:
    content = path.read_text(encoding="utf-8")
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)
    return content


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def ensure_gitignore(project_root: Path) -> None:
    block = (
        "\n# CodexFlow runtime state\n"
        ".codex-agent/tasks/\n"
        ".codex-agent/inception/\n"
        ".codex-agent/evals/\n"
        ".codex-agent/events/\n"
        ".codex-agent/**/*.log\n"
    )
    gitignore_path = project_root / ".gitignore"
    existing = gitignore_path.read_text(encoding="utf-8") if gitignore_path.exists() else ""
    if "# CodexFlow runtime state" not in existing:
        new_content = existing.rstrip() + ("\n" if existing and not existing.endswith("\n") else "") + block
        gitignore_path.write_text(new_content, encoding="utf-8")


def seed_project_memory(agent_root: Path, project_name: str, project_root: Path, brain_root: Path) -> list[Path]:
    template_dir = brain_root / "skills" / "agent-dev-loop" / "assets" / "project-template"
    replacements = {
        "__PROJECT_NAME__": project_name,
        "__REPO_ROOT__": str(project_root),
        "__DATE__": str(date.today()),
    }
    created: list[Path] = []
    for template_path in sorted(path for path in template_dir.rglob("*") if path.is_file()):
        output_path = agent_root / template_path.relative_to(template_dir)
        if write_if_missing(output_path, render_template(template_path, replacements)):
            created.append(output_path)
    return created


def seed_roadmap(agent_root: Path, idea: str | None, mode: str) -> None:
    roadmap_path = agent_root / "ROADMAP.md"
    if not roadmap_path.exists():
        return
    existing = roadmap_path.read_text(encoding="utf-8")
    if "## Current Milestone\n\n- Name:\n- Objective:\n- Done when:\n" not in existing:
        return

    if mode == "inception":
        milestone_name = "inception"
        objective = "Turn the rough project idea into a scoped phase-1 spec and an approved first delivery slice."
        done_when = "The latest inception packet has a stable SPEC.md and PLAN.md, and the first delivery task can start without major ambiguity."
        sequence = [
            "[approved] clarify-and-rewrite-idea -> restate the project and surface the highest-risk ambiguities",
            "[approved] lock-phase-1-spec -> define scope, non-goals, outputs, constraints, and acceptance criteria",
            "[approved] open-first-delivery-task -> convert the spec into the first implementation task",
        ]
    else:
        milestone_name = "delivery"
        objective = "Execute the current approved phase using resumable tasks and milestone-driven continuity."
        done_when = "The approved milestone tasks are complete or a milestone stop condition is reached."
        sequence = [
            "[approved] discover-context -> understand the codebase, constraints, and active artifacts",
            "[approved] execute-first-task -> implement the first approved delivery slice",
        ]

    updated = existing.replace(
        "## Current Milestone\n\n- Name:\n- Objective:\n- Done when:\n",
        (
            "## Current Milestone\n\n"
            f"- Name: {milestone_name}\n"
            f"- Objective: {objective}\n"
            f"- Done when: {done_when}\n"
        ),
    )
    updated = updated.replace(
        "## Approved Task Sequence\n\n1. `[pending]` Replace with the first approved task slug and objective.\n2. `[pending]` Replace with the second approved task slug and objective.\n",
        "## Approved Task Sequence\n\n" + "\n".join(f"{index}. `{item}`" for index, item in enumerate(sequence, start=1)) + "\n",
    )
    roadmap_path.write_text(updated, encoding="utf-8")


def create_local_agents(project_root: Path, project_name: str, brain_root: Path) -> None:
    template_path = brain_root / "bootstrap" / "project-agents-template.md"
    content = render_template(
        template_path,
        {
            "__BRAIN_ROOT__": str(brain_root),
            "__PROJECT_ROOT__": str(project_root),
            "__PROJECT_NAME__": project_name,
        },
    )
    write_if_missing(project_root / "AGENTS.md", content)


def create_start_file(project_root: Path, project_name: str, brain_root: Path, mode: str) -> Path:
    template_path = brain_root / "bootstrap" / "first-message-template.md"
    content = render_template(
        template_path,
        {
            "__BRAIN_ROOT__": str(brain_root),
            "__PROJECT_ROOT__": str(project_root),
            "__PROJECT_NAME__": project_name,
            "__MODE__": mode,
        },
    )
    output_path = project_root / "START_Codex.md"
    if not output_path.exists():
        output_path.write_text(content, encoding="utf-8")
    return output_path


def create_inception_packet(agent_root: Path, brain_root: Path, project_name: str, idea: str) -> Path:
    template_dir = brain_root / "skills" / "idea-to-spec" / "assets" / "inception-template"
    packet_id = f"{date.today():%Y%m%d}-{normalize_slug(project_name)}"
    packet_dir = agent_root / "inception" / packet_id
    packet_dir.mkdir(parents=True, exist_ok=True)

    replacements = {
        "__PACKET_ID__": packet_id,
        "__DATE__": str(date.today()),
        "__REPO_ROOT__": str(agent_root.parent),
        "__IDEA__": idea.strip(),
    }
    for template_path in sorted(template_dir.glob("*.md")):
        output_path = packet_dir / template_path.name
        if not output_path.exists():
            output_path.write_text(render_template(template_path, replacements), encoding="utf-8")
    return packet_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize a new project to use the CodexFlow external brain.",
    )
    parser.add_argument(
        "--project-root",
        default=".",
        help="Project root to attach to CodexFlow; defaults to the current directory",
    )
    parser.add_argument(
        "--project-name",
        help="Human-readable project name; defaults to the project directory name",
    )
    parser.add_argument(
        "--idea",
        help="Optional rough project idea; if provided, inception mode is initialized automatically",
    )
    parser.add_argument(
        "--brain-root",
        help="Optional path to the CodexFlow brain; defaults to this repository",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Prompt for missing values interactively",
    )
    return parser.parse_args()


def prompt_text(label: str, default: str | None = None, optional: bool = False) -> str | None:
    suffix = f" [{default}]" if default else ""
    raw = input(f"{label}{suffix}: ").strip()
    if raw:
        return raw
    if default is not None:
        return default
    if optional:
        return None
    return ""


def prompt_yes_no(label: str, default: bool = True) -> bool:
    suffix = "Y/n" if default else "y/N"
    raw = input(f"{label} [{suffix}]: ").strip().lower()
    if not raw:
        return default
    return raw in {"y", "yes"}


def maybe_prompt(args: argparse.Namespace) -> argparse.Namespace:
    if len(sys.argv) > 1 and not args.interactive:
        return args

    project_root = Path(args.project_root).resolve()
    inferred_name = args.project_name or project_root.name
    print("CodexFlow init")
    print(f"Project root: {project_root}")

    args.project_name = prompt_text("Project name", inferred_name) or inferred_name
    want_inception = prompt_yes_no("Start from a rough idea / inception flow", default=bool(args.idea) or True)
    if want_inception:
        args.idea = prompt_text("One-sentence project idea", args.idea, optional=False) or args.idea
    else:
        args.idea = None
    return args


def main() -> int:
    args = maybe_prompt(parse_args())
    brain_root = Path(args.brain_root).resolve() if args.brain_root else Path(__file__).resolve().parent.parent
    project_root = Path(args.project_root).resolve()
    project_name = args.project_name or project_root.name
    mode = "inception" if args.idea else "delivery"

    agent_root = project_root / ".codex-agent"
    agent_root.mkdir(parents=True, exist_ok=True)
    (agent_root / "tasks").mkdir(parents=True, exist_ok=True)

    created = seed_project_memory(agent_root, project_name, project_root, brain_root)
    create_local_agents(project_root, project_name, brain_root)
    ensure_gitignore(project_root)
    seed_roadmap(agent_root, args.idea, mode)
    start_file = create_start_file(project_root, project_name, brain_root, mode)

    packet_dir = None
    if args.idea:
        packet_dir = create_inception_packet(agent_root, brain_root, project_name, args.idea)

    print(f"Project attached to CodexFlow: {project_root}")
    print(f"Brain root: {brain_root}")
    print(f"Mode: {mode}")
    if created:
        print("Created project memory:")
        for path in created:
            print(f"  - {path}")
    print(f"Local entrypoint: {project_root / 'AGENTS.md'}")
    print(f"Start file: {start_file}")
    print(f"Roadmap: {agent_root / 'ROADMAP.md'}")
    if packet_dir:
        print(f"Inception packet: {packet_dir}")
    print("")
    print("Start Codex in this project and say:")
    print("")
    print(f"Read `{project_root / 'AGENTS.md'}` and start this project.")
    print("")
    print("First:")
    print("- follow the local project AGENTS entrypoint")
    print("- use the external CodexFlow brain")
    print("- read `.codex-agent/PROJECT.md`")
    print("- read `.codex-agent/TASTE.md`")
    print("- then read only the active taste layer files listed in `.codex-agent/TASTE.md`")
    print("- read `.codex-agent/ROADMAP.md`")
    print("- consult `.codex-agent/events/project-events.jsonl` only if recent state is unclear")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
