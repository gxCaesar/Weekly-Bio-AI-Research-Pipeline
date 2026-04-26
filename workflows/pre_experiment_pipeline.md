# 实验前自动化流程（Pre-Experiment Pipeline）

该流程将你上传的科研 skills 串成一条可重复执行的标准化流水线：

1. **Stage A / paper_reader**：跟踪最近论文，沉淀候选方向。
2. **Stage B / idea_library**：对候选方向做新颖性验证与打分。
3. **Stage C / research_copilot**：将 top ideas 转为可执行研究方案。
4. **Stage D / conference_plan 或 journal_plan**：按投稿目标生成 venue-specific 包。

## 部署（先做）

```bash
bash ./scripts/deploy_research_skills.sh ./skill.zip
# 默认安装到当前仓库 ./skills/
```

## 一键生成执行 Runbook

Codespaces 推荐：
```bash
make preexp-codespace
```

### 方式 A：环境变量

```bash
PROJECT=virtual_cell_agent \
DOMAIN='virtual cell + llm agent' \
VENUE_TYPE=dual \
TIME_BUDGET_WEEKS=8 \
GPU_BUDGET='1x A100 80GB' \
./scripts/run_pre_experiment_pipeline.sh
```

### 方式 B：YAML 配置

```bash
./scripts/run_pre_experiment_pipeline.sh --config workflows/pre_experiment_config.example.yaml
```

## 输出位置

`reports/pre_experiment/<date>-<project>/`

包含：
- `RUNBOOK.md`（执行总入口）
- `pipeline_context.md`
- `stage_a_paper_reader.md`
- `stage_b_idea_library.md`
- `stage_c_research_copilot.md`
- `stage_d_venue_specialization.md`
- `execution_checklist.md`
- `gate_report.md`

## 建议执行策略

- 每周至少跑 1 次完整流程。
- Stage B 的 top3 ideas 进入 Stage C，避免一次只押注 1 个方向。
- Gate 未通过时，不进入下一阶段，先回滚到前一阶段修正。
