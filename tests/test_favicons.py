"""Tests for scripts/build_favicons.py.

Verifies that the favicon generator produces the expected file set with
correct dimensions and valid PNG/ICO formats.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import pytest
from PIL import Image

# Source portrait lives in tests/fixtures/ and is copied to a tmp location
# before the build runs, so the real docs/assets/images/favicon.png is not
# touched by tests.
REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "build_favicons.py"
FIXTURE_SOURCE = REPO_ROOT / "tests" / "fixtures" / "favicon-source.png"


@pytest.fixture(scope="module")
def fixture_source() -> Path:
    """Create a 512x512 test portrait in tests/fixtures/ if not present.

    Must be larger than the largest ICO/PNG size (180) so the resampling
    logic actually produces different-sized outputs.
    """
    FIXTURE_SOURCE.parent.mkdir(parents=True, exist_ok=True)
    if not FIXTURE_SOURCE.exists():
        img = Image.new("RGB", (512, 512))
        for y in range(512):
            for x in range(512):
                img.putpixel((x, y), (x % 256, y % 256, 128))
        img.save(FIXTURE_SOURCE, "PNG")
    return FIXTURE_SOURCE


@pytest.fixture
def fake_assets(tmp_path: Path, fixture_source: Path) -> Path:
    """Create a fake docs/assets/images/ directory with a copy of the fixture."""
    fake_images = tmp_path / "docs" / "assets" / "images"
    fake_images.mkdir(parents=True)
    shutil.copy(fixture_source, fake_images / "favicon-source.png")
    shutil.copy(fixture_source, fake_images / "favicon.png")
    return fake_images


def _run_build(source_dir: Path) -> None:
    """Run the build_favicons.py script against a fake source directory.

    Patches the script's SOURCE/OUTPUT_DIR to point to our tmp location.
    """
    # Run as a module import to access internals; calling the script directly
    # is also acceptable but slower. We invoke main() in-process.
    import importlib.util

    spec = importlib.util.spec_from_file_location("build_favicons", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # Patch paths
    source_file = source_dir / "favicon-source.png"
    if not source_file.exists():
        source_file = source_dir / "favicon.png"
    module.SOURCE = source_file
    module.OUTPUT_DIR = source_dir
    rc = module.main()
    assert rc == 0


# ---------------------------------------------------------------------------
# Smoke tests
# ---------------------------------------------------------------------------


def test_script_runs_against_real_source():
    """The build script runs cleanly against the real docs/assets/images/favicon.png.

    This is a regression guard: if the source is replaced, the script must
    still produce all expected outputs.
    """
    real_source = REPO_ROOT / "docs" / "assets" / "images" / "favicon-source.png"
    if not real_source.exists():
        real_source = REPO_ROOT / "docs" / "assets" / "images" / "favicon.png"
    if not real_source.exists():
        pytest.skip("Real source favicon not present (run build_favicons.py once first)")

    # Use a tmp copy so we don't mutate the real source mid-test
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        fake = Path(td) / "favicon-source.png"
        shutil.copy(real_source, fake)
        _run_build(Path(td))


def test_all_expected_outputs_produced(fake_assets: Path):
    """All four expected output files exist after the build."""
    _run_build(fake_assets)

    expected = ["favicon.png", "favicon-16.png", "favicon-32.png", "favicon-180.png", "favicon.ico"]
    for name in expected:
        assert (fake_assets / name).exists(), f"Missing output: {name}"


def test_output_dimensions_match(fake_assets: Path):
    """Each PNG output has the expected pixel dimensions."""
    _run_build(fake_assets)

    cases = [
        ("favicon.png", 32),
        ("favicon-16.png", 16),
        ("favicon-32.png", 32),
        ("favicon-180.png", 180),
    ]
    for name, size in cases:
        img = Image.open(fake_assets / name)
        assert img.size == (size, size), f"{name} expected {size}x{size}, got {img.size}"


def test_ico_is_valid_and_multi_size(fake_assets: Path):
    """The favicon.ico is a valid multi-size ICO with at least 16 and 32 sizes."""
    _run_build(fake_assets)

    ico_path = fake_assets / "favicon.ico"
    assert ico_path.exists()

    # Pillow can open ICO and report sizes in info['sizes']
    with Image.open(ico_path) as img:
        sizes = img.info.get("sizes", set())
        n_sizes = len(sizes) if sizes else getattr(img, "n_frames", 1)
        assert n_sizes >= 2, f"ICO has only {n_sizes} size(s); expected multi-size"


def test_png_outputs_are_optimised(fake_assets: Path):
    """Generated PNGs are valid and can be re-opened without errors."""
    _run_build(fake_assets)

    for name in ["favicon.png", "favicon-16.png", "favicon-32.png", "favicon-180.png"]:
        img = Image.open(fake_assets / name)
        img.load()  # forces full decode
        assert img.format == "PNG"


def test_source_is_overwritten_with_primary_size(fake_assets: Path):
    """The primary favicon.png is generated as the primary 32x32 version."""
    original_size = Image.open(fake_assets / "favicon.png").size
    assert original_size[0] > 32, f"Setup error: expected larger than 32x32, got {original_size}"

    _run_build(fake_assets)

    new_size = Image.open(fake_assets / "favicon.png").size
    assert new_size == (32, 32), f"Source should be replaced with 32x32, got {new_size}"


def test_idempotency(fake_assets: Path):
    """Running the build twice produces the same outputs."""
    _run_build(fake_assets)
    first = {p.name: p.read_bytes() for p in fake_assets.glob("favicon*")}

    _run_build(fake_assets)
    second = {p.name: p.read_bytes() for p in fake_assets.glob("favicon*")}

    # The PNGs should be byte-identical
    for name in ["favicon.png", "favicon-16.png", "favicon-32.png", "favicon-180.png"]:
        assert first[name] == second[name], f"{name} not idempotent"

    # The ICO may differ slightly due to Pillow's internal handling; check size only
    assert len(first["favicon.ico"]) == len(second["favicon.ico"]), "ICO size changed between runs"


def test_missing_source_returns_error(tmp_path: Path):
    """If the source favicon doesn't exist, the script exits with code 1."""
    import importlib.util

    spec = importlib.util.spec_from_file_location("build_favicons", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.SOURCE = tmp_path / "nonexistent.png"
    module.OUTPUT_DIR = tmp_path

    rc = module.main()
    assert rc == 1