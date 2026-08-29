# Design System: Alexandre Franco Enterprise Architecture Portfolio
**Project ID:** `avfranco-br/portfolio`

## 1. Visual Theme & Atmosphere
The design system of the **Alexandre Franco Enterprise Architecture Portfolio** conveys an **executive, authoritative, high-trust, and minimalist** atmosphere. Built upon a customized MkDocs Material foundation, the design emphasizes clean visual hierarchy, generous structural whitespace, dual-mode theme flexibility (Light & Dark), and sharp typography suitable for enterprise architecture decision-makers and C-suite leadership.

---

## 2. Color Palette & Roles

### Light Theme (Default)
* **Pristine Canvas White (`#ffffff`):** Primary page background and hero container surface.
* **Deep Charcoal Heading (`#1a1a1a` / `#000000`):** Primary typography for high-contrast titles (`h1`, `h2`) and hero headers.
* **Executive Indigo Accent (`#3f51b5`):** Accent color for subtitle badges, interactive button highlights, link states, and focus outlines.
* **Muted Slate Subtext (`#64748b`):** Secondary metadata, venture labels, and paragraph body text.
* **Subtle Neutral Border (`#e0e0e0`):** Card container outlines, external link tags, and horizontal section dividers.

### Dark Theme (Slate)
* **Midnight Slate Background (`#0f172a`):** Deep dark mode canvas background.
* **Elevated Surface Slate (`#1e293b`):** Dark mode card backgrounds, navigation bars, and dropdown containers.
* **High-Contrast Off-White Text (`#f8fafc`):** Primary text color for dark mode reading comfort.
* **Bright Indigo Highlight (`#5c6bc0`):** Accent color for links, buttons, and active tabs in dark mode.

---

## 3. Typography Rules

* **Font Stack:** Clean sans-serif system stack (`Roboto`, `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `sans-serif`).
* **Title (`h1`):** `2.5rem` (40px), font weight `800` (Extra Bold), tight line height (`1.15`), borderless bottom.
* **Section Header (`h2`):** `1.5rem` to `1.75rem`, font weight `700` (Bold), with bottom margin spacing for card grid separation.
* **Subtitle Copy:** `1.25rem` (20px), font weight `600` (Semi-Bold), styled in Executive Indigo.
* **Body Copy:** `1.0rem` (16px), font weight `400` (Regular), comfortable line height (`1.6`).
* **Code / Monospace:** System monospace (`Roboto Mono`, `ui-monospace`, `SFMono-Regular`) used for architecture tags, classification levels, and CLI snippets.

---

## 4. Component Stylings

* **Buttons (`.md-button`):**
  * **Primary Action:** Solid Executive Indigo (`#3f51b5`) background, white text, 4px border radius (`rounded-sm`), 8px 16px padding.
  * **Secondary / Outline:** Transparent background with subtle border outline (`1px solid var(--md-default-fg-color--lighter)`), 4px border radius, high-contrast hover fill.
* **Cards & Grid Containers (`.grid.cards`):**
  * Rectangular cards with subtle border outlines (`1px solid var(--md-default-fg-color--lighter)`).
  * Rounded corners (`4px` border radius).
  * Internal padding (`1rem` to `1.25rem`).
  * Right-arrow octicon link indicator (`:octicons-arrow-right-24:`) for engagement navigation.
* **Venture Badges:**
  * Compact inline pill/box tags (`padding: 0.25rem 0.65rem`).
  * Border radius `4px`, 1px subtle neutral border.
  * Typography: `0.85rem` font size with trailing external arrow `↗`.
* **Profile Headshot Frame:**
  * Circular thumbnail (`border-radius: 50%`, `150px` width x `150px` height).
  * 3px solid background-matched border (`var(--md-default-bg-color)`).
  * Subtle elevation drop shadow (`box-shadow: 0 4px 12px rgba(0,0,0,0.15)`).
* **Admonitions & Alerts (`> [!NOTE]`, `> [!TIP]`):**
  * Left accent bar (`4px` solid indigo/accent color).
  * Soft tinted background fill (`var(--md-admonition-bg)`).
  * Bold title header with inline SVG icon indicator.

---

## 5. Layout Principles

* **Hero Container (`.mdx-hero`):** Maximum width `900px`, centered flex layout (`align-items: center`, `justify-content: space-between`, `gap: 2rem`), responsive flex wrapping (`flex: 1 1 480px` text block vs `flex: 0 0 160px` avatar block).
* **Content Width:** Main body text bounded at `1200px` max width with `2rem` horizontal margins for optimal readability.
* **Grid Layout:** Responsive multi-column CSS Grid (`.grid.cards`) for portfolio engagements and core capability themes.
* **Navigation:** Sticky top navigation bar (`navigation.tabs.sticky`), automatically hidden on the primary hero index page for an uncluttered landing experience.
