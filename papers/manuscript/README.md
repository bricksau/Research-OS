# papers/manuscript/ (唯一母本库)

- **唯一母本原则（Single Master Principle）**：保持论文正文只有一个主干文件（如 `Master.docx` 或 `Paper_Master.md`）。
- **杜绝版本分裂**：严禁出现 `论文_修改版_v2_最终定稿_导师又看.docx` 等命名。历史版本依靠 Git 提交记录管理。
- **Word 母本的镜像**：`scripts/checks/docx_to_md.py` 为每个 `.docx` 生成同名 `.md`（正文、标题、表格、脚注），检查脚本和 AI 助手读镜像；镜像不手改。
- **数字与核心句**：正文里的每个关键数字登记在 `config/expected_numbers.yaml`，核心主张登记在 `config/claims_register.yaml`。
