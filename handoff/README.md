# handoff/（交给另一个模型或读者的只读审查）

建议把 AI 协同分成三个相互制衡的角色：
1. **主笔（Author）**：在本仓库里写正文和分析脚本的人或 AI 会话（如 Claude Code），唯一有权改母本；
2. **只读审查者（Reviewer）**：任何第二模型或第二位读者，用 `review_request_template.md` 盲审、交叉质检，**不改任何文件**，只运行 `scripts/checks/check_all.sh --readonly`；
3. **验证脚本（Auditor）**：`scripts/checks/check_all.sh`，数字、核心主张和镜像一致性靠脚本，不靠任何一方的记忆。

收回的报告存到 `papers/review/Review_YYYYMMDD_<来源>.md`。报告里的数字和引语先用脚本比对再采用。
