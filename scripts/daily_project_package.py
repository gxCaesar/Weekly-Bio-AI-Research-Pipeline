#!/usr/bin/env python3
"""Build a daily project package from report + idea outputs."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate daily project package")
    p.add_argument("--report-dir", default="reports")
    p.add_argument("--idea-dir", default="reports/ideas")
    p.add_argument("--output-root", default="reports/projects")
    p.add_argument("--date", default=None, help="YYYY-MM-DD, default today UTC")
    return p.parse_args()


def load_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def load_idea(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    args = parse_args()
    date_str = args.date or dt.datetime.utcnow().strftime("%Y-%m-%d")

    report_path = Path(args.report_dir) / f"{date_str}.md"
    idea_path = Path(args.idea_dir) / f"{date_str}.json"
    out_dir = Path(args.output_root) / date_str

    report_text = load_text(report_path)
    idea = load_idea(idea_path)

    title = idea.get("title", "Bio+AI 自动化研究项目")
    hypothesis = idea.get("hypothesis", "待根据每日调研报告完善")
    venues = idea.get("submission_fit", [])
    top_venues = ", ".join([f"{x.get('venue')}({x.get('score')})" for x in venues[:3]]) or "NeurIPS / ICML / Nature Methods"

    survey_md = f"""# 调研报告（{date_str}）\n\n## 研究背景\n{hypothesis}\n\n## 每日调研摘要\n请结合下方自动抓取报告继续补充：\n\n---\n\n{report_text or '（今日报告缺失，需补跑 make run-daily）'}\n"""

    proposal_md = f"""# 研究方案（{date_str}）\n\n## 项目名称\n{title}\n\n## 核心假设\n{hypothesis}\n\n## 创新点（自动草案）\n1. 结合每日热点形成可快速验证的创新假设。\n2. 使用公开数据构建可复现实验管线。\n3. 预留会议/期刊双轨投稿策略。\n\n## 实验计划（第一版）\n- 数据准备\n- 模型训练\n- 评估与消融\n- 结果整理\n"""

    venue_md = f"""# Venue 评估（{date_str}）\n\n## 推荐投稿目标\n{top_venues}\n\n## 评估维度\n- 新颖性\n- 可行性（算力/时间）\n- 生物学意义\n- 可复现性\n\n## 决策建议\n- 若方法创新突出，优先顶会。\n- 若生物学验证完整，优先期刊。\n"""

    code_readme = f"""# Code Delivery Plan\n\n## 目标\n交付完整可运行代码（数据、训练、评估、作图、消融）。\n\n## 目录建议\n- configs/\n- data/\n- models/\n- training/\n- evaluation/\n- scripts/\n\n## 每日更新要求\n- 保持 README 可执行\n- 记录依赖和命令\n- 固定随机种子\n"""

    manuscript_md = f"""# Manuscript Draft (No Results)\n\n## 1. Introduction\n- Problem motivation\n- Gap and challenge\n\n## 2. Related Work\n- AI side\n- Bioinformatics side\n\n## 3. Method\n- Overall architecture\n- Key modules\n\n## 4. Experimental Setup\n- Datasets\n- Baselines\n- Metrics\n\n## 5. Results (TO FILL AFTER EXPERIMENTS)\n- Main results\n- Ablation\n- Case studies\n"""

    handoff_html = f"""<!doctype html><html><head><meta charset='utf-8'><title>Project Handoff {date_str}</title></head><body>
<h1>项目交付说明（{date_str}）</h1>
<h2>项目背景</h2><p>{hypothesis}</p>
<h2>学生需要做什么</h2><ul><li>按 proposal 执行数据与训练</li><li>记录实验日志与结果表</li><li>将结果填入 manuscript 的 Results 章节</li></ul>
<h2>交付物清单</h2><ul><li>调研报告 survey.md</li><li>研究方案 proposal.md</li><li>venue评估 venue_assessment.md</li><li>manuscript_draft.md</li></ul>
</body></html>"""

    read_first = f"""# READ_FIRST\n\n## 你将看到的文件\n- survey.md: 调研报告\n- proposal.md: 研究方案\n- venue_assessment.md: 投稿决策\n- code_plan/README.md: 代码交付规范\n- manuscript_draft.md: 论文草稿（结果前）\n- handoff.html: 给学生执行说明\n\n## 学生执行步骤\n1. 先读 proposal.md\n2. 按 code_plan/README.md 完成代码与实验\n3. 把结果回填到 manuscript_draft.md 的 Results 章节\n4. 更新图表与结论后提交最终论文\n"""

    write(out_dir / "survey.md", survey_md)
    write(out_dir / "proposal.md", proposal_md)
    write(out_dir / "venue_assessment.md", venue_md)
    write(out_dir / "code_plan" / "README.md", code_readme)
    write(out_dir / "manuscript_draft.md", manuscript_md)
    write(out_dir / "handoff.html", handoff_html)
    write(out_dir / "READ_FIRST.md", read_first)

    print(f"[OK] Daily project package generated: {out_dir}")


if __name__ == "__main__":
    main()
