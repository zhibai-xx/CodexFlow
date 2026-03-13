#!/usr/bin/env python3
"""Launch a detached long-running command with persistent logs."""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def normalize_label(raw: str) -> str:
    label = re.sub(r"[^a-z0-9]+", "-", raw.strip().lower())
    label = re.sub(r"-{2,}", "-", label).strip("-")
    return label or "run"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Launch a long-running command for an agent task.",
    )
    parser.add_argument("task_dir", help="Task directory created by init_agent_task.py")
    parser.add_argument("label", help="Short label for this run")
    parser.add_argument(
        "command",
        nargs=argparse.REMAINDER,
        help="Command to run after --",
    )
    return parser.parse_args()


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def append_run_log(task_dir: Path, created_at: str, label: str, status: str, command: list[str], run_dir: Path) -> None:
    runs_md = task_dir / "RUNS.md"
    line = (
        f"- `{created_at}` | `{label}` | status=`{status}` | "
        f"command=`{shlex.join(command)}` | run_dir=`{run_dir}`\n"
    )
    if runs_md.exists():
        with runs_md.open("a", encoding="utf-8") as handle:
            handle.write(line)


def launch(task_dir: Path, label: str, command: list[str]) -> int:
    if command and command[0] == "--":
        command = command[1:]
    if not command:
        print("[ERROR] Missing command. Use -- <command ...>", file=sys.stderr)
        return 1

    run_id = f"{timestamp()}-{normalize_label(label)}"
    run_dir = task_dir / "runs" / run_id
    run_dir.mkdir(parents=True, exist_ok=False)

    meta = {
        "label": label,
        "created_at": now_iso(),
        "task_dir": str(task_dir),
        "run_dir": str(run_dir),
        "status": "queued",
        "command": command,
    }
    write_json(run_dir / "meta.json", meta)
    (run_dir / "command.txt").write_text(" ".join(command) + "\n", encoding="utf-8")
    append_run_log(task_dir, meta["created_at"], label, "queued", command, run_dir)

    worker_cmd = [
        sys.executable,
        str(Path(__file__).resolve()),
        "--worker-run-dir",
        run_dir.as_posix(),
        "--",
        *command,
    ]
    worker = subprocess.Popen(
        worker_cmd,
        cwd=task_dir,
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )

    meta["worker_pid"] = worker.pid
    meta["status"] = "starting"
    write_json(run_dir / "meta.json", meta)
    append_run_log(task_dir, now_iso(), label, "starting", command, run_dir)

    print(run_dir)
    print("")
    print("Inspect with:")
    print(f"  python3 {Path(__file__).resolve().parent / 'inspect_long_run.py'} {run_dir}")
    return 0


def run_worker(run_dir: Path, command: list[str]) -> int:
    if command and command[0] == "--":
        command = command[1:]
    if not command:
        print("[ERROR] Missing command for worker.", file=sys.stderr)
        return 1
    meta_path = run_dir / "meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    task_dir = Path(meta["task_dir"])
    label = meta["label"]
    meta["status"] = "running"
    meta["started_at"] = now_iso()
    meta["runner_pid"] = os.getpid()
    write_json(meta_path, meta)
    append_run_log(task_dir, meta["started_at"], label, "running", command, run_dir)

    stdout_path = run_dir / "stdout.log"
    stderr_path = run_dir / "stderr.log"
    with stdout_path.open("wb") as stdout_handle, stderr_path.open("wb") as stderr_handle:
        completed = subprocess.run(command, cwd=task_dir, stdout=stdout_handle, stderr=stderr_handle)

    meta["finished_at"] = now_iso()
    meta["exit_code"] = completed.returncode
    meta["status"] = "completed" if completed.returncode == 0 else "failed"
    write_json(meta_path, meta)
    append_run_log(task_dir, meta["finished_at"], label, meta["status"], command, run_dir)
    return completed.returncode


def main() -> int:
    if len(sys.argv) >= 3 and sys.argv[1] == "--worker-run-dir":
        run_dir = Path(sys.argv[2]).resolve()
        command = sys.argv[3:]
        if command and command[0] == "--":
            command = command[1:]
        return run_worker(run_dir, command)

    args = parse_args()
    task_dir = Path(args.task_dir).resolve()
    return launch(task_dir, args.label, args.command)


if __name__ == "__main__":
    raise SystemExit(main())
