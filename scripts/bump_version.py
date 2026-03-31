#!/usr/bin/env python3
"""Bump the version of a skill in SKILL.md frontmatter and catalog.json."""

import json
import os
import re
import sys


def bump_semver(version: str, part: str) -> str:
    """Bump a semver string by the given part."""
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)$", version)
    if not match:
        raise ValueError(f"Invalid semver: {version}")

    major, minor, patch = int(match.group(1)), int(match.group(2)), int(match.group(3))

    if part == "major":
        return f"{major + 1}.0.0"
    elif part == "minor":
        return f"{major}.{minor + 1}.0"
    elif part == "patch":
        return f"{major}.{minor}.{patch + 1}"
    else:
        raise ValueError(f"Invalid bump part: {part} (use major, minor, or patch)")


def get_current_version(skill_md_path: str) -> str:
    """Extract the current version from SKILL.md frontmatter."""
    with open(skill_md_path, "r") as f:
        content = f.read()

    match = re.search(r"^version:\s*(.+)$", content, re.MULTILINE)
    if not match:
        raise ValueError("Could not find 'version:' in SKILL.md frontmatter")
    return match.group(1).strip()


def update_skill_md(skill_md_path: str, old_version: str, new_version: str):
    """Update the version in SKILL.md frontmatter."""
    with open(skill_md_path, "r") as f:
        content = f.read()

    content = re.sub(
        r"^(version:\s*)" + re.escape(old_version),
        rf"\g<1>{new_version}",
        content,
        count=1,
        flags=re.MULTILINE,
    )

    with open(skill_md_path, "w") as f:
        f.write(content)


def update_catalog(catalog_path: str, skill_name: str, new_version: str):
    """Update the version for a skill in catalog.json."""
    if not os.path.isfile(catalog_path):
        print(f"Warning: {catalog_path} not found, skipping catalog update")
        return

    with open(catalog_path, "r") as f:
        catalog = json.load(f)

    for skill in catalog.get("skills", []):
        if skill["name"] == skill_name:
            skill["version"] = new_version
            break
    else:
        print(f"Warning: skill '{skill_name}' not found in catalog.json")
        return

    with open(catalog_path, "w") as f:
        json.dump(catalog, f, indent=2)
        f.write("\n")


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <skill-directory> <major|minor|patch>")
        sys.exit(1)

    skill_dir = sys.argv[1]
    bump_part = sys.argv[2]

    skill_name = os.path.basename(os.path.normpath(skill_dir))
    skill_md = os.path.join(skill_dir, "SKILL.md")

    if not os.path.isfile(skill_md):
        print(f"Error: SKILL.md not found in '{skill_dir}'")
        sys.exit(1)

    old_version = get_current_version(skill_md)
    new_version = bump_semver(old_version, bump_part)

    print(f"{skill_name}: {old_version} -> {new_version}")

    update_skill_md(skill_md, old_version, new_version)

    # Find catalog.json relative to the skill directory
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(skill_dir)))
    catalog_path = os.path.join(repo_root, "catalog.json")
    update_catalog(catalog_path, skill_name, new_version)

    print("Done. Remember to commit and tag:")
    print(f"  git add {skill_md} catalog.json")
    print(f"  git commit -m '{skill_name}: bump to {new_version}'")
    print(f"  git tag {skill_name}@{new_version}")


if __name__ == "__main__":
    main()
