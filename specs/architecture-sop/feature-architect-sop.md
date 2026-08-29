# Feature Specification: Enterprise Architecture SOP

**Feature Branch**: `feature/architect-sop-evolution`

**Created**: 2026-08-29

**Status**: Approved

**Input**: User request to evolve Architect SOP into an Enterprise Architecture Customer Engagement System: (1) Decoupled from mandatory SDLC/repo artifacts, (2) Structured around 5 customer engagement stages (Discover & Align, Target Architecture & Strategy, Governance & Decision Framework, Delivery Enablement & Execution Steering, Value Realisation & Organizational Handover), (3) Supporting 4 Engagement Archetypes (Strategic EA Assessment, Target Blueprint, Governance Model, Delivery Steering).

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Master SOP & Customer Engagement Stages (Priority: P1)

As an Enterprise Architect / AI Advisor or prospective client, I want to read a comprehensive Master SOP on the website detailing Alex's customer engagement methodology across all 5 stages and 4 engagement archetypes.

**Why this priority**: Core value proposition; establishes the single source of truth for the entire architecture consulting and operating model.

**Independent Test**: Navigating to `/sop/` renders the Master SOP overview and allows browsing each of the 5 stage guides (`01-discover-align` to `05-value-realisation-handover`), passing `mkdocs build --strict`.

**Acceptance Scenarios**:

1. **Given** a user visiting the site, **When** they click "Architecture SOP" in navigation, **Then** they see `docs/sop/index.md` introducing the 5 customer engagement stages and the 4 Engagement Archetypes.
2. **Given** a reader on stage `01-discover-align.md`, **When** reading the content, **Then** it details Strategy, Problem definition, Current State baseline assessment, Desired State (Intent) vision, and Domain diagnostic gap analysis.
3. **Given** a reader on stage `04-delivery-enablement.md`, **When** reading the content, **Then** it presents delivery enablement and execution steering fit for the customer's delivery model, positioning repo/code artifacts as optional depth tools for Archetype D engagements.

---

### User Story 2 - Agentic Co-Pilot Projection (Priority: P2)

As an AI coding agent or system architect LLM co-pilot, I want an explicit system prompt and schema document that encodes the SOP rules, enabling automated deconstruction of business use cases, engagement archetype selection, C4 diagram generation, and technology options evaluation.

**Why this priority**: Enables AI agents (like Antigravity / Gemini) to act as autonomous architectural co-pilots adhering strictly to Alex's engagement SOP.

**Independent Test**: Viewing `docs/sop/agent-architect-prompt.md` provides complete, structured system prompt instructions and output schemas.

**Acceptance Scenarios**:

1. **Given** an AI agent context, **When** loading `docs/sop/agent-architect-prompt.md`, **Then** the prompt contains step-by-step chain-of-thought rules for customer engagement triage, archetype selection, and target blueprint generation.

---

### User Story 3 - Site Navigation & Governance Integration (Priority: P3)

As a contributor or automated CI pipeline, I want the SOP pages to be integrated into `mkdocs.yml` navigation and verified via `scripts/run_governance.sh` to ensure zero broken links, clean terminology, and strict build integrity.

**Why this priority**: Maintains repository governance contract (`AGENTS.md`) and prevents drift.

**Independent Test**: Running `bash scripts/run_governance.sh` succeeds with zero errors and zero terminology warnings.

**Acceptance Scenarios**:

1. **Given** all `docs/sop/*.md` files exist and are referenced in `mkdocs.yml`, **When** `bash scripts/run_governance.sh` is executed, **Then** the build completes with exit code 0.

---

### Edge Cases

- What happens if an engagement is purely strategic (Archetype A)? The SOP guides the creation of high-level Strategy Maps and  Roadmaps without generating SDLC/code artifacts.
- How does the SOP handle hands-on delivery (Archetype D)? Code-level governance (ADR-as-Code, SDD, CI linters) is seamlessly enabled as an optional depth tier.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide `docs/sop/index.md` summarizing the 5 customer engagement stages and 4 Engagement Archetypes.
- **FR-002**: System MUST provide `docs/sop/01-discover-align.md` detailing Strategy, Problem, Current State assessment, Desired State (Intent), and Domain diagnostic gap analysis.
- **FR-003**: System MUST provide `docs/sop/02-target-architecture.md` detailing target architecture options, C4 models, vendor trade-offs, and technology pattern selection.
- **FR-004**: System MUST provide `docs/sop/03-governance-framework.md` detailing ADRs, NFR P0–P3 priorities, ARB setup, and compliance/guardrail rules.
- **FR-005**: System MUST provide `docs/sop/04-delivery-enablement.md` detailing execution steering,  roadmaps, delivery principles, and adaptive quality gates.
- **FR-006**: System MUST provide `docs/sop/05-value-realisation-handover.md` detailing operational readiness review, value realization assessment, and organizational handover.
- **FR-007**: System MUST provide `docs/sop/agent-architect-prompt.md` encoding the system architect co-pilot persona and step-by-step engagement CoT rules.
- **FR-008**: System MUST update `mkdocs.yml` to include the "Architecture SOP" section in site navigation.

### Success Criteria *(mandatory)*

- **SC-001**: 100% of the 5 engagement stages documented with clear rationale, inputs, activities, outputs, and archetype depth guidelines.
- **SC-002**: `bash scripts/run_governance.sh` executes cleanly with 0 build errors and 0 terminology warnings.
