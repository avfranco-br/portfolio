# Feature Specification: Architecture SOP Structure Reorganisation

**Feature Branch**: `005-sop-structure-reorg`

**Created**: 2026-09-17

**Status**: Draft

**Input**: User description: "update the existing Architecture SOP content structure to the new following structure: Core EA Practice → Discover & Align → Target Architecture & Strategy → Governance & Decision Enablement → Delivery Enablement & Execution Steering → Value Realisation & Organisational Handover; Engagement Methods → Architecture Decision Review → Architecture Assessment & Roadmap → Architecture Health Check → Architecture Automation Opportunity Assessment; Illustrative Evidence → Decision Review report → Assessment & Transformation Roadmap report. Source files are under docs/sop/methods."

## Clarifications

### Session 2026-09-17

- Q: Where should the auxiliary "AI Augmented Workflows" and "Agent Co-Pilot Prompt" pages be positioned within the updated navigation? → A: Option A: Place under a dedicated sub-section "AI Augmented Architecture" alongside the 3 primary tiers.
- Q: What depth of documentation should be provided for the new Architecture Health Check page in this initial implementation? → A: Option A: Full foundational method definition (covering Purpose, Relationship to Core EA SOP, 4 Health Dimensions, Assessment Phases, and Key Deliverables) matching the quality and structure of the other engagement methods.
- Q: In `mkdocs.yml`, should Stage 03 under "Core EA Practice" be labelled "Governance & Decision Enablement" or retain "03. Governance & Decision Framework"? → A: Option A: Label it "Governance & Decision Enablement" in navigation and align the page header in `docs/sop/03-governance-framework.md` to match.
- Q: Should the physical filenames under `docs/sop/methods/` remain as they are, or should illustrative reports be moved to `docs/sop/evidence/`? → A: Option A: Keep physical file paths as-is under `docs/sop/methods/` and structure them cleanly via `mkdocs.yml` navigation and the index page to prevent broken external links or cross-narrative regressions.

### Session 2026-09-18

- Q: How should the long linear Mermaid flows (e.g., in `docs/sop/index.md`) be restructured for legibility? → A: Option A: Restructure into multi-row folded flows or grouped stage subgraphs with wrapped text, combined with lightweight responsive container styling.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Structured Practice Exploration (Priority: P1)

As a portfolio visitor (enterprise architect, technology leader, or client), I want to view the Architecture SOP organised cleanly into three distinct domains—Core EA Practice, Engagement Methods, and Illustrative Evidence—so that I can quickly navigate between foundational operating lifecycle stages, specific advisory consulting methods, and illustrative deliverable artifacts.

**Why this priority**: Directly solves the conflation problem identified in the concept and problem definition, establishing a professional EA operating model hierarchy.

**Independent Test**: Can be tested by navigating the site menu in MkDocs preview and verifying that the three tiers appear under Architecture SOP with their corresponding child pages and links working without 404s.

**Acceptance Scenarios**:

1. **Given** a visitor browsing the Architecture SOP section, **When** they view the navigation menu, **Then** they see three clearly demarcated groups: "Core EA Practice", "Engagement Methods", and "Illustrative Evidence".
2. **Given** a visitor exploring "Core EA Practice", **When** they click any of the 5 practice stages, **Then** they are taken to the respective stage documentation (01 Discover & Align, 02 Target Architecture & Strategy, 03 Governance & Decision Enablement, 04 Delivery Enablement & Execution Steering, 05 Value Realisation & Organisational Handover).

---

### User Story 2 - Engagement Method and Health Check Discovery (Priority: P2)

As a technology leader looking for specific architectural interventions, I want to access four dedicated Engagement Methods (Architecture Decision Review, Architecture Assessment & Roadmap, Architecture Health Check, Architecture Automation Opportunity Assessment) so that I can evaluate concrete architectural methods that can be applied to targeted organisational problems.

**Why this priority**: Completes the engagement method portfolio by ensuring all four methods—including the Architecture Health Check—are available and structured systematically.

**Independent Test**: Can be tested by clicking on each of the 4 Engagement Methods in the navigation and verifying each page renders valid markdown, structured metadata, and clear method outlines.

