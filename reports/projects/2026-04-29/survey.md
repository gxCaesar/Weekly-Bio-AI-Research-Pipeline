# 调研报告（2026-04-29）

## 研究背景
将多智能体协作用于单细胞机制发现，可显著提升假设生成质量与验证效率。

## 每日调研摘要
请结合下方自动抓取报告继续补充：

---

# 每日 Bio+AI 自动调研报告（2026-04-29）

> 此报告由 GitHub Actions 每天自动在云端生成。

## AI / LLM / Agent 热点

1. **An Intelligent Fault Diagnosis Method for General Aviation Aircraft Based on Multi-Fidelity Digital Twin and FMEA Knowledge Enhancement**
   - 发布时间: Wed, 29 Apr 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2604.22777
   - 摘要: arXiv:2604.22777v1 Announce Type: new 
Abstract: Fault diagnosis of general aviation aircraft faces challenges including scarce real fault data, diverse fault types, and weak fault signatures. This paper proposes an intelligent fault diagnosis framework based on multi-fidelity di
2. **PExA: Parallel Exploration Agent for Complex Text-to-SQL**
   - 发布时间: Wed, 29 Apr 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2604.22934
   - 摘要: arXiv:2604.22934v1 Announce Type: new 
Abstract: LLM-based agents for text-to-SQL often struggle with latency-performance trade-off, where performance improvements come at the cost of latency or vice versa. We reformulate text-to-SQL generation within the lens of software test co
3. **The Power of Power Law: Asymmetry Enables Compositional Reasoning**
   - 发布时间: Wed, 29 Apr 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2604.22951
   - 摘要: arXiv:2604.22951v1 Announce Type: new 
Abstract: Natural language data follows a power-law distribution, with most knowledge and skills appearing at very low frequency. While a common intuition suggests that reweighting or curating data towards a uniform distribution may help mod
4. **On the Existence of an Inverse Solution for Preference-Based Reductions in Argumentation**
   - 发布时间: Wed, 29 Apr 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2604.22958
   - 摘要: arXiv:2604.22958v1 Announce Type: new 
Abstract: Preference-based argumentation frameworks (PAFs) extend Dung's approach to abstract argumentation (AAFs) by encoding preferences over arguments. Such preferences control the transformation of attacks into defeats, and different app
5. **Towards Causally Interpretable Wi-Fi CSI-Based Human Activity Recognition with Discrete Latent Compression and LTL Rule Extraction**
   - 发布时间: Wed, 29 Apr 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2604.22979
   - 摘要: arXiv:2604.22979v1 Announce Type: new 
Abstract: We address Human Activity Recognition (HAR) utilizing Wi-Fi Channel State Information (CSI) under the joint requirements of causal interpretability, symbolic controllability, and direct operation on high-dimensional raw signals. De
6. **FormalScience: Scalable Human-in-the-Loop Autoformalisation of Science with Agentic Code Generation in Lean**
   - 发布时间: Wed, 29 Apr 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2604.23002
   - 摘要: arXiv:2604.23002v1 Announce Type: new 
Abstract: Formalising informal mathematical reasoning into formally verifiable code is a significant challenge for large language models. In scientific fields such as physics, domain-specific machinery (\textit{e.g.} Dirac notation, vector c

## Bio / Bioinformatics 热点

1. **Pervasive and programmed nucleosome distortion on single chromatin fibres**
   - 发布时间: Wed, 29 Apr 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41586-026-10418-6
2. **A telomere-to-telomere reference genome for Stemona tuberosa**
   - 发布时间: Tue, 28 Apr 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41597-026-07266-4
3. **Accurate profiling of single-cell alternative transcript start sites by correcting RNA degradation**
   - 发布时间: Tue, 28 Apr 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72298-8
4. **When the genome learned its own vocabulary**
   - 发布时间: Mon, 27 Apr 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41576-026-00966-y
5. **In silico discovery of nanobody binders to a G-protein coupled receptor using AlphaFold-Multimer**
   - 发布时间: Thu, 23 Apr 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72093-5
6. **Multiomics immune profiling of a patient-relevant orthotopic lung cancer model using SEPARATE-Seq**
   - 发布时间: Thu, 23 Apr 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72247-5

## 今日可执行 Idea

- 建议方向：构建 agent 驱动的科研工作流，聚焦 single-cell 场景，并用 reasoning 提升假设生成质量；短期可在公开 protein 数据上完成可复现实验基线。

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

