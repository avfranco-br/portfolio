---
title: "Master Interview Playbook Generator: Building an Evidence-Bounded Career Projection System"
description: "How decoupling canonical portfolio evidence from target runtime context and enforcing automated claim-linting builds evidence-bounded AI career projection workflows."
pubDate: 2026-08-07
tags:
  - "ai-architecture"
  - "multi-agent-systems"
  - "career-projection"
  - "claim-linting"
author: "Alexandre Franco"
slug: "master-interview-playbook-generator-evidence-bounded-career-projection"
target: tech-blog
status: approved
content_type: technical-problem-solution
claim_calibration:
  status: approved
  claims_reviewed: 6
  direct_claims: 3
  derived_claims: 0
  observed_outcomes: 2
  unsupported_claims_removed_or_reframed: 1
---

# Master Interview Playbook Generator: Building an Evidence-Bounded Career Projection System

## The Practitioner Challenge: Career Context Without Positioning Inflation

I wanted to build a system that could take my existing professional evidence and turn it into a role-specific interview playbook without quietly upgrading my experience along the way.

Generative AI workflows are increasingly used to draft role-tailored artifacts, from technical proposals to career positioning playbooks. However, unconstrained language models frequently suffer from positioning inflation. When prompting an LLM to map broad portfolio experience against specific role requirements, models naturally default to overly optimistic claims, blurring the boundary between verified engineering experience and aspirational intent.

For enterprise architects and AI platform engineers building domain-specific LLM applications, this challenge extends beyond resume tailoring. It mirrors a broader structural problem in generative systems: how to adapt authoritative knowledge to diverse target contexts without compromising factual grounding.

Preparing for executive technical interviews—such as AI CoE Lead or Head of AI & Automation roles—requires deep contextual tailoring. Yet, using ad-hoc prompts for each role leads to repeated context assembly overhead and inconsistent claim boundaries. To address this, I built the **Master Interview Playbook Generator**, an automated multi-agent workflow designed to project canonical portfolio evidence into target-specific interview playbooks while enforcing strict, code-governed claim calibration.

<!-- more -->

## Architectural Approach: The 4-Layer Decoupled Pipeline

To isolate target-scoped context from polluting source evidence, the generator relies on structural decoupling across four distinct architectural layers:

1. **Knowledge Layer (`okf/`)**: The canonical repository storing immutable portfolio evidence, verified project telemetry, and core engineering achievements.
2. **Runtime Layer (`out/<target-slug>/runtime/`)**: A target-isolated execution environment where job descriptions, enterprise intelligence, and role requirements are analyzed.
3. **Coaching Layer (`okf/`)**: Strategic positioning framework and domain guidance templates that govern conversation framing.
4. **Projection Layer (`out/<target-slug>/`)**: The output space where generated interview playbooks reside after passing automated quality gates.

```
+-------------------------------------------------------------------+
|                        KNOWLEDGE LAYER                            |
|    okf/ (Immutable Portfolio Evidence & Verified Artifacts)       |
+---------------------------------+---------------------------------+
                                  |
                                  v
+---------------------------------+---------------------------------+
|                         RUNTIME LAYER                             |
|    out/<target-slug>/runtime/ (Target Context & Intelligence)     |
+---------------------------------+---------------------------------+
                                  |
                                  v
+---------------------------------+---------------------------------+
|                         COACHING LAYER                            |
|    okf/ (Strategic Frameworks & Conversation Guidance)            |
+---------------------------------+---------------------------------+
                                  |
                                  v
+---------------------------------+---------------------------------+
|                        PROJECTION LAYER                           |
|    out/<target-slug>/ (Generated Artifacts & Quality Gates)       |
+-------------------------------------------------------------------+
```

The orchestration flow executes via a 23-step multi-agent sequence defined in `skills/playbook-orchestrator/SKILL.md`. By isolating canonical facts within `okf/`, target-specific prompts can synthesize runtime intelligence without mutating baseline source facts.

## Enforcing Grounding Boundaries: Automated Claim Linting & Fit Ceilings

Prompt instructions alone are insufficient to bound factual claims in generative workflows. To constrain positioning claims deterministically, the system implements automated quality gates in Python before any generated playbook is finalized.

### 1. Classification Tags & Footnote Attribution

The linter enforces explicit evidence tags (`[evidence]`, `[inference]`, `[recommendation]`, `[assumption]`) and mandates source footnote attributions (`[^source-id]`) on all factual assertions. The following test snippet from `tests/test_lint.py` demonstrates how generated concepts are validated:

