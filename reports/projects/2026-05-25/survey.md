# 调研报告（2026-05-25）

## 研究背景
将多智能体协作用于单细胞机制发现，可显著提升假设生成质量与验证效率。

## 每日调研摘要
请结合下方自动抓取报告继续补充：

---

# 每日 Bio+AI 自动调研报告（2026-05-25）

> 此报告由 GitHub Actions 每天自动在云端生成。

## AI / LLM / Agent 热点

1. **BOHM: Zero-Cost Hierarchical Attribution for Compound AI Systems**
   - 发布时间: Mon, 25 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.22866
   - 摘要: arXiv:2605.22866v1 Announce Type: new 
Abstract: Compound AI systems route tasks through hierarchies of specialised components. Attribution is dominated by Shapley-based methods (SHAP), which decompose a coalition value function into per-component marginal contributions and requi
2. **NeuroNL2LTL: A Neurosymbolic Framework for Natural Language Translation of Linear Temporal Logic**
   - 发布时间: Mon, 25 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.22874
   - 摘要: arXiv:2605.22874v1 Announce Type: new 
Abstract: Effectively translating between natural language (NL) and formal logics like Linear Temporal Logic (LTL) requires expertise that limits formal verification's reach in safety-critical development. Template-based approaches sacrifice
3. **RMA: an Agentic System for Research-Level Mathematical Problems**
   - 发布时间: Mon, 25 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.22875
   - 摘要: arXiv:2605.22875v1 Announce Type: new 
Abstract: We present $\textbf{Research Math Agents (RMA)}$, an agentic framework for automated reasoning on research-level mathematical problems. Unlike prior studies centered on competition mathematics or formal theorem proving, RMA targets
4. **SciAtlas: A Large-Scale Knowledge Graph for Automated Scientific Research**
   - 发布时间: Mon, 25 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.22878
   - 摘要: arXiv:2605.22878v1 Announce Type: new 
Abstract: The exponential growth of global academic output has confronted researchers and AI agents with an unprecedented ``information explosion,'' where fragmented and unstructured knowledge organization impedes deep interdisciplinary inte
5. **Energy per Successful Goal: Goal-Level Energy Accounting for Agentic AI Systems**
   - 发布时间: Mon, 25 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.22883
   - 摘要: arXiv:2605.22883v1 Announce Type: new 
Abstract: Current AI energy benchmarks measure consumption at the granularity of a single model invocation or training run. For classical single-turn workloads this unit remains coherent. For agentic systems - where a single user goal may tr
6. **ImProver 2: Iteratively Self-Improving LMs for Neurosymbolic Proof Optimization**
   - 发布时间: Mon, 25 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.22885
   - 摘要: arXiv:2605.22885v1 Announce Type: new 
Abstract: Formal mathematics libraries are rapidly expanding, creating a growing need to refactor verified proofs for maintainability and to improve training data quality for neural provers. However, scalable proof optimization is hindered b

## Bio / Bioinformatics 热点

- 暂无可用条目

## 今日可执行 Idea

- 建议方向：构建 agent 驱动的科研工作流，聚焦 single-cell 场景，并用 agent 提升假设生成质量；短期可在公开 drug 数据上完成可复现实验基线。

## 明日建议跟踪

- 持续监控同主题 3 天内是否升温（重复出现 + 新增代码/数据）。
- 如果某主题连续升温，自动进入立项池并补充实验计划。

## 强化 Idea 模块（实验设计 + 投稿匹配分）

### 题目
- 多智能体协作驱动的单细胞机制发现自动化研究框架

### 核心假设
- 将多智能体协作用于单细胞机制发现，可显著提升假设生成质量与验证效率。

### 实验设计（可执行）
- 数据：公开数据集 + 1个外部独立验证队列（避免过拟合）。
- 方法：主方法 vs 单Agent基线 vs 无推理链基线（至少3组对比）。
- 评估：AUC/F1 + 新靶点命中率 + 人工专家一致性评分。
- 消融：去除检索模块、去除反馈回路、去除多智能体协作。
- 复现：固定随机种子、公开配置文件、输出误差条与显著性检验。

### 投稿匹配分（10分制）
- **NeurIPS**: 9.3 / 10（方法创新+大规模实验）
- **Nature Biotechnology**: 9.2 / 10（转化医学与产业潜力）
- **Nature Methods**: 9.1 / 10（高生物学验证）
- **ICML**: 9.0 / 10（机器学习理论/泛化）

### 主要风险
- 外部验证数据分布偏移导致指标下降。
- LLM 生成假设可能出现看似合理但不可验证的问题。
- 生物学验证成本高，需要提前规划最小验证闭环。

