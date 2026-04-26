.PHONY: help setup-secrets run-daily run-idea run-email

help:
	@echo "Available commands:"
	@echo "  make setup-secrets   # 交互配置 GitHub Secrets"
	@echo "  make run-daily       # 生成当日日报"
	@echo "  make run-idea        # 生成强化 idea 模块"
	@echo "  make run-email       # 发送当日报告到邮箱（需本地环境变量）"

setup-secrets:
	./scripts/setup_github_secrets.sh

run-daily:
	python3 scripts/daily_report.py

run-idea:
	python3 scripts/strong_idea.py

run-email:
	python3 scripts/send_email.py \
	  --smtp-user "$$GMAIL_SMTP_USER" \
	  --smtp-pass "$$GMAIL_SMTP_PASS" \
	  --from-email "$$GMAIL_FROM_EMAIL" \
	  --to-email "cgx510510@gmail.com"
