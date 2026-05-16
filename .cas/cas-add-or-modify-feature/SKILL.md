---
name: cas-add-or-modify-feature
description: MANDATORY skill for any feature request or structural modification. Use when adding features, extending functionality, modifying existing behaviour, or introducing integrations. This skill MUST be invoked before making any code changes to ensure architectural alignment, pattern reuse, and governance compliance.
---

# Skill: cas-add-or-modify-feature

## Intent
Introduce a new feature aligned with existing architecture, ensuring consistency with module boundaries, reuse of established patterns, and prevention of architectural drift.

**When to use this skill:**
- User asks to "add a feature" or "extend the system"
- User wants to modify existing functionality that affects structure or behaviour
- User proposes a new integration or capability
- Any request that changes architecture, module boundaries, or system behaviour
- BEFORE implementing any feature or structural change, this skill MUST be invoked

**When NOT to use this skill:**
- Small bug fixes with no architectural impact
- Formatting, linting, or minor refactoring with no structural change
- Refactoring existing code without adding new features (use cas-refactor-module instead)

---

## Constraints (Prevent)

These constraints prevent architectural drift and maintain system integrity:

- **Module boundaries** - Align with existing module boundaries; no cross-layer imports
- **Pattern reuse** - Reuse existing patterns before introducing new structures
- **No duplication** - Don't duplicate existing logic or functionality
- **Separation of concerns** - Maintain clear layer separation
- **Traceability** - Document architectural impact and rationale
- **Provider abstraction** - External integrations (LLMs, APIs) require abstraction layers
- **MUST explicitly reference** at least one pattern from `.cas/patterns/patterns-catalogue.yaml`
- **MUST justify** the chosen architectural structure using patterns
- **MUST NOT include** meta-commentary outside the defined output schema
- **MUST produce exactly one** output block conforming to OUTPUT.schema.yaml
- **MUST include** a `decision` block in every output
- **MUST set** decision.status to one of: accepted | rejected | proposed

**Reference files:**
- `.cas/rules/architecture_rules.md` - Core architecture constraints
- `.cas/patterns/patterns-catalogue.yaml` - Reusable patterns

---

## Instructions

Follow this sequence to add a feature while preserving architectural integrity:

### 1. Understand the Request
- Read the feature request and identify its purpose
- Ask clarifying questions if the scope is ambiguous
- Identify the target module (user may specify, or infer from system structure)

### 2. Load Context
- Read `.cas/rules/architecture_rules.md` to understand constraints
- Read `.cas/patterns/patterns-catalogue.yaml` to find reusable patterns
- Review existing code structure in `src/` to avoid duplication

### 3. Validate Against Rules
- Check that the feature doesn't violate module boundaries
- Verify no cross-layer dependencies are introduced
- Ensure external integrations use provider abstractions

### 4. Design the Implementation
- Identify which files need to be created or modified
- Identify applicable patterns from patterns-catalogue.yaml
- Select the most appropriate pattern(s)
- Justify why these patterns are used
- If no pattern applies, explicitly justify the new structure
- Ensure all architecture rules are preserved

### 5. Produce Output
- MUST produce a single valid output block
- MUST always include the `decision` block, even for accepted features

---

## Output Contract

Your output must conform to this structure:

```yaml
output:
  feature:
    name: string        # Feature identifier
    module: string      # Target module
    description: string # What it does

  decision:
    status: string        # accepted | rejected | proposed
    reason: string        # Explanation for decision (especially for rejections)
    alternative: string   # Suggested alternative approach if rejected

  code_changes:
    - file: string      # Path to file
      change_type: string  # create | modify | delete
      summary: string      # What changed and why

  architecture_decision:
    description: string     # Architectural decision rationale
    rationale: string       # Why this approach was taken over alternatives
  
  architectural_impact:
    - affected_components: [string]
      pattern_usage: [string]  # Pattern IDs from catalogue
      pattern_justification: string  # Why this pattern applies or why a new structure is needed

  risks:
    - description: string  # Potential issues

  validation_notes:
    - description: string  # How you validated against rules
```

**Why this matters:** The structured output ensures the feature can be machine-validated against architecture rules and tracked for governance.

**Important:**
- OUTPUT.schema.yaml is the authoritative definition of this structure
- Do not duplicate or restate the schema elsewhere
- Output must be a single, clean YAML block with no surrounding commentary

---

## Anti-Patterns (must avoid)
- Introducing tight coupling between modules
- Creating new modules without justification
- Duplicating existing logic
- Bypassing established patterns
- Implicit dependencies or hidden integrations

---

## Pattern Usage
- Identify and reuse existing patterns before introducing new structures
- If no pattern applies, explicitly justify the new structure
- Prefer provider-abstraction for external integrations
- Maintain layered-architecture boundaries

---

## Examples

See `EXAMPLES.md` for worked examples showing input/output pairs.
