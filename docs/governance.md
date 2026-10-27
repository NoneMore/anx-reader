# Project governance

This is the shared governance policy for `NoneMore/anx-reader`. It applies to PRs targeting `main`. Changes made before adoption do not require retroactive Specs or ADRs.

## Principles and documentation

- **Code first:** Tracked code and relevant build/runtime evidence establish current behavior. Active Specs describe intended changes; archived Specs record historical outcomes, not necessarily current or deployed behavior.
- **Development:** [`DEVELOPMENT.md`](DEVELOPMENT.md) covers setup, builds, and tests.
- **Architecture and decisions:** Document important implemented boundaries in `docs/architecture/` and consequential architectural decisions in `docs/adr/` when useful. Record superseding decisions in new ADRs rather than rewriting old ones.
- **Documentation updates:** Update development guidance and architecture docs when related workflows or implemented boundaries change; unrelated edits need no documentation updates.
- **Comments:** Preserve non-obvious invariants, constraints, and rationale near the relevant code; do not restate obvious behavior.
- **Navigation:** Consult only material relevant to the task. `AGENTS.md` directs agents to this policy rather than defining separate governance rules.

## PR-scoped Change lifecycle

Every PR targeting `main` follows the same lifecycle. A Change belongs to one PR; a PR may include several Changes. A Change represents a cohesive intent, not a list of tasks; keep Specs proportional to the size and complexity of the work.

1. **Activate first:** Introduce a new `specs/active/<change>/spec.md` before changing files outside `specs/`. All participating Changes must be active before the first implementation commit. A Spec activation commit must not also modify non-`specs/` files.
2. **Implement:** Keep intent and scope current during implementation and review. Add optional `design.md` or `tasks.md` only when useful; track volatile progress and ownership in PRs or issues.
3. **Archive before merge:** Move each Change directory to `specs/archive/<change>/` and record actual outcomes, verification, and unresolved work, including partial or cancelled results. If implementation changes after archival, update the outcome and verification. The prospective merge tree must contain no tracked files under `specs/active/`.

If a PR closes without merging, record the reason in the PR; no archive is required.

Change names must be unique lowercase `kebab-case` (up to 80 characters); do not reuse names already active or archived on the target branch. Do not alter historical archives or reactivate completed Changes.

Required `spec.md` sections (case-insensitive Markdown `##` headings):

- **Active:** `Intent` (goal and motivation), `Scope` (included/excluded work), `Acceptance Criteria` (observable checks).
- **Archive adds:** `Outcome` (actual result), `Verification` (evidence and limitations), `Unresolved` (remaining risks or `None`).

## Review and enforcement

- `.github/workflows/pr-spec.yaml` checks the structural lifecycle and prospective merge tree using `scripts/governance/check_pr_spec.py`. `.github/workflows/ci.yaml` runs Flutter analysis and tests. CI cannot judge intent or prove deployed behavior.
- Human review evaluates change scope, implementation, verification, and relevant risks.
- Configure `main` branch protection to require `pr-spec / validate` and Flutter CI (`analyze-and-test`) checks. Until then, CI results are advisory rather than enforced merge gates.
- Before final validation, rebase or merge the latest `main` into the PR branch.
- Do not push directly to `main` except for urgent recovery when the normal PR process is unavailable. Record the reason, affected SHA, scope, and validation; restore protections and document follow-up work in a compliant PR. Do not fabricate retroactive Specs.
