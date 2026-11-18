# Research-OS: 通用实证与社科研究操作系统架构

## 1. 设计哲学 (Philosophy)
Research-OS 旨在解决社科与经济学实证研究中长期的“散乱痛点”：
- **数据与论文断联**：表格数字手工抄写，改了代码忘了改论文；
- **AI 幻觉滋生**：直接让 AI 写论文导致虚假文献、空洞修辞、伪造数据；
- **多端协作混乱**：云盘同步损坏 Git 仓库，不同电脑版本打架。

## 2. 五层分层架构 (5-Layer Architecture)
```text
┌──────────────────────────────────────────────────────────┐
│         Layer 5. Grounded Manuscript (唯一母本层)         │
│          papers/manuscript/ (Master.docx / Master.md)    │
└────────────────────────────┬─────────────────────────────┘
                             │ (数字严格绑定)
┌────────────────────────────▼─────────────────────────────┐
│      Layer 4. Publication Asset Factory (出版资产工厂)     │
│        output/tables/ (CSV), output/figures/ (300 DPI)   │
└────────────────────────────┬─────────────────────────────┘
                             │ (确定性脚本生成)
┌────────────────────────────▼─────────────────────────────┐
│     Layer 3. Indicator & SSOT Engine (指标与真实源引擎)    │
│        src/analysis/ (Python), src/r_scripts/ (R)        │
└────────────────────────────┬─────────────────────────────┘
                             │ (标准面板输入)
┌────────────────────────────▼─────────────────────────────┐
│       Layer 2. Data Harmonization (数据清洗与对齐)        │
│        data/raw/ → data/interim/ → data/processed/       │
└────────────────────────────┬─────────────────────────────┘
                             │ (外生真实数据)
┌────────────────────────────▼─────────────────────────────┐
│          Layer 1. Defense & Rules (防御规则与提示词)       │
│        rules/academic_grounding.md, baize/ (白泽引擎)     │
└──────────────────────────────────────────────────────────┘
```

## 3. 贯穿五层的检查（v2.1）
五层之间的“严格回溯”不靠自觉，靠 `scripts/checks/check_all.sh`：

| 连接 | 检查 | 登记处 |
|---|---|---|
| Layer 3/4 → Layer 5（数字进正文） | `src/analysis/verify_ssot.py`：从 CSV 重新取值、只四舍五入一次，再到正文查找 | `config/expected_numbers.yaml` |
| Layer 5 内部（同一主张处处一致） | `scripts/checks/claims_check.py`；`--where` 定位 | `config/claims_register.yaml` |
| Word 母本 → 可读文本 | `scripts/checks/docx_to_md.py` 生成 `.md` 镜像 | — |
| Layer 1 → Layer 5（行文） | `scripts/checks/style_scan.py`（只列候选，由人判断） | `config/style_rules.yaml` |

提交前钩子 `.githooks/pre-commit` 在母本、配置、输出表或脚本进入提交时自动运行只读检查。
