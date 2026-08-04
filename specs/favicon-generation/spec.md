# Favicon Generation — Design Spec

**Date:** 2026-08-03
**Status:** Proposed
**Scope:** Generate proper multi-size favicons from `docs/assets/images/favicon.png`

---

## 1. Problem

The repository has a portrait image saved as `docs/assets/images/favicon.png` (274×320 pixels, RGB). It is intended as the site's favicon, but:

1. The `mkdocs.yml` `theme.favicon` setting points to `assets/images/alexandrefranco.png` (a non-existent file).
2. The `favicon.png` file itself is not a properly-sized favicon — it is a full portrait. At the typical favicon display sizes (16×16, 32×32 in browser tabs), it will be downscaled and appear blurry or indistinct.
3. There is no Apple-touch-icon (180×180) or `.ico` multi-size asset for browser compatibility.

## 2. Goal

Generate a set of properly-sized favicon assets from the source portrait using Pillow (already installed via `mkdocs-material[imaging]`). Wire them into Material's theme.

## 3. Non-Goals

- Designing a new logo. The portrait is the source asset; we resample, not redesign.
- Adding SVG favicons (which would require vectorising the portrait — out of scope).
- Changing the site logo (the in-page header logo, controlled by `theme.icon.logo`).

## 4. Approach

### 4.1 Source asset

`docs/assets/images/favicon.png` — 274×320 portrait.

### 4.2 Generated assets

| File | Size | Purpose |
|------|------|---------|
| `docs/assets/images/favicon.png` | 32×32 | Browser tab favicon (resampled from source) |
| `docs/assets/images/favicon-16.png` | 16×16 | Older browsers, Windows pinned tabs |
| `docs/assets/images/favicon-32.png` | 32×32 | Standard modern favicon |
| `docs/assets/images/favicon-180.png` | 180×180 | Apple touch icon (iOS home screen) |
| `docs/assets/images/favicon.ico` | multi-size (16+32) | IE/legacy support |

### 4.3 mkdocs.yml changes

```yaml
theme:
  favicon: assets/images/favicon.png       # for the <link rel="icon"> tag
  icon:
    logo: material/library

extra:
  manifest: manifests/site.webmanifest     # optional, see §4.4
```

Material automatically serves `favicon-32.png` and `favicon-180.png` if they exist alongside the configured `favicon`. To explicitly include the Apple-touch-icon and `.ico`:

```yaml
extra:
  head: |
    <link rel="icon" type="image/png" sizes="16x16" href="assets/images/favicon-16.png">
    <link rel="icon" type="image/png" sizes="32x32" href="assets/images/favicon-32.png">
    <link rel="apple-touch-icon" sizes="180x180" href="assets/images/favicon-180.png">
```

Wait — Material doesn't render `extra.head` (per Wave 2 correction §8.4). Use `extra_css`/`extra_javascript` only for what they support. Instead, use Material's documented `theme.favicon` and rely on convention for the multi-size variants:

- The configured `theme.favicon` is the primary `<link rel="icon">` in the `<head>`.
- Browsers automatically request `favicon.ico` from the site root if no `<link>` is set; this is handled by GitHub Pages serving any matching file.

So the practical wiring is:
- Set `theme.favicon: assets/images/favicon.png` (32×32 generated).
- Place `favicon.ico` at the repo root so GitHub Pages serves it at `/favicon.ico`.
- Place `favicon-180.png` next to `favicon.png` for Apple touch (browsers will request it; convention only).

### 4.4 Build script

A new `scripts/build_favicons.py` script:

```python
"""Generate multi-size favicon assets from docs/assets/images/favicon.png (source)."""
from PIL import Image
from pathlib import Path

SOURCE = Path(__file__).parent.parent / "docs" / "assets" / "images" / "favicon.png"
OUTPUT_DIR = SOURCE.parent

# Generate each size with high-quality resampling
for size, name in [(16, "favicon-16.png"), (32, "favicon-32.png"), (180, "favicon-180.png")]:
    img = Image.open(SOURCE)
    img.thumbnail((size, size), Image.Resampling.LANCZOS)
    img.save(OUTPUT_DIR / name, "PNG", optimize=True)

# Replace the source favicon.png with a 32×32 optimised version
img = Image.open(SOURCE)
img.thumbnail((32, 32), Image.Resampling.LANCZOS)
img.save(SOURCE, "PNG", optimize=True)

# Multi-size .ico (16+32)
ico_sizes = [(16, 16), (32, 32)]
ico_imgs = [Image.open(OUTPUT_DIR / f"favicon-{s[0]}.png") for s in ico_sizes]
ico_imgs[0].save(OUTPUT_DIR / "favicon.ico", format="ICO", sizes=ico_sizes)

print("Favicons generated:", ", ".join(p.name for p in OUTPUT_DIR.glob("favicon*")))
```

### 4.5 Integration with governance script

Append to `scripts/run_governance.sh`:

```bash
echo ""
echo "Generating favicon variants..."
python scripts/build_favicons.py
```

This ensures that whenever the source portrait is updated, all derived sizes are regenerated. The script is idempotent — re-running with the same source produces the same outputs.

### 4.6 Tests

Add to `tests/test_favicons.py`:

- Source file exists.
- All expected outputs exist after running the build script.
- Output files are valid PNG / ICO.
- Output file dimensions match expectations.

## 5. Acceptance Criteria

- `scripts/build_favicons.py` runs without errors.
- All four output files exist with correct sizes.
- `mkdocs.yml` references `favicon.png` (32×32).
- `bash scripts/run_governance.sh` regenerates favicons and passes.
- `pytest tests/` passes (14 existing + new favicon tests).
- Built site HTML contains `<link rel="icon" href="assets/images/favicon.png">`.

## 6. Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Pillow not installed (if running without `[imaging]`) | Script imports Pillow at runtime; clear error if missing |
| Source portrait is replaced and sizes drift | Build script regenerates from current source on every governance run |
| ICO multi-size generation produces a non-standard file | Use Pillow's documented ICO format with explicit sizes list |
| Browser still ignores generated sizes | Material sets `<link rel="icon" href="...">`; size hints are advisory but conventional |

## 7. Rollback Plan

| Change | Rollback |
|--------|----------|
| Generated favicon files | Delete the generated files; restore the original 274×320 `favicon.png` from git |
| `mkdocs.yml` favicon reference | Revert to pointing at `alexandrefranco.png` (or the original blank config) |
| `build_favicons.py` script | Delete the file |
| `run_governance.sh` integration | Remove the `python scripts/build_favicons.py` line |