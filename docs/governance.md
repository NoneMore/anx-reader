# Project governance (personal fork)

This document is the canonical, human-facing governance policy for `NoneMore/anx-reader`. The repository is a personal fork of `Anxcye/anx-reader`, not the upstream project's official release or support channel. This policy governs changes to the fork's `main` integration branch; it does not reinstate upstream community-management or automated publishing workflows.

## Authority and navigation

- **Code first:** tracked implementation plus relevant runtime/build evidence describe *current* behavior. Tests help verify behavior; neither comments nor documents can overrule implementation evidence. A change specification describes intended *future* behavior, not what is deployed.
- **Development:** [`DEVELOPMENT.md`](DEVELOPMENT.md) is the practical setup, build, and test guide. Keep workflow instructions there rather than duplicating command details here.
- **Architecture:** `docs/architecture/` describes current component boundaries and important code locations. Update it when implemented work materially changes those boundaries. Avoid a permanent catalog of low-level features.
- **Comments:** preserve non-obvious local invariants, rationale, or interface assumptions close to the relevant implementation, but do not narrate obvious code.
- **ADR:** `docs/adr/` captures consequential architectural *decisions and rationale*, not every bug fix. A new ADR names older decisions it supersedes (fully or partly); do not rewrite older ADRs to point forward. Old decisions may be moved to `docs/adr/archive/`.
- **Change:** `specs/` stores change-scoped intent and historical outcomes. Archived specifications are **not** authoritative documentation of current system behavior. PR discussions, tests, Git and deployment evidence remain distinct.
- **Agents:** `AGENTS.md` is only an adapter pointing to this human-facing policy. It must not become a second, conflicting source of shared governance rules.

Read only the material relevant to a task: development guidance for setup; architecture for system navigation; code for actual implementation; an active Change for intended work; ADRs when the reason for an old decision matters.

## Strict PR-scoped Change contract

Every PR targeting `main`, including documentation, CI, dependency updates, automated PRs, and upstream synchronization, must:

1. Introduce at least one **new** `specs/active/<change>/spec.md` with substantive `Intent`, `Scope`, and `Acceptance Criteria` sections. Names are unique lowercase `kebab-case` (maximum 80 characters) and may not reuse an already active or archived name from the target branch.
2. Commit an active Spec **before any implementation files** are modified in that PR. Put all participating Changes in active state before the first implementation commit, preferably as standalone Spec commits. A Spec activation commit must not simultaneously modify non-`specs/` files.
3. Keep the intended outcome and scope current throughout implementation and review. `design.md` and `tasks.md` are optional; use issue/PR tracking for volatile ownership and status rather than duplicating it.
4. Before merge, move each participating Change directory to `specs/archive/<change>/`, retaining its name. Record substantive `Outcome`, `Verification`, and `Unresolved` sections, including partial, cancelled, or superseded outcomes and untested platforms. If implementation changes after archival, refresh the outcome record and recheck relevant evidence.
5. Leave **no tracked files** under `specs/active/` in the prospective merge result. Do not silently alter historical archives, re-activate completed Changes, or regard archive placement as proof of deployment.

One Change belongs to one PR; a PR may contain several Changes. A planned proposal may live under `specs/planned/<change>/` and then be moved into `active/` in its implementing PR. Because every PR requires an active-and-archived Change, proposed-only PRs have additional ceremony; prefer not to add long-lived planned files until useful. A PR closed without merging documents cancellation in its PR discussion; no merged archive is required.

Suggested `spec.md` sections (Markdown `##` headers, case-insensitive for CI):

- `Intent`: intended result and motivation.
- `Scope`: included/excluded behavior and limits.
- `Acceptance Criteria`: observable checks.
- `Outcome` (archive): what actually happened, including partial/cancelled work.
- `Verification` (archive): tests, references and limitations.
- `Unresolved` (archive): remaining risks or explicitly `None`.

The archive retains the entire Change directory and history. Fine-grained work state belongs in PRs or the active tracker.

## Review and CI enforcement

- `.github/workflows/pr-spec.yaml` checks Git history and the prospective merge tree using `scripts/governance/check_pr_spec.py`. CI verifies structure and required sections, **not** whether tests passed, intent was useful, or acceptance criteria were actually met.
- `.github/workflows/ci.yaml` runs Flutter analysis and tests. Its current analyzer flags `--no-fatal-infos --no-fatal-warnings`; successful checks do not imply a warning-free tree.
- Human review examines change scope, architecture impacts, user-data safety, upstream conflict preservation, tests, and release implications. Do not trust a checkbox or archive folder as evidence of correctness.
- PR check runs are advisory until the repository administrator configures and verifies `main` branch protection with required `pr-spec / validate` and Flutter CI checks. A `pull_request` workflow alone does not prevent merging or direct pushes. Do not claim enforcement before checking actual settings.
- The initial governance-bootstrap PR is **transitional**: because the validator is not yet on `main`, its workflow checks the proposed validator from the PR and must receive manual review. After that PR merges, checks should use the version from the PR's base commit.
- For check reliability, PR branches must contain the target base tip (rebase or merge the latest `main` before final validation). A PR's final merge result must pass the lifecycle check.

## Exceptions and direct pushes

There are **no PR-level path, author, label, bot, docs-only, or `[skip-spec]` exemptions**. Small changes can use a short, meaningful Spec; automated dependency PRs must follow Spec-first or be reconstructed before merge. Draft PRs may fail during work, but must pass before merge. Work on personal branches and a separately designated upstream mirror branch is not PR-scoped until targeting `main`.

Normal direct pushes to `main` are prohibited by policy, even if GitHub permissions currently permit them. An exceptional **break-glass** repair is permitted only when normal PR governance/build infrastructure is inoperable and urgent recovery is needed. Record the reason, scope, affected SHA and validation evidence; make the smallest change, restore branch protection immediately, and create a subsequent compliant PR to document the incident and follow-ups. Do **not** backdate or fabricate a pre-implementation Spec; document the bypass honestly. When branch protection can be used, enable enforcement for administrators too while retaining documented emergency recovery access.

## Upstream and fork-specific changes

- `main` is the fork's integration branch. Follow `Anxcye/anx-reader` (normally `upstream/develop`) as the upstream source; document the purpose of the existing `develop` branch separately before changing or deleting it.
- Sync upstream through a dedicated `sync/*` PR with a new Change that records upstream source SHA, original fork base SHA, conflicts, retained fork patches, regression tests and final outcome. Upstream Git merge commits do not exempt the PR from Change activation.
- **Never reintroduce removed upstream community triage, store-signing, auto-release or publishing automation merely because upstream introduced them.** Any intentional policy reversal requires its own reviewed Change.
- Preserve custom `third_party/` overrides and relevant reading, data-migration, database/sync, AI and platform-specific changes unless the Change explicitly justifies replacing them.
- Check license notices and third-party obligations before distributing fork builds; the fork is not an official upstream distribution channel.

## Adopting and evolving this policy

Existing commits and historical changes before adoption are not retroactively required to have Specs or ADRs. After bootstrap, change this policy, CI, or its validator only through a compliant PR and test the validator on passing/failing synthetic Git histories. Build and architecture documents should evolve when the *related* workflows or implemented boundaries change, not whenever any code is edited.
