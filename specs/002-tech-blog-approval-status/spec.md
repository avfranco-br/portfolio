# Feature Specification: Tech Blog Approval Status Publishing Filter

**Feature Branch**: `002-add-tech-blog`

**Created**: 2026-08-09

**Status**: Draft

**Input**: User description: "change the current tech-blog feature to publish only status.approved"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Publish Only Approved Articles (Priority: P1)

As a site administrator and author, I want only technical blog posts with `status: approved` in their frontmatter to be published and rendered in the site navigation, so that draft or under-review articles are not exposed to visitors.

**Why this priority**: Core publishing safety rule preventing unapproved content exposure on the live portfolio platform.

**Independent Test**: Add an article with `status: draft` or missing approval status to `docs/tech-blog/` and verify it is excluded from navigation and the generated blog index page, while articles with `status: approved` are rendered properly.

**Acceptance Scenarios**:

1. **Given** a markdown article in `docs/tech-blog/` with `status: approved` in its YAML frontmatter, **When** the site is built via `mkdocs build --strict`, **Then** the article is published and included in the Tech Blog navigation and index listing.
2. **Given** a markdown article in `docs/tech-blog/` with `status: draft` or unapproved status, **When** the site build occurs, **Then** the article is excluded from published navigation and public index listings.

---

### User Story 2 - Author Frontmatter Approval Workflow (Priority: P2)

As a technical content author, I want a standard frontmatter contract (`status: approved | draft | review`) across all tech blog markdown files, so that article approval state is explicit, auditable, and version-controlled.

**Why this priority**: Ensures clear contract definition and governance traceability across technical articles.

**Independent Test**: Inspect all markdown files under `docs/tech-blog/` and verify that each contains a valid `status` field in its YAML frontmatter.

**Acceptance Scenarios**:

1. **Given** technical articles in `docs/tech-blog/`, **When** validated by the governance runner, **Then** every article conforms to the frontmatter schema including the `status` attribute.

---

### Edge Cases

- What happens when an article in `docs/tech-blog/` does not define a `status` attribute? Default behavior treats missing `status` as unapproved (`draft`) to prevent accidental content leakage.
- What happens when an excluded draft article is referenced elsewhere? The build validation checks ensure excluded files do not cause broken internal links.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST require a `status` attribute in YAML frontmatter for all technical blog posts under `docs/tech-blog/`.
- **FR-002**: System MUST only publish and render technical blog posts in navigation and index listings where `status` is explicitly set to `approved`.
- **FR-003**: System MUST treat missing, `draft`, or `review` status values as unapproved, excluding them from public navigation listings.
- **FR-004**: System MUST maintain strict build validation (`mkdocs build --strict`) without broken links or unlinked file warnings for both approved and unapproved posts.

### Key Entities

- **Technical Article Frontmatter**: Includes `title`, `pubDate`, `tags`, `author`, `slug`, `target`, and `status` (`approved` | `draft` | `review`).
- **Tech Blog Index**: Navigation and overview page reflecting only approved articles.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of published technical blog posts on the live site have verified `status: approved` frontmatter metadata.
- **SC-002**: Zero unapproved or draft articles appear in the public navigation or blog index listing.
- **SC-003**: `bash scripts/run_governance.sh` passes with zero build failures or link warnings.

## Assumptions

- Articles stored in `docs/tech-blog/` use standard YAML frontmatter blocks.
- Unapproved or draft articles remain stored in the repository source for iterative drafting without being exposed in the rendered public site navigation.
