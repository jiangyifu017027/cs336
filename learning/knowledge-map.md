# CS336 课程掌握进度表

> 本文件是**唯一的课程进度表**：按模块列出每个知识点及其重点，你自己勾选掌握度。
> AI 只维护"讲解"列（讲过哪几条），不替你判掌握、不提问（2026-11-25 起）。
> 范围 = 轻量计划：主线 L01–L03 + A1；概念线 L05/L07/L09/L10/L13/L15–L17；可选 A3。其余讲次不在本表。

## 怎么勾选

| 列 | 谁填 | 含义 |
|---|---|---|
| 讲解 | AI | `✅` 已按讲义讲过；`—` 还没讲 |
| 掌握 | 你 | `⬜` 未学 / `🟡` 有印象 / `🟢` 能自己解释 / `🔵` 能独立使用（作业或实验验证过） |

- 条目编号形如 `L03-4`，可以直接对 AI 说"讲 L03-4"。
- 主线（L01–L03 + A1）建议学到 🔵；概念线学到 🟢 即可。
- 每次学完只改"掌握"列，真正的验证在 A1 作业里。

## 总览

| 模块 | 深度 | 内容 | 条目数 |
|---|---|---|---|
| A 基础与分词（L01） | 主线 | 语言模型流水线、token/byte、BPE | 9 |
| B PyTorch 与资源账本（L02） | 主线 | tensor、显存、FLOPs、精度、初始化 | 8 |
| C 架构与超参数（L03） | 主线 | Transformer、RMSNorm、SwiGLU、RoPE、attention 变体 | 7 |
| A1 实践 | 主线作业 | 从零实现并训练小 LM | 12 |
| D GPU（L05） | 概念 | 内存层级、roofline、tiling | 6 |
| E 并行基础（L07） | 概念 | 集合通信、DP/TP/PP、ZeRO | 8 |
| F Scaling laws（L09） | 概念 | 幂律、Chinchilla、isoflops | 7 |
| G 推理（L10） | 概念 | prefill/decode、KV cache、量化、投机解码 | 7 |
| H 数据（L13） | 概念 | 数据来源与配比、过滤、版权 | 6 |
| I 对齐（L15–L17） | 概念 | SFT/RLHF/DPO、GRPO、策略梯度 | 18 |
| 跨讲主线 M1–M4 | 综合 | 显存账本、FLOPs、效率权衡、训练阶段 | 4 |
| A3 实践（可选） | 可选作业 | 本地 scaling 小实验 | 3 |

---

# A 基础与分词（L01，主线）

**本模块重点**：理解"模型吃的是 token ID 而不是文字"，以及为什么 BPE 是当前主流。核心是 **L01-5/6（byte 与字符的区别）、L01-8（压缩率）、L01-9（BPE 训练流程）**——这四条直接对应 A1 的 tokenizer 实现。L01-1～3 是课程定位与历史背景，了解即可。

| # | 知识点（重点） | 讲解 | 掌握 |
|---|---|---|---|
| L01-1 | 课程定位：Mechanics / Mindset / Intuitions 三类知识，哪些能从小模型迁移到前沿 | ✅ | ⬜ |
| L01-2 | 效率框架：`accuracy = efficiency × resources`，给定 compute+data 预算下最大化效率 | ✅ | ⬜ |
| L01-3 | 语言模型演进：pre-neural → neural → foundation models → scaling → 开放模型 | ✅ | ⬜ |
| L01-4 | tokenizer 接口：`encode`/`decode` 往返、`vocabulary size`；模型输入是 token ID | ✅ | ⬜ |
| L01-5 | **byte tokenization**：UTF-8 编码、0–255、1 byte = 1 token、词表 256 | ✅ | ⬜ |
| L01-6 | **character tokenization**：Unicode 码点（`ord`/`chr`）、约 15 万字符、长尾浪费词表 | ✅ | ⬜ |
| L01-7 | word tokenization：正则切分、词表随语料膨胀、`UNK` 与 perplexity 问题 | ✅ | ⬜ |
| L01-8 | **压缩率** `num_bytes / num_tokens`；序列长度 ↔ 上下文长度与 attention 二次开销 | ✅ | ⬜ |
| L01-9 | **BPE**：常见序列一个 token；训练 = 统计相邻对 → 合并最高频对；A1 要求的增强（special tokens、pre-tokenization、速度） | ✅ | ⬜ |

