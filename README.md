# CS336 学习仓库

斯坦福 CS336《Language Modeling from Scratch》自学仓库。
目标：从零实现一个大语言模型的全部核心组件（tokenizer → Transformer → 训练 → 系统优化 → 数据管线 → 对齐）。

- 课程主页（最新学期）：https://cs336.stanford.edu/
- Spring 2025 归档版（作业/讲义公开）：https://stanford-cs336.github.io/spring2025/

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
├── README.md                  # 本文件：总览 + 学习路线
├── AGENTS.md                  # 中文沟通、学习档案和作业辅助边界
├── .agents/skills/            # 4 个本地 AI 学习 skills
├── learning/                  # 个人进度、疑问、术语和会话复盘
├── lectures/                  # 17 讲笔记索引 + 每讲笔记模板
├── assignments/               # 5 个大作业，每个作业一个文件夹
│   ├── a1-basics/assignment1-basics/      # A1: BPE + Transformer + 优化器，训练小 LM
│   ├── a2-systems/assignment2-systems/    # A2: FlashAttention2 + DDP/FSDP + 优化器分片
│   ├── a3-scaling/assignment3-scaling/    # A3: 小规模训练实验 + scaling law 拟合与外推
│   ├── a4-data/assignment4-data/          # A4: Common Crawl → 预训练数据（过滤 + 去重）
│   └── a5-alignment/assignment5-alignment/ # A5: GRPO/推理 RL，选做 SFT + DPO + 安全对齐
├── resources/
│   ├── spring2025-lectures/   # 全部讲义（PDF + 可执行幻灯片 + trace）
│   └── papers/                # 课程推荐论文（PDF 离线缓存 + README 索引）
├── scripts/                   # 环境安装/检查、讲义本地服务器
└── STATUS.md                  # 环境、数据、资料的现状与缺口
```

## 环境与资料状态

- 环境检查：`./scripts/check_envs.sh`
- 一键安装/更新：`./scripts/setup_envs.sh [a1|a2|a3|a4|a5|all]`
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
- 版本：讲义索引与 A1 为 Spring 2025；本地 A2–A5 已更新为 Spring 2026。作业内容以各仓库内的 handout PDF、公开测试和 starter 为准
- 每个仓库自带 `AGENTS.md`（课程给 AI 助手的工作守则：做"助教"而非"解题器"）
- 自己的代码写在包内对应模块；`notes.md` 记实现思路、踩坑和复盘
- 每个作业使用独立的 `uv` 环境；优先通过 `./scripts/setup_envs.sh [a1|a2|a3|a4|a5|all]` 安装，或按各作业 README 在作业根目录执行 `uv sync`，避免依赖冲突

## 课程内容与作业地图

课程共有 **17 讲、5 次作业**，主线是：从零实现语言模型 → 优化 GPU 与多卡系统 → 用小实验预测大规模训练 → 构建数据管线 → 做对齐与推理强化学习。

### 17 讲总览

| 讲 | 主题 | 核心内容 |
|---|---|---|
| 01 | Overview, tokenization | 语言模型流水线、token/byte、character/word tokenization、BPE、压缩率 |
| 02 | PyTorch, resource accounting | tensor 与 shape/dtype/device、FLOPs、显存账本、数值精度、MFU、初始化 |
| 03 | Architectures, hyperparameters | Transformer、RMSNorm、SwiGLU、RoPE、attention 变体、超参数与稳定性 |
| 04 | Mixture of experts | 专家路由、稀疏激活、专家并行、容量与计算的解耦 |
| 05 | GPUs | GPU 与内存层级、数据搬运、算术强度、roofline、tiling |
| 06 | Kernels, Triton | GPU kernel、Triton 编程模型、算子融合、benchmark 与调优 |
| 07 | Parallelism basics | 集合通信、数据/张量/流水线/序列并行、ZeRO/FSDP |
| 08 | Parallelism | NCCL、通信计算重叠、组合并行策略、显存与通信取舍 |
| 09 | Scaling laws basics | 幂律、Kaplan/Chinchilla、计算最优分配、isoflops、数据受限 |
| 10 | Inference | prefill/decode、KV cache、量化、蒸馏、投机解码、推理调度 |
| 11 | Scaling laws details | scaling law 拟合与外推、学习率/batch size/schedule 的规模化选择 |
| 12 | Evaluation | 知识与推理 benchmark、指令遵循、LM-as-a-judge、代码/agent 评测、数据污染 |
| 13 | Data | 数据来源与配比、不同训练阶段的数据、文本提取、过滤、版权与许可 |
| 14 | Data filtering & dedup | 质量与有害内容过滤、Gopher 规则、精确去重、MinHash 近似去重 |
| 15 | Alignment: SFT / RLHF | SFT、奖励模型、PPO、DPO、RLHF 的副作用与工程问题 |
| 16 | Alignment: RL | RLVR、GRPO、Dr. GRPO、推理模型训练流程 |
| 17 | Reasoning RL mechanics | 策略梯度、baseline、off-policy、组归一化、实验可复现性 |

讲次索引见 [lectures/README.md](lectures/README.md)，逐条知识点见 [learning/knowledge-map.md](learning/knowledge-map.md)。

### 作业文件怎么组织

A1、A2、A4、A5 都不是只填充已有文件里的几个 TODO：核心实现通常由学生在对应 package 中自行组织，再用 `tests/adapters.py` 连接官方测试。**除 `adapters.py` 外，不应修改测试来让测试通过。** 以下路径均相对各作业根目录。

### A1 Basics：从零实现并训练语言模型

目录：`assignments/a1-basics/assignment1-basics/`

- 内容：BPE 训练与 encode/decode、special tokens、流式编码；Linear、Embedding、RMSNorm、SiLU/SwiGLU、attention、RoPE、Transformer block 和完整 LM；softmax、交叉熵、梯度裁剪、AdamW、余弦学习率、batch 采样、checkpoint；在 TinyStories 和 OpenWebText 上训练。
- 必改：`tests/adapters.py`，连接自己的实现与公开测试。
- 核心实现：在 `cs336_basics/` 中自行添加和组织模块，具体文件名不强制。
- 其他：训练脚本与实验记录自行维护；`pretokenization_example.py` 是示例，不是核心 TODO。

### A2 Systems：GPU 算子与分布式训练

目录：`assignments/a2-systems/assignment2-systems/`

- 内容：PyTorch/Triton 版 FlashAttention2 前向与反向；DDP 参数广播、梯度同步和通信重叠；FSDP 参数分片、all-gather、梯度 reduce-scatter 与混合精度；sharded optimizer。
- 必改：`tests/adapters.py`。
- 核心实现：在 `cs336_systems/` 中自行添加和组织模块。
- 基础模型：`cs336-basics/` 是官方 A1 实现，可保留或按 README 换成自己的 A1，不是 A2 的主要开发区域。

### A3 Scaling：小规模实验与大规模预测

目录：`assignments/a3-scaling/assignment3-scaling/`

- 内容：在预算内提交不同规模和超参数的训练实验，收集 loss，拟合 scaling law，外推更大规模的训练配置和最终 loss，并通过 API 提交预测。
- 代码边界：没有待完成的 `NotImplementedError` 或空白 adapters，不需要补全服务端源码。
- 入口：`examples/client_example.ipynb` 演示查询预算、提交实验、读取结果与最终提交。
- 自己的文件：实验 notebook、拟合脚本和分析文件自行组织；`cs336_scaling/` 主要是已提供的训练 API 与调度基础设施。

### A4 Data：数据清洗、过滤、去重与训练验证

目录：`assignments/a4-data/assignment4-data/`

- 内容：Common Crawl HTML 文本提取、语言识别、个人信息遮蔽、NSFW/有害言论/质量分类、Gopher 质量过滤、精确行去重、MinHash 模糊去重，以及用处理后的数据训练模型。
- 必改：`tests/adapters.py`。
- 核心实现：在 `cs336_data/` 中自行添加和组织模块。
- 额外 TODO：`cs336_data/wet_files.py` 中有完整数据下载流程的语言过滤位置。
- 不要修改：`cs336_basics/` 中的官方训练逻辑；`scripts/train.py` 是提供的训练入口。
- 环境配置：仅在需要调整本地或 Modal 环境时处理 `cs336_data/common.py`、`modal_utils.py`，它们不是核心算法任务。

### A5 Alignment：GRPO 主作业与可选安全对齐

目录：`assignments/a5-alignment/assignment5-alignment/`

- 主作业：prompt/response tokenization 与 response mask、逐 token log probability 与 entropy、rollout 奖励、组内 baseline 与优势归一化、on/off-policy 策略梯度、GRPO/GSPO clipping、microbatch 损失聚合与训练步骤。
- 可选补充：SFT 数据打包与 batch 遍历、MMLU/GSM8K 输出解析、DPO 单样本损失、安全对齐与 RLHF 实验。
- 必改：`tests/adapters.py`。
- 核心实现：在 `cs336_alignment/` 中自行添加和组织模块，训练与分析脚本自行维护。
- 测试边界：主作业必测 `tests/test_grpo.py`；`test_data.py`、`test_metrics.py`、`test_dpo.py` 对应可选补充。
- 已有工具：`vllm_utils.py`、`drgrpo_grader.py`、`checkpoint.py` 等是辅助工具，不是集中等待填空的 starter 文件。

### 讲次与作业对应

| 作业 | 主要对应讲次 | 核心产出 |
|---|---|---|
| A1 | L01–L03 | tokenizer、Transformer、训练组件与实际训练 |
| A2 | L05–L08 | GPU attention、DDP、FSDP、优化器分片 |
| A3 | L09、L11 | scaling 实验、拟合与大尺度预测 |
| A4 | L12–L14 | 数据提取、过滤、去重与训练验证 |
| A5 | L15–L17 | GRPO/推理 RL；可选 SFT、DPO、安全对齐 |

每阶段先读 handout 明确要求，再学对应 lecture，最后独立实现。个人阶段顺序、时间预算与滚动计划统一见 [learning/plan.md](learning/plan.md)；当前进度见 [learning/progress.md](learning/progress.md)。各 PDF 中的书面报告、评分细则与提交格式仍以对应 handout 为准。

## 算力与工程约定

- A1/A3 的小模型可在单卡消费级 GPU（如 24G）上完成；A2 需要 GPU 做 benchmark；A4 数据管线吃 CPU/磁盘；A5 建议更大显存
- 云端 GPU 参考：RunPod / Lambda Labs；国内也可考虑 AutoDL
- 原则：先在 CPU/小数据上验证正确性，再上 GPU 跑正式训练，省钱
- Windows 说明：A2 的 Triton 部分建议在 WSL2 中进行；其余作业原生 Windows + Git Bash 基本够用
- 进度追踪：日常进度与复盘记录在 `learning/`；作业完成后也可在对应 `notes.md` 总结并 commit 一次

## 学习资源

### 官方资源
- **课程视频（YouTube 播放列表）**：https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV — 每讲对应一个视频，B 站一般有搬运（搜 "CS336"），网络不方便时可选
- **课程主页（最新学期）**：https://cs336.stanford.edu/
- **Spring 2025 归档页**（作业/讲义最全的公开版）：https://stanford-cs336.github.io/spring2025/
- **讲义交互版**：运行 `./scripts/serve_lectures.sh`，浏览器打开
  `http://localhost:8000/spring2025-lectures/index.html?trace=var/traces/lecture_01.json`
  （17 讲的 trace 已全部在本地）
- **本地论文库**：`resources/papers/`，索引见 `resources/papers/README.md`

### 社区资源（参考用，别抄作业实现）
- 中文精读笔记（GitHub 搜 "CS336"，有整门课的中文讲义+可运行推导）
- 他人的 CS336 作业实现仓库很多——按课程诚信要求，实现阶段不要去看

### 学完 CS336 后的后续课程（agent 方向）
- Hugging Face Agents Course（免费，agent 工程）：https://huggingface.co/learn/agents-course
- Berkeley CS285 Deep RL（从零手写 RL 算法，衔接 A5）：https://rail.eecs.berkeley.edu/deeprlcourse/
- Anthropic Academy（免费，agentic 工程实践）

## 学术诚信提醒

课程官方政策：可以用 LLM 问概念和低级编程问题，但**不能直接让 AI 代写作业实现**。
每个作业仓库里的 `AGENTS.md` 写明了 AI 助手的工作守则，在本仓库内我将照做：
讲概念、帮你 debug（用引导式提问）、review 你的代码——但不动手写实现。
先读完 handout 再动手，实现时不去抄网上现成的 CS336 作业代码。
