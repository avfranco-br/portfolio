# Agent Context: GEMINI.md

You are an interactive CLI agent specialising in software engineering. This repository enforces **CAS Governance**.

> **Speckit integration:** This project uses **Speckit 0.8.3** (per `.specify/init-options.json` and `.specify/integration.json`). The configured AI is Gemini. Use Speckit templates in `.specify/templates/` when bootstrapping a new feature.

## Mandatory Instructions

1. **Always read `AGENTS.md` first** — it is the primary governance contract for every agent (Claude, Gemini, human).
2. **Use CAS Skills**: Before modifying any code, you MUST activate the appropriate skill in `.cas/` (`cas-add-or-modify-feature` or `cas-refactor-module`).
3. **Specification-First**: If a user asks for a feature, your first step is to create or update a spec in `specs/`. See `AGENTS.md` § "SDD Triggers" for what counts as a structural change.
4. **Surgical Edits**: Prefer precise code replacements over overwriting entire files.
5. **Validate Behavior**: Never assume a change is correct. Always run `bash scripts/run_governance.sh` before committing.

## Repo at a Glance

- **Type:** MkDocs portfolio platform (no `src/` directory; "code" is Markdown + Python).
- **Validation:** `mkdocs build --strict` (build) + `scripts/validate_governance.py` (terminology).
- **CI/CD:** Three workflows — `portfolio-governance`, `cas-validate-sdd`, `deploy`.
- **Site URL:** https://avfranco-br.github.io/portfolio/

## Topic Management

Use the `update_topic` tool (when available) to keep the user informed of your strategic intent and progress across multi-turn tasks.

## Code Conventions

- British English in all prose.
- Hyphen-free canonical terms (e.g., `AI native`, `governance aware`, `coding agent`, `multi agent`).
- Full canonical list: `governance/terminology.yaml`.
- Mermaid diagrams are supported in Markdown (configured in `mkdocs.yml`).

## Local Commands

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt   # one-off: adds pytest
mkdocs serve                            # local preview
bash scripts/run_governance.sh          # full validation
python scripts/validate_governance.py   # terminology only
pytest tests/                           # validator test suite
```

## Further Reading

- `CLAUDE.md` — Claude-specific quick reference.
- `AGENTS.md` — full governance contract (authoritative).
- `ARCHITECTURE.md` — layered system architecture.
- `.specify/templates/` — Speckit templates for new specs/plans/tasks.