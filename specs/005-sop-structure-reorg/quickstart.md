# Quickstart Validation Guide: Architecture SOP Reorganisation

This guide describes how to validate the three-tier Architecture SOP reorganisation locally before submitting or deploying.

## 1. Prerequisites

Ensure Python dependencies are installed:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## 2. Test Execution & Verification

### Step A: Verify Terminology and Governance Checks
Verify that no forbidden synonyms, hyphenation errors, or terminology drift have been introduced:

```bash
python scripts/validate_governance.py
```
*Expected*: Exit 0 with no terminology violations.

### Step B: Run the Validator Test Suite
Ensure the governance test suite continues to pass:

```bash
pytest tests/
```
*Expected*: All tests pass.

### Step C: Strict Build Validation
Run strict MkDocs compilation to detect broken links, missing assets, or navigation discrepancies:

```bash
mkdocs build --strict
```
*Expected*: Successful build with 0 warnings and 0 errors, output written to `site/`.

### Step D: Local Preview & Visual Inspection
Start the local development server:

```bash
mkdocs serve
```
Open [http://127.0.0.1:8000/sop/](http://127.0.0.1:8000/sop/) in your browser:
- [ ] Verify that **How I work** → **Architecture SOP** expands into:
  - **Overview**
  - **Core EA Practice** (5 stages)
  - **Engagement Methods** (4 methods, including Architecture Health Check)
  - **Illustrative Evidence** (2 reports)
  - **AI Augmented Architecture** (2 AI pages)
- [ ] Navigate to the new [Architecture Health Check](http://127.0.0.1:8000/sop/methods/architecture-health-check/) page and verify formatting.
- [ ] Verify that the overview page ([`sop/index.md`](http://127.0.0.1:8000/sop/)) diagram and practice relationship section accurately reference the 3 tiers.