# B PyTorch 与资源账本（L02，主线）

**本模块重点**：会算两笔账——**FLOPs（L02-4/5）和显存（L02-2/3）**。这是"为什么这个模型能/不能在这张卡上训练"的基础，也是 A1 训练部分的前置。你的 PyTorch 起点较弱，L02-1（tensor/shape/dtype/device）必须先过关，其余都建立在它上面。

| # | 知识点（重点） | 讲解 | 掌握 |
|---|---|---|---|
| L02-1 | **tensor 基础**：shape、dtype、device，为什么 shape 是一切的出发点 | — | ⬜ |
| L02-2 | **训练四件套**：参数 / 梯度 / 优化器状态 / 激活，各占多少显存 | — | ⬜ |
| L02-3 | **数值精度**：float32 / float16 / bfloat16 / fp8 的字节数与取舍 | — | ⬜ |
| L02-4 | **矩阵乘法 FLOPs**：`2·m·n·p`，线性层与 attention 各项的量级 | — | ⬜ |
| L02-5 | 一次前向/反向的 compute 与 memory 估算（含 Transformer 那张具体账） | — | ⬜ |
| L02-6 | MFU：定义、典型数值、为什么比"峰值 FLOPs"更有意义 | — | ⬜ |
| L02-7 | 参数初始化：初始化尺度为什么影响能否训练 | — | ⬜ |
| L02-8 | 数据搬运开销：为什么 CPU→GPU 拷贝会成为瓶颈 | — | ⬜ |

# C 架构与超参数（L03，主线）

**本模块重点**：现代 LLM 的"标准配方"——**RMSNorm（L03-3）、SwiGLU（L03-2）、RoPE（L03-4）、pre-norm、attention 变体（L03-5）**。A1 要实现的每个模块都对应这里的一条；L03-1（整体骨架与 shape 流转）是把它们串起来的主线，建议学到能画出整张图。

| # | 知识点（重点） | 讲解 | 掌握 |
|---|---|---|---|
| L03-1 | **Transformer 骨架**：attention + MLP + 残差 + norm，token 维度如何流转 | — | ⬜ |
| L03-2 | **激活函数**：ReLU / GeLU / SwiGLU / GeGLU 的差别与门控思路 | — | ⬜ |
| L03-3 | **归一化**：LayerNorm vs RMSNorm；pre-norm vs post-norm 的稳定性差异 | — | ⬜ |
| L03-4 | **位置编码**：sinusoidal / RoPE / NoPE 各自解决什么 | — | ⬜ |
| L03-5 | **attention 变体**：full / sliding window / linear；GQA、MQA 如何省推理成本 | — | ⬜ |
| L03-6 | 超参数选择：head dim、aspect ratio、层数与宽度、词表大小 | — | ⬜ |
| L03-7 | 稳定性技巧：logit soft-capping、正则化、串行 vs 并行层 | — | ⬜ |

# A1 实践（主线作业）

**本模块重点**：把上面三讲变成能跑的代码。这是整门课的核心产出——**自己写的、能在 TinyStories 上训练的小语言模型**。tokenizer 部分（A1-1～6）先做，模型部分（A1-7～9）等 L02/L03 学完，训练部分（A1-10～12）最后。每题的要求以 handout 为准；下面按功能块列出，方便勾选。

