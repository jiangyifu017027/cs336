# CS336 知识清单（自评掌握度）

> 用途：把全课程核心知识拆成可勾选条目，**掌握度由你自己判断**，写作业时顺便验证。
> AI 只负责讲解并按编号汇报“讲了哪几条”，不再提问、不要求复述（2026-11-23 起）。

## 怎么用

| 列 | 谁填 | 含义 |
|---|---|---|
| 讲解 | AI | `✅` 已按讲义讲过；`—` 还没讲 |
| 掌握 | 你 | `⬜` 未学 / `🟡` 有印象 / `🟢` 能自己解释 / `🔵` 能独立使用（作业/实验验证过） |

- 条目编号形如 `L03-4`，可以直接说“讲 L03-4”“L07 那几条我不懂”。
- 每次学完只改“掌握”列，不用写长篇笔记；真正的证据在作业里。
- 讲次状态（`progress.md`）大致等于该讲最高的掌握档，但对不上也没关系，以这里的条目为准。

## 全部条目的分类总览

| 模块 | 讲次 | 条目数 | 对应作业 |
|---|---|---|---|
| A 基础与分词 | L01 | 9 | A1 |
| B PyTorch 与资源账本 | L02 | 8 | A1、A2 |
| C 架构与超参数 | L03、L04 | 13 | A1、A3 |
| D 系统：GPU / kernel / 并行 / 推理 | L05、L06、L07、L08、L10 | 32 | A2 |
| E Scaling laws | L09、L11 | 13 | A3 |
| F 数据与评测 | L12、L13、L14 | 19 | A4 |
| G 对齐：SFT / RLHF / RL | L15、L16、L17 | 18 | A5 |

另有 5 条**跨讲主线**（M1–M5），贯穿全程，最后统一自评。

---

# A 基础与分词（L01）

| # | 知识点 | 类型 | 讲解 | 掌握 |
|---|---|---|---|---|
| L01-1 | 课程定位：三类知识 Mechanics / Mindset / Intuitions 各是什么，哪些能从小模型迁移到前沿 | Mindset | — | ⬜ |
| L01-2 | 效率框架：`accuracy = efficiency × resources`；给定 compute+data 预算下最大化效率 | Mindset | — | ⬜ |
| L01-3 | 语言模型演进脉络：pre-neural → neural ingredients → foundation models → scaling/闭源 → 开放模型 | Intuition | — | ⬜ |
| L01-4 | tokenizer 接口：`encode`/`decode` 往返、`vocabulary size`；模型吃的是 token ID 而非字符 | Mechanics | ✅ | ⬜ |
| L01-5 | byte tokenization：UTF-8 编码、0–255、1 byte = 1 token、词表 256 | Mechanics | ✅ | ⬜ |
| L01-6 | character tokenization：Unicode 码点（`ord`/`chr`）、约 15 万字符、长尾字符浪费词表 | Mechanics | ✅ | ⬜ |
| L01-7 | word tokenization：正则切分（含 GPT-2 regex）、词表随语料膨胀、`UNK` 与 perplexity 问题 | Mechanics | ✅ | ⬜ |
| L01-8 | 压缩率 `compression ratio = num_bytes / num_tokens`，以及序列长度 ↔ 上下文长度/attention 二次开销 | Mechanics | ✅ | ⬜ |
| L01-9 | BPE 动机与流程：常见序列一个 token、稀有序列多个 token；训练 = 统计相邻对 → 合并最高频对；A1 要求的增强（只遍历相关 merge、special tokens、pre-tokenization、速度） | Mechanics | ✅ | ⬜ |

---

# B PyTorch 与资源账本（L02）

