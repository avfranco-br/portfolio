# Portfolio Documentation Refresh — Design Spec

**Date:** 2026-08-02
**Status:** Proposed
**Scope:** Documentation alignment + workflow correction

---

## 1. Problem

The repository's primary documentation files (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`) were authored at project bootstrap (May 2026) and have drifted from the current state. Specifically:

- `CLAUDE.md` and `AGENTS.md` describe a generic software-development context but the repo is a **MkDocs portfolio site** with an embedded governance framework.
- `GEMINI.md` references Speckit boilerplate (`<!-- SPECKIT START -->`) that is no longer the source of operational truth.
- `ARCHITECTURE.md` does not exist; there is no single document describing the layered structure (content site + governance layer + CAS skill framework).
- `.github/workflows/cas-validate-sdd.yml` watches `src/**` — a path that does not exist in this repository — making the workflow inert.
- Recent commits introduced new artefacts (`scripts/validate_governance.py`, `governance/terminology.yaml`, `docs/narratives/`, six narrative pages) that none of the agent-context files mention.

## 2. Goal

Produce a coherent, current documentation set that:

1. Reflects the **actual layered architecture** (portfolio site + governance + CAS framework).
2. Gives AI coding agents enough context to operate correctly on the first interaction.
3. Closes the gap between the SDD validation workflow and the actual codebase.
4. Guides the **next iteration** of work without prescribing it.

## 3. Non-Goals

- No new governance features (terminology additions, new patterns, new CI checks).
- No content changes to `docs/*.md` narratives.
- No change to MkDocs configuration or site theme.
- No change to the CAS skill implementations (`.cas/cas-*`).

## 4. Target Architecture

The documentation set will reflect a **three-layer model**:

```
┌─────────────────────────────────────────────────────────────┐
│ Layer 1 — Portfolio Site (MkDocs Material)                  │
│   docs/index.md, docs/about.md, docs/selected-work.md,      │
│   docs/architecture-philosophy.md, docs/contact.md,         │
│   docs/narratives/*.md, docs/assets/, docs/diagrams/        │
└─────────────────────────────────────────────────────────────┘
                          ▲
                          │  validated by
┌─────────────────────────────────────────────────────────────┐
│ Layer 2 — Governance Layer                                  │
│   governance/terminology.yaml                               │
│   scripts/validate_governance.py                            │
│   scripts/run_governance.sh                                 │
│   .cas/rules/architecture_rules.md                          │
│   .cas/patterns/patterns-catalogue.yaml                     │
└─────────────────────────────────────────────────────────────┘
                          ▲
                          │  enforced by
┌─────────────────────────────────────────────────────────────┐
│ Layer 3 — CI/CD Pipeline                                    │
│   .github/workflows/portfolio-governance.yml  (PR + main)   │
│   .github/workflows/cas-validate-sdd.yml     (PR only)      │
│   .github/workflows/deploy.yml               (main push)    │
└─────────────────────────────────────────────────────────────┘
```

## 5. Documentation Files

### 5.1 `CLAUDE.md` — Project root context

**Purpose:** Primary agent context for Claude Code. Concise, command-focused, current.

**Required content:**
- Project summary (one paragraph: portfolio platform + governance automation).
- Quick start commands (`pip install -r requirements.txt`, `mkdocs serve`, `scripts/run_governance.sh`).
- Directory map (key paths only).
- Operational mandates (SDD, CAS skills, governance layer).
- Link to `AGENTS.md` for full governance contract.

**Out of scope:** No duplicated content from `AGENTS.md`. No verbose explanations.

### 5.2 `AGENTS.md` — Governance contract

**Purpose:** Single source of truth for **all** coding agents (Claude, Gemini, humans). The governance contract.

**Required content:**
- SDD adapted to this repo: spec required for changes in `docs/**` when paired with `mkdocs.yml` changes; skip for prose-only edits.
- CAS skill registry (`cas-add-or-modify-feature`, `cas-refactor-module`).
- Governance layer description (terminology policy, validator script).
- All three workflows and what they do.
- The "no spec, no code" rule with explicit exception mechanism.

