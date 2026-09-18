# Concept: Mermaid Diagram Legibility & Responsive Presentation

- **Slug**: mermaid-diagram-legibility
- **Created**: 2026-09-18
- **Recommended option**: Option A — Hybrid Layout Refactoring & Responsive Container Styling

## Options

### Option A — Hybrid Layout Refactoring & Responsive Container Styling (Recommended)
- **Sketch**: A two-pronged approach addressing both structure and container rendering:
  1. **Layout refactoring**: Convert excessively wide linear chains (e.g., 8–14 nodes in a single `flowchart LR` line in `docs/sop/index.md` Section 15 and Overview) into multi-tier / folded rows (`flowchart TD` or multi-stage subgraphs). Grouping related phases (e.g., *Strategic Framing* → *Architectural Analysis* → *Delivery & Value Realisation*) allows diagrams to stack naturally with larger nodes, readable fonts, and zero horizontal shrinking.
  2. **Responsive CSS container**: Add a light stylesheet (`docs/css/mermaid.css` or theme override) that ensures SVG diagrams maintain a minimum readable font size, set appropriate `min-width` / touch horizontal scrolling on constrained viewports, and prevent aggressive SVG scaling down.
- **Appetite**: small (1–2 days)
- **Trade-offs**: Strikes an optimal balance: structural refactoring makes the diagrams intrinsically more readable and visually impactful on any medium, while the CSS safeguard ensures no diagram is crushed even on small tablet/mobile screens. Requires touching diagram syntax in affected markdown pages and registering a CSS file in `mkdocs.yml`.
- **Rabbit holes**: Over-engineering CSS or introducing heavy JavaScript zoom libraries that conflict with MkDocs Material's built-in print or dark mode palettes.

### Option B — Pure Structural Re-layout (Zero CSS/Configuration Changes)
- **Sketch**: Keep the MkDocs theme configuration and stylesheets completely untouched. Refactor only the Mermaid markdown code across affected pages: replace ultra-wide single-line `flowchart LR` definitions with top-down (`flowchart TD`) or multi-line looped topologies with wrapped node text.
- **Appetite**: small (1 day)
- **Trade-offs**: Extremely low footprint—requires zero changes to `mkdocs.yml`, CSS assets, or build scripts. However, on narrow viewports (such as mobile screens), even medium-width diagrams may still shrink slightly without container min-width/scroll rules.
- **Rabbit holes**: Trying to force complex 13-stage continuous chains into pure vertical flows without subgraphs can result in overly tall, fragmented diagrams that require excessive page scrolling.

### Option C — Pan & Zoom Interactive Viewer Integration
- **Sketch**: Integrate an interactive client-side Pan/Zoom library (e.g., `svg-pan-zoom` or medium-zoom plugin) that allows users to click, drag, and zoom in on any rendered Mermaid diagram in a modal or canvas overlay.
- **Appetite**: medium (3–4 days)
- **Trade-offs**: Preserves all wide diagrams in their original geometry and gives users full interactive control. However, it violates Constitution Principle I and IV (adds custom client-side JS/asset weight, creates maintenance overhead, and fails to fix the default unzoomed visual quality for casual readers).
- **Rabbit holes**: Theme conflicts with dark/light mode toggling, touch gesture conflicts on mobile, and potential breaking changes when MkDocs Material updates its Mermaid rendering pipeline.

## Recommendation

**Option A (Hybrid Layout Refactoring & Responsive Container Styling)** is recommended.
Architectural diagrams should communicate clearly at first glance without requiring user interaction or browser zooming. Refactoring wide sequential chains into logical stages/subgraphs directly addresses the root cause of the shrinking (too many linear nodes in one line), while a simple, lightweight CSS rule ensures that rendered diagram SVGs maintain minimum font sizes and graceful overflow scrolling across desktop, tablet, and mobile devices.

## Out of Scope (for the recommended option)

- Modifying the underlying architectural methodology, stages, or naming in the SOP.
- Adding third-party JavaScript zoom or pan libraries.
- Rewriting diagrams that already render with clear, readable typography.

## Assumptions to Validate

- The primary offenders are the long linear `flowchart LR` chains in `docs/sop/index.md` (Overview Strategy-to-Value chain, Section 15 Traceability chain, Section 16 AI workflow); other pages will be audited to identify any similar wide chains.
- MkDocs Material's `extra_css` mechanism can cleanly supply responsive styling for `.mermaid` containers without theme side-effects.
- Governance and strict build tests will continue to pass without issues.
