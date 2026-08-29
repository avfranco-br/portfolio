# Implementation Plan: Automated CI/CD IP Assessment & Content Governance

**Feature Branch**: `feature/ci-ip-governance-automation` | **Spec**: [spec.md](spec.md)

## Architecture Overview

```
                        [validate_governance.py]
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
 [validate_terminology]  [validate_frontmatter]   [validate_ip_governance]
                                                             │
                                                   ┌─────────┴─────────┐
                                                   ▼                   ▼
                                            [Validation Mode]    [--fix-ip Mode]
                                            (Inspects Banners    (Injects Banners
                                             & Footers)           & Footers)
```

## Technical Design

1. **IP Governance Engine (`scripts/validate_governance.py`)**:
   - Add `validate_ip_governance(docs_dir, fix=False)` function.
   - Define taxomomy path mapping:
     - `docs/sop/*.md` or `docs/narratives/cas*.md`: `RESTRICTED / HIGHLY CONFIDENTIAL` (or `RESTRICTED`)
     - `docs/narratives/*.md`: `CONFIDENTIAL - CLIENT CASE STUDY` (or `CONFIDENTIAL`)
     - `docs/tech-blog/posts/*.md`: `PUBLIC - THOUGHT LEADERSHIP` (or `PUBLIC`)
     - `docs/*.md`: `PUBLIC`
   - Define canonical banner text templates:
     - `> [!IMPORTANT]\n> **Classification Level**: \`RESTRICTED / HIGHLY CONFIDENTIAL\` — Alexandre Franco Enterprise Architecture Portfolio.\n`
     - `> [!NOTE]\n> **Classification Level**: \`CONFIDENTIAL - CLIENT CASE STUDY\` — Alexandre Franco Enterprise Architecture Portfolio.\n`
     - `> [!NOTE]\n> **Classification Level**: \`PUBLIC - THOUGHT LEADERSHIP\` — Alexandre Franco Enterprise Architecture Portfolio.\n`
     - `> [!NOTE]\n> **Classification Level**: \`PUBLIC\` — Alexandre Franco Enterprise Architecture Portfolio.\n`
   - Define canonical footer text template:
     - `*© 2026 Alexandre Franco. Ideas-to-Life. All rights reserved.*`
   - Parse Markdown files handling YAML frontmatter cleanly.

2. **CLI Entrypoint & Argparse (`scripts/validate_governance.py`)**:
   - Support `--fix-ip` flag to auto-remediate missing or invalid headers/footers in place.

3. **Pytest Integration (`tests/test_validate_ip.py`)**:
   - Write tests for valid files, missing headers, missing footers, invalid classification values, frontmatter preservation, and `--fix-ip` idempotency.

4. **Runner Script (`scripts/run_governance.sh`)**:
   - Pass any optional CLI arguments through to `python scripts/validate_governance.py "$@"`.

5. **CI Workflow (`.github/workflows/portfolio-governance.yml`)**:
   - Retain existing execution of `python scripts/validate_governance.py`, which now automatically includes IP governance checking.
