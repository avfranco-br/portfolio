<!--
Sync Impact Report:
- Version change: Initial → 1.0.0
- List of modified principles:
    - [PRINCIPLE_1_NAME] → I. Documentation-First
    - [PRINCIPLE_2_NAME] → II. Specification-Driven Development (SDD)
    - [PRINCIPLE_3_NAME] → III. CAS Governance Operationalisation
    - [PRINCIPLE_4_NAME] → IV. Operational Simplicity & Sustainability
    - [PRINCIPLE_5_NAME] → V. Systems Thinking & Transparency
- Added sections: Technical Constraints, Development Workflow
- Removed sections: None
- Templates requiring updates:
    - ✅ .specify/templates/plan-template.md
    - ✅ .specify/templates/spec-template.md
    - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->

# Portfolio Constitution

## Core Principles

### I. Documentation-First
The portfolio is a "systems-first intelligence notebook". All content MUST be markdown-native, git-friendly, and lightweight. Avoid dynamic backend systems, heavy frontend frameworks, or custom CSS/JS bloat. Document the "why" and systemic context alongside the "what".

### II. Specification-Driven Development (SDD)
No feature implementation or structural change shall begin without a corresponding specification in `specs/`. All architectural decisions must be documented with rationale. Ground all changes in the approved blueprint.

### III. CAS Governance Operationalisation
Mandatory CAS Skills in `.cas/` MUST be used for all modifications. Use the appropriate skill (e.g., `cas-add-or-modify-feature`) before coding to ensure architectural alignment and pattern reuse.

### IV. Operational Simplicity & Sustainability
The system MUST be maintainable by a single person. Prioritise native MkDocs Material features over custom overrides. Avoid premature automation, dynamic backend APIs, and unnecessary platform sophistication.

### V. Systems Thinking & Transparency
Architecture is a tool for visibility and enterprise transformation (EA4All). Use Mermaid diagrams to illustrate systemic context, transformational states, and architectural flows. Maintain technical transparency throughout the repository.

## Technical Constraints

- **Stack**: MkDocs, MkDocs Material, GitHub Pages.
- **Architecture**: Static site generation only; no databases, headless CMS, or backend APIs.
- **Observability**: Focus on publication and clarity over tracking; no telemetry or analytics in Phase 1.
- **Visuals**: Professional, documentation-first aesthetics using theme defaults.

## Development Workflow

- **Lifecycle**: Strictly follow the Research -> Strategy -> Execution (Plan-Act-Validate) cycle.
- **Implementation**: Deliver changes in thin vertical slices; each increment must leave the system in a working, testable state.
- **Deployment**: Zero-touch deployment via GitHub Actions; commits to `main` automatically publish to GitHub Pages.

## Governance

- The Constitution is the foundational mandate for all project operations and supersedes all other practices.
- Amendments require a formal specification in `specs/`, user approval, and a semantic version bump.
- All code reviews and contributions must verify compliance with these principles.

**Version**: 1.0.0 | **Ratified**: 2026-05-16 | **Last Amended**: 2026-05-16
