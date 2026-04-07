#!/bin/bash
# ─────────────────────────────────────────────────────────────────
# Manual Rollback Script for Railway Environments
# Usage: ./scripts/rollback.sh <environment> [deployment_id]
# ─────────────────────────────────────────────────────────────────

set -euo pipefail

ENVIRONMENT="${1:-}"
DEPLOYMENT_ID="${2:-}"

if [ -z "$ENVIRONMENT" ]; then
  echo "Usage: $0 <dev|staging|production> [deployment_id]"
  exit 1
fi

# Validate environment
case "$ENVIRONMENT" in
  dev|staging|production) ;;
  *) echo "❌ Invalid environment: $ENVIRONMENT"; exit 1 ;;
esac

echo "🔄 Initiating rollback for environment: $ENVIRONMENT"

# Switch to correct environment
railway environment use "$ENVIRONMENT"

if [ -z "$DEPLOYMENT_ID" ]; then
  # Get the previous successful deployment
  echo "Fetching deployment history..."
  DEPLOYMENTS=$(railway deployments list --json 2>/dev/null)
  
  # Get second most recent deployment (index 1)
  DEPLOYMENT_ID=$(echo "$DEPLOYMENTS" | jq -r '.[1].id' 2>/dev/null || echo "")
  
  if [ -z "$DEPLOYMENT_ID" ] || [ "$DEPLOYMENT_ID" = "null" ]; then
    echo "❌ Could not determine previous deployment ID"
    exit 1
  fi
fi

echo "Rolling back to deployment: $DEPLOYMENT_ID"

# Confirm for production
if [ "$ENVIRONMENT" = "production" ]; then
  read -p "⚠️  Are you sure you want to rollback PRODUCTION? (yes/no): " CONFIRM
  if [ "$CONFIRM" != "yes" ]; then
    echo "Rollback cancelled"
    exit 0
  fi
fi

railway deployments rollback "$DEPLOYMENT_ID"

echo "✅ Rollback complete for $ENVIRONMENT environment"
echo "Rolled back to deployment: $DEPLOYMENT_ID"

