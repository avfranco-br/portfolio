# Phase 0: Research & Alignment

## Decision Log

### 1. Navigation Hierarchy & Material Theme Mapping
- **Decision**: Restructure `mkdocs.yml` under the `How I work` → `Architecture SOP` section into three explicit top-level sub-groups plus one auxiliary sub-group:
  - `Overview`: `sop/index.md`
  - `Core EA Practice`: Stages 01 to 05
  - `Engagement Methods`: 4 methods (Decision Review, Assessment & Roadmap, Health Check, Automation Opportunity Assessment)
  - `Illustrative Evidence`: 2 sample reports
  - `AI Augmented Architecture`: 2 AI pages
- **Rationale**: MkDocs Material supports nested navigation tabs and sections (`navigation.sections` enabled). This maps cleanly to the user's requested mental model without requiring custom CSS or theme hacking.
- **Alternatives Considered**: Flattening all methods and evidence directly into the root SOP navigation (rejected: causes clutter and fails to distinguish methods from deliverables); separating evidence into an external folder hierarchy (rejected: risks broken relative references and image links).

### 2. Architecture Health Check Method Design
- **Decision**: Author `docs/sop/methods/architecture-health-check.md` following the exact architectural conventions, headings, and classification notes of the other three engagement methods:
  - Frontmatter metadata (`title`, `description`, `tags`, `version: "1.0"`)
  - Purpose & Problem Triggers
  - Relationship to the Core EA SOP (mapping to Stages 01, 02, 03, 04, 05)
  - 4 Evaluation Dimensions: Strategic Alignment & Purpose, Architectural Integrity & Tech Debt, Operational Viability & Observability, Delivery Friction & Change Velocity
  - 4 Diagnostic Stages: Scoping & Setup → Evidence & Architecture Reconnaissance → Diagnostic Analysis & Health Scoring → Findings, Action Plan & Roadmapping
  - Concrete Diagnostic Deliverables (Architecture Health Scorecard, Critical Finding Register, 30-60-90 Day Remediation Plan)
- **Rationale**: Ensures complete parity with `architecture-decision-review.md`, `architecture-assessment-and-roadmap.md`, and `architecture-automation-opportunity-assessment.md`.
- **Alternatives Considered**: Creating a short stub page (rejected: user confirmed full foundational method scope during clarification).

### 3. Overview Landing Page (`docs/sop/index.md`) Modernisation
- **Decision**: Update Section 22 ("Relationship to Other Practice Areas") and overview narrative in `docs/sop/index.md` to reflect the three-tier taxonomy (Core Practice, Engagement Methods, Illustrative Evidence), updating the Mermaid diagram to clearly show how the SOP branches into the 4 Engagement Methods and connects to the Illustrative Evidence artifacts.
- **Rationale**: Keeps the landing page completely synchronized with the published navigation bar.
- **Alternatives Considered**: Leaving `index.md` unchanged (rejected: causes inconsistency between the menu and page text).

### 4. Stage 03 Terminology Standardisation
- **Decision**: Update `docs/sop/03-governance-framework.md` to establish "Governance & Decision Enablement" as the primary title and canonical concept, aligning with `docs/sop/index.md` and the navigation menu.
- **Rationale**: Eliminates lexical drift and ensures consistency across the portfolio.
