# Decision: Mermaid Diagram Legibility & Scaling

- **Slug**: mermaid-diagram-legibility
- **Decided**: 2026-09-18
- **Verdict**: go
- **Artifacts reviewed**: problem.md | concept.md

## Scorecard

| Criterion | Rating | Justification |
|-----------|--------|---------------|
| Problem validity | strong | Real visual defect demonstrated by user screenshots: wide horizontal Mermaid flows shrink excessively inside MkDocs Material, rendering text unreadable. |
| Evidence strength | strong | Directly confirmed in `docs/sop/index.md` (Overview chain with 8 nodes, Section 15 chain with 14 nodes) and reproduced visually. |
| Value vs. inaction | strong | Visual legibility is essential for an EA portfolio demonstrating systems thinking; unreadable diagrams undermine credibility. |
| Feasibility / appetite | strong | Option A fits easily within a small appetite (1–2 days) by refactoring wide chains into stacked rows/subgraphs and adding simple responsive CSS. |
| Strategic fit | strong | Fully adheres to Constitution Principle I (markdown-native, lightweight) and Principle V (systems thinking & visual transparency). |
| Risk posture | strong | Non-breaking changes: preserves diagram semantics, avoids heavy client-side JavaScript, and is validated by `mkdocs build --strict`. |

## Verdict & Rationale

**Verdict: GO.**
The issue directly impairs the primary visual presentation of the Enterprise Architecture operating model. Option A (Hybrid Layout Refactoring & Responsive Container Styling) provides an elegant, lightweight solution by restructuring wide diagrams into naturally readable multi-row/subgraph flows while introducing light CSS for graceful responsive overflow.

## If go — Handoff to `/speckit-specify`

- **Problem**: Long linear horizontal Mermaid diagrams scale down excessively within MkDocs Material prose columns, rendering diagram text and nodes unreadable on standard desktop and mobile displays.
- **Chosen approach**: Option A — Refactor excessively wide `flowchart LR` diagrams into structured multi-tier rows or subgraphs, complemented by lightweight responsive CSS container styling.
- **In scope / out of scope**:
  - *In scope*: Refactoring wide linear Mermaid flows (specifically in `docs/sop/index.md` and auditing other `docs/**/*.md` files); adding responsive Mermaid container styling via `docs/stylesheets/mermaid.css` or MkDocs theme overrides; verifying readability across viewports.
  - *Out of scope*: Changing architectural semantics or stage definitions; adding third-party JavaScript pan/zoom libraries; modifying non-Mermaid content.
- **Success metrics**: Diagram node labels and text render with high visual clarity and font sizes comparable to body prose; 0 broken links; 100% pass on `mkdocs build --strict` and governance test suite.
- **Carried-forward open questions**:
  - Which specific diagrams outside `docs/sop/index.md` require structural refactoring vs. benefiting purely from the responsive container styling?
