#!/usr/bin/env bash
# Delete merged/stale remote branches on zero-cost-wealth-playbook-tool.
# Requires: gh auth login
set -euo pipefail
REPO="${REPO:-eric847b/zero-cost-wealth-playbook-tool}"

BRANCHES=(
  release-packaging
  fleet-ops-upgrade
  feat/add-mit-license
  feat/client-pack-zip
  feat/client-template-pack
  feat/consultant-cashflow-niche
  feat/creator-cashflow-niche
  feat/sales-one-pager
  feat-client-onboarding-checklist
  evolve/failure-solver-v3.5
  evolve/fs-core-modules
  evolve/fs-core-py
)

for b in "${BRANCHES[@]}"; do
  echo "Deleting $b ..."
  gh api -X DELETE "repos/${REPO}/git/refs/heads/${b}" 2>/dev/null \
    && echo "  ok" \
    || echo "  skip (missing or protected)"
done

# Dependabot leftovers
gh api "repos/${REPO}/branches?per_page=100" --jq '.[].name' \
  | grep '^dependabot/' \
  | while read -r b; do
      echo "Deleting $b ..."
      gh api -X DELETE "repos/${REPO}/git/refs/heads/${b}" 2>/dev/null \
        && echo "  ok" || echo "  skip"
    done

echo "Done. Remaining:"
gh api "repos/${REPO}/branches?per_page=100" --jq '.[].name'
