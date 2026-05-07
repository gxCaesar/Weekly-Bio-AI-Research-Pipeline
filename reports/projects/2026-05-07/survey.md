# 调研报告（2026-05-07）

## 研究背景
将多智能体协作用于单细胞机制发现，可显著提升假设生成质量与验证效率。

## 每日调研摘要
请结合下方自动抓取报告继续补充：

---

# 每日 Bio+AI 自动调研报告（2026-05-07）

> 此报告由 GitHub Actions 每天自动在云端生成。

## AI / LLM / Agent 热点

1. **CreativityBench: Evaluating Agent Creative Reasoning via Affordance-Based Tool Repurposing**
   - 发布时间: Thu, 07 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.02910
   - 摘要: arXiv:2605.02910v2 Announce Type: new 
Abstract: Recent advances in large language models have led to strong performance on reasoning and environment-interaction tasks, yet their ability for creative problem-solving remains underexplored. We study this capability through the lens
2. **Stable Agentic Control: Tool-Mediated LLM Architecture for Autonomous Cyber Defense**
   - 发布时间: Thu, 07 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.03034
   - 摘要: arXiv:2605.03034v1 Announce Type: new 
Abstract: Agentic systems involved in high-stake decision-making under adversarial pressure need formal guarantees not offered by existing approaches. Motivated by the operational needs of security operations centers (SOCs) that must configu
3. **Computing Thiele Rules on Interval Elections and their Generalizations**
   - 发布时间: Thu, 07 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.03067
   - 摘要: arXiv:2605.03067v1 Announce Type: new 
Abstract: Approval-based committee voting has received significant attention in the social choice community. Among the studied rules, Thiele rules, and especially Proportional Approval Voting (PAV), stand out for desirable properties such as
4. **Making the Invisible Visible: Understanding the Mismatch Between Organizational Goals and Worker Experiences in AI Adoption**
   - 发布时间: Thu, 07 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.03078
   - 摘要: arXiv:2605.03078v1 Announce Type: new 
Abstract: While AI is often introduced into organizations to drive innovation and efficiency, many adoption efforts fail as workers resist and struggle to integrate these systems. These failures point to a deeper issue: workers, the very peo
5. **Programmatic Context Augmentation for LLM-based Symbolic Regression**
   - 发布时间: Thu, 07 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.03101
   - 摘要: arXiv:2605.03101v1 Announce Type: new 
Abstract: Symbolic regression (SR), the task of discovering mathematical expressions that best describe a given dataset, remains a fundamental challenge in scientific discovery. Traditional approaches, primarily based on genetic algorithms a
6. **Are you with me? A Framework for Detecting Mental Model Discrepancies in Task-Based Team Dialogues**
   - 发布时间: Thu, 07 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.03149
   - 摘要: arXiv:2605.03149v1 Announce Type: new 
Abstract: Humans typically use natural language to update teammates on task states. Since not all updates are communicated, discrepancies arise between the team members' mental models that negatively affect overall team performance. How can 

## Bio / Bioinformatics 热点

1. **Genome assembly of Astatotilapia latifasciata uncovers B chromosome–linked chromatin reorganization**
   - 发布时间: Thu, 7 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41437-026-00847-4
2. **Single-cell Stereo-seq reveals regulatory mechanisms driving regeneration of injured proximal tubules during AKI**
   - 发布时间: Wed, 6 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72679-z
3. **On the importance of being powerful to detecting specific regulations in omics studies**
   - 发布时间: Mon, 4 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41477-026-02303-x
4. **SCMBench: benchmarking domain-specific and foundation models for single-cell multi-omics data integration**
   - 发布时间: Sat, 2 May 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72570-x
5. **Spatial-aware detection of copy number alterations from spatial transcriptomics using SpaCNA**
   - 发布时间: Wed, 29 Apr 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41467-026-72284-0
6. **Pervasive and programmed nucleosome distortion on single chromatin fibres**
   - 发布时间: Wed, 29 Apr 2026 00:00:00 +0000
   - 链接: https://www.nature.com/articles/s41586-026-10418-6

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
- **NeurIPS**: 9.2 / 10（方法创新+大规模实验）
- **Nature Biotechnology**: 9.1 / 10（转化医学与产业潜力）
- **Nature Methods**: 9.0 / 10（高生物学验证）
- **ICML**: 8.9 / 10（机器学习理论/泛化）

### 主要风险
- 外部验证数据分布偏移导致指标下降。
- LLM 生成假设可能出现看似合理但不可验证的问题。
- 生物学验证成本高，需要提前规划最小验证闭环。

