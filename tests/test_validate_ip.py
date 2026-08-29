"""Tests for IP classification & copyright validation in scripts/validate_governance.py.

All unit tests use tmp_path fixtures to isolate test environments.
The final integration test runs against the real repository docs/ directory.
"""

from __future__ import annotations
from pathlib import Path
from validate_governance import validate_ip_governance, get_canonical_banner, get_canonical_footer


def test_empty_docs_tree_returns_no_ip_findings(tmp_path: Path):
    """An empty docs directory produces zero IP findings."""
    docs_tree = tmp_path / "docs"
    docs_tree.mkdir()
    findings = validate_ip_governance(str(docs_tree))
    assert findings == []


def test_clean_page_with_banner_and_footer_passes(tmp_path: Path):
    """A page containing both a valid classification banner and copyright footer produces zero findings."""
    docs_tree = tmp_path / "docs"
    docs_tree.mkdir()
    content = (
        "# Title\n\n"
        "> [!NOTE]\n"
        "> **Classification Level**: `PUBLIC` — Alexandre Franco Enterprise Architecture Portfolio.\n\n"
        "Some body prose.\n\n"
        "---\n\n"
        "*© 2026 Alexandre Franco. Ideas-to-Life. All rights reserved.*\n"
    )
    (docs_tree / "index.md").write_text(content, encoding="utf-8")

    findings = validate_ip_governance(str(docs_tree))
    assert findings == []


def test_detects_missing_banner(tmp_path: Path):
    """A page missing a classification banner triggers an IP finding."""
    docs_tree = tmp_path / "docs"
    docs_tree.mkdir()
    content = (
        "# Title\n\n"
        "Some body prose.\n\n"
        "*© 2026 Alexandre Franco. Ideas-to-Life. All rights reserved.*\n"
    )
    (docs_tree / "index.md").write_text(content, encoding="utf-8")

    findings = validate_ip_governance(str(docs_tree))
    assert len(findings) == 1
    assert "Missing required IP classification banner" in findings[0]["issue"]


def test_detects_missing_footer(tmp_path: Path):
    """A page missing a copyright footer triggers an IP finding."""
    docs_tree = tmp_path / "docs"
    docs_tree.mkdir()
    content = (
        "> [!NOTE]\n"
        "> **Classification Level**: `PUBLIC` — Portfolio.\n\n"
        "# Title\n\n"
        "Some body prose.\n"
    )
    (docs_tree / "index.md").write_text(content, encoding="utf-8")

    findings = validate_ip_governance(str(docs_tree))
    assert len(findings) == 1
    assert "Missing required IP copyright footer" in findings[0]["issue"]


def test_auto_fix_injects_banner_and_footer(tmp_path: Path):
    """Running validate_ip_governance with fix=True injects missing banner and footer."""
    docs_tree = tmp_path / "docs"
    docs_tree.mkdir()
    sop_dir = docs_tree / "sop"
    sop_dir.mkdir()
    sop_file = sop_dir / "index.md"
    sop_file.write_text("# Architecture SOP\n\nStandard procedure body.\n", encoding="utf-8")

    # Initial validation reports findings
    findings = validate_ip_governance(str(docs_tree), fix=False)
    assert len(findings) == 2

    # Auto-fix mode repairs the file
    fix_findings = validate_ip_governance(str(docs_tree), fix=True)
    assert fix_findings == []

    updated_text = sop_file.read_text(encoding="utf-8")
    assert "RESTRICTED / HIGHLY CONFIDENTIAL" in updated_text
    assert "© 2026 Alexandre Franco" in updated_text


def test_auto_fix_preserves_yaml_frontmatter(tmp_path: Path):
    """Auto-fix mode inserts the header banner AFTER YAML frontmatter."""
    docs_tree = tmp_path / "docs"
    docs_tree.mkdir()
    page_file = docs_tree / "page.md"
    page_file.write_text(
        "---\ntitle: Sample Page\nstatus: approved\n---\n\n# Page Title\n\nPage content.\n",
        encoding="utf-8",
    )

    validate_ip_governance(str(docs_tree), fix=True)
    updated_text = page_file.read_text(encoding="utf-8")

    assert updated_text.startswith("---\ntitle: Sample Page\nstatus: approved\n---")
    assert "> [!NOTE]" in updated_text
    assert "© 2026 Alexandre Franco" in updated_text


def test_auto_fix_is_idempotent(tmp_path: Path):
    """Running fix=True multiple times produces no additional changes."""
    docs_tree = tmp_path / "docs"
    docs_tree.mkdir()
    page_file = docs_tree / "page.md"
    page_file.write_text("# Page Title\n\nPage content.\n", encoding="utf-8")

    validate_ip_governance(str(docs_tree), fix=True)
    first_pass_content = page_file.read_text(encoding="utf-8")

    validate_ip_governance(str(docs_tree), fix=True)
    second_pass_content = page_file.read_text(encoding="utf-8")

    assert first_pass_content == second_pass_content


def test_real_repo_docs_pass_ip_validation():
    """All existing documentation pages in the real repository pass IP validation."""
    repo_root = Path(__file__).resolve().parent.parent
    docs_dir = repo_root / "docs"
    assert docs_dir.exists(), f"Docs directory not found at {docs_dir}"

    findings = validate_ip_governance(str(docs_dir), fix=False)
    assert findings == [], f"Real repo has IP governance issues: {findings}"
