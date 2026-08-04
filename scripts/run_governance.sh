#!/usr/bin/env bash

set -e

echo "Generating favicon variants from source portrait..."
python scripts/build_favicons.py

echo ""
echo "Running MkDocs structural validation..."
mkdocs build --strict

echo ""
echo "Running terminology governance validation..."
python scripts/validate_governance.py

echo ""
echo "Portfolio governance validation completed successfully."
