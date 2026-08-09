# Tasks: Tech Blog Approval Status Publishing Filter

**Input**: Design documents from `/specs/002-tech-blog-approval-status/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/frontmatter-contract.md, quickstart.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2)
- Exact file paths included in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project configuration and environment setup

- [x] T001 Verify virtual environment and python dependencies in `.venv/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core governance checks required before story tasks

- [x] T002 Verify governance runner script `scripts/run_governance.sh` executes `.venv` binaries cleanly

---

## Phase 3: User Story 1 - Publish Only Approved Articles (Priority: P1) 🎯 MVP

**Goal**: Exclude unapproved or draft articles from public navigation and blog index listings, rendering only `status: approved` articles.

**Independent Test**: Build site using `bash scripts/run_governance.sh` and verify only articles with `status: approved` appear in `mkdocs.yml` navigation and `docs/tech-blog/index.md`.

### Implementation for User Story 1

- [x] T003 [P] [US1] Audit YAML frontmatter across all articles in `docs/tech-blog/` for `status: approved` attribute
- [x] T004 [P] [US1] Update `docs/tech-blog/index.md` listing to include only approved technical articles
- [x] T005 [US1] Update `mkdocs.yml` navigation to register only approved technical articles under `Tech Blog` section

**Checkpoint**: User Story 1 MVP fully functional - only approved articles published.

---

## Phase 4: User Story 2 - Author Frontmatter Approval Workflow (Priority: P2)

**Goal**: Validate article frontmatter status (`approved`, `draft`, `review`) automatically during governance checks.

**Independent Test**: Run `python scripts/validate_governance.py` and verify it checks for frontmatter schema compliance and reports status warnings.

### Implementation for User Story 2

- [x] T006 [P] [US2] Update `scripts/validate_governance.py` to validate `status` attribute in YAML frontmatter for files in `docs/tech-blog/`
- [x] T007 [P] [US2] Add unit test cases in `tests/test_validate_terminology.py` to verify frontmatter status validation logic

**Checkpoint**: Both User Story 1 and User Story 2 complete and verified.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Final verification and documentation updates

- [x] T008 [P] Update feature specification documentation in `specs/002-tech-blog-approval-status/spec.md`
- [x] T009 Execute quickstart validation guide scenarios from `specs/002-tech-blog-approval-status/quickstart.md`
- [x] T010 Run full test suite `pytest tests/` and governance check `bash scripts/run_governance.sh`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: Can start immediately.
- **Foundational (Phase 2)**: Depends on Setup completion.
- **User Story 1 (Phase 3)**: Depends on Foundational completion.
- **User Story 2 (Phase 4)**: Depends on Foundational completion.
- **Polish (Phase 5)**: Depends on completion of User Stories 1 & 2.

### Parallel Opportunities

- T003 and T004 can run in parallel.
- T006 and T007 can run in parallel.
- T008 can run in parallel with final verification.
