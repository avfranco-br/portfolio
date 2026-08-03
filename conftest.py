"""Repository-root conftest.

Adds the scripts/ directory to sys.path so test modules can
`from validate_governance import ...` regardless of where pytest is invoked.
This file runs before any test module is collected, which an in-test
fixture cannot do.
"""

import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent / "scripts"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))