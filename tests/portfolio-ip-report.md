# Intellectual Property Assessment Report

## portfolio Analysis — Documentation & Governance Scope

**Assessment Date**: `2026-08-29`  
**Scope**: `docs/`, `governance/`, `specs/` (Documentation & Governance Content)  
**Assessor**: `AI System Architect & IP Assessment Review`  
**Classification Level**: `CONFIDENTIAL - INTERNAL USE ONLY`  
**Brand Context**: `© 2026 Alexandre Franco. Ideas-to-Life. All rights reserved.`  

---

## Executive Summary

This report delivers a thorough Intellectual Property (IP), Data Classification, and Security Assessment for the **portfolio** platform (covering the target scope: `docs/`, `governance/`, and `specs/`). The target repository is an MkDocs-based enterprise architecture portfolio and publishing platform designed to showcase executive leadership, the Continuous Architecture System (CAS), agentic co-pilot frameworks, standard operating procedures, and technical architecture specifications.

### Key Findings

- **Proprietary Assets (Category 1 🔴 / Category 2 🟡)**: 
  - The **Continuous Architecture System (CAS)** dual-governance model ([docs/narratives/cas.md](file:///Users/avfranco/GitHub/portfolio/docs/narratives/cas.md#L19-L36)).
  - The **Agentic System Architect Co-Pilot System Prompt & Schema** ([docs/sop/agent-architect-prompt.md](file:///Users/avfranco/GitHub/portfolio/docs/sop/agent-architect-prompt.md#L23-L121)).
  - Custom architecture SOP workflows ([docs/sop/01-discover-align.md](file:///Users/avfranco/GitHub/portfolio/docs/sop/01-discover-align.md) through [05-value-realisation-handover.md](file:///Users/avfranco/GitHub/portfolio/docs/sop/05-value-realisation-handover.md)).
  - The custom corporate governance terminology policy ([governance/terminology.yaml](file:///Users/avfranco/GitHub/portfolio/governance/terminology.yaml#L1-L17)).
  - Strategic technical blog posts covering deterministic delta extraction, claim linting, and four-layer agentic pipelines ([docs/tech-blog/posts/](file:///Users/avfranco/GitHub/portfolio/docs/tech-blog/posts)).
- **Sensitive Information (❗)**: 
  - Personal work email address (`alexandre.franco@mostelli.com`) and direct Google Calendar booking link exposed in public Markdown ([docs/contact.md](file:///Users/avfranco/GitHub/portfolio/docs/contact.md#L29-L30)).
  - Proprietary client transformation strategies and operating models for named enterprise clients (BAT and BBC Studios) ([docs/narratives/bat-transformation.md](file:///Users/avfranco/GitHub/portfolio/docs/narratives/bat-transformation.md#L30-L39), [docs/narratives/bbc-studios-digital-evolution.md](file:///Users/avfranco/GitHub/portfolio/docs/narratives/bbc-studios-digital-evolution.md)).
- **Generic & Open-Source Patterns (Category 3 🟢)**: 
  - MkDocs site layouts, standard C4 / Mermaid diagram syntax ([docs/sop/agent-architect-prompt.md](file:///Users/avfranco/GitHub/portfolio/docs/sop/agent-architect-prompt.md#L97-L100)), boilerplate Speckit contracts, and standard markdown schemas in `specs/`.
- **Security Posture (⚠️)**: 
  - Overall strong static posture. Cloudflare Web Analytics beacon script ([docs/js/cloudflare-insights.js](file:///Users/avfranco/GitHub/portfolio/docs/js/cloudflare-insights.js#L9)) contains an unpopulated placeholder token (`YOUR_BEACON_TOKEN_HERE`), preventing tracking until populated. No hardcoded API keys or private credentials were found in the inspected scope.

---

## 1. Per-Module / Per-File Deep Dive

### 1.1 `docs/sop/` (Standard Operating Procedures & Agent Prompts)

- **IP Classification**: 🔴 **HIGHLY PROPRIETARY**
- **Proprietary Elements (✅)**: 
  - The complete 5-stage Enterprise Architecture Operating Model ([docs/sop/01-discover-align.md](file:///Users/avfranco/GitHub/portfolio/docs/sop/01-discover-align.md) to [05-value-realisation-handover.md](file:///Users/avfranco/GitHub/portfolio/docs/sop/05-value-realisation-handover.md)).
  - The canonical **Agentic System Architect Co-Pilot System Prompt** ([docs/sop/agent-architect-prompt.md](file:///Users/avfranco/GitHub/portfolio/docs/sop/agent-architect-prompt.md#L23-L121)), including 4 engagement archetypes (A: Strategic EA, B: Target Architecture Blueprint, C: Governance & Operating Model, D: Delivery Steering) and structured chain-of-thought instructions.
  - AI-augmented architecture operating model ([docs/sop/ai-augmented-architecture.md](file:///Users/avfranco/GitHub/portfolio/docs/sop/ai-augmented-architecture.md)).
- **Sensitive Information (❗)**: Detailed methodology revealing proprietary consulting tradecraft, framework mechanics, and delivery strategies.
- **Security Status (⚠️)**: Publicly readable; if intended as exclusive commercial IP, requires access control or copyright protection.
- **Generic Elements (ℹ️)**: Basic C4 diagram structure and standard ADR template structure.
- **Risk Level**: **HIGH** (High IP value, accessible open-access via public repo/site).

---

### 1.2 `docs/narratives/` (Executive Case Studies & Strategic Narratives)

- **IP Classification**: 🟡 **CONTEXTUALIZED GENERIC / INTERNAL**
- **Proprietary Elements (✅)**: 
  - Theoretical framework for **Continuous Architecture System (CAS)** ([docs/narratives/cas.md](file:///Users/avfranco/GitHub/portfolio/docs/narratives/cas.md#L19-L36)).
  - **CAS Coding Agent Collaboration** framework ([docs/narratives/cas-coding-agent-collaboration.md](file:///Users/avfranco/GitHub/portfolio/docs/narratives/cas-coding-agent-collaboration.md)).
  - **EA4ALL** (Democratising Architectural Intelligence) narrative ([docs/narratives/ea4all.md](file:///Users/avfranco/GitHub/portfolio/docs/narratives/ea4all.md)).
  - **Runner Agentic Intelligence** case study ([docs/narratives/runner-agentic-intelligence.md](file:///Users/avfranco/GitHub/portfolio/docs/narratives/runner-agentic-intelligence.md)).
- **Sensitive Information (❗)**: 
  - Explicit client names and global transformation details: British American Tobacco ([docs/narratives/bat-transformation.md](file:///Users/avfranco/GitHub/portfolio/docs/narratives/bat-transformation.md#L1-L7)) and BBC Studios ([docs/narratives/bbc-studios-digital-evolution.md](file:///Users/avfranco/GitHub/portfolio/docs/narratives/bbc-studios-digital-evolution.md#L1-L7)).
- **Security Status (⚠️)**: Ensure public disclosure of client case studies complies with non-disclosure agreements (NDAs) and client confidentiality guidelines.
- **Generic Elements (ℹ️)**: High-level Industry standard transformation challenges (agile vs governance, technical debt).
- **Risk Level**: **MEDIUM** (Public exposure risk if client names/details are bound by strict NDAs).

---

### 1.3 `governance/` (Corporate & Repository Governance Rules)

- **IP Classification**: 🟡 **CONTEXTUALIZED GENERIC**
- **Proprietary Elements (✅)**: 
  - Standardized corporate terminology enforcement schema ([governance/terminology.yaml](file:///Users/avfranco/GitHub/portfolio/governance/terminology.yaml#L1-L17)) enforcing canonical terms (`AI native`, `coding agent`, `operational intelligence`, `governance aware`, `architecture operationalisation`).
- **Sensitive Information (❗)**: Internal operational rules and taxonomy preferences.
- **Security Status (⚠️)**: Clean. No secrets or credentials.
- **Generic Elements (ℹ️)**: YAML schema format and git-based linting principles.
- **Risk Level**: **LOW** (Safe for internal and controlled public publication).

---

### 1.4 `docs/tech-blog/` (Technical Architecture Posts)

- **IP Classification**: 🟡 **CONTEXTUALIZED GENERIC / PUBLIC**
- **Proprietary Elements (✅)**: 
  - Articles detailing technical innovations:
    - *Decoupling Git Diff Parsing from Architecture Evaluation* ([docs/tech-blog/posts/2026-05-17-decoupling-git-diff-parsing-architecture-evaluation.md](file:///Users/avfranco/GitHub/portfolio/docs/tech-blog/posts/2026-05-17-decoupling-git-diff-parsing-architecture-evaluation.md))
    - *Deterministic Delta Extraction Before Semantic AI Analysis* ([docs/tech-blog/posts/2026-05-17-deterministic-delta-extraction-before-semantic-ai-analysis.md](file:///Users/avfranco/GitHub/portfolio/docs/tech-blog/posts/2026-05-17-deterministic-delta-extraction-before-semantic-ai-analysis.md))
    - *Preventing Generative Over-Claiming with Claim Linting* ([docs/tech-blog/posts/2026-08-07-preventing-generative-over-claiming-with-claim-linting.md](file:///Users/avfranco/GitHub/portfolio/docs/tech-blog/posts/2026-08-07-preventing-generative-over-claiming-with-claim-linting.md))
    - *Four-Layer Agentic Pipeline Architecture* ([docs/tech-blog/posts/2026-08-08-four-layer-agentic-pipeline-architecture.md](file:///Users/avfranco/GitHub/portfolio/docs/tech-blog/posts/2026-08-08-four-layer-agentic-pipeline-architecture.md))
- **Sensitive Information (❗)**: Methodological IP on preventing LLM hallucination and claim verification.
- **Security Status (⚠️)**: Intended for public marketing/thought-leadership.
- **Generic Elements (ℹ️)**: General AI engineering concepts, git diff fundamentals.
- **Risk Level**: **LOW** (Designed for public dissemination).

---

### 1.5 `specs/` (Feature Specifications & Architectural Plans)

- **IP Classification**: 🟡 **CONTEXTUALIZED GENERIC / INTERNAL**
- **Proprietary Elements (✅)**: 
  - Architectural blueprints for portfolio features ([specs/001-portfolio-restructure/spec.md](file:///Users/avfranco/GitHub/portfolio/specs/001-portfolio-restructure/spec.md)).
  - Tech Blog approval status and draft publishing contracts ([specs/002-tech-blog-approval-status/spec.md](file:///Users/avfranco/GitHub/portfolio/specs/002-tech-blog-approval-status/spec.md)).
  - Architecture SOP evolution blueprints ([specs/architecture-sop/architect-sop-evolution.md](file:///Users/avfranco/GitHub/portfolio/specs/architecture-sop/architect-sop-evolution.md)).
- **Sensitive Information (❗)**: Internal product roadmap, pending unreleased features, design trade-offs.
- **Security Status (⚠️)**: Public visibility reveals internal technical strategy and roadmap velocity.
- **Generic Elements (ℹ️)**: Speckit templates, standard data models, checklist schemas.
- **Risk Level**: **MEDIUM** (Exposes internal engineering roadmap and draft concepts).

---

### 1.6 `docs/` core pages & `docs/js/` (Site Shell & Client Scripts)

- **IP Classification**: 🟢 **GENERIC / PUBLIC**
- **Proprietary Elements (✅)**: Personal brand messaging and executive profile ([docs/about.md](file:///Users/avfranco/GitHub/portfolio/docs/about.md), [docs/index.md](file:///Users/avfranco/GitHub/portfolio/docs/index.md)).
- **Sensitive Information (❗)**: Direct corporate email `alexandre.franco@mostelli.com` ([docs/contact.md:L29](file:///Users/avfranco/GitHub/portfolio/docs/contact.md#L29)) and calendar link `https://calendar.app.google/1cKarCCmCoNExvov7` ([docs/contact.md:L30](file:///Users/avfranco/GitHub/portfolio/docs/contact.md#L30)).
- **Security Status (⚠️)**: `docs/js/cloudflare-insights.js` line 9 contains `"token": "YOUR_BEACON_TOKEN_HERE"`. No security risk, but script fails silently with 404 until real token is inserted.
- **Generic Elements (ℹ️)**: Cloudflare web analytics snippet, standard MkDocs metadata.
- **Risk Level**: **LOW**.

---

## 2. IP Categories Summary

### 🔴 Category 1: Highly Proprietary Content
- **Files Included**:
  - `docs/sop/agent-architect-prompt.md`
  - `docs/sop/01-discover-align.md` through `05-value-realisation-handover.md`
  - `docs/sop/ai-augmented-architecture.md`
  - `docs/narratives/cas.md`
  - `docs/narratives/cas-coding-agent-collaboration.md`
- **Contents Summary**: Proprietary Enterprise Architecture operational prompts, 5-stage SOP methodologies, CAS dual-governance model, and coding agent orchestration frameworks.
- **Protection & Safeguards Required**: Explicit copyright header (`© 2026 Alexandre Franco. Ideas-to-Life. All rights reserved.`), trade secret protection if commercialized, or clear open-source license specification if shared.

### 🟡 Category 2: Contextualized Generic Content
- **Files Included**:
  - `docs/narratives/bat-transformation.md`
  - `docs/narratives/bbc-studios-digital-evolution.md`
  - `docs/narratives/ea4all.md`
  - `docs/narratives/runner-agentic-intelligence.md`
  - `governance/terminology.yaml`
  - `docs/tech-blog/posts/*.md`
  - All feature specifications under `specs/`
- **Contents Summary**: Client case studies, domain-specific terminology rules, technical blog articles, and feature specifications.
- **Protection & Safeguards Required**: Verify NDA compliance for named client narratives (BAT, BBC Studios). Ensure frontmatter approval workflow is enforced before blog publishing.

### 🟢 Category 3: Generic Tools & Reference Assets
- **Files Included**:
  - `docs/index.md`, `docs/about.md`, `docs/contact.md`, `docs/architecture-philosophy.md`
  - `docs/js/cloudflare-insights.js`
  - `docs/assets/**` (headshot, favicons, PDF CV)
  - `specs/001-portfolio-restructure/contracts/*` (standard markdown contracts)
- **Contents Summary**: Public marketing pages, static assets, generic JavaScript snippets, standard markdown schemas.
- **Protection & Safeguards Required**: Standard public web hosting protection; keep asset metadata clean.

---

## 3. Security & Compliance Assessment

### Current Security Posture

1. **Secrets & Credentials**: Inspecting `docs/`, `governance/`, and `specs/` revealed **zero exposed private API keys, passwords, or authentication tokens**.
2. **Client-Side Scripts**: `docs/js/cloudflare-insights.js` uses an unpopulated placeholder token `YOUR_BEACON_TOKEN_HERE` ([docs/js/cloudflare-insights.js#L9](file:///Users/avfranco/GitHub/portfolio/docs/js/cloudflare-insights.js#L9)), which prevents tracking errors or privacy leaks.
3. **Data Exposure**: Personal email address `alexandre.franco@mostelli.com` and Google Calendar appointment link are published in plaintext ([docs/contact.md#L29-L30](file:///Users/avfranco/GitHub/portfolio/docs/contact.md#L29-L30)), which exposes the owner to potential email harvesting or calendar spam.
4. **Client Confidentiality**: Narrative files cite specific corporate entities (BAT, BBC Studios). If these case studies contain confidential transformation details, they could pose a compliance risk under enterprise NDAs.

### Recommended Security & Governance Enhancements

#### Immediate (High Priority)
- **NDA & Client Name Review**: Audit [docs/narratives/bat-transformation.md](file:///Users/avfranco/GitHub/portfolio/docs/narratives/bat-transformation.md) and [docs/narratives/bbc-studios-digital-evolution.md](file:///Users/avfranco/GitHub/portfolio/docs/narratives/bbc-studios-digital-evolution.md) against active non-disclosure agreements. Anonymize client names to industry descriptors (e.g. "Global FMCG Enterprise", "Major Public Broadcaster") if required by NDA terms.
- **Cloudflare Beacon Token**: Replace `YOUR_BEACON_TOKEN_HERE` in [docs/js/cloudflare-insights.js](file:///Users/avfranco/GitHub/portfolio/docs/js/cloudflare-insights.js#L9) with the actual token or manage via build-time environment variable injection.

#### Short-term (Medium Priority)
- **Spam Guarding on Contact Page**: Obfuscate `alexandre.franco@mostelli.com` in [docs/contact.md](file:///Users/avfranco/GitHub/portfolio/docs/contact.md#L29) or replace with a contact form endpoint to mitigate automated scraping.
- **Explicit License & Copyright Notices**: Add explicit copyright notices (`© 2026 Alexandre Franco. Ideas-to-Life. All rights reserved.`) to all Category 1 SOP files under `docs/sop/`.

#### Long-term (Strategic)
- **IP Watermarking & Publishing Pipeline**: Implement an automated pre-publish CI check in `.github/workflows/` that validates post approval status (per [specs/002-tech-blog-approval-status/spec.md](file:///Users/avfranco/GitHub/portfolio/specs/002-tech-blog-approval-status/spec.md)) and scans for sensitive internal references prior to GitHub Pages deployment.

---

## 4. Data Classification Summary

| Classification Level | Scope / Files Included | Access Control & Handling |
| :--- | :--- | :--- |
| 🌐 **PUBLIC** | `docs/index.md`, `docs/about.md`, `docs/contact.md`, `docs/tech-blog/posts/*.md`, `docs/assets/**` | Unrestricted public web distribution via GitHub Pages. |
| 🏢 **INTERNAL** | `governance/terminology.yaml`, `specs/**`, `docs/architecture-philosophy.md` | Internal team and repository contributors. Exposes product roadmap & standards. |
| 🔒 **CONFIDENTIAL** | `docs/narratives/bat-transformation.md`, `docs/narratives/bbc-studios-digital-evolution.md` | Restricted visibility subject to client NDA and trade secrecy verification. |
| 🔴 **RESTRICTED / HIGHLY CONFIDENTIAL** | `docs/sop/agent-architect-prompt.md`, `docs/sop/*.md`, `docs/narratives/cas.md` | Core IP & proprietary methodology. Requires explicit copyright protection & licensing strategy. |

---

## 5. Legal & Compliance Considerations

### Intellectual Property Ownership
- All original frameworks, prompt engineering structures, SOP steps, CAS methodology documents, and narrative prose in `docs/` and `specs/` represent original intellectual property owned outright by **Alexandre Franco / Ideas-to-Life** (`© 2026 Alexandre Franco. Ideas-to-Life. All rights reserved.`).

### Third-Party Dependencies & Attribution
- **MkDocs & Material for MkDocs**: Used as the site generator and theme under BSD / MIT licenses. Compliance is satisfied via standard dependency declarations in `requirements.txt`.
- **Mermaid.js**: Used for rendering target architecture diagrams ([docs/sop/agent-architect-prompt.md#L97-L100](file:///Users/avfranco/GitHub/portfolio/docs/sop/agent-architect-prompt.md#L97-L100)). Standard MIT open-source usage.

### Legal Recommendations
1. **Copyright Notice Addition**: Standardize copyright notices across all documentation files to clearly establish ownership:
   `© 2026 Alexandre Franco. Ideas-to-Life. All rights reserved.`
2. **License Declaration**: Add an explicit `LICENSE` file or section clarifying permissible use of the SOP prompts (e.g. Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 or proprietary license).

---

## 6. Recommendations by Stakeholder Role

| Stakeholder Role | Immediate Actions (P0/P1) | Short-Term Roadmap (P2) | Strategic Objectives (P3) |
| :--- | :--- | :--- | :--- |
| **Repository / Project Owner** | Audit named client case studies (BAT, BBC Studios) for NDA compliance. | Standardize copyright footers across `docs/sop/` and `docs/narratives/`. | Establish clear licensing model for the Agent Architect Co-Pilot prompt. |
| **Legal & Compliance** | Verify client narrative authorization & NDA boundaries. | Draft clear usage terms for open repository content vs commercial IP. | Register trademarks or formal IP rights for "Continuous Architecture System (CAS)" if desired. |
| **Information Security** | Obfuscate contact email address to prevent scraping. | Inject Cloudflare beacon token securely via build environment variables. | Integrate automated secrets and PII scanning into CI workflow. |
| **Architecture Leadership** | Enforce governance terminology linters in `governance/terminology.yaml`. | Operationalize the blog draft approval contract in `specs/002-tech-blog-approval-status/`. | Scale CAS dual-governance model for external client engagements. |

---

## 7. Risk Matrix Table

| Content Category | Exposure Risk | Business Impact | Recommended Action |
| :--- | :--- | :--- | :--- |
| **SOP & Agent Prompt IP** (`docs/sop/`) | **HIGH** | **HIGH** | Add explicit copyright notices (`© 2026 Alexandre Franco. Ideas-to-Life.`); formalize commercial vs open-source licensing. |
| **Client Narratives** (`docs/narratives/bat-*, bbc-*`) | **MEDIUM** | **HIGH** | Audit against client NDAs; sanitize brand names if authorization is not on file. |
| **Feature Specs & Roadmap** (`specs/`) | **MEDIUM** | **LOW** | Keep under internal review; avoid committing sensitive unannounced feature details. |
| **Public Thought Leadership** (`docs/tech-blog/`) | **LOW** | **LOW** | Safe for public publication; enforce frontmatter approval linter. |
| **Client Analytics Script** (`docs/js/cloudflare-insights.js`) | **LOW** | **LOW** | Replace placeholder token `YOUR_BEACON_TOKEN_HERE` with valid Cloudflare analytics token. |

---

## 8. Conclusion & Value Proposition

The assessed scope (`docs/`, `governance/`, `specs/`) contains significant high-value intellectual property, most notably the **Agentic System Architect Co-Pilot framework**, the **Continuous Architecture System (CAS)** dual-governance model, and structured Enterprise Architecture Standard Operating Procedures.

By formalizing IP safeguards—specifically adding explicit copyright notices, verifying client NDA boundaries for narratives, and enforcing governance linters—the platform can safely balance **public thought-leadership visibility** with **robust protection of proprietary architecture methodologies**.

---

## Appendix: File Inventory

### High-Risk Files (Restricted / Proprietary — Category 1 🔴)
- `docs/sop/agent-architect-prompt.md`
- `docs/sop/01-discover-align.md`
- `docs/sop/02-target-architecture.md`
- `docs/sop/03-governance-framework.md`
- `docs/sop/04-delivery-enablement.md`
- `docs/sop/05-value-realisation-handover.md`
- `docs/sop/ai-augmented-architecture.md`
- `docs/sop/index.md`
- `docs/narratives/cas.md`
- `docs/narratives/cas-coding-agent-collaboration.md`

### Medium-Risk Files (Confidential / Internal — Category 2 🟡)
- `docs/narratives/bat-transformation.md`
- `docs/narratives/bbc-studios-digital-evolution.md`
- `docs/narratives/ea4all.md`
- `docs/narratives/runner-agentic-intelligence.md`
- `governance/terminology.yaml`
- `governance/README.md`
- `specs/001-portfolio-restructure/spec.md`
- `specs/001-portfolio-restructure/plan.md`
- `specs/001-portfolio-restructure/tasks.md`
- `specs/001-portfolio-restructure/data-model.md`
- `specs/001-portfolio-restructure/research.md`
- `specs/001-portfolio-restructure/quickstart.md`
- `specs/001-portfolio-restructure/checklists/requirements.md`
- `specs/001-portfolio-restructure/contracts/homepage-hero-contract.md`
- `specs/001-portfolio-restructure/contracts/narrative-structure-contract.md`
- `specs/002-tech-blog-approval-status/spec.md`
- `specs/002-tech-blog-approval-status/plan.md`
- `specs/002-tech-blog-approval-status/tasks.md`
- `specs/002-tech-blog-approval-status/data-model.md`
- `specs/002-tech-blog-approval-status/research.md`
- `specs/002-tech-blog-approval-status/quickstart.md`
- `specs/002-tech-blog-approval-status/checklists/requirements.md`
- `specs/002-tech-blog-approval-status/contracts/frontmatter-contract.md`
- `specs/architecture-sop/architect-sop-evolution.md`
- `specs/architecture-sop/feature-architect-sop.md`
- `specs/claude-specs.md/custom-domain-migration.md`
- `specs/claude-specs.md/homepage-optimisation.md`
- `specs/claude-specs.md/portfolio-look-and-feel-restructure.md`
- `specs/favicon-generation/spec.md`
- `specs/lighthouse-baseline.md`
- `specs/livereload-polling/spec.md`
- `specs/mkdocs-optimization/plan.md`
- `specs/mkdocs-optimization/spec.md`
- `specs/mkdocs-optimization/tasks.md`
- `specs/mkdocs-quick-wins/spec.md`
- `specs/mkdocs-wave-2/spec.md`
- `specs/portfolio-bootstrap-blueprint.md`
- `specs/portfolio-documentation-update/spec.md`
- `specs/site-gitignore/spec.md`
- `specs/tech-blog/spec.md`
- `specs/validator-test-suite/spec.md`

### Low-Risk Files (Public / Generic — Category 3 🟢)
- `docs/index.md`
- `docs/about.md`
- `docs/contact.md`
- `docs/architecture-philosophy.md`
- `docs/how-i-work.md`
- `docs/selected-work.md`
- `docs/CNAME`
- `docs/diagrams/architecture.md`
- `docs/js/cloudflare-insights.js`
- `docs/tech-blog/index.md`
- `docs/tech-blog/posts/2026-05-17-decoupling-git-diff-parsing-architecture-evaluation.md`
- `docs/tech-blog/posts/2026-05-17-deterministic-delta-extraction-before-semantic-ai-analysis.md`
- `docs/tech-blog/posts/2026-08-07-career-projection-generator-evidence-bounded-career-projection.md`
- `docs/tech-blog/posts/2026-08-07-preventing-generative-over-claiming-with-claim-linting.md`
- `docs/tech-blog/posts/2026-08-08-four-layer-agentic-pipeline-architecture.md`
- `docs/assets/alexandre-franco-cv.pdf`
- `docs/assets/images/favicon-16.png`
- `docs/assets/images/favicon-32.png`
- `docs/assets/images/favicon-180.png`
- `docs/assets/images/favicon-source.png`
- `docs/assets/images/favicon.ico`
- `docs/assets/images/favicon.png`
- `docs/assets/images/headshot.png`

### Unreviewed / Unknown Risk Files
- *None* — 100% of files within target scope (`docs/`, `governance/`, `specs/`) were categorized and assessed.
