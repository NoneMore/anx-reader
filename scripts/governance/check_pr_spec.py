#!/usr/bin/env python3
"""Validate the fork's strict PR-scoped change lifecycle using Git history.

This checks structural evidence only, not semantic correctness or test quality.
Usage: check_pr_spec.py --base SHA --head SHA --merge SHA
"""

import argparse
import re
import subprocess
import sys

CHANGE_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SPEC_PATH = re.compile(r"^specs/(planned|active|archive)/([^/]+)/spec\.md$")
CHANGE_PATH = re.compile(r"^specs/(planned|active|archive)/([^/]+)(?:/|$)")
BASE_SECTIONS = ("Intent", "Scope", "Acceptance Criteria")
ARCHIVED_SECTIONS = BASE_SECTIONS + ("Outcome", "Verification", "Unresolved")


class ValidationError(Exception):
    pass


def git(*args, binary=False):
    proc = subprocess.run(
        ["git", *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False
    )
    if proc.returncode:
        raise ValidationError(f"git {' '.join(args)} failed: {proc.stderr.decode(errors='replace').strip()}")
    return proc.stdout if binary else proc.stdout.decode("utf-8", errors="replace").strip()


def files_at(revision):
    return set(git("ls-tree", "-rz", "--name-only", revision, binary=True).decode("utf-8").split("\0")) - {""}


def file_at(revision, path):
    return git("show", f"{revision}:{path}")


def changed_files(old, new):
    raw = git("diff", "--name-only", "-z", old, new, binary=True)
    return set(raw.decode("utf-8").split("\0")) - {""}


def change_names(paths, state):
    return {m.group(2) for path in paths if (m := CHANGE_PATH.match(path)) and m.group(1) == state}


def validate_spec(revision, path, sections):
    text = file_at(revision, path)
    if not text.strip():
        raise ValidationError(f"G03: empty spec: {path} at {revision[:12]}")
    blocks = re.split(r"(?m)^##\s+", text)
    section_map = {}
    for block in blocks[1:]:
        heading, _, body = block.partition("\n")
        section_map[heading.strip().lower()] = body.strip()
    for section in sections:
        content = section_map.get(section.lower(), "")
        if not content or content.lower() in {"todo", "tbd", "pending", "待补充", "待归档时填写"}:
            raise ValidationError(f"G03/G07: missing substantive '{section}' in {path} at {revision[:12]}")


def validate(base, head, merge):
    git("rev-parse", "--verify", f"{base}^{{commit}}")
    git("rev-parse", "--verify", f"{head}^{{commit}}")
    git("rev-parse", "--verify", f"{merge}^{{commit}}")
    ancestor = subprocess.run(["git", "merge-base", "--is-ancestor", base, head], check=False)
    if ancestor.returncode:
        raise ValidationError("G00: PR head is not based on the current base SHA; update the branch")

    base_files = files_at(base)
    merge_files = files_at(merge)
    existing = change_names(base_files, "active") | change_names(base_files, "archive")
    commits = git("rev-list", "--first-parent", "--reverse", f"{base}..{head}").splitlines()
    activated = set()
    first_implementation = None
    activation_commits = {}

    for commit in commits:
        parents = git("rev-list", "--parents", "-n", "1", commit).split()
        if len(parents) < 2:
            raise ValidationError(f"G00: commit without parent in PR chain: {commit}")
        previous = parents[1]
        before = files_at(previous)
        after = files_at(commit)
        delta = changed_files(previous, commit)
        just_activated = set()
        for path in after - before:
            match = SPEC_PATH.match(path)
            if not match or match.group(1) != "active":
                continue
            name = match.group(2)
            if not CHANGE_NAME.fullmatch(name) or len(name) > 80:
                raise ValidationError(f"G03: invalid change name: {name}")
            if name in existing:
                raise ValidationError(f"G02: change name already used on base: {name}")
            if name in activated:
                raise ValidationError(f"G02: duplicate activation in PR: {name}")
            validate_spec(commit, path, BASE_SECTIONS)
            just_activated.add(name)
            activation_commits[name] = commit
        activated.update(just_activated)

        implementation = {p for p in delta if not p.startswith("specs/")}
        if implementation and first_implementation is None:
            first_implementation = commit
        if implementation and just_activated:
            raise ValidationError(f"G04: activation and implementation in same commit {commit[:12]}")

    if not activated:
        raise ValidationError("G01: PR history does not introduce a new specs/active/<change>/spec.md")
    if first_implementation:
        first_index = commits.index(first_implementation)
        for name, sha in activation_commits.items():
            if commits.index(sha) > first_index:
                raise ValidationError(f"G04: {name} was activated after implementation started")

    for name in activated:
        archive_path = f"specs/archive/{name}/spec.md"
        if archive_path not in merge_files:
            raise ValidationError(f"G05: archive missing for {name}")
        validate_spec(merge, archive_path, ARCHIVED_SECTIONS)

    active_leftovers = sorted(p for p in merge_files if p.startswith("specs/active/"))
    if active_leftovers:
        raise ValidationError(f"G06: tracked active files remain in merge tree: {active_leftovers[:5]}")

    new_archive_names = change_names(merge_files - base_files, "archive")
    if not new_archive_names <= activated:
        raise ValidationError(f"G08: archived without activation: {sorted(new_archive_names - activated)}")
    old_archives = change_names(base_files, "archive")
    for path in changed_files(base, merge):
        match = CHANGE_PATH.match(path)
        if match and match.group(1) == "archive" and match.group(2) in old_archives:
            raise ValidationError(f"G08: existing archive is immutable: {path}")

    return sorted(activated)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    parser.add_argument("--merge", required=True)
    args = parser.parse_args()
    try:
        names = validate(args.base, args.head, args.merge)
    except ValidationError as exc:
        print(f"PR-Spec validation FAILED: {exc}", file=sys.stderr)
        return 1
    print("PR-Spec validation PASSED: " + ", ".join(names))
    return 0


if __name__ == "__main__":
    sys.exit(main())
