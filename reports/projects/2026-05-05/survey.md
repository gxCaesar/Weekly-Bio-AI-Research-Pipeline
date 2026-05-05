# 调研报告（2026-05-05）

## 研究背景
将多智能体协作用于单细胞机制发现，可显著提升假设生成质量与验证效率。

## 每日调研摘要
请结合下方自动抓取报告继续补充：

---

# 每日 Bio+AI 自动调研报告（2026-05-05）

> 此报告由 GitHub Actions 每天自动在云端生成。

## AI / LLM / Agent 热点

1. **TADI: Tool-Augmented Drilling Intelligence via Agentic LLM Orchestration over Heterogeneous Wellsite Data**
   - 发布时间: Tue, 05 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.00060
   - 摘要: arXiv:2605.00060v1 Announce Type: new 
Abstract: We present TADI (Tool-Augmented Drilling Intelligence), an agentic AI system that transforms drilling operational data into evidence-based analytical intelligence. Applied to the Equinor Volve Field dataset, TADI integrates 1,759 d
2. **AgentReputation: A Decentralized Agentic AI Reputation Framework**
   - 发布时间: Tue, 05 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.00073
   - 摘要: arXiv:2605.00073v1 Announce Type: new 
Abstract: Decentralized, agentic AI marketplaces are rapidly emerging to support software engineering tasks such as debugging, patch generation, and security auditing, often operating without centralized oversight. However, existing reputati
3. **Minimal, Local, Causal Explanations for Jailbreak Success in Large Language Models**
   - 发布时间: Tue, 05 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.00123
   - 摘要: arXiv:2605.00123v1 Announce Type: new 
Abstract: Safety trained large language models (LLMs) can often be induced to answer harmful requests through jailbreak prompts. Because we lack a robust understanding of why LLMs are susceptible to jailbreaks, future frontier models operati
4. **Are Tools All We Need? Unveiling the Tool-Use Tax in LLM Agents**
   - 发布时间: Tue, 05 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.00136
   - 摘要: arXiv:2605.00136v1 Announce Type: new 
Abstract: Tool-augmented reasoning has become a popular direction for LLM-based agents, and it is widely assumed to improve reasoning and reliability. However, we demonstrate that this consensus does not always hold: in the presence of seman
5. **TUR-DPO: Topology- and Uncertainty-Aware Direct Preference Optimization**
   - 发布时间: Tue, 05 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.00224
   - 摘要: arXiv:2605.00224v1 Announce Type: new 
Abstract: Aligning large language models (LLMs) with human preferences is commonly done via reinforcement learning from human feedback (RLHF) with Proximal Policy Optimization (PPO) or, more simply, via Direct Preference Optimization (DPO). 
6. **ARMOR 2025: A Military-Aligned Benchmark for Evaluating Large Language Model Safety Beyond Civilian Contexts**
   - 发布时间: Tue, 05 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.00245
   - 摘要: arXiv:2605.00245v1 Announce Type: new 
Abstract: Large language models (LLMs) are now being explored for defense applications that require reliable and legally compliant decision support. They also hold significant potential to enhance decision making, coordination, and operation

## Bio / Bioinformatics 热点

1. **On the importance of being powerful to detecting specific regulations in omics studies**
   - 发布时间: Mon, 4 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41477-026-02303-x
2. **SCMBench: benchmarking domain-specific and foundation models for single-cell multi-omics data integration**
   - 发布时间: Sat, 2 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72570-x
3. **Spatial-aware detection of copy number alterations from spatial transcriptomics using SpaCNA**
   - 发布时间: Wed, 29 Apr 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72284-0
4. **Pervasive and programmed nucleosome distortion on single chromatin fibres**
   - 发布时间: Wed, 29 Apr 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41586-026-10418-6
5. **A telomere-to-telomere reference genome for Stemona tuberosa**
   - 发布时间: Tue, 28 Apr 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41597-026-07266-4
6. **Accurate profiling of single-cell alternative transcript start sites by correcting RNA degradation**
   - 发布时间: Tue, 28 Apr 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72298-8

## 今日可执行 Idea

- 建议方向：构建 agent 驱动的科研工作流，聚焦 single-cell 场景，并用 agent 提升假设生成质量；短期可在公开 multi-omics 数据上完成可复现实验基线。

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
- **NeurIPS**: 9.4 / 10（方法创新+大规模实验）
- **Nature Biotechnology**: 9.3 / 10（转化医学与产业潜力）
- **Nature Methods**: 9.2 / 10（高生物学验证）
- **ICML**: 9.1 / 10（机器学习理论/泛化）

### 主要风险
- 外部验证数据分布偏移导致指标下降。
- LLM 生成假设可能出现看似合理但不可验证的问题。
- 生物学验证成本高，需要提前规划最小验证闭环。

