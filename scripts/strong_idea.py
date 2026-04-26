#!/usr/bin/env python3
"""Generate a stronger daily research idea block and append to report."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path


AI_KEYWORDS = {
    "agent": "多智能体协作",
    "reasoning": "可验证推理链",
    "multimodal": "多模态融合",
    "retrieval": "检索增强",
    "rl": "强化学习优化",
    "long context": "长上下文记忆",
    "transformer": "Transformer 架构改进",
}

BIO_KEYWORDS = {
    "single-cell": "单细胞机制发现",
    "genomics": "基因组功能注释",
    "drug": "药物重定位",
    "target": "靶点发现",
    "rna": "RNA 调控网络",
    "protein": "蛋白结构-功能预测",
    "multi-omics": "多组学联合建模",
    "clinical": "临床风险分层",
}

VENUE_RULES = [
    ("方法创新+大规模实验", "NeurIPS", 8.8),
    ("机器学习理论/泛化", "ICML", 8.5),
    ("推理/Agent系统", "ICLR", 8.3),
    ("生物算法和系统生物学", "RECOMB", 8.0),
    ("生物信息学应用", "ISMB", 7.8),
    ("高生物学验证", "Nature Methods", 8.6),
    ("转化医学与产业潜力", "Nature Biotechnology", 8.7),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Append stronger idea module to daily report")
    parser.add_argument("--report-dir", default="reports", help="Report directory")
    parser.add_argument("--output-dir", default="reports/ideas", help="Structured idea output directory")
    parser.add_argument("--date", default=None, help="Report date YYYY-MM-DD (default: today UTC)")
    return parser.parse_args()


def detect_keywords(text: str, mapping: dict[str, str]) -> list[str]:
    found = []
    low = text.lower()
    for key in mapping:
        if key in low:
            found.append(key)
    return found


def score_submission_fit(ai_hits: list[str], bio_hits: list[str]) -> list[dict[str, str | float]]:
    score_boost = min(1.0, (len(ai_hits) + len(bio_hits)) * 0.1)
    ranked = []
    for why, venue, base in VENUE_RULES:
        ranked.append({"venue": venue, "score": round(min(9.5, base + score_boost), 2), "why": why})
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked[:4]


def build_idea(ai_hits: list[str], bio_hits: list[str]) -> dict:
    ai_focus = AI_KEYWORDS.get(ai_hits[0], "多智能体协作") if ai_hits else "多智能体协作"
    bio_focus = BIO_KEYWORDS.get(bio_hits[0], "单细胞机制发现") if bio_hits else "单细胞机制发现"

    title = f"{ai_focus}驱动的{bio_focus}自动化研究框架"
    hypothesis = f"将{ai_focus}用于{bio_focus}，可显著提升假设生成质量与验证效率。"

    experiment_plan = [
        "数据：公开数据集 + 1个外部独立验证队列（避免过拟合）。",
        "方法：主方法 vs 单Agent基线 vs 无推理链基线（至少3组对比）。",
        "评估：AUC/F1 + 新靶点命中率 + 人工专家一致性评分。",
        "消融：去除检索模块、去除反馈回路、去除多智能体协作。",
        "复现：固定随机种子、公开配置文件、输出误差条与显著性检验。",
    ]

    risks = [
        "外部验证数据分布偏移导致指标下降。",
        "LLM 生成假设可能出现看似合理但不可验证的问题。",
        "生物学验证成本高，需要提前规划最小验证闭环。",
    ]

    submissions = score_submission_fit(ai_hits, bio_hits)

    return {
        "title": title,
        "hypothesis": hypothesis,
        "ai_hits": ai_hits,
        "bio_hits": bio_hits,
        "experiment_plan": experiment_plan,
        "risks": risks,
        "submission_fit": submissions,
    }


def append_markdown(report_path: Path, idea: dict) -> None:
    lines = [
        "",
        "## 强化 Idea 模块（实验设计 + 投稿匹配分）",
        "",
        f"### 题目\n- {idea['title']}",
        "",
        f"### 核心假设\n- {idea['hypothesis']}",
        "",
        "### 实验设计（可执行）",
    ]
    for step in idea["experiment_plan"]:
        lines.append(f"- {step}")

    lines.extend(["", "### 投稿匹配分（10分制）"])
    for item in idea["submission_fit"]:
        lines.append(f"- **{item['venue']}**: {item['score']} / 10（{item['why']}）")

    lines.extend(["", "### 主要风险", *[f"- {r}" for r in idea["risks"]], ""])

    with report_path.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main() -> None:
    args = parse_args()
    date_str = args.date or dt.datetime.utcnow().strftime("%Y-%m-%d")
    report_path = Path(args.report_dir) / f"{date_str}.md"
    if not report_path.exists():
        raise FileNotFoundError(f"Report not found: {report_path}")

    content = report_path.read_text(encoding="utf-8")
    if "## 强化 Idea 模块（实验设计 + 投稿匹配分）" in content:
        print(f"[OK] Enhanced idea block already exists: {report_path}")
        return

    ai_hits = detect_keywords(content, AI_KEYWORDS)
    bio_hits = detect_keywords(content, BIO_KEYWORDS)
    idea = build_idea(ai_hits, bio_hits)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_json = output_dir / f"{date_str}.json"
    output_json.write_text(json.dumps(idea, ensure_ascii=False, indent=2), encoding="utf-8")

    append_markdown(report_path, idea)
    print(f"[OK] Enhanced idea appended: {report_path}")
    print(f"[OK] Structured idea saved: {output_json}")


if __name__ == "__main__":
    main()
