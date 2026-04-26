#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DATE_TAG="$(date -u +%F)"

CONFIG_PATH=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --config)
      CONFIG_PATH="$2"
      shift 2
      ;;
    *)
      echo "[ERROR] unknown argument: $1" >&2
      echo "Usage: $0 [--config workflows/pre_experiment_config.example.yaml]" >&2
      exit 1
      ;;
  esac
done

PROJECT="${PROJECT:-bio_ai_project}"
DOMAIN="${DOMAIN:-single-cell + LLM}"
VENUE_TYPE="${VENUE_TYPE:-dual}"
TIME_BUDGET_WEEKS="${TIME_BUDGET_WEEKS:-8}"
GPU_BUDGET="${GPU_BUDGET:-1x A100 80GB}"
NOVELTY_GATE_MIN="${NOVELTY_GATE_MIN:-3.5}"
OUT_DIR="${OUT_DIR:-}"
SKILLS_HOME="${SKILLS_HOME:-$ROOT_DIR/skills}"

yaml_get() {
  local key="$1"
  local file="$2"
  local raw
  raw="$(awk -F':' -v k="$key" '$1==k {sub(/^[^:]*:[[:space:]]*/, "", $0); print $0; exit}' "$file")"
  raw="${raw%%#*}"
  raw="$(echo "$raw" | xargs)"
  raw="${raw%\"}"
  raw="${raw#\"}"
  raw="${raw%\'}"
  raw="${raw#\'}"
  echo "$raw"
}

if [[ -n "$CONFIG_PATH" ]]; then
  if [[ ! -f "$CONFIG_PATH" ]]; then
    echo "[ERROR] config file not found: $CONFIG_PATH" >&2
    exit 1
  fi
  PROJECT="$(yaml_get project "$CONFIG_PATH")"
  DOMAIN="$(yaml_get domain "$CONFIG_PATH")"
  VENUE_TYPE="$(yaml_get venue_type "$CONFIG_PATH")"
  TIME_BUDGET_WEEKS="$(yaml_get time_budget_weeks "$CONFIG_PATH")"
  GPU_BUDGET="$(yaml_get gpu_budget "$CONFIG_PATH")"
  NOVELTY_GATE_MIN="$(yaml_get novelty_gate_min "$CONFIG_PATH")"
fi

if [[ -z "$OUT_DIR" ]]; then
  OUT_DIR="$ROOT_DIR/reports/pre_experiment/$DATE_TAG-$PROJECT"
fi

mkdir -p "$OUT_DIR"

for s in paper_reader idea_library research_copilot; do
  if [[ ! -e "$SKILLS_HOME/$s/SKILL.md" ]]; then
    echo "[ERROR] missing required skill: $s ($SKILLS_HOME/$s)" >&2
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

case "$VENUE_TYPE" in
  conference) STAGE_D_SKILL="conference_plan" ;;
  journal) STAGE_D_SKILL="journal_plan" ;;
  dual) STAGE_D_SKILL="conference_plan + journal_plan" ;;
  *)
    echo "[ERROR] VENUE_TYPE must be one of: conference|journal|dual" >&2
    exit 1
    ;;
esac

cat > "$OUT_DIR/pipeline_context.md" <<CTX
# Pre-Experiment Pipeline Context

- date: $DATE_TAG
- project: $PROJECT
- domain: $DOMAIN
- venue_type: $VENUE_TYPE
- time_budget_weeks: $TIME_BUDGET_WEEKS
- gpu_budget: $GPU_BUDGET
- novelty_gate_min: $NOVELTY_GATE_MIN

## stage outputs
- stage_a_paper_reader.md
- stage_b_idea_library.md
- stage_c_research_copilot.md
- stage_d_venue_specialization.md
- execution_checklist.md
- gate_report.md
CTX

cat > "$OUT_DIR/stage_a_paper_reader.md" <<A
# Stage A - paper_reader

执行命令（复制到对话中）:

a) Use skill paper_reader.

b) Domain: $DOMAIN

c) 仅关注最近 14 天文献，输出：
- 前沿主题列表
- 关键论文 10 篇
- 每篇 3 行结论
- 触发的新idea列表

输出目录：$OUT_DIR/stage_a_output
A

cat > "$OUT_DIR/stage_b_idea_library.md" <<B
# Stage B - idea_library

执行命令（复制到对话中）:

a) Use skill idea_library.

b) 读取 Stage A 输出并生成 >=10 个候选 idea。

c) 每个 idea 输出 novelty check（含对比工作）与 feasibility 评估，最后给出 top3。

约束：$GPU_BUDGET, $TIME_BUDGET_WEEKS weeks
输出目录：$OUT_DIR/stage_b_output
B

cat > "$OUT_DIR/stage_c_research_copilot.md" <<C
# Stage C - research_copilot

执行命令（复制到对话中）:

a) Use skill research_copilot.

b) 输入：Stage B top3。

c) 输出 proposal、architecture blueprint、ablation plan、学生执行清单。

约束：$GPU_BUDGET, $TIME_BUDGET_WEEKS weeks, venue=$VENUE_TYPE
输出目录：$OUT_DIR/stage_c_output
C

cat > "$OUT_DIR/stage_d_venue_specialization.md" <<D
# Stage D - venue specialization

执行命令（复制到对话中）:

a) Use skill $STAGE_D_SKILL.

b) 输入：Stage C outputs。

c) 输出 venue-specific 投稿包（结构、检查清单、补充材料计划）。

输出目录：$OUT_DIR/stage_d_output
D

cat > "$OUT_DIR/execution_checklist.md" <<E
# Execution Checklist

- [ ] Stage A 已完成并写入 stage_a_output
- [ ] Stage B 已完成并选出 top3 ideas
- [ ] Stage C 已完成并生成 proposal + plan
- [ ] Stage D 已完成并生成 venue-specific package
- [ ] Gate 检查已通过
E

cat > "$OUT_DIR/gate_report.md" <<G
# Gate Report Template

## Gate-1 Novelty
- [ ] top idea novelty score >= $NOVELTY_GATE_MIN

## Gate-2 Feasibility
- [ ] train/eval fits $GPU_BUDGET
- [ ] total schedule <= $TIME_BUDGET_WEEKS weeks

## Gate-3 Reproducibility
- [ ] dataset access paths defined
- [ ] baseline list and metrics frozen

## Gate-4 Submission-readiness
- [ ] venue-specific checklist completed
- [ ] post-experiment plan created
G

cat > "$OUT_DIR/RUNBOOK.md" <<R
# RUNBOOK

1. 打开 stage_a_paper_reader.md，执行 A 阶段。
2. 打开 stage_b_idea_library.md，执行 B 阶段。
3. 打开 stage_c_research_copilot.md，执行 C 阶段。
4. 打开 stage_d_venue_specialization.md，执行 D 阶段。
5. 在 execution_checklist.md 和 gate_report.md 打勾。
R

echo "[OK] pre-experiment pipeline generated: $OUT_DIR"
