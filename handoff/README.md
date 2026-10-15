# handoff/ (会话交接与多模型协同)

在严谨的实证研究中，建议将 AI 协同流程划分为三个相互制衡的角色：
1. **主笔/编写者（Author / Writer）**：使用 Claude / Cursor / 本地环境撰写正文或分析脚本；
2. **只读审查者（Read-only Reviewer）**：使用 OpenAI Codex / ChatGPT / 独立 AI，执行盲审与交叉质检，**严禁修改任何文件**；
3. **验证脚本（Automated Auditor）**：Python / R 脚本运行 SSOT 闭环检查，杜绝心算。

每次将阶段性研究成果交由审查模型质检时，请复用 `codex_review_template.md`，并将审查结论留存交接记录。
