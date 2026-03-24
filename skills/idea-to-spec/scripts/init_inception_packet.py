#!/usr/bin/env python3
"""Create an inception packet for an early-stage project idea."""

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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize an inception packet for a rough project idea.",
    )
    parser.add_argument("slug", help="Short packet identifier")
    parser.add_argument("idea", help="One-sentence summary of the idea")
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root that should contain .codex-agent/inception/",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.root).resolve()
    script_dir = Path(__file__).resolve().parent
    template_dir = script_dir.parent / "assets" / "inception-template"
    packet_id = f"{date.today():%Y%m%d}-{normalize_slug(args.slug)}"
    packet_dir = repo_root / ".codex-agent" / "inception" / packet_id

    if packet_dir.exists():
        print(f"[ERROR] Inception packet already exists: {packet_dir}", file=sys.stderr)
        return 1

    packet_dir.mkdir(parents=True, exist_ok=False)

    replacements = {
        "__PACKET_ID__": packet_id,
        "__DATE__": str(date.today()),
        "__REPO_ROOT__": str(repo_root),
        "__IDEA__": args.idea.strip(),
    }

    for template_path in sorted(template_dir.glob("*.md")):
        content = template_path.read_text(encoding="utf-8")
        for placeholder, value in replacements.items():
            content = content.replace(placeholder, value)
        (packet_dir / template_path.name).write_text(content, encoding="utf-8")

    print(packet_dir)
    print("")
    print("Next:")
    print(f"  1. Rewrite the idea in {packet_dir / 'IDEA.md'}")
    print(f"  2. Capture ambiguities in {packet_dir / 'QUESTIONS.md'}")
    print(f"  3. Convert the idea into a scoped phase-1 spec in {packet_dir / 'SPEC.md'}")
    print(f"  4. Write the first delivery plan in {packet_dir / 'PLAN.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
