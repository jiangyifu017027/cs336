# 我的 CS336 学习进度

> 本文件记录“人学到了什么”；环境和数据状态见根目录 `STATUS.md`。

## 学习偏好

- 主要语言：简体中文。
- 英语水平：CET-4 左右；技术术语保留英文，复杂原文配合中文解释。
- 辅导方式：直觉和例子优先，再进入公式、shape 和实现；通过提问检查理解。
- 内容忠实度：严格按课程讲义（`lecture_NN.py` / PDF）的顺序与内容讲解，不超前引入后续讲次概念；助教补充用【补充】标注（2026-11-22 用户明确要求，已写入 cs336-study skill）。
- 每周可学习时间：待确认。
- Python / PyTorch / 数学基础：待诊断，不预设为已掌握。

## 当前位置

- **阶段**：Phase 0 学前诊断 → Phase 1 / A1 Basics。
- **当前主题**：Lecture 01 — Overview, tokenization。
- **当前作业**：A1 尚未开始实现。
- **环境**：A1 环境及数据已可用；这不表示课程任务已完成。
- **下一次最小动作**：进行 10 分钟前置诊断，然后学习“语言模型整体流水线”和“token 与 byte 的关系”。
- **建议命令**：`/skill:cs336-study 从第 1 讲开始，先做简短诊断，再讲 token 和 byte`

## 学前诊断（等待用户回答）

- [ ] Python：能否独立写函数、类，使用 `dict/list`、类型标注和调试器？
- [ ] PyTorch：是否理解 tensor、shape、broadcasting、梯度与基本训练循环？
- [ ] 数学：是否熟悉向量/矩阵乘法、softmax、交叉熵和链式法则？
- [ ] 学习投入：每周大约能投入多少小时？希望多久完成 A1？

## 讲次进度

状态含义：`未开始` → `学习中` → `已初学，待复习` → `已掌握`。状态提升必须有实际学习证据。

| 讲次 | 主题 | 状态 | 掌握证据 / 遗留问题 |
|---|---|---|---|
| 01 | Overview, tokenization | 未开始 | 下一步先做学前诊断 |
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

暂无。第一次学习结束后在 `sessions/` 新建记录，并在这里保留最近一条链接。
