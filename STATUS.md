# 环境与资料状态

> 最后检查：2026-11-21 02:05（WSL2 Ubuntu 26.04，RTX 5060 8GB）
> 环境由每个作业独立的 `uv` venv 管理；用 `./scripts/check_envs.sh` 随时复查。

## 总览

| 作业 | 环境 | 关键依赖 | 数据 | 状态 |
|------|------|----------|------|------|
| A1 Basics | `assignments/a1-basics/.../.venv` | Python 3.12 / torch 2.11 cu128 | TinyStories + OWT，14GB | ✅ 可用；代码待实现 |
| A2 Systems | `assignments/a2-systems/.../.venv` | Python 3.12 / torch 2.11 cu130 | 无外部数据 | ✅ 可用；待接 A1 实现 |
| A3 Scaling | `assignments/a3-scaling/.../.venv` | Python 3.12 / JAX 0.9.1 CUDA13 | 仅 isoflops 曲线 | ✅ 环境可用；数据需 Modal/API |
| A4 Data | `assignments/a4-data/.../.venv` | Python 3.12 / torch 2.11 cu130 | offline 资产约 3GB | ✅ 可用；完整 crawl 未下 |
| A5 Alignment | `assignments/a5-alignment/.../.venv` | Python 3.12 / torch 2.10 cu129 | 86MB 数据集 | ✅ 可用；大模型需云 GPU |

## 一键命令

```bash
# 检查所有环境（只读）
./scripts/check_envs.sh

# 安装/更新某个作业
./scripts/setup_envs.sh a1
./scripts/setup_envs.sh a2
./scripts/setup_envs.sh a3      # 自动带 --extra server
./scripts/setup_envs.sh a4
./scripts/setup_envs.sh a5

# 全部
./scripts/setup_envs.sh all
```

每个作业目录仍然是标准用法：

```bash
cd assignments/a1-basics/assignment1-basics
uv run python -c "import torch; print(torch.cuda.get_device_name(0))"
uv run pytest tests/ -q
```

## 环境细节

### A1 — Basics

- Python 3.12.16，`torch 2.11.0+cu128`，CUDA 12.8
- GPU 检查通过：RTX 5060，compute capability `(12, 0)`，bf16 matmul 正常
- `uv run pytest tests/test_model.py` 会得到 13 个 `NotImplementedError`：
  这是 starter 代码的正常状态，不是环境问题
- 数据：`data/` 下 TinyStories train/valid + OWT train/valid，共约 14GB

### A2 — Systems

- Python 3.12.16，`torch 2.11.0+cu130`，CUDA 13.0
- GPU bf16 matmul 检查通过
- 单卡可以跑 attention/benchmark 相关部分；DDP/FSDP 测试需要多卡
- `cs336-basics` 目前仍指向官方的 `./cs336-basics` 占位包。
  完成 A1 后，把 `pyproject.toml` 的 `[tool.uv.sources]` 改成：

  ```toml
  cs336-basics = { path = "../../a1-basics/assignment1-basics", editable = true }
  ```

  然后重新 `uv sync`。

### A3 — Scaling

- Python 3.12.16，JAX 0.9.1，`jax.devices()` 能看到 `CudaDevice(id=0)`
- 已安装 `--extra server`（JAX CUDA13、FastAPI、polars、transformers 等）
- 非学生没有 `A3_API_KEY`，不能用 Stanford hosted API
- 非学生的本地路径需要 tokenized DCLM 数据（官方脚本用 Modal，
  约 500B tokens，量级 ~1TB），当前没有下载
- 目前只有 `data/isoflops_curves.json`；适合先读讲义/写分析代码，
  真要跑训练建议用云 GPU + 官方/自己的数据管线
- 注意：A3 的 `tests/` 需要本地 PostgreSQL（测试会 CREATE DATABASE），
  当前 WSL 没有装 Postgres，所以 7 个测试会报 `INTERNAL_API_KEY` / DB 连接错误；
  这不影响 JAX 环境和 `cs336_scaling` 代码本身

### A4 — Data