**Acceptance Scenarios**:

1. **Given** a visitor looking for architectural review methods, **When** they navigate to "Engagement Methods", **Then** they can access Architecture Decision Review, Architecture Assessment & Roadmap, Architecture Health Check, and Architecture Automation Opportunity Assessment.
2. **Given** a visitor accessing Architecture Health Check, **When** the page loads, **Then** it presents the method's purpose, relationship to Core EA SOP, focus areas, and evaluation framework.

---

### User Story 3 - Examining Real-world Illustrative Deliverables (Priority: P3)

As a hiring manager or prospective advisory client, I want to examine sample deliverables under "Illustrative Evidence" (Decision Review report, Assessment & Transformation Roadmap report) separately from methodology descriptions, so that I can see concrete demonstration artifacts produced by these methods without confusing them with the methodology guides.

**Why this priority**: Separates "how to perform the method" from "what a sample deliverable looks like", preventing conceptual confusion.

**Independent Test**: Can be tested by navigating to "Illustrative Evidence" and opening both reports, confirming images, diagrams, and report sections render properly.

**Acceptance Scenarios**:

1. **Given** a user viewing "Illustrative Evidence", **When** they select "Decision Review report", **Then** they see the sample report deliverable for an AI document classification service decision.
2. **Given** a user viewing "Illustrative Evidence", **When** they select "Assessment & Transformation Roadmap report", **Then** they see the illustrative B2B services transformation assessment report.

---

### User Story 4 - Legible & Responsive Mermaid Architecture Diagrams (Priority: P1)

As a visitor exploring the Architecture SOP and methodology pages on any screen or viewport, I want Mermaid diagrams to display with crisp, legible typography and well-proportioned boxes without being scaled down to microscopic sizes, so that I can immediately read, understand, and trace the architectural flows.

**Why this priority**: Solves a direct visual defect where wide horizontal diagrams scale down excessively, hindering comprehension of the core methodology.

**Independent Test**: Can be tested by viewing `docs/sop/index.md` (Overview and Section 15) at 100% zoom on desktop and mobile viewports, verifying all node labels and text remain easily readable without zooming or text truncation.

**Acceptance Scenarios**:

1. **Given** a visitor viewing the Architecture SOP Overview page, **When** they look at the Strategy-to-Value lifecycle diagram and Section 15 Evidence Traceability diagram, **Then** the diagrams are structured as folded multi-row or grouped subgraph flows where typography is easily readable at 100% zoom.
2. **Given** a visitor viewing diagrams on mobile or narrow viewports, **When** a diagram exceeds the viewport width, **Then** the diagram container provides smooth horizontal scroll without shrinking node text below readable size.

---

### Edge Cases

- **Broken cross-references**: When existing pages or narratives link to `sop/methods/*.md` or `sop/03-governance-framework.md`, internal markdown links must remain valid or be cleanly updated.
- **Auxiliary pages positioning**: Existing auxiliary SOP documents (`sop/ai-augmented-architecture.md` and `sop/agent-architect-prompt.md`) must be appropriately positioned (e.g. within Core EA Practice or an AI Enablement subsection) without disrupting the 3 requested primary tiers.
- **Diagram theme contrast in dark/light mode**: Refactored subgraphs and custom styling must respect MkDocs Material slate and default color palettes without unreadable text contrast.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System navigation (`mkdocs.yml`) MUST structure the "Architecture SOP" section into three distinct groups:
  1. **Core EA Practice**:
     - Discover & Align (`sop/01-discover-align.md`)
     - Target Architecture & Strategy (`sop/02-target-architecture.md`)
     - Governance & Decision Enablement (`sop/03-governance-framework.md`)
     - Delivery Enablement & Execution Steering (`sop/04-delivery-enablement.md`)
     - Value Realisation & Organisational Handover (`sop/05-value-realisation-handover.md`)
  2. **Engagement Methods**:
     - Architecture Decision Review (`sop/methods/architecture-decision-review.md`)
     - Architecture Assessment & Roadmap (`sop/methods/architecture-assessment-and-roadmap.md`)
     - Architecture Health Check (`sop/methods/architecture-health-check.md`)
     - Architecture Automation Opportunity Assessment (`sop/methods/architecture-automation-opportunity-assessment.md`)
  3. **Illustrative Evidence**:
     - Decision Review report (`sop/methods/architecture-decision-review-report.v2.md`)
     - Assessment & Transformation Roadmap report (`sop/methods/architecture-assessment-roadmap-report.v2.md`)
  4. **AI Augmented Architecture**:
     - AI Augmented Workflows (`sop/ai-augmented-architecture.md`)
     - Agent Co-Pilot Prompt (`sop/agent-architect-prompt.md`)
