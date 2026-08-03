# Architecture: Portfolio Platform

**Last reviewed:** 2026-08-02
**Status:** Active
**Owner:** Alexandre Franco

---

## 1. System Overview

This repository is a **public portfolio platform** for architecture, governance, and operational transformation work, hosted on GitHub Pages. It is a **content-first** MkDocs site augmented with a **lightweight governance layer** and a **CAS skill framework** that guides AI agent behaviour.

The platform's core thesis is operational: governance through enablement rather than friction, architecture as operational capability, and continuous validation rather than periodic review. The technical architecture mirrors that thesis.

## 2. Layered Architecture

The system has three distinct layers, each with a clear responsibility:

![Layered Architecture Diagram](diagrams/architecture.md)

See [`docs/diagrams/architecture.md`](docs/diagrams/architecture.md) for the rendered Mermaid diagram with full node-to-path mapping. The three layers are:

- **Layer 1 — Content Site:** Authored Markdown in `docs/`, compiled to static HTML in `site/`, served via GitHub Pages.
- **Layer 2 — Governance:** Terminology policy, validator script, runner, CAS rules, CAS patterns, and skill specifications.
- **Layer 3 — CI/CD:** Three GitHub Actions workflows that validate and deploy.

**Boundary rules:**
- Layer 1 has **no executable code** other than the Python validator in Layer 2.
- Layer 2 scripts never import from Layer 1 (the validator only reads files).
- Layer 3 never duplicates Layer 2 logic — it invokes `mkdocs build` and `python scripts/validate_governance.py` directly.

## 3. Repository Topology

```
portfolio/
├── AGENTS.md                       Governance contract (all agents)
├── ARCHITECTURE.md                 This file
├── CLAUDE.md                       Claude-specific context
├── GEMINI.md                       Gemini-specific context
├── README.md                       Public-facing intro
├── LICENSE                         MIT
├── mkdocs.yml                      Site configuration + navigation
├── requirements.txt                Python dependencies (MkDocs Material)
│
├── docs/                           Layer 1: content source
│   ├── index.md                    Home / about-me entry
│   ├── about.md                    Strategic career narrative
│   ├── architecture-philosophy.md Operating principles
│   ├── selected-work.md            Curated transformation initiatives
│   ├── contact.md                  Contact invitation
│   ├── narratives/                 Long-form case studies (6 pages)
│   ├── assets/                     Static assets (favicon, images)
│   └── diagrams/                   Mermaid diagrams (currently empty)
│
├── governance/                     Layer 2: governance policy
│   ├── README.md                   Governance layer overview
│   └── terminology.yaml            Canonical terms + rejected variants
│
├── scripts/                        Layer 2: validation tooling
│   ├── run_governance.sh           Combined runner (build + terminology)
│   └── validate_governance.py      Terminology validator
│
├── tests/                          Layer 2: validator test suite
│   ├── conftest.py                 Shared fixtures (policy_clean, docs_tree, write)
│   └── test_validate_terminology.py   14 tests covering validator behaviour
├── pytest.ini                      pytest configuration
├── requirements-dev.txt            Dev dependencies (pytest)
│
├── .cas/                           CAS framework (use-site, not impl)
│   ├── rules/
│   │   └── architecture_rules.md   Module boundaries, contracts, etc.
│   ├── patterns/
│   │   └── patterns-catalogue.yaml 18 reusable patterns
│   ├── cas-add-or-modify-feature/  Feature workflow skill
│   └── cas-refactor-module/        Refactor workflow skill
│
├── .specify/                       Speckit 0.8.3 bootstrap
│   ├── init-options.json           Gemini configured as AI agent
│   ├── integration.json            Speckit integration metadata
│   ├── templates/                  Spec/plan/task templates
│   ├── extensions/                 Custom Speckit extensions
│   ├── workflows/                  Speckit workflow definitions
│   ├── scripts/                    Helper scripts
│   ├── plans/                      Generated plans
│   ├── tasks/                      Generated tasks
│   └── memory/                     Session memory
│
├── .github/workflows/              Layer 3: CI/CD
│   ├── portfolio-governance.yml    Build + terminology (PR + main)
│   ├── cas-validate-sdd.yml        SDD check (PR)
│   └── deploy.yml                  GitHub Pages deploy (main)
│
├── specs/                          Specifications (SDD)
│   ├── portfolio-bootstrap-blueprint.md
│   ├── mkdocs-optimization/        (spec, plan, tasks)
│   └── portfolio-documentation-update/  This documentation update
│
├── site/                           Generated build output (Layer 1 → 3)
└── tmp/                            Working scratch space
```

