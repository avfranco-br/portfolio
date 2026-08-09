# Quickstart Validation Guide: Tech Blog Approval Status Filter

This guide provides runnable scenarios to verify that only articles with `status: approved` are published.

## Scenario 1: Verify Approved Posts Are Published

1. Check that all published articles under `docs/tech-blog/` have `status: approved` in YAML frontmatter.
2. Run governance check:
   ```bash
   bash scripts/run_governance.sh
   ```
3. Expected Outcome: Build succeeds with 0 warnings, and approved articles appear in `mkdocs.yml` navigation.

## Scenario 2: Verify Draft Posts Are Excluded

1. Create a temporary draft post `docs/tech-blog/test-draft.md` with `status: draft`.
2. Run governance check:
   ```bash
   bash scripts/run_governance.sh
   ```
3. Expected Outcome: `test-draft.md` is omitted from public navigation and index listings, and build passes cleanly.
4. Clean up `docs/tech-blog/test-draft.md`.
