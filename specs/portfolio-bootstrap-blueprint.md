# Portfolio MVP Implementation Blueprint

**Status:** Draft / Approved
**Context:** Enterprise Architecture, Systems-Thinking, Governance-Oriented Portfolio
**Stack:** MkDocs Material, Markdown, GitHub Pages
**Focus:** Minimal, Maintainable, Documentation-First

---

## 1. Repository Structure

The MVP repository structure prioritises clear separation of concerns, ensuring that the documentation-first approach is unencumbered by complex build tooling.

```text
avfranco-portfolio/
├── .cas/                     # Architecture & Governance Rules (pre-existing)
├── .github/
│   └── workflows/
│       └── deploy.yml        # GitHub Actions workflow for Pages deployment
├── docs/                     # Root documentation directory
│   ├── assets/               # Static assets (images, branding)
│   │   ├── images/           # Images assets
│   ├── narratives/           # Transformation narratives
│   │   ├── cas.md            # Continuous Architecture System
│   │   ├── rai.md            # Governance-Oriented AI Operationalisation (Runner Agentic Intelligence experiment)
│   │   └── ea4all.md         # Architecture with Transparency, Efficiency, and Collaboration
│   ├── diagrams/             # Visual architectural diagrams (mermaid, SVG, drawio, etc)
│   ├── index.md              # Homepage V1
│   ├── about.md              # Professional summary
│   ├── philosophy.md         # Architecture Philosophy
│   ├── selected-work.md      # Case studies & deliverables
│   └── contact.md            # Contact and links
├── specs/                    # Specifications and Design Docs (this file)
├── mkdocs.yml                # MkDocs configuration
├── requirements.txt          # Python dependencies (MkDocs + Material)
└── README.md                 # Repository overview and operational guide
```

### Folder Analysis & Governance
- **`docs/`**: The core source of truth. Governance Value: Decouples content from presentation. Future: Easily modularised using MkDocs macros if necessary.
- **`docs/narratives/`**: Dedicated space for deep-dive transformational cases. Governance Value: Promotes structured case studies over disjointed blogs. Future: Can evolve into a full knowledge base.
- **`.github/workflows/`**: Infrastructure as Code (IaC) for deployment. Governance Value: Ensures repeatable, automated, repeatable and low-friction deployments. Future: Integration of link checkers and markdown linting.
- **`specs/`**: Architectural documentation (SDD). Governance Value: Enforces "think before building". Future: Storage for Architectural Decision Records (ADRs).

---

## 2. MkDocs Bootstrap Instructions

To bootstrap the site locally and begin authoring, follow these concise operational steps:

### Installation
Assuming macOS, `zsh`, and `uv` for modern Python package management:

```bash
# 1. Initialise the virtual environment
uv venv

# 2. Activate the virtual environment
source .venv/bin/activate

# 3. Create requirements.txt
echo "mkdocs-material\nmkdocs-roamlinks-plugin" > requirements.txt

# 4. Install dependencies
uv pip install -r requirements.txt
```

### Local Development Commands
```bash
# Start the local live-reloading server
mkdocs serve

# Build the static site (to test the output in ./site)
mkdocs build
```

---

## 3. Recommended `mkdocs.yml`

This configuration provides a calm, executive-readable aesthetic out of the box, with minimal plugins to avoid operational bloat.

```yaml
site_name: Alexandre Franco | Enterprise Architect
site_description: Enterprise Architecture, Systems Thinking, and Governance Operationalisation
site_author: Alexandre Franco
site_url: https://avfranco.github.io/avfranco-portfolio/

theme:
  name: material
  favicon: assets/images/favicon.png
  icon:
    logo: material/library
    repo: fontawesome/brands/github
  features:
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.sections
    - navigation.top
    - search.suggest
    - search.highlight
    - toc.integrate
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: white
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: black
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - toc:
      permalink: true

nav:
  - Home: index.md
  - About: about.md
  - Architecture Philosophy: philosophy.md
  - Transformation Narratives:
      - Continuous Architecture System (CAS): narratives/cas.md
      - Governance-Oriented AI (RAI): narratives/rai.md
      - EA4All / Architecture Visibility: narratives/ea4all.md
  - Selected Work: selected-work.md
  - Contact: contact.md
```

---

## 4. Initial Homepage Structure (`docs/index.md`)

The homepage serves as an executive summary and entry point. Do not over-engineer; rely on clean typography and Markdown grids if necessary.

```markdown
# Building Systems. Operationalising Governance. Enabling Transformation.

---

## Introduction
<!-- Placeholder: Brief 2-3 sentence executive summary of my role, focusing on connecting business strategy to technical execution via systems thinking and governance. -->

## Core Capabilities
<!-- Placeholder: Bulleted list or a clean grid outlining key strengths:
- Enterprise Architecture & Systems Thinking
- Governance Operationalisation
- AI Systems & RAI Frameworks
- Technical Strategy & Alignment
-->

## Transformation Narratives
<!-- Placeholder: Links to the core narratives.
- [Continuous Architecture System (CAS)](narratives/cas.md)
- [Governance-Oriented AI (RAI)](narratives/rai.md)
- [EA4All / Architecture Visibility](narratives/ea4all.md)
-->

## Architecture Philosophy
<!-- Placeholder: A single paragraph summarising the philosophy, linking to the full Philosophy page. -->

## Get in Touch
<!-- Placeholder: Link to Contact page or direct professional links (LinkedIn). -->
```

