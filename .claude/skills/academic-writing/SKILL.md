---
name: academic-writing
description: >-
  Writing and revision rules for the manuscript of a Research-OS project (empirical economics, IPE, social
  science papers and dissertations, in English, Korean or Chinese). Use it whenever you draft, revise, review or
  tighten text for the master, an abstract, a literature review, hypotheses, results, conclusions or limitations,
  a journal submission or a report for an advisor; for requests like "改一下这段", "帮我润色", "检查写作",
  "reviewer comments"; and whenever you decide how strongly to word a finding. Use it even for a single sentence:
  most rules here exist because a single sentence once went wrong.
---

# 学术写作规范

目标：文字达到正常期刊论文和博士论文的标准，措辞不比证据强，读起来像研究者写的。去 AI 腔的词表和风格包在 `baize/`。

## 一、措辞和证据的强度
**最容易被审稿人抓住的，是措辞比证据强。** 写每个结论句前先问：证据支持到哪一层？然后用那一层的词。

| 证据 | 可以写 | 不要写 |
|---|---|---|
| 理论预期 | is expected to, is likely to, should | will, must |
| 检验通过（条件关联） | is supported by the data, is associated with, moved with | proves, demonstrates that X caused Y |
| 方向一致但不显著 | is consistent in direction but not significant | is supported / is not supported |
| 方向相反或被否证 | is not supported | is rejected outright（样本很小时） |
| 只有描述 | coincided with, preceded, followed | led to, drove, resulted in |
| 解释，未检验 | can be read as, is plausible | the mechanism shows |

- 不同假说的判定分开写，不合并成“都没被支持”。判定以结果表和 `config/claims_register.yaml` 为准。
- 题目和研究问题可以用 "effect"，但第 1 章就要说明检验的是条件关联还是因果识别。
- 代理变量没测到的，不外推：否定结果只否定“这种测量下的预测”。背景事实（如建厂周期）只说明“可能”，不是测量。

## 二、论证的结构
- 每一部分只做它该做的事：综述介绍理论，框架只组合综述过的理论；结果章报告，结论章解释。
- 理论为假说服务：推不出假说、也不用于测量或解释的理论，删掉或降到脚注。
- 限制写一次、写完整（方法章），结论处总结，别处一句带过。
- 一个事实或数字只在第一次需要的地方写全，别处指回；结论不出现前文没有的结论和数字。
- 正文不写修改经过和研究过程（“看了数据以后”“事后改动”“按导师意见”），不写表态句。

## 三、行文
- 写连贯的段落，不用 First/Second 式机械列点和正文 bullet；不凑三点，不写段尾总结句和路标句（“本节将讨论……”）。
- 先写主语和动作，一句一个主要论点；测得的结果和对它的解释分句写。
- 术语一次定义，此后不换说法；废止的说法登记在 `claims_register.yaml` 的 `stale` 里。

## 四、事实、数字、引文
- 数字从 `output/tables/` 照抄并登记到 `config/expected_numbers.yaml`，只四舍五入一次；找不到现成输出就说没有。
- 引语逐字复制并对照原文；查不到原句时不加引号。
- 只引核对过原文的说法；网页来源写 URL 和真实访问日期；不确定的条目标“需要人工核实”。

## 五、交稿前自查
1. `python3 scripts/checks/style_scan.py <母本或镜像.md> [--section 4]`，逐条看（只是候选，判断由你做）。
2. 对照第一节检查每个结论句的强度。
3. 运行 `bash scripts/checks/check_all.sh`。
4. 向作者报告：改了什么、为什么；哪些改动落在作者自己写的句子上；还有哪些没核实。
