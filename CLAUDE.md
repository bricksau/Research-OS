# 工作入口（给 Claude Code 和其他 AI 助手）

这是一个实证研究项目（论文 / 学位论文），按 Research-OS 的规则运行。先读本页，再按任务只读需要的部分。

## 开始工作
1. 读 `STATUS.md`（一页：各项成果的现状和下一步）。只读和这次任务有关的文件夹，不要先通读各 README 和整份母本。
2. 找某句话在哪里：`python3 scripts/checks/claims_check.py --where "短语"`，不要逐个打开文件。
3. 工作流程（改母本、检查、记录、提交、同步、交接）用项目 skill `research-workflow`；写或改论文文字用 `academic-writing`（都在 `.claude/skills/`）。

## 三条铁律
- **数字只抄不算**：正文里的数字来自 `output/tables/` 的脚本输出，并登记在 `config/expected_numbers.yaml`；不心算、不手算。
- **引语和文献对照原文**：说不出出自哪个文件、第几页的，不写；不编造作者、年份、卷期、DOI。
- **唯一母本**：`papers/manuscript/` 里只有一份母本（`.docx` 或 `.md`）。Word 母本的 `.md` 镜像由脚本生成，不手改。

## 改完以后
`bash scripts/checks/check_all.sh`（几秒钟，每项一行）。不通过就不提交；不要为了通过去改检查脚本，要改的是母本、数据或 `config/` 里的预期值。

## 文件夹
| 文件夹 | 内容 |
|---|---|
| `papers/manuscript/` | 唯一母本（和生成的 `.md` 镜像） |
| `papers/review/` | 对照稿、审稿意见、每周日志 `Change_Log_YYYYMMDD.md` |
| `data/raw/` → `interim/` → `processed/` | 原始数据只读；清洗由 `src/` 的脚本完成 |
| `src/analysis/`、`src/r_scripts/` | Python 与 R 分析；所有数字都由这里生成 |
| `output/tables/`、`output/figures/` | 脚本输出，不手改 |
| `config/` | `expected_numbers.yaml`（数字溯源）、`claims_register.yaml`（核心主张）、`style_rules.yaml`（行文扫描） |
| `scripts/checks/` | 检查脚本和 `check_all.sh`；`scripts/sync/` 多电脑同步 |
| `baize/`、`rules/` | 去 AI 腔的写作提示词和防幻觉准则（可复制到任何 AI 工具） |
| `handoff/` | 交给另一个模型只读审查的任务单 |
| `advisor/` | 给导师的材料 |

## 规则
- `archive/`、`history/` 里的文件不作依据。每个文件夹的顶层只放现行文件。
- 一件任务（同一天、同一章的连续修改）做完提交一次：母本、`STATUS.md`、当周日志一起提交。
- 推送在一段工作结束或换电脑前做一次（`bash scripts/sync/sync.sh`）。
