# 课程推荐论文（离线缓存，轻量精选版）

> 2026-11-23 在 Mac 上重建，来源为 spring2025 各讲 `lecture_NN.py` 与 `references.py` 中出现的 PDF 链接（去重后）。
> 2026-11-25 按轻量计划精选：只保留保留讲次（主线 L01–L03 + 概念线 L05/L07/L09/L10/L13/L15–L17，以及 A1/A3）会用到或直接相关的论文，共 55 篇；删除 19 篇（原 74 篇）——对应 L04/L06/L08/L11/L12/L14 与 A2/A4/A5 的论文（MoE、MMLU、MegaScale、Mixtral、Triton、MiniCPM、GPT-4 报告等），以及无保留讲次引用的其余论文。被删论文可按 arXiv 链接重新下载；旧完整索引见 WSL/D 盘旧副本。

## 主线：L01 tokenization

| 文件 | 说明 | 链接 |
|---|---|---|
| shannon_51.pdf | Shannon：英语熵与预测（语言模型的起点） | https://www.princeton.edu/~wbialek/rome/refs/shannon_51.pdf |
| bengio03a.pdf | Bengio 2003：神经概率语言模型 | https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf |
| D07-1090.pdf | Brants 2007：机器翻译中的 5-gram 语言模型（2T tokens） | https://aclanthology.org/D07-1090.pdf |
| language_models_are_unsupervised_multitask_learners.pdf | GPT-2：无监督多任务学习 | https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf |
| 2305.07185 - MEGABYTE- Predicting Million-byte Sequences with Multiscale Transformers.pdf | MEGABYTE：字节级多尺度建模 | https://arxiv.org/pdf/2305.07185.pdf |

## 主线：L02 PyTorch / 数值与优化基础

| 文件 | 说明 | 链接 |
|---|---|---|
| 1710.03740 - Mixed Precision Training.pdf | 混合精度训练 | https://arxiv.org/pdf/1710.03740.pdf |
| 2209.05433 - FP8 Formats for Deep Learning.pdf | FP8 数值格式 | https://arxiv.org/pdf/2209.05433.pdf |
| 2310.18313 - FP8-LM- Training FP8 Large Language Models.pdf | FP8-LM：FP8 训练大模型 | https://arxiv.org/pdf/2310.18313.pdf |
| duchi11a.pdf | AdaGrad：自适应梯度（优化器谱系） | https://www.jmlr.org/papers/volume12/duchi11a/duchi11a.pdf |
| glorot10a.pdf | Xavier/Glorot 初始化 | https://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf |
| transformers.pdf | Thickstun：Transformers 基础讲义 | https://johnthickstun.com/docs/transformers.pdf |

## 主线：L03 架构 + A1 训练组件

| 文件 | 说明 | 链接 |
|---|---|---|
| 1706.03762 - Attention Is All You Need.pdf | Transformer 原始论文 | https://arxiv.org/pdf/1706.03762.pdf |
| 1409.3215 - Sequence to Sequence Learning with Neural Networks.pdf | seq2seq（注意力机制的前史） | https://arxiv.org/pdf/1409.3215.pdf |
| 1409.0473 - Neural Machine Translation by Jointly Learning to Align and Translate.pdf | Bahdanau 注意力 | https://arxiv.org/pdf/1409.0473.pdf |
| 1607.06450 - Layer Normalization.pdf | LayerNorm | https://arxiv.org/pdf/1607.06450.pdf |
| 2002.04745 - On Layer Normalization in the Transformer Architecture.pdf | pre-norm vs post-norm | https://arxiv.org/pdf/2002.04745.pdf |
| 2002.05202 - GLU Variants Improve Transformer.pdf | SwiGLU 激活 | https://arxiv.org/pdf/2002.05202.pdf |
| 2104.09864 - RoFormer- Enhanced Transformer with Rotary Position Embedding.pdf | RoPE 位置编码 | https://arxiv.org/pdf/2104.09864.pdf |
| 1904.10509 - Generating Long Sequences with Sparse Transformers.pdf | Sparse Transformer（稀疏注意力） | https://arxiv.org/pdf/1904.10509.pdf |
| 2004.05150 - Longformer- The Long-Document Transformer.pdf | Longformer（滑窗注意力） | https://arxiv.org/pdf/2004.05150.pdf |
| 1412.6980 - Adam- A Method for Stochastic Optimization.pdf | Adam | https://arxiv.org/pdf/1412.6980.pdf |
| 1711.05101 - Decoupled Weight Decay Regularization.pdf | AdamW（A1 优化器） | https://arxiv.org/pdf/1711.05101.pdf |
| 1608.03983 - SGDR- Stochastic Gradient Descent with Warm Restarts.pdf | 余弦学习率调度（A1） | https://arxiv.org/pdf/1608.03983.pdf |
| 1910.10683 - Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer.pdf | T5（编码器-解码器与 C4） | https://arxiv.org/pdf/1910.10683.pdf |
| 2204.02311 - PaLM- Scaling Language Modeling with Pathways.pdf | PaLM（架构细节与 MFU） | https://arxiv.org/pdf/2204.02311.pdf |
| 2204.06745 - GPT-NeoX-20B- An Open-Source Autoregressive Language Model.pdf | GPT-NeoX-20B（并行 attention/FF、RoPE 实践） | https://arxiv.org/pdf/2204.06745.pdf |
| 2403.08295 - Gemma- Open Models Based on Gemini Research and Technology.pdf | Gemma（MQA/RoPE/GeGLU/RMSNorm） | https://arxiv.org/pdf/2403.08295.pdf |
| 2310.06825 - Mistral 7B.pdf | Mistral 7B（GQA、滑窗注意力） | https://arxiv.org/pdf/2310.06825.pdf |

