#!/usr/bin/env python3
"""Send latest report by email via SMTP, with optional attachments."""

from __future__ import annotations

import argparse
import datetime as dt
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


def main() -> None:
    args = parse_args()
    date_str = args.date or dt.datetime.utcnow().strftime("%Y-%m-%d")
    report_path = Path(args.report_dir) / f"{date_str}.md"
    idea_path = Path(args.idea_dir) / f"{date_str}.json"
    project_dir = Path(args.project_dir) / date_str

    if not report_path.exists():
        raise FileNotFoundError(f"Report not found: {report_path}")

    report_text = report_path.read_text(encoding="utf-8")
    short_body = "\n".join(report_text.splitlines()[:80])

    msg = EmailMessage()
    msg["Subject"] = f"[Daily Bio+AI Report] {date_str}"
    msg["From"] = args.from_email
    msg["To"] = args.to_email
    msg.set_content(
        "每日自动报告（简要）如下，完整文件已附带（如启用附件）：\n\n"
        f"{short_body}\n\n"
        f"报告路径: {report_path}\n"
        f"Idea 路径: {idea_path}\n"
        f"Project 包路径: {project_dir}\n"
    )

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


if __name__ == "__main__":
    main()
