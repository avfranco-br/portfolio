# Validator Test Suite — Design Spec

**Date:** 2026-08-03
**Status:** Proposed
**Scope:** Add automated tests for `scripts/validate_governance.py`

---

## 1. Problem

`scripts/validate_governance.py` is the only executable component of the governance layer. It runs in CI on every PR but is **untested**:

- No regression protection if the YAML schema changes.
- No guarantee that code-block stripping still works after refactoring.
- No confidence that word-boundary matching behaves correctly across canonical terms.
- Manual `print()` statements are the only "test" today.

A regression here would silently allow rejected terminology into the deployed portfolio.

## 2. Goal

Add a pytest suite that covers the script's behaviour and gives future contributors a safety net for refactoring.

## 3. Non-Goals

- Changing the validator's behaviour or output format.
- Replacing the inline `print()` statements with a proper logger.
- Restructuring the script into multiple modules.
- Adding type hints (out of scope; can be a separate thread).

## 4. Test Layout

```
tests/
├── __init__.py                # marks as a package (optional)
├── conftest.py                # shared fixtures (policy, docs tree)
├── test_validate_terminology.py   # the actual tests
└── fixtures/
    ├── policy_clean.yaml      # canonical terms, no rejects
    └── policy_full.yaml       # full canonical terms with all rejects
```

Pytest discovers tests automatically. The CI pipeline does not need to be updated because tests are run locally during development and the validator itself runs in CI for behaviour checks.

A minimal `pytest.ini` (or `pyproject.toml [tool.pytest.ini_options]`) pins the test paths so `pytest` invoked from the repo root finds the suite.

## 5. Test Cases

The suite must cover **10 distinct behaviours**:

| # | Test | Setup | Assertion |
|---|------|-------|-----------|
| 1 | Empty docs tree → no findings | empty docs dir | `findings == []` |
| 2 | Clean content → no findings | valid content with canonical terms | `findings == []` |
| 3 | Detects "AI-native" (hyphen variant) | single .md with `AI-native` | one finding, `preferred == "AI native"` |
| 4 | Case-insensitive detection | `AI-NATIVE`, `ai-native`, `Ai-Native` | all three produce findings |
| 5 | Word boundary precision | `AI natively` (different word) | no finding |
| 6 | Line number accuracy | doc with finding on line 5 | `finding.line == 5` |
| 7 | Recursion into nested dirs | finding in `docs/narratives/sub/` | finding with correct relative path |
| 8 | Code-block isolation | `AI-native` inside ```...``` | no finding |
| 9 | Inline-code isolation | `` `AI-native` `` on a line | no finding |
| 10 | Markdown link-target isolation | `AI-native` only inside `[text](AI-native)` | no finding |

Plus one **integration test** (optional but valuable):
- Run `validate_terminology` against the **actual repo** and assert it returns 0 findings (the repo is known-clean).

## 5a. Validator Fixes Required by Tests

The test suite revealed **one real bug in the validator**:

### Bug 1: Tilde-fence code blocks are not stripped

**Symptom:** `~~~ ... ~~~` fences are valid Markdown code blocks, but the validator's regex `r'```.*?```'` only matches backtick fences. A rejected term inside a tilde fence is incorrectly flagged.

**Fix:** Extend the fence-stripping step in `scripts/validate_governance.py` to handle both backtick and tilde fences. Two substitutions: one for ` ``` ... ``` ` and one for ` ~~~ ... ~~~ `. The fix must preserve newlines so line numbers remain accurate.

### Test 10 correction (not a bug)

The original test for markdown link-target isolation placed a rejected term in both the link text and the URL. The validator correctly strips only the URL target and leaves link text intact — which is the desired behaviour (confirmed by a new test 11). Test 10 was updated to put the rejected term **only** in the URL.

## 6. Acceptance Criteria

- `pytest tests/` runs the suite.
- All 10 tests pass.
- The integration test passes against the real repo.
- No production code in `scripts/` was modified.
- A `pytest` dev dependency is added to `requirements.txt` or a separate `requirements-dev.txt`.

## 7. Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Tests become flaky due to filesystem ordering | Sort findings before asserting |
| `os.walk` order varies across platforms | Use `sorted()` on findings, or assert by `set` membership |
| Pytest discovery broken by missing `__init__.py` | Use rootdir-based config; pytest handles this without `__init__.py` since 4.0 |
| Tests run against the real `docs/` accidentally | Fixtures use `tmp_path` exclusively |

## 8. Out-of-Scope Items (recorded for future)

- Property-based tests (hypothesis).
- Coverage reporting (e.g., `pytest-cov`).
- Mutation testing.
- Pre-commit hook integration.