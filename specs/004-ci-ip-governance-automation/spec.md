# Feature Specification: Automated CI/CD IP Assessment & Content Governance

**Feature Branch**: `feature/ci-ip-governance-automation`

**Created**: 2026-08-29

**Status**: In Progress

**Input**: User request: "Implement the IP-assessment and IP-generator (update a page with IP information - header + footer) as part of the CI/CD pipeline as Github Actions into a new branch."

## User Scenarios & Testing

### User Story 1 - Automated IP Classification & Copyright Validation in CI (Priority: P1)

As a repository owner and enterprise architect, I want every Markdown page in `docs/` automatically validated during CI pipeline runs (`scripts/validate_governance.py` and GitHub Actions), so that unclassified pages or missing copyright footers are immediately detected before merging into `main`.

**Why this priority**: Ensures continuous, deterministic IP protection across all portfolio content without relying on manual checks.

**Independent Test**: Run `python scripts/validate_governance.py` on a clean `docs/` tree to verify zero IP findings, and on a temporary page missing an IP banner/footer to verify exact line and issue reporting.

**Acceptance Scenarios**:

1. **Given** files in `docs/sop/*.md` and `docs/narratives/cas*.md`, **When** evaluated by the IP validator, **Then** it verifies a `> [!IMPORTANT]` or `> [!NOTE]` top callout banner containing `Classification Level: RESTRICTED` or `RESTRICTED / HIGHLY CONFIDENTIAL`.
2. **Given** client case studies in `docs/narratives/*.md`, **When** evaluated, **Then** it verifies a classification banner containing `Classification Level: CONFIDENTIAL` or `CONFIDENTIAL - CLIENT CASE STUDY`.
3. **Given** technical blog posts in `docs/tech-blog/posts/*.md`, **When** evaluated, **Then** it verifies a banner containing `Classification Level: PUBLIC` or `PUBLIC - THOUGHT LEADERSHIP`.
4. **Given** core site pages in `docs/*.md`, **When** evaluated, **Then** it verifies a banner containing `Classification Level: PUBLIC`.
5. **Given** any Markdown page under `docs/**/*.md`, **When** evaluated, **Then** it verifies a copyright footer containing `*© 2026 Alexandre Franco. Ideas-to-Life. All rights reserved.*` (or equivalent standard copyright string).

---

### User Story 2 - Auto-Annotator / Generator CLI (`--fix-ip`) (Priority: P1)

As a contributor or automated workflow runner, I want a CLI flag `--fix-ip` in `scripts/validate_governance.py`, so that any new or existing Markdown page missing IP classification banners or copyright footers can be automatically annotated with the proper header and footer.

**Why this priority**: Streamlines content authoring and enables automated remediation in CI/CD or local pre-commit hooks.

**Independent Test**: Create an unannotated page in a temporary directory, run `validate_ip_governance(docs_dir, fix=True)`, and verify the file is updated with both the path-appropriate classification banner at the top and the copyright footer at the bottom.

**Acceptance Scenarios**:

1. **Given** an unannotated page at `docs/narratives/new-engagement.md`, **When** `--fix-ip` is run, **Then** a `CONFIDENTIAL - CLIENT CASE STUDY` banner is prepended after any frontmatter, and a copyright footer is appended to the file.
2. **Given** a page with existing valid banners and footers, **When** `--fix-ip` is run, **Then** the file remains unchanged (idempotent execution).

---

### User Story 3 - GitHub Actions CI/CD Orchestration (Priority: P1)

As a DevOps maintainer, I want `.github/workflows/portfolio-governance.yml` to execute the full governance suite (mkdocs strict build + terminology + IP classification checks), so that PRs and pushes to `main` strictly enforce IP compliance.

**Why this priority**: Protects `main` branch integrity and guarantees zero IP drift in production.

**Independent Test**: Verify `.github/workflows/portfolio-governance.yml` includes the IP validation step and passes in GitHub Actions environment.

**Acceptance Scenarios**:

1. **Given** a pull request with an unclassified Markdown page, **When** the GitHub Action runs, **Then** the governance validation step reports IP classification findings and exits according to governance policy.

---

### User Story 4 - Automated Unit Test Suite (Priority: P1)

As a software engineer, I want pytest unit tests in `tests/test_validate_ip.py`, so that the IP validation logic, path rules, and auto-fix mechanisms are regression-tested with 100% test pass rate.

**Why this priority**: Guarantees system stability and prevents regressions during future script refactorings.

**Independent Test**: Run `pytest tests/` and verify all tests pass.

---

## Technical Dependencies & Constraints

- **Python 3.12+**: Built using standard library (`os`, `re`, `argparse`, `sys`, `pathlib`).
- **Markdown Integrity**: Frontmatter blocks (`--- ... ---`) must be preserved when inserting classification banners.
- **Idempotency**: `--fix-ip` must be completely idempotent; running it multiple times must not duplicate banners or footers.