| # | 任务（重点） | 状态 |
|---|---|---|
| A1-1 | Unicode 书面题（unicode1/unicode2 六小问）：理解 UTF 编码与多字节字符 | ⬜ 待独立完成 |
| A1-2 | BPE 训练：统计相邻对、合并、保存词表与 merge 规则 | ⬜ |
| A1-3 | BPE encode/decode：与训练结果一致的编码与解码 | ⬜ |
| A1-4 | special tokens 处理 | ⬜ |
| A1-5 | 流式编码（大文件分块处理） | ⬜ |
| A1-6 | tokenizer 相关测试全部通过 | ⬜ |
| A1-7 | 基础模块：Linear、Embedding、RMSNorm、SiLU/SwiGLU | ⬜ |
| A1-8 | attention 与 RoPE、Transformer block、完整 LM | ⬜ |
| A1-9 | `test_model.py` 通过 | ⬜ |
| A1-10 | 训练组件：softmax、交叉熵、梯度裁剪、AdamW、余弦学习率、batch 采样、checkpoint | ⬜ |
| A1-11 | 训练循环跑通，TinyStories 小跑 | ⬜ |
| A1-12 | A1 全部单测通过，完成一次训练实验记录 | ⬜ |

---

# D GPU（L05，概念线）

**本模块重点**：一句话——**"慢的原因通常是搬数据，不是算数据"**。抓住 L05-3（roofline / arithmetic intensity）这条主线，就能判断一段代码是 compute-bound 还是 memory-bound；L05-1/2 是理解它的硬件基础。学到能解释概念即可，不需要写 kernel。

| # | 知识点（重点） | 讲解 | 掌握 |
|---|---|---|---|
| L05-1 | GPU 结构：SM / SP、DRAM 与 SRAM、内存层级 | — | ⬜ |
| L05-2 | 执行模型：kernel 调度、为什么"数据移动"才是瓶颈 | — | ⬜ |
| L05-3 | **arithmetic intensity 与 roofline**：判断 compute-bound / memory-bound | — | ⬜ |
| L05-4 | tiling：用 shared memory 复用数据，tile size 的影响 | — | ⬜ |
| L05-5 | L2 cache 与内存 burst 读取的影响 | — | ⬜ |
| L05-6 | 位宽与带宽：更少 bit = 更少搬运（与量化的关系） | — | ⬜ |

# E 并行基础（L07，概念线）

**本模块重点**：四种并行各自"切什么、在哪里通信"——**数据并行切 batch（L07-3）、张量并行切矩阵（L07-5）、流水线切层（L07-6）、ZeRO/FSDP 切状态（L07-4）**。先掌握 L07-1/2 的通信原语，后面都是它们的组合。

| # | 知识点（重点） | 讲解 | 掌握 |
|---|---|---|---|
| L07-1 | **集合通信原语**：broadcast / gather / reduce / all-gather / reduce-scatter / all-reduce | — | ⬜ |
| L07-2 | `all-reduce = reduce-scatter + all-gather` 的分解与代价直觉 | — | ⬜ |
| L07-3 | **数据并行**：梯度 all-reduce、global batch size 与梯度累积 | — | ⬜ |
| L07-4 | **ZeRO / FSDP**：参数、梯度、优化器状态分片换显存 | — | ⬜ |
| L07-5 | **张量并行**：按列/按行切矩阵，attention 与 MLP 的切法与额外通信 | — | ⬜ |
| L07-6 | 流水线并行：按层切、micro-batch、bubble 与利用率 | — | ⬜ |
| L07-7 | 序列/上下文并行（ring attention）与专家并行 | — | ⬜ |
| L07-8 | 并行下的显存账本：激活占大头，组合策略的取舍 | — | ⬜ |

# F Scaling laws（L09，概念线）

**本模块重点**：**Chinchilla 的"模型与数据同步放大"（L09-3）和 isoflops 曲线（L09-4）**——给定算力预算怎么分配模型大小和 token 数。L09-5（小实验拟合外推）是可选 A3 作业的理论基础。

