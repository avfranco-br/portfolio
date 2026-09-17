# Concept: Architecture SOP Structure Reorganisation

- **Slug**: architecture-sop-restructure
- **Created**: 2026-09-17
- **Recommended option**: Option A — Three-Tier Navigation & Section Reorganisation

## Options

### Option A — Three-Tier Navigation & Section Reorganisation
- **Sketch**: Reorganise the Architecture SOP documentation within `mkdocs.yml` and `docs/sop/` into three distinct structural groupings: **Core EA Practice** (Stages 01–05), **Engagement Methods** (Decision Review, Assessment & Roadmap, Health Check, Automation Opportunity Assessment), and **Illustrative Evidence** (Decision Review report, Assessment & Transformation Roadmap report). Add a stub/page for Architecture Health Check (or link to existing methodology reference) to complete the quartet, while keeping the AI augmented workflows and agent prompts appropriately linked or situated.
- **Appetite**: small (1–2 days)
- **Trade-offs**: Provides an intuitive, cleanly stratified user experience reflecting professional EA practice hierarchy (Foundation Practice vs. Applied Methods vs. Tangible Deliverables/Evidence). Requires updating navigation in `mkdocs.yml`, introducing/repointing file paths under `docs/sop/`, and verifying cross-references and MkDocs strict build pass.
- **Rabbit holes**: Overcomplicating directory file moves (e.g. moving too many physical paths at once breaking internal markdown links and requiring extensive redirects). Can be mitigated by keeping physical files stable or staging relocations carefully.

### Option B — Pure Nav-Level Restructuring (Zero File Moves)
- **Sketch**: Retain all physical Markdown files in their existing locations (`docs/sop/*.md` and `docs/sop/methods/*.md`), but restructure the `mkdocs.yml` navigation tree into the requested hierarchical grouping: Core EA Practice (Stages 01–05), Engagement Methods (4 methods), and Illustrative Evidence (2 reports).
- **Appetite**: small (half day)
- **Trade-offs**: Extremely low risk and zero file renaming or broken relative links. Sacrifices filesystem mirroring of the navigation taxonomy (content authoring layout remains flat/mixed under `methods/`).
- **Rabbit holes**: Ongoing authoring confusion between methods and evidence files sharing the same directory without naming/folder distinction.

### Option C — Comprehensive SOP Directory & Nav Realignment
- **Sketch**: Full physical directory overhaul: partition `docs/sop/` into `docs/sop/core/`, `docs/sop/methods/`, and `docs/sop/evidence/`, moving all respective markdown files, updating all internal markdown relative links, diagrams, image assets, `mkdocs.yml`, and updating references across portfolio narratives and `docs/sop/index.md`.
- **Appetite**: medium (3–5 days)
- **Trade-offs**: Clean 1:1 parity between filesystem architecture and published site navigation. However, introduces broad churn, potential broken incoming URLs or deep backlinks, and increases risk of governance validator or build errors.
- **Rabbit holes**: Cascading broken relative links across large documents (some >70KB), diagram image paths, and external cross-narrative references.

## Recommendation

**Option A (Three-Tier Navigation & Section Reorganisation)** is recommended. It directly achieves the strategic taxonomy desired (Core EA Practice → Engagement Methods → Illustrative Evidence) in both the published navigation and the SOP index landing page, creates a dedicated home for the Health Check method, and separates illustrative reports from methodology guides, while controlling operational churn and link-rot risk.

## Out of Scope (for the recommended option)

- Rewriting the underlying methodology content of Stages 01–05 or existing methods (content remains intact; focus is structural organisation and taxonomy).
- Refactoring the broader portfolio narrative structures outside of the Architecture SOP section.
- Replacing or modifying the CAS governance engine or CI validation workflows.

## Assumptions to Validate

- Architecture Health Check page content needs clarification on whether an initial outline/stub is sufficient or if full method documentation is to be imported/authored.
- Existing references to illustrative reports in other narrative pages need validation to prevent link breakage.
- The placement of "AI Augmented Workflows" and "Agent Co-Pilot Prompt" within this new three-tier structure (e.g., whether they stay under Core EA Practice, become a separate sub-section, or sit under Overview).
