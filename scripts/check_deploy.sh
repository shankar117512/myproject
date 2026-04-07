#!/bin/bash
# Check deployment health across all environments

set -euo pipefail

echo "═══════════════════════════════════════"
echo "  Railway Deployment Status Check"
echo "═══════════════════════════════════════"

for ENV in dev staging production; do
  echo ""
  echo "── Environment: $ENV ──────────────────"
  railway environment use "$ENV" 2>/dev/null
  railway status 2>/dev/null || echo "  Status unavailable"
done

echo ""
echo "═══════════════════════════════════════"