| # | 知识点（重点） | 讲解 | 掌握 |
|---|---|---|---|
| L09-1 | 经验观察：loss 随参数量/数据量呈幂律下降 | — | ⬜ |
| L09-2 | Kaplan 2020 的结论与后续修正 | — | ⬜ |
| L09-3 | **Chinchilla**：`D* ≈ 20·N*` 的推导与含义 | — | ⬜ |
| L09-4 | **isoflops 曲线**：固定 FLOPs 预算下如何分配 N 与 D | — | ⬜ |
| L09-5 | 拟合方法：小模型实验 → 函数形式 → 外推，及"上界 vs 实际 loss"的陷阱 | — | ⬜ |
| L09-6 | 数据受限：重复数据价值下降、如何估计可用数据量 | — | ⬜ |
| L09-7 | 下游指标 scaling 常常不可预测（与 loss 不同） | — | ⬜ |

# G 推理（L10，概念线）

**本模块重点**：**prefill 与 decode 的不同瓶颈（L10-1）+ KV cache（L10-2）**——这两条解释了为什么推理优化和训练优化是两回事。其余条目（GQA、量化、投机解码）都是围绕"省 KV、少搬数据"的展开。

| # | 知识点（重点） | 讲解 | 掌握 |
|---|---|---|---|
| L10-1 | **prefill（compute-bound）vs decode（memory-bound）** | — | ⬜ |
| L10-2 | **KV cache**：decode 每步只生成一个 token，显存却被 KV 吃掉 | — | ⬜ |
| L10-3 | 降低 KV 成本的结构手段：GQA / MLA / local attention | — | ⬜ |
| L10-4 | 有损加速：量化、剪枝、蒸馏 | — | ⬜ |
| L10-5 | 无损加速：speculative decoding 的"草稿 + 并行打分" | — | ⬜ |
| L10-6 | 动态负载处理：batching、KV 复用、调度 | — | ⬜ |
| L10-7 | 非 Transformer 路线：state-space models、diffusion LMs | — | ⬜ |

# H 数据（L13，概念线）

**本模块重点**：**"能力目标决定数据构成"（L13-1）和三个训练阶段的数据差异（L13-2）**。L13-6 的加工链条（HTML → 文本 → 过滤 → 去重）给你一个数据管线的整体图景；版权（L13-5）了解基本约束即可。

| # | 知识点（重点） | 讲解 | 掌握 |
|---|---|---|---|
| L13-1 | **数据来源与配比**：网页、书籍、代码、论文；能力目标决定数据构成 | — | ⬜ |
| L13-2 | **三个阶段的数据**：pretraining / mid-training / post-training 各要什么 | — | ⬜ |
| L13-3 | 数据量估算：按 token 预算反推需要多少原始数据 | — | ⬜ |
| L13-4 | 模型式过滤（model-based filtering）的基本思路 | — | ⬜ |
| L13-5 | 版权与许可：copyright、license、fair use、ToS 的实际约束 | — | ⬜ |
| L13-6 | **数据加工链条**：HTML/PDF → 文本 → 过滤 → 去重 | — | ⬜ |

# I 对齐（L15–L17，概念线）

**本模块重点**：L15 抓 **SFT（L15-2）→ RLHF/PPO（L15-3/4）→ DPO（L15-5）** 这条演进线；L16/17 抓 **GRPO 与 PPO 的差异——用组内 baseline 代替 value function（L16-2、L17-4）**，这是当前推理模型训练的核心。策略梯度基础（L17-1/3）是理解后面一切的前提。

## L15 SFT / RLHF

