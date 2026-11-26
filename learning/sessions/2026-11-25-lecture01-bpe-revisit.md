# 2026-11-25 L01 复讲：BPE（用户主动要求）

## 背景

用户进入 train_bpe 实现阶段，主动要求重点讲解 BPE。这是 L01-9 的第二次讲解（首次见 2026-11-23 记录），按讲义 `lecture_01.py` 顺序完整复讲。

## 覆盖内容（对应 knowledge-map）

- L01-9 BPE：动机（byte/word/character tokenizer 的硬伤）→ 训练三步循环（统计相邻对 → 选最高频 → 合并）→ 手算讲义例子 `"the cat in the hat"`（3 轮 merge：th → the → "the "，18 token → 13）→ encode 按 merges 顺序重放 / decode 查 vocab 拼字节 → A1 四项增强要求（只处理出现的 merges、special tokens、pre-tokenization、速度）。
- 强调点：encode 是重放训练顺序而非重新统计；vocab 新条目是确定的字节拼接；byte 级 256 token 永存所以无 UNK；平局行为以 handout 为准（讲义代码只是取先扫描到的）。
- 关联 L01-8 压缩率。

## 状态

- 纯讲解，未提问、未出检查题；掌握度留待用户自评。
- 下一步不变：用户独立实现 train_bpe，通过 `tests/test_train_bpe.py`。
