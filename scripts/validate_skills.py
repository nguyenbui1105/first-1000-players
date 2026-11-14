#!/usr/bin/env python3
"""Validate every skill in skills/ against the Agent Skills rules this repo follows.

Checks:
- SKILL.md exists and starts with YAML frontmatter containing name and description
- name: <= 64 chars, lowercase letters/digits/hyphens, matches folder, no reserved words
- description: non-empty, <= 1024 chars, no angle brackets
- SKILL.md body under 500 lines
- every reference file linked as `references/...` or `scripts/...` exists
- reference files over 100 lines contain a "Contents" section
- every skill listed in .claude-plugin/marketplace.json exists, and every skill folder is listed
- evals/<skill>.json exists with at least 3 cases
Exit code 1 if any error.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RESERVED = ("anthropic", "claude")


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    block = text[4:end]
    body = text[end + 4:].lstrip("\n")
    data = {}
    for line in block.splitlines():
        if ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            data[key.strip()] = value.strip().strip('"').strip("'")
    return data, body


def main() -> int:
    errors, warnings = [], []
    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())

    for d in skill_dirs:
        tag = f"[{d.name}]"
        skill_md = d / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{tag} missing SKILL.md")
            continue
        text = skill_md.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{tag} missing or malformed frontmatter")
            continue
        name = fm.get("name", "")
        desc = fm.get("description", "")
        if not name:
            errors.append(f"{tag} frontmatter has no name")
        else:
            if len(name) > 64:
                errors.append(f"{tag} name longer than 64 chars")
            if not NAME_RE.match(name):
                errors.append(f"{tag} name must be lowercase letters, digits, hyphens")
            if name != d.name:
                errors.append(f"{tag} name '{name}' does not match folder")
            if any(r in name for r in RESERVED):
                errors.append(f"{tag} name contains a reserved word")
        if not desc:
            errors.append(f"{tag} frontmatter has no description")
        else:
            if len(desc) > 1024:
                errors.append(f"{tag} description is {len(desc)} chars (max 1024)")
            if "<" in desc or ">" in desc:
                errors.append(f"{tag} description contains angle brackets")
        lines = body.count("\n") + 1
        if lines >= 500:
            errors.append(f"{tag} SKILL.md body is {lines} lines (keep under 500)")

        for ref in sorted(set(re.findall(r"`((?:references|scripts)/[^`\s]+)`", body))):
            if not (d / ref).exists():
                errors.append(f"{tag} links {ref} but it does not exist")

        for ref_file in (d / "references").glob("*.md") if (d / "references").is_dir() else []:
            ref_text = ref_file.read_text(encoding="utf-8")
            if ref_text.count("\n") > 100 and "contents" not in ref_text.lower():
                warnings.append(f"{tag} {ref_file.name} is over 100 lines without a Contents section")

        eval_file = ROOT / "evals" / f"{d.name}.json"
        if not eval_file.is_file():
            errors.append(f"{tag} missing evals/{d.name}.json")
        else:
            try:
                cases = json.loads(eval_file.read_text(encoding="utf-8")).get("cases", [])
                if len(cases) < 3:
                    errors.append(f"{tag} evals/{d.name}.json has {len(cases)} cases (need 3+)")
            except json.JSONDecodeError as exc:
                errors.append(f"{tag} evals/{d.name}.json is not valid JSON: {exc}")

    manifest = ROOT / ".claude-plugin" / "marketplace.json"
    if manifest.is_file():
        data = json.loads(manifest.read_text(encoding="utf-8"))
        listed = set()
        for plugin in data.get("plugins", []):
            for s in plugin.get("skills", []):
                listed.add(pathlib.PurePosixPath(s).name)
                if not (ROOT / s).is_dir():
                    errors.append(f"[manifest] lists {s} but folder is missing")
        for d in skill_dirs:
            if d.name not in listed:
                errors.append(f"[manifest] skill {d.name} is not listed in marketplace.json")
    else:
        errors.append("[manifest] .claude-plugin/marketplace.json not found")

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error:   {e}")
    print(f"\n{len(skill_dirs)} skills checked, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
