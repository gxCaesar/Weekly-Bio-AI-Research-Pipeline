#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DATE_TAG="$(date -u +%F)"
PROJECT="${PROJECT:-bio_ai_project}"
DOMAIN="${DOMAIN:-single-cell + LLM}"
VENUE_TYPE="${VENUE_TYPE:-dual}"
TIME_BUDGET_WEEKS="${TIME_BUDGET_WEEKS:-8}"
GPU_BUDGET="${GPU_BUDGET:-1x A100 80GB}"
OUT_DIR="${OUT_DIR:-$ROOT_DIR/reports/pre_experiment/$DATE_TAG-$PROJECT}"
SKILLS_HOME="${CODEX_HOME:-$HOME/.codex}/skills"

mkdir -p "$OUT_DIR"

# Basic validation
for s in paper_reader idea_library research_copilot; do
  if [[ ! -e "$SKILLS_HOME/$s/SKILL.md" ]]; then
    echo "[ERROR] missing required skill: $s ($SKILLS_HOME/$s)" >&2
    echo "[HINT] run ./scripts/deploy_research_skills.sh first" >&2
    exit 1
  fi
done

if [[ "$VENUE_TYPE" == "conference" && ! -e "$SKILLS_HOME/conference_plan/SKILL.md" ]]; then
  echo "[ERROR] conference_plan is required for VENUE_TYPE=conference" >&2
  exit 1
fi

if [[ "$VENUE_TYPE" == "journal" && ! -e "$SKILLS_HOME/journal_plan/SKILL.md" ]]; then
  echo "[ERROR] journal_plan is required for VENUE_TYPE=journal" >&2
  exit 1
fi

cat > "$OUT_DIR/pipeline_context.md" <<CTX
# Pre-Experiment Pipeline Context

- date: $DATE_TAG
- project: $PROJECT
- domain: $DOMAIN
- venue_type: $VENUE_TYPE
- time_budget_weeks: $TIME_BUDGET_WEEKS
- gpu_budget: $GPU_BUDGET

## stage outputs
- stage_a_paper_reader.md
- stage_b_idea_library.md
- stage_c_research_copilot.md
- stage_d_venue_specialization.md
- gate_report.md
CTX

cat > "$OUT_DIR/stage_a_paper_reader.md" <<A
# Stage A - paper_reader

Prompt:
\`\`\`
Use skill paper_reader.
Domain: $DOMAIN
Time window: recent 14 days
Goal: produce fast scan + deep read shortlist + knowledge links.
Output path: $OUT_DIR/stage_a_output
\`\`\`
A

cat > "$OUT_DIR/stage_b_idea_library.md" <<B
# Stage B - idea_library

Prompt:
\`\`\`
Use skill idea_library.
Input: Stage A outputs in $OUT_DIR/stage_a_output
Goal: generate 10 candidate ideas, run novelty verification, score by theory × bio significance.
Select top 3 ideas with risk and feasibility notes under $GPU_BUDGET.
Output path: $OUT_DIR/stage_b_output
\`\`\`
B

cat > "$OUT_DIR/stage_c_research_copilot.md" <<C
# Stage C - research_copilot

Prompt:
\`\`\`
Use skill research_copilot.
Inputs:
- Stage B top-3 ideas from $OUT_DIR/stage_b_output
Constraints:
- Hardware: $GPU_BUDGET
- Timeline: $TIME_BUDGET_WEEKS weeks
- Venue type preference: $VENUE_TYPE
Goal:
- produce proposal, architecture blueprint, experiment plan, and student handoff package.
Output path: $OUT_DIR/stage_c_output
\`\`\`
C

if [[ "$VENUE_TYPE" == "conference" ]]; then
  STAGE_D_SKILL="conference_plan"
elif [[ "$VENUE_TYPE" == "journal" ]]; then
  STAGE_D_SKILL="journal_plan"
else
  STAGE_D_SKILL="conference_plan + journal_plan (dual-track)"
fi

cat > "$OUT_DIR/stage_d_venue_specialization.md" <<D
# Stage D - venue specialization

Prompt:
\`\`\`
Use skill $STAGE_D_SKILL.
Input: Stage C outputs from $OUT_DIR/stage_c_output
Goal: convert generic plan into venue-specific submission strategy and deliverables.
Output path: $OUT_DIR/stage_d_output
\`\`\`
D

cat > "$OUT_DIR/gate_report.md" <<G
# Gate Report Template

## Gate-1 Novelty
- [ ] novelty score >= threshold

## Gate-2 Feasibility
- [ ] train/eval fits $GPU_BUDGET
- [ ] total schedule <= $TIME_BUDGET_WEEKS weeks

## Gate-3 Reproducibility
- [ ] dataset access paths defined
- [ ] baseline list and evaluation metrics frozen

## Gate-4 Submission-readiness
- [ ] venue-specific checklist completed
- [ ] post-experiment plan created
G

echo "[OK] pre-experiment pipeline scaffold generated: $OUT_DIR"
