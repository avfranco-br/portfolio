# Spec 003: Portfolio Look & Feel Restructure (MkDocs Material)

**Site:** `alexandrefranco.dev` (MkDocs Material, GitHub Actions deploy)
**Status:** Partially ready for implementation — see Two-Tier Scope below
**Depends on:** Spec 001 (homepage copy — assumed implemented; this spec relocates that copy into a new hero component rather than replacing it)
**Blocks:** None

---

## Context

The current site uses MkDocs Material's default documentation layout: left sidebar navigation, dense prose blocks, no hero/identity section, no visual distinction between career engagements. This reads as a technical wiki, not a personal career portfolio. The goal is to restructure the *presentation* — templates, layout, visual components — without migrating, deleting, or trimming any existing written content (per the standing decision from the Spec 001/002 discussion: no content moves until Mostelli has a confirmed destination for CAS/EA4ALL).

This spec stays within MkDocs Material (no framework migration) to avoid disrupting the GitHub Actions pipeline and custom domain just stabilized in Spec 002.

## Goal

Make the site visually read as a portfolio: a personal hero/landing moment, card-based navigation into work rather than sidebar-only browsing, and consistent visual structure for each career engagement — while every existing page and its full content remains intact and reachable.

## Non-Goals (explicitly out of scope for this spec)

- Do NOT delete, shorten, or migrate any existing narrative content (BAT, BBC Studios, EA4ALL, CAS, etc.) — restructure presentation only, not content ownership. (Standing decision from prior sessions.)
- Do NOT remove any existing page or nav destination — pages may be *presented* differently (e.g. surfaced as cards from the homepage) but must remain individually reachable at their current URLs to avoid breaking any existing inbound links.
- Do NOT change `alexandrefranco.dev` DNS, Cloudflare, or GitHub Pages settings (covered by Spec 002, already complete).
- Do NOT touch mostelli.com or ideas-to-life.ai.
- Do NOT migrate the framework to Astro or any non-MkDocs stack (explicit decision — Option A chosen over Option B).

---

## Two-Tier Scope

**Tier 1 — Implementable now (no new assets required from Alexandre):**
R1, R2, R3 below. These restructure existing text/layout only.

**Tier 2 — Needs assets from Alexandre before implementation:**
R4, R5, R6, R7 below. Each names exactly what's needed. Agent should implement Tier 1 first and flag Tier 2 items as blocked-pending-input rather than guessing placeholder content.

---

## Tier 2 Content Sourcing: OKF Knowledge Bundle

Tier 2 content (R4–R7) is maintained by Alexandre as a Google OKF (Open Knowledge Format) bundle — a directory of markdown files with YAML frontmatter — stored separately from the portfolio repo. The coding agent should **read this bundle directly** at implementation time rather than have content manually re-typed into this spec, since OKF is designed to be agent-readable without translation and avoids transcription drift (typos in cert names, wrong years in the timeline, etc.).

**Access:** The OKF bundle lives in a separate local directory/repo. Alexandre will provide the exact path when kicking off Tier 2 implementation — grant the agent read access to that path alongside the portfolio repo for that session.

**Sourcing approach:** Static generation only. The agent should read the relevant OKF fields at implementation time and emit plain markdown/HTML/CSS into the portfolio site (consistent with the rest of the site being a static MkDocs build) — not wire up any live/runtime query against the knowledge graph. If Alexandre wants the site to reflect future OKF updates automatically, that would be a build-time re-fetch step (e.g. a workflow step that pulls the latest OKF bundle before `mkdocs build`) — flag this as a separate decision, out of scope for this spec unless explicitly requested.

**Field mapping (agent to confirm against actual OKF schema, adjust as needed):**
- R4 (headshot) — locate the image asset reference in the bundle; copy the actual image file into `docs/assets/images/`.
- R5 (certifications) — locate the structured cert list (name, issuing body, date if present); render as the badge row.
- R6 (CV/résumé) — locate the CV file reference or generate from structured career data if no single PDF exists in the bundle; confirm with Alexandre which is the case before assuming.
- R7 (career timeline) — locate the structured role/org/date-range entries; render chronologically.

If any Tier 2 item's data isn't present in the OKF bundle in the expected shape, the agent should flag it back rather than inventing values — same rule as before, just now checking the bundle instead of asking Alexandre to type it out.



### R1 — Custom hero homepage template (Tier 1)