- **FR-002**: System MUST provide a full foundational "Architecture Health Check" method document under `docs/sop/methods/architecture-health-check.md` consistent with existing engagement methods, specifying:
     - Method purpose, scope, and engagement triggers
     - Relationship and capability mapping to Core EA SOP (Stages 01–05)
     - Core health dimensions (e.g. strategic alignment, technical debt/sustainability, governance/operability, delivery friction)
     - Multi-phase assessment lifecycle (Scoping & Discovery → Evidence Gathering → Diagnostic Analysis → Findings & Action Plan)
     - Typical diagnostic outputs (Scorecards, Critical Risk Register, Priority Recommendations)
- **FR-003**: The SOP Overview landing page (`docs/sop/index.md`) MUST reflect this three-tier architecture in its text and stage/method diagrams.
- **FR-004**: Auxiliary AI pages MUST be housed under the dedicated "AI Augmented Architecture" sub-section directly adjacent to the primary tiers.
- **FR-005**: All relative markdown links and image paths between SOP documents, methods, and evidence reports MUST resolve cleanly without 404 errors.
- **FR-006**: Stage 03 documentation (`docs/sop/03-governance-framework.md`) title and headings MUST align to "Governance & Decision Enablement" matching the navigation label and `docs/sop/index.md`.
- **FR-007**: Wide horizontal Mermaid diagrams in `docs/sop/index.md` (Overview Strategy-to-Value chain, Section 15 Traceability chain, and Section 21 Architecture Loop) MUST be restructured into multi-row folded flows or logical subgraphs to prevent excessive scaling down and maintain legible text.
- **FR-008**: System MUST include a lightweight responsive CSS rule (e.g. via `docs/css/mermaid.css` registered in `mkdocs.yml` `extra_css`) ensuring Mermaid SVG containers maintain horizontal scrollability on narrow viewports without shrinking node text below readable body size.

### Key Entities

- **Core EA Practice Stage**: Foundational lifecycle stage (01 to 05) defining an enterprise architectural capability, its questions, inputs, and outputs.
- **Engagement Method**: A repeatable, bounded advisory engagement method selecting capabilities from the Core EA Practice for a specific client intervention.
- **Illustrative Evidence**: A concrete, sanitized sample report or deliverable illustrating the outputs of an Engagement Method.
- **Mermaid Architectural Flow**: Markdown-fenced diagram representing lifecycle, capability, or governance transitions.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of the three specified tiers and child items are present in `mkdocs.yml` navigation.
- **SC-002**: `mkdocs build --strict` executes with 0 warnings and 0 errors.
- **SC-003**: `python scripts/validate_governance.py` passes all terminology and structural checks.
- **SC-004**: All 4 engagement methods and 2 illustrative evidence reports render with functional internal anchors, links, and diagrams.
- **SC-005**: All Mermaid diagrams in `docs/sop/index.md` render node labels with clear, readable typography (equivalent to 12–14px body text) at 100% browser zoom without text truncation or microscopic scaling.

## Assumptions

- Source files under `docs/sop/methods/` can remain in their current directory or be logically grouped in navigation to prevent high-churn file renames and broken external incoming bookmarks.
- British English conventions apply across any new or updated headings and descriptions.
- The new Architecture Health Check method page will follow the established Engagement Method template (Purpose, Relationship to Core EA SOP, Framework, Outputs).
- Auxiliary AI pages (`ai-augmented-architecture.md` and `agent-architect-prompt.md`) can sit cleanly under an "AI Augmented Architecture" subsection or alongside Core EA Practice.