| # | 知识点（重点） | 讲解 | 掌握 |
|---|---|---|---|
| L15-1 | base model 与对齐目标：指令遵循、风格、安全 | — | ⬜ |
| L15-2 | **SFT**：数据形态、为什么少量数据就能显著改变行为 | — | ⬜ |
| L15-3 | 偏好数据与 reward model 的训练 | — | ⬜ |
| L15-4 | **PPO**：policy gradient 方差大 → TRPO → clip 比率 | — | ⬜ |
| L15-5 | **DPO**：不用 RL 循环、直接从偏好数据构造目标 | — | ⬜ |
| L15-6 | RLHF 的副作用：长度偏差、overoptimization、熵坍缩 | — | ⬜ |
| L15-7 | 安全对齐的工程问题：过度拒答与部署前测试 | — | ⬜ |

## L16 RLVR / GRPO

| # | 知识点（重点） | 讲解 | 掌握 |
|---|---|---|---|
| L16-1 | RLVR 设置：可验证奖励（数学/代码）为什么适合 RL | — | ⬜ |
| L16-2 | **GRPO 与 PPO 的关键差异**：组内 baseline 代替 value function | — | ⬜ |
| L16-3 | 长度归一化与长度奖励的设计（含 Dr. GRPO 的修正） | — | ⬜ |
| L16-4 | 完整配方：reasoning SFT → RL → 通用 SFT/RLHF 的顺序 | — | ⬜ |
| L16-5 | 窄域 RL 能缓解 overoptimization 的原因 | — | ⬜ |
| L16-6 | RL 训练的系统侧成本与利用率问题 | — | ⬜ |

## L17 策略梯度机制

| # | 知识点（重点） | 讲解 | 掌握 |
|---|---|---|---|
| L17-1 | **策略梯度与 baseline**：advantage 的定义与方差 | — | ⬜ |
| L17-2 | 重要性采样与 off-policy 修正 | — | ⬜ |
| L17-3 | 从目标函数反推梯度：奖励如何进入 loss | — | ⬜ |
| L17-4 | **组内标准化（GRPO）**与移除长度偏置后的等价形式 | — | ⬜ |
| L17-5 | RL 实验的可复现性问题：为什么同配方结果差异大 | — | ⬜ |

---

# 跨讲主线（最后统一自评）

| # | 主线 | 涉及讲次 | 掌握 |
|---|---|---|---|
| M1 | **显存账本**：参数 / 梯度 / 优化器状态 / 激活 / KV cache 各占多少，如何用分片换显存 | L02、L07、L10 | ⬜ |
| M2 | **FLOPs 与算术强度**：从矩阵乘法估 FLOPs，用 intensity 判断瓶颈 | L02、L05、L09 | ⬜ |
| M3 | **效率—规模权衡**：同样的预算，模型多大、数据多少、并行怎么切 | L01、L09 | ⬜ |
| M4 | **训练阶段演进**：pretrain → mid-train → SFT → RLHF → RLVR，每阶段目标与代价 | L13、L15、L16、L17 | ⬜ |

# A3 实践（可选轻量版）

**说明**：主线走完后由你决定要不要做。只做本地小规模实验，跳过 API 预测提交。

| # | 任务 | 状态 |
|---|---|---|
| A3-1 | 设计并跑一组不同规模/超参数的本地训练实验，收集 loss | ⬜ |
| A3-2 | 拟合 scaling law（isoflops / 幂律） | ⬜ |
| A3-3 | 外推更大规模的配置与 loss，写简短分析 | ⬜ |

---

## 更新记录

- 2026-11-25：改为唯一课程进度表。范围限定为轻量计划（主线 L01–L03 + A1；概念线 L05/L07/L09/L10/L13/L15–L17；可选 A3），删除不在计划内的讲次条目；每个模块补充"本模块重点"说明；A1/A3 增加实践勾选清单。时间管理式的学习计划（plan.md）已删除。
- 2026-11-25：L01 补讲 L01-1～L01-3（课程定位、效率框架、LM 演进），模块 A 全部 9 条均已讲解；掌握度留待用户自评。
- 2026-11-23：建立清单。L01 已讲解 6 条（L01-4～L01-9）；掌握度均留待用户自评。