## 4. Content Architecture

### 4.1 Site map (from `mkdocs.yml`)

| Top-level nav | Sub-pages |
|---------------|-----------|
| Home | `index.md` |
| Architecture Philosophy | `architecture-philosophy.md` |
| About | `about.md` |
| Selected Work | `selected-work.md` |
| Enterprise Transformation | BAT, BBC Studios |
| AI Native Systems | EA4ALL, Runner Agentic Intelligence |
| Governance Systems | Continuous Architecture System (CAS), Governance Aware Coding Agent Collaboration |
| Contact | `contact.md` |

### 4.2 Narrative taxonomy

The `docs/narratives/` directory groups long-form case studies by theme:

- **Enterprise Transformation** — proven delivery at scale (BAT, BBC Studios).
- **AI Native Systems** — operational AI with governance guardrails (EA4ALL, RAI).
- **Governance Systems** — CAS as an architectural concept, and its application to coding-agent collaboration.

### 4.3 MkDocs features enabled

- Material theme with light/dark toggle.
- Mermaid diagram support (`pymdownx.superfences` with custom fence).
- Search (`mkdocs-search`), roam-links, minify, social plugins.
- Permalinks on heading anchors.

## 5. Governance Architecture

### 5.1 Terminology policy

`governance/terminology.yaml` declares canonical terms and rejected variants:

```yaml
canonical_terms:
  "AI native":        reject: ["AI-native", "AI powered"]
  "coding agent":     reject: ["coding-agent"]
  "operational intelligence": reject: []
  "governance aware": reject: []
  "architecture operationalisation": reject: []
  "repository-driven": reject: []
```

This list is the **single source of truth** for terminology across prose, code comments, and documentation.

### 5.2 Validation flow

```
mkdocs build --strict              # → fails on broken links/nav
            │
            ▼
scripts/validate_governance.py    # → warns on rejected terms
            │
            ▼
       CI passes?
```

Both steps run locally via `bash scripts/run_governance.sh` and in CI via `portfolio-governance.yml`.

### 5.3 CAS rules and patterns

- **Rules** (`.cas/rules/architecture_rules.md`) define non-negotiable constraints: module boundaries, dependency direction, determinism, contracts, pattern reuse, traceability.
- **Patterns** (`.cas/patterns/patterns-catalogue.yaml`) catalog 18 reusable design patterns (`build-time-governance`, `deterministic-core-selective-augmentation`, `contract-first-architecture`, etc.). The CAS skills reference these IDs in their output.

The CAS skills **consume** these rules and patterns when invoked — they are not a framework implementation but a **reference for AI agents**.

## 6. CAS Framework Integration

The `.cas/` directory contains **skill specifications**, not runnable agents:

- `cas-add-or-modify-feature/SKILL.md` — invoked when adding or modifying features. Produces a structured YAML output (`decision`, `code_changes`, `architecture_decision`, `architectural_impact`, `risks`, `validation_notes`).
- `cas-refactor-module/SKILL.md` — invoked when restructuring without behaviour change. Same output schema, different decision precedence (preserve observable behaviour first).

These skills are **advisory** in this repo — no CI step currently invokes them. They exist to guide AI agent behaviour when humans or AI propose structural changes.

## 7. CI/CD Pipeline

### 7.1 `portfolio-governance.yml`

| Trigger | branches: `main` push + PR |
|---------|----------------------------|
| Purpose | Validate build and terminology |
| Steps | checkout → setup-python (3.11) → `pip install -r requirements.txt pyyaml` → `mkdocs build --strict` → `python scripts/validate_governance.py` |

### 7.2 `cas-validate-sdd.yml`

| Trigger | PR targeting `main`/`master` |
|---------|------------------------------|
| Purpose | Enforce Specification-Driven Development |
| Watched paths | `docs/**`, `mkdocs.yml`, `scripts/**`, `governance/**`, `.cas/**` (after adaptation — see §10) |
| Logic | If structural files changed without `specs/**` or `.specify/**`, fail with hint to add spec or use `[bugfix]` / `[skip-governance]` exemption |

### 7.3 `deploy.yml`

