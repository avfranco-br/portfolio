# Problem Definition: Mermaid Diagram Legibility & Scaling

- **Slug**: mermaid-diagram-legibility
- **Created**: 2026-09-18
- **Inputs used**: user input only

## Problem Statement

Several wide horizontal (`flowchart LR`) Mermaid diagrams across the site—most visibly on the Enterprise Architecture SOP Overview page (such as the Strategy-to-Value chain in the Overview and the 13-stage lifecycle chain in Section 15)—scale down excessively to fit within the standard MkDocs Material prose column width. This causes boxes and typography to shrink to an unreadable size on standard desktop displays and mobile screens, forcing users to squint, zoom their entire browser, or skip the architectural diagrams entirely.

## Affected Users & Stakeholders

- **Users**: Technology leaders, hiring managers, architects, and portfolio visitors attempting to read end-to-end architectural lifecycles, capability chains, and methodology flows.
- **Stakeholders**: Alexandre Franco (Portfolio Owner) — relies on diagrams to communicate systems thinking, architectural rigor, and end-to-end traceability cleanly.

## Goals

- Ensure all architectural diagrams across the portfolio are immediately legible at standard zoom and viewport widths without microscopic text or crushed boxes.
- Establish a consistent layout and presentation strategy for wide linear workflows (e.g., vertical/multi-row flow layout, container zooming/scrolling, responsive styling, or layout refactoring).
- Maintain 100% compliance with MkDocs Material theme aesthetics and strict build validation (`mkdocs build --strict`).

## Non-Goals

- Changing the conceptual semantics, stages, or architectural meaning of the diagrams.
- Replacing Mermaid with static raster images or proprietary diagramming formats (must remain markdown-native per Constitution Principle I).
- Altering unrelated prose or navigation structure.

## Success Metrics

- Text inside all Mermaid diagrams is easily legible at 100% browser zoom on standard laptop/desktop resolutions (1366x768 to 1920x1080) and tablet viewports.
- No horizontal diagram squashes text below standard body reading size (approx. 12–14px rendered equivalent).
- `mkdocs build --strict` and governance tests continue to pass with 0 errors.

## Cost of Inaction

Key architectural visualisations—which form the core demonstration of Alexandre's systems-first philosophy—remain unreadable, giving visitors an impression of poor UX and preventing them from absorbing the methodology.

## Open Questions

- [NEEDS CLARIFICATION: Should wide diagrams be refactored into multi-row / top-down (TD) structures, or supported via interactive zoom / responsive overflow containers in MkDocs?]
- [NEEDS CLARIFICATION: Are there specific diagrams outside `docs/sop/index.md` (e.g., narratives, case studies) that also suffer from this issue and need auditing?]
