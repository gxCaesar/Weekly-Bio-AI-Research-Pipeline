# GitHub 每日科研自动化完整设置指南（中文）

## 入口在哪里（最快）

你有两个入口：

1. **GitHub 网页入口**：仓库 -> `Actions` -> `Daily Bio+AI Research Report` -> `Run workflow`。
2. **本地命令入口**：在仓库根目录执行 `make help`，再按提示执行 `make setup-secrets` / `make run-daily` / `make run-idea`。

---

本指南帮你把项目从 0 到 1 跑通：
1) 每天凌晨 2:00（北京时间）自动生成日报；
2) 自动生成强化 idea（实验设计 + 投稿匹配分）；
3) 自动发送到邮箱 `cgx510510@gmail.com`；
4) 自动把结果提交回仓库。

---

## 0. 如果你已泄露 App Password（先做这个）

1. 立刻打开 Google 账号安全设置 → App Passwords。
2. 删除（Revoke）已泄露的那个 App Password。
3. 重新创建一个新的 App Password。
4. 用新密码重新配置 `GMAIL_SMTP_PASS`。

---

## 0.5 安装 GitHub CLI（gh）

如果你本机没有 `gh`，先安装：

- macOS (Homebrew): `brew install gh`
- Windows (winget): `winget install --id GitHub.cli`
- Ubuntu/Debian: `sudo apt-get update && sudo apt-get install -y gh`

安装后检查：

```bash
gh --version
```

---

## 1. 准备前提

- 你拥有该 GitHub 仓库的写权限。
- 本地已安装并登录 GitHub CLI：
  ```bash
  gh --version
  gh auth login
  ```
- 你有一个 Gmail 邮箱用于发件，并已开启 2FA。

---

## 2. 创建 Gmail App Password（必须）

> `GMAIL_SMTP_PASS` 不是邮箱登录密码，必须使用 App Password（应用专用密码）。

步骤：
1. 打开 Google 账号安全设置（Security）。
2. 开启两步验证（2-Step Verification）。
3. 进入 App Passwords，创建一个用于 `Mail` 的密码。
4. 复制该 16 位密码，稍后用于 `GMAIL_SMTP_PASS`。

---

## 3. 配置仓库 Secrets（推荐一键脚本）

在仓库根目录执行（推荐交互模式，避免密码进历史记录）：

```bash
./scripts/setup_github_secrets.sh
```

或使用环境变量模式：

```bash
GMAIL_SMTP_USER='your@gmail.com' \
GMAIL_SMTP_PASS='your_16_digit_app_password' \
GMAIL_FROM_EMAIL='your@gmail.com' \
./scripts/setup_github_secrets.sh
```

成功后会看到：
`[OK] Secrets configured: GMAIL_SMTP_USER, GMAIL_SMTP_PASS, GMAIL_FROM_EMAIL`

---

## 4. 检查工作流是否启用

仓库中工作流文件：
- `.github/workflows/daily_research_report.yml`

关键行为：
- 每天 `02:00 Asia/Shanghai`（对应 UTC `18:00`）自动执行；
- 顺序执行：
  1) `scripts/daily_report.py`
  2) `scripts/strong_idea.py`
  3) `scripts/send_email.py`
  4) 提交 `reports/*.md` 和 `reports/ideas/*.json`

---

## 5. 第一次手动触发验证（强烈建议）

1. 打开仓库页面 → **Actions**。
2. 选择 **Daily Bio+AI Research Report**。
3. 点击 **Run workflow**。
4. 等待任务完成并检查：
   - 是否生成 `reports/YYYY-MM-DD.md`
   - 是否生成 `reports/ideas/YYYY-MM-DD.json`
   - 邮箱 `cgx510510@gmail.com` 是否收到邮件

---

## 6. 常见问题排查

### Q1: 没收到邮件
- 检查仓库 Secrets 是否完整。
- 检查 `GMAIL_SMTP_PASS` 是否为 App Password。
- 查看 Actions 日志中 `Send report email` 步骤。

### Q2: 工作流成功但报告内容为空
- 可能是运行环境网络限制导致 RSS 抓取失败。
- 先确认脚本仍能输出文件（这是正常降级行为）。
- 可后续增加备用数据源或代理。

### Q3: 脚本已运行但仓库没有新提交
- 如果当天文件内容未变化，工作流会跳过 commit（正常行为）。

---

## 7. 你现在可以做的两件事

1. 先执行第 3 步配置 Secrets；
2. 立即执行第 5 步手动触发验证一次。

这样就可以确保从今天开始每天自动运行。


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