| # | 知识点 | 类型 | 讲解 | 掌握 |
|---|---|---|---|---|
| L02-1 | tensor 基础：shape、dtype、device，以及为什么 shape 是一切的出发点 | Mechanics | — | ⬜ |
| L02-2 | 训练四件套：参数 / 梯度 / 优化器状态 / 激活，各自占用多少显存 | Mechanics | — | ⬜ |
| L02-3 | 数值精度账本：float32 / float16 / bfloat16 / fp8 的字节数与取舍（范围 vs 精度） | Mechanics | — | ⬜ |
| L02-4 | 矩阵乘法 FLOPs：`2·m·n·p`，以及线性层、attention 各项的量级 | Mechanics | — | ⬜ |
| L02-5 | 一次前向/反向的 compute 与 memory 估算（含 `Transformers` 那张具体账） | Mechanics | — | ⬜ |
| L02-6 | MFU（model FLOPs utilization）：定义、典型数值、为什么它比“峰值 FLOPs”更有意义 | Mindset | — | ⬜ |
| L02-7 | 参数初始化：初始化尺度为什么影响能否训练 | Mechanics | — | ⬜ |
| L02-8 | pinned memory 等数据搬运开销：为什么 CPU→GPU 拷贝会成为瓶颈 | Mechanics | — | ⬜ |

---

# C 架构与超参数（L03、L04）

| # | 知识点 | 类型 | 讲解 | 掌握 |
|---|---|---|---|---|
| L03-1 | Transformer 骨架回顾：attention + MLP + 残差 + norm，token 维度如何流转 | Mechanics | — | ⬜ |
| L03-2 | 激活函数：ReLU / GeLU / SwiGLU / GeGLU 的差别与门控（gating）思路 | Mechanics | — | ⬜ |
| L03-3 | 归一化：LayerNorm vs RMSNorm；pre-norm vs post-norm 的稳定性差异 | Mechanics | — | ⬜ |
| L03-4 | 位置编码：sinusoidal / RoPE / NoPE、SWA 各自解决什么 | Mechanics | — | ⬜ |
| L03-5 | attention 变体：full / sliding window / linear；GQA、MQA 如何省推理成本 | Mechanics | — | ⬜ |
| L03-6 | 超参数选择：head dim、aspect ratio、层数与宽度的取舍、词表大小（各模型实例） | Intuition | — | ⬜ |
| L03-7 | 稳定性技巧与正则化：logit soft-capping、正则化手段、串行 vs 并行层 | Mechanics | — | ⬜ |
| L04-1 | MoE 结构：routed / active / shared experts、fine-grained ratio 的含义 | Mechanics | — | ⬜ |
| L04-2 | routing 方案：top-k、hashing、线性分配、用 RL 学路由 | Mechanics | — | ⬜ |
| L04-3 | 为什么“同 FLOPs 下更多参数更好”：稀疏激活的容量—计算解耦 | Mindset | — | ⬜ |
| L04-4 | MoE 的并行能力与代价：expert parallel、多机优势、通信复杂度 | Mechanics | — | ⬜ |
| L04-5 | MoE 训练的不稳定性与训练目标的经验性 | Intuition | — | ⬜ |
| L04-6 | MLA（multi-head latent attention）与 RoPE 的冲突，及 MTP 等多步预测思路 | Mechanics | — | ⬜ |

---

# D 系统：GPU / kernel / 并行 / 推理（L05、L06、L07、L08、L10）

