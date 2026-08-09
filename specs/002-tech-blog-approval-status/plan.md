# Implementation Plan: Tech Blog Approval Status Publishing Filter

**Branch**: `002-add-tech-blog` | **Date**: 2026-08-09 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/002-tech-blog-approval-status/spec.md`

## Summary

Enforce a publishing filter on the Tech Blog section so that only technical markdown articles in `docs/tech-blog/` with explicit YAML frontmatter `status: approved` are published and included in site navigation and index listings. Articles with `status: draft`, `status: review`, or missing status are excluded.

## Technical Context

**Language/Version**: Python 3.13, Markdown

**Primary Dependencies**: MkDocs, MkDocs Material, PyYAML

**Storage**: Markdown files (`docs/tech-blog/*.md`)

**Testing**: pytest, `bash scripts/run_governance.sh` (`mkdocs build --strict`, `validate_governance.py`)

**Target Platform**: GitHub Pages (static site)

**Project Type**: Static Site / Portfolio Platform

**Performance Goals**: Sub-2s static site build time

**Constraints**: Zero runtime JS dependencies for status filtering; zero broken link warnings in strict build mode.

**Scale/Scope**: 5+ technical articles in `docs/tech-blog/`

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **I. Documentation-First**: Markdown-native, git-friendly, static site generation.
- [x] **II. Specification-Driven Development**: Spec created at `specs/002-tech-blog-approval-status/spec.md`.
- [x] **III. CAS Governance Operationalisation**: Validated via CAS rules and `scripts/validate_governance.py`.
- [x] **IV. Operational Simplicity & Sustainability**: Uses native MkDocs navigation and build validation without custom plugin bloat.
- [x] **V. Systems Thinking & Transparency**: Architecture decision documented.

*Gate Status*: **PASSED**

## Project Structure

### Documentation (this feature)

```text
specs/002-tech-blog-approval-status/
├── plan.md              # This file
├── research.md          # Phase 0 research decisions
├── data-model.md        # Entity definitions & validation rules
├── quickstart.md        # Runnable verification scenarios
└── contracts/
    └── frontmatter-contract.md # YAML frontmatter status schema contract
```

### Source Code (repository root)

```text
docs/tech-blog/
├── index.md             # Overview page listing only status: approved posts
└── *.md                 # Tech blog articles with YAML frontmatter (status: approved)

scripts/
├── validate_governance.py # Frontmatter & terminology governance validator
└── run_governance.sh     # Master governance check runner

mkdocs.yml               # Configured nav listing approved posts
```

**Structure Decision**: Single static site project layout under `docs/tech-blog/`, `mkdocs.yml`, and `scripts/`.

## Complexity Tracking

*No constitution violations. Table left empty.*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
