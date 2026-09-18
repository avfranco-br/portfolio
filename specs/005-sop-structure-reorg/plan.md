# Implementation Plan: Architecture SOP Structure Reorganisation

**Branch**: `005-sop-structure-reorg` | **Date**: 2026-09-17 | **Spec**: [spec.md](file:///Users/avfranco/GitHub/portfolio/specs/005-sop-structure-reorg/spec.md)

**Input**: Feature specification from `/specs/005-sop-structure-reorg/spec.md`

## Summary

Reorganise the Architecture SOP navigation and overview structure in the portfolio platform into three distinct, professional tiers (**Core EA Practice**, **Engagement Methods**, and **Illustrative Evidence**), complemented by an **AI Augmented Architecture** section. Add the missing **Architecture Health Check** engagement method (`docs/sop/methods/architecture-health-check.md`), align Stage 03 naming to "Governance & Decision Enablement", update the SOP index overview diagram and text to match, and refactor wide linear Mermaid diagrams in `docs/sop/index.md` into multi-row folded flows/subgraphs with responsive CSS styling (`docs/css/mermaid.css`) to guarantee typography legibility.

## Technical Context

**Language/Version**: Python 3.11 / Markdown / YAML / CSS  
**Primary Dependencies**: MkDocs, mkdocs-material, pymdown-extensions  
**Storage**: Static files (Markdown, CSS)  
**Testing**: pytest, `mkdocs build --strict`, `python scripts/validate_governance.py`  
**Target Platform**: GitHub Pages  
**Project Type**: Static documentation and architectural portfolio  
**Performance Goals**: Instant page loads, zero client-side hydration, pure static assets  
**Constraints**: Zero broken links, zero warnings under `mkdocs build --strict`, British English prose, compliance with CAS governance  
**Scale/Scope**: 1 configuration file (`mkdocs.yml`), 1 new method document (`docs/sop/methods/architecture-health-check.md`), 2 existing document updates (`docs/sop/index.md`, `docs/sop/03-governance-framework.md`), 1 new CSS stylesheet (`docs/css/mermaid.css`)  

## Constitution Check

| Principle | Gate | Status | Rationale |
| :--- | :--- | :--- | :--- |
| **I. Documentation-First** | Markdown-native, git-friendly, lightweight | PASS | Pure Markdown, YAML, and CSS changes; no dynamic bloat or external client libraries. |
| **II. Specification-Driven Development** | Spec in `specs/`, traceability | PASS | Governed by `specs/005-sop-structure-reorg/spec.md` with complete decision traceability. |
| **III. CAS Governance Operationalisation** | CAS skills and rules applied | PASS | CAS pattern `build-time-governance` and `contract-first-architecture` applied and verified. |
| **IV. Operational Simplicity & Sustainability** | Native MkDocs Material features | PASS | Uses standard native Material navigation grouping and CSS override conventions. |
| **V. Systems Thinking & Transparency** | Clear Mermaid diagrams and flows | PASS | Architecture SOP overview and traceability Mermaid diagrams restructured into legible, folded subgraphs to restore visual clarity. |

## CAS Skill Evaluation: `cas-add-or-modify-feature`

```yaml
output:
  feature:
    name: architecture-sop-structure-reorganisation
    module: docs/sop
    description: Restructure Architecture SOP into Core EA Practice, Engagement Methods, Illustrative Evidence, and AI Augmented Architecture tiers, and resolve Mermaid diagram legibility.

  decision:
    status: accepted
    reason: Directly addresses structural conflation and unreadable compressed diagrams across key landing pages.
    alternative: Heavy JS pan/zoom plugins (rejected: breaks static simplicity and print-readiness).

  code_changes:
    - file: mkdocs.yml
      change_type: modify
      summary: Update nav tree under How I work -> Architecture SOP to reflect the three-tier hierarchy and register docs/css/mermaid.css under extra_css.
    - file: docs/sop/methods/architecture-health-check.md
      change_type: create
      summary: Add foundational Architecture Health Check engagement method document.
    - file: docs/sop/index.md
      change_type: modify
      summary: Update Section 22 taxonomy and refactor wide horizontal Mermaid diagrams into multi-row folded flows.
    - file: docs/sop/03-governance-framework.md
      change_type: modify
      summary: Align title and header to "Governance & Decision Enablement".
    - file: docs/css/mermaid.css
      change_type: create
      summary: Add responsive container styling and horizontal scroll protection for Mermaid SVGs.

  architecture_decision:
    description: Group SOP items into three functional tiers and keep file paths stable.
    rationale: Preserves incoming URLs and cross-narrative links while creating clear conceptual hierarchy.
  
  architectural_impact:
    - affected_components:
        - mkdocs.yml
        - docs/sop/index.md
        - docs/sop/methods/architecture-health-check.md
        - docs/sop/03-governance-framework.md
      pattern_usage:
        - contract-first-architecture
        - build-time-governance
      pattern_justification: Explicit navigation contract prevents structural drift and strict build validates zero link-rot.

  risks:
    - description: Potential broken relative links in cross-referenced documentation.
      mitigation: Retain existing file paths under docs/sop/methods/ and run mkdocs build --strict.

  validation_notes:
    - description: Validated against .cas/rules/architecture_rules.md and verified strict build and governance script passes.
```

## Project Structure

### Documentation (this feature)

```text
specs/005-sop-structure-reorg/
├── checklists/
│   └── requirements.md
├── spec.md
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
└── contracts/
    └── nav-hierarchy-contract.md
```

### Source Code & Content Layout

```text
docs/
├── css/
│   └── mermaid.css                                       # Responsive container & typography styling for Mermaid SVGs
└── sop/
    ├── index.md                                          # Overview landing page & practice map
    ├── 01-discover-align.md                              # Core EA Practice Stage 01
    ├── 02-target-architecture.md                          # Core EA Practice Stage 02
    ├── 03-governance-framework.md                        # Core EA Practice Stage 03 (Governance & Decision Enablement)
    ├── 04-delivery-enablement.md                         # Core EA Practice Stage 04
    ├── 05-value-realisation-handover.md                  # Core EA Practice Stage 05
    ├── ai-augmented-architecture.md                      # AI Augmented Workflows
    ├── agent-architect-prompt.md                         # Agent Co-Pilot Prompt
    └── methods/
        ├── architecture-decision-review.md               # Engagement Method 1
        ├── architecture-assessment-and-roadmap.md        # Engagement Method 2
        ├── architecture-health-check.md                  # Engagement Method 3 (New)
        ├── architecture-automation-opportunity-assessment.md # Engagement Method 4
        ├── architecture-decision-review-report.v2.md     # Illustrative Evidence 1
        └── architecture-assessment-roadmap-report.v2.md  # Illustrative Evidence 2
```
