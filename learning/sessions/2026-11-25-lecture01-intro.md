# 2026-11-25 L01：课程定位、效率框架、LM 演进（L01-1～3）

## 背景

- 用户要求"讲解 A1 相关的知识，使用相关课程材料，不要参杂你的理解"。
- 模块 A 中 L01-4～9 已于 2026-11-23 讲过，本次补讲剩余的 L01-1～3（背景了解级条目）。

## 讲解内容（依据 `resources/spring2025-lectures/lecture_01.py`）

- **L01-1 课程定位**：研究者与底层技术脱节 → understanding via building；语言模型工业化（1.8T 参数传闻、$100M、20 万 H100、Stargate）；More is different（FLOPs 比例随规模变、行为涌现）；三类知识 Mechanics / Mindset / Intuitions，前两者可迁移、直觉部分不可迁移。
- **L01-2 效率框架**：bitter lesson 的正确解读是"能规模化的算法"；`accuracy = efficiency × resources`；ImageNet 2012–2019 算法效率 44×；framing = 给定 compute+data 预算最大化效率；课程示例：Common Crawl + 32 张 H100 两周；今天 compute-constrained、明天 data-constrained。
- **L01-3 LM 演进**：pre-neural（Shannon、n-gram）→ neural ingredients（Bengio 2003 → Transformer 2017 → 模型并行）→ early foundation models（ELMo/BERT/T5）→ embracing scaling 走向封闭（GPT-2/3、PaLM、Chinchilla）→ open models（Pile/GPT-J、OPT、BLOOM、Llama、Qwen、DeepSeek、OLMo 2）；开放三层次 closed / open-weight / open-source。
- 附讲义对 A1 的定位：实现 BPE tokenizer + Transformer + cross-entropy + AdamW + 训练循环，在 TinyStories / OpenWebText 上训练，H100 90 分钟预算比 perplexity。

## 方式

- 纯讲解，未提问、未出检查题、未要求复述；内容全部取自讲义原文，未加补充。

## 结果

- `learning/knowledge-map.md`：L01-1、L01-2、L01-3 标记"已讲解"（模块 A 共 9 条全部讲完）；掌握度留待用户自评。
- `learning/progress.md`：L01 行更新为"L01-1～9 已全部讲解"。

## 下一步（不变）

- 用户独立完成 unicode1/unicode2 六个小问（handout §2.1–2.2 前置概念已讲解），可交 AI review。
- 之后进入 BPE 训练/编码代码题；模型与训练部分等 L02/L03。
