#!/usr/bin/env python3
"""Generate a daily Bio+AI trend report from RSS sources."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import re
from pathlib import Path
from typing import Any
from urllib.request import urlopen
import xml.etree.ElementTree as ET

import json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate daily research report")
    parser.add_argument("--config", default="config/sources.json", help="YAML source config")
    parser.add_argument("--output-dir", default="reports", help="Output directory")
    parser.add_argument("--date", default=None, help="Report date YYYY-MM-DD (default: today UTC)")
    parser.add_argument("--max-items", type=int, default=6, help="Max items per category")
    return parser.parse_args()


def load_config(path: str) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def fetch_rss(url: str) -> list[dict[str, str]]:
    with urlopen(url, timeout=20) as resp:
        data = resp.read()

    root = ET.fromstring(data)
    items: list[dict[str, str]] = []

    for item in root.findall("./channel/item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        pub_date = (item.findtext("pubDate") or item.findtext("dc:date") or "").strip()
        description = (item.findtext("description") or "").strip()
        description = re.sub(r"<[^>]+>", "", html.unescape(description)).strip()

        if title and link:
            items.append(
                {
                    "title": title,
                    "link": link,
                    "pub_date": pub_date,
                    "summary": description[:280],
                }
            )

    return items


def normalize_titles(items: list[dict[str, str]]) -> list[dict[str, str]]:
    seen: set[str] = set()
    unique: list[dict[str, str]] = []
    for it in items:
        key = re.sub(r"\W+", "", it["title"].lower())
        if key in seen:
            continue
        seen.add(key)
        unique.append(it)
    return unique


def pick_top(items: list[dict[str, str]], max_items: int) -> list[dict[str, str]]:
    return items[:max_items]


def extract_keywords(titles: list[str], vocabulary: list[str]) -> list[str]:
    found = []
    joined = " ".join(titles).lower()
    for word in vocabulary:
        if word.lower() in joined:
            found.append(word)
    return found[:3]


def generate_idea(ai_titles: list[str], bio_titles: list[str]) -> str:
    ai_vocab = ["agent", "reasoning", "multimodal", "long context", "rl", "retrieval", "diffusion", "transformer"]
    bio_vocab = ["single-cell", "genomics", "drug", "target", "rna", "protein", "multi-omics", "clinical"]

    ai_keys = extract_keywords(ai_titles, ai_vocab) or ["agent", "reasoning"]
    bio_keys = extract_keywords(bio_titles, bio_vocab) or ["single-cell", "drug"]

    return (
        f"建议方向：构建 {ai_keys[0]} 驱动的科研工作流，聚焦 {bio_keys[0]} 场景，并用 {ai_keys[-1]} "
        f"提升假设生成质量；短期可在公开 {bio_keys[-1]} 数据上完成可复现实验基线。"
    )


def render_section(title: str, items: list[dict[str, str]]) -> str:
    lines = [f"## {title}", ""]
    if not items:
        lines.append("- 暂无可用条目")
        lines.append("")
        return "\n".join(lines)

    for idx, it in enumerate(items, start=1):
        lines.append(f"{idx}. **{it['title']}**")
        if it["pub_date"]:
            lines.append(f"   - 发布时间: {it['pub_date']}")
        lines.append(f"   - 链接: {it['link']}")
        if it["summary"]:
            lines.append(f"   - 摘要: {it['summary']}")
    lines.append("")
    return "\n".join(lines)


def build_report(date_str: str, ai_items: list[dict[str, str]], bio_items: list[dict[str, str]]) -> str:
    ai_titles = [i["title"] for i in ai_items]
    bio_titles = [i["title"] for i in bio_items]
    idea = generate_idea(ai_titles, bio_titles)

    content = [
        f"# 每日 Bio+AI 自动调研报告（{date_str}）",
        "",
        "> 此报告由 GitHub Actions 每天自动在云端生成。",
        "",
        render_section("AI / LLM / Agent 热点", ai_items),
        render_section("Bio / Bioinformatics 热点", bio_items),
        "## 今日可执行 Idea",
        "",
        f"- {idea}",
        "",
        "## 明日建议跟踪",
        "",
        "- 持续监控同主题 3 天内是否升温（重复出现 + 新增代码/数据）。",
        "- 如果某主题连续升温，自动进入立项池并补充实验计划。",
        "",
    ]
    return "\n".join(content)


def main() -> None:
    args = parse_args()
    date_str = args.date or dt.datetime.utcnow().strftime("%Y-%m-%d")

    cfg = load_config(args.config)
    ai_all: list[dict[str, str]] = []
    bio_all: list[dict[str, str]] = []

    for source in cfg.get("ai", []):
        if source.get("type") != "rss":
            continue
        try:
            ai_all.extend(fetch_rss(source["url"]))
        except Exception as exc:  # noqa: BLE001
            print(f"[WARN] AI source failed: {source.get('name')} ({exc})")

    for source in cfg.get("bio", []):
        if source.get("type") != "rss":
            continue
        try:
            bio_all.extend(fetch_rss(source["url"]))
        except Exception as exc:  # noqa: BLE001
            print(f"[WARN] Bio source failed: {source.get('name')} ({exc})")

    ai_items = pick_top(normalize_titles(ai_all), args.max_items)
    bio_items = pick_top(normalize_titles(bio_all), args.max_items)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{date_str}.md"
    output_file.write_text(build_report(date_str, ai_items, bio_items), encoding="utf-8")
    print(f"[OK] Report generated: {output_file}")


if __name__ == "__main__":
    main()
