# Establish strict PR-scoped governance for the personal fork

## Intent

Introduce a human-first code-governance entry point, strict Spec-first and archive-before-merge Change lifecycle, and reproducible structural PR checks for `NoneMore/anx-reader` without restoring upstream community/release automation.

## Scope

Includes human-readable governance rules, lightweight Agent navigation, PR template, PR lifecycle validator and synthetic history tests, CI PR trigger, and README governance links. Excludes branch-protection changes, merging this PR, automatic releases, refactoring application code, full architecture mapping, and retroactive Specs for historical commits.

## Acceptance Criteria

- A reviewer can reach canonical governance from both English and Chinese READMEs.
- A new Active Change Spec is committed before implementation changes and archived before merge.
- Lifecycle checker rejects Spec-less, late-Spec, missing-archive, reused-name, modified-historical-archive and leftover-active cases.
- Synthetic Git-history tests pass and PR workflow invokes validator against base/head/prospective merge revisions.
- PR-triggered Flutter CI is enabled without reintroducing publishing/signing credentials.
- Bootstrap limitation and subsequent branch-protection configuration are explicitly documented.

## Outcome

Governance policy, Agent pointer, PR template, Python Git-history checker, its synthetic tests, and PR workflow were added. The bootstrap Change was activated before the implementation and moved into archive before requesting merge. No application code, branch-protection settings, or release automation were changed. Enforcement remains advisory until the administrator enables required branch checks after bootstrap merge. The governance guide, Agent entry point, and routine PR template were subsequently simplified, removing upstream/fork-specific standing requirements without changing the Spec lifecycle or validator.

## Verification

Locally executed `python3 -m unittest discover -s test/governance -v` with 13 passing synthetic Git-history tests prior to publishing. GitHub PR checks must be reviewed for the final submitted commit; Flutter analyze/tests were not run in this documentation/CI-authoring environment. Branch-protection and post-bootstrap trusted-base validator behavior require manual verification following merge.

## Unresolved

Before mandatory enforcement, confirm GitHub Actions behavior for the bootstrap and a negative-control PR, ensure main branch protection requires both PR-Spec and Flutter checks, and decide the future role of the pre-existing `develop` branch. No release or app-platform build verification was performed as part of this governance change.
