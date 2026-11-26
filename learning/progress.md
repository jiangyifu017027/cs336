# 我的 CS336 学习进度

> 本文件记录“人学到了什么”；环境和数据状态见根目录 `STATUS.md`。

## 学习偏好

- 主要语言：简体中文。
- 英语水平：CET-4 左右；技术术语保留英文，复杂原文配合中文解释。
- 协作方式（2026-11-25 起；2026-11-26 扩大）：AI 负责**记录进度 + 告诉用户接下来做什么（含作业剩余题目）**，不主动提问、不做理解检查、不要求复述；概念讲解仅在用户主动要求时进行（cs336-study）。**2026-11-26 起：用户口述核心思路，AI 直接实现/修改作业代码并跑测试验证**（用户为业余自学者、非注册学生，明确决定）。日常主入口是 cs336-review。
- 内容忠实度：严格按课程讲义（`lecture_NN.py` / PDF）的顺序与内容讲解，不超前引入后续讲次概念；助教补充用【补充】标注（2026-11-22 用户明确要求，已写入 cs336-study skill）。
- 掌握度：由用户自评，并在写作业过程中自我验证；AI 只负责讲清知识、维护 `learning/knowledge-map.md` 的“已讲解”标记。**2026-11-26 起 AI 按用户思路代写的代码不作为掌握度证据**（不伪造进度）。
- 每周可学习时间（2026-11-22 确认）：工作日 30 min/天，周末 4 h/天，约 10.5 h/周。
- 学习速度：偏慢（自述）；基础：AI 专业本科二年级，有简单 ML/DL 基础（自述）。
- Python / PyTorch / 数学起点：已于 2026-11-23 完成诊断，三项均需从基础补起，详见下方记录。
- **课程掌握进度表：见 `learning/knowledge-map.md`**（2026-11-25 起为唯一进度表，含各模块重点与 A1/A3 实践勾选；时间管理式学习计划 plan.md 已删除）。范围：主线 L01–L03 + A1 完整做；L05/L07/L09/L10/L13/L15–L17 概念级；A3 可选轻量版。

## 当前位置

- **阶段**：主线 A1 Basics（进行中）。
- **当前主题**：BPE tokenizer 实现（handout §2.3–2.7）— 训练三步、编码/解码、special tokens、效率手段等基础知识已讲解（2026-11-25 首讲 + 复讲）。
- **当前作业**：unicode1、unicode2 共六个小问待作答；train_bpe（15 分）与 tokenizer（15 分）待实现。
- **环境**：WSL2 的 A1 环境及数据已于 2026-11-21 验证可用；当前 Mac 副本待复查。这不表示课程任务已完成。
- **下一次最小动作**（2026-11-26 新模式）：用户口述 train_bpe 实现思路 → AI 编写代码并运行 `tests/test_train_bpe.py` 验证 → AI 逐段解释实现。
- **命令执行**：2026-11-26 起 AI 可直接运行作业相关命令与 pytest（用户授权，见根 AGENTS.md 作业边界）；用户计划用手机端（Paseo/web）指挥，见 sessions/2026-11-26 记录。

## 待办清单（AI 每次会话更新，2026-11-25 起）

### 下一步最小动作

用户口述 train_bpe 实现思路 → AI 实现并跑通 `tests/test_train_bpe.py` → AI 逐段解释实现（unicode1/unicode2 六小问可并行；书面题建议用户自己答，AI 可核对讲解）。

### 当前作业剩余题目（A1 Basics，tokenizer 部分）

按 handout 第 2 节顺序（共 7 题 42 分，已读题未实现）：

- [ ] unicode1：书面题，六个小问待作答（§2.1–2.2 前置概念已讲解；答完可让 AI 核对讲解）
- [ ] unicode2：书面题，同上
- [ ] train_bpe：代码题 15 分，基础知识（训练三步、tie-breaking、special tokens、效率手段）已讲解；等用户口述思路后由 AI 实现
- [ ] train_bpe_tinystories / train_bpe_expts_owt：实验题，依赖 train_bpe 完成
- [ ] tokenizer（encode/decode/encode_iterable）：代码题 15 分，编码镜像过程与 U+FFFD 解码已讲解；train_bpe 完成后由 AI 按用户思路实现
- [ ] tokenizer_experiments：实验题 4 分，依赖前两者
- [ ] A1 模型部分（Transformer 各模块）：未开始，等 L02/L03
- [ ] A1 训练部分（优化器、训练循环）：未开始

> 精确的题号、分值与要求以 handout 为准；用户说"作业里还要做哪些"时，AI 应重新读 handout 对应章节并补全此清单，不凭记忆列题。

### 当前模块检查点

L01（基础与分词）收尾：自认为说清 BPE 训练在做什么后，在 `knowledge-map.md` 把 L01-9 勾为 🟢，其余 L01 条目按实际自评勾选。

## 学前诊断（2026-11-23 完成）

方式：对话自评 + 3 个微检查（`setdefault` 输出、broadcasting shape、矩阵乘法 shape），用户对全部三组回答“都不会”。