### 5.3 `GEMINI.md` — Gemini-specific context

**Purpose:** Bridge between `.specify/init-options.json` (which sets Gemini as the configured agent) and the codebase.

**Required content:**
- Reference to `AGENTS.md` as primary contract.
- Speckit 0.8.3 acknowledgement (with version pin).
- Gemini-specific tool affordances (topic management, search grounding).
- Local conventions only.

### 5.4 `ARCHITECTURE.md` — NEW

**Purpose:** Architectural reference for the portfolio platform.

**Required sections:**
1. **System Overview** — one-paragraph mission and three-layer model.
2. **Repository Topology** — annotated tree of important paths.
3. **Content Architecture** — how `docs/` maps to the site nav (`mkdocs.yml`).
4. **Governance Architecture** — terminology policy, validator, architecture rules.
5. **CAS Framework Integration** — how `.cas/` skills relate to the codebase (this is a *use-site*, not a framework implementation).
6. **CI/CD Pipeline** — diagram + per-workflow responsibilities.
7. **Extension Points** — where to add new content, patterns, terminology entries.
8. **Operational Principles** — distilled from README and index.md.
9. **Next Iterations** — explicit guidance for upcoming work (see §6).

## 6. Next Iterations Guidance

ARCHITECTURE.md must explicitly capture the following **open threads** so future agents can pick them up:

| Thread | Description | Location |
|--------|-------------|----------|
| Diagram generation | `docs/diagrams/` exists but is empty; Mermaid is configured in `mkdocs.yml` | `docs/diagrams/` |
| Asset pipeline | `docs/assets/` present; no build step yet | `docs/assets/` |
| Speckit bootstrap | `.specify/templates/`, `.specify/plans/` available but unused since initialisation | `.specify/` |
| `.tmp/` directory | Empty placeholder (`tmp/`) | `tmp/` |
| `site/` build output | Generated, committed | `site/` (consider gitignore review) |
| Cas workflow `src/` mismatch | Workflow needs adapting | this spec |

## 7. Workflow Adaptation

`.github/workflows/cas-validate-sdd.yml` will be updated to:

- Trigger on changes to `docs/**` AND `mkdocs.yml` (content + nav = structural change).
- Require a corresponding spec in `specs/` or `.specify/`.
- Skip for changes to `docs/assets/**`, `docs/diagrams/**` (binary/auxiliary).
- Retain `[skip-governance]` and `[bugfix]` exemption markers.

The trigger path change is the only modification. No new validation logic; the existing exemption and check logic is preserved.

## 8. Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Breaking link from CLAUDE.md rewrite for existing agent sessions | Keep file in same path; preserve "agent context" framing at top |
| Workflow change triggers false-positive CI failures on first run | The new path filter is **more restrictive** than the old (which always passed because `src/` never existed), so no new failures |
| ARCHITECTURE.md becoming stale | Place "Last reviewed" date and reference commit hash in header |
| Overlap/conflict between AGENTS.md and CLAUDE.md | CLAUDE.md explicitly defers to AGENTS.md for governance details |

## 9. Acceptance Criteria

- All four files exist at expected paths.
- All four files reflect the current state (verified against `git status`, `git log`).
- `mkdocs build --strict` still passes (no broken nav links from doc updates).
- `scripts/run_governance.sh` still passes (no terminology drift introduced).
- `.github/workflows/cas-validate-sdd.yml` adapted per §7.
- A new spec exists at `specs/portfolio-documentation-update/spec.md` (this file).
- Commit message format follows existing convention: `feat:`, `chore:`, `fix:` prefixes.

## 10. Out-of-Scope Items (recorded for future)

- Adding new terminology entries to `governance/terminology.yaml`.
- Restructuring `.cas/` patterns catalogue.
- Migrating from Speckit 0.8.3.
- Removing `site/` from version control.
- Adding tests for `scripts/validate_governance.py`.
- Replacing `update_topic` mention in GEMINI.md (tool may not exist in current Gemini CLI).