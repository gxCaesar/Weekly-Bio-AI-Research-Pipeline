# 调研报告（2026-05-08）

## 研究背景
将多智能体协作用于单细胞机制发现，可显著提升假设生成质量与验证效率。

## 每日调研摘要
请结合下方自动抓取报告继续补充：

---

# 每日 Bio+AI 自动调研报告（2026-05-08）

> 此报告由 GitHub Actions 每天自动在云端生成。

## AI / LLM / Agent 热点

1. **Understanding Annotator Safety Policy with Interpretability**
   - 发布时间: Fri, 08 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.05329
   - 摘要: arXiv:2605.05329v1 Announce Type: new 
Abstract: Safety policies define what constitutes safe and unsafe AI outputs, guiding data annotation and model development. However, annotation disagreement is pervasive and can stem from multiple sources such as operational failures (annot
2. **ZAYA1-8B Technical Report**
   - 发布时间: Fri, 08 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.05365
   - 摘要: arXiv:2605.05365v1 Announce Type: new 
Abstract: We present ZAYA1-8B, a reasoning-focused mixture-of-experts (MoE) model with 700M active and 8B total parameters, built on Zyphra's MoE++ architecture. ZAYA1-8B's core pretraining, midtraining, and supervised fine-tuning (SFT) were
3. **Partial Evidence Bench: Benchmarking Authorization-Limited Evidence in Agentic Systems**
   - 发布时间: Fri, 08 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.05379
   - 摘要: arXiv:2605.05379v1 Announce Type: new 
Abstract: Enterprise agents increasingly operate inside scoped retrieval systems, delegated workflows, and policy-constrained evidence environments. In these settings, access control can be enforced correctly while the system still produces 
4. **BALAR : A Bayesian Agentic Loop for Active Reasoning**
   - 发布时间: Fri, 08 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.05386
   - 摘要: arXiv:2605.05386v1 Announce Type: new 
Abstract: Large language models increasingly operate in interactive settings where solving a task requires multiple rounds of information exchange with a user. However, most current systems treat dialogue reactively and lack a principled mec
5. **Intelligent CCTV for Urban Design: AI-Based Analysis of Soft Infrastructure at Intersections**
   - 发布时间: Fri, 08 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.05402
   - 摘要: arXiv:2605.05402v1 Announce Type: new 
Abstract: Artificial intelligence (AI) and computer vision are transforming transportation data collection. This study introduces an AI-enabled analytics framework leveraging existing CCTV infrastructure to evaluate the impact of soft interv
6. **When Helpfulness Becomes Sycophancy: Sycophancy is a Boundary Failure Between Social Alignment and Epistemic Integrity in Large Language Models**
   - 发布时间: Fri, 08 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.05403
   - 摘要: arXiv:2605.05403v1 Announce Type: new 
Abstract: This position paper argues that sycophancy in LLMs is a boundary failure between social alignment and epistemic integrity. Existing work often operationalizes sycophancy through external behavior such as agreement with incorrect us

## Bio / Bioinformatics 热点

1. **ZAT-DNA enables DNA data storage with molecular-layer non-replicability**
   - 发布时间: Fri, 8 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72869-9
2. **Genome assembly of Astatotilapia latifasciata uncovers B chromosome–linked chromatin reorganization**
   - 发布时间: Thu, 7 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41437-026-00847-4
3. **Single-cell Stereo-seq reveals regulatory mechanisms driving regeneration of injured proximal tubules during AKI**
   - 发布时间: Wed, 6 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72679-z
4. **On the importance of being powerful to detecting specific regulations in omics studies**
   - 发布时间: Mon, 4 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41477-026-02303-x
5. **SCMBench: benchmarking domain-specific and foundation models for single-cell multi-omics data integration**
   - 发布时间: Sat, 2 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72570-x
6. **Spatial-aware detection of copy number alterations from spatial transcriptomics using SpaCNA**
   - 发布时间: Wed, 29 Apr 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72284-0

## 今日可执行 Idea

- 建议方向：构建 agent 驱动的科研工作流，聚焦 single-cell 场景，并用 reasoning 提升假设生成质量；短期可在公开 multi-omics 数据上完成可复现实验基线。

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

