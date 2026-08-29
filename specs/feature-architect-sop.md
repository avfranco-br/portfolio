# Feature Specification: Evolved Architect SOP & Projection Engine

**Feature Branch**: `feature/architect-sop-evolution`

**Created**: 2026-08-29

**Status**: Approved

**Input**: User request to refine Architect SOP: (1) Technology-agnostic (AI is an option, not a mandatory hammer), (2) Stage 01 must explicitly reflect Strategy, Problem, Current State assessment, and Desired State (Intent), (3) Stage 04 must be tool-agnostic delivery orchestration (decoupled from CAS product dependency).

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Master SOP Content & Technology-Agnostic 5-Stage Lifecycle (Priority: P1)

As an Enterprise Architect / AI Advisor or prospective client, I want to read a comprehensive, technology-agnostic Master SOP on the website detailing Alex's transformation methodology across all 5 stages.

**Why this priority**: Core value proposition; establishes the single source of truth for the entire architecture operating model.

**Independent Test**: Navigating to `/sop/` renders the Master SOP overview and allows browsing each of the 5 stage guides (`01-frame-align` to `05-evolve-observe`), passing `mkdocs build --strict`.

**Acceptance Scenarios**:

1. **Given** a user visiting the site, **When** they click "Architecture SOP" in navigation, **Then** they see `docs/sop/index.md` introducing the technology-agnostic 5-stage lifecycle.
2. **Given** a reader on stage `01-frame-align.md`, **When** reading the content, **Then** it details Strategy, Problem definition, Current State baseline assessment, Desired State (Intent) vision, and 10-Domain diagnostic gap analysis.
3. **Given** a reader on stage `02-architect-decouple.md`, **When** reading the content, **Then** it presents technology-agnostic option selection (traditional, event-driven, SaaS/COTS, or AI/Agentic where appropriate).
4. **Given** a reader on stage `04-operationalise-orchestrate.md`, **When** reading the content, **Then** it details tool-agnostic delivery orchestration and specification-driven execution.

---

### User Story 2 - Agentic Co-Pilot Projection (Priority: P2)

As an AI coding agent or system architect LLM co-pilot, I want an explicit system prompt and schema document that encodes the Master SOP rules, enabling automated deconstruction of business use cases, Current/Desired state assessment, C4 diagram generation, and technology-agnostic pattern selection.

**Why this priority**: Enables AI agents (like Antigravity / Gemini) to act as autonomous architectural co-pilots adhering strictly to Alex's SOP.

**Independent Test**: Viewing `docs/sop/agent-architect-prompt.md` provides complete, structured system prompt instructions and JSON/Markdown output schemas.

**Acceptance Scenarios**:

1. **Given** an AI agent context, **When** loading `docs/sop/agent-architect-prompt.md`, **Then** the prompt contains step-by-step chain-of-thought rules for Current/Desired state assessment, gap analysis, and technology-agnostic solution mapping.

---

### User Story 3 - Site Navigation & Continuous Governance Integration (Priority: P3)

As a contributor or automated CI pipeline, I want the SOP pages to be integrated into `mkdocs.yml` navigation and verified via `scripts/run_governance.sh` to ensure zero broken links, clean terminology, and strict build integrity.

**Why this priority**: Maintains repository governance contract (`AGENTS.md`) and prevents drift.

**Independent Test**: Running `bash scripts/run_governance.sh` succeeds with zero errors and zero terminology warnings.

**Acceptance Scenarios**:

1. **Given** all `docs/sop/*.md` files exist and are referenced in `mkdocs.yml`, **When** `bash scripts/run_governance.sh` is executed, **Then** the build completes with exit code 0.

---

### Edge Cases

- What happens if AI is not the right fit for a problem? The SOP explicitly mandates evaluating simpler, deterministic, or SaaS/COTS solutions first.
- How does stage 04 handle non-CAS delivery tools? The framework defines universal delivery principles (specs, thin slices, quality gates) compatible with any CI/CD toolchain.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide `docs/sop/index.md` summarizing the technology-agnostic 5-stage lifecycle.
- **FR-002**: System MUST provide `docs/sop/01-frame-align.md` detailing Strategy, Problem, Current State assessment, Desired State (Intent), and 10-domain diagnostic gap analysis.
- **FR-003**: System MUST provide `docs/sop/02-architect-decouple.md` detailing provider-agnostic abstractions, C4 models, and technology-agnostic pattern selection (microservices, event-driven, COTS, AI).
- **FR-004**: System MUST provide `docs/sop/03-govern-formalise.md` detailing ADRs as Code, NFR P0–P3 priorities, and governance guardrails.
- **FR-005**: System MUST provide `docs/sop/04-operationalise-orchestrate.md` detailing tool-agnostic delivery orchestration, specification-driven execution, and pipeline quality gates.
- **FR-006**: System MUST provide `docs/sop/05-evolve-observe.md` detailing operational & reasoning observability, feedback loops, and team handover.
- **FR-007**: System MUST provide `docs/sop/agent-architect-prompt.md` encoding the agentic system architect persona and step-by-step CoT rules.
- **FR-008**: System MUST update `mkdocs.yml` to include the "Architecture SOP" section in the site navigation.

### Success Criteria *(mandatory)*

- **SC-001**: 100% of the 5 stages documented with clear rationale, inputs, activities, outputs, and technology-agnostic practices.
- **SC-002**: `bash scripts/run_governance.sh` executes cleanly with 0 build errors and 0 terminology warnings.
