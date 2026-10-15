# 多电脑同步与协同指南 (Multi-Device Sync Guide)

本系统支持在 Mac、Windows 与平板电脑之间无缝协同。

## 1. 黄金分工原则
- **代码、脚本、表格、Markdown、配置**：走 GitHub（私有或个人仓库），使用 `scripts/sync/sync.sh`。
- **文献 PDF 原件（大文件/版权物）**：走 Google Drive、OneDrive 或本地坚果云等，不放进 GitHub 根目录。
- **重要提醒**：**绝对不要将包含 `.git` 文件夹的整个仓库直接丢进百度网盘/iCloud/OneDrive 同步盘根目录下**，云盘的后台文件锁会破坏 Git 的索引。

## 2. 日常同步操作
- **开始工作前**：运行同步脚本拉取其他电脑的更新；
- **结束工作后**：运行同步脚本自动提交并推送本机更新。
  - **Mac**：终端运行 `bash scripts/sync/sync.sh` 或双击 `scripts/sync/sync.command`；
  - **Windows**：双击 `scripts\sync\sync.cmd`。
