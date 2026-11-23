# CS336 英文术语表

只加入学习中实际遇到的词。优先记“语境含义”，不追求一次背大量词典释义。

| English | 中文 | 本文/课程中的含义 | 来源 | 复习状态 |
|---|---|---|---|---|
| language model | 语言模型 | 对 token 序列的概率分布建模（Lecture 01 原话：a language model places a probability distribution over sequences of tokens） | 预设入学词汇 / L01 | 已见，待回忆 |
| tokenizer | 分词器 | 在文本与 token ID 序列之间转换的组件 | 预设入学词汇 / L01 | 已见，待回忆 |
| token | token / 词元 | 模型处理序列时的基本单位，不一定等于一个自然语言单词 | 预设入学词汇 / L01 | 已见，可判断“token≠单词” |
| vocabulary | 词表 | token 与 ID 映射所覆盖的集合；vocabulary size 是可能 token 的数量 | 预设入学词汇 / L01 | 已见，待回忆 |
| byte | 字节 | 一个 byte 表示 0～255；UTF-8 下 `a` 占 1 byte，`🌍` 占 4 byte | 预设入学词汇 / L01 | 已理解 |
| subword | 子词 | 介于字符/字节与完整单词之间的序列单位（BPE 产出的单位属于这一类） | 预设入学词汇 | 未学 |
| Byte Pair Encoding (BPE) | 字节对编码 / BPE | 一种通过反复合并相邻对来构建分词单位的方法；细节待学习 | 预设入学词汇 | 未学 |
| end-to-end | 端到端 | 从输入到最终目标整体连接或训练；具体语境需结合原文 | 通用词汇 | 未学 |
| Unicode string | Unicode 字符串 | 原始文本的表示形式；是 tokenizer 编码的输入 | L01 | 已见 |
| encode / decode | 编码 / 解码 | encode：字符串 → token ID 序列；decode：ID 序列 → 字符串。二者应能往返（round-trip） | L01 | 已掌握 |
| token ID | token 编号 | 令牌在词表中的整数下标，模型实际处理的数值 | L01 | 已见 |
| UTF-8 | UTF-8 编码 | 最常见的 Unicode 编码方式，把字符串变成 0～255 的 byte 序列 | L01 | 已见，能举例 |
| compression ratio | 压缩率 | 讲义定义为 num_bytes / num_tokens；byte tokenizer 恒为 1，表示没有压缩 | L01 | 已见，未提问 |
| context length | 上下文长度 | Transformer 一次能处理的 token 数上限；attention 开销随序列长度二次增长 | L01 | 已见，未提问 |
| code point | 码点 | Unicode 给每个字符分配的整数编号，`ord`/`chr` 在其与字符之间互转 | L01 | 已见 |
| character-based tokenization | 字符级分词 | 每个 Unicode 字符就是一个 token；词表大且长尾字符稀有 | L01 | 已理解其缺点 |
| word-based tokenization | 词级分词 | 按词切分后映射为整数；词表随语料膨胀，未见词变 UNK | L01 | 已理解其缺点 |
| UNK token | 未登录词标记 | 训练时未出现的词被压成的特殊符号；会让 perplexity 计算受影响 | L01 | 已见，未掌握细节 |
| perplexity | 困惑度 | 语言模型的教科书评测指标；词表/UNK 处理变化会影响其可比性 | L01 | 已见，未提问 |
