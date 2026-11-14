#!/usr/bin/env python3
"""Validate the skills, manifest, evals and docs of this repo.

Checks:
- SKILL.md has YAML frontmatter with name and description (parsed with PyYAML
  when installed, otherwise a fallback parser that handles quoted and
  multi-line values)
- name: <= 64 chars, lowercase letters/digits/hyphens, matches folder, no reserved words
- description: non-empty, <= 1024 chars, no angle brackets
- SKILL.md body under 500 lines
- every `references/...` or `scripts/...` path mentioned in SKILL.md exists
- reference files over 100 lines contain a "Contents" section (warning)
- .claude-plugin/marketplace.json lists exactly the skill folders
- evals/<skill>.json exists with at least 3 cases
- local links and #anchors in README.md, README.vi.md and CONTRIBUTING.md resolve
Exit code 1 if any error.
"""
import json
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DOCS = ["README.md", "README.vi.md", "CONTRIBUTING.md"]
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RESERVED = ("anthropic", "claude")

try:
    import yaml  # type: ignore
except ImportError:  # fallback keeps the script dependency-free
    yaml = None


def _fallback_yaml(block: str) -> dict:
    data, key, buf, mode = {}, None, [], None

    def flush():
        if key is not None:
            joiner = "\n" if mode == "|" else " "
            data[key] = joiner.join(x.strip() for x in buf).strip()

    for line in block.splitlines():
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m and not line.startswith((" ", "\t")):
            flush()
            key, value = m.group(1), m.group(2).strip()
            buf, mode = [], None
            if value in ("|", ">", "|-", ">-"):
                mode = value[0]
            elif len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                buf = [value[1:-1]]
            elif value:
                buf = [value]
        elif key is not None:
            buf.append(line)
    flush()
    return data


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    block = text[4:end]
    body = text[end + 4:].lstrip("\n")
    if yaml is not None:
        try:
            data = yaml.safe_load(block) or {}
        except yaml.YAMLError as exc:
            raise ValueError(f"invalid YAML frontmatter: {exc}") from exc
        if not isinstance(data, dict):
            raise ValueError("frontmatter is not a mapping")
        return {k: ("" if v is None else str(v)) for k, v in data.items()}, body
    return _fallback_yaml(block), body


def github_slug(heading: str) -> str:
    """Approximate GitHub's heading anchor: lowercase, keep letters/marks/numbers/_/-/space."""
    out = []
    for ch in heading.strip().lower():
        cat = unicodedata.category(ch)
        if ch in " -" or cat[0] in "LMN" or cat == "Pc":
            out.append(ch)
    return "".join(out).replace(" ", "-")


def anchors_of(path: pathlib.Path) -> set:
    slugs, seen = set(), {}
    in_code = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", line)
        if m:
            slug = github_slug(re.sub(r"[`*_\[\]]|\(.*?\)", "", m.group(1)))
            n = seen.get(slug, 0)
            slugs.add(slug if n == 0 else f"{slug}-{n}")
            seen[slug] = n + 1
    return slugs


def check_doc_links(errors: list) -> None:
    link_re = re.compile(r"\]\(([^)\s]+)\)|(?:src|href)=\"([^\"]+)\"")
    for doc in DOCS:
        path = ROOT / doc
        if not path.is_file():
            continue
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        for m in link_re.finditer(text):
            target = m.group(1) or m.group(2)
            if re.match(r"^(https?:|mailto:)", target):
                continue
            file_part, _, anchor = target.partition("#")
            dest = path if not file_part else (path.parent / file_part)
            if not dest.exists():
                errors.append(f"[{doc}] broken link: {target}")
                continue
            if anchor and dest.suffix == ".md" and anchor not in anchors_of(dest):
                errors.append(f"[{doc}] anchor not found: {target}")


def main() -> int:
    errors, warnings = [], []
    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())

    for d in skill_dirs:
        tag = f"[{d.name}]"
        skill_md = d / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"{tag} missing SKILL.md")
            continue
        try:
            fm, body = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        except ValueError as exc:
            errors.append(f"{tag} {exc}")
            continue
        if fm is None:
            errors.append(f"{tag} missing or malformed frontmatter")
            continue
        name, desc = fm.get("name", ""), fm.get("description", "")
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
                errors.append(f"{tag} mentions {ref} but it does not exist")

        ref_dir = d / "references"
        for ref_file in sorted(ref_dir.glob("*.md")) if ref_dir.is_dir() else []:
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
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"[manifest] invalid JSON: {exc}")
            data = {}
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

    check_doc_links(errors)

    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error:   {e}")
    parser = "PyYAML" if yaml else "fallback parser"
    print(f"\n{len(skill_dirs)} skills checked ({parser}), {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