## 概念线：L05 GPUs

| 文件 | 说明 | 链接 |
|---|---|---|
| nvidia-a100-datasheet-us-nvidia-1758950-r4-web.pdf | A100 官方规格（内存层级/算力） | https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet-us-nvidia-1758950-r4-web.pdf |
| osdi22-yu.pdf | FlashAttention：IO 感知 attention（L05/L10 均引用） | https://www.usenix.org/system/files/osdi22-yu.pdf |
| 2412.19437 - DeepSeek-V3 Technical Report.pdf | DeepSeek-V3（FP8 训练与现代系统实践） | https://arxiv.org/pdf/2412.19437.pdf |

## 概念线：L07 并行基础

| 文件 | 说明 | 链接 |
|---|---|---|
| 1909.08053 - Megatron-LM- Training Multi-Billion Parameter Language Models Using Model Parallelism.pdf | Megatron-LM：张量并行 | https://arxiv.org/pdf/1909.08053.pdf |
| 2104.04473 - Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM.pdf | Megatron：TP/PP/DP 组合与 MFU | https://arxiv.org/pdf/2104.04473.pdf |
| 1811.06965 - GPipe- Efficient Training of Giant Neural Networks using Pipeline Parallelism.pdf | GPipe：流水线并行 | https://arxiv.org/pdf/1811.06965.pdf |

## 概念线：L09 scaling laws

| 文件 | 说明 | 链接 |
|---|---|---|
| 2001.08361 - Scaling Laws for Neural Language Models.pdf | Kaplan 幂律 | https://arxiv.org/pdf/2001.08361.pdf |
| 2203.15556 - Training Compute-Optimal Large Language Models.pdf | Chinchilla：计算最优配比 | https://arxiv.org/pdf/2203.15556.pdf |
| 2005.14165 - Language Models are Few-Shot Learners.pdf | GPT-3 | https://arxiv.org/pdf/2005.14165.pdf |
| 1812.06162 - An Empirical Model of Large-Batch Training.pdf | critical batch size | https://arxiv.org/pdf/1812.06162.pdf |
| 2401.02954 - DeepSeek LLM- Scaling Open-Source Language Models with Longtermism.pdf | DeepSeek-LLM：非嵌入 FLOPs 的 IsoFLOP | https://arxiv.org/pdf/2401.02954.pdf |

## 概念线：L10 推理

| 文件 | 说明 | 链接 |
|---|---|---|
| 2309.06180 - Efficient Memory Management for Large Language Model Serving with PagedAttention.pdf | vLLM：PagedAttention | https://arxiv.org/pdf/2309.06180.pdf |
| 2305.13245 - GQA- Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints.pdf | GQA/MQA（推理加速） | https://arxiv.org/pdf/2305.13245.pdf |

（FlashAttention、FP8-LM、Longformer 见 L05/L02/L03 分组。）

## 概念线：L13 数据

| 文件 | 说明 | 链接 |
|---|---|---|
| 2101.00027 - The Pile- An 800GB Dataset of Diverse Text for Language Modeling.pdf | The Pile | https://arxiv.org/pdf/2101.00027.pdf |
| 2112.11446 - Scaling Language Models- Methods, Analysis & Insights from Training Gopher.pdf | Gopher（含 MassiveText 数据配比） | https://arxiv.org/pdf/2112.11446.pdf |
| 2302.13971 - LLaMA- Open and Efficient Foundation Language Models.pdf | LLaMA（开放数据配方） | https://arxiv.org/pdf/2302.13971.pdf |
| 2402.00838 - OLMo- Accelerating the Science of Language Models.pdf | OLMo/Dolma（全开放数据与模型） | https://arxiv.org/pdf/2402.00838.pdf |
| 2502.02737 - SmolLM2- When Smol Goes Big -- Data-Centric Training of a Small Language Model.pdf | SmolLM2（数据为中心的小模型） | https://arxiv.org/pdf/2502.02737.pdf |
| 2303.15715 - Foundation Models and Fair Use.pdf | 版权与合理使用 | https://arxiv.org/pdf/2303.15715.pdf |

## 概念线：L15–L17 对齐

| 文件 | 说明 | 链接 |
|---|---|---|
| 2203.02155 - Training language models to follow instructions with human feedback.pdf | InstructGPT：RLHF | https://arxiv.org/pdf/2203.02155.pdf |
| 1707.06347 - Proximal Policy Optimization Algorithms.pdf | PPO | https://arxiv.org/pdf/1707.06347.pdf |
| 2305.18290 - Direct Preference Optimization- Your Language Model is Secretly a Reward Model.pdf | DPO | https://arxiv.org/pdf/2305.18290.pdf |
| 2305.11206 - LIMA- Less Is More for Alignment.pdf | LIMA：少数据对齐 | https://arxiv.org/pdf/2305.11206.pdf |
| 2307.09288 - Llama 2- Open Foundation and Fine-Tuned Chat Models.pdf | Llama 2（SFT/RLHF 与安全） | https://arxiv.org/pdf/2307.09288.pdf |
| 2402.03300 - DeepSeekMath- Pushing the Limits of Mathematical Reasoning in Open Language Models.pdf | DeepSeekMath：GRPO 出处 | https://arxiv.org/pdf/2402.03300.pdf |
| 2501.12948 - DeepSeek-R1- Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.pdf | DeepSeek-R1：推理 RL | https://arxiv.org/pdf/2501.12948.pdf |
| 2501.12599 - Kimi k1.5- Scaling Reinforcement Learning with LLMs.pdf | Kimi k1.5 | https://arxiv.org/pdf/2501.12599.pdf |
