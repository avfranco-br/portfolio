# MkDocs Quick Wins — Design Spec

**Date:** 2026-08-03
**Status:** Implemented (with two corrections during execution)
**Scope:** Apply four low-risk, high-impact MkDocs/Material improvements

---

## 1. Goal

Apply four quick-win improvements identified in the MkDocs/Material best-practices assessment:

1. **`mkdocs build --strict` in `deploy.yml`** — prevent silent broken deploys.
2. **`validation:` block in `mkdocs.yml`** — declare the policy in code rather than relying solely on the CLI flag (per-option log levels; see §7.1).
3. **`repo_url` + `edit_uri` in `mkdocs.yml`** — add "Edit this page" links to every page.
4. **Front-matter on `index.md` and `about.md`** — establish the pattern for browser-tab titles and SEO descriptions.

## 2. Non-Goals

- Adding front-matter to the remaining 9 pages (out of scope; this PR establishes the pattern only).
- Configuring the `social` plugin with per-card images.
- Adding analytics.
- Customising the theme.

## 3. Changes

### 3.1 `.github/workflows/deploy.yml`

Replace:

```yaml
- name: Build MkDocs
  run: mkdocs build
```

With:

```yaml
- name: Build MkDocs
  run: mkdocs build --strict
```

### 3.2 `mkdocs.yml`

Add the following blocks (merged into the existing structure without disturbing other config):

```yaml
# Site repository (enables "Edit this page" links)
repo_url: https://github.com/avfranco-br/portfolio
edit_uri: edit/main/docs/

# Declare validation policy in code (was previously only a CLI flag)
validation:
  links: strict
  nav: strict
  omitted_files: ignore
  absolute_links: warn
  unrecognized_links: warn
```

**Note:** `repo_url` and `edit_uri` together activate the "Edit this page" link in the Material theme footer. `repo_url` alone would activate a "View source" link in the header.

### 3.3 `docs/index.md`

Add YAML front-matter at the top:

```yaml
---
title: Alexandre Franco — Enterprise Architect & AI Transformation Advisor
description: Architecture, governance, and operational transformation for AI native delivery ecosystems.
---
```

### 3.4 `docs/about.md`

Add YAML front-matter at the top:

```yaml
---
title: About — Alexandre Franco
description: Career narrative and architectural operating philosophy.
---
```

## 4. Acceptance Criteria

- `bash scripts/run_governance.sh` passes (build + terminology clean).
- `pytest tests/` passes (14 tests).
- `mkdocs build --strict` exits 0 with the new `validation:` block.
- `deploy.yml` uses `mkdocs build --strict`.
- `index.md` and `about.md` render with the new front-matter title in the browser tab (verified by inspecting built HTML).
- `repo_url` produces an "Edit this page" link on a built page (verified by inspecting built HTML).

## 5. Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| `validation:` block flags a previously hidden broken link | The CI workflow already runs strict mode, so any real breakage should already be visible. If a new warning appears, fix it before merging. |
| `repo_url` adds a visible header link to GitHub | The repo is already public; this is a feature, not a bug. |
| Front-matter `title:` overrides H1 incorrectly | The H1 remains the visible heading; the front-matter `title` is what Material uses for the browser tab and nav title. This is the documented Material behaviour. |
| `edit_uri` path mismatch | `edit/main/docs/` assumes the default branch is `main`. Verified against `git status` showing branch `main`. |

## 6. Rollback Plan

Each change is independent. To rollback:

1. **deploy.yml** — revert the `--strict` flag.
2. **mkdocs.yml** — remove the `validation:` and `repo_url`/`edit_uri` blocks.
3. **index.md / about.md** — remove the YAML front-matter blocks.

No destructive operations; all changes are additive or replace-with-equivalent.

---

## 7. Corrections Made During Implementation

Two corrections were needed after the initial spec was written:

### 7.1 Validation sub-options take log levels, not booleans

The original spec wrote:

```yaml
validation:
  links: strict
  nav: strict
```

MkDocs rejected this with: `Sub-option 'nav': Expected a key-value mapping (dict) but received: <class 'str'>`. The valid values per sub-option are `warn`, `info`, or `ignore`. `strict` is a **CLI flag** (`mkdocs build --strict`) that converts warnings to errors; it is not a config value.

**Fix:** Set each sub-option to `warn` so it emits a warning, which `--strict` then promotes to failure. The actual config in `mkdocs.yml` is:

```yaml
validation:
  links:
    not_found: warn
    absolute_links: warn
    unrecognized_links: warn
    anchors: info
  nav:
    omitted_files: info
    not_found: warn
    absolute_links: warn
```

### 7.2 Per-page Edit link requires `content.action.edit` feature flag

Adding `repo_url` + `edit_uri` alone produced the header GitHub link but **not** the per-page pencil. The `actions.html` partial is conditional on `theme.features` containing `content.action.edit`.

**Fix:** Added `content.action.edit` to `theme.features` in `mkdocs.yml`. After this, every page renders with an Edit pencil pointing to `https://github.com/avfranco-br/portfolio/edit/main/docs/<page>.md`.

## 8. Verification

After corrections:

- `bash scripts/run_governance.sh` → ✅ passes (build + terminology clean).
- `pytest tests/` → ✅ 14/14 pass.
- Built `site/index.html` contains:
  - Header GitHub source link ✅
  - Per-page Edit pencil pointing to `https://github.com/avfranco-br/portfolio/edit/main/docs/index.md` ✅
  - Front-matter `<title>` and `<meta name="description">` ✅
  - Auto-generated Open Graph + Twitter Card meta tags ✅

The four quick wins are all live.