Add a homepage template override (`overrides/home.html` extending Material's `main.html`, or equivalent per current MkDocs Material theming setup — verify against existing `mkdocs.yml` `theme.custom_dir` config, create if not present).

In the homepage's frontmatter, set:
```yaml
hide:
  - navigation
  - toc
```
so the homepage renders as a full-width hero rather than doc-sidebar layout.

Hero content, top to bottom:
1. Name: "Alexandre Franco"
2. Title line: "Enterprise Architect & AI Transformation Advisor"
3. The existing Spec 001 intro paragraph (the "I'm Alexandre Franco..." copy) — relocate it into this hero, don't duplicate it elsewhere.
4. CTA button row, linking to: Selected Work (in-site anchor/page), Contact (in-site page), [Mostelli](https://mostelli.com), [Ideas to Life](https://ideas-to-life.ai)
5. Placeholder for a headshot photo (see R4 — leave an `<img>` tag with a clearly marked placeholder `src` and an HTML comment `<!-- TODO: replace with headshot, see Spec 003 R4 -->` if the photo isn't available yet, rather than blocking the rest of the hero on it)

### R2 — Selected Work as a card grid (Tier 1)

Convert the homepage's/Selected Work index's current bullet-list or prose presentation of engagements into Material's built-in grid card syntax:

```markdown
<div class="grid cards" markdown>

-   :material-office-building: **BAT Transformation**

    ---

    One-line summary of the engagement.

    [:octicons-arrow-right-24: Read more](link-to-existing-page.md)

</div>
```

- Source the one-line summary from the existing page's own opening sentence — do not invent new claims, extract/lightly-trim from what's already written on that page.
- Each card links to the **existing, unmodified page** — this is a navigation/index change, not a content edit to the linked pages themselves.
- Apply this same card treatment to: BAT Transformation, BBC Studios, EA4ALL, CAS, and any other existing "Selected Work" entries currently in the nav.

### R3 — Consistent structure within each engagement page (Tier 1)

For each existing engagement page (BAT, BBC Studios, EA4ALL, CAS, etc.), add subheadings to organize the **existing** prose into a consistent pattern:

```markdown
## Challenge
## Approach
## Outcome
```

This is a re-heading/re-ordering task, not a rewrite: take the existing paragraphs and place them under the most fitting of these three headings. If a page's existing content doesn't cleanly map to all three sections, leave the ones that fit populated and note in a PR comment which section(s) had no corresponding existing content — do not fabricate content to fill gaps.

### R4 — Headshot photo (Tier 2 — blocked pending asset)

**Needed from Alexandre:** a professional headshot image file (JPEG/PNG, reasonably high resolution).

Once provided: add to `docs/assets/images/`, wire into the R1 hero template, remove the placeholder comment.

### R5 — Certifications/skills badges (Tier 2 — blocked pending input)

**Needed from Alexandre:** the exact list of certifications to display (e.g. confirm "TOGAF" and "SAFe" are current/complete, plus name the specific AI certifications currently just referenced generically).

Once provided: add a small badge/icon row near the hero or About section.

### R6 — Downloadable CV/résumé (Tier 2 — blocked pending asset)

**Needed from Alexandre:** a CV/résumé PDF.

Once provided: add to `docs/assets/` and link from the hero CTA row (R1) and/or Contact page.

### R7 — Career timeline (Tier 2 — blocked pending input)

**Needed from Alexandre:** a confirmed list of career milestones (role, organization, year range) to display as a simple vertical timeline.

Once provided: implement using Material's built-in support or a lightweight custom component — agent to propose approach once data is available, since the right implementation depends on how many entries there are.

---

## Acceptance Criteria

**Tier 1:**
- [ ] Homepage renders as a hero layout (no sidebar/TOC), containing name, title, Spec 001 copy, and working CTA links.
- [ ] Selected Work entries render as a card grid, each linking to its existing, unmodified page.
- [ ] Every existing page previously reachable via nav is still reachable (spot-check URLs before/after).
- [ ] Each engagement page has Challenge/Approach/Outcome subheadings applied to existing content, with no content deleted (word-count sanity check: page word count after ≥ word count before, allowing for heading text added).
- [ ] Site builds cleanly via the existing GitHub Action with no broken links.

**Tier 2 (per item, once unblocked):**
- [ ] R4: headshot displays correctly in hero, placeholder comment removed.
- [ ] R5: badge row displays the confirmed certification list.
- [ ] R6: CV download link works and serves the correct, current file.
- [ ] R7: timeline renders with confirmed milestones in correct chronological order.

## Rollback

Tier 1 changes are template/markdown-only and revertible via git. Tier 2 items are additive (new files/links) and can be removed independently without affecting Tier 1 structure.

## Open Items for Alexandre (needed to unblock Tier 2)

1. The filesystem path to the OKF knowledge bundle, and confirmation the agent will be granted read access to it for the Tier 2 implementation session.
2. Confirmation of whether the CV/résumé (R6) exists as a single file in the bundle, or needs to be generated from structured career data — the agent should not assume either way.

(Items previously listed as manual copy/paste — headshot, cert list, CV, career timeline — are now expected to be sourced from the OKF bundle per the sourcing section above, rather than typed out here.)
