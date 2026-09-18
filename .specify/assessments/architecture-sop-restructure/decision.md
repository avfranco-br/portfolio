# Decision: Architecture SOP Structure Reorganisation

- **Slug**: architecture-sop-restructure
- **Decided**: 2026-09-17
- **Verdict**: go
- **Artifacts reviewed**: problem.md | concept.md

## Scorecard

| Criterion | Rating | Justification |
|-----------|--------|---------------|
| Problem validity | strong | The current documentation structure conflates core lifecycle stages, standalone engagement consulting methods, and sample deliverable evidence. |
| Evidence strength | strong | Source files exist in `docs/sop/` and `docs/sop/methods/`, clearly demonstrating the need for logical separation and clearer taxonomy. |
| Value vs. inaction | strong | Clear taxonomy immediately elevates practice readability, user navigation, and demonstrates disciplined enterprise architecture organisation. |
| Feasibility / appetite | strong | Option A is well-bounded within a small appetite (1–2 days) without requiring disruptive overhauls. |
| Strategic fit | strong | Aligns directly with CAS principles and professional presentation of Enterprise Architecture practice and engagement methods. |
| Risk posture | strong | Main risks (link-rot, broken relative markdown paths, strict build failures) are well-understood and protected by local `mkdocs build --strict` and governance tests. |

## Verdict & Rationale

**Verdict: GO.**
The proposed three-tier taxonomy (Core EA Practice, Engagement Methods, Illustrative Evidence) provides immediate structural clarity, clearly positioning the underlying operating model versus actionable engagement methods and real-world evidence deliverables. Option A delivers this safely and incrementally.

## If go — Handoff to `/speckit-specify`

- **Problem**: Conflation of core lifecycle practice, specific engagement consulting methods, and illustrative deliverable reports in site navigation and structure.
- **Chosen approach**: Option A — Three-Tier Navigation & Section Reorganisation across `mkdocs.yml`, `docs/sop/index.md`, and relevant paths.
- **In scope / out of scope**:
  - *In scope*: Reorganising navigation into Core EA Practice (5 stages), Engagement Methods (4 methods including Health Check), and Illustrative Evidence (2 reports); updating `docs/sop/index.md` to reflect this taxonomy; adding/establishing the Health Check page.
  - *Out of scope*: Deep textual rewrites of stages or reports; restructuring outside `docs/sop`; CAS workflow changes.
- **Success metrics**: Clean three-tier navigation in `mkdocs.yml`, 0 broken links, and 100% pass on `mkdocs build --strict` and `python scripts/validate_governance.py`.
- **Carried-forward open questions**:
  - Content depth for the Architecture Health Check entry (starter guide vs full method).
  - Positioning for AI Augmented Workflows and Agent Co-Pilot Prompt alongside the three tiers.
