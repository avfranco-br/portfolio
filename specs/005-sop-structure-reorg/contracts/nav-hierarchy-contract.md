# Navigation Contract: Architecture SOP

## Contract Specification: `mkdocs.yml` Navigation Schema

The `nav` entry for `How I work` MUST conform to the following hierarchy:

```yaml
nav:
  # ... previous nav entries ...
  - How I work:
      - Methodology: how-i-work.md
      - Architecture SOP:
          - Overview: sop/index.md
          - Core EA Practice:
              - 01. Discover & Align: sop/01-discover-align.md
              - 02. Target Architecture & Strategy: sop/02-target-architecture.md
              - 03. Governance & Decision Enablement: sop/03-governance-framework.md
              - 04. Delivery Enablement & Execution Steering: sop/04-delivery-enablement.md
              - 05. Value Realisation & Organisational Handover: sop/05-value-realisation-handover.md
          - Engagement Methods:
              - Architecture Decision Review: sop/methods/architecture-decision-review.md
              - Architecture Assessment & Roadmap: sop/methods/architecture-assessment-and-roadmap.md
              - Architecture Health Check: sop/methods/architecture-health-check.md
              - Architecture Automation Opportunity Assessment: sop/methods/architecture-automation-opportunity-assessment.md
          - Illustrative Evidence:
              - Decision Review report: sop/methods/architecture-decision-review-report.v2.md
              - Assessment & Transformation Roadmap report: sop/methods/architecture-assessment-roadmap-report.v2.md
          - AI Augmented Architecture:
              - AI Augmented Workflows: sop/ai-augmented-architecture.md
              - Agent Co-Pilot Prompt: sop/agent-architect-prompt.md
  # ... following nav entries ...
```

## Contract Validation Rules

1. Every item listed under `Architecture SOP` MUST point to a valid Markdown file that exists on disk under `docs/`.
2. All 5 Core EA Practice stages MUST be present in order (01 to 05).
3. All 4 Engagement Methods MUST be present.
4. Both Illustrative Evidence reports MUST be present.
5. All AI Augmented Architecture pages MUST be present.
6. `mkdocs build --strict` MUST exit with status 0 and no unresolved navigation warnings.
