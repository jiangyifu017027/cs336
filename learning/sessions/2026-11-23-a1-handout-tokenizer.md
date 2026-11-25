# 2026-11-23｜A1 handout：tokenizer 部分题意卡

- 实际用时：未记录
- 对应讲次/作业：A1 handout Section 2（§2.1–2.7）；承接 L01-9 的 BPE 讲解
- 本次目标：只读要求、不写实现；整理各 Problem 的输入/输出/约束/测试方式

## 讲解覆盖

- Section 2 全部 7 个 Problem 的题意卡：unicode1（1 分）、unicode2（3 分）、train_bpe（15 分）、train_bpe_tinystories（2 分）、train_bpe_expts_owt（2 分）、tokenizer（15 分）、tokenizer_experiments（4 分），共 42 分。
- handout 比讲义多出的字面规则：tie-breaking 取字典序更大者；special token 是硬边界且不参与 merge 统计；vocab_size 含初始 256 字节 + merges + special tokens；merges 按创建顺序排列、编码按同一顺序应用；decode 用 U+FFFD 容错（`errors='replace'`）；`encode_iterable` 流式、内存恒定。
- 未覆盖知识清单条目（本次是作业要求阅读，不是新讲次内容）；L01-9 的 “A1 增强要求” 在 handout 中对应到具体字面规则。

## AI 辅助摘要

- handout PDF 已提取为纯文本：`learning/reading/cs336_assignment1_basics.txt`（47 页，含页码标记），后续定位引用都用它。
- 术语表新增 9 词：lexicographically greater、replacement character (U+FFFD)、deliverable、serialize、throughput、lazily yield / generator、hard boundary、downscaling / debug dataset。
- 书面题（unicode1/unicode2、各实验题的回答）只整理了“问什么”，未给答案；遵守作业 AGENTS.md 与 handout 的 AI 政策。

## 用户主动反馈

无。用户仅提出“继续学习”；本次按偏好纯讲解，未出检查题，未记录掌握度。

## 问题与处理

- 问题与报错：无。
- 状态：无需处理。
- 遗留：Section 2 各题答案均需用户自己完成；Mac 副本的 A1 环境未复查（WSL2 已验证可用）。

## 下一步

- 下一次最小动作：用户自己在 Python 解释器中完成 unicode1 + unicode2 三道书面小题（不需要写实现代码），可交给 AI review 表述。
- 之后：按 handout 顺序进入 train_bpe 的实现思考（AI 只答疑、诊断、review，不写代码）。
