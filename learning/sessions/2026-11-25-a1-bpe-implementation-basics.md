# 2026-11-25｜A1：BPE tokenizer 实现的基础知识

- 对应讲次/作业：A1 handout §2.3–2.7；承接 L01-9（BPE 训练与使用）
- 用户请求：「实现 BPE tokenizer；讲解这块的基础知识」
- 边界：按作业 AGENTS.md，AI 不写实现代码/伪代码；本次只讲 handout 与讲义中已有的知识，实现由用户完成

## 讲解覆盖

- §2.3 subword 定位：byte-level 序列太长、word-level 有 OOV；subword 用词表大小换压缩；byte-level BPE 兼顾两者。
- §2.4 训练三步：词表初始化（256 字节）→ pre-tokenization（GPT-2 正则、`finditer`、计数加权）→ 迭代合并最高频相邻对（字典序更大者破平局）；special tokens 硬边界、入词表、不参与统计；handout 完整例子（low/lower/widest/newest，6 次 merge 后 `newest → [ne, west]`）。
- §2.6 编码/解码：编码镜像训练（预分词 → 按创建顺序应用 merges，handout 例子 `'the cat ate' → [9,7,1,5,10,3]`）；解码查表拼接 + `errors='replace'`（U+FFFD）；`encode_iterable` 惰性产出、token 不跨块。
- §2.5 handout 明示的效率手段：multiprocessing 并行预分词（chunk 边界对齐 special token，starter code 可原样用）、预分词前剥离 special tokens（`re.split` + `re.escape`）、合并步骤建索引增量更新（不可并行）、cProfile/py-spy 性能分析、downscaling 调试数据集。
- 交付接口与测试：`train_bpe(input_path, vocab_size, special_tokens) -> (vocab: dict[int,bytes], merges: list[tuple[bytes,bytes]])` + adapter `run_train_bpe`；`Tokenizer` 类五接口 + adapter `get_tokenizer`；资源限制与实验题清单（只列问题，未给答案）。

## 方式

- 纯讲解，未提问、未出检查题；内容全部取自讲义与 handout，无【补充】发挥；未给任何实现方案。

## 结果

- `learning/vocabulary.md` 新增 7 词：OOV、pre-token、multiprocessing/parallelize、chunk boundary、incremental update、profiling（含原已记的 downscaling 标注无变化）。
- `learning/progress.md`：当前位置更新为"BPE 实现基础知识已讲解，待用户实现"；待办清单按 handout 精确题名列出。
- knowledge-map 无新增"已讲解"条目（本次属作业知识整合，L01-9 已于 11-23 标记）。

## 下一步

- 用户独立实现 train_bpe 并跑 `tests/test_train_bpe.py`；之后 Tokenizer 类与 `tests/test_tokenizer.py`。
- unicode1/unicode2 六小问可并行完成。
- 卡顿时 AI 只答疑、解释报错、review 代码，不写代码。
