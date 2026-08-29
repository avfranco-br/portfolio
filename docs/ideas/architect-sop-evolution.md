# Architect SOP Evolution: Technology-Agnostic Transformation System

## Problem Statement
How Might We evolve Alex's Architect Standard Operating Procedure (SOP) into a technology-agnostic Enterprise Architecture methodology that connects Business Strategy, Current & Desired State Analysis, Governance, and Delivery Execution—providing a single source of truth from which multi-audience artifacts (Executive Briefs, Agent Co-pilot Prompts, and Engineering Governance) can be projected?

## Recommended Direction: Evolved 5-Stage Lifecycle & Projection Engine

### Core Lifecycle: The 5 Strategic Stages
1. **01. Frame & Align (Strategy, Baseline & Intent):** Understanding strategic goals, framing the problem, assessing the Current State, defining the Desired State (Intent), and executing gap analysis across 10 diagnostic domains.
2. **02. Architect & Decouple (Target Design & Abstractions):** Designing technology-agnostic system boundaries, establishing provider-agnostic abstractions, selecting target architectural patterns (traditional, event-driven, SaaS/COTS, or AI/Agentic where appropriate), and modeling C4 views.
3. **03. Govern & Formalise (Contracts, ADRs & Controls):** Authoring ADRs as Code, enforcing contract-first API/schema specifications, establishing P0–P3 NFR boundaries, and defining safety/compliance heuristics.
4. **04. Operationalise & Orchestrate (Delivery Execution & Quality Gates):** Driving tool-agnostic delivery orchestration via specification-driven execution, surgical slice implementation, and automated pipeline quality gates.
5. **05. Evolve & Observe (Observability, Continuous Improvement & Handover):** Implementing operational & reasoning observability, continuous improvement feedback loops, auditable health metrics, and empowering team ownership.

### Dynamic Projection Engine (Multi-Audience Output)
From the Master SOP, three target projections are derived:
- **Executive Projection:** 1-Page Business Value Bridge & 30/60/90 Transformation Roadmap.
- **Agentic Co-Pilot Projection:** System Architect Prompts, C4 template generators, and structured requirements mapping schemas.
- **Delivery & Governance Projection:** Automated policy linters, NFR assessment checklists, and CI/CD quality gate workflows.

## Key Assumptions to Validate
- [ ] The framework remains strictly technology-agnostic, recommending AI or traditional systems based on problem fit.
- [ ] Stage 01 cleanly bridges Current State baseline to Desired State vision without delaying early alignment.
- [ ] Delivery orchestration patterns apply universally regardless of whether teams use CAS, GitOps, or standard CI/CD pipelines.

## MVP Scope (Phase 1 Build)
- **Idea Blueprint:** `docs/ideas/architect-sop-evolution.md`
- **Master SOP Documentation:** `docs/sop/index.md` (Overview & technology-agnostic 5-stage lifecycle).
- **Stage Guides:** `docs/sop/01-frame-align.md` through `docs/sop/05-evolve-observe.md`.
- **Co-Pilot Schema:** `docs/sop/agent-architect-prompt.md` (System prompt for architectural co-pilots).
- **Site Integration:** Update `mkdocs.yml` navigation structure under "Architecture SOP".

## Not Doing (and Why)
- **Mandatory Technology Lock-In (AI-First Bias or Cloud Lock-In):** Technology selection is driven by problem fit, cost, and feasibility.
- **Tool-Specific Delivery Mandates:** Delivery orchestration is tool-agnostic (CAS, GitHub Actions, Jenkins, or Jira are supported delivery mechanisms).
- **Static Ivory-Tower EA Documents (PDF manuals):** Replaced entirely with repository-driven Markdown, code, and agent-accessible schemas.
