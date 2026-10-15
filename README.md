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

### 3. 【只读质检员机制】Codex / Multi-Agent Read-Only Handoff
- 采用**“主笔（Author）- 质检员（Reviewer）- 自动化脚本（Auditor）”**三权分立机制；
- 配套提供 `handoff/codex_review_template.md`，使外部 AI 专注检查代码理论一致性与刁钻答辩追问，严禁乱动代码文件。

### 4. 【多电脑无痛同步】Multi-Device Git Sync
- 专为跨电脑（Mac 主力、Windows、轻薄平板）科研学者打造；
- 提供一键双击同步脚本：Mac 双击 `scripts/sync/sync.command`，Windows 双击 `scripts/sync/sync.cmd`；
- 智能捕获改动、自动防冲突保全，避免云盘同步导致 Git 损坏。

---

## 📁 目录结构速览 (Directory Layout)

```text
Research-OS/
├── README.md                      ← 项目总览与工作指南（本文件）
├── LICENSE                        ← MIT 开源协议
├── pyproject.toml                 ← Python 项目依赖配置 (Python 3.11+)
├── bootstrap.py                   ← ★ 一键环境初始化与数据库生成脚本
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
├── handoff/                       ← 与 Codex/Claude 协同的交接任务单
│   └── codex_review_template.md   ← 外部只读质检员审查模板
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
│   ├── analysis/                  ← Python 实证、统计核验、SSOT 一致性审计
│   └── r_scripts/                 ← R 语言 300 DPI 出版级图表脚本与计量分析
│
├── output/                        ← 脚本自动生成的纯净产出物（严禁手动修改）
│   ├── tables/                    ← 导出的 CSV / Excel 数据表
│   └── figures/                   ← 导出的 300 DPI 高清学术图表
│
├── advisor/                       ← 导师面谈一页纸清单、答辩图表集与评委材料
├── docs/                          ← 架构设计文档与三台电脑同步说明
└── scripts/                       ← 自动化工具集（多机同步、环境自检）
```

---

## 🚀 快速上手 (Quick Start)

### 步骤 1：基于本模板创建您的新课题仓库
点击 GitHub 页面右上角的绿色按钮 **「Use this template」** $	o$ **「Create a new repository」**，输入您的专属课题名称（如 `China-EV-Trade-OS`）。

### 步骤 2：克隆并初始化本地环境
```bash
# 1. 克隆您自己的课题仓库
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# 2. 运行初始化脚本 (自动检测目录、写入配置、初始化本地 SQLite 数据库)
python3 bootstrap.py
```

### 步骤 3：在日常研究中使用
1. **与 AI 对话前**：将 `baize/system_prompt_baize_master.md` 或 `rules/academic_grounding.md` 复制为您的 AI 工具（Claude Projects / Custom GPT / Cursor / VS Code）的 **System Prompt**；
2. **放入数据与代码**：将原始数据放入 `data/raw/`，在 `src/` 中编写可复现的清洗与计算脚本；
3. **完成阶段性产出后**：将正文片段与数据表丢给 Codex，附带 `handoff/codex_review_template.md` 进行苛刻的只读质检；
4. **跨设备同步**：在终端运行 `bash scripts/sync/sync.sh`（或在桌面上双击 `sync.command` / `sync.cmd`），1 秒完成多电脑无冲突备份。

---

## 📜 开源协议 (License)

本项目采用 [MIT License](LICENSE) 开源。  
您可以自由地将本架构用于博士论文、学术期刊发表或智库咨询报告中。  
如果本架构对您的学术旅程有所启发，欢迎在 GitHub 上点亮一颗 ⭐️ Star！
