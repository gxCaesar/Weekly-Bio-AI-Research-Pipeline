import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import scripts.strong_idea as si


class TestStrongIdea(unittest.TestCase):
    def test_detect_keywords_hits(self):
        hits = si.detect_keywords("agent reasoning for single-cell drug discovery", si.AI_KEYWORDS)
        self.assertIn("agent", hits)
        self.assertIn("reasoning", hits)

    def test_build_idea_has_submission_fit(self):
        idea = si.build_idea(["agent", "reasoning"], ["single-cell", "drug"])
        self.assertIn("submission_fit", idea)
        self.assertEqual(len(idea["submission_fit"]), 4)
        self.assertGreaterEqual(idea["submission_fit"][0]["score"], idea["submission_fit"][-1]["score"])

    def test_append_and_json_output(self):
        with TemporaryDirectory() as td:
            tmp_path = Path(td)
            report = tmp_path / "2026-04-26.md"
            report.write_text("# 每日 Bio+AI 自动调研报告（2026-04-26）\n\nagent single-cell\n", encoding="utf-8")

            idea = si.build_idea(["agent"], ["single-cell"])
            si.append_markdown(report, idea)

            text = report.read_text(encoding="utf-8")
            self.assertIn("## 强化 Idea 模块（实验设计 + 投稿匹配分）", text)

            out_json = tmp_path / "idea.json"
            out_json.write_text(json.dumps(idea, ensure_ascii=False), encoding="utf-8")
            self.assertTrue(json.loads(out_json.read_text(encoding="utf-8"))["title"])


if __name__ == "__main__":
    unittest.main()
