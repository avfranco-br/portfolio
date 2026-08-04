# Spec 001: Portfolio Homepage Copy Rewrite

**Site:** `avfranco-br.github.io/portfolio` (MkDocs Material) — will move to `alexandrefranco.dev`
**Status:** Ready for implementation
**Depends on:** None (safe to implement immediately)
**Blocks:** None

---

## Context

The portfolio site's `mkdocs.yml` `site_name` and page `title` metadata have already been corrected to remove the "Ideas to Life" branding collision with ideas-to-life.ai. The homepage **body copy**, however, still uses platform/mission language ("this portfolio serves as an entry point into a broader ecosystem...") that duplicates the positioning of Mostelli (the business consulting site) and reads as a company/product site rather than a personal career portfolio.

This site's audience and purpose: a personal career portfolio, read primarily by (a) corporate recruiters/hiring managers evaluating senior Enterprise Architect roles, and (b) prospective business contacts doing due diligence before engaging Mostelli. It should read as first-person track record, not as a second business platform.

## Goal

Rewrite the homepage intro copy (the content currently under the `# Architecture. Governance. Operational Transformation.` heading, before the "Core Capability Themes" section) to:
1. Read as personal/first-person, not platform/mission language.
2. Clearly identify the author by name early in the copy.
3. Reference Mostelli and Ideas-to-Life as related properties, without restating their positioning or mission statements.
4. Preserve all existing structural content below this section (Core Capability Themes list, Architecture & Governance Narratives, Architecture Philosophy, Operational Perspective) — **do not edit or remove these sections in this spec.**

## Non-Goals (explicitly out of scope for this spec)

- Do NOT change the site nav structure.
- Do NOT remove, trim, or migrate any narrative pages (Enterprise Transformation, AI Native Systems, Governance Systems, CAS, EA4ALL, etc.).
- Do NOT touch `mkdocs.yml` `site_name`, page `title`, or meta description (already handled in a prior change).
- Do NOT add or modify domain/CNAME configuration.
- Do NOT create or edit any content on mostelli.com or ideas-to-life.ai.

## Requirements

### R1 — Replace homepage intro copy

Locate the homepage source file (`docs/index.md` or equivalent). Replace the introductory content block — from the opening bold statement through the paragraph ending "...capability-driven transformation" (i.e., everything between the `#` heading and the `### Core Capability Themes` heading) — with the following copy:

```markdown
**Enterprise Architect. AI Transformation Advisor.**

I'm Alexandre Franco — an Enterprise Architect with four decades of experience
across complex enterprise systems, now focused on operationalising AI within
governance-aware architecture practices.

This site is my career portfolio: selected engagements, architecture
philosophy, and the thinking behind the work I lead. I'm the founder of
[Mostelli](https://mostelli.com), an advisory practice helping organisations
align strategy, architecture, governance and AI, and I publish ongoing
experiments and patterns at [Ideas to Life](https://ideas-to-life.ai).
```

### R2 — Preserve the `#` page heading

Do not change the top-level page heading text (`# Architecture. Governance. Operational Transformation.`) — this spec only replaces the body paragraphs beneath it. (A future spec may revisit the heading itself.)

### R3 — Leave downstream sections untouched

Confirm the following sections remain byte-for-byte unchanged after this edit:
- `### Core Capability Themes`
- `### Architecture & Governance Narratives`
- `### Architecture Philosophy`
- `### Operational Perspective`
- Footer line with LinkedIn / Selected Work links

## Acceptance Criteria

- [ ] Homepage renders the new intro copy exactly as specified in R1.
- [ ] The words "ecosystem," "platform" (referring to the site itself), and "entry point" no longer appear in the homepage intro copy.
- [ ] "Alexandre Franco" appears by name within the first two sentences of body copy.
- [ ] Links to `mostelli.com` and `ideas-to-life.ai` are present and functional.
- [ ] No other file, page, or nav item is modified.
- [ ] Site builds successfully via `mkdocs build` with no broken links or warnings introduced by this change.

## Rollback

Single-file change to homepage source; revert via git if the rendered result doesn't match acceptance criteria.
