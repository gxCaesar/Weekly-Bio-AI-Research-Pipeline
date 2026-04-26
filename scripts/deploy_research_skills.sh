#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ZIP_PATH="${1:-$ROOT_DIR/skill.zip}"
EXTRACT_DIR="${2:-$ROOT_DIR/.tmp/skill_unpack}"
SKILLS_HOME="${CODEX_HOME:-$HOME/.codex}/skills"

REQUIRED_SKILLS=(
  paper_reader
  idea_library
  research_plan
  conference_plan
  journal_plan
  research_copilot
  paper_polish_conf
  paper_polish_journal
  rebuttal_plan
)

echo "[INFO] zip: $ZIP_PATH"
echo "[INFO] extract to: $EXTRACT_DIR"
echo "[INFO] skills home: $SKILLS_HOME"

if [[ ! -f "$ZIP_PATH" ]]; then
  echo "[ERROR] zip not found: $ZIP_PATH" >&2
  exit 1
fi

rm -rf "$EXTRACT_DIR"
mkdir -p "$EXTRACT_DIR"
unzip -q "$ZIP_PATH" -d "$EXTRACT_DIR"

# Normalize archive root.
ARCHIVE_ROOT="$EXTRACT_DIR/skill"
if [[ ! -d "$ARCHIVE_ROOT" ]]; then
  CANDIDATE="$(find "$EXTRACT_DIR" -maxdepth 2 -type d -name skill | head -n 1 || true)"
  if [[ -z "$CANDIDATE" ]]; then
    echo "[ERROR] cannot find skill/ directory in archive" >&2
    exit 1
  fi
  ARCHIVE_ROOT="$CANDIDATE"
fi

# Clean known noisy files.
find "$EXTRACT_DIR" -name '__MACOSX' -type d -prune -exec rm -rf {} + || true
find "$ARCHIVE_ROOT" -name '.DS_Store' -delete || true
rm -rf "$ARCHIVE_ROOT/.git" "$ARCHIVE_ROOT/research_plan-workspace" || true

mkdir -p "$SKILLS_HOME"

for skill in "${REQUIRED_SKILLS[@]}"; do
  src="$ARCHIVE_ROOT/$skill"
  dst="$SKILLS_HOME/$skill"
  if [[ ! -f "$src/SKILL.md" ]]; then
    echo "[ERROR] invalid skill: $skill (missing SKILL.md)" >&2
    exit 1
  fi
  rm -rf "$dst"
  ln -s "$src" "$dst"
  echo "[OK] linked $skill -> $src"
done

echo "[INFO] deployment finished. Installed skills:"
ls -la "$SKILLS_HOME" | sed 's/^/[INFO] /'
