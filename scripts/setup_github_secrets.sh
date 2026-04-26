#!/usr/bin/env bash
set -euo pipefail

# Usage (recommended: do not put secrets in shell history):
#   ./scripts/setup_github_secrets.sh
#
# Optional non-interactive mode:
#   GMAIL_SMTP_USER='xxx@gmail.com' \
#   GMAIL_SMTP_PASS='app_password' \
#   GMAIL_FROM_EMAIL='xxx@gmail.com' \
#   ./scripts/setup_github_secrets.sh

if ! command -v gh >/dev/null 2>&1; then
  echo "[ERROR] GitHub CLI (gh) is required. Install: https://cli.github.com/"
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "[ERROR] gh is not authenticated. Run: gh auth login"
  exit 1
fi


if [ -n "${GITHUB_TOKEN:-}" ] || [ -n "${GH_TOKEN:-}" ]; then
  echo "[ERROR] Detected GITHUB_TOKEN/GH_TOKEN in environment."
  echo "This is usually an integration token and often cannot manage repository secrets."
  echo "Please run: unset GITHUB_TOKEN GH_TOKEN"
  echo "Then login with personal account: gh auth login"
  exit 1
fi

TARGET_REPO="${GH_REPO:-}"
if [ -z "$TARGET_REPO" ]; then
  TARGET_REPO="$(gh repo view --json nameWithOwner -q .nameWithOwner 2>/dev/null || true)"
fi

if [ -z "$TARGET_REPO" ]; then
  echo "[ERROR] Cannot detect target repo. Set GH_REPO, e.g.:"
  echo "        GH_REPO=gxCaesar/Weekly-Bio-AI-Research-Pipeline ./scripts/setup_github_secrets.sh"
  exit 1
fi

if [ -z "${GMAIL_SMTP_USER:-}" ]; then
  read -r -p "GMAIL_SMTP_USER (e.g. your@gmail.com): " GMAIL_SMTP_USER
fi

if [ -z "${GMAIL_FROM_EMAIL:-}" ]; then
  read -r -p "GMAIL_FROM_EMAIL (usually same as SMTP user): " GMAIL_FROM_EMAIL
fi

if [ -z "${GMAIL_SMTP_PASS:-}" ]; then
  read -r -s -p "GMAIL_SMTP_PASS (Gmail App Password): " GMAIL_SMTP_PASS
  echo
fi

# Gmail app password is often displayed with spaces; strip them.
GMAIL_SMTP_PASS="${GMAIL_SMTP_PASS// /}"

: "${GMAIL_SMTP_USER:?GMAIL_SMTP_USER is required}"
: "${GMAIL_SMTP_PASS:?GMAIL_SMTP_PASS is required}"
: "${GMAIL_FROM_EMAIL:?GMAIL_FROM_EMAIL is required}"

if ! gh api "repos/${TARGET_REPO}/actions/secrets/public-key" >/dev/null 2>&1; then
  echo "[ERROR] Cannot access Actions secrets API for ${TARGET_REPO}."
  echo "Possible reasons:"
  echo "  1) You are using GitHub App/CI integration token (not a personal login)."
  echo "  2) Your account/token lacks permissions to manage repository secrets."
  echo "  3) Repo is not under your accessible scope."
  echo "Fix: run 'gh auth login' with your personal account, or set a PAT with 'repo' scope."
  echo "Then retry with: GH_REPO=${TARGET_REPO} ./scripts/setup_github_secrets.sh"
  exit 1
fi

echo -n "$GMAIL_SMTP_USER" | gh secret set GMAIL_SMTP_USER --repo "$TARGET_REPO"
echo -n "$GMAIL_SMTP_PASS" | gh secret set GMAIL_SMTP_PASS --repo "$TARGET_REPO"
echo -n "$GMAIL_FROM_EMAIL" | gh secret set GMAIL_FROM_EMAIL --repo "$TARGET_REPO"

echo "[OK] Secrets configured in ${TARGET_REPO}: GMAIL_SMTP_USER, GMAIL_SMTP_PASS, GMAIL_FROM_EMAIL"
