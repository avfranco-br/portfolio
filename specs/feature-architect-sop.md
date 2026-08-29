# Feature Specification: Evolved Architect SOP & Projection Engine

**Feature Branch**: `feature/architect-sop-evolution`

**Created**: 2026-08-29

**Status**: Approved

**Input**: User request to evolve Architect SOP into an end-to-end framework connecting Strategy, Architecture, Governance, Delivery, and AI based on Option A (5-stage lifecycle: Frame & Align, Architect & Decouple, Govern & Formalise, Operationalise & Orchestrate, Evolve & Observe).

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Master SOP Content & 5-Stage Lifecycle (Priority: P1)

As an Enterprise Architect / AI Advisor or prospective client, I want to read a comprehensive, structured Master SOP on the website that details Alex's end-to-end transformation methodology across all 5 stages.

**Why this priority**: Core value proposition; establishes the single source of truth for the entire architecture operating model.

**Independent Test**: Navigating to `/sop/` renders the Master SOP overview and allows browsing each of the 5 stage guides (`01-frame-align` to `05-evolve-observe`), passing `mkdocs build --strict`.

**Acceptance Scenarios**:

1. **Given** a user visiting the site, **When** they click "Architecture SOP" in navigation, **Then** they see `docs/sop/index.md` introducing the 5-stage strategic lifecycle.
2. **Given** a reader on stage `01-frame-align.md`, **When** reading the content, **Then** it details Strategy-to-Capability mapping, problem-first value framing, and the 10-Domain diagnostic triage (130+ NFR questions).
3. **Given** a reader on stage `03-govern-formalise.md`, **When** reading the content, **Then** it details ADRs as Code, AI safety guardrails, and P0-P3 risk prioritization.
4. **Given** a reader on stage `05-evolve-observe.md`, **When** reading the content, **Then** it details reasoning observability, LLM flywheels ("Beyond Evals"), and team empowerment.

---

### User Story 2 - Agentic Co-Pilot Projection (Priority: P2)

As an AI coding agent or system architect LLM co-pilot, I want an explicit system prompt and schema document that encodes the Master SOP rules, enabling automated deconstruction of business use cases, 10-domain NFR mapping, C4 diagram generation, and agentic pattern selection.

**Why this priority**: Enables AI agents (like Antigravity / Gemini) to act as autonomous architectural co-pilots adhering strictly to Alex's SOP.

**Independent Test**: Viewing `docs/sop/agent-architect-prompt.md` provides complete, structured system prompt instructions and JSON/Markdown output schemas.

**Acceptance Scenarios**:

1. **Given** an AI agent context, **When** loading `docs/sop/agent-architect-prompt.md`, **Then** the prompt contains step-by-step chain-of-thought rules for deconstructing use cases and mapping requirements to AI services and patterns.

---

### User Story 3 - Site Navigation & Continuous Governance Integration (Priority: P3)

As a contributor or automated CI pipeline, I want the SOP pages to be integrated into `mkdocs.yml` navigation and verified via `scripts/run_governance.sh` to ensure zero broken links, clean terminology, and strict build integrity.

**Why this priority**: Maintains repository governance contract (`AGENTS.md`) and prevents drift.

**Independent Test**: Running `bash scripts/run_governance.sh` succeeds with zero errors and zero terminology warnings.

**Acceptance Scenarios**:

1. **Given** all `docs/sop/*.md` files exist and are referenced in `mkdocs.yml`, **When** `bash scripts/run_governance.sh` is executed, **Then** the build completes with exit code 0.

---

### Edge Cases

- What happens if a terminology check finds uncanonical terms (e.g. `AI-native` instead of `AI native`)? Validator flags it and build output guides correction.
- How does MkDocs handle navigation order? Explicit nav entries under `Architecture SOP` maintain strict 01 to 05 sequence.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide `docs/sop/index.md` summarizing the 5-stage lifecycle.
- **FR-002**: System MUST provide `docs/sop/01-frame-align.md` detailing strategy framing, capability maps, and 10-domain diagnostic triage.
- **FR-003**: System MUST provide `docs/sop/02-architect-decouple.md` detailing provider-agnostic abstractions, C4 models, and agentic pattern selection.
- **FR-004**: System MUST provide `docs/sop/03-govern-formalise.md` detailing ADRs as Code, NFR P0–P3 priorities, and AI guardrail safety heuristics.
- **FR-005**: System MUST provide `docs/sop/04-operationalise-orchestrate.md` detailing the Continuous Architecture System (CAS), surgical slices, and build validation.
- **FR-006**: System MUST provide `docs/sop/05-evolve-observe.md` detailing reasoning observability, improvement flywheels ("Beyond Evals"), and operational handover.
- **FR-007**: System MUST provide `docs/sop/agent-architect-prompt.md` encoding the agentic system architect persona and step-by-step CoT rules.
- **FR-008**: System MUST update `mkdocs.yml` to include the "Architecture SOP" section in the site navigation.

### Key Entities

- **Stage Guide**: A Markdown document defining one of the 5 strategic stages.
- **Co-Pilot Prompt**: A system prompt document usable by LLMs/Agents to execute SOP-driven architectural analysis.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of the 5 stages documented with clear rationale, inputs, activities, outputs, and AI enablement practices.
- **SC-002**: `bash scripts/run_governance.sh` executes cleanly with 0 build errors and 0 terminology warnings.
- **SC-003**: All pages rendered correctly in MkDocs Material theme preview.

## Assumptions

- Canonical terms follow `governance/terminology.yaml` rules (hyphen-free: `AI native`, `governance aware`, `coding agent`, `multi agent`).
- Content draws from existing `AI-Architecture-Enablement`, `docs/about.md`, `docs/how-i-work.md`, and `Certifications.csv`.
