---
name: cas-refactor-module
description: MANDATORY skill for refactoring an existing module from a specific target path using repository architecture rules and pattern catalogue guidance while preserving observable behaviour. Use when asked to refactor, restructure, decouple, simplify, decompose, or remove hardcoding/coupling in existing code while preserving observable behaviour.
---

# Skill: cas-refactor-module

## Intent
Refactor existing code to improve architectural alignment, enforce patterns, and remove anti-patterns while preserving current system behaviour.

---

## Inputs
- Read `INPUT.schema.yaml` before proceeding.
- Use `input.target_path` as the primary inspection target.
- Use `input.refactor_request` to determine the requested change.
- Treat `input.constraints` as additional hard constraints unless they conflict with repository architecture rules.

---

## Decision Precedence
Apply rules in this order:
1. Preserve observable behaviour.
2. Follow `.cas/rules/architecture-rules.md`.
3. Respect the requested constraints when they do not conflict with 1 or 2.
4. Reuse existing patterns from `.cas/patterns/patterns-catalogue.yaml`.
5. Prefer the smallest structural change that satisfies the request.

If the request conflicts with behaviour preservation or architecture rules, reject it or propose a constrained alternative rather than forcing a refactor.

---

## Constraints (Prevent)
- MUST NOT change observable behaviour
- MUST preserve existing contracts and interfaces unless explicitly justified
- MUST apply rules from `.cas/rules/architecture-rules.md`
- MUST use patterns from `.cas/patterns/patterns-catalogue.yaml`
- MAY introduce new supporting modules/components if required for structural improvement
- MUST NOT introduce external integrations
- MUST include a `decision` block in every output
- MUST set decision.status to one of: accepted | rejected | proposed
- MUST produce exactly one output block conforming to OUTPUT.schema.yaml
- MUST use pattern IDs exactly as defined in `.cas/patterns/patterns-catalogue.yaml`
- OUTPUT.schema.yaml is the single source of truth
- MUST NOT include meta-commentary outside the YAML output
- MUST NOT enter plan or execution mode before producing output
- MUST NOT proceed with the implementation until approved by the user
---

## Instructions

### 1. Understand Current State
- Read the input and inspect the target path.
- Analyze existing module structure.
- Identify responsibilities and dependencies.

### 2. Identify Refactoring Opportunities
- Detect anti-patterns (e.g., hardcoding, coupling, mixed concerns)
- Identify applicable patterns from patterns-catalogue.yaml
- Prefer existing patterns over inventing new ones

### 3. Validate Against Rules
- Ensure proposed refactor does not violate architecture rules
- Ensure behaviour remains unchanged
- If no safe refactor path exists, mark the decision as `rejected`

### 4. Design Refactoring
- Define new structure (modules, responsibilities)
- Apply selected patterns
- Justify structural changes and why they are the minimum viable change
- If a new pattern is required, mark the decision as `proposed`

### 5. Produce Output
- MUST produce a single valid YAML block
- MUST include the `decision` block
- Do not include any text before or after the YAML block

### 6. Populate the Output Fields
- `feature`: name the refactor and identify the affected module
- `decision`: state the outcome, reason, and rejected alternative
- `code_changes`: list only files or modules that change or would change
- `architecture_decision`: capture the architectural conclusion, not a file summary
- `architectural_impact`: list affected components, pattern IDs, and why they apply
- `risks`: record remaining behavioural or structural risks
- `validation_notes`: describe how behavioural equivalence was or would be checked

---

## Output Contract
See OUTPUT.schema.yaml

---

## Anti-Patterns (must avoid)
- Changing behaviour unintentionally
- Introducing new features during refactor
- Tight coupling between modules
- Hidden dependencies
- Hardcoded configuration or prompts

---

## Pattern Usage
- Identify and reuse existing patterns
- If new pattern is required → decision.status must be "proposed"

---

## Validation Notes
- Behaviour must remain identical before and after refactor
- Refactor must improve structure and maintainability
- Prefer the smallest verifiable change set that achieves the goal
