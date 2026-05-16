# Operational Governance: AGENTS.md

This repository uses the **Continuous Architecture System (CAS)** to ensure architectural integrity and operational discipline. All coding agents (AI) and human contributors must adhere to the following rules.

## Core Mandates

1. **Specification-Driven Development (SDD)**: No feature implementation or structural change shall begin without a corresponding specification (e.g., in `specs/` or `.specify/`).
2. **CAS Skill Enforcement**: Mandatory CAS Skills located in `.cas/` MUST be used before any code modifications.
3. **Decision Traceability**: Every architectural decision must be documented with rationale.
4. **Minimal Drift**: Code changes must align strictly with the approved specification and architectural rules.

## Interaction Workflow

1. **Research**: Map the codebase and understand the existing patterns.
2. **Specify**: Define the "What" and "Why" in a specification file.
3. **Align**: Invoke the relevant CAS Skill (e.g., `cas-add-or-modify-feature`) to validate the design against rules.
4. **Implement**: Execute the change based on the validated design.
5. **Validate**: Verify the change with tests and CI checks.

## Skill Registry

- **cas-add-or-modify-feature**: Use for any new feature or change to existing behavior.
- **cas-refactor-module**: Use for restructuring code without changing behavior.

---
*This file is a governance contract. Do not modify without an approved architectural decision.*
