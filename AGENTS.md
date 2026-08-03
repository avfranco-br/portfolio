# Operational Governance: AGENTS.md

This repository uses the **Continuous Architecture System (CAS)** to ensure architectural integrity and operational discipline. All coding agents (AI) and human contributors must adhere to the following rules.

> **Scope:** This is a MkDocs portfolio platform. "Code" means MkDocs Markdown content, Python governance scripts, and CI workflows. There is no `src/` directory.

## Core Mandates

1. **Specification-Driven Development (SDD)**: No feature implementation or structural change shall begin without a corresponding specification in `specs/` (or `.specify/`).
2. **CAS Skill Enforcement**: Mandatory CAS Skills located in `.cas/` MUST be used before any code modifications.
3. **Decision Traceability**: Every architectural decision must be documented with rationale (in the spec).
4. **Minimal Drift**: Code changes must align strictly with the approved specification and architectural rules.

## SDD Triggers (Adapted for This Repo)

The SDD rule applies when the change is **structural**, not purely cosmetic. Specifically:

| Change scope | Spec required? |
|--------------|----------------|
| `docs/*.md` content only (prose) | No |
| `docs/*.md` + `mkdocs.yml` (nav) | **Yes** — structural |
| New page under `docs/narratives/` | **Yes** |
| `scripts/*.py` change | **Yes** |
| `.github/workflows/*.yml` change | **Yes** |
| `governance/terminology.yaml` change | **Yes** |
| `.cas/**` change | **Yes** |
| `docs/assets/**`, `docs/diagrams/**` only | No (binary/auxiliary) |
| Commit message contains `[skip-governance]` or `[bugfix]` | No (explicit exemption) |

The CI workflow `.github/workflows/cas-validate-sdd.yml` enforces this on every pull request.

## Interaction Workflow

1. **Research**: Map the codebase and understand the existing patterns.
2. **Specify**: Define the "What" and "Why" in a specification file under `specs/`.
3. **Align**: Invoke the relevant CAS Skill (`cas-add-or-modify-feature` or `cas-refactor-module`) to validate the design against rules.
4. **Implement**: Execute the change based on the validated design.
5. **Validate**: Run `bash scripts/run_governance.sh` locally, then push and verify CI passes.

## CAS Skill Registry

- **`cas-add-or-modify-feature`**: Use for any new feature, narrative page, or change to existing behaviour.
- **`cas-refactor-module`**: Use for restructuring code without changing behaviour (e.g., splitting a long narrative, reorganising scripts).

Both skills produce a structured YAML output block with `decision`, `architecture_decision`, `architectural_impact`, and `validation_notes` sections.

## Continuous Governance Validation

The repository includes a lightweight automation layer to ensure structural and content integrity:

1. **Build Integrity**: All changes are validated using `mkdocs build --strict` to prevent broken navigation or missing targets.
2. **Terminology Consistency**: A terminology policy (`governance/terminance/terminology.yaml`) defines canonical terms. The `scripts/validate_governance.py` script checks for rejected variants to maintain narrative consistency.
3. **CI Orchestration**: Three GitHub Actions workflows:
   - `portfolio-governance.yml` — runs on every PR and push to `main`. Executes `mkdocs build --strict` and `scripts/validate_governance.py`.
   - `cas-validate-sdd.yml` — runs on every PR. Verifies structural changes are accompanied by a specification.
   - `deploy.yml` — runs on push to `main`. Builds the site and deploys to GitHub Pages.

## Local Validation

```bash
# Quick: serve site locally
mkdocs serve

# Full governance check (build + terminology)
bash scripts/run_governance.sh

# Terminology only
python scripts/validate_governance.py

# Test suite (pytest)
pytest tests/
```

The terminology validator produces **guidance-level warnings** by default (does not fail the build); `mkdocs build --strict` will fail on broken links or nav errors. The pytest suite under `tests/` covers `scripts/validate_governance.py` and must pass before any change to the validator.

## Architectural Constraints

See `.cas/rules/architecture_rules.md` for the canonical rules:

- Module boundaries (single responsibility, explicit interfaces, no cross-layer imports).
- Dependency management (core logic must not depend on external providers without abstractions).
- Determinism (core orchestration must remain deterministic).
- Contracts (outputs conform to explicit schemas).
- Pattern reuse (existing patterns before new structures).
- Traceability (every change includes rationale).

See `.cas/patterns/patterns-catalogue.yaml` for reusable patterns (e.g., `build-time-governance`, `deterministic-core-selective-augmentation`, `contract-first-architecture`).

## Security

Never log or commit secrets, API keys, or sensitive credentials. This is a public portfolio site; assume everything committed will be deployed.

---

*This file is a governance contract. Do not modify without an approved architectural decision recorded in `specs/`.*