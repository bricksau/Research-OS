---
name: research-workflow
description: >-
  Working routine for a Research-OS project (an empirical paper or dissertation with one master manuscript, data
  and analysis scripts): how to start a session, read only what is needed, change the master, run the checks
  (check_all.sh, expected_numbers.yaml, claims_register.yaml), record work (STATUS.md, weekly change log, commits),
  sync between computers, hand work to another model for read-only review and check what comes back, and choose
  the model. Use it at the start of every session in the repository and whenever you are about to change the
  master, commit, update STATUS or the log, sync, write a handoff or check a reviewer's report. Wording rules are
  in academic-writing; use both when writing into the master.
---

# 研究工作流程

目的：把额度和注意力花在研究本身，不花在重复的读取、记录、对齐和交接上。下面每条规则都来自一篇真实博士论文的开销（一个月 200 多次提交里，现状页改了 100 多次、十几次提交只为记一个小决定）。

## 一、开工
1. 读 `STATUS.md`（一页），只读和任务有关的文件夹；长母本只读相关的节，不通读。
2. 找一句话在哪：`python3 scripts/checks/claims_check.py --where "短语"`。
3. 改 Word 母本之前先看 `git status --short`：母本若有作者未提交的保存，先比对、单独提交这份保存，再在它上面改。

## 二、改母本
- 母本只有一份（`papers/manuscript/`）。Word 母本只改文字，不动格式；`.md` 镜像由 `scripts/checks/docx_to_md.py` 生成，不手改。
- 措辞要作者定的地方，先写对照稿（`papers/review/Draft_<主题>_<日期>.md`，改前 / 改后 / 理由），作者同意后再写入。
- 改到核心主张（假说、判定、定义、废止用语）：先改 `config/claims_register.yaml`，再在同一次修改里改它列出的每一处。
- 新数字：先由脚本写进 `output/tables/`，再登记到 `config/expected_numbers.yaml`，最后写进正文。
- 改完运行 `bash scripts/checks/check_all.sh`。不通过时改母本、数据或预期值，**不改检查脚本**。

## 三、记录、提交、同步
- **一件任务做完提交一次**：母本、`STATUS.md`、当周日志在同一次提交里。中间步骤不单独提交，除非要交给别的会话或模型。
- **STATUS 只写现状和下一步**，每格不超过两行；经过写进 `papers/review/Change_Log_<周一日期>.md`（模板 `Change_Log_TEMPLATE.md`）。
- **作者的小决定攒着记**：讨论中定下的事先记在对照稿的“待定事项”里，一轮讨论结束后统一写入、提交一次。
- 提交前钩子（`.githooks/pre-commit`）会跑只读检查；`sync.sh` 提交时只警告不拒绝，保证保存总能备份。
- **推送**：一段工作结束或换电脑前运行一次 `bash scripts/sync/sync.sh`，不必每次提交都推。

## 四、会话和分支
- “一件事”= 同一天、同一章（或同一篇论文）的连续修改，在同一个会话、同一个分支里做完。不要把每一步拆成新会话：每个新会话都要重新读一遍，最后还要合并。
- **同一时间只让一个分支改 Word 母本**：docx 是二进制，两个分支都改只能手工合并。其他并行会话只出报告或对照稿。
- 换到不相关的任务（另一篇论文、给导师的材料）才开新会话。

## 五、交给另一个模型审查
- 用 `handoff/review_request_template.md`，审查方只读，只能跑 `check_all.sh --readonly`。
- 收回的报告是线索，不是结论：报告里的数字、引语、页码一律用脚本或原文比对后再采用；改动由主笔写入。
- 论证层面的修改，在对照稿末尾写“自查”（证据强度、和登记册是否一致、有没有新数字未登记）后再写入。

## 六、模型和分工
- 写正文、对照稿、判断审稿意见：主模型。
- 跑检查、查位置、数词频、更新日志、同步：便宜的子代理（`.claude/agents/runner.md`）。
- 数字和引语的比对交给脚本，不交给模型的记忆。
