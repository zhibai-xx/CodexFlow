#!/usr/bin/env python3
"""Create an evaluation packet for reviewing agent delivery quality."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path


def normalize_slug(raw: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", raw.strip().lower())
    slug = re.sub(r"-{2,}", "-", slug).strip("-")
    return slug or "eval"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize an evaluation packet for a Codex run.",
    )
    parser.add_argument("slug", help="Short evaluation identifier")
    parser.add_argument("scope", help="Task, milestone, or phase summary")
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root that should contain .codex-agent/evals/",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.root).resolve()
    script_dir = Path(__file__).resolve().parent
    template_dir = script_dir.parent / "assets" / "eval-template"
    packet_id = f"{date.today():%Y%m%d}-{normalize_slug(args.slug)}"
    packet_dir = repo_root / ".codex-agent" / "evals" / packet_id

    if packet_dir.exists():
        print(f"[ERROR] Evaluation packet already exists: {packet_dir}", file=sys.stderr)
        return 1

    packet_dir.mkdir(parents=True, exist_ok=False)

    replacements = {
        "__PACKET_ID__": packet_id,
        "__DATE__": str(date.today()),
        "__REPO_ROOT__": str(repo_root),
        "__SCOPE__": args.scope.strip(),
    }

    for template_path in sorted(template_dir.glob("*.md")):
        content = template_path.read_text(encoding="utf-8")
        for placeholder, value in replacements.items():
            content = content.replace(placeholder, value)
        (packet_dir / template_path.name).write_text(content, encoding="utf-8")

    print(packet_dir)
    print("")
    print("Next:")
    print(f"  1. Fill in {packet_dir / 'SUMMARY.md'}")
    print(f"  2. Score the run in {packet_dir / 'SCORES.md'}")
    print(f"  3. Record concrete failures in {packet_dir / 'FINDINGS.md'}")
    print(f"  4. Convert the review into changes in {packet_dir / 'ACTION_ITEMS.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
