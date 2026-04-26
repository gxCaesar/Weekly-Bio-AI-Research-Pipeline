# 每天凌晨 2:00 的 Bio+AI 科研自动化方案（可落地）

## 1) 目标定义（先把系统做“可持续”）

每天自动产出一份 **Bio × AI（LLM/Agent）调研简报**，包含：
- 当天/近 24~72 小时 AI/LLM/Agent 最新热点（论文、开源仓库、公司动态、benchmark 结果）；
- 同期生命健康 / bioinformatics 热点（单细胞、基因组、药物发现、多组学、临床 AI）；
- 两者交叉形成的 **3 个潜在研究方向**；
- 其中 1 个方向给出 **可执行 idea（可投稿路径 + 实验计划）**。

> 建议把目标拆成：
> - 第 1 阶段：稳定抓取 + 去重 + 可信排序；
> - 第 2 阶段：自动生成“方向组合”；
> - 第 3 阶段：自动做小型可行性评估与实验提案。

---

## 2) 每日 2:00 自动化总流程（DAG）

### A. 数据采集层（2:00 开始）
1. AI 方向源：
   - arXiv（cs.AI / cs.LG / cs.CL / stat.ML）
   - OpenReview（ICLR/NeurIPS/ICML/ACL 等最近动态）
   - Papers with Code（新 SOTA）
   - GitHub Trending（LLM/Agent/tooling）
   - 头部实验室与公司 blog（OpenAI/Anthropic/Google DeepMind/Meta AI 等）

2. Bio 方向源：
   - bioRxiv / medRxiv
   - Nature / Cell / Science 子刊新闻与 highlights
   - PubMed 新文（可按关键词）
   - 单细胞与基因工具生态（Scanpy/scvi-tools/Seurat 生态、AlphaFold 系衍生方向）

3. 高价值补充：
   - ClinicalTrials（药物与适应症动态）
   - FDA / EMA 公告（监管与批准信号）

### B. 预处理层
- 去重：标题 + DOI + 语义向量近邻去重。
- 质量过滤：
  - 论文：是否有代码、数据、实验完整性；
  - repo：stars 增速、维护活跃度、issue 质量；
  - 新闻：来源可信度分级。
- 结构化：统一输出字段（标题、摘要、任务、数据集、方法关键词、时间、链接、影响力分）。

### C. 热点识别层
- 主题聚类（embedding + HDBSCAN/LDA）。
- 计算“热点分数”：
  - 新颖性（近 7 天首次出现）
  - 增速（提及量/引用量/star 增速）
  - 可迁移性（能否跨域到 bio）
- 输出 Top-N 热点主题（AI 与 Bio 各一组）。

### D. 交叉发现层（核心）
- 用规则 + LLM 生成交叉组合：
  - `AI 热点能力` × `Bio 高痛点场景` → 候选问题
- 例：
  - 长上下文 Agent × 多组学知识图谱 × 靶点发现
  - 推理型 LLM × 单细胞轨迹推断 × 机制解释
  - 多智能体工作流 × 自动假设生成 × 药物重定位

### E. 报告生成层（2:20~2:35）
自动生成 Markdown/PDF 报告：
1. 今日 AI 热点（5~10 条）
2. 今日 Bio 热点（5~10 条）
3. 跨域结合方向（3 条）
4. 今日推荐 idea（1 条，含实验计划）
5. 风险与下步数据需求

### F. 分发与提醒层（2:40）
- 邮件 / 飞书 / Slack 推送。
- 若某方向连续 3 天升温，自动标记“优先立项”。

---

## 3) 你最该先做的“最小可行版本”（2 周）

### 第 1 周
- 打通 arXiv + bioRxiv + PubMed + GitHub Trending 抓取。
- 建立统一 schema 与去重。
- 每天生成基础日报（仅摘要整理）。

### 第 2 周
- 增加热点评分与聚类。
- 增加 AI×Bio 自动交叉模块。
- 每日报告末尾稳定输出 1 个“可执行 idea”。

> 先保证“每天能稳定出一份 70 分报告”，再追求“偶尔 95 分灵感”。

---

## 4) “顶刊/顶会导向”idea 评估标准（自动打分）

每个候选 idea 进行 0~5 分打分：
1. **Novelty**：是否明确区别于近 6 个月已有工作；
2. **Significance**：解决的是否为真痛点（如临床可转化、药物发现效率）；
3. **Technical Depth**：是否有方法学创新，不只是工程拼接；
4. **Validation Strength**：是否能在公开数据 + 外部数据双验证；
5. **Reproducibility**：数据和代码可复现性；
6. **Submission Fit**：对应 venue 的匹配度（Nature Methods / Nature Biotechnology / NeurIPS / ICML / ICLR / RECOMB / ISMB）。

总分 >= 22 才进入“重点候选池”。

---

## 5) 一个示例“每日可执行 idea”模板

### Idea 标题
**BioAgent-RL: 面向单细胞靶点发现的多智能体假设生成与证据验证框架**

### 核心假设
多智能体（文献 agent、数据 agent、统计验证 agent）协作，可以在单细胞数据中更高效地产生“可验证的新靶点假设”。

### 方法草图
- Agent A：读文献，提取通路/基因关系；
- Agent B：在 scRNA-seq 数据上做差异与轨迹分析；
- Agent C：执行统计检验并回传置信度；
- 协调器：基于奖励函数（新颖性+可验证性）选择下一轮探索策略。

### 实验设计
- 数据：公开肿瘤单细胞数据集 + 外部独立队列；
- 对比：传统 pipeline、单 LLM pipeline、多智能体无反馈版本；
- 指标：命中已知靶点比例、新靶点验证成功率、分析耗时。

### 投稿路径
- 方法学强：NeurIPS/ICML (AI for Science track)
- 生物验证强：Nature Methods / Nature Biotechnology

---

## 6) 工程落地建议（技术栈）

- 调度：GitHub Actions cron / Airflow / Prefect（每天 2:00 UTC+8 或你的本地时区）。
- 存储：
  - 原始数据：对象存储；
  - 元数据：PostgreSQL；
  - 向量检索：pgvector / Weaviate。
- LLM 层：
  - 摘要与抽取：高性价比模型；
  - 关键判断（idea 打分）：高能力模型；
  - 强制 JSON schema 输出，便于程序消费。
- 可追溯性：每条结论绑定来源 URL + 时间戳。

---

## 7) 你可以立刻开始的下一步

1. 固定 20~30 个高质量数据源（AI 10 个 + Bio 10 个 + 监管/产业 5~10 个）。
2. 我可以先帮你定义统一数据 schema（paper/repo/news 三类）。
3. 再给你一版“日报模板 + 自动评分模板”。
4. 最后实现 cron 在凌晨 2:00 自动运行并推送。

如果你愿意，我下一步可以直接给你：
- `sources.yaml`（数据源配置）
- `report_template.md`（日报模板）
- `idea_scoring.json`（idea 自动评分规则）
