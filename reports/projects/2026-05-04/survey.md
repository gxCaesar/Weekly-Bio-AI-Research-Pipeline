# 调研报告（2026-05-04）

## 研究背景
将多智能体协作用于单细胞机制发现，可显著提升假设生成质量与验证效率。

## 每日调研摘要
请结合下方自动抓取报告继续补充：

---

# 每日 Bio+AI 自动调研报告（2026-05-04）

> 此报告由 GitHub Actions 每天自动在云端生成。

## AI / LLM / Agent 热点

1. **Putting HUMANS first: Efficient LAM Evaluation with Human Preference Alignment**
   - 发布时间: Mon, 04 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.00022
   - 摘要: arXiv:2605.00022v1 Announce Type: new 
Abstract: The rapid proliferation of large audio models (LAMs) demands efficient approaches for model comparison, yet comprehensive benchmarks are costly. To fill this gap, we investigate whether minimal subsets can reliably evaluate LAMs wh
2. **NorBERTo: A ModernBERT Model Trained for Portuguese with 331 Billion Tokens Corpus**
   - 发布时间: Mon, 04 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.00086
   - 摘要: arXiv:2605.00086v1 Announce Type: new 
Abstract: High-quality corpora are essential for advancing Natural Language Processing (NLP) in Portuguese. Building on previous encoder-only models such as BERTimbau and Albertina PT-BR, we introduce NorBERTo, a modern encoder based on the 
3. **How Frontier LLMs Adapt to Neurodivergence Context: A Measurement Framework for Surface vs. Structural Change in System-Prompted Responses**
   - 发布时间: Mon, 04 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.00113
   - 摘要: arXiv:2605.00113v1 Announce Type: new 
Abstract: We examine if frontier chat-based large language models (LLMs) adjust their outputs based on neurodivergence (ND) context in system prompts and describe the nature of these adjustments. Specifically, we propose NDBench, a 576-outpu
4. **ViLegalNLI: Natural Language Inference for Vietnamese Legal Texts**
   - 发布时间: Mon, 04 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.00116
   - 摘要: arXiv:2605.00116v1 Announce Type: new 
Abstract: In this article, we introduce ViLegalNLI, the first large-scale Vietnamese Natural Language Inference (NLI) dataset specifically constructed for the legal domain. The dataset consists of 42,012 premise-hypothesis pairs derived from
5. **Cultural Benchmarking of LLMs in Standard and Dialectal Arabic Dialogues**
   - 发布时间: Mon, 04 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.00119
   - 摘要: arXiv:2605.00119v1 Announce Type: new 
Abstract: There is a significant gap in evaluating cultural reasoning in LLMs using conversational datasets that capture culturally rich and dialectal contexts. Most Arabic benchmarks focus on short text snippets in Modern Standard Arabic (M
6. **Timing is Everything: Temporal Scaffolding of Semantic Surprise in Humor**
   - 发布时间: Mon, 04 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.00143
   - 摘要: arXiv:2605.00143v1 Announce Type: new 
Abstract: Humor is a fundamental cognitive phenomenon in which humans derive pleasure from the expectation violations and their resolution, exemplifying the brain's dynamic capacity for predictive processing. Classical humor theories emphasi

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
- **NeurIPS**: 9.3 / 10（方法创新+大规模实验）
- **Nature Biotechnology**: 9.2 / 10（转化医学与产业潜力）
- **Nature Methods**: 9.1 / 10（高生物学验证）
- **ICML**: 9.0 / 10（机器学习理论/泛化）

### 主要风险
- 外部验证数据分布偏移导致指标下降。
- LLM 生成假设可能出现看似合理但不可验证的问题。
- 生物学验证成本高，需要提前规划最小验证闭环。

