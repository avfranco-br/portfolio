# Agent Context: CLAUDE.md

You are an expert software engineer and architect. This repository operates under **CAS Governance**.

> **Note:** This is a **MkDocs portfolio platform** with an embedded CAS governance framework. It is a content site, not a typical software codebase. There is no `src/` directory; "code" means MkDocs Markdown + Python governance scripts.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Serve site locally (hot reload)
mkdocs serve

# Full governance validation (build + terminology)
bash scripts/run_governance.sh
```

## Operational Mandates

1. **Enforce SDD**: Do not implement features without a validated specification in `specs/`.
2. **Skill-Driven Workflow**: You MUST use the skills located in `.cas/` for all structural changes.
3. **Architectural Alignment**: Check `.cas/rules/` and `.cas/patterns/` before proposing new designs.
4. **No Hidden Logic**: Avoid hacks or suppressing warnings. Use idiomatic and explicit language features.

## Development Cycle

1. **Research**: Use grep and find to understand the system.
2. **Spec**: Draft a clear requirement set under `specs/`.
3. **Skill**: Run `cas-add-or-modify-feature` to confirm architectural fit.
4. **Code**: Implement the change surgically.
5. **Verify**: Run `bash scripts/run_governance.sh` to prove the fix/feature.

## Repository Topology

| Path | Purpose |
|------|---------|
| `docs/` | MkDocs content source — site pages and narratives |
| `docs/narratives/` | Long-form architecture/governance case studies |
| `governance/terminology.yaml` | Canonical terminology policy |
| `scripts/validate_governance.py` | Terminology validator (runs in CI) |
| `scripts/run_governance.sh` | Combined build + terminology check |
| `.cas/rules/architecture_rules.md` | Architectural constraints |
| `.cas/patterns/patterns-catalogue.yaml` | Reusable design patterns |
| `.cas/cas-add-or-modify-feature/` | Skill: feature workflow |
| `.cas/cas-refactor-module/` | Skill: refactor workflow |
| `.github/workflows/` | Three CI/CD workflows (see AGENTS.md) |
| `mkdocs.yml` | Site configuration + navigation |
| `specs/` | Specifications (SDD) |

## Conventions

- British English throughout prose.
- Hyphen-free canonical terms: `AI native`, `governance aware`, `coding agent`, `multi agent`.
- See `governance/terminology.yaml` for the full canonical list and rejected variants.

## Security

Never log or commit secrets, API keys, or sensitive credentials.

## Further Reading

- **Governance contract:** `AGENTS.md` — full operational rules for all agents.
- **System architecture:** `ARCHITECTURE.md` — layered design and extension points.