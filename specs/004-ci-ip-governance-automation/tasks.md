# Tasks: Automated CI/CD IP Assessment & Content Governance

**Feature Branch**: `feature/ci-ip-governance-automation` | **Spec**: [spec.md](spec.md) | **Plan**: [plan.md](plan.md)

## Phase 1: Core Script & CLI Development

- [x] **Task 1.1**: Implement `validate_ip_governance(docs_dir, fix=False)` in `scripts/validate_governance.py` with banner & footer checking logic.
- [x] **Task 1.2**: Implement `--fix-ip` auto-annotation / generation logic in `scripts/validate_governance.py`.
- [x] **Task 1.3**: Update `scripts/run_governance.sh` to forward CLI arguments (`"$@"`) to `validate_governance.py`.

## Phase 2: Unit Testing & Verification

- [x] **Task 2.1**: Create `tests/test_validate_ip.py` with test cases for clean docs, missing headers, missing footers, frontmatter parsing, path taxonomy mapping, and `--fix-ip` idempotency.
- [x] **Task 2.2**: Run `pytest tests/` and ensure 100% test pass rate across all test files.

## Phase 3: CI/CD Pipeline & Repo Validation

- [x] **Task 3.1**: Verify `.github/workflows/portfolio-governance.yml` executes updated `scripts/validate_governance.py`.
- [x] **Task 3.2**: Execute `bash scripts/run_governance.sh` against the actual repository to confirm zero IP findings on existing pages.

## Phase 4: Git Commit & Governance Sign-off

- [x] **Task 4.1**: Stage and commit all changes on `feature/ci-ip-governance-automation`.
