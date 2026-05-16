# Architecture Rules

## Module Boundaries

- Each module must have a single responsibility
- Cross-module interaction must occur via explicit interfaces
- No direct cross-layer imports

## Dependency Management

- Core logic must not depend on external providers (LLM, APIs)
- External systems must be accessed via provider abstractions

## Determinism

- Core orchestration must remain deterministic
- Non-deterministic components must be isolated and optional

## Contracts

- All outputs must conform to explicit schemas
- No implicit or dynamic structures

## Pattern Reuse

- Existing patterns must be reused before introducing new ones
- New structures require justification

## Traceability

- All changes must include architectural impact and rationale
