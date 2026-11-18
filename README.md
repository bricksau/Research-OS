# Research-OS: 通用实证与社科研究智能操作系统
> **A Defense-Grade, Question-Driven Research Intelligence Operating System (OS) for Empirical Economics & Social Sciences.**

[![GitHub Template](https://img.shields.io/badge/GitHub-Template%20Repository-blue.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python: >=3.11](https://img.shields.io/badge/Python->=3.11-brightgreen.svg)](#)
[![R: >=4.3](https://img.shields.io/badge/R->=4.3-blue.svg)](#)
[![Anti-AI: Defense-Grade](https://img.shields.io/badge/Anti--AI-Human%20Cadence-orange.svg)](baize/)

---

## 📖 项目愿景 (Philosophy)

在 AI 辅助科研时代，实证经济学、国际政治经济学（IPE）与社会科学研究者面临着前所未有的挑战：
1. **AI 幻觉泛滥**：大模型批量制造空洞词汇（crucial, profound, tapestry...）、虚假因果与虚构文献；
2. **数据与论文断联**：表格数字手工涂改抄写，代码改了论文没改，在答辩与匿名审稿中屡遭硬伤爆破；
3. **版本失控与多端摩擦**：网盘同步损坏 Git 仓库，不同电脑版本冲突；
4. **代码黑盒恐慌**：文科/社科学者面对清洗代码缺乏信心，无法做到对底层计算事实的 100% 穿透。

**Research-OS** 是一套开箱即用、经过顶刊与博士论文严苛实战检验的**开源科研基础设施与人机协同范式**。它将繁杂的“写论文”提升为工程化、可复现、具备顶级防御力的“研究操作系统”。

---

## 🏛️ 核心架构：五层体系 (5-Layer Architecture)

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   Layer 5. Grounded Manuscript Suite                   │
│                     唯一母本层 (Master.docx / .md)                      │
│             严禁版本分裂 · 数字 1:1 锚定 · 杜绝手工自由发挥               │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ (严格回溯)
┌───────────────────────────────────▼────────────────────────────────────┐
│                  Layer 4. Publication Asset Factory                    │
│                      出版资产工厂 (output/tables, figures)               │
│               自动化 CSV 表格 · 300 DPI 出版级高分辨率图表                │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ (确定性代码运行)
┌───────────────────────────────────▼────────────────────────────────────┐
│                 Layer 3. Indicator & SSOT Verification                 │
│                      指标计算与单一真理源引擎 (src/)                      │
│        拒绝口算/心算 · Python 逻辑核算 · R 计量统计 · MISMATCH = 0 闭环   │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ (数据流注入)
┌───────────────────────────────────▼────────────────────────────────────┐
│                    Layer 2. Data Harmonization                         │
│                      数据标准化与清洗层 (data/)                         │
│           data/raw/ (绝对只读) → interim/ → processed/ (标准面板)       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ (底层规则约束)
┌───────────────────────────────────▼────────────────────────────────────┐
│                  Layer 1. Defense & AI Rules Armor                     │
│                       防御级学术规则与白泽引擎                          │
│     rules/academic_grounding.md (防幻觉准则) · baize/ (去 AI 化提示词)  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🌟 核心功能特性 (Key Features)

### 1. 【白泽引擎】Project BaiZe: 防御级去 AI 化提示词引擎
- **内置 50+ 典型 AI 空洞大词熔断库**：彻底粉碎大模型的高频浮夸词汇，恢复学者长短句真实呼吸感；
- **微观制度穿透**：强制论述锚定在海关 6 位编码、实物量（吨/kg）、单价与微观供需事实；
- **即插即用风格适配器（Adapters）**：一键切换导师审阅风格、SSCI 审稿人视角、智库决策内参范式。
- 详见 [`baize/README.md`](baize/README.md)。

### 2. 【防幻觉求真铁律】Academic Grounding Rules
- **切断无据生成**：所有引述、数据必须来自本地文件；未提及的严禁脑补；
- **禁止心算/口算**：所有差额、增长率必须由 Python/R 脚本运行 stdout 输出，禁止模型概率猜测。
- 详见 [`rules/academic_grounding.md`](rules/academic_grounding.md)。

### 3. 【只读质检员机制】Multi-Model Read-Only Review
- 采用**“主笔（Author）- 质检员（Reviewer）- 自动化脚本（Auditor）”**三权分立机制，不绑定任何一家模型；
- 配套提供 `handoff/review_request_template.md`：审查方只读，只能跑 `check_all.sh --readonly`，报告按“位置 → 原文 → 问题 → 建议”写，收回后数字与引语一律用脚本比对再采用。

### 4. 【多电脑无痛同步】Multi-Device Git Sync
- 专为跨电脑（Mac 主力、Windows、轻薄平板）科研学者打造；
- 提供一键双击同步脚本：Mac 双击 `scripts/sync/sync.command`，Windows 双击 `scripts/sync/sync.cmd`；
- 智能捕获改动、自动防冲突保全，避免云盘同步导致 Git 损坏；每台电脑同步时自动启用提交前检查。

### 5. 【一键检查】Automated Checks (`scripts/checks/check_all.sh`)
每次改完母本、数据或分析脚本，几秒钟、每项一行：
- **SSOT 数字溯源**（`src/analysis/verify_ssot.py` + `config/expected_numbers.yaml`）：正文里的每个关键数字从 CSV 重新取值、按规则只四舍五入一次，再到正文里查找；不一致即 `MISMATCH`；
- **核心主张登记册**（`scripts/checks/claims_check.py` + `config/claims_register.yaml`）：假说、判定、定义在每一处说法一致，废止的说法不回流；`--where "短语"` 一条命令找到某句话的所有位置；
- **Word 母本镜像**（`scripts/checks/docx_to_md.py`）：`.docx` → 同名 `.md`（标题、正文、表格、脚注），让脚本和 AI 不打开 Word 也能读全文；
- **行文扫描**（`scripts/checks/style_scan.py` + `config/style_rules.yaml`）：列出 AI 套话、措辞强于证据（proves / led to）、机械列点、路标句、正文里交代修改经过等候选，逐条由人判断；
- **提交前钩子**（`.githooks/pre-commit`）：母本、配置、输出表或脚本进入提交时自动跑只读检查。

### 6. 【AI 助手原生入口】Claude Code / Agents Ready
- `CLAUDE.md`（入口页）+ `AGENTS.md`（给其他代理）+ `STATUS.md`（一页现状）：任何 AI 会话先读一页，而不是通读全仓库；
- `.claude/skills/research-workflow`（改母本、记录、提交、交接的流程）与 `.claude/skills/academic-writing`（证据强度对照表、论证结构、行文规则）；
- `.claude/agents/runner.md`：把跑检查、查位置这类机械活交给便宜的子代理。

---

## 📁 目录结构速览 (Directory Layout)

```text
Research-OS/
├── README.md                      ← 项目总览与工作指南（本文件）
├── LICENSE                        ← MIT 开源协议
├── pyproject.toml                 ← Python 项目依赖配置 (Python 3.11+)
├── bootstrap.py                   ← ★ 一键初始化：检查依赖、建目录与数据库、启用钩子、首次跑检查
├── CLAUDE.md / AGENTS.md          ← ★ AI 助手入口页（工作规则）
├── STATUS.md                      ← ★ 一页现状：各项成果的现状与下一步
├── .claude/                       ← Claude Code 项目 skills（研究流程、学术写作）与子代理
├── .githooks/pre-commit           ← 提交前自动跑只读检查
├── config/                        ← expected_numbers.yaml · claims_register.yaml · style_rules.yaml
│
├── baize/                         ← ★【白泽】去 AI 痕迹与学术风格提示词引擎
│   ├── system_prompt_baize_master.md  ← 白泽总纲：可直接导入任意 AI 系统的核心母版
│   ├── rules/anti_ai_shield.md        ← 50+ 禁用大词库与长短句节奏
│   ├── adapters/                      ← 期刊/导师/智库风格切换包
│   └── docs/empirical_orchestrator_manifesto.md ← 文科/社科学者的数据操盘手宣言
│
├── rules/                         ← 注入给 AI Agent 的行为准则
│   └── academic_grounding.md      ← 学术求真与防幻觉行为准则（开卷提取、禁止心算）
│
├── handoff/                       ← 交给另一个模型的只读审查任务单
│   └── review_request_template.md ← 只读审查模板（不绑定模型）
│
├── papers/                        ← 论文写作与审查中心
│   ├── manuscript/                ← ★ 唯一母本库（单母本原则）
│   ├── review/                    ← 审稿人意见、修改对照表与模拟审查报告
│   └── references_pdf/            ← 文献 PDF（本地或网盘管理，不入公共 Git）
│
├── data/                          ← SSOT 数据源
│   ├── raw/                       ← 原始数据（海关、年鉴、问卷，只读不可变）
│   ├── interim/                   ← 中间清洗结果
│   └── processed/                 ← 最终供回归/画图的标准面板数据
│
├── src/                           ← 确定性计算与可视化代码
│   ├── analysis/                  ← Python 实证与 SSOT 核对（verify_ssot.py、example_table.py）
│   └── r_scripts/                 ← R 语言 300 DPI 出版级图表脚本与计量分析
│
├── output/                        ← 脚本自动生成的纯净产出物（严禁手动修改）
│   ├── tables/                    ← 导出的 CSV / Excel 数据表
│   └── figures/                   ← 导出的 300 DPI 高清学术图表
│
├── advisor/                       ← 导师面谈一页纸清单、答辩图表集与评委材料
├── docs/                          ← 架构设计文档与三台电脑同步说明
└── scripts/                       ← checks/（一键检查、镜像、行文扫描）· sync/（多机同步）
```

---

## 🚀 快速上手 (Quick Start)

### 步骤 1：基于本模板创建您的新课题仓库
点击 GitHub 页面右上角的绿色按钮 **「Use this template」** → **「Create a new repository」**，输入您的专属课题名称（如 `China-EV-Trade-OS`）。

### 步骤 2：克隆并初始化本地环境
```bash
# 1. 克隆您自己的课题仓库
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# 2. 安装依赖并初始化（检查依赖、建目录与数据库、启用提交前钩子、首次运行检查）
pip install pyyaml python-docx pandas pytest
python3 bootstrap.py
```
首次运行时，检查跑的是仓库自带的合成示例（`data/raw/example/` → `output/tables/example_trade_balance.csv` → 母本第 4 节的一句话）。换成自己的数据后，把示例数据、示例脚本、示例句和 `config/` 里标着 example 的条目一起删掉。

### 步骤 3：在日常研究中使用
1. **与 AI 协作**：用 Claude Code 时直接在仓库里开会话，它会读 `CLAUDE.md` 和 `.claude/skills/`；用网页版 AI 工具（Claude Projects / Custom GPT / Cursor）时，把 `baize/system_prompt_baize_master.md` 或 `rules/academic_grounding.md` 设为 **System Prompt**；
2. **放入数据与代码**：将原始数据放入 `data/raw/`，在 `src/` 中编写可复现的清洗与计算脚本，结果写进 `output/tables/`；
3. **写进正文的数字**：先登记到 `config/expected_numbers.yaml`，再写进母本；改完运行 `bash scripts/checks/check_all.sh`；
4. **记录**：一件任务做完更新一次 `STATUS.md`（只写现状和下一步），经过写进 `papers/review/Change_Log_<周>.md`；
5. **完成阶段性产出后**：用 `handoff/review_request_template.md` 交给另一个模型做只读质检，收回的报告用脚本核对后再采用；
6. **跨设备同步**：在终端运行 `bash scripts/sync/sync.sh`（或在桌面上双击 `sync.command` / `sync.cmd`），1 秒完成多电脑无冲突备份。

---

## 🗒️ 更新记录 (Changelog)

### v2.1（2026-11）：从一篇真实博士论文里回收的经验
- **新增一键检查**：`scripts/checks/check_all.sh`、可用的 SSOT 核对（`verify_ssot.py` + `expected_numbers.yaml`，取代只会打印“通过”的旧模板）、核心主张登记册与 `--where` 定位、Word 母本镜像、行文扫描、提交前钩子；
- **新增 AI 助手入口**：`CLAUDE.md`、`AGENTS.md`、`STATUS.md`、两个 Claude Code skill、一个子代理；
- **审查不再绑定 Codex**：`handoff/review_request_template.md` 适用于任何模型或读者；
- **修正**：`src/core/paths.py` 改为以仓库为根（原来依赖当前目录）；`bootstrap.py` 不再内嵌第二份源码（两份副本会互相漂移）；文档中未渲染的 `$\to$` 改为 →；`sync.sh` 改为带 `--autostash` 的 rebase；
- **新增测试**：`tests/`（`pytest`）。

---

## 📜 开源协议 (License)

本项目采用 [MIT License](LICENSE) 开源。  
您可以自由地将本架构用于博士论文、学术期刊发表或智库咨询报告中。  
如果本架构对您的学术旅程有所启发，欢迎在 GitHub 上点亮一颗 ⭐️ Star！
