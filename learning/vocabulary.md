# CS336 英文术语表

只加入学习中实际遇到的词。优先记“语境含义”，不追求一次背大量词典释义。

> 最后一列只表示**是否讲过**（AI 维护）。掌握度不由 AI 判定，请在 `learning/knowledge-map.md` 自行勾选（2026-11-23 起）。

| English | 中文 | 本文/课程中的含义 | 来源 | 讲解状态 |
|---|---|---|---|---|
| language model | 语言模型 | 对 token 序列的概率分布建模（Lecture 01 原话：a language model places a probability distribution over sequences of tokens） | 预设入学词汇 / L01 | 已讲解 |
| tokenizer | 分词器 | 在文本与 token ID 序列之间转换的组件 | 预设入学词汇 / L01 | 已讲解 |
| token | token / 词元 | 模型处理序列时的基本单位，不一定等于一个自然语言单词 | 预设入学词汇 / L01 | 已讲解 |
| vocabulary | 词表 | token 与 ID 映射所覆盖的集合；vocabulary size 是可能 token 的数量 | 预设入学词汇 / L01 | 已讲解 |
| byte | 字节 | 一个 byte 表示 0～255；UTF-8 下 `a` 占 1 byte，`🌍` 占 4 byte | 预设入学词汇 / L01 | 已讲解 |
| subword | 子词 | 介于字符/字节与完整单词之间的序列单位（BPE 产出的单位属于这一类） | 预设入学词汇 | 未讲 |
| Byte Pair Encoding (BPE) | 字节对编码 / BPE | 从单字节 token 开始，反复合并最高频相邻 token 对，以构建词表和合并规则 | L01 | 已讲解 |
| merge | 合并 | BPE 中把一对相邻 token 替换成一个新 token；训练产生的 merges 在编码时按顺序使用 | L01 | 已讲解 |
| adjacent pair | 相邻对 | 当前 token 序列中紧挨着的两个 token，BPE 每轮统计的是这种对 | L01 | 已讲解 |
| pre-tokenization | 预分词 | 在运行 BPE 前先把文本切成初始片段，例如使用 GPT-2 的正则表达式 | L01 | 已讲解 |
| special token | 特殊 token | 需要单独识别并保留的标记，例如 `<|endoftext|>` | L01 | 已讲解 |
| end-to-end | 端到端 | 从输入到最终目标整体连接或训练；具体语境需结合原文 | 通用词汇 | 未讲 |
| Unicode string | Unicode 字符串 | 原始文本的表示形式；是 tokenizer 编码的输入 | L01 | 已讲解 |
| encode / decode | 编码 / 解码 | encode：字符串 → token ID 序列；decode：ID 序列 → 字符串。二者应能往返（round-trip） | L01 | 已讲解 |
| token ID | token 编号 | 令牌在词表中的整数下标，模型实际处理的数值 | L01 | 已讲解 |
| UTF-8 | UTF-8 编码 | 最常见的 Unicode 编码方式，把字符串变成 0～255 的 byte 序列 | L01 | 已讲解 |
| compression ratio | 压缩率 | 讲义定义为 num_bytes / num_tokens；byte tokenizer 恒为 1，表示没有压缩 | L01 | 已讲解 |
| context length | 上下文长度 | Transformer 一次能处理的 token 数上限；attention 开销随序列长度二次增长 | L01 | 已讲解 |
| code point | 码点 | Unicode 给每个字符分配的整数编号，`ord`/`chr` 在其与字符之间互转 | L01 | 已讲解 |
| character-based tokenization | 字符级分词 | 每个 Unicode 字符就是一个 token；词表大且长尾字符稀有 | L01 | 已讲解 |
| word-based tokenization | 词级分词 | 按词切分后映射为整数；词表随语料膨胀，未见词变 UNK | L01 | 已讲解 |
| UNK token | 未登录词标记 | 训练时未出现的词被压成的特殊符号；会让 perplexity 计算受影响 | L01 | 已讲解 |
| perplexity | 困惑度 | 语言模型的教科书评测指标；词表/UNK 处理变化会影响其可比性 | L01 | 已讲解 |
| lexicographically greater | 字典序更大 | BPE 训练频率并列时的决胜规则：取字典序更大的 pair；handout 例子 `max([("A","B"),("A","C"),("B","ZZ"),("BA","A")])` 得 `('BA','A')` | A1 handout §2.4 | 已讲解 |
| replacement character (U+FFFD) | 替换字符  | Unicode 官方替换字符；decode 遇到非法字节序列时用它占位（`errors='replace'`） | A1 handout §2.6.2 | 已讲解 |
| deliverable | 提交物 | 每道 Problem 要求交付的东西：一两句话回答 / 代码 / 序列化文件 | A1 handout 全部 Problem 框 | 已讲解 |
| serialize | 序列化 | 把 vocab、merges 等对象保存到磁盘，之后可重新加载 | A1 handout §2.5 | 已讲解 |
| throughput | 吞吐量 | 单位时间处理的量（如 bytes/s）；用来推算 tokenize 大语料的总耗时 | A1 handout §2.7 | 已讲解 |
| lazily yield / generator | 惰性产生 / 生成器 | 不一次性读入全部文本，逐段产出 token ID，使内存占用恒定 | A1 handout §2.6.1 | 已讲解 |
| hard boundary | 硬边界 | special token 把文本切成互不影响的段，BPE 合并不允许跨越 | A1 handout §2.5 | 已讲解 |
| downscaling / debug dataset | 降规模 / 调试数据集 | 先用小数据（如 TinyStories 验证集 22K 篇）跑通并暴露瓶颈，再上全量 | A1 handout §2.5 | 已讲解 |
