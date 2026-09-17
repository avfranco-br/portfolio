# Problem Definition: Architecture SOP Structure Reorganisation

- **Slug**: architecture-sop-restructure
- **Created**: 2026-09-17
- **Inputs used**: user input only

## Problem Statement

The Architecture SOP documentation navigation currently mixes core practice lifecycle stages, specialised engagement methods, and illustrative output deliverables under a relatively flat or unstratified structure. Readers and stakeholders looking to explore enterprise architecture capability cannot immediately distinguish between foundational practice guidance, reusable engagement methods, and concrete exemplar reports.

## Affected Users & Stakeholders

- **Users**: Enterprise architects, technology leaders, hiring managers, and portfolio visitors — they struggle to quickly differentiate between practice stages, engagement consulting methods, and illustrative deliverable artifacts.
- **Stakeholders**: Alexandre Franco (Portfolio Owner) — needs the portfolio to clearly reflect a mature, structured Enterprise Architecture operating model and distinct engagement capabilities.

## Goals

- Establish a clear three-tier taxonomy for the Architecture SOP:
  1. **Core EA Practice** (Stages 01–05)
  2. **Engagement Methods** (Decision Review, Assessment & Roadmap, Health Check, Automation Opportunity Assessment)
  3. **Illustrative Evidence** (Decision Review report, Assessment & Transformation Roadmap report)
- Align MkDocs site navigation and SOP index to this structure cleanly without broken links or strict build failures.
- Ensure all 4 engagement methods and 2 illustrative evidence documents have clear homes and navigation paths.

## Non-Goals

- Rewriting existing stage or method narrative text.
- Re-architecting the portfolio outside the Architecture SOP domain.
- Overhauling CAS governance or CI workflows.

## Success Metrics

- Clean three-tier hierarchy visible in `mkdocs.yml` navigation and SOP index.
- 100% pass on `mkdocs build --strict` and `scripts/validate_governance.py`.
- Clear, distinct access to all 4 Engagement Methods and 2 Illustrative Evidence reports.

## Cost of Inaction

Portfolio visitors conflate high-level EA operating models with specific project methods and sample engagement deliverables, diluting the perceived clarity and systematic rigour of the practice.

## Open Questions

- Should "Architecture Health Check" be introduced as an initial summary/stub or full method in this cycle?
- Where should auxiliary pages ("AI Augmented Workflows", "Agent Co-Pilot Prompt") sit within or alongside the three tiers?
