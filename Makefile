.PHONY: help setup-secrets run-daily run-idea run-email deploy-skills run-preexp run-preexp-config preexp-codespace

help:
	@echo "Available commands:"
	@echo "  make setup-secrets   # 交互配置 GitHub Secrets"
	@echo "  make run-daily       # 生成当日日报"
	@echo "  make run-idea        # 生成强化 idea 模块"
	@echo "  make run-email       # 发送当日报告到邮箱（需本地环境变量）"
	@echo "  make deploy-skills   # 解压并部署 9 个科研 skill"
	@echo "  make run-preexp      # 生成实验前自动化流程脚手架"
	@echo "  make run-preexp-config # 基于 YAML 配置生成流程"
	@echo "  make preexp-codespace # Codespaces: 先部署再生成流程"

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

deploy-skills:
	bash ./scripts/deploy_research_skills.sh

run-preexp:
	bash ./scripts/run_pre_experiment_pipeline.sh

run-preexp-config:
	bash ./scripts/run_pre_experiment_pipeline.sh --config workflows/pre_experiment_config.example.yaml

preexp-codespace:
	bash ./scripts/deploy_research_skills.sh
	bash ./scripts/run_pre_experiment_pipeline.sh --config workflows/pre_experiment_config.example.yaml
