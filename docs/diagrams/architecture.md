# Portfolio Platform — Layered Architecture

This diagram captures the **three-layer model** of the portfolio platform: a content site, a governance layer, and the CI/CD pipeline that enforces both. It is the canonical visual reference for `ARCHITECTURE.md` §2.

```mermaid
flowchart TB
    subgraph L1["Layer 1 — Content Site (MkDocs Material)"]
        direction TB
        A1["docs/index.md, docs/about.md<br/>docs/architecture-philosophy.md<br/>docs/selected-work.md, docs/contact.md"]
        A2["docs/narratives/<br/>6 long-form case studies"]
        A3["docs/assets/<br/>images, favicon"]
        A4["docs/diagrams/<br/>Mermaid sources"]
        A5[("site/<br/>generated HTML")]
    end

    subgraph L2["Layer 2 — Governance"]
        direction TB
        G1["governance/terminology.yaml<br/>canonical terms + rejected variants"]
        G2["scripts/validate_governance.py<br/>terminology validator"]
        G3["scripts/run_governance.sh<br/>combined runner"]
        G4[".cas/rules/architecture_rules.md"]
        G5[".cas/patterns/patterns-catalogue.yaml"]
        G6[".cas/cas-add-or-modify-feature/<br/>.cas/cas-refactor-module/<br/>skill specifications"]
    end

    subgraph L3["Layer 3 — CI/CD"]
        direction TB
        C1["portfolio-governance.yml<br/>(PR + main push)<br/>build + terminology"]
        C2["cas-validate-sdd.yml<br/>(PR only)<br/>SDD spec presence"]
        C3["deploy.yml<br/>(main push only)<br/>build + GitHub Pages"]
    end

    A1 --> A5
    A2 --> A5
    A3 --> A5
    A4 --> A5

    G2 -. reads .-> G1
    G3 -. invokes .-> G2
    G6 -. references .-> G4
    G6 -. references .-> G5

    C1 -. invokes .-> G3
    C1 -. invokes .-> G2
    C2 -. requires spec for .-> A1
    C2 -. requires spec for .-> A2
    C2 -. requires spec for .-> G1
    C3 -. builds .-> A5

    style L1 fill:#e8f4f8,stroke:#1f6feb,stroke-width:2px,color:#0b3d5c
    style L2 fill:#fdf6e3,stroke:#b58900,stroke-width:2px,color:#5c4b00
    style L3 fill:#f0e6f6,stroke:#7d3c98,stroke-width:2px,color:#3d1f5c
```

## Reading the diagram

- **Solid arrows** inside Layer 1 represent content flow: authored Markdown → generated `site/`.
- **Dashed arrows** between layers represent *invocation* or *enforcement*: CI workflows invoke scripts; scripts read policy files; CAS skills reference rules and patterns.
- **Each layer has a distinct color** to make boundaries visible at a glance.
- The `site/` node is shown as a **cylinder** to signal that it is generated output, not authored content.

## How this maps to code

| Diagram node | Repo path |
|--------------|-----------|
| A1 | `docs/*.md` (top-level pages) |
| A2 | `docs/narratives/*.md` |
| A3 | `docs/assets/` |
| A4 | `docs/diagrams/*.md` (this file) |
| A5 | `site/` (generated) |
| G1 | `governance/terminology.yaml` |
| G2 | `scripts/validate_governance.py` |
| G3 | `scripts/run_governance.sh` |
| G4 | `.cas/rules/architecture_rules.md` |
| G5 | `.cas/patterns/patterns-catalogue.yaml` |
| G6 | `.cas/cas-add-or-modify-feature/`, `.cas/cas-refactor-module/` |
| C1 | `.github/workflows/portfolio-governance.yml` |
| C2 | `.github/workflows/cas-validate-sdd.yml` |
| C3 | `.github/workflows/deploy.yml` |

See `ARCHITECTURE.md` §2 for the narrative explanation of each layer.