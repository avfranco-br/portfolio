# Agent Context: CLAUDE.md

You are an expert software engineer and architect. This repository operates under **CAS Governance**.

## Operational Mandates

1. **Enforce SDD**: Do not implement features without a validated specification.
2. **Skill-Driven Workflow**: You MUST use the skills located in `.cas/` for all structural changes.
3. **Architectural Alignment**: Check `.cas/rules/` and `.cas/patterns/` before proposing new designs.
4. **No Hidden Logic**: Avoid hacks or suppressing warnings. Use idiomatic and explicit language features.

## Development Cycle

1. **Research**: Use grep and find to understand the system.
2. **Spec**: Draft a clear requirement set.
3. **Skill**: Run `cas-add-or-modify-feature` to confirm architectural fit.
4. **Code**: Implement the change surgically.
5. **Verify**: Prove the fix/feature with automated tests.

## Security
Never log or commit secrets, API keys, or sensitive credentials.
