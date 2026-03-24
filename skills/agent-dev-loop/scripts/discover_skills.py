#!/usr/bin/env python3
"""Discover and rank available skills from the repo and Codex home."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

import yaml

STOPWORDS = {
    "a",
    "an",
    "and",
    "as",
    "at",
    "by",
    "for",
    "from",
    "how",
    "i",
    "in",
    "into",
    "of",
    "on",
    "or",
    "the",
    "to",
    "update",
    "use",
    "with",
}


@dataclass
class Skill:
    name: str
    description: str
    path: Path
    source: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="List and rank available skills.",
    )
    parser.add_argument(
        "query",
        nargs="?",
        default="",
        help="Optional task or domain query used for ranking",
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root whose local skills should be scanned",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Maximum number of ranked results to print",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable JSON-like output",
    )
    return parser.parse_args()


def tokenize(text: str) -> list[str]:
    return [
        token
        for token in re.findall(r"[a-z0-9]+", text.lower())
        if len(token) > 1 and token not in STOPWORDS
    ]


def load_skill(skill_md: Path, source: str) -> Skill | None:
    content = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    frontmatter = yaml.safe_load(match.group(1))
    if not isinstance(frontmatter, dict):
        return None
    name = str(frontmatter.get("name", "")).strip()
    description = str(frontmatter.get("description", "")).strip()
    if not name or not description:
        return None
    return Skill(name=name, description=description, path=skill_md.resolve(), source=source)


def scan_skills(repo_root: Path) -> list[Skill]:
    roots = [
        ("repo-local", repo_root / "skills"),
        ("codex-home", Path.home() / ".codex" / "skills"),
    ]
    found: dict[Path, Skill] = {}
    for source, root in roots:
        if not root.exists():
            continue
        for skill_md in sorted(root.rglob("SKILL.md")):
            skill = load_skill(skill_md, source)
            if skill:
                found[skill.path] = skill
    return sorted(found.values(), key=lambda skill: (skill.source, skill.name))


def score_skill(skill: Skill, query: str) -> tuple[int, list[str]]:
    query_tokens = tokenize(query)
    if not query_tokens:
        return 0, []
    name_tokens = set(tokenize(skill.name.replace("-", " ")))
    desc_tokens = tokenize(skill.description)

    score = 0
    matched: list[str] = []
    for token in query_tokens:
        token_score = 0
        if token in name_tokens:
            token_score += 5
        desc_hits = desc_tokens.count(token)
        if desc_hits:
            token_score += min(desc_hits, 3) * 2
        if token_score:
            score += token_score
            matched.append(token)
    if query.lower() in skill.description.lower():
        score += 3
    if skill.source == "repo-local":
        score += 1
    return score, matched


def print_text(skills: list[Skill], query: str, limit: int) -> None:
    if query:
        ranked = []
        for skill in skills:
            score, matched = score_skill(skill, query)
            if score > 0:
                ranked.append((score, matched, skill))
        ranked.sort(key=lambda item: (-item[0], item[2].source, item[2].name))
        if not ranked:
            print(f'No skill matched query: "{query}"')
            return
        print(f'Ranked skills for: "{query}"')
        for index, (score, matched, skill) in enumerate(ranked[:limit], start=1):
            reason = ", ".join(dict.fromkeys(matched)) or "broad description match"
            print(f"{index}. {skill.name} [{skill.source}] score={score}")
            print(f"   path: {skill.path}")
            print(f"   why: matched {reason}")
            print(f"   desc: {skill.description}")
    else:
        print("Available skills:")
        for skill in skills:
            print(f"- {skill.name} [{skill.source}]")
            print(f"  path: {skill.path}")
            print(f"  desc: {skill.description}")


def print_json(skills: list[Skill], query: str, limit: int) -> None:
    import json

    payload = []
    for skill in skills:
        score, matched = score_skill(skill, query)
        payload.append(
            {
                "name": skill.name,
                "source": skill.source,
                "path": str(skill.path),
                "description": skill.description,
                "score": score,
                "matched_terms": matched,
            }
        )
    if query:
        payload.sort(key=lambda item: (-item["score"], item["source"], item["name"]))
    else:
        payload.sort(key=lambda item: (item["source"], item["name"]))
    print(json.dumps(payload[:limit], indent=2, ensure_ascii=False))


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    skills = scan_skills(repo_root)
    if args.json:
        print_json(skills, args.query, args.limit)
    else:
        print_text(skills, args.query, args.limit)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
