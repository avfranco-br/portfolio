"""Tests for scripts/validate_governance.py.

The validator is imported as a module. Tests rely on the conftest fixture
that prepends scripts/ to sys.path so the import resolves.

Each test uses tmp_path fixtures exclusively — no test touches the real
docs/ directory of the repository.
"""

from __future__ import annotations

from pathlib import Path

# Imported after conftest has patched sys.path.
from validate_governance import validate_terminology


# ---------------------------------------------------------------------------
# 1. Empty docs tree → no findings
# ---------------------------------------------------------------------------


def test_empty_docs_tree_returns_no_findings(policy_clean: Path, docs_tree: Path):
    """With an empty docs/ directory, the validator reports zero findings."""
    findings = validate_terminology(str(policy_clean), str(docs_tree))
    assert findings == []


# ---------------------------------------------------------------------------
# 2. Clean content → no findings
# ---------------------------------------------------------------------------


def test_clean_content_returns_no_findings(
    policy_clean: Path, docs_tree: Path, write
):
    """Markdown using only canonical terms produces zero findings."""
    write(
        docs_tree / "index.md",
        "# Welcome\n\nThis platform is AI native and supports coding agent workflows.\n",
    )
    write(
        docs_tree / "about.md",
        "We use a coding agent for routine refactors and embrace AI native delivery.\n",
    )

    findings = validate_terminology(str(policy_clean), str(docs_tree))
    assert findings == []


# ---------------------------------------------------------------------------
# 3. Detects "AI-native" (hyphen variant)
# ---------------------------------------------------------------------------


def test_detects_ai_native_hyphen_variant(policy_clean: Path, docs_tree: Path, write):
    """The hyphenated variant AI-native is detected and AI native reported as preferred."""
    write(docs_tree / "index.md", "We build AI-native systems.\n")

    findings = validate_terminology(str(policy_clean), str(docs_tree))
    assert len(findings) == 1
    finding = findings[0]
    assert finding["found"].lower() == "ai-native"
    assert finding["preferred"] == "AI native"
    assert finding["file"] == "index.md"


# ---------------------------------------------------------------------------
# 4. Case-insensitive detection
# ---------------------------------------------------------------------------


def test_detection_is_case_insensitive(policy_clean: Path, docs_tree: Path, write):
    """All casing variants of a rejected term produce findings."""
    write(
        docs_tree / "page.md",
        "Line 1: AI-NATIVE\nLine 2: ai-native\nLine 3: Ai-Native\n",
    )

    findings = validate_terminology(str(policy_clean), str(docs_tree))
    # Three rejected variants on three lines.
    assert len(findings) == 3
    # Sorted by line because they appear in source order.
    lines = sorted(f["line"] for f in findings)
    assert lines == [1, 2, 3]


# ---------------------------------------------------------------------------
# 5. Word boundary precision
# ---------------------------------------------------------------------------


def test_word_boundary_precision(policy_clean: Path, docs_tree: Path, write):
    """`AI natively` is a different word and must not match `AI-native`."""
    write(docs_tree / "page.md", "We work AI natively and embrace AI-native delivery.\n")

    findings = validate_terminology(str(policy_clean), str(docs_tree))
    # Only the second occurrence (AI-native) should match.
    assert len(findings) == 1
    assert findings[0]["found"].lower() == "ai-native"


def test_hyphenated_term_boundary_for_coding_agent(
    policy_clean: Path, docs_tree: Path, write
):
    """`coding-agent` matches but `coding-agents` (plural) does NOT match the singular reject.

    The validator uses \\b boundaries, so 'coding-agent' as a hyphenated compound
    is detected, while 'coding-agents' is technically a different surface form
    that the policy does not currently cover. We assert this is the documented
    behaviour so any change to boundaries is intentional.
    """
    write(
        docs_tree / "page.md",
        "Use a coding-agent for this task. We use many coding-agents.\n",
    )

    findings = validate_terminology(str(policy_clean), str(docs_tree))
    # Only the singular 'coding-agent' should be flagged.
    assert len(findings) == 1
    assert findings[0]["found"].lower() == "coding-agent"


# ---------------------------------------------------------------------------
# 6. Line number accuracy
# ---------------------------------------------------------------------------


def test_line_number_accuracy(policy_clean: Path, docs_tree: Path, write):
    """The reported line number matches the line where the rejected term appears."""
    content = "\n".join(
        [
            "# Heading",                       # line 1
            "",                                 # line 2
            "Paragraph one is fine.",          # line 3
            "",                                 # line 4
            "We adopt AI-native delivery.",    # line 5 — finding expected here
            "",                                 # line 6
            "More prose below.",               # line 7
        ]
    )
    write(docs_tree / "page.md", content + "\n")

    findings = validate_terminology(str(policy_clean), str(docs_tree))
    assert len(findings) == 1
    assert findings[0]["line"] == 5


