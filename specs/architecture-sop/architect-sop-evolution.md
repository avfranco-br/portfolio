# Architect SOP Evolution: Enterprise Architecture Customer Engagement System

## Problem Statement
How Might We frame Alex's Architect SOP as an Engagement-Adaptive Enterprise Architecture Operating Model—one that governs how an Enterprise Architect engages with customers from strategic alignment through to value realization, scaling deliverable depth across 4 engagement archetypes without forcing software development (SDLC) artifacts onto non-engineering engagements?

## Recommended Direction: Customer Engagement Lifecycle & Archetype Matrix

### Core Lifecycle: The 5 Strategic Customer Engagement Stages
1. **01. Discover & Align (Strategy, Context & Baseline Assessment):** Understanding customer strategy, business drivers, problem statement, desired state intent, assessing current state baseline (capabilities, technical debt), and executing Domain diagnostic gap analysis.
2. **02. Target Architecture & Strategy (Options, Blueprint & Trade-offs):** Formulating target architecture options (COTS, Cloud, Microservices, AI/Agentic), evaluating technology/vendor trade-offs, designing C4 models, and creating the Target Architecture Blueprint.
3. **03. Governance & Decision Framework (Controls, Guardrails & Standards):** Establishing governance fit for customer context—whether Executive ADRs, Architecture Review Board (ARB) processes, NFR priorities (P0–P3), compliance rules, or (when applicable) repository-based ADRs.
4. **04. Delivery Enablement & Execution Steering (Roadmap & Delivery Guidance):** Translating target architecture into an actionable execution roadmap ( days), defining delivery principles, empowering delivery teams, and setting up quality gates appropriate for the customer's delivery model (Agile, SAFe, GitOps, SDD).
5. **05. Value Realisation & Organizational Handover (Impact & Enablement):** Assessing operational readiness, verifying value realization against Stage 01 business goals, establishing continuous improvement feedback loops, and executing structured organizational handover.

### Engagement Archetype Matrix (Adaptive SOP Depth)
The Master SOP defines 4 Engagement Archetypes to match customer mandates:
- **Archetype A: Strategic EA Assessment:** High-level Strategy, Current State Audit, Gap Analysis, and  Transformation Roadmap.
- **Archetype B: Target Architecture Blueprint:** Desired State Vision, Technology Options, C4 Models, Vendor Trade-offs, and Architecture Specifications.
- **Archetype C: Enterprise Governance & Operating Model:** Governance Framework, ARB Setup, Guardrails, Risk & NFR Priority Matrix.
- **Archetype D: Delivery Steering & Implementation (Ongoing / Sprints):** Hands-on Architecture, Architecture-as-Code, SDD, CI/CD Quality Gates, and Repository Governance.

### Dynamic Projection Engine (Multi-Audience Output)
- **Executive Projection:** 1-Page Business Value Bridge &  Strategic Transformation Roadmap.
- **Agentic Co-Pilot Projection:** System Architect Prompts (`agent-architect-prompt.md`) and JSON schemas enabling AI coding agents to execute automated architectural analysis and C4 generation.
- **Delivery & Governance Projection:** Governance charters, ARB checklists, NFR assessment matrices, and CI/CD quality gate workflows.

## Key Assumptions to Validate
- [ ] The 5 engagement stages cleanly accommodate both high-level advisory and deep delivery engagements.
- [ ] Deliverables scale dynamically based on the selected Engagement Archetype (A, B, C, or D).
- [ ] Implementation artifacts (ADR-as-Code, SDD, Telemetry) are presented as optional depth tools for Archetype D.

## MVP Scope (Phase 1 Build)
- **Idea Blueprint:** `docs/ideas/architect-sop-evolution.md`
- **Master SOP Documentation:** `docs/sop/index.md` (Overview & Engagement Lifecycle).
- **Stage Guides:** `docs/sop/01-discover-align.md` through `docs/sop/05-value-realisation-handover.md`.
- **Co-Pilot Schema:** `docs/sop/agent-architect-prompt.md` (System prompt for architectural co-pilots).
- **Site Integration:** Update `mkdocs.yml` navigation structure under "Architecture SOP".

## Not Doing (and Why)
- **Forcing SDLC Artifacts on All Engagements:** Code repos, linters, and telemetry pipelines apply only to Archetype D (Delivery Steering).
- **Mandatory Technology Lock-In (AI-First Bias or Cloud Lock-In):** Technology selection is driven by problem fit, cost, and feasibility.
- **Static Ivory-Tower EA Documents (PDF manuals):** Replaced entirely with living Markdown, modular templates, and agent-accessible schemas.