---

## 5. Transformation Narrative Structure

Transformation narratives replace traditional "blogs". They are structured analyses of systemic improvements.

**Directory:** `docs/narratives/`
**Naming Convention:** `[topic-acronym-or-short-name].md` (e.g., `cas.md`, `rai.md`).

### Narrative Template Structure
Each narrative should adhere to this Markdown structure:

```markdown
# [Narrative Title]

## Context & The Problem Space
<!-- Outline the systemic friction or business challenge. -->

## The Architectural Approach
<!-- The philosophy and strategy used to address the problem. Why was this approach chosen? -->

## Implementation & Operationalisation
<!-- How the strategy was executed. Focus on governance, constraints, and process change. -->

## Impact & Value Delivered
<!-- Tangible outcomes, behavioural shifts, and systemic improvements. -->
```

### Governance Guidance
- Narratives must remain objective and analytical.
- Avoid subjective storytelling; focus on the system, the architecture, and the outcome.
- Use Mermaid diagrams to illustrate the "Before" and "After" systemic states.

---

## 6. Architecture Philosophy Structure (`docs/philosophy.md`)

This page grounds the portfolio in a distinct, professional methodology.

```markdown
# Architecture Philosophy

## Systems Thinking Over Siloed Execution
<!-- Guidance: Discuss the importance of viewing the enterprise as a holistic system. -->

## Governance as an Enabler, Not a Blocker
<!-- Guidance: Explain how operationalised governance accelerates delivery by removing ambiguity. -->

## Operational Sustainability
<!-- Guidance: Focus on maintainability, simplicity, and building for the long term. -->

## The Role of the Architect
<!-- Guidance: The architect as a connector between strategy and execution, not an ivory tower academic. -->
```

**Guidance:** Keep the tone executive, pragmatic, and grounded in operational reality. Avoid hyperbole, "AI revolution" clichés, and manifesto-style preaching.

---

## 7. Visual & UX Guidance

- **Typography:** Rely on MkDocs Material defaults (Roboto / Roboto Mono). They are highly legible and professional.
- **Colour Palette:** Use the defined `default`/`slate` schemes with a neutral primary colour (White/Black) and a subdued accent (Indigo/Teal). Avoid aggressive brand colours.
- **Content Density:** Embrace whitespace. Use short paragraphs, bullet points, and `admonition` blocks (Note, Abstract, Info) for highlighting key architectural principles without breaking the reading flow.
- **Diagrams:** Use native Mermaid.js blocks for system context diagrams. Ensure diagrams are minimal, well-labelled, and use standard architectural conventions (e.g., C4 model concepts).
- **Navigation Behaviour:** Utilise top-level tabs for primary sections, with sidebars reserved for page-level Table of Contents. This mimics high-end technical documentation.

---

## 8. GitHub Pages Deployment Workflow

A zero-touch deployment model using GitHub Actions.

**File:** `.github/workflows/deploy.yml`

```yaml
name: Deploy MkDocs Portfolio
on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install mkdocs-material
      - name: Deploy to GitHub Pages
        run: mkdocs gh-deploy --force
```

**Operational Maintenance Guidance:**
- Commits to `main` automatically deploy to the `gh-pages` branch.
- Ensure GitHub Repository Settings -> Pages is set to deploy from the `gh-pages` branch (Root).

---

## 9. Suggested Initial Commit Sequence

1. **`docs: bootstrap MkDocs structure and specifications`**
   *Why:* Establishes the foundation and architectural intent (this document) before execution.
2. **`build: configure mkdocs.yml and base dependencies`**
   *Why:* Sets up the application engine and navigational skeleton.
3. **`feat: add homepage and philosophy scaffolds`**
   *Why:* Provides the entry point and foundational framing of the portfolio.
4. **`feat: add transformation narrative structures`**
   *Why:* Instantiates the core value-delivery content areas.
5. **`ci: configure GitHub Actions deployment workflow`**
   *Why:* Automates the path to production immediately, adhering to IaC principles.
6. **`docs: publish initial MVP content`**
   *Why:* Final review and pushing the initial text, triggering the first live deployment.

---

## 10. MVP Scope Protection Guidance

**MANDATORY ENFORCEMENT:** To preserve the integrity and maintainability of the MVP, the following are strictly OUT OF SCOPE for this phase:

- **NO Custom CSS/JS Bloat:** Do not override MkDocs Material styling unless absolutely critical for readability.
- **NO Advanced Frontend Frameworks:** No React, Vue, or Astro. If it cannot be expressed in Markdown or Mermaid, it does not belong in the MVP.
- **NO Backend APIs or Databases:** The portfolio is entirely static. Form submissions should be handled via `mailto:` links or external services (e.g., LinkedIn) for the MVP.
- **NO Complex Telemetry:** Do not implement Google Analytics or advanced tracking in Phase 1. Focus on publication over observation.
- **NO Pre-mature Automation:** Do not build complex Python scripts to auto-generate markdown files from external data sources yet.
- **NO Heavy AI Features:** While the content discusses Governance-Oriented AI, the portfolio itself should not integrate LLM chatbots or dynamic AI generation at runtime.

**Scope Protection Strategy:** Any request to deviate from the Markdown-first, static MkDocs architecture must be documented in a new specification and explicitly challenged against the "Maintainable by one person" principle.