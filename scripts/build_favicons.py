"""Generate multi-size favicon assets from docs/assets/images/favicon.png (source).

Run via `python scripts/build_favicons.py` or as part of `scripts/run_governance.sh`.

Outputs:
    docs/assets/images/favicon.png      (resampled to 32x32, optimised)
    docs/assets/images/favicon-16.png   (16x16)
    docs/assets/images/favicon-32.png   (32x32)
    docs/assets/images/favicon-180.png  (180x180, Apple touch icon)
    docs/assets/images/favicon.ico      (multi-size: 16+32, for IE/legacy)

Idempotent: re-running with the same source produces the same outputs.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print(
        "Error: Pillow is not installed. "
        "Install it via `pip install Pillow` (already included in mkdocs-material[imaging]).",
        file=sys.stderr,
    )
    sys.exit(1)

SOURCE_NAME = "favicon-source.png"
DEFAULT_SOURCE_NAME = "favicon.png"

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
SOURCE = REPO_ROOT / "docs" / "assets" / "images" / SOURCE_NAME
if not SOURCE.exists():
    SOURCE = REPO_ROOT / "docs" / "assets" / "images" / DEFAULT_SOURCE_NAME
OUTPUT_DIR = SOURCE.parent

PNG_SIZES = [
    (16, "favicon-16.png"),
    (32, "favicon-32.png"),
    (180, "favicon-180.png"),
]
PRIMARY_SIZE = 32  # The size of the source-of-truth favicon.png replacement


def generate_png_sizes(source: Path, output_dir: Path) -> list[Path]:
    """Generate per-size PNG variants from the source image."""
    outputs: list[Path] = []
    for size, name in PNG_SIZES:
        img = Image.open(source)
        img.thumbnail((size, size), Image.Resampling.LANCZOS)
        if img.size != (size, size):
            square = Image.new("RGBA", (size, size), (0, 0, 0, 0))
            offset = ((size - img.size[0]) // 2, (size - img.size[1]) // 2)
            square.paste(img, offset)
            img = square
        if img.mode != "RGBA":
            img = img.convert("RGB")
        out = output_dir / name
        img.save(out, "PNG", optimize=True)
        outputs.append(out)
    return outputs


def replace_primary_favicon(source: Path, primary_size: int, output_dir: Path | None = None) -> Path:
    """Generate the primary 32x32 favicon.png asset."""
    target_dir = output_dir if output_dir is not None else source.parent
    out = target_dir / "favicon.png"
    img = Image.open(source)
    img.thumbnail((primary_size, primary_size), Image.Resampling.LANCZOS)
    if img.size != (primary_size, primary_size):
        square = Image.new("RGBA", (primary_size, primary_size), (0, 0, 0, 0))
        offset = ((primary_size - img.size[0]) // 2, (primary_size - img.size[1]) // 2)
        square.paste(img, offset)
        img = square
    if img.mode != "RGBA":
        img = img.convert("RGB")
    img.save(out, "PNG", optimize=True)
    return out


def generate_ico(output_dir: Path, sizes: list[tuple[int, int]], source: Path) -> Path:
    """Generate a multi-size ICO from the source image."""
    img = Image.open(source).convert("RGBA")
    out = output_dir / "favicon.ico"
    img.save(out, format="ICO", sizes=sizes)
    return out


def main() -> int:
    global SOURCE, OUTPUT_DIR
    if not SOURCE.exists():
        fallback = SOURCE.parent / SOURCE_NAME
        if fallback.exists():
            SOURCE = fallback
        else:
            fallback_default = SOURCE.parent / DEFAULT_SOURCE_NAME
            if fallback_default.exists():
                SOURCE = fallback_default
            else:
                print(f"Error: source favicon not found at {SOURCE}", file=sys.stderr)
                return 1

    print(f"Source: {SOURCE} ({Image.open(SOURCE).size})")
    print(f"Output dir: {OUTPUT_DIR}")

    png_outputs = generate_png_sizes(SOURCE, OUTPUT_DIR)
    print(f"Generated PNG variants: {', '.join(p.name for p in png_outputs)}")

    primary = replace_primary_favicon(SOURCE, PRIMARY_SIZE, OUTPUT_DIR)
    print(f"Replaced primary favicon: {primary.name} ({Image.open(primary).size})")

    ico = generate_ico(OUTPUT_DIR, [(16, 16), (32, 32)], SOURCE)
    print(f"Generated ICO: {ico.name}")

    print("Favicon generation complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