| Trigger | push to `main` |
|---------|----------------|
| Purpose | Build site and deploy to GitHub Pages |
| Steps | checkout → setup-python (3.12) → `pip install -r requirements.txt` → `mkdocs build` → `actions/configure-pages` → upload artifact → `actions/deploy-pages` |
| Permissions | `contents: read`, `pages: write`, `id-token: write` |
| Concurrency | `pages` group (no cancel-in-progress) |

## 8. Extension Points

When extending the platform, the canonical entry points are:

| Want to... | Add or modify |
|-----------|---------------|
| Publish a new narrative page | `docs/narratives/<name>.md` + entry in `mkdocs.yml` nav |
| Add a new top-level section | `mkdocs.yml` nav + a new `docs/<section>.md` |
| Add a new diagram | `docs/diagrams/<name>.md` (Mermaid supported) |
| Enforce a new term | `governance/terminology.yaml` |
| Add a new CI check | `.github/workflows/<name>.yml` |
| Add a new pattern | `.cas/patterns/patterns-catalogue.yaml` (new ID + description) |
| Define a new architecture rule | `.cas/rules/architecture_rules.md` |
| Bootstrap a new feature | Create `specs/<feature-name>/spec.md` then invoke `cas-add-or-modify-feature` |

## 9. Operational Principles

Distilled from `README.md` and `docs/index.md`:

- **Governance through enablement, not friction.**
- **Lightweight operational controls over heavyweight process.**
- **Continuous validation over periodic review.**
- **Architecture as operational capability, not static documentation.**
- **Sustainable transformation through operational trust.**
- **British English in prose; canonical terms without hyphens.**

## 10. Known Gaps & Next Iterations

The following threads are **open** and should be the focus of upcoming work:

| # | Thread | Description | Suggested first step |
|---|--------|-------------|----------------------|
| 1 | `docs/diagrams/` is empty | Mermaid is configured but no diagrams exist | Add 1–2 system diagrams (e.g., governance pipeline flow) |
| 2 | SDD workflow adapted to docs | `cas-validate-sdd.yml` originally watched `src/**` (does not exist in this repo) | Update path filter to `docs/**`, `mkdocs.yml`, `scripts/**`, `governance/**`, `.cas/**` |
| 3 | Speckit templates underused | `.specify/templates/` exists from bootstrap but is rarely used | ✅ Decision: keep Speckit installed. Reasons: (1) no current sprint with new features or refactoring that justifies using the framework, (2) parallel exploration of alternative SDD frameworks. Re-evaluate when either condition changes. |
| 4 | ~~`site/` is committed~~ | ~~Generated output was in version control~~ | ✅ Already done — `.gitignore` line 35 (`/site`) was in place from the initial commit; `git ls-files site/` returns 0 files; `site/` has never been tracked. The 3.4 MB on disk is regenerated by every `mkdocs build` run and is never committed. |
| 5 | ~~Validator has no tests~~ | ~~`scripts/validate_governance.py` was untested~~ | ✅ Done — see `tests/` (14 tests, including a regression guard against the real repo) |
| 6 | ~~No diagram of the three layers~~ | ~~This doc had ASCII art only~~ | ✅ Done — see [`docs/diagrams/architecture.md`](docs/diagrams/architecture.md) |
| 7 | ~~`.gemini/` directory present~~ | Listed as a "bootstrap artefact" needing review | ✅ Resolved — not a bootstrap artefact. `.gemini/commands/speckit.*.toml` are the **Speckit → Gemini CLI integration manifests** (14 commands: specify, clarify, plan, tasks, implement, checklist, analyze, constitution, plus 5 git helpers). Tracked by `.specify/integrations/gemini.manifest.json` with SHA-256 hashes. Correctly gitignored (line 38 of `.gitignore`); each developer regenerates from the manifest. Decision follows from thread #3 (keep Speckit): keep `.gemini/`. |

## 11. References

- **Governance contract:** `AGENTS.md`
- **Claude context:** `CLAUDE.md`
- **Gemini context:** `GEMINI.md`
- **Public intro:** `README.md`
- **MkDocs config:** `mkdocs.yml`
- **Terminology policy:** `governance/terminology.yaml`
- **CAS rules:** `.cas/rules/architecture_rules.md`
- **CAS patterns:** `.cas/patterns/patterns-catalogue.yaml`
- **Specifications:** `specs/`

---

*This document is reviewed as part of any architectural change. Update the "Last reviewed" date and reference commit hash in the header when changes occur.*