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
