#!/usr/bin/env python3
"""Send latest report by email via SMTP, with optional attachments."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import mimetypes
import smtplib
from email.message import EmailMessage
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Send report via email")
    parser.add_argument("--report-dir", default="reports", help="Report directory")
    parser.add_argument("--idea-dir", default="reports/ideas", help="Idea json directory")
    parser.add_argument("--project-dir", default="reports/projects", help="Project package root")
    parser.add_argument("--date", default=None, help="Report date YYYY-MM-DD (default: today UTC)")
    parser.add_argument("--smtp-host", default="smtp.gmail.com")
    parser.add_argument("--smtp-port", type=int, default=587)
    parser.add_argument("--smtp-user", required=True)
    parser.add_argument("--smtp-pass", required=True)
    parser.add_argument("--from-email", required=True)
    parser.add_argument("--to-email", required=True)
    parser.add_argument("--attach-files", action="store_true", help="Attach generated files")
    parser.add_argument("--brief-lines", type=int, default=18, help="Max lines from report in email brief")
    return parser.parse_args()


def attach_file(msg: EmailMessage, path: Path) -> None:
    if not path.exists() or not path.is_file():
        return
    ctype, _ = mimetypes.guess_type(str(path))
    if ctype is None:
        maintype, subtype = "application", "octet-stream"
    else:
        maintype, subtype = ctype.split("/", 1)
    msg.add_attachment(path.read_bytes(), maintype=maintype, subtype=subtype, filename=path.name)


def parse_idea_title(idea_path: Path) -> str:
    if not idea_path.exists():
        return "（今日未生成结构化 idea）"
    try:
        data = json.loads(idea_path.read_text(encoding="utf-8"))
        return data.get("title", "（idea 标题缺失）")
    except Exception:
        return "（idea 解析失败）"


def main() -> None:
    args = parse_args()
    date_str = args.date or dt.datetime.utcnow().strftime("%Y-%m-%d")
    report_path = Path(args.report_dir) / f"{date_str}.md"
    idea_path = Path(args.idea_dir) / f"{date_str}.json"
    project_dir = Path(args.project_dir) / date_str

    if not report_path.exists():
        raise FileNotFoundError(f"Report not found: {report_path}")

    report_text = report_path.read_text(encoding="utf-8")
    brief_text = "\n".join(report_text.splitlines()[: args.brief_lines])
    idea_title = parse_idea_title(idea_path)

    attachments = [
        report_path,
        idea_path,
        project_dir / "survey.md",
        project_dir / "proposal.md",
        project_dir / "venue_assessment.md",
        project_dir / "manuscript_draft.md",
        project_dir / "handoff.html",
        project_dir / "READ_FIRST.md",
        project_dir / "code_plan/README.md",
    ]
    attached_names: list[str] = []

    msg = EmailMessage()
    msg["Subject"] = f"📬 [Daily Bio+AI Brief] {date_str}"
    msg["From"] = args.from_email
    msg["To"] = args.to_email

    text_body = (
        f"📌 每日简报（{date_str}）\n\n"
        f"🧠 今日核心 Idea: {idea_title}\n"
        f"📂 报告路径: {report_path}\n"
        f"📂 Idea 路径: {idea_path}\n"
        f"📂 Project 包: {project_dir}\n\n"
        "📝 报告摘要:\n"
        f"{brief_text}\n\n"
        "（本邮件为自动发送）"
    )
    msg.set_content(text_body)

    html_body = f"""
    <html><body style='font-family:Arial,Helvetica,sans-serif;'>
      <h2>📬 Daily Bio+AI Brief <span style='color:#666;'>({date_str})</span></h2>
      <p>🧠 <b>今日核心 Idea</b>: {html.escape(idea_title)}</p>
      <p>📂 <b>报告路径</b>: {html.escape(str(report_path))}<br/>
         📂 <b>Idea 路径</b>: {html.escape(str(idea_path))}<br/>
         📂 <b>Project 包</b>: {html.escape(str(project_dir))}</p>
      <h3>📝 简要摘要</h3>
      <pre style='background:#f7f7f7;padding:12px;border-radius:8px;white-space:pre-wrap;'>{html.escape(brief_text)}</pre>
      <p>✅ 本邮件由 GitHub Actions 自动生成。</p>
    </body></html>
    """
    msg.add_alternative(html_body, subtype="html")

    if args.attach_files:
        for path in attachments:
            if path.exists() and path.is_file():
                attach_file(msg, path)
                attached_names.append(path.name)

    if args.attach_files:
        attach_file(msg, report_path)
        attach_file(msg, idea_path)
        for rel in [
            "survey.md",
            "proposal.md",
            "venue_assessment.md",
            "manuscript_draft.md",
            "handoff.html",
            "READ_FIRST.md",
            "code_plan/README.md",
        ]:
            attach_file(msg, project_dir / rel)

    with smtplib.SMTP(args.smtp_host, args.smtp_port, timeout=30) as server:
        server.starttls()
        server.login(args.smtp_user, args.smtp_pass)
        server.send_message(msg)

    print(f"[OK] Email sent to {args.to_email} with report {report_path}")
    if attached_names:
        print(f"[OK] Attached files: {', '.join(attached_names)}")


if __name__ == "__main__":
    main()
