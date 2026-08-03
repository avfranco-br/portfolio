"""Shared pytest fixtures for the validator test suite.

Each fixture builds a self-contained filesystem under tmp_path so tests
are hermetic and do not depend on the real docs/ tree.

The repository-root conftest.py adds scripts/ to sys.path so we can
`from validate_governance import ...` here.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml


@pytest.fixture
def policy_clean(tmp_path: Path) -> Path:
    """Minimal policy with only canonical terms, no rejected variants."""
    policy = {
        "canonical_terms": {
            "AI native": {"reject": ["AI-native", "AI powered"]},
            "coding agent": {"reject": ["coding-agent"]},
        }
    }
    p = tmp_path / "policy.yaml"
    p.write_text(yaml.safe_dump(policy))
    return p


@pytest.fixture
def docs_tree(tmp_path: Path) -> Path:
    """Return a writable docs/ directory inside tmp_path."""
    docs = tmp_path / "docs"
    docs.mkdir()
    return docs


def write_md(path: Path, content: str) -> Path:
    """Write a Markdown file, creating parent directories as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def findings_by_file(findings: list[dict]) -> dict[str, list[dict]]:
    """Group findings by relative file path for easier assertions."""
    out: dict[str, list[dict]] = {}
    for f in findings:
        out.setdefault(f["file"], []).append(f)
    return out


@pytest.fixture
def find_by_file():
    """Return the helper as a fixture so tests can call it directly."""
    return findings_by_file


@pytest.fixture
def write():
    """Return the write_md helper as a fixture."""
    return write_md