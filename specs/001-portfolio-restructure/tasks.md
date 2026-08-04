# Tasks: Portfolio Look & Feel Restructure (MkDocs Material)

**Input**: Design documents from `/specs/001-portfolio-restructure/`  
**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md`

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: User story label (US1, US2, US3, US4)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Configure MkDocs overrides directory setting in `mkdocs.yml`

- [x] T001 Configure `theme.custom_dir: overrides` in `mkdocs.yml`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core template override structure required before homepage customization

- [x] T002 [P] Create base layout override in `overrides/home.html` extending Material `main.html`

---

## Phase 3: User Story 1 - Full-Width Executive Hero Homepage (Priority: P1) 🎯 MVP

**Goal**: Transform the root page (`/`) into a full-width executive hero landing page without sidebars.

**Independent Test**: Load `http://127.0.0.1:8000/`. Verify page displays name, title, intro text, and CTA buttons across full container width without left navigation or right TOC sidebars.

### Implementation for User Story 1

- [x] T003 [P] [US1] Update frontmatter in `docs/index.md` with `template: home.html` and `hide: [navigation, toc]`
- [x] T004 [P] [US1] Implement full-width Hero HTML template block in `overrides/home.html` per `homepage-hero-contract.md`
- [x] T005 [US1] Add headshot placeholder container comment `<!-- TODO: replace with headshot, see Spec 003 R4 -->` in `overrides/home.html`

**Checkpoint**: At this point, User Story 1 (MVP) is fully functional and testable independently.

---

## Phase 4: User Story 2 - Selected Work Card Grid Navigation (Priority: P2)

**Goal**: Convert Selected Work list into responsive Material card grid navigation.

**Independent Test**: View Selected Work section on homepage/selected-work page. Click card links to confirm they navigate to existing engagement narratives.

### Implementation for User Story 2

- [x] T006 [P] [US2] Implement Card Grid component `<div class="grid cards" markdown>` in `docs/index.md` for BAT, BBC Studios, EA4ALL, and CAS
- [x] T007 [P] [US2] Add Selected Work Card Grid component to `docs/selected-work.md` per `homepage-hero-contract.md`

**Checkpoint**: User Stories 1 AND 2 are independently functional.

---

## Phase 5: User Story 3 - Standardized Engagement Page Structure (Priority: P3)

**Goal**: Organize existing prose in narrative pages under `## Challenge`, `## Approach`, and `## Outcome` subheadings.

**Independent Test**: Open each narrative page and confirm subheadings are applied in order without reducing total word count.

### Implementation for User Story 3

- [x] T008 [P] [US3] Organize prose in `docs/narratives/bat-transformation.md` under `## Challenge`, `## Approach`, and `## Outcome` per `narrative-structure-contract.md`
- [x] T009 [P] [US3] Organize prose in `docs/narratives/bbc-studios-digital-evolution.md` under `## Challenge`, `## Approach`, and `## Outcome` per `narrative-structure-contract.md`
- [x] T010 [P] [US3] Organize prose in `docs/narratives/ea4all.md` under `## Challenge`, `## Approach`, and `## Outcome` per `narrative-structure-contract.md`
- [x] T011 [P] [US3] Organize prose in `docs/narratives/cas.md` under `## Challenge`, `## Approach`, and `## Outcome` per `narrative-structure-contract.md`

**Checkpoint**: All Tier 1 user stories are complete and testable independently.

---

## Phase 6: User Story 4 - OKF-Sourced Professional Assets & Milestones (Priority: P4 - Tier 2)

**Goal**: Integrate headshot, cert badges, CV PDF download, and career timeline when OKF knowledge bundle path access is provided.

**Independent Test**: Verify headshot renders in hero, cert badges display, CV link downloads PDF, and timeline displays chronologically.

### Implementation for User Story 4

- [ ] T012 [P] [US4] Copy headshot image from OKF bundle to `docs/assets/images/headshot.jpg` and wire into `overrides/home.html`
- [ ] T013 [P] [US4] Add certification badges row in `docs/index.md` / `docs/about.md` from OKF bundle
- [ ] T014 [P] [US4] Copy CV PDF to `docs/assets/alexandre-franco-cv.pdf` and link from hero CTA buttons
- [ ] T015 [US4] Render career timeline component in `docs/about.md` from OKF bundle milestones

---

## Phase 7: Polish & Governance Validation

**Purpose**: Final verification and zero-drift governance check

- [x] T016 [P] Run `bash scripts/run_governance.sh` to verify `mkdocs build --strict` and terminology check pass
- [x] T017 [P] Run `pytest tests/` test suite to verify 0 regressions
- [x] T018 Execute `quickstart.md` validation scenarios and word count sanity check script

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - start immediately.
- **Foundational (Phase 2)**: Depends on Phase 1 completion.
- **User Stories (Phases 3-5, Tier 1)**: Depend on Phase 2 completion. Can run sequentially (US1 → US2 → US3) or in parallel.
- **Tier 2 User Story (Phase 6)**: Depends on OKF bundle path access provided by Alexandre.
- **Polish (Phase 7)**: Depends on Tier 1 tasks (T001-T011) completion.

### Parallel Opportunities

- T003 & T004 in US1 can run in parallel.
- T006 & T007 in US2 can run in parallel.
- T008, T009, T010, T011 in US3 can all run in parallel (different narrative files).
- T012, T013, T014 in US4 can run in parallel once unblocked.
- T016 & T017 in Polish phase can run in parallel.

---

## Implementation Strategy

### MVP First (User Story 1 Only)
1. Complete Phase 1 & 2 (Setup & Foundational)
2. Complete Phase 3 (User Story 1)
3. Validate: Run `mkdocs serve` to test executive hero homepage
4. Deploy/Demo MVP increment

### Incremental Delivery
1. MVP (Hero Homepage) → Deploy
2. Add US2 (Card Grid Navigation) → Deploy
3. Add US3 (Narrative Re-heading) → Deploy
4. Add US4 (Tier 2 OKF Assets) → Deploy when unblocked