| # | 知识点 | 类型 | 讲解 | 掌握 |
|---|---|---|---|---|
| L05-1 | GPU 结构：SM / SP、DRAM 与 SRAM、内存层级（仓库 : 工厂 类比） | Mechanics | — | ⬜ |
| L05-2 | 执行模型：kernel 如何被调度、为什么“数据移动”才是瓶颈 | Mechanics | — | ⬜ |
| L05-3 | arithmetic intensity（FLOPs / bytes）与 roofline model：判断 compute-bound 还是 memory-bound | Mindset | — | ⬜ |
| L05-4 | tiling：用 shared memory 复用数据，tile size 如何影响利用率与边界浪费 | Mechanics | — | ⬜ |
| L05-5 | L2 cache 的利用与“内存按 burst 读取”的影响 | Mechanics | — | ⬜ |
| L05-6 | 位宽与带宽：更少 bit = 更少搬运（与量化、精度选择的关系） | Mechanics | — | ⬜ |
| L06-1 | 用 benchmark 测 matmul：如何判断实现是否接近硬件上限 | Mechanics | — | ⬜ |
| L06-2 | Triton 编程模型：block、program id、如何表达 tile 级并行 | Mechanics | — | ⬜ |
| L06-3 | 融合（fusion）与减少中间读写为什么能提速 | Mechanics | — | ⬜ |
| L06-4 | 软硬件协同：给定 tile 大小，如何估算 shared memory 与寄存器压力 | Mechanics | — | ⬜ |
| L06-5 | 从“能跑”到“跑满”的调优顺序（先算 intensity，再选 tile） | Mindset | — | ⬜ |
| L07-1 | 集合通信原语：broadcast / scatter / gather / reduce / all-gather / reduce-scatter / all-reduce | Mechanics | — | ⬜ |
| L07-2 | `all-reduce = reduce-scatter + all-gather` 的分解与代价直觉 | Mechanics | — | ⬜ |
| L07-3 | 数据并行：梯度 all-reduce、global batch size 与梯度累积 | Mechanics | — | ⬜ |
| L07-4 | ZeRO / FSDP：把参数、梯度、优化器状态分片，换显存 | Mechanics | — | ⬜ |
| L07-5 | 张量并行：按列/按行切矩阵，attention 与 MLP 的切法与额外通信 | Mechanics | — | ⬜ |
| L07-6 | 流水线并行：按层切、micro-batch、bubble 与利用率 | Mechanics | — | ⬜ |
| L07-7 | 序列/上下文并行（ring attention）与专家并行 | Mechanics | — | ⬜ |
| L07-8 | 显存账本在并行下怎么算：激活占大头，以及“线性 scaling 显存”的组合方式 | Mindset | — | ⬜ |
| L08-1 | 通信实现：NCCL、`torch.distributed` 的基本用法与拓扑 | Mechanics | — | ⬜ |
| L08-2 | 通信与计算重叠：为什么重叠能把通信“藏起来” | Mechanics | — | ⬜ |
| L08-3 | 组合策略：ZeRO + TP + PP 同时用（以 Yi 等模型为例） | Intuition | — | ⬜ |
| L08-4 | 并行切分的选择依据：模型大小、batch、节点内/间带宽 | Mindset | — | ⬜ |
| L08-5 | 单卡 scaling 的极限，以及为什么必须走向多卡 | Mindset | — | ⬜ |
| L08-6 | 序列维度切分下 attention 的通信模式 | Mechanics | — | ⬜ |
| L10-1 | 推理负载特征：prefill（compute-bound）vs decode（memory-bound） | Mechanics | — | ⬜ |
| L10-2 | KV cache：为什么 decode 每步只生成一个 token，显存却被 KV 吃掉 | Mechanics | — | ⬜ |
| L10-3 | 降低 KV 成本的结构手段：GQA / MLA / CLA / local attention | Mechanics | — | ⬜ |
| L10-4 | 有损加速：量化（LLM.int8、AWQ 等）、剪枝、蒸馏 | Mechanics | — | ⬜ |
| L10-5 | 无损加速：speculative decoding 的“草稿 + 并行打分”为何不改变分布 | Mechanics | — | ⬜ |
| L10-6 | 动态负载处理：batching、KV 复用、调度 | Mechanics | — | ⬜ |
| L10-7 | 非 Transformer 路线：state-space models、diffusion LMs | Intuition | — | ⬜ |

---

# E Scaling laws（L09、L11）

