# 调研报告（2026-05-19）

## 研究背景
将多智能体协作用于单细胞机制发现，可显著提升假设生成质量与验证效率。

## 每日调研摘要
请结合下方自动抓取报告继续补充：

---

# 每日 Bio+AI 自动调研报告（2026-05-19）

> 此报告由 GitHub Actions 每天自动在云端生成。

## AI / LLM / Agent 热点

1. **AgentWall: A Runtime Safety Layer for Local AI Agents**
   - 发布时间: Tue, 19 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.16265
   - 摘要: arXiv:2605.16265v1 Announce Type: new 
Abstract: The safety of autonomous AI agents is increasingly recognized as a critical open problem. As agents transition from passive text generators to active actors capable of executing shell commands, modifying files, calling APIs, and br
2. **ANNEAL: Adapting LLM Agents via Governed Symbolic Patch Learning**
   - 发布时间: Tue, 19 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.16309
   - 摘要: arXiv:2605.16309v1 Announce Type: new 
Abstract: LLM-based agents can recover from individual execution errors, yet they repeatedly fail on the same fault when the underlying process knowledge--operator schemas, preconditions, and constraints--remains unrepaired. Existing self-ev
3. **From Prompts to Protocols: An AI Agent for Laboratory Automation**
   - 发布时间: Tue, 19 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.16552
   - 摘要: arXiv:2605.16552v1 Announce Type: new 
Abstract: Automating science laboratories enables faster, safer, more accurate, and more reproducible execution of protocols, accelerating the discovery and testing of new materials, drugs, and more. However, setting up and running autonomou
4. **Skim: Speculative Execution for Fast and Efficient Web Agents**
   - 发布时间: Tue, 19 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.16565
   - 摘要: arXiv:2605.16565v1 Announce Type: new 
Abstract: Skim is a speculative execution framework for web agents that exploits the predictable structure of purpose-built websites. Today's web-agent expense is not intrinsic to the tasks but a property of how agents are composed: frontier
5. **Scalable Uncertainty Reasoning in Knowledge Graphs**
   - 发布时间: Tue, 19 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.16568
   - 摘要: arXiv:2605.16568v1 Announce Type: new 
Abstract: Knowledge Graphs are pivotal for semantic data integration. The real-world data they model is often inherently uncertain. Within knowledge graphs, uncertainty manifests in three distinct levels: imprecise attribute values, probabil
6. **Counterparty Modeling is Not Strategy: The Limits of LLM Negotiators**
   - 发布时间: Tue, 19 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.16575
   - 摘要: arXiv:2605.16575v1 Announce Type: new 
Abstract: Negotiation requires more than inferring what the other side wants: it requires using that information to make advantageous offers and counteroffers over multiple turns. We study whether large language model (LLM) agents do this in

## Bio / Bioinformatics 热点

1. **HESpotEx: a dual-stream deep learning framework for spot-level gene expression prediction from histological images**
   - 发布时间: Fri, 15 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s43588-026-00992-0
2. **Transcriptional landscape of pulmonary artery endothelium reveals subpopulation- and disease-specific remodeling signatures**
   - 发布时间: Mon, 11 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s42003-026-10204-0
3. **CroCoDeEL: accurate control-free detection of cross-sample contamination in metagenomic data**
   - 发布时间: Sat, 9 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72637-9
4. **ZAT-DNA enables DNA data storage with molecular-layer non-replicability**
   - 发布时间: Fri, 8 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72869-9
5. **Genome assembly of Astatotilapia latifasciata uncovers B chromosome–linked chromatin reorganization**
   - 发布时间: Thu, 7 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41437-026-00847-4
6. **Single-cell Stereo-seq reveals regulatory mechanisms driving regeneration of injured proximal tubules during AKI**
   - 发布时间: Wed, 6 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72679-z

## 今日可执行 Idea

- 建议方向：构建 agent 驱动的科研工作流，聚焦 single-cell 场景，并用 reasoning 提升假设生成质量；短期可在公开 single-cell 数据上完成可复现实验基线。

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

