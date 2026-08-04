# Data Model & Content Schema

**Feature**: Portfolio Look & Feel Restructure (MkDocs Material)  
**Branch**: `001-portfolio-restructure`  
**Date**: 2026-08-04

---

## Conceptual Entities & Layout Schemas

This portfolio operates as a static site. The "data model" represents structural Markdown and HTML template components that enforce visual consistency.

---

### 1. Executive Hero Component (`overrides/home.html` / `index.md`)

Represents the landing hero layout on the homepage.

```yaml
HeroComponent:
  Name: "Alexandre Franco"
  Title: "Enterprise Architect & AI Transformation Advisor"
  IntroCopy: "I'm Alexandre Franco. Over the past 20 years..." # From Spec 001
  HeadshotContainer:
    Src: "assets/images/headshot.jpg" # Or placeholder HTML comment (Tier 2)
    Alt: "Alexandre Franco"
  ActionButtons:
    - Label: "Selected Work"
      Href: "#selected-work"
      Style: "md-button md-button--primary"
    - Label: "Contact"
      Href: "contact/"
      Style: "md-button"
    - Label: "Mostelli"
      Href: "https://mostelli.com"
      External: true
    - Label: "Ideas to Life"
      Href: "https://ideas-to-life.ai"
      External: true
```

---

### 2. Selected Work Card Grid (`index.md` / `selected-work.md`)

Represents the card grid component for narrative navigation.

```yaml
CardGridComponent:
  ContainerClass: "grid cards"
  Cards:
    - Id: "bat-transformation"
      Title: "BAT Transformation"
      Icon: ":material-office-building:"
      Summary: "One-sentence lead summary extracted from BAT narrative."
      TargetUrl: "narratives/bat-transformation.md"
    - Id: "bbc-studios"
      Title: "BBC Studios Digital Evolution"
      Icon: ":material-television-classic:"
      Summary: "One-sentence lead summary extracted from BBC Studios narrative."
      TargetUrl: "narratives/bbc-studios-digital-evolution.md"
    - Id: "ea4all"
      Title: "EA4ALL AI Native Enterprise Architecture"
      Icon: ":material-brain:"
      Summary: "One-sentence lead summary extracted from EA4ALL narrative."
      TargetUrl: "narratives/ea4all.md"
    - Id: "cas"
      Title: "Continuous Architecture System (CAS)"
      Icon: ":material-shield-sync:"
      Summary: "One-sentence lead summary extracted from CAS narrative."
      TargetUrl: "narratives/cas.md"
```

---

### 3. Engagement Narrative Schema (`docs/narratives/*.md`)

Defines the required section hierarchy for narrative pages.

```yaml
EngagementNarrative:
  Title: String # Level 1 Heading (# Title)
  Metadata:
    Type: "Case Study"
    Role: String
  Sections:
    Challenge:
      Heading: "## Challenge"
      Body: String # Existing background & problem space prose
    Approach:
      Heading: "## Approach"
      Body: String # Existing architecture & execution strategy prose
    Outcome:
      Heading: "## Outcome"
      Body: String # Existing results, impact & takeaways prose
```

---

### 4. OKF Asset Sourcing Mapping (Tier 2)

Maps local OKF knowledge bundle data to portfolio static files.

| OKF Bundle Source | Target Location in Portfolio | Presentation Format |
|---|---|---|
| `headshot.png` / `headshot.jpg` | `docs/assets/images/headshot.jpg` | Hero image |
| `certifications.yml` | `docs/index.md` / `docs/about.md` | Material icon/badge row |
| `cv_latest.pdf` | `docs/assets/alexandre-franco-cv.pdf` | Downloadable PDF CTA link |
| `career_timeline.yml` | `docs/about.md` | Vertical milestone list |