| # | 知识点 | 分类 | 讲解 | 掌握 |
|---|---|---|---|---|
| L09-1 | 经验观察：loss 随参数量/数据量呈幂律下降 | Mechanics | — | ⬜ |
| L09-2 | Kaplan 2020 的结论与后续修正 | Mechanics | — | ⬜ |
| L09-3 | Chinchilla：`D* ≈ 20·N*`（1.4B 参数配 28B tokens）的推导与含义 | Mechanics | — | ⬜ |
| L09-4 | isoflops 曲线：固定 FLOPs 预算下如何分配 N 与 D | Mindset | — | ⬜ |
| L09-5 | 拟合方法：小模型实验 → 函数形式 → 外推，以及“上界 vs 实际 loss”的陷阱 | Mechanics | — | ⬜ |
| L09-6 | 数据受限：重复数据价值下降、如何估计可用数据量 | Mechanics | — | ⬜ |
| L09-7 | 下游指标 scaling 常常不可预测（与 loss 不同） | Intuition | — | ⬜ |
| L11-1 | Chinchilla 方法细节：给定预算如何反解最优 N、D | Mechanics | — | ⬜ |
| L11-2 | 学习率与初始化的跨尺度迁移（μP 等思路） | Mechanics | — | ⬜ |
| L11-3 | 学习率 schedule：cosine vs WSD，及其对“随时截断训练”的影响 | Mechanics | — | ⬜ |
| L11-4 | batch size scaling 与 critical batch size | Mechanics | — | ⬜ |
| L11-5 | MoE 参数规模的 isoflops 拟合（以 DeepSeek / CerebrasGPT 为例） | Mechanics | — | ⬜ |
| L11-6 | compute-to-downstream scaling：把“训练算力”换算成“下游表现” | Mindset | — | ⬜ |

---

# F 数据与评测（L12、L13、L14）

| # | 知识点 | 类型 | 讲解 | 掌握 |
|---|---|---|---|---|
| L12-1 | benchmark 分数与 “vibes”：为什么单一分数不足以说明能力 | Mindset | — | ⬜ |
| L12-2 | 知识类评测：MMLU、MMLU-Pro、GPQA、HLE 的难度阶梯与污染问题 | Mechanics | — | ⬜ |
| L12-3 | 偏好/竞技场评测：Chatbot Arena 的机制与偏差 | Mechanics | — | ⬜ |
| L12-4 | 指令遵循与生成任务评测：IFEval、AlpacaEval、WildBench、LM-as-judge | Mechanics | — | ⬜ |
| L12-5 | 代码与 agent 评测：SWEBench、CyBench、MLEBench | Mechanics | — | ⬜ |
| L12-6 | 安全评测与 train-test overlap：HarmBench、AIR-Bench、jailbreaking、数据泄漏 | Mechanics | — | ⬜ |
| L13-1 | 数据来源与配比：网页、书籍、代码、论文；能力目标决定数据构成 | Intuition | — | ⬜ |
| L13-2 | 三个阶段的数据：pretraining / mid-training / post-training 各要什么 | Mechanics | — | ⬜ |
| L13-3 | 数据量估算：按 token 预算反推需要多少原始数据 | Mindset | — | ⬜ |
| L13-4 | 模型式过滤（model-based filtering）的基本思路 | Mechanics | — | ⬜ |
| L13-5 | 版权与许可：copyright、license、fair use（§107）、ToS 的实际约束 | Intuition | — | ⬜ |
| L13-6 | 数据加工链条：HTML/PDF → 文本 → 过滤 → 去重 | Mechanics | — | ⬜ |
| L14-1 | 质量分类器：fastText、bag of words / n-grams 的基线做法 | Mechanics | — | ⬜ |
| L14-2 | 通用过滤框架与各种实例化（正负样本、阈值、迭代） | Mechanics | — | ⬜ |
| L14-3 | 有害内容过滤：分类器与规则的分工 | Mechanics | — | ⬜ |
| L14-4 | CCNet 的段落级质量打分思路 | Mechanics | — | ⬜ |
| L14-5 | 去重为什么省算力并减少记忆（memorization） | Mindset | — | ⬜ |
| L14-6 | 精确去重与近似去重：Jaccard 相似度、MinHash、Bloom filter | Mechanics | — | ⬜ |
| L14-7 | 过滤/去重的取舍：阈值过严会损失多样性 | Intuition | — | ⬜ |

