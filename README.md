# CS336 学习仓库（轻量版）

斯坦福 CS336《Language Modeling from Scratch》自学仓库。
目标：从零实现并训练一个小语言模型（tokenizer → Transformer → 训练），并对其余核心主题（GPU/并行、scaling laws、推理、数据、对齐）建立概念级理解。

- 课程主页（最新学期）：https://cs336.stanford.edu/
- Spring 2025 归档版（作业/讲义公开）：https://stanford-cs336.github.io/spring2025/

> 2026-11-25 按轻量计划清理：只保留主线 L01–L03 + A1，以及可选 A3 轻量版；概念线 L05/L07/L09/L10/L13/L15–L17 只学概念；L04/L06/L08/L11/L12/L14 与 A2/A4/A5 的本地资料已删除。学习计划见 [learning/plan.md](learning/plan.md)。

## AI 中文学习助教（已配置）

本仓库已配置中文学习、英文伴读、作业诊断和复盘进度四个本地 skills。首次使用或修改配置后，在 Kimi Code CLI 中执行 `/reload`，然后可以直接说：

- “从第 1 讲开始，用中文带我学习”
- “帮我读懂 A1 handout 这一部分，不要给实现答案”
- “帮我分析这个报错并引导我定位”
- “结束本次学习，更新我的进度”

也可以显式使用 `/skill:cs336-study`、`/skill:cs336-english`、`/skill:cs336-assignment` 和 `/skill:cs336-review`。完整说明见 [learning/README.md](learning/README.md)，当前学习位置见 [learning/progress.md](learning/progress.md)。

## 目录结构

```
CS336/
├── README.md                  # 本文件：总览 + 轻量学习路线
├── AGENTS.md                  # 中文沟通、学习档案和作业辅助边界
├── .agents/skills/            # 4 个本地 AI 学习 skills
├── learning/                  # 个人进度、疑问、术语和会话复盘
├── lectures/                  # 11 讲笔记索引 + 每讲笔记模板
├── assignments/               # 作业（轻量版只保留 A1 与可选 A3）
│   ├── a1-basics/assignment1-basics/      # A1: BPE + Transformer + 优化器，训练小 LM
│   └── a3-scaling/assignment3-scaling/    # A3（可选轻量版）: 小规模 scaling law 实验
├── resources/
│   ├── spring2025-lectures/   # 保留讲次的讲义（PDF + 可执行幻灯片 + trace）
│   └── papers/                # 课程推荐论文（PDF 离线缓存 + README 索引）
├── scripts/                   # 环境安装/检查、讲义本地服务器
└── STATUS.md                  # 环境、数据、资料的现状与缺口
```

## 环境与资料状态

- 环境检查：`./scripts/check_envs.sh`
- 一键安装/更新：`./scripts/setup_envs.sh [a1|a3|all]`
- 本机现状与缺口：见 [STATUS.md](STATUS.md)
- 讲义索引与笔记模板：[lectures/README.md](lectures/README.md)
- 论文库（离线 PDF）：[resources/papers/README.md](resources/papers/README.md)

本地看可执行讲义：

```bash
./scripts/serve_lectures.sh
# 浏览器打开
# http://localhost:8000/spring2025-lectures/index.html?trace=var/traces/lecture_01.json
```

每个作业文件夹的约定：

- 官方仓库已下载到各 `aN-xxx/assignmentN-xxx/` 子目录（内含 handout PDF、`cs336_xxx/` starter 包、tests）
- 版本：讲义索引与 A1 为 Spring 2025；本地 A3 已更新为 Spring 2026。作业内容以各仓库内的 handout PDF、公开测试和 starter 为准
- 每个仓库自带 `AGENTS.md`（课程给 AI 助手的工作守则：做"助教"而非"解题器"）
- 自己的代码写在包内对应模块；`notes.md` 记实现思路、踩坑和复盘
- 每个作业使用独立的 `uv` 环境；优先通过 `./scripts/setup_envs.sh [a1|a3]` 安装，或按各作业 README 在作业根目录执行 `uv sync`，避免依赖冲突

## 课程内容地图

主线一句话：**从零实现并训练一个语言模型**；其余保留讲次建立概念级理解，覆盖“做快、做大、做好”三个方向。

### 保留的 11 讲

| 讲 | 主题 | 深度 | 核心内容 |
|---|---|---|---|
| 01 | Overview, tokenization | 主线 | 语言模型流水线、token/byte、character/word tokenization、BPE、压缩率 |
| 02 | PyTorch, resource accounting | 主线 | tensor 与 shape/dtype/device、FLOPs、显存账本、数值精度、MFU、初始化 |
| 03 | Architectures, hyperparameters | 主线 | Transformer、RMSNorm、SwiGLU、RoPE、attention 变体、超参数与稳定性 |
| 05 | GPUs | 概念 | GPU 与内存层级、数据搬运、算术强度、roofline、tiling |
| 07 | Parallelism basics | 概念 | 集合通信、数据/张量/流水线/序列并行、ZeRO/FSDP |
| 09 | Scaling laws basics | 概念 | 幂律、Kaplan/Chinchilla、计算最优分配、isoflops、数据受限 |
| 10 | Inference | 概念 | prefill/decode、KV cache、量化、蒸馏、投机解码、推理调度 |
| 13 | Data | 概念 | 数据来源与配比、不同训练阶段的数据、文本提取、过滤、版权与许可 |
| 15 | Alignment: SFT / RLHF | 概念 | SFT、奖励模型、PPO、DPO、RLHF 的副作用与工程问题 |
| 16 | Alignment: RL | 概念 | RLVR、GRPO、Dr. GRPO、推理模型训练流程 |
| 17 | Reasoning RL mechanics | 概念 | 策略梯度、baseline、off-policy、组归一化、实验可复现性 |

