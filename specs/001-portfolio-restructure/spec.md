# Feature Specification: Portfolio Look & Feel Restructure (MkDocs Material)

**Feature Branch**: `001-portfolio-restructure`

**Created**: 2026-08-04

**Status**: Draft

**Input**: User description: "Portfolio Look & Feel Restructure (MkDocs Material) @[specs/claude-specs.md/portfolio-look-and-feel-restructure.md]"

## Context & Strategy

The portfolio currently resolves at `alexandrefranco.dev` using MkDocs Material's default documentation layout (left sidebar navigation, dense prose blocks, no hero section, and no visual distinction between career engagements). This presents as a technical documentation wiki rather than a senior executive/architect portfolio. 

The goal is to restructure the presentation layer—templates, layout, and visual component organization—without deleting, trimming, or moving any existing written content, ensuring all existing page URLs remain intact and accessible.

Implementation is split into a **Two-Tier Scope**:
- **Tier 1 (Immediate)**: Restructure existing text and layout into a full-width hero homepage, card grid navigation, and standardized `Challenge / Approach / Outcome` engagement sections.
- **Tier 2 (OKF Sourced)**: Integrate headshot image, certification badge row, downloadable CV/résumé, and career timeline when unblocked by sourcing from the candidate's OKF (Open Knowledge Format) bundle.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Full-Width Executive Hero Homepage (Priority: P1)

As a site visitor or potential client, I want to land on a full-width executive hero section containing Alexandre Franco's name, title, intro copy, and primary action buttons, so that I immediately understand his core identity and value proposition without distraction from documentation sidebars.

**Why this priority**: First impressions dictate portfolio engagement. Replacing the wiki sidebar layout on the homepage with an executive hero establishes immediate credibility.

**Independent Test**: Navigate to `https://alexandrefranco.dev/`. Verify the page renders full-width without a left sidebar or table of contents, displaying the name, title, introduction text, and CTA buttons.

**Acceptance Scenarios**:

1. **Given** a visitor navigates to the homepage (`/`), **When** the page renders, **Then** no left navigation sidebar or TOC sidebar is visible, and a hero component is displayed across the full container width.
2. **Given** the hero component renders, **When** viewed on desktop or mobile, **Then** it presents the name "Alexandre Franco", title "Enterprise Architect & AI Transformation Advisor", the intro paragraph, and CTA buttons linking to Selected Work, Contact, Mostelli, and Ideas to Life.

---

### User Story 2 - Selected Work Card Grid Navigation (Priority: P2)

As a visitor scanning portfolio engagements, I want to view Selected Work as a grid of visually distinct cards with one-line summaries and arrow links, so that I can intuitively explore key career transformations.

**Why this priority**: Replaces dense bullet lists with modern, card-based navigation while preserving existing URLs.

**Independent Test**: Scroll to the Selected Work section on the homepage or navigation index. Verify engagements (BAT, BBC Studios, EA4ALL, CAS) render in a card grid using MkDocs Material grid card syntax, each linking to its respective existing page.

**Acceptance Scenarios**:

1. **Given** the Selected Work section on the homepage, **When** rendered, **Then** each engagement appears inside an interactive grid card with an icon, title, single-sentence summary, and "Read more" link.
2. **Given** a user clicks "Read more" on any card (e.g., BAT Transformation), **When** navigated, **Then** the existing engagement page loads at its original URL without broken links.

---

### User Story 3 - Standardized Engagement Page Structure (Priority: P3)

As a reader reviewing a specific career engagement, I want the prose structured under clear `Challenge`, `Approach`, and `Outcome` headings, so that I can digest complex transformations quickly.

**Why this priority**: Improves scannability across all long-form narratives without altering underlying facts or word counts.

**Independent Test**: Open any engagement page (e.g., `/narratives/bat-transformation.md`). Verify the existing content is organized under `## Challenge`, `## Approach`, and `## Outcome` subheadings.

**Acceptance Scenarios**:

1. **Given** an existing narrative page, **When** rendered, **Then** existing content is grouped under `## Challenge`, `## Approach`, and `## Outcome` subheadings without removing any sentences or paragraphs.
2. **Given** the updated narrative page, **When** total word count is compared before and after, **Then** post-update word count is equal to or greater than the original word count.

---

### User Story 4 - OKF-Sourced Professional Assets & Milestones (Priority: P4 - Tier 2)

As a visitor reviewing credentials, I want to see a headshot photo, certification badges, a downloadable CV, and a career timeline sourced from the OKF knowledge bundle once provided, so that I have a complete executive overview.

**Why this priority**: Enhances visual polish and proof points once external assets/data are unblocked.

**Independent Test**: Verify headshot renders in hero, cert badges display near About section, CV download link serves PDF, and timeline displays chronological roles.

**Acceptance Scenarios**:

1. **Given** the OKF bundle path is provided, **When** Tier 2 assets are integrated, **Then** `docs/assets/images/headshot.jpg` renders in the hero without placeholder comments.
2. **Given** CV PDF and career milestone data in OKF, **When** integrated, **Then** CV link downloads the PDF and timeline renders chronologically.

---

### Edge Cases

- What happens when an engagement narrative does not have content matching all three subheadings (`Challenge`, `Approach`, `Outcome`)?  
  *Fallback*: Populate the sections that fit and leave missing sections uncreated; do not fabricate filler content.
- What happens if Tier 2 assets (headshot, CV, OKF bundle) are delayed?  
  *Fallback*: Tier 1 features deploy cleanly with an HTML placeholder comment (`<!-- TODO: replace with headshot, see Spec 003 R4 -->`) and standard CTA links.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a custom homepage template (`overrides/home.html`) that hides navigation and table-of-contents sidebars (`hide: [navigation, toc]`) for the root page (`index.md`).
- **FR-002**: System MUST render a full-width Hero section on the homepage containing name ("Alexandre Franco"), title ("Enterprise Architect & AI Transformation Advisor"), intro copy, and CTA buttons.
- **FR-003**: System MUST display Selected Work engagements as MkDocs Material card grids (`<div class="grid cards" markdown>`), with each card containing an icon, title, one-sentence summary, and arrow link.
- **FR-004**: System MUST preserve all existing URLs and page files (BAT, BBC Studios, EA4ALL, CAS) without deleting or shortening narrative content.
- **FR-005**: System MUST organize narrative prose on engagement pages into `## Challenge`, `## Approach`, and `## Outcome` subheadings.
- **FR-006**: System MUST support Tier 2 static generation from the OKF knowledge bundle (headshot, certifications, CV PDF, timeline) when the local OKF directory path is supplied.
- **FR-007**: System MUST pass `mkdocs build --strict` with zero broken links or navigation warnings.

### Key Entities

- **Hero Component**: Presentation block containing identity header, title, intro copy, CTA action buttons, and headshot container.
- **Selected Work Card Grid**: Grid layout component mapping engagement metadata to Material card structures.
- **Engagement Narrative**: Structured Markdown page containing `Challenge`, `Approach`, and `Outcome` sections.
- **OKF Knowledge Bundle**: External structured local repository containing source evidence, career milestones, certification records, and media assets.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Homepage renders full-width hero layout without sidebar or TOC navigation elements on 100% of tested viewports.
- **SC-002**: 100% of existing navigation pages remain reachable at their original URLs with zero broken links reported during `mkdocs build --strict`.
- **SC-003**: Word count on each restructured narrative page after heading organization is ≥ original word count.
- **SC-004**: Site build and automated governance validation (`bash scripts/run_governance.sh`) complete successfully with 0 errors.

## Assumptions

- **Architecture Constraint**: Solution remains strictly within MkDocs Material static site generation (no Astro migration or backend APIs per Constitution Principle IV).
- **Content Preservation**: No narrative text is deleted, shortened, or re-homed to external sites during Tier 1.
- **Tier 2 Sourcing**: Tier 2 assets (headshot, CV PDF, certification list, career milestones) will be read statically from the local OKF knowledge bundle when Alexandre provides the directory path.
