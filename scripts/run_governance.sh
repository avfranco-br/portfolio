#!/usr/bin/env bash

set -e

echo "Running MkDocs structural validation..."
mkdocs build --strict

echo ""
echo "Running terminology governance validation..."
python scripts/validate_governance.py

echo ""
echo "Portfolio governance validation completed successfully."
