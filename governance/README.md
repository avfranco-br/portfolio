# Portfolio Governance

This directory contains the lightweight operational governance layer for the portfolio repository.

## Governance Philosophy

We treat documentation as an operational asset. Governance is implemented as a **continuous validation loop** that enables quality without introducing friction. This approach aligns with the **Continuous Architecture System (CAS)** principles:

- **Preventive:** Catch structural drift before it reaches production.
- **Enabled:** Use automation to guide authors toward consistency.
- **Lightweight:** Prefer simple, deterministic scripts over heavy frameworks.

## Terminology Validation

Narrative consistency is maintained through a canonical terminology policy.

- **Policy:** Defined in `terminology.yaml`.
- **Enforcement:** The `scripts/validate_governance.py` tool scans for rejected variants (e.g., preferring "AI native" over "AI-native").
- **Nature:** These checks are informational. They provide guidance rather than blocking builds, preserving editorial flow while maintaining standards.

## Continuous Integrity (CI)

The `.github/workflows/portfolio-governance.yml` orchestrates our operational standards on every change:

1.  **Structural Integrity:** Uses `mkdocs build --strict` to ensure no broken links or navigation errors exist.
2.  **Governance Reporting:** Executes the terminology validator to report inconsistencies in the CI logs.

## Directory Structure

- `terminology.yaml`: The single source of truth for canonical terms.
- `scripts/`: Operational scripts for validation and governance reporting.
