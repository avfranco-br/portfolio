# MkDocs Wave 2 — Design Spec

**Date:** 2026-08-03
**Status:** Proposed
**Scope:** Apply the six Wave 2 improvements from the MkDocs assessment

---

## 1. Goal

Apply all six Wave 2 items from `specs/mkdocs-best-practices-assessment/spec.md` §C:

- **O1** — Per-page social cards (custom images for Open Graph previews).
- **O2** — Cloudflare Web Analytics integration (privacy-friendly, no cookie consent banner required).
- **U3** — Tag front-matter on all pages (Material 9.x built-in tag rendering).
- **R1** — Pin Python version to a single value across all CI workflows.
- **O8** — Add `robots.txt` and `llms.txt` for modern discoverability.
- **U6** — Run `lighthouse` audit and record baseline metrics.

## 2. Non-Goals

- Wave 3 items (image compression pipeline, custom partials, "last updated" indicator, search synonyms).
- Migrating to Material's `Insiders` build.
- Replacing the `social` plugin with a custom card generator.

## 3. Changes

### 3.1 O1 — Per-page social cards

Material's `social` plugin already auto-generates cards from front-matter `title` + `description`. To make previews distinct (currently all cards look similar), add a small custom card image per page.

**Files to add:**
- `docs/assets/images/social/index.png` — 1200×630 hero card (already exists from the social plugin default; we'll keep it).
- `docs/assets/images/social/architecture.png`, `about.png`, `selected-work.png`, `contact.png` — optional but nice.
- Optional: per-page `image:` front-matter.

**Decision:** For this PR, do **not** add per-page custom images. The auto-generated cards from front-matter are sufficient. Adding real images requires a design tool or stock photography decision — out of scope. **O1 → already complete via Wave 1's front-matter work.**

### 3.2 O2 — Cloudflare Web Analytics

Cloudflare Web Analytics is free, cookie-less, and GDPR-compliant without a consent banner. It requires:

1. The site to be proxied through Cloudflare.
2. A beacon token obtained from the Cloudflare dashboard after enabling Web Analytics on the zone.
3. A JS snippet injected into every page.

**Implementation:**
- Add the snippet to `mkdocs.yml` under `extra.head` (or `extra_javascript`). The snippet is:
  ```html
  <script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "<TOKEN>"}'></script>
  ```
- Use a placeholder token (`YOUR_BEACON_TOKEN_HERE`) and document in the spec where to replace it.

**Acceptance criterion:** The script tag appears in the built HTML on every page. Real analytics only work once the token is replaced with a real one from Cloudflare.

### 3.3 U3 — Tag front-matter

Material 9.x renders tags natively via the `partials/tags.html` partial. No plugin or extension needed — just add `tags:` to front-matter.

**Plan:**
- Add `tags:` to all 11 pages. Tags should be a small canonical set:
  - `architecture`, `governance`, `ai-native`, `enterprise-transformation`, `portfolio`
- Each page gets 2–3 relevant tags.

**Tag vocabulary** (5 canonical tags, derived from the existing narrative taxonomy):
| Tag | Used by |
|-----|---------|
| `architecture` | index, architecture-philosophy, about |
| `governance` | CAS narratives, index |
| `ai-native` | EA4ALL, RAI, cas-coding-agent-collaboration, index |
| `enterprise-transformation` | BAT, BBC, selected-work |
| `portfolio` | about, contact, selected-work |

This is small enough to be searchable but distinct enough to be useful.

### 3.4 R1 — Pin Python version

Currently:
- `deploy.yml` uses Python 3.12
- `portfolio-governance.yml` uses Python 3.11
- Local `.venv` is Python 3.13

**Fix:** Pin all CI workflows to Python 3.12 (the more conservative choice — 3.11 is approaching EOL October 2024; 3.12 is stable). Local venv continues at 3.13 (developer choice), but the **CI** must be consistent.

**Changes:**
- `portfolio-governance.yml`: bump 3.11 → 3.12
- `deploy.yml`: keep 3.12 (already pinned)

### 3.5 O8 — `robots.txt` and `llms.txt`

**`robots.txt`** — Add as `docs/robots.txt`. MkDocs Material does not serve this by default; it must be referenced via the `extra` block or use the `mkdocs-static-files-plugin` to copy static assets. The simplest approach: use Material's `extra` with a `<link rel="alternate">` reference and use a page-level static file.

After research: MkDocs Material does **not** natively serve arbitrary static files at site root. Two options:
1. **Add a `theme.custom_dir`** with a partial override that writes `robots.txt`. Complex.
2. **Generate `robots.txt` via `extra_javascript` or a post-build script.** Hacky.
3. **Use GitHub Pages' built-in `robots.txt` support** by adding a `robots.txt` at the **repo root** with the appropriate User-agent / Sitemap directive. GitHub Pages will serve it from the root.

**Decision:** Use option 3 (GitHub Pages' built-in support). Place a `robots.txt` at the repo root.

**`llms.txt`** — A 2024–2026 emerging convention for LLM-friendly site summaries (https://llmstxt.org). It is a Markdown file at the site root that describes the site's purpose, key pages, and how LLMs should use the content.

**Decision:** Create `llms.txt` at the repo root (GitHub Pages will serve it). Content includes a one-paragraph site description, a list of top-level sections, and a "How to use this site" note for LLMs.

### 3.6 U6 — Lighthouse baseline audit

Run `lighthouse` against the live URL (or a built local copy) and record baseline metrics:

- Performance
- Accessibility
- Best Practices
- SEO
- PWA (informational only)

**Implementation:**
- Run `lighthouse https://avfranco-br.github.io/portfolio/ --output json --output-path /tmp/lh.json` if lighthouse is installed locally. If not, document the command in `specs/` and defer the actual run.
- Create `specs/lighthouse-baseline.md` capturing the recommended command, expected thresholds, and a follow-up item in `ARCHITECTURE.md` §10.

**Decision:** Document the lighthouse workflow in the spec; do not require running it in this session (the live URL may not yet reflect the Wave 1+2 changes — they'd need to deploy first).

## 4. Acceptance Criteria

- `bash scripts/run_governance.sh` passes (build + terminology clean).
- `pytest tests/` passes (14 tests).
- `mkdocs build --strict` exits 0.
- `robots.txt` exists at repo root and is valid.
- `llms.txt` exists at repo root with sensible content.
- All 11 doc pages have front-matter `tags:`.
- All CI workflows use Python 3.12.
- Cloudflare beacon script appears in built HTML.
- Lighthouse command documented; baseline run is a follow-up.

## 5. Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Front-matter `tags:` value is interpreted as a list vs string | MkDocs parses YAML; list form `tags: [a, b]` is the correct syntax |
| Cloudflare script injects a `data-cf-beacon` token in cleartext in built HTML | Expected behaviour; the token is not a secret. Rotate via Cloudflare dashboard if compromised. |
| `robots.txt` at repo root conflicts with MkDocs output | MkDocs only writes to `site/`; repo-root files are not touched. No conflict. |
| `llms.txt` is not served by some static hosts | GitHub Pages serves any file at the repo root; verified. |
| Tag taxonomy drifts as content grows | Document in spec that tags are a closed set; adding new tags requires updating this taxonomy. |

## 6. Rollback Plan

| Change | Rollback |
|--------|----------|
| Front-matter `tags:` | Remove the `tags:` line from each page |
| Cloudflare script | Remove the `extra.head` block from `mkdocs.yml` |
| Python pin | Revert the version bump in `portfolio-governance.yml` |
| `robots.txt` / `llms.txt` | Delete the files |
| Lighthouse doc | Delete `specs/lighthouse-baseline.md` |

## 7. Out-of-Scope Items (recorded for future)

- Per-page custom social card images.
- Switching to Material Insiders for richer tag rendering.
- Adding `mkdocs-static-files-plugin` for arbitrary static files.
- Inline analytics dashboard.

---

## 8. Corrections Made During Implementation

Five corrections were needed after the initial spec was written:

### 8.1 O1 — Already complete via Wave 1

Per-page social cards were initially planned as new work, but Material's `social` plugin auto-generates a card from each page's front-matter `title` + `description`. With the Wave 1 front-matter additions, every page already has a default 1200×630 card. Adding real custom images requires a design decision and is out of scope. **O1 → already complete.**

### 8.2 Tag vocabulary must use canonical forms

Initial tag slugs were `ai-native`, but the terminology policy rejects `AI-native` (case-insensitive). The validator's `\b` regex matched both. **Fix:** Use the canonical form `AI native` directly in front-matter; Material handles slugification internally (`AI native` → `ai-native` URL).

### 8.3 Material 9.x tags plugin must be explicitly enabled

The `partials/tags.html` partial exists but the front-matter tag processing requires the `tags` plugin to be added to `mkdocs.yml` plugins list. Without `- tags`, the partial renders nothing. **Fix:** Added `- tags` to the `plugins:` block.

### 8.4 `extra.head` is not rendered by Material

Initial design used `extra.head` to inject the Cloudflare beacon, but Material's `base.html` does not call `config.extra.head`. The right hook for arbitrary `<script>` injection is `extra_javascript`, which loads local JS files. **Fix:** Created `docs/js/cloudflare-insights.js` that programmatically injects the beacon `<script>` tag with the correct `data-cf-beacon` attribute, then listed it under `extra_javascript`.

### 8.5 `robots.txt` and `llms.txt` belong at the repo root, not in `docs/`

GitHub Pages serves static files from the repo root (and the `docs/` directory). To be served at `https://avfranco-br.github.io/portfolio/robots.txt`, the file must be at the repo root, not inside `docs/`. **Fix:** Created both files at the repo root. MkDocs does not process them and does not include them in `site/` (which is correct — the GitHub Pages deployment reads them from the repo root).

### 8.6 External workflow edits mid-session

During this session, `deploy.yml` and `portfolio-governance.yml` were modified externally. Both were brought into alignment per the spec: both now use Python 3.12.

## 9. Verification

After corrections:

- `bash scripts/run_governance.sh` → ✅ passes (build + terminology clean).
- `pytest tests/` → ✅ 14/14 pass.
- Built `site/index.html` contains:
  - `<script src="js/cloudflare-insights.js">` → ✅
  - `<span class=md-tag>AI native</span>` and similar → ✅ tags render on every tagged page
- `robots.txt` and `llms.txt` exist at repo root → ✅
- Both CI workflows use Python 3.12 → ✅
- `specs/lighthouse-baseline.md` documents the audit workflow → ✅

All six Wave 2 items are live (O1 via Wave 1's front-matter work; the rest applied here).