> 未保留的讲次：L04 MoE、L06 Triton、L08 并行进阶、L11 scaling 细节、L12 评测、L14 去重细节。本地讲义与笔记已删除；以后想补可从课程官方仓库重新获取。

讲次索引见 [lectures/README.md](lectures/README.md)，逐条知识点见 [learning/knowledge-map.md](learning/knowledge-map.md)。

### 作业文件怎么组织

A1、A3 都不是只填充已有文件里的几个 TODO：核心实现通常由学生在对应 package 中自行组织，再用 `tests/adapters.py` 连接官方测试。**除 `adapters.py` 外，不应修改测试来让测试通过。** 以下路径均相对各作业根目录。

#### A1 Basics：从零实现并训练语言模型

目录：`assignments/a1-basics/assignment1-basics/`

- 内容：BPE 训练与 encode/decode、special tokens、流式编码；Linear、Embedding、RMSNorm、SiLU/SwiGLU、attention、RoPE、Transformer block 和完整 LM；softmax、交叉熵、梯度裁剪、AdamW、余弦学习率、batch 采样、checkpoint；在 TinyStories 和 OpenWebText 上训练。
- 必改：`tests/adapters.py`，连接自己的实现与公开测试。
- 核心实现：在 `cs336_basics/` 中自行添加和组织模块，具体文件名不强制。
- 其他：训练脚本与实验记录自行维护；`pretokenization_example.py` 是示例，不是核心 TODO。

#### A3 Scaling：小规模实验与大规模预测（可选轻量版）

目录：`assignments/a3-scaling/assignment3-scaling/`

- 内容：在预算内提交不同规模和超参数的训练实验，收集 loss，拟合 scaling law，外推更大规模的训练配置和最终 loss，并通过 API 提交预测。
- 轻量版做法：跳过 API 提交与非学生不可用的 hosted 训练，只做本地小规模实验与拟合；详见 [learning/plan.md](learning/plan.md)。
- 代码边界：没有待完成的 `NotImplementedError` 或空白 adapters，不需要补全服务端源码。
- 入口：`examples/client_example.ipynb` 演示查询预算、提交实验、读取结果与最终提交。
- 自己的文件：实验 notebook、拟合脚本和分析文件自行组织；`cs336_scaling/` 主要是已提供的训练 API 与调度基础设施。

### 讲次与作业对应

| 作业 | 主要对应讲次 | 核心产出 | 状态 |
|---|---|---|---|
| A1 | L01–L03 | tokenizer、Transformer、训练组件与实际训练 | 主线，完整做 |
| A3（可选轻量版） | L09、L11 | 本地小规模 scaling 实验、拟合与外推 | 主线走完后由用户决定 |

先读 handout 明确要求，再学对应 lecture，最后独立实现。个人时间预算与滚动计划见 [learning/plan.md](learning/plan.md)；当前进度见 [learning/progress.md](learning/progress.md)。PDF 中的书面报告、评分细则与提交格式仍以对应 handout 为准。

## 算力与工程约定

- A1 的小模型可在单卡消费级 GPU（如 24G）上完成；A3 轻量版小实验本地或云端均可
- 云端 GPU 参考：RunPod / Lambda Labs；国内也可考虑 AutoDL
- 原则：先在 CPU/小数据上验证正确性，再上 GPU 跑正式训练，省钱
- Windows 说明：A1/A3 原生 Windows + Git Bash 基本够用
- 进度追踪：日常进度与复盘记录在 `learning/`；作业完成后也可在对应 `notes.md` 总结并 commit 一次

## 学习资源

### 官方资源
- **课程视频（YouTube 播放列表）**：https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV — 每讲对应一个视频，B 站一般有搬运（搜 "CS336"），网络不方便时可选
- **课程主页（最新学期）**：https://cs336.stanford.edu/
- **Spring 2025 归档页**（作业/讲义最全的公开版）：https://stanford-cs336.github.io/spring2025/
- **讲义交互版**：运行 `./scripts/serve_lectures.sh`，浏览器打开
  `http://localhost:8000/spring2025-lectures/index.html?trace=var/traces/lecture_01.json`
  （保留讲次的 trace 已在本地）
- **本地论文库**：`resources/papers/`，索引见 `resources/papers/README.md`

### 社区资源（参考用，别抄作业实现）
- 中文精读笔记（GitHub 搜 "CS336"，有整门课的中文讲义+可运行推导）
- 他人的 CS336 作业实现仓库很多——按课程诚信要求，实现阶段不要去看

### 学完 CS336 后的后续课程（agent 方向）
- Hugging Face Agents Course（免费，agent 工程）：https://huggingface.co/learn/agents-course
- Berkeley CS285 Deep RL（从零手写 RL 算法，衔接 L15–L17 概念线）：https://rail.eecs.berkeley.edu/deeprlcourse/
- Anthropic Academy（免费，agentic 工程实践）

## 学术诚信提醒

课程官方政策：可以用 LLM 问概念和低级编程问题，但**不能直接让 AI 代写作业实现**。
每个作业仓库里的 `AGENTS.md` 写明了 AI 助手的工作守则，在本仓库内我将照做：
讲概念、帮你 debug（用引导式提问）、review 你的代码——但不动手写实现。
先读完 handout 再动手，实现时不去抄网上现成的 CS336 作业代码。
