# Live Reload Polling Hook — Design Spec

**Date:** 2026-08-04
**Status:** Proposed
**Scope:** Guarantee reliable live reloading during `mkdocs serve` on macOS.

---

## 1. Problem

On macOS (Darwin), `watchdog.observers.Observer` defaults to `FSEventsObserver`. In certain local terminal environments (e.g. IDE terminals, background subshells, or macOS 15 system event loop configurations), FSEvents stream events can stall or be dropped. As a result, `mkdocs serve` stops detecting file modifications (such as edits to `docs/index.md`), preventing automatic site rebuilds.

## 2. Goal

Ensure `mkdocs serve` reliably detects all file modifications across `docs/`, `scripts/`, `specs/`, and `governance/` and immediately rebuilds the site during local development on macOS.

## 3. Approach

Create an MkDocs hook script (`scripts/mkdocs_hooks.py`) registered in `mkdocs.yml`:

```python
"""MkDocs hooks for local development and governance."""
import platform
import watchdog.observers
import watchdog.observers.polling

# On macOS, FSEventsObserver can miss events in certain subshells/terminals.
# Fallback to PollingObserver to guarantee reliable file watching.
if platform.system() == "Darwin":
    watchdog.observers.Observer = watchdog.observers.polling.PollingObserver
```

And in `mkdocs.yml`:

```yaml
hooks:
  - scripts/mkdocs_hooks.py
```

## 4. Acceptance Criteria

- `mkdocs serve` starts cleanly without errors.
- Any modification to `docs/index.md` or other watched files triggers an immediate rebuild log (`Detected file changes...`).
- `mkdocs build --strict` and `pytest tests/` pass without failure.
