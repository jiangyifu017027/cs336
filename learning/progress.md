# 我的 CS336 学习进度

> 本文件记录“人学到了什么”；环境和数据状态见根目录 `STATUS.md`。

## 学习偏好

- 主要语言：简体中文。
- 英语水平：CET-4 左右；技术术语保留英文，复杂原文配合中文解释。
- 辅导方式：直觉和例子优先，再进入公式、shape 和实现；**默认纯讲解，不通过提问检查理解**（2026-11-23 起）。
- 内容忠实度：严格按课程讲义（`lecture_NN.py` / PDF）的顺序与内容讲解，不超前引入后续讲次概念；助教补充用【补充】标注（2026-11-22 用户明确要求，已写入 cs336-study skill）。
- **交互方式（2026-11-23 用户明确要求）**：以**纯讲解**为主，不主动出检查题、不问回忆题、不要求复述。掌握度由用户自己判断，并在写作业过程中自我验证；AI 只负责把知识讲清楚、按 `learning/knowledge-map.md` 分类组织，方便用户记录掌握情况。用户主动要求出题时除外。
- 每周可学习时间（2026-11-22 确认）：工作日 30 min/天，周末 4 h/天，约 10.5 h/周。
- 学习速度：偏慢（自述）；基础：AI 专业本科二年级，有简单 ML/DL 基础（自述）。
- Python / PyTorch / 数学的具体水平：待 Phase 0 诊断，不预设为已掌握。
- **总体学习计划：见 `learning/plan.md`**（阶段路线图 + 每周节奏模板 + 每日跟踪流程）。

## 当前位置

- **阶段**：P1 / A1 Basics（对应 plan.md 的 W1，进行中）。
- **当前主题**：Lecture 01 — tokenization：L01-4～9 均已讲解；本次完成 BPE 训练、encode/decode 与 A1 增强要求概览，掌握度待用户自评。
- **当前作业**：A1 尚未开始实现。
- **环境**：A1 环境及数据已可用；这不表示课程任务已完成。
- **下一次最小动作**：阅读 A1 handout 的 tokenizer 部分，理解输入、输出与要求，不写实现。
- **建议命令**：`/skill:cs336-english 读 A1 handout 的 tokenizer 部分`

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
| A1 Basics | 未开始 | 环境和 TinyStories/OWT 数据已就绪；先学第 1 讲并读 handout |
| A2 Systems | 未开始 | 等 A1；后续再处理 Triton/分布式 |
| A3 Scaling | 未开始 | 等 A1/A2；注意非学生 API 与数据限制 |
| A4 Data | 未开始 | 离线资产足够后续单测与调试 |
| A5 Alignment | 未开始 | 后续大模型训练优先考虑云 GPU |

## 最近会话

- [2026-11-23 L01：BPE 训练与使用](sessions/2026-11-23-lecture01-bpe.md)：完成 L01-9 纯讲解；未出检查题，掌握度待用户自评。
- [2026-11-23 L01：character / word tokenization 与 BPE 动机](sessions/2026-11-23-lecture01-char-word.md)：回忆题与共同弱点答对；迁移题、复述均跳过。
- [2026-11-23 L01：token 与 byte](sessions/2026-11-23-lecture01-token-byte.md)：3 道检查题全对（含理由补充），复述跳过。
