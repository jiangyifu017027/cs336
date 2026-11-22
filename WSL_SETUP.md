# CS336 on WSL2 — 本机环境说明

本机已把 CS336 的工作副本迁到 WSL2 (Ubuntu) 里，本文件记录怎么用、注意什么。

## 落地结构

| 位置 | 说明 |
| --- | --- |
| `D:\WSL\Ubuntu\ext4.vhdx` | WSL 发行版虚拟磁盘（已从 C 盘移到 D 盘，避免训练数据撑爆 C 盘） |
| `~/cs336` | **主工作副本**（在 WSL 的 ext4 里，pip/git/pytest 都快很多） |
| `/mnt/d/CS336` | Windows 侧副本（约 18GB，代码+材料+数据，**无 venv**），作为备份；`~/cs336` 才是你在跑的那份 |
| `C:\Users\few\.wslconfig` | WSL 内存/交换/自动回收配置（20GB / 8GB） |

硬件：Ryzen 7 5700X (8C/16T)、32GB RAM、**RTX 5060 8GB (Blackwell, sm_120)**。
→ 决定了 torch 必须是 **CUDA 12.8+** 的版本，A1 的 `pyproject.toml` 已固定走 `pytorch-cu128` 源，Windows / WSL 两边都能 `uv sync`。

当前 A1–A5 五个 uv 环境都已建好（A1/A2/A4 使用 CUDA 12.8/13.0 的 torch，
A3 使用 JAX CUDA13，A5 使用官方 lock 的 torch），逐项状态见 `STATUS.md`；
随时用 `./scripts/check_envs.sh` 复查，用 `./scripts/setup_envs.sh aN` 重建。

## 常用操作

```bash
# 从 Windows 终端进入
wsl                      # 默认进 ~
wsl -d Ubuntu            # 同上

# 进课程目录
cd ~/cs336               # 或别名: cs336
```

每个作业是独立环境（Python 3.12，由 uv 自动下载管理，不用系统 Python 3.14）：

```bash
cd ~/cs336/assignments/a1-basics/assignment1-basics
uv sync                  # 建/更新 .venv（首次约 3GB 下载）
uv run python xxx.py     # 在环境里跑
.venv/bin/activate       # 或者手动激活（bash: source .venv/bin/activate）
uv run pytest tests/     # 跑测试
```

已配置的 shell 别名（`~/.bashrc`）：

| 别名 | 作用 |
| --- | --- |
| `cs336` | `cd ~/cs336` |
| `a1` / `a2` / `a3` / `a4` / `a5` | 进对应作业目录 |

## GPU 检查

```bash
nvidia-smi                                   # WSL 里能直接看到 5060
python -c "import torch; print(torch.__version__, torch.version.cuda, torch.cuda.get_device_name(0), torch.cuda.get_device_capability(0))"
# 期望: 2.11.0+cu128 12.8 NVIDIA GeForce RTX 5060 (12, 0)
```

**注意**：WSL 里不要自己装 NVIDIA 驱动（不要在 apt 里装 `nvidia-driver-*`），
Windows 驱动 + `/usr/lib/wsl/lib` 已经提供 CUDA 透传。

## VS Code

已装 `ms-vscode-remote.remote-wsl`。推荐用法：在 WSL 里 `cd ~/cs336 && code .`，
会打开 Remote-WSL 窗口，Python 解释器选 `~/cs336/.../.venv/bin/python`。

## 数据

A1 的数据在 `~/cs336/assignments/a1-basics/assignment1-basics/data/`（14GB）：

- `TinyStoriesV2-GPT4-train.txt` 2.2GB
- `owt_train.txt` 11.9GB

WSL 磁盘在 D 盘，还有 ~560GB 可用，放 FineWeb / checkpoint 都够。
如果要用 Windows 侧的大文件，别名 `/mnt/d/...` 也能访问，但**训练时慢**，尽量拷进 ext4。

## 备份 / 同步回 Windows

```bash
rsync -a --delete \
  --exclude '.venv/' --exclude 'data/' --exclude 'local-shared-data/' \
  --exclude '__pycache__/' --exclude '.pytest_cache/' --exclude '.setup/' \
  ~/cs336/ /mnt/d/CS336/
```

（`--exclude data/` 是因为 Windows 副本里已有那 14GB，不必来回拷。）

## A2 (systems) 起步时要注意

`assignment2-systems/pyproject.toml` 里 `cs336-basics` 默认指向同目录的
`./cs336-basics` 占位包。要换成你自己的 A1 实现：

```toml
[tool.uv.sources]
cs336-basics = { path = "../../a1-basics/assignment1-basics", editable = true }
```

Triton 部分在 WSL 里跑最稳（这也是当初选 WSL2 的原因）；`triton` 会随 torch 一起装好。

## 可选：加速 pip/npm 类下载

```bash
export UV_DEFAULT_INDEX=https://mirrors.aliyun.com/pypi/simple
```
（torch 的 cu128 wheel 仍走官方 download.pytorch.org，实测 ~5MB/s 可接受。）

## Git 版本管理

已做一次初始提交，把官方课程材料（1034 个文件 / 252MB）作为基线：

```bash
cd ~/cs336
git log --oneline          # 基线提交
git status                 # 你写的代码会显示为 modified
git diff cs336_basics/     # 看自己改了什么
git add -A && git commit -m "feat(a1): BPE tokenizer"
```

分支是 `master`；提交身份是本仓库本地配置（`few <few@localhost>`），想改：

```bash
git config user.name "你的名字"
git config user.email "you@example.com"
```

**不入库的内容**（`.gitignore`，共约 14GB）：`data/`（训练语料）、`.venv/`、`wheels/`、`*.sqlite`（讲义的 profiler 中间产物）、`.setup/`。
测试快照 `tests/_snapshots/*.npz` 和 `tests/fixtures/*` 是**要**入库的（测试依赖它们）。

### 备份到 D 盘（已配置）

`D:\CS336-backup.git` 是一个裸仓库（bare repo），`master` 已跟踪它：推一次改动只要

```bash
git push backup           # 或 git push（因为已设置 upstream）
```

从备份恢复（万一 WSL 磁盘坏了）：

```bash
git clone /mnt/d/CS336-backup.git ~/cs336-new    # 拿到全部代码与历史
# 数据语料不在 git 里，需要另行下载（见 A1 handout / README）
```

注意：`D:\CS336-backup.git` 只存**代码/材料与历史**（约 280MB）；
A1 的 14GB 语料 + A4 的约 3GB offline 资产仍在 `D:\CS336\...` 下（不进 git）。

## 排错

- `wsl` 报 localhost 代理提示：NAT 模式下 WSL 不继承 Windows 的 localhost 代理，属于提示信息；
  本机直连可用，若哪天 apt/pip 挂了再考虑 `.wslconfig` 里加镜像网络。
- 磁盘没释放：`wsl --shutdown` 后，`sparseVhd=true` 会在下次关闭时回收。
- 想彻底重来：删除 `~/cs336/.venv` 重新 `uv sync` 即可，不用动系统 Python。