# ---------------------------------------------------------------------------
# 7. Recursion into nested dirs
# ---------------------------------------------------------------------------


def test_finds_terms_in_nested_directories(
    policy_clean: Path, docs_tree: Path, write
):
    """Findings inside nested subdirectories are reported with a path relative to docs_dir."""
    write(
        docs_tree / "narratives" / "cas.md",
        "We avoid AI-native framing and prefer AI native instead.\n",
    )

    findings = validate_terminology(str(policy_clean), str(docs_tree))
    assert len(findings) == 1
    # Path must be relative to docs_dir, not absolute.
    assert findings[0]["file"] == "narratives/cas.md"
    assert "/" in findings[0]["file"]


# ---------------------------------------------------------------------------
# 8. Code-block isolation
# ---------------------------------------------------------------------------


def test_rejected_term_inside_fenced_code_block_is_ignored(
    policy_clean: Path, docs_tree: Path, write
):
    """A rejected term inside a ```...``` code block must NOT trigger a finding."""
    content = (
        "# Heading\n"
        "\n"
        "Normal prose is fine.\n"
        "\n"
        "```\n"
        "This AI-native string is in a code block.\n"
        "```\n"
        "\n"
        "Back to prose.\n"
    )
    write(docs_tree / "page.md", content)

    findings = validate_terminology(str(policy_clean), str(docs_tree))
    assert findings == []


def test_rejected_term_inside_tilde_fenced_code_block_is_ignored(
    policy_clean: Path, docs_tree: Path, write
):
    """Same isolation applies to ~~~ fences."""
    content = (
        "~~~markdown\n"
        "AI-native here is fine.\n"
        "~~~\n"
    )
    write(docs_tree / "page.md", content)

    findings = validate_terminology(str(policy_clean), str(docs_tree))
    assert findings == []


# ---------------------------------------------------------------------------
# 9. Inline-code isolation
# ---------------------------------------------------------------------------


def test_rejected_term_inside_inline_code_is_ignored(
    policy_clean: Path, docs_tree: Path, write
):
    """A rejected term inside `backticks` (inline code) must NOT trigger a finding."""
    write(
        docs_tree / "page.md",
        "Use the `AI-native` placeholder in this example.\n",
    )

    findings = validate_terminology(str(policy_clean), str(docs_tree))
    assert findings == []


# ---------------------------------------------------------------------------
# 10. Markdown link-target isolation
# ---------------------------------------------------------------------------


def test_rejected_term_inside_markdown_link_target_is_ignored(
    policy_clean: Path, docs_tree: Path, write
):
    """A rejected term inside the URL part of a markdown link is NOT flagged.

    Only the link target (URL) is stripped before scanning — link text is
    visible prose and must be detected (see next test).

    Example: [safe overview](https://example.com/AI-native) → the URL
    target is stripped, link text "safe overview" is canonical, so no finding.
    """
    write(
        docs_tree / "page.md",
        "Read the [safe overview](https://example.com/AI-native) for context.\n",
    )

    findings = validate_terminology(str(policy_clean), str(docs_tree))
    assert findings == []


def test_rejected_term_in_link_text_is_still_detected(
    policy_clean: Path, docs_tree: Path, write
):
    """A rejected term inside the visible link text IS flagged.

    Only the link target is stripped — the link text remains visible prose.
    """
    write(
        docs_tree / "page.md",
        "Please read our [AI-native overview](https://example.com/safe-url).\n",
    )

    findings = validate_terminology(str(policy_clean), str(docs_tree))
    assert len(findings) == 1
    assert findings[0]["found"].lower() == "ai-native"


# ---------------------------------------------------------------------------
# Integration test against the real repository
# ---------------------------------------------------------------------------


def test_real_repo_passes_validation():
    """The actual repo (with its policy and docs/) produces zero findings.

    This is a regression guard: if anyone introduces a hyphenated variant
    in prose (outside code blocks and links), this test will fail.
    """
    repo_root = Path(__file__).resolve().parent.parent
    policy = repo_root / "governance" / "terminology.yaml"
    docs = repo_root / "docs"

    assert policy.exists(), f"Policy not found at {policy}"
    assert docs.exists(), f"Docs dir not found at {docs}"

    findings = validate_terminology(str(policy), str(docs))
    assert findings == [], (
        f"Real repo has terminology drift: {findings}. "
        f"Run `python scripts/validate_governance.py` for details."
    )