#!/usr/bin/env bash

set -e

# Use virtualenv python and mkdocs if .venv exists
if [ -d ".venv" ]; then
    PYTHON_CMD=".venv/bin/python"
    MKDOCS_CMD=".venv/bin/mkdocs"
else
    PYTHON_CMD="python"
    MKDOCS_CMD="mkdocs"
fi

echo "Generating favicon variants from source portrait..."
$PYTHON_CMD scripts/build_favicons.py

echo ""
echo "Running MkDocs structural validation..."
$MKDOCS_CMD build --strict

echo ""
echo "Running terminology governance validation..."
$PYTHON_CMD scripts/validate_governance.py

echo ""
echo "Portfolio governance validation completed successfully."