- Python 3.12.16，`torch 2.11.0+cu130`，CUDA 13.0
- `fasttext`、`resiliparse`、`fastwarc`、`mmh3`、`nltk` 导入正常
- `local-shared-data/` 已放好 offline 资产（已校验文件大小/可加载）：
  Paloma tokenized validation（19MB）、CC example WARC（778MB）/WET（60MB）、
  `lid.176.bin`（125MB）、Dolma hatespeech（946MB）/NSFW（946MB）fastText 模型
- 官方 `scripts/download_data.py --offline-only` 会因 `SUNET_ID` 未填而拒绝 import；
  本仓库用 `scripts/fetch_a4_offline.py` 下载同样的文件，不改课程 starter
- 完整 2500 个 WET + wiki URL 管线需要先实现 `is_english` 并配置 Modal；
  当前未下载（数据量很大）

### A5 — Alignment

- Python 3.12，torch 2.10.0+cu129 / CUDA 12.9，GPU bf16 matmul 通过
- 默认依赖（不含 `flash-attn` / `vllm` 的 `gpu` extra）
- 官方 `uv.lock` 的 `gpu` extra 与 macOS arm64 环境冲突，直接 `uv sync`
  会重解析失败；本仓库用 `uv sync --frozen` 安装默认依赖
- 26 个测试可正常 collect；starter 未实现时按预期 `NotImplementedError`
- `data/` 已有 gsm8k、mmlu、hh、simple_safety_tests、alpaca_eval，约 86MB
- 单元测试可跑 CPU；真正 SFT/GRPO 训练需要更大显存或 Modal/云 GPU
- `flash-attn` / `vllm` 需要时再装：

  ```bash
  uv sync --frozen --extra gpu
  ```

  8GB 卡不建议本地装 vLLM 大模型；优先用云。

## 资料

| 资料 | 位置 | 状态 |
|------|------|------|
| 讲义索引 + 17 讲笔记模板 | `lectures/` | ✅ |
| 8 讲 PDF | `resources/spring2025-lectures/nonexecutable/` | ✅ |
| 9 讲可执行幻灯片 + trace | `resources/spring2025-lectures/` | ✅ |
| 本地看幻灯片 | `./scripts/serve_lectures.sh` | ✅ 已验证 200 |
| 课程推荐论文 | `resources/papers/` | ✅ 74 篇 PDF，约 175MB |
| 速查表 | `resources/cheatsheets/` | ✅ PyTorch/GPU/Triton/分布式/分词 |

本地看可执行讲义：

```bash
./scripts/serve_lectures.sh
# http://localhost:8000/spring2025-lectures/index.html?trace=var/traces/lecture_01.json
```

## 已知缺口 / 建议顺序

1. **A1 代码本身**：`cs336_basics/` 仍是 starter，需要按 handout 实现 BPE、
   Transformer、优化器和训练循环。环境已就绪，直接 `uv run pytest` 驱动开发。
2. **A2 的 `cs336-basics`**：等 A1 有实现后替换占位包，再跑 A2 的测试。
3. **A3 数据/API**：没有学生 API key；本地全量 tokenized DCLM 不现实。
   先把 A3 当作 scaling law 阅读 + 小规模本地实验，正式跑用云。
4. **A4 完整数据**：先实现 `cs336_data.wet_files.is_english`，再决定是否
   下载 2500 个 WET；当前 offline 资产足够跑单测和 pipeline 调试。
5. **A5 大模型**：默认环境只保证单测；Llama/Qwen 权重、vLLM、flash-attn
   按需从云上跑，别在本机 8GB 卡上硬塞。
6. **W&B / HuggingFace**：需要时再 `wandb login` / `hf auth login`，
   当前未配置（不影响本地测试）。

## 备份

```bash
# 代码/笔记/资料同步到 D 盘工作副本（数据目录不重复搬）
rsync -a --delete \
  --exclude '.venv/' --exclude 'data/' --exclude 'local-shared-data/' \
  --exclude '__pycache__/' --exclude '.pytest_cache/' \
  ~/cs336/ /mnt/d/CS336/

# git 备份（bare repo）
git push backup
```

> `D:\CS336` 是 Windows 侧备份；`~/cs336` 是主工作副本。
> 大数据（A1 data、A4 local-shared-data）不进 git，但已 rsync 到 D。
