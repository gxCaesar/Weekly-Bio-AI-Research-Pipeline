# 调研报告（2026-05-28）

## 研究背景
将多智能体协作用于单细胞机制发现，可显著提升假设生成质量与验证效率。

## 每日调研摘要
请结合下方自动抓取报告继续补充：

---

# 每日 Bio+AI 自动调研报告（2026-05-28）

> 此报告由 GitHub Actions 每天自动在云端生成。

## AI / LLM / Agent 热点

1. **Identifying and Understanding Human Values in Text: A Tailorable LLM-based Architecture**
   - 发布时间: Thu, 28 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.27373
   - 摘要: arXiv:2605.27373v1 Announce Type: new 
Abstract: As intelligent systems become more autonomous, the scientific community focuses on creating decision-making mechanisms that include ethical and moral considerations, unlike traditional utility-maximisation models. To achieve this, 
2. **Soro: A Lightweight Foundation Model and Chatbot for Tajik**
   - 发布时间: Thu, 28 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.27379
   - 摘要: arXiv:2605.27379v1 Announce Type: new 
Abstract: We present Soro, a family of Tajik-specialized conversational large language models (LLMs) designed for real-world deployment under tight compute and connectivity constraints in Tajikistan. Starting from open-weight Gemma 3 checkpo
3. **On the Origin of Synthetic Information by Means of Steganographic Inheritance**
   - 发布时间: Thu, 28 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.27551
   - 摘要: arXiv:2605.27551v1 Announce Type: new 
Abstract: The origin of species has been the mystery of mysteries in natural science. By analogy, the origin of synthetic information, we suggest, is the mystery of mysteries in information science. The question carries a moral weight that a
4. **DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks and Observability Paradox in LLM-based Scheduling Agents**
   - 发布时间: Thu, 28 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.27566
   - 摘要: arXiv:2605.27566v1 Announce Type: new 
Abstract: Progress in neural combinatorial optimization for Dynamic Flexible Job Shop Scheduling Problem (DFJSP) is currently hindered by a methodological tension: static benchmarks encourage benchmark overfitting, while uncalibrated generat
5. **Why LLMs Fail at Causal Discovery and How Interventional Agents Escape**
   - 发布时间: Thu, 28 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.27567
   - 摘要: arXiv:2605.27567v1 Announce Type: new 
Abstract: Causal discovery is a cornerstone of scientific reasoning, yet whether large language models can perform it reliably remains an open question. Recent benchmarks show that even fine-tuned models plateau on simple causal graphs and d
6. **RULER: Representation-Level Verification of Machine Unlearning**
   - 发布时间: Thu, 28 May 2026 00:00:00 -0400
   - 链接: https://arxiv.org/abs/2605.27569
   - 摘要: arXiv:2605.27569v1 Announce Type: new 
Abstract: Machine unlearning aims to remove the influence of specific training records from a deployed model without retraining from scratch. Current protocols verify this at the output level through membership inference, retain accuracy, an

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

