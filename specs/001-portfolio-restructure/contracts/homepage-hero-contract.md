# Interface Contract: Homepage Hero & Card Grid Layout

**Feature**: Portfolio Look & Feel Restructure  
**Target File**: `docs/index.md` and `overrides/home.html`

---

## 1. Frontmatter Contract (`docs/index.md`)

```yaml
---
template: home.html
title: Alexandre Franco | Enterprise Architect & AI Transformation Advisor
hide:
  - navigation
  - toc
---
```

- **`template: home.html`**: Directs MkDocs Material to render using the custom hero template.
- **`hide: [navigation, toc]`**: Suppresses sidebars so the content area spans the full page width.

---

## 2. Card Grid HTML Contract (`docs/index.md`)

```html
<div class="grid cards" markdown>

-   :material-office-building: **BAT Transformation**

    ---

    Enterprise-wide architecture modernization across global operations.

    [:octicons-arrow-right-24: Read engagement](narratives/bat-transformation.md)

-   :material-television-classic: **BBC Studios Digital Evolution**

    ---

    Digital media infrastructure transformation and platform architecture.

    [:octicons-arrow-right-24: Read engagement](narratives/bbc-studios-digital-evolution.md)

-   :material-brain: **EA4ALL AI Native Enterprise Architecture**

    ---

    AI-native architectural principles for enterprise intelligence systems.

    [:octicons-arrow-right-24: Read engagement](narratives/ea4all.md)

-   :material-shield-sync: **Continuous Architecture System (CAS)**

    ---

    Deterministic governance and specification-driven coding agent workflows.

    [:octicons-arrow-right-24: Read engagement](narratives/cas.md)

</div>
```
