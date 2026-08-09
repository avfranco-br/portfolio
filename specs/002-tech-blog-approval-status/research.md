# Phase 0 Research: Tech Blog Approval Status Publishing Filter

## Decision 1: Technical Article Approval Filter Mechanism

- **Decision**: Filter published technical blog posts by reading YAML frontmatter `status` (`approved` vs `draft`/`review`), reflecting approved posts in `mkdocs.yml` navigation and `docs/tech-blog/index.md`.
- **Rationale**: MkDocs Material renders pages based on navigation configuration. Explicitly registering only `status: approved` articles in `mkdocs.yml` navigation and index listings guarantees zero unapproved content exposure.
- **Alternatives Considered**:
  - Custom MkDocs plugin: Rejected to maintain operational simplicity per Constitution Principle IV (Operational Simplicity & Sustainability).
  - Client-side JavaScript hiding: Rejected because unapproved markdown files would still be compiled into static HTML and accessible.

## Decision 2: Default Approval State for Unspecified Articles

- **Decision**: Treat missing `status` attributes as `draft` (unapproved).
- **Rationale**: Secure fail-safe default preventing accidental publication of draft or WIP technical content.
- **Alternatives Considered**:
  - Defaulting missing status to `approved`: Rejected due to risk of content leakage.

## Decision 3: Build Integrity & Draft Isolation

- **Decision**: Validate frontmatter status during `scripts/validate_governance.py` execution while allowing draft files to exist in `docs/tech-blog/` without breaking `mkdocs build --strict`.
- **Rationale**: Authors can draft articles locally in git branches while maintaining strict build validation across published pages.
- **Alternatives Considered**:
  - Moving drafts out of `docs/`: Rejected because keeping drafts alongside published articles in version control simplifies authoring workflow.
