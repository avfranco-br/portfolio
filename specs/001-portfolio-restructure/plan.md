# Implementation Plan: Portfolio Look & Feel Restructure (MkDocs Material)

**Branch**: `001-portfolio-restructure` | **Date**: 2026-08-04 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/001-portfolio-restructure/spec.md`

## Summary

Restructure the presentation layer of the portfolio site into an executive-grade presentation while preserving 100% of existing written content, page URLs, and GitHub Pages deployment infrastructure. 

Tier 1 creates a full-width hero homepage (`overrides/home.html`), card grid navigation for Selected Work engagements, and standardized `Challenge / Approach / Outcome` subheadings on long-form narrative pages. Tier 2 integrates headshot media, certification badges, CV PDF download, and career timeline when unblocked by OKF knowledge bundle access.

## Technical Context

**Language/Version**: Markdown / Python 3.12  
**Primary Dependencies**: MkDocs 1.6+, MkDocs Material 9.5+  
**Storage**: Static Markdown files (`docs/`), theme template overrides (`overrides/home.html`)  
**Testing**: `mkdocs build --strict`, `pytest tests/`, `bash scripts/run_governance.sh`  
**Target Platform**: GitHub Pages (Static HTML/CSS)  
**Project Type**: Static Portfolio Site  
**Performance Goals**: Fast page load (<1s), 100% Lighthouse accessibility score  
**Constraints**: Static site generation only, zero dynamic backend API or custom JS bloat (per Constitution Principle I & IV), preserve all existing URLs & content word count  
**Scale/Scope**: ~15 pages, Tier 1 immediate restructuring + Tier 2 OKF asset integration  

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Principle I (Documentation-First)**: **PASS** — Markdown-native, git-friendly template overrides (`overrides/home.html` extending Material `main.html`).
- **Principle II (SDD)**: **PASS** — Specification `specs/001-portfolio-restructure/spec.md` exists and is ratified.
- **Principle III (CAS Governance)**: **PASS** — Follows `cas-add-or-modify-feature` and build-time governance rules.
- **Principle IV (Operational Simplicity)**: **PASS** — Leverages native MkDocs Material features (`grid cards`, `overrides/`, `hide: [navigation, toc]`) without complex external frameworks or JS bloat.
- **Principle V (Systems Thinking & Transparency)**: **PASS** — Narrative structure and architectural flows remain transparently linked.

**Status**: ALL GATES PASSED (0 violations).

## Project Structure

### Documentation (this feature)

```text
specs/001-portfolio-restructure/
├── spec.md              # Feature specification
├── plan.md              # Implementation plan (/speckit-plan output)
├── research.md          # Phase 0 research output (/speckit-plan output)
├── data-model.md        # Phase 1 data model output (/speckit-plan output)
├── quickstart.md        # Phase 1 quickstart output (/speckit-plan output)
├── contracts/           # Layout contracts
│   ├── homepage-hero-contract.md
│   └── narrative-structure-contract.md
└── checklists/
    └── requirements.md  # Specification quality checklist
```

### Source Code (repository root)

```text
docs/
├── index.md             # Custom hero frontmatter & Selected Work card grid
├── about.md             # Profile & career background
├── selected-work.md     # Selected Work card grid index
├── narratives/          # Restructured narrative pages with Challenge/Approach/Outcome
│   ├── bat-transformation.md
│   ├── bbc-studios-digital-evolution.md
│   ├── ea4all.md
│   └── cas.md
└── assets/
    └── images/          # Image assets & headshot photo

overrides/
└── home.html            # Custom hero template extending Material main.html

mkdocs.yml               # Theme configuration (custom_dir: overrides)
```

**Structure Decision**: Single project layout with native MkDocs Material template override directory (`overrides/`).

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
