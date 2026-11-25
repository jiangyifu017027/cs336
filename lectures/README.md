# CS336 讲义索引与笔记（Spring 2025）

> 本目录 2026-11-23 在 Mac 上重建（原目录在 WSL/D 盘，未入 git）。
> 2026-11-25 按轻量计划清理：L04/L06/L08/L11/L12/L14 的笔记与本地讲义已删除，只保留主线（01–03）与概念线（05、07、09、10、13、15–17）共 11 讲。
> 每讲一个笔记文件，学习时按 cs336-study / cs336-review 流程填写。

## 资料怎么用

- **可执行讲义**：`resources/spring2025-lectures/lecture_NN.py`，配合 trace 在浏览器看：
  ```bash
  ./scripts/serve_lectures.sh
  # http://localhost:8000/spring2025-lectures/index.html?trace=var/traces/lecture_01.json
  ```
- **PDF 幻灯片**：`resources/spring2025-lectures/nonexecutable/` 直接打开。
- **推荐论文**：`resources/papers/`（含 README 索引）。

## 讲次一览

| 讲 | 主题 | 深度 | 资料形式 | 笔记 |
|---|---|---|---|---|
| 01 | Overview, tokenization | 主线 | 可执行讲义 | [笔记](lecture_01.md) |
| 02 | PyTorch, resource accounting | 主线 | 可执行讲义 | [笔记](lecture_02.md) |
| 03 | Architectures, hyperparameters | 主线 | PDF | [笔记](lecture_03.md) |
| 05 | GPUs | 概念 | PDF | [笔记](lecture_05.md) |
| 07 | Parallelism basics | 概念 | PDF | [笔记](lecture_07.md) |
| 09 | Scaling laws basics | 概念 | PDF | [笔记](lecture_09.md) |
| 10 | Inference | 概念 | 可执行讲义 | [笔记](lecture_10.md) |
| 13 | Data | 概念 | 可执行讲义 | [笔记](lecture_13.md) |
| 15 | Alignment: SFT / RLHF | 概念 | PDF | [笔记](lecture_15.md) |
| 16 | Alignment: RL | 概念 | PDF | [笔记](lecture_16.md) |
| 17 | Reasoning RL mechanics | 概念 | 可执行讲义 | [笔记](lecture_17.md) |
