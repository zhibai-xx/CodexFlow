#!/usr/bin/env python3
"""Append a structured JSONL event to a project or task event log."""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Append a structured event to a CodexFlow project or task event log.",
    )
    parser.add_argument(
        "target",
        help="Path to a .codex-agent directory, a task directory, or a specific .jsonl file",
    )
    parser.add_argument("event_type", help="Short event type, for example review-complete")
    parser.add_argument("summary", help="One-sentence summary of what happened")
    parser.add_argument(
        "--artifact",
        action="append",
        default=[],
        help="Artifact path or identifier to attach to the event; repeat as needed",
    )
    parser.add_argument(
        "--meta",
        action="append",
        default=[],
        metavar="KEY=VALUE",
        help="Extra metadata fields to store; repeat as needed",
    )
    parser.add_argument(
        "--status",
        help="Optional status label, for example passed, failed, or blocked",
    )
    return parser.parse_args()


def parse_meta(items: list[str]) -> dict[str, str]:
    meta: dict[str, str] = {}
    for item in items:
        key, sep, value = item.partition("=")
        if not sep or not key:
            raise SystemExit(f"[ERROR] Invalid --meta entry: {item!r}. Expected KEY=VALUE.")
        meta[key] = value
    return meta


def resolve_event_file(target: Path) -> tuple[Path, dict[str, str]]:
    if target.is_file():
        if target.suffix != ".jsonl":
            raise SystemExit(f"[ERROR] Expected a .jsonl event file, got: {target}")
        return target, {}

    if (target / "TASK.md").exists():
        return target / "EVENTS.jsonl", {"scope": "task", "task_id": target.name}

    if (target / "PROJECT.md").exists():
        return target / "events" / "project-events.jsonl", {"scope": "project"}

    raise SystemExit(
        "[ERROR] Target must be a task directory, a .codex-agent directory, or a specific .jsonl file."
    )


def main() -> int:
    args = parse_args()
    target = Path(args.target).resolve()
    event_file, inferred = resolve_event_file(target)
    event_file.parent.mkdir(parents=True, exist_ok=True)

    event = {
        "ts": datetime.now().astimezone().isoformat(timespec="seconds"),
        "type": args.event_type,
        "summary": args.summary,
        "source": "append_event.py",
    }
    event.update(inferred)
    if args.artifact:
        event["artifacts"] = args.artifact
    if args.status:
        event["status"] = args.status
    meta = parse_meta(args.meta)
    if meta:
        event["meta"] = meta

    with event_file.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=True) + "\n")

    print(event_file)
    print(json.dumps(event, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
