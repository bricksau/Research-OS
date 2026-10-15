# 白泽（Project BaiZe）—— 防御级去 AI 化学术方法提示词引擎
> **“白泽出，能人言，达于万物之情，以示天下，去邪精之伪。”** ——《抱朴子》

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Domain: Social Sciences & Economics](https://img.shields.io/badge/Domain-Empirical%20Economics%20%7C%20IPE-green.svg)](#)
[![Anti-AI: Defense-Grade](https://img.shields.io/badge/Anti--AI-Human%20Cadence-orange.svg)](#)

---

## 📖 项目愿景 (Philosophy)

在大语言模型（LLM）普及的时代，学术界充斥着由 AI 批量生成的浮夸大词、空洞因果、虚假文献与同质化句式。这导致大量论文在审稿人面前“一眼假”，因“缺乏真实学者质感与防御力”而被迅速退稿。

**「白泽」（Project BaiZe）** 是一套专为社科经贸、国际政治经济学（IPE）与实证研究者打造的**防御级去 AI 化科研方法提示词引擎**：
1. **辨伪去妄（Anti-AI Shield）**：彻底粉碎大模型的高频空洞词汇（crucial, profound, tapestry...），恢复学者真实思考的长短句呼吸感；
2. **微观穿透（Empirical Anchoring）**：拒绝宏观口号，将论点死死锚定在海关 6 位码、物量（吨/克重）、单价与实物供需的微观事实中；
3. **情境自律（Epistemic Modesty）**：分清会计事实描述（Accounting Description）与因果推论（Causal Inference），不强行把政策套成虚拟变量（Dummy）；
4. **防御写作（Pre-emptive Defense）**：在审稿人动手前，先一步将潜在的数据局限与制度盲区转化为学术深度的防辩装甲；
5. **模块插拔（Modular Style Adapters）**：既沉淀研究者不可磨灭的个人学术签名，又能随时按需加载指导教授、SSCI 顶刊或国家级智库的特定审阅风格；
6. **战略操盘（Empirical Orchestration）**：彻底打破文科/社科背景在面对代码算法时的本领恐慌，确立“学者定义业务与常识风控，AI 承担代码清洗与公式实现”的现代研究范式。

---

## 🏛️ 架构全景 (Architecture)

```text
baize/
├── README.md                          ← 本文件：哲学、指引与架构地图
├── system_prompt_baize_master.md      ← ★ 白泽总纲：可直接导入任意 AI 工具的核心母版提示词
│
├── docs/
│   └── empirical_orchestrator_manifesto.md ← ★【白泽·数据操盘手宣言】：文科博士的 AI 协同、黑盒审计与降维防御指南
│
├── rules/
│   └── anti_ai_shield.md              ← 【白泽·辟邪】：50+ 典型 AI 禁用词汇库与学者声调律令
│
├── profiles/
│   ├── zhuang_empirical_gvc.md        ← 【白泽·庄严】：庄全专属签名风格（量价穿透、微观海关、纯会计分层、操盘风控）
│   └── custom_profile_template.md     ← 个人风格定义模板（供他人克隆自己的学术签名）
│
├── adapters/                          ← 【白泽·通神】：他人/期刊风格扩展包
│   ├── advisor_pragmatic.md           ← 导师审阅风格（降调、口径统一、极度凝练）
│   ├── ssci_journal_editor.md         ← SSCI 国际经贸/应用经济学审稿人风格（识别边界、反事实透明）
│   ├── kci_area_studies.md            ← KCI 区域研究/政经历史风格（如《중소연구》实务范式）
│   └── thinktank_policy.md            ← 国家智库对策报告风格（聚焦去风险、落地建议）
│
└── examples/
    └── 01_before_after_demonstration.md ← 实战教学：从 AI 机械废话到白泽防御级正文的蜕变对比
```

---

## 🚀 快速上手 (Quick Start)

### 场景 A：在日常 AI 工具中使用（Claude Projects / Custom GPTs / Cursor / ChatGPT）
1. 打开 `baize/system_prompt_baize_master.md`；
2. 复制全文，粘贴进你的 **System Prompt** 或 **Custom Instructions**；
3. 你的 AI 助手即刻被赋予“白泽学术神格”。在撰写或润色时，输入：
   > “请使用白泽引擎，并加载 `[PROFILE: ZQRIOS]`，对以下段落进行量价分离与防御性学术改写：……”

### 场景 B：加载特定学术风格
如果你希望论文适应特定期刊或导师审阅习惯，只需在对话开头输入指令：
- `[LOAD_ADAPTER: Advisor_Pragmatic]` $\to$ 激活题目与结论降调、单口径化、极简摘要；
- `[LOAD_ADAPTER: SSCI_Journal_Editor]` $\to$ 激活因果边界声明与内生性防辩；
- `[LOAD_ADAPTER: ThinkTank_Policy]` $\to$ 激活以“精准去风险（Selective De-risking）”为导向的政策建言。

---

## 📜 开源许可 (License)

本项目采用 [MIT License](LICENSE) 开源。  
你可以自由分享、修改、将其作为个人研究体系的基石，或赠送给对你至关重要的学术同袍。唯一的要求是保留对求真知、拒虚饰之学术精神的敬畏。
