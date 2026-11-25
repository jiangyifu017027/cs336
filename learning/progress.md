# 我的 CS336 学习进度

> 本文件记录“人学到了什么”；环境和数据状态见根目录 `STATUS.md`。

## 学习偏好

- 主要语言：简体中文。
- 英语水平：CET-4 左右；技术术语保留英文，复杂原文配合中文解释。
- 辅导方式：直觉和例子优先，再进入公式、shape 和实现；**默认纯讲解，不主动出检查题、不问回忆题、不要求复述**；只有用户主动要求出题、复习或诊断时才进入问答（2026-11-23 起）。
- 内容忠实度：严格按课程讲义（`lecture_NN.py` / PDF）的顺序与内容讲解，不超前引入后续讲次概念；助教补充用【补充】标注（2026-11-22 用户明确要求，已写入 cs336-study skill）。
- 掌握度：由用户自评，并在写作业过程中自我验证；AI 只负责讲清知识、维护 `learning/knowledge-map.md` 的“已讲解”标记。
- 每周可学习时间（2026-11-22 确认）：工作日 30 min/天，周末 4 h/天，约 10.5 h/周。
- 学习速度：偏慢（自述）；基础：AI 专业本科二年级，有简单 ML/DL 基础（自述）。
- Python / PyTorch / 数学起点：已于 2026-11-23 完成诊断，三项均需从基础补起，详见下方记录。
- **总体学习计划：见 `learning/plan.md`**（2026-11-25 重构为轻量版，原完整路线不再保留）：主线 L01–L03 + A1 完整做；L05/L07/L09/L10/L13/L15–L17 降为概念级纯讲解；L04/L06/L08/L11/L12/L14 与 A2/A4/A5 实现不在计划内；A3 可选轻量版。

## 当前位置

- **阶段**：P1 / A1 Basics（进行中）。
- **当前主题**：A1 handout §2.1–2.2 — Unicode 码点、`repr` / `print`、UTF 编码与多字节字符；巩固 L01-5、L01-6，掌握度待用户自评。
- **当前作业**：A1 尚未开始实现；tokenizer 部分的 7 个 Problem 已读题，unicode1、unicode2 共六个小问待用户独立作答。
- **环境**：WSL2 的 A1 环境及数据已于 2026-11-21 验证可用；当前 Mac 副本待用户复查。这不表示课程任务已完成。
- **下一次最小动作**：在 Python 解释器中运行 handout §2.1 已给出的表达式并比较 §2.2 的编码结果，独立写出六个小问的简短草稿，可交给 AI review。
- **建议命令**：遵守作业仓库规则，由用户自行运行解释器实验；AI 不代为执行。

## 学前诊断（2026-11-23 完成）

方式：对话自评 + 3 个微检查（`setdefault` 输出、broadcasting shape、矩阵乘法 shape），用户对全部三组回答“都不会”。

- [x] Python：不能独立写带类型标注的函数/类；不知 `dict.setdefault` 行为 → 接近零基础。读 starter 代码时需逐行讲解。
- [x] PyTorch：未写过训练循环；broadcasting 不会 → 零基础。L02 是重点，需放慢。
- [x] 数学：矩阵乘法 shape、softmax、交叉熵均不会 → 零基础。用到时以【补充】即时补，不单独开数学课。
- [x] 学习投入：10.5 h/周（2026-11-22 已确认）；A1 目标完成时长未设定。

校准结论：三项起点均低于 plan.md 的预设下限，但课程本身覆盖 PyTorch（L02）和所需数学；按 plan.md 风险规则，真实速度以 P1 前两周数据为准再校准，暂不重排计划。

## 讲次进度

状态含义：`未开始` → `学习中` → `已初学，待复习` → `已掌握`。掌握状态由用户自评 + 作业证据决定（2026-11-23 起不再靠课堂提问判定）；逐条知识点的勾选见 `learning/knowledge-map.md`。

| 讲次 | 主题 | 状态 | 掌握证据 / 遗留问题 |
|---|---|---|---|
| 01 | Overview, tokenization | 学习中 | L01-4～9 已讲解；2026-11-23 BPE 训练与使用采用纯讲解，掌握度待自评；L01-1～3 未讲 |
| 02 | PyTorch, resource accounting | 未开始 | |
| 03 | Architectures, hyperparameters | 未开始 | |
| 04 | Mixture of experts | 未开始 | |
| 05 | GPUs | 未开始 | |
| 06 | Kernels, Triton | 未开始 | |
| 07 | Parallelism basics | 未开始 | |
| 08 | Parallelism | 未开始 | |
| 09 | Scaling laws basics | 未开始 | |
| 10 | Inference | 未开始 | |
| 11 | Scaling laws details | 未开始 | |
| 12 | Evaluation | 未开始 | |
| 13 | Data | 未开始 | |
| 14 | Data filtering & dedup | 未开始 | |
| 15 | Alignment: SFT / RLHF | 未开始 | |
| 16 | Alignment: RL | 未开始 | |
| 17 | Reasoning RL mechanics | 未开始 | |

## 作业进度

| 作业 | 状态 | 当前证据 / 下一步 |
|---|---|---|
| A1 Basics | 读题 | WSL2 环境和 TinyStories/OWT 数据已就绪，Mac 待复查；tokenizer 部分题意卡及 Unicode 前置概念已整理；下一步由用户独立完成 unicode1/unicode2 六个小问 |
| A2 Systems | 不在计划内 | 仅 L05/L07 概念级覆盖 |
| A3 Scaling | 可选轻量版 | 主线走完后由用户决定；只做本地小实验，注意非学生 API 与数据限制 |
| A4 Data | 不在计划内 | 仅 L13 概念级覆盖 |
| A5 Alignment | 不在计划内 | 仅 L15–L17 概念级覆盖；以后若想补做，大模型训练优先考虑云 GPU |

## 最近会话

- [2026-11-23 A1 handout：Unicode 书面题前置概念](sessions/2026-11-23-a1-unicode-concepts.md)：巩固 L01-5/6；未给答案、未出检查题，六个小问待用户独立完成。
- [2026-11-23 A1 handout：tokenizer 题意卡](sessions/2026-11-23-a1-handout-tokenizer.md)：Section 2 共 7 题 42 分的要求与字面规则整理；未出检查题。
- [2026-11-23 L01：BPE 训练与使用](sessions/2026-11-23-lecture01-bpe.md)：完成 L01-9 纯讲解；未出检查题，掌握度待用户自评。
- [2026-11-23 L01：character / word tokenization 与 BPE 动机](sessions/2026-11-23-lecture01-char-word.md)：回忆题与共同弱点答对；迁移题、复述均跳过。
- [2026-11-23 L01：token 与 byte](sessions/2026-11-23-lecture01-token-byte.md)：3 道检查题全对（含理由补充），复述跳过。