- [x] Python：不能独立写带类型标注的函数/类；不知 `dict.setdefault` 行为 → 接近零基础。读 starter 代码时需逐行讲解。
- [x] PyTorch：未写过训练循环；broadcasting 不会 → 零基础。L02 是重点，需放慢。
- [x] 数学：矩阵乘法 shape、softmax、交叉熵均不会 → 零基础。用到时以【补充】即时补，不单独开数学课。
- [x] 学习投入：10.5 h/周（2026-11-22 已确认）；A1 目标完成时长未设定。

校准结论：三项起点均较低，但课程本身覆盖 PyTorch（L02）和所需数学；学习速度以实际进展为准，不预设已掌握。

## 讲次进度

状态含义：`未开始` → `学习中` → `已初学，待复习` → `已掌握`。掌握状态由用户自评 + 作业证据决定（2026-11-23 起不再靠课堂提问判定）；逐条知识点的勾选见 `learning/knowledge-map.md`。

| 讲次 | 主题 | 深度 | 状态 | 掌握证据 / 遗留问题 |
|---|---|---|---|---|
| 01 | Overview, tokenization | 主线 | 学习中 | L01-1～9 已全部讲解；掌握度待用户在 knowledge-map.md 自评 |
| 02 | PyTorch, resource accounting | 主线 | 未开始 | |
| 03 | Architectures, hyperparameters | 主线 | 未开始 | |
| 05 | GPUs | 概念 | 未开始 | |
| 07 | Parallelism basics | 概念 | 未开始 | |
| 09 | Scaling laws basics | 概念 | 未开始 | |
| 10 | Inference | 概念 | 未开始 | |
| 13 | Data | 概念 | 未开始 | |
| 15 | Alignment: SFT / RLHF | 概念 | 未开始 | |
| 16 | Alignment: RL | 概念 | 未开始 | |
| 17 | Reasoning RL mechanics | 概念 | 未开始 | |

> 逐条掌握度以 `learning/knowledge-map.md` 为准；L04/L06/L08/L11/L12/L14 不在计划内，不列。

## 作业进度

| 作业 | 状态 | 当前证据 / 下一步 |
|---|---|---|
| A1 Basics | 读题 | WSL2 环境和 TinyStories/OWT 数据已就绪，Mac 待复查；tokenizer 部分题意卡及 Unicode 前置概念已整理；下一步由用户独立完成 unicode1/unicode2 六个小问 |
| A2 Systems | 不在计划内 | 仅 L05/L07 概念级覆盖 |
| A3 Scaling | 可选轻量版 | 主线走完后由用户决定；只做本地小实验，注意非学生 API 与数据限制 |
| A4 Data | 不在计划内 | 仅 L13 概念级覆盖 |
| A5 Alignment | 不在计划内 | 仅 L15–L17 概念级覆盖；以后若想补做，大模型训练优先考虑云 GPU |

## 后续学习目标（CS336 之后）

- **Stanford CS329Z — Engineering AI Agents（Fall 2025）**：理解 Claude Code / Pi 这类 coding agent 的工作机制（harness / scaffold，即模型外面的工程层）。官网 cs329z.stanford.edu，幻灯片与视频公开。2026-11-25 用户确定加入。
  - 重点讲次：第 3–5 讲（tool use / function calling 与 MCP、框架与 harness 对比 mini-SWE-agent / OpenHands / Pi、ReAct / CodeAct / compaction 等设计模式）、第 11 讲（拆解 SWE-agent / Claude Code / OpenHands 架构）。
  - 前置：CS336 主线（transformer、推理、post-training）学完后开始。
  - 配套动手（可选）：自己写一个最小 agent + 读一个开源 harness（OpenHands 或 Pi）。
  - 备选补充：Berkeley Agentic AI MOOC（F25，agenticai-learning.org/f25），偏 agentic RL / post-training 研究，需要时再看。

## 最近会话

- [2026-11-26 协作模式变更：AI 直接实现作业代码](sessions/2026-11-26-collab-mode-change.md)：用户（业余自学者）决定改为"口述思路 → AI 实现并验证"；AGENTS.md、skill、进度档案均已同步；手机端走 Paseo + GitHub。
- [2026-11-25 L01 复讲：BPE](sessions/2026-11-25-lecture01-bpe-revisit.md)：用户主动要求重点复讲 L01-9；含手算例子与 A1 增强要求；未提问，掌握度待自评。
- [2026-11-23 A1 handout：Unicode 书面题前置概念](sessions/2026-11-23-a1-unicode-concepts.md)：巩固 L01-5/6；未给答案、未出检查题，六个小问待用户独立完成。
- [2026-11-23 A1 handout：tokenizer 题意卡](sessions/2026-11-23-a1-handout-tokenizer.md)：Section 2 共 7 题 42 分的要求与字面规则整理；未出检查题。
- [2026-11-23 L01：BPE 训练与使用](sessions/2026-11-23-lecture01-bpe.md)：完成 L01-9 纯讲解；未出检查题，掌握度待用户自评。
- [2026-11-23 L01：character / word tokenization 与 BPE 动机](sessions/2026-11-23-lecture01-char-word.md)：回忆题与共同弱点答对；迁移题、复述均跳过。
- [2026-11-23 L01：token 与 byte](sessions/2026-11-23-lecture01-token-byte.md)：3 道检查题全对（含理由补充），复述跳过。
