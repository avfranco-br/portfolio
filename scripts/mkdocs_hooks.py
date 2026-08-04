"""MkDocs hooks for local development and governance.

Ensures cross-platform reliability for live reloading on macOS by configuring
watchdog to use PollingObserver during `mkdocs serve`.
"""

from __future__ import annotations

import platform
import watchdog.observers
import watchdog.observers.polling

# On macOS (Darwin), FSEventsObserver can stall or miss events in subshells
# or IDE terminals. Fallback to PollingObserver to guarantee reliable file watching.
if platform.system() == "Darwin":
    watchdog.observers.Observer = watchdog.observers.polling.PollingObserver
