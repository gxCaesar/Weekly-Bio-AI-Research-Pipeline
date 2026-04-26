# Weekly-Bio-AI-Research-Pipeline

## Cloud daily execution (每天云端自动执行)

## 入口（你要点哪里）

### 入口 A：网页上运行（推荐）
1. 打开你的 GitHub 仓库页面。  
2. 点顶部 **Actions**。  
3. 选择 **Daily Bio+AI Research Report**。  
4. 点 **Run workflow**。

### 入口 B：本地命令行运行（最直接）
在仓库根目录执行：
```bash
make help
make setup-secrets
make run-daily
make run-idea
make test
```


这个仓库已经支持在云端（GitHub Actions）每天自动执行，默认在 **北京时间凌晨 2:00** 生成一份日报，并自动推送到 `cgx510510@gmail.com`。

### 已实现内容
- 自动从 `config/sources.json` 中读取 AI 和 Bio RSS 源。
- 运行 `scripts/daily_report.py` 生成 `reports/YYYY-MM-DD.md`。
- 运行 `scripts/strong_idea.py` 追加“强化 Idea 模块（实验设计 + 投稿匹配分）”，并输出结构化文件 `reports/ideas/YYYY-MM-DD.json`。
- 运行 `scripts/send_email.py` 自动发邮件到指定收件箱。
- GitHub Actions 自动提交当天报告与结构化 idea 文件到仓库。

### 关键文件
- 工作流：`.github/workflows/daily_research_report.yml`
- 数据源配置：`config/sources.json`
- 报告生成脚本：`scripts/daily_report.py`
- 强化 idea 脚本：`scripts/strong_idea.py`
- 邮件发送脚本：`scripts/send_email.py`
- Secrets 一键配置脚本：`scripts/setup_github_secrets.sh`
- 输出目录：`reports/`
- `Makefile`（统一入口命令，含 `make test`）

### 必要 Secrets（GitHub 仓库 Settings → Secrets and variables → Actions）
- `GMAIL_SMTP_USER`: Gmail 登录账号（通常同发件邮箱）
- `GMAIL_SMTP_PASS`: Gmail App Password（不是邮箱登录密码）
- `GMAIL_FROM_EMAIL`: 发件人邮箱地址

> 如果 Secrets 未配置，工作流会跳过发信步骤，但仍会生成并提交日报。

### 一键配置 GitHub Secrets（推荐）
先在本地登录 GitHub CLI：
```bash
gh auth login
```
然后执行：
```bash
GMAIL_SMTP_USER='your@gmail.com' \
GMAIL_SMTP_PASS='your_app_password' \
GMAIL_FROM_EMAIL='your@gmail.com' \
./scripts/setup_github_secrets.sh
```

### 手动触发
1. 进入 GitHub 仓库的 **Actions**。
2. 选择 **Daily Bio+AI Research Report**。
3. 点击 **Run workflow** 可立即生成当天报告并尝试发送邮件。

### 本地调试
```bash
python scripts/daily_report.py --date 2026-04-26 --max-items 5
python scripts/strong_idea.py --date 2026-04-26
python scripts/send_email.py \
  --date 2026-04-26 \
  --smtp-user "$GMAIL_SMTP_USER" \
  --smtp-pass "$GMAIL_SMTP_PASS" \
  --from-email "$GMAIL_FROM_EMAIL" \
  --to-email "cgx510510@gmail.com"
```

## Proposal
- 每日自动化科研调研方案：`daily_2am_research_automation_plan.md`


## 快速上手
- 完整设置指南：`SETUP_GUIDE_ZH.md`


### `GMAIL_SMTP_PASS` 是什么？
- 不是你的邮箱登录密码。
- 它是 Gmail 的 **App Password（应用专用密码）**，通常是 16 位字符。
- 你需要先开启 Google 账号两步验证（2FA），然后在 Google 账号安全设置里创建 App Password。


### 安全提醒（非常重要）
- **不要**在聊天、issue、代码、截图里暴露 `GMAIL_SMTP_PASS`。
- 如果你已经泄露过 App Password，请立刻在 Google 账号里 **撤销并重建**。
- 推荐使用 `./scripts/setup_github_secrets.sh` 的交互模式输入密码，避免写入 shell history。


### 安装 gh（如果未安装）
- macOS: `brew install gh`
- Windows: `winget install --id GitHub.cli`
- Ubuntu/Debian: `sudo apt-get update && sudo apt-get install -y gh`


### 交互输入示例
执行：
```bash
./scripts/setup_github_secrets.sh
```
你会依次看到提示：
- `GMAIL_SMTP_USER (e.g. your@gmail.com):`
- `GMAIL_FROM_EMAIL (usually same as SMTP user):`
- `GMAIL_SMTP_PASS (Gmail App Password):`（这一行是隐藏输入，不会回显）

输入完成后按回车，看到 `[OK] Secrets configured...` 就表示成功。


### Secrets 设置报错（403 Resource not accessible by integration）
- 说明当前 `gh` 身份没有仓库 Secrets 管理权限（常见于 GitHub App/CI token）。
- 先执行 `gh auth login` 切到个人账号。
- 再用仓库参数重试：`GH_REPO=gxCaesar/Weekly-Bio-AI-Research-Pipeline ./scripts/setup_github_secrets.sh`
- 如果仍失败，请用 PAT（classic）并至少包含 `repo` scope。

- 如果你在 Codespaces/CI 里看到提示 `The value of the GITHUB_TOKEN environment variable is being used for authentication`，先执行：
  ```bash
  unset GITHUB_TOKEN GH_TOKEN
  gh auth logout -h github.com -u || true
  gh auth login
  ```
  然后再执行：
  ```bash
  GH_REPO=gxCaesar/Weekly-Bio-AI-Research-Pipeline ./scripts/setup_github_secrets.sh
  ```



## Secrets 配置成功后（下一步）

1. 在 GitHub 页面进入 **Actions**。  
2. 打开 **Daily Bio+AI Research Report**。  
3. 点击 **Run workflow** 先手动跑一次。  
4. 运行完成后检查：
   - `reports/YYYY-MM-DD.md` 是否生成；
   - `reports/ideas/YYYY-MM-DD.json` 是否生成；
   - `cgx510510@gmail.com` 是否收到邮件；
   - Actions 日志里 `Send report email` 步骤是否成功。
5. 若手动运行成功，就等待定时任务（每天北京时间 02:00）自动执行。
