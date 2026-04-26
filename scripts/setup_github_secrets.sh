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

echo -n "$GMAIL_SMTP_USER" | gh secret set GMAIL_SMTP_USER
echo -n "$GMAIL_SMTP_PASS" | gh secret set GMAIL_SMTP_PASS
echo -n "$GMAIL_FROM_EMAIL" | gh secret set GMAIL_FROM_EMAIL

echo "[OK] Secrets configured: GMAIL_SMTP_USER, GMAIL_SMTP_PASS, GMAIL_FROM_EMAIL"
