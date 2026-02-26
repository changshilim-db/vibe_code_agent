#!/usr/bin/env python3
"""Create .agents from .claude skills and agents."""

from __future__ import annotations

import shutil
from pathlib import Path


def find_project_root(start: Path) -> Path:
    for candidate in (start, *start.parents):
        if (candidate / ".claude").is_dir():
            return candidate
    raise FileNotFoundError("Could not find project root containing .claude")


def copy_skills(skills_dir: Path, target_dir: Path) -> None:
    if not skills_dir.exists():
        return

    # Copy only the contents of `.claude/skills` into `.agents`.
    for src in skills_dir.iterdir():
        dest = target_dir / src.name
        if src.is_dir():
            shutil.copytree(src, dest, dirs_exist_ok=True)
        elif src.is_file():
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)


def copy_agents(agents_dir: Path, target_dir: Path) -> None:
    if not agents_dir.exists():
        return

    for src in agents_dir.iterdir():
        if not src.is_file():
            continue

        agent_name = src.stem
        agent_folder = target_dir / agent_name
        agent_folder.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, agent_folder / "SKILL.md")


def main() -> None:
    root = find_project_root(Path(__file__).resolve().parent)

    skills_dir = root / ".claude" / "skills"
    agents_dir = root / ".claude" / "agents"
    target_dir = root / ".agents"
    claude_md = root / "CLAUDE.md"
    agents_md = root / "AGENTS.md"

    target_dir.mkdir(parents=True, exist_ok=True)

    copy_skills(skills_dir, target_dir)
    copy_agents(agents_dir, target_dir)
    if claude_md.exists():
        shutil.copy2(claude_md, agents_md)

    print(f"Created/updated: {target_dir}")


if __name__ == "__main__":
    main()
