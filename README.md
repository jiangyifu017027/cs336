# CS336 学习仓库

斯坦福 CS336《Language Modeling from Scratch》自学仓库。
目标：从零实现一个大语言模型的全部核心组件（tokenizer → Transformer → 训练 → 系统优化 → 数据管线 → 对齐）。

- 课程主页（最新学期）：https://cs336.stanford.edu/
- Spring 2025 归档版（作业/讲义公开）：https://stanford-cs336.github.io/spring2025/

## AI 中文学习助教（已配置）

本仓库已配置中文学习、英文伴读、作业诊断和复盘进度四个本地 skills。首次使用或修改配置后，在 Pi 中执行 `/reload`，然后可以直接说：

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
│   ├── a2-systems/assignment2-systems/    # A2: 性能分析 + Triton FlashAttention2 + 分布式
│   ├── a3-scaling/assignment3-scaling/    # A3: 理解各组件作用 + 拟合 scaling law
│   ├── a4-data/assignment4-data/          # A4: Common Crawl → 预训练数据（过滤 + 去重）
│   └── a5-alignment/assignment5-alignment/ # A5: SFT + RL(GRPO) 数学推理，选做 DPO
├── resources/
│   ├── spring2025-lectures/   # 全部讲义（PDF + 可执行幻灯片 + trace）
│   ├── papers/                # 课程推荐论文（PDF 离线缓存 + README 索引）
│   └── cheatsheets/           # PyTorch / Triton / 分布式 / Profiling 速查
├── scripts/                   # 环境安装/检查、讲义本地服务器
├── STATUS.md                  # 环境、数据、资料的现状与缺口
└── scratch/                   # 随堂练习、草稿实验（随便折腾，不进正式作业）
```

## 环境与资料状态

- 环境检查：`./scripts/check_envs.sh`
- 一键安装/更新：`./scripts/setup_envs.sh [a1|a2|a3|a4|a5|all]`
- 本机现状与缺口：见 [STATUS.md](STATUS.md)
- 讲义索引与笔记模板：[lectures/README.md](lectures/README.md)
- 论文库（离线 PDF）：[resources/papers/README.md](resources/papers/README.md)
- 速查表：[resources/cheatsheets/README.md](resources/cheatsheets/README.md)

本地看可执行讲义：

```bash
./scripts/serve_lectures.sh
# 浏览器打开
# http://localhost:8000/spring2025-lectures/index.html?trace=var/traces/lecture_01.json
```

每个作业文件夹的约定：

- 官方仓库已下载到各 `aN-xxx/assignmentN-xxx/` 子目录（内含 handout PDF、`cs336_xxx/` starter 包、tests）
- 注意：A5 仓库已更新为 2026 版（`cs336_spring2026_assignment5_*.pdf`），与 2025 归档页略有差异，以仓库内 PDF 为准
- 每个仓库自带 `AGENTS.md`（课程给 AI 助手的工作守则：做"助教"而非"解题器"）
- 自己的代码写在包内对应模块；`notes.md` 记实现思路、踩坑和复盘
- 每个作业独立 Python 环境（`uv venv && uv pip install -e .`），避免依赖冲突

## 学习路线（按作业推进）

每阶段先读 handout 明确要求，再看对应 lecture，最后动手实现。

### Phase 0：环境准备（几天）
- [ ] 确认基础：Python 熟练度、PyTorch、微积分/线代/概率
- [ ] 装好 PyTorch（GPU 版）、uv、Git
- [ ] （热身，可选）Karpathy 的 nanoGPT / makemore，找回"手写训练循环"的手感

### Phase 1 → Assignment 1：基础（约 2~3 周，最重）
- [ ] BPE tokenizer：从字节级开始手写，处理合并、特殊 token、效率优化
- [ ] Transformer：embedding、RoPE、causal attention、GELU、残差、LayerNorm、输出投影
- [ ] 优化器：AdamW + warmup + cosine 学习率调度
- [ ] 在 FineWeb 10B 子集上训练一个小 LM，跑通完整闭环
- 对应 lecture：intro、tokenization、transformers、optimizers

### Phase 2 → Assignment 2：系统（约 1~2 周）
- [ ] 用 PyTorch profiler 给模型和各层做性能分析
- [ ] 手写 Triton 版 FlashAttention2（**Windows 建议用 WSL2**，Triton 原生 Windows 支持不稳）
- [ ] 混合精度 + 梯度checkpointing + DDP/FSDP 分布式训练
- 对应 lecture：GPU 架构、内存层级、kernels/Triton、并行策略

### Phase 3 → Assignment 3：Scaling（约 1 周）
- [ ] 消融实验：理解 Transformer 每个组件的作用
- [ ] 拟合 scaling law，用少量实验外推更大模型的 loss
- [ ] 学会用 W&B 等工具做实验追踪

### Phase 4 → Assignment 4：数据（约 2 周）
- [ ] 从 Common Crawl 原始 dump 提取正文
- [ ] 质量过滤 + MinHash 去重
- [ ] 对比不同数据配方对模型效果的影响

### Phase 5 → Assignment 5：对齐与推理 RL（约 1~2 周）
- [ ] SFT：微调模型解数学题
- [ ] RL（GRPO 类算法）强化推理能力
- [ ] （选做）DPO 做安全对齐

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
- **本地论文库**：`resources/papers/`，索引见 `README.md`
- **本地速查表**：`resources/cheatsheets/`

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
