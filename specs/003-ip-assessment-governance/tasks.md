# Tasks: Intellectual Property Assessment & Content Governance

**Feature Branch**: `feature/ip-assessment-report` | **Spec**: [spec.md](spec.md) | **Plan**: [plan.md](plan.md)

## Phase 1: Assessment & Report Generation

- [x] **Task 1.1**: Conduct deep-dive IP, data classification, and security audit of target scope (`docs/`, `governance/`, `specs/`).
- [x] **Task 1.2**: Generate standardized 8-section report at `tests/portfolio-ip-report.md` conforming to `experiments/intellectual-property.md` rules.

## Phase 2: Content Safeguards & Banners Implementation

- [x] **Task 2.1**: Apply Category 1 🔴 `RESTRICTED / HIGHLY CONFIDENTIAL` GitHub alert banners and copyright footers to `docs/sop/*.md` and `docs/narratives/cas*.md`.
- [x] **Task 2.2**: Apply Category 2 🟡 `CONFIDENTIAL - CLIENT CASE STUDY` GitHub alert banners and copyright footers to client case studies (`bat`, `bbc-studios`, `ea4all`, `runner`).
- [x] **Task 2.3**: Apply Category 2 🟡 `PUBLIC - THOUGHT LEADERSHIP` GitHub alert banners and copyright footers to technical blog posts (`docs/tech-blog/posts/*.md`).
- [x] **Task 2.4**: Apply Category 3 🟢 `PUBLIC` GitHub alert banners and copyright footers to core site pages (`index`, `about`, `contact`, `how-i-work`, `selected-work`, `architecture-philosophy`).
- [x] **Task 2.5**: Fix typo in `docs/contact.md` (`Introdcution Call` -> `Introduction Call`).

## Phase 3: Branch Management & Git Hygiene

- [x] **Task 3.1**: Stash uncommitted changes, sync with updated `main`, and create feature branch `feature/ip-assessment-report`.
- [x] **Task 3.2**: Restore stashed changes cleanly onto `feature/ip-assessment-report` branch.
- [x] **Task 3.3**: Commit all 26 modified/created files under conventional commit header `feat(governance): add IP attribution, classification banners, and assessment report`.

## Phase 4: Validation & Quality Gates

- [x] **Task 4.1**: Execute `mkdocs build --strict` to verify site navigation, layout rendering, and link integrity.
- [x] **Task 4.2**: Execute `python scripts/validate_governance.py` to verify canonical terminology compliance.
- [x] **Task 4.3**: Execute `pytest tests/` to verify test suite passes 25/25 tests.