```python
def lint_okf_concept_content(content: str) -> list[str]:
    """Validates OKF concept content for required claim classification tags 
    and source footnote attributions.
    """
    errors = []
    required_tags = ["[evidence]", "[inference]", "[recommendation]", "[assumption]"]
    
    # Check for at least one valid classification tag
    if not any(tag in content for tag in required_tags):
        errors.append("Missing required classification tag prefix")

    # Mandate footnote attribution for evidence assertions
    if "[evidence]" in content and "[^" not in content:
        errors.append("Evidence claims require explicit source footnote attribution [^source-id]")
        
    return errors
```

### 2. Alignment Ceilings to Mitigate Overpositioning

To bound experience mapping when matching portfolio achievements to role requirements, the system applies fit constraint rules tested in `tests/test_v06_success_criteria.py`. These rules establish an alignment ceiling that caps projected readiness based on direct evidence:

- **Direct Experience** $\rightarrow$ Capped at **Strong Alignment**
- **Adjacent Experience** $\rightarrow$ Capped at **Moderate Alignment**
- **Transferable Skill** $\rightarrow$ Capped at **Transferable Alignment**
- **Absent Evidence** $\rightarrow$ Flagged as **Gap**

```python
def validate_fit_constraint(evidence_level: str, claimed_alignment: str) -> bool:
    """Enforces alignment ceiling rules to mitigate positioning inflation."""
    MAX_ALIGNMENT = {
        "Direct": "Strong",
        "Adjacent": "Moderate",
        "Transferable": "Transferable",
        "Absent": "Gap"
    }
    
    allowed = MAX_ALIGNMENT.get(evidence_level, "Gap")
    # Returns False if claimed alignment exceeds the maximum allowed ceiling
    return is_within_ceiling(claimed_alignment, max_allowed=allowed)
```

If an output attempts to elevate an "Adjacent" architectural capability into a "Strong" direct fit claim, the `archetype-fit-validator` flags an inflation warning and fails the quality gate.

## Key Decisions & Architectural Trade-offs

Building an evidence-bounded projection system involves explicit compromises between flexibility and deterministic governance:

* **Immutable Canonical Storage vs. Target Isolation**
  * *Rationale*: Storing canonical portfolio facts in an immutable repository (`okf/`) isolates source experience from target-scoped runtime adjustments.
  * *Trade-off*: Increases execution context assembly overhead per target slug, but mitigates target bias from polluting canonical portfolio facts.
* **Automated Post-Generation Linting vs. Prompt Instruction Alone**
  * *Rationale*: Prompting LLMs to stay truthful often fails under complex contextual blending. Deterministic post-generation linting enforces explicit footnote links and classification tags.
  * *Trade-off*: Requires dedicated validation agent passes (`projection-validator`, `brand-validator`), adding orchestration complexity and execution latency.

## Results & Lessons Learned: Commercial Reality vs. Technical Pipeline Completion

Executing the Master Interview Playbook Generator across multiple enterprise role scenarios yielded tailored, evidence-grounded artifacts while maintaining strict claim boundaries. However, testing exposed a critical distinction between technical pipeline completion and real-world viability.

During execution testing against an Enterprise Governance Architect role scenario, the generator produced a technically sound playbook matching all required architecture competencies. However, evaluating the role's real commercial context revealed a five-day on-site commitment constraint that rendered the opportunity commercially unviable.

This outcome highlighted a key practitioner lesson: **pipeline execution completion is merely an intermediate milestone**. In domain-specific generative workflows, output validation cannot stop at schema validity or prompt compliance—it must validate output fidelity against real commercial constraints and operational commitments.

Maintaining portfolio evidence in sync with evolving career experience remains an ongoing operational consideration. However, decoupling source data from target projections provides a durable foundation for updating evidence without refactoring target-specific execution pipelines.

## Key Takeaways for AI Engineers

When building domain-specific LLM workflows where accuracy and claim integrity are critical:

1. **Decouple Storage from Context**: Keep core domain knowledge immutable; build target-scoped runtime environments dynamically.
2. **Implement Hard Alignment Ceilings**: Do not rely on prompt phrasing to constrain model optimism—enforce ceiling rules in code.
3. **Validate Beyond Syntax**: Verify that validation gates assess operational and commercial viability alongside technical output schema compliance.
