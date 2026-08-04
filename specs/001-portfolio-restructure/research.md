# Phase 0 Research & Technology Choices

**Feature**: Portfolio Look & Feel Restructure (MkDocs Material)  
**Branch**: `001-portfolio-restructure`  
**Date**: 2026-08-04

---

## 1. Homepage Template Override (`overrides/home.html`)

### Decision
Use MkDocs Material's built-in theme override mechanism (`theme.custom_dir: overrides` in `mkdocs.yml`) to create `overrides/home.html` extending `main.html`.

### Rationale
- MkDocs Material allows page-level layout overrides by placing HTML templates in `overrides/` and referencing them via template metadata or using Material's block overriding (`{% extends "main.html" %}`).
- In `docs/index.md`, set `hide: [navigation, toc]` in frontmatter to suppress the left sidebar navigation and right table-of-contents sidebar, allowing the page content to expand to full container width.
- This adheres strictly to Constitution Principle IV (Operational Simplicity) by utilizing MkDocs Material's native extension hooks rather than replacing the framework or injecting heavy custom CSS/JS.

### Alternatives Considered
- **Migrating to Astro / Next.js**: Rejected because it violates Constitution Principle IV (simplicity), breaks the existing GitHub Actions deployment pipeline, and requires unnecessary framework overhead.
- **Injecting global CSS hacks to hide sidebars on index page**: Rejected because using native `hide: [navigation, toc]` frontmatter is clean, supported out of the box, and maintainable.

---

## 2. Card Grid Presentation for Selected Work (`<div class="grid cards" markdown>`)

### Decision
Use MkDocs Material's native Card Grid Markdown extension syntax (`<div class="grid cards" markdown>`) to present Selected Work narratives (BAT, BBC Studios, EA4ALL, CAS) on the homepage.

### Rationale
- Material for MkDocs natively supports responsive card layouts when Python-Markdown's `markdown` attribute is enabled on container `div`s.
- Each card displays a icon class (e.g. `:material-office-building:`), bold title, one-line summary extracted from the narrative's lead sentence, and an arrow link (`[:octicons-arrow-right-24: Read more](narratives/...)`).
- Cards provide an immediate visual cue that the site is a curated executive portfolio while preserving all underlying narrative file paths and URLs.

### Alternatives Considered
- **Raw HTML cards with custom CSS flexbox**: Rejected because MkDocs Material's `grid cards` class handles responsive breakpoints, dark/light theme switching, and spacing out-of-the-box.

---

## 3. Standardized Narrative Sectioning (`Challenge`, `Approach`, `Outcome`)

### Decision
Organize existing long-form prose in engagement narratives (BAT, BBC Studios, EA4ALL, CAS) under three explicit Markdown level-2 headings: `## Challenge`, `## Approach`, and `## Outcome`.

### Rationale
- Executive readers require scannable narrative arcs. Standardizing on `Challenge / Approach / Outcome` provides consistent structure across all career case studies.
- Content re-heading is strictly additive: existing paragraphs are grouped under the matching section header. No sentences are deleted or modified in meaning.

### Alternatives Considered
- **Rewriting narrative prose into brief bullet points**: Rejected to honor the core constraint: content preservation (no content deletion or trimming without confirmed destination).

---

## 4. Static Sourcing from OKF (Open Knowledge Format) Bundle (Tier 2)

### Decision
Source Tier 2 assets (headshot image, certification badges, CV PDF, and career timeline) via static file copying at build time from the local OKF knowledge bundle when the path is provided.

### Rationale
- Sourcing data from the OKF bundle ensures zero transcription drift for career dates, certifications, and credentials.
- The build process remains 100% static: assets and structured data are read during static site setup and compiled into static HTML/Markdown, maintaining zero-runtime dependency per Constitution Principle I & IV.

### Alternatives Considered
- **Runtime API / JavaScript fetch against a live OKF server**: Rejected because it introduces dynamic runtime dependencies, latency, and potential failure points, violating the static site architecture mandate.
