# Lighthouse Baseline Audit

**Date:** 2026-08-03
**Status:** Workflow documented; baseline run is a follow-up after Wave 2 deploys

---

## Why this exists

The MkDocs assessment (`specs/mkdocs-best-practices-assessment/spec.md`) recommended a Lighthouse audit as Wave 2 item U6. This document captures the recommended command, expected thresholds, and the procedure for recording baseline metrics.

## When to run

After the Wave 2 changes have been deployed to `https://avfranco-br.github.io/portfolio/`. The audit measures the live site, not the local build.

## Command

Run from any directory:

```bash
npx lighthouse https://avfranco-br.github.io/portfolio/ \
  --output html \
  --output-path ./lighthouse-report.html \
  --chrome-flags="--headless --no-sandbox" \
  --only-categories=performance,accessibility,best-practices,seo
```

For JSON output (easier to diff):

```bash
npx lighthouse https://avfranco-br.github.io/portfolio/ \
  --output json \
  --output-path ./lighthouse-report.json \
  --chrome-flags="--headless --no-sandbox" \
  --only-categories=performance,accessibility,best-practices,seo
```

## Expected thresholds

| Category | Target | Notes |
|----------|--------|-------|
| Performance | ≥ 90 | MkDocs Material sites typically score 95–100 on static hosting |
| Accessibility | ≥ 95 | Material defaults are good; verify skip-to-content and ARIA landmarks |
| Best Practices | ≥ 90 | Should be high; check console errors and HTTPS usage |
| SEO | ≥ 95 | Front-matter `title` + `description` (Wave 1) help; verify sitemap and meta description |

## Procedure

1. **Install lighthouse** (one-off): `npm install -g lighthouse`
2. **Run the audit** against the live URL.
3. **Record results** in a new section below — append a dated entry with the four scores.
4. **Open issues** for any category below threshold.

## Baseline run

*(To be recorded after Wave 2 deploys.)*

| Date | Performance | Accessibility | Best Practices | SEO | Notes |
|------|-------------|---------------|----------------|-----|-------|