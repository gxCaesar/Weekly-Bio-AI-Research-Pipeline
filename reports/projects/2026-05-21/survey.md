# 调研报告（2026-05-21）

## 研究背景
将多智能体协作用于单细胞机制发现，可显著提升假设生成质量与验证效率。

## 每日调研摘要
请结合下方自动抓取报告继续补充：

---

# 每日 Bio+AI 自动调研报告（2026-05-21）

> 此报告由 GitHub Actions 每天自动在云端生成。

## AI / LLM / Agent 热点

1. **Position: Let's Develop Data Probes to Fundamentally Understand How Data Affects LLM Performance**
   - 发布时间: Thu, 21 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.18801
   - 摘要: arXiv:2605.18801v1 Announce Type: new 
Abstract: Data is fundamental to large language models (LLMs). However, understanding of what makes certain data useful for different stages of an LLM workflow, including training, tuning, alignment, in-context learning, etc., and why, remai
2. **Operationalizing Document AI: A Microservice Architecture for OCR and LLM Pipelines in Production**
   - 发布时间: Thu, 21 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.18818
   - 摘要: arXiv:2605.18818v1 Announce Type: new 
Abstract: Academic research tends to focus on new models for document understanding creating a wide gap in the literature between model definition and running models at production scale. To close that gap, we present a microservice architect
3. **Evaluating the Utility of Personal Health Records in Personalized Health AI**
   - 发布时间: Thu, 21 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.18937
   - 摘要: arXiv:2605.18937v1 Announce Type: new 
Abstract: Patient-managed Personal Health Records (PHRs) promises to empower patients to better understand their health; but information in the record is complex, potentially hindering insights. In this study, we assess the potential of larg
4. **Learn-by-Wire Training Control Governance: Bounded Autonomous Training Under Stress for Stability and Efficiency**
   - 发布时间: Thu, 21 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.19008
   - 摘要: arXiv:2605.19008v1 Announce Type: new 
Abstract: Modern language-model training is increasingly exposed to instability, degraded runs, and wasted compute, especially under aggressive learning-rate, scale, and runtime-stress conditions. This paper introduces Learn-by-Wire Guard (L
5. **AgentNLQ: A General-Purpose Agent for Natural Language to SQL**
   - 发布时间: Thu, 21 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.19010
   - 摘要: arXiv:2605.19010v1 Announce Type: new 
Abstract: Natural language to SQL (NL2SQL) conversion is an important problem for researchers and enterprises due to the ubiquitous importance of relational databases in broad-ranging practical problems. Despite the rapid advancements in the
6. **KAN-MLP-Mixer: A comprehensive investigation of the usage of Kolmogorov-Arnold Networks (KANs) for improving IMU-based Human Activity Recognition**
   - 发布时间: Thu, 21 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.19031
   - 摘要: arXiv:2605.19031v1 Announce Type: new 
Abstract: Kolmogorov-Arnold Networks (KANs) have demonstrated an exceptional ability to learn complex functions on clean, low-dimensional data but struggle to maintain performance on noisy and imperfect real-world datasets. In contrast, conv

## Bio / Bioinformatics 热点

1. **omicsGMF: a multi-tool for dimensionality reduction, batch correction and imputation in bulk- and single-cell proteomics**
   - 发布时间: Wed, 20 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-73402-8
2. **HESpotEx: a dual-stream deep learning framework for spot-level gene expression prediction from histological images**
   - 发布时间: Fri, 15 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s43588-026-00992-0
3. **Transcriptional landscape of pulmonary artery endothelium reveals subpopulation- and disease-specific remodeling signatures**
   - 发布时间: Mon, 11 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s42003-026-10204-0
4. **CroCoDeEL: accurate control-free detection of cross-sample contamination in metagenomic data**
   - 发布时间: Sat, 9 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72637-9
5. **ZAT-DNA enables DNA data storage with molecular-layer non-replicability**
   - 发布时间: Fri, 8 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72869-9
6. **Genome assembly of Astatotilapia latifasciata uncovers B chromosome–linked chromatin reorganization**
   - 发布时间: Thu, 7 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41437-026-00847-4

## 今日可执行 Idea

- 建议方向：构建 agent 驱动的科研工作流，聚焦 single-cell 场景，并用 agent 提升假设生成质量；短期可在公开 single-cell 数据上完成可复现实验基线。

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
- **NeurIPS**: 9.2 / 10（方法创新+大规模实验）
- **Nature Biotechnology**: 9.1 / 10（转化医学与产业潜力）
- **Nature Methods**: 9.0 / 10（高生物学验证）
- **ICML**: 8.9 / 10（机器学习理论/泛化）

### 主要风险
- 外部验证数据分布偏移导致指标下降。
- LLM 生成假设可能出现看似合理但不可验证的问题。
- 生物学验证成本高，需要提前规划最小验证闭环。

