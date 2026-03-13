#!/usr/bin/env python3
"""Inspect a detached long-running command and tail its logs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def tail_lines(path: Path, count: int) -> list[str]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    return lines[-count:]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect a long-running command launched by start_long_run.py",
    )
    parser.add_argument("run_dir", help="Run directory returned by start_long_run.py")
    parser.add_argument("--tail", type=int, default=20, help="Number of lines to tail from each log")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_dir = Path(args.run_dir).resolve()
    meta = json.loads((run_dir / "meta.json").read_text(encoding="utf-8"))

    print(f"Run: {run_dir}")
    print(f"Status: {meta.get('status', 'unknown')}")
    print(f"Command: {' '.join(meta.get('command', []))}")
    if "created_at" in meta:
        print(f"Created: {meta['created_at']}")
    if "started_at" in meta:
        print(f"Started: {meta['started_at']}")
    if "finished_at" in meta:
        print(f"Finished: {meta['finished_at']}")
    if "exit_code" in meta:
        print(f"Exit code: {meta['exit_code']}")

    stdout_tail = tail_lines(run_dir / "stdout.log", args.tail)
    stderr_tail = tail_lines(run_dir / "stderr.log", args.tail)

    print("")
    print("stdout tail:")
    if stdout_tail:
        for line in stdout_tail:
            print(line)
    else:
        print("(empty)")

    print("")
    print("stderr tail:")
    if stderr_tail:
        for line in stderr_tail:
            print(line)
    else:
        print("(empty)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
