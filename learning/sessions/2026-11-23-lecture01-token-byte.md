# 2026-11-23｜Lecture 01：token 与 byte

- 实际用时：未记录（约 30～40 分钟，用户未报具体时长）
- 对应讲次/作业：Lecture 01 — Overview, tokenization（只讲 tokenization 入门部分）
- 本次目标：能用自己的话说明 ① 文本怎么变成 token ② token 与 byte 的区别

## 完成证据

- 起点：两道直觉题（`Hello!` 是否被当作 6 个字符输入；token 是否等于单词）用户答“不知道”，按零基础开讲。
- 讲完概念后 3 道检查题：
  1. byte tokenizer 下 `🌍` 产生几个 token → 答 `4` ✅
  2. “一个 token 就是一个单词”是否正确 → 答“错误” ✅
  3. `文本 → ① → token ID 序列 → ② → 文本` → 答 `encode` / `decode` ✅
- 追问理由后：
  1. `🌍` → “byte 是一个长度为 4 的数组” ✅（措辞已校准为“UTF-8 编码后得到 4 个 byte”）
  2. token ≠ 单词 → 举“数字可能每几位会被变为一个 token”✅（讲义中的三个现象之一）

## AI 辅助摘要

- 原始文本是 Unicode 字符串；语言模型处理的是 token 序列，token 用整数（token ID）表示。tokenizer 负责 `encode`（字符串→ID 序列）与 `decode`（ID 序列→字符串），`vocabulary size` 是可能 token 的数量。
- token 不是“单词”：讲义用 GPT-2 tokenizer 展示 ① 单词与前导空格可能同属一个 token（`" world"`）② 句首与句中同一个词表示不同 ③ 数字按几位切分。
- byte 是数据单位，取值 0～255；UTF-8 下 `a` 占 1 byte，`🌍` 占 4 byte（`f0 9f 8c 8d`）。
- byte-based tokenizer 把每个 byte 变成一个 token：词表只有 256，`compression ratio = 1`，序列过长；Transformer 上下文长度有限且 attention 随序列长度二次增长，所以直接用 raw bytes 在今天的架构下计算效率差。BPE 本讲只做出口，细节留到后续。

## 用户复述与理解缺口

- **未做复述**（用户明确选择跳过）。
- 已表现出的理解：encode/decode 方向、byte tokenizer 的“1 byte = 1 token”规则、token 不等于词/数字。
- 尚待验证：能否在不看书的情况下把“为什么不直接用 byte”讲完整（复述被跳过，计划 W1 检查点未取得证据）；`vocabulary size`、`compression ratio` 未单独提问。

## 问题与处理

- 问题：无阻塞性疑问。
- 状态：—
- 下一步观察：下次开始先做 2 道针对“为什么不用 byte / 不用单词”的回忆题，补上 W1 检查点证据。

## 下一步

- 下一次最小动作：按 plan.md W1 周末任务，细读 L01 讲义 tokenization 段落（character / word tokenization 两个反例），然后做 15 分钟回忆测验。
- 建议复习日期：2026-11-24（1 天后，回忆 token/byte 与三种 tokenizer 的缺点）、2026-11-26（3 天后）、2026-11-30（7 天后）
