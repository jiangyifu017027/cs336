# 环境与资料状态

> 本文区分 **当前 Mac 副本**与 **WSL2 已验证快照**，不把一台机器的结论直接套到另一台。
> WSL2 最后检查：2026-11-21 02:05（Ubuntu 26.04，RTX 5060 8GB）。
> 环境由每个作业独立的 `uv` venv 管理；需要复查时运行 `./scripts/check_envs.sh`。2026-11-26 起用户已授权 AI 直接运行此类命令与作业测试（见根 `AGENTS.md` 作业边界）。
> 2026-11-25 按轻量计划清理：A2/A4/A5 目录与 L04/L06/L08/L11/L12/L14 讲义已从 Mac 副本删除；WSL2 侧旧副本仍存在，但不再维护。

## 当前 Mac 副本（2026-11-23）

- 工作路径：`/Users/mac/Developer/Personal/cs336`。
- 已确认 `lectures/`、`resources/spring2025-lectures/` 和 `resources/papers/` 目录存在。
- 当前没有 `resources/cheatsheets/` 和 `scratch/`；根 README 与学习说明已移除对应入口，需要时再恢复或创建。
- A1、A3 的 Mac 作业环境、依赖与数据均未复查，不能沿用 WSL2 的“可用”结论。
- 用户可在项目根目录运行 `./scripts/check_envs.sh` 并把输出交给 AI；该脚本只检查环境，不代表课程学习进度。

## WSL2 已验证快照（2026-11-21）

以下环境细节、测试现象、数据规模和备份路径均属于 WSL2，除非之后另行验证，不表示当前 Mac 状态。
A2/A4/A5 的 WSL2 环境当时验证为可用，但按 2026-11-25 轻量计划不再维护（对应作业目录已从 Mac 副本删除）。

### 环境总览

| 作业 | 环境 | 关键依赖 | 数据 | WSL2 状态 |
|------|------|----------|------|------|
| A1 Basics | `assignments/a1-basics/.../.venv` | Python 3.12 / torch 2.11 cu128 | TinyStories + OWT，14GB | ✅ 可用；代码待实现 |
| A3 Scaling | `assignments/a3-scaling/.../.venv` | Python 3.12 / JAX 0.9.1 CUDA13 | 仅 isoflops 曲线 | ✅ 环境可用；数据需 Modal/API |

## 一键命令

```bash
# 检查所有环境（只读）
./scripts/check_envs.sh

# 安装/更新某个作业
./scripts/setup_envs.sh a1
./scripts/setup_envs.sh a3      # 自动带 --extra server

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

## 资料

| 资料 | 位置 | 状态 |
|------|------|------|
| 讲义索引 + 11 讲笔记模板 | `lectures/` | ✅（仅保留轻量计划的 11 讲） |
| 6 讲 PDF | `resources/spring2025-lectures/nonexecutable/` | ✅（L03/05/07/09/15/16） |
| 5 讲可执行幻灯片 + trace | `resources/spring2025-lectures/` | ✅（L01/02/10/13/17） |
| 本地看幻灯片 | `./scripts/serve_lectures.sh` | ✅ 已验证 200 |
| 课程推荐论文 | `resources/papers/` | ✅ 55 篇 PDF，约 110MB（2026-11-25 按轻量计划精选，原 74 篇） |

本地看可执行讲义：

```bash
./scripts/serve_lectures.sh
# http://localhost:8000/spring2025-lectures/index.html?trace=var/traces/lecture_01.json
```

## 已知缺口 / 建议顺序

1. **A1 代码本身**：`cs336_basics/` 仍是 starter，需要按 handout 实现 BPE、
   Transformer、优化器和训练循环。环境已就绪，直接 `uv run pytest` 驱动开发。
2. **A3 数据/API**（可选作业）：没有学生 API key；本地全量 tokenized DCLM 不现实。
   先把 A3 当作 scaling law 阅读 + 小规模本地实验，正式跑用云。
3. **W&B / HuggingFace**：需要时再 `wandb login` / `hf auth login`，
   当前未配置（不影响本地测试）。

## WSL2 备份（不适用于当前 Mac 路径）

以下命令中的 `~/cs336`、`/mnt/d/` 和 `D:\CS336` 均属于 WSL2/Windows 备份流程，不要在当前 Mac 副本中直接照用。

```bash
# 代码/笔记/资料同步到 D 盘工作副本（数据目录不重复搬；.git 不同步，D 盘是纯文件副本）
rsync -a --delete \
  --exclude '.git/' \
  --exclude '.venv/' --exclude 'data/' --exclude 'local-shared-data/' \
  --exclude '__pycache__/' --exclude '.pytest_cache/' \
  ~/cs336/ /mnt/d/CS336/

# git 推送到 GitHub 私有仓库
git push
```

> `D:\CS336` 是 Windows 侧备份；`~/cs336` 是主工作副本。
> 大数据（A1 data）不进 git，但已 rsync 到 D。

远端（2026-11-22 重建）：

| remote | 地址 | 说明 |
|---|---|---|
| `origin` | `https://github.com/jiangyifu017027/cs336.git` | GitHub **私有**仓库 |

- 入库内容：`assignments/`（现仅 A1、A3）、`learning/`、`scripts/`、`.agents/`、顶层文档。
- 不入库：数据集与虚拟环境（`data/`、`.venv/` 等，体积大且可重新下载）。
- 课程材料（`resources/`、`lectures/`）：自 2026-11-25 起入库，作为私有仓库备份（原“仅本地保留”策略已调整）。
- 旧历史已废弃；改动前的完整快照：`/mnt/d/cs336-snapshots/cs336-20261122-2223.bundle`（可用 `git clone` 直接恢复）。
- 凭证由 VS Code 提供（`GIT_ASKPASS`），无需在仓库里保存 token。
