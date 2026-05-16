# Agent Context: GEMINI.md

You are an interactive CLI agent specializing in software engineering. This repository enforces **CAS Governance**.

## Mandatory Instructions

1. **Always read AGENTS.md**: This is your primary source of operational boundaries.
2. **Use CAS Skills**: Before modifying any code, you MUST activate the appropriate skill in `.cas/`.
3. **Specification-First**: If a user asks for a feature, your first step is to create or update a spec in `specs/`.
4. **Surgical Edits**: Prefer precise code replacements over overwriting entire files.
5. **Validate Behavior**: Never assume a change is correct. Always run tests or validation scripts.

## Topic Management
Use the `update_topic` tool (if available) to keep the user informed of your strategic intent and progress across multi-turn tasks.

## Code Conventions
- Adhere to the local project style found in existing source files.
- Prioritize composition and delegation over complex inheritance.
- Ensure all new logic is covered by unit or integration tests.

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan
<!-- SPECKIT END -->
