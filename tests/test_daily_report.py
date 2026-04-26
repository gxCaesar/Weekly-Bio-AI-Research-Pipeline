import unittest

import scripts.daily_report as dr


class TestDailyReport(unittest.TestCase):
    def test_normalize_titles_removes_duplicates(self):
        items = [
            {"title": "A study on Agents", "link": "u1", "pub_date": "", "summary": ""},
            {"title": "A-study on agents!", "link": "u2", "pub_date": "", "summary": ""},
            {"title": "Different Paper", "link": "u3", "pub_date": "", "summary": ""},
        ]
        out = dr.normalize_titles(items)
        self.assertEqual(len(out), 2)

    def test_build_report_contains_sections(self):
        ai = [{"title": "Agent reasoning", "link": "u1", "pub_date": "today", "summary": "s1"}]
        bio = [{"title": "single-cell target", "link": "u2", "pub_date": "today", "summary": "s2"}]
        text = dr.build_report("2026-04-26", ai, bio)
        self.assertIn("# 每日 Bio+AI 自动调研报告（2026-04-26）", text)
        self.assertIn("## AI / LLM / Agent 热点", text)
        self.assertIn("## Bio / Bioinformatics 热点", text)
        self.assertIn("## 今日可执行 Idea", text)


if __name__ == "__main__":
    unittest.main()
