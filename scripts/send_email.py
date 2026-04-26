#!/usr/bin/env python3
"""Send latest report by email via SMTP."""

from __future__ import annotations

import argparse
import datetime as dt
import smtplib
from email.message import EmailMessage
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Send report via email")
    parser.add_argument("--report-dir", default="reports", help="Report directory")
    parser.add_argument("--date", default=None, help="Report date YYYY-MM-DD (default: today UTC)")
    parser.add_argument("--smtp-host", default="smtp.gmail.com")
    parser.add_argument("--smtp-port", type=int, default=587)
    parser.add_argument("--smtp-user", required=True)
    parser.add_argument("--smtp-pass", required=True)
    parser.add_argument("--from-email", required=True)
    parser.add_argument("--to-email", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    date_str = args.date or dt.datetime.utcnow().strftime("%Y-%m-%d")
    report_path = Path(args.report_dir) / f"{date_str}.md"

    if not report_path.exists():
        raise FileNotFoundError(f"Report not found: {report_path}")

    report_text = report_path.read_text(encoding="utf-8")

    msg = EmailMessage()
    msg["Subject"] = f"[Daily Bio+AI Report] {date_str}"
    msg["From"] = args.from_email
    msg["To"] = args.to_email
    msg.set_content(
        "每日自动报告已生成，正文如下：\n\n"
        f"{report_text}\n\n"
        f"(文件路径: {report_path})"
    )

    with smtplib.SMTP(args.smtp_host, args.smtp_port, timeout=30) as server:
        server.starttls()
        server.login(args.smtp_user, args.smtp_pass)
        server.send_message(msg)

    print(f"[OK] Email sent to {args.to_email} with report {report_path}")


if __name__ == "__main__":
    main()
