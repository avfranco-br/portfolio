# Quickstart Validation Guide: Portfolio Look & Feel Restructure

**Feature**: Portfolio Look & Feel Restructure  
**Branch**: `001-portfolio-restructure`

---

## 1. Prerequisites

- Python 3.12+ installed with virtual environment active (`.venv`)
- Dependencies installed (`pip install -r requirements.txt` & `pip install -r requirements-dev.txt`)

---

## 2. Validation Steps

### Step 1: Run Local Preview Server
```bash
mkdocs serve
```
- Open `http://127.0.0.1:8000/` in browser.
- Verify the homepage displays as a full-width hero layout (no left sidebar navigation, no right TOC sidebar).
- Verify Selected Work entries appear as responsive card grids.

### Step 2: Run Full Governance & Build Validation
```bash
bash scripts/run_governance.sh
```
- Confirms `mkdocs build --strict` completes with 0 warnings or broken links.
- Confirms terminology validation passes with 0 forbidden variants.

### Step 3: Run Automated Test Suite
```bash
pytest tests/
```
- Verifies all 22+ unit and governance integration tests pass cleanly.

### Step 4: Word Count Sanity Verification
```bash
python -c '
import glob
for path in glob.glob("docs/narratives/*.md"):
    with open(path) as f:
        print(f"{path}: {len(f.read().split())} words")
'
```
- Confirms post-restructure word count on every narrative page is equal to or greater than pre-restructure count.