---

# G 对齐（L15、L16、L17）

| # | 知识点 | 类型 | 讲解 | 掌握 |
|---|---|---|---|---|
| L15-1 | base model 与对齐目标：指令遵循、风格、安全 | Mechanics | — | ⬜ |
| L15-2 | SFT / 指令微调：数据形态、为什么少量数据就能显著改变行为 | Mechanics | — | ⬜ |
| L15-3 | 偏好数据与 reward model 的训练 | Mechanics | — | ⬜ |
| L15-4 | PPO 的演进：policy gradient 方差大 → TRPO → clip 比率 | Mechanics | — | ⬜ |
| L15-5 | DPO：不用 RL 循环、直接从偏好数据构造目标的推导要点 | Mechanics | — | ⬜ |
| L15-6 | RLHF 的副作用：长度偏差、overoptimization、mode collapse/熵坍缩 | Intuition | — | ⬜ |
| L15-7 | 安全对齐的工程问题：过度拒答（over-refusal）与部署前测试 | Intuition | — | ⬜ |
| L16-1 | RLVR 设置：可验证奖励（数学/代码）为什么适合 RL | Mechanics | — | ⬜ |
| L16-2 | GRPO 与 PPO 的关键差异：用组内 baseline 代替 value function | Mechanics | — | ⬜ |
| L16-3 | 长度归一化与长度奖励的设计（含 Dr. GRPO 的修正） | Mechanics | — | ⬜ |
| L16-4 | 完整配方：reasoning SFT → RL → 通用 SFT/RLHF 的顺序与取舍 | Intuition | — | ⬜ |
| L16-5 | 窄域 RL 能缓解 overoptimization 的原因 | Intuition | — | ⬜ |
| L16-6 | RL 训练的系统侧成本与利用率问题 | Mindset | — | ⬜ |
| L17-1 | 策略梯度与 baseline：advantage 的定义与方差 | Mechanics | — | ⬜ |
| L17-2 | 重要性采样与 off-policy 修正 | Mechanics | — | ⬜ |
| L17-3 | 从目标函数反推梯度：奖励如何进入 loss | Mechanics | — | ⬜ |
| L17-4 | 组内标准化（GRPO）与移除长度偏置后的等价形式 | Mechanics | — | ⬜ |
| L17-5 | RL 实验的可复现性问题：为什么同配方结果差异大 | Intuition | — | ⬜ |

---

# 跨讲主线（贯穿，最后统一自评）

| # | 主线 | 涉及讲次 | 掌握 |
|---|---|---|---|
| M1 | **显存账本**：参数 / 梯度 / 优化器状态 / 激活 / KV cache 各占多少，如何用分片换显存 | L02、L07、L08、L10 | ⬜ |
| M2 | **FLOPs 与算术强度**：从矩阵乘法估 FLOPs，用 intensity 判断瓶颈 | L02、L05、L06、L09 | ⬜ |
| M3 | **效率—规模权衡**：同样的预算，模型多大、数据多少、并行怎么切 | L01、L09、L11 | ⬜ |
| M4 | **数据质量 → 能力**：过滤、去重、配比如何体现在评测上 | L12、L13、L14 | ⬜ |
| M5 | **训练阶段演进**：pretrain → mid-train → SFT → RLHF → RLVR，每阶段目标与代价 | L13、L15、L16、L17 | ⬜ |

---

## 更新记录

- 2026-11-23：建立清单（条目来自 `resources/spring2025-lectures/` 的讲义标题与 PDF 大纲）。L01 已讲解 6 条（L01-4～L01-9）；掌握度均留待用户自评。
