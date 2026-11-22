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
  --exclude '.git/' \
  --exclude '.venv/' --exclude 'data/' --exclude 'local-shared-data/' \
  --exclude '__pycache__/' --exclude '.pytest_cache/' --exclude '.setup/' \
  ~/cs336/ /mnt/d/CS336/
```

（`--exclude data/` 是因为 Windows 副本里已有那 14GB，不必来回拷。
`--exclude '.git/'` 是因为 `/mnt/d` 是 drvfs 挂载、所有文件强制 777，
带 `.git` 会让每个文件都显示权限变更；D 盘只做纯文件副本，
历史由 GitHub origin 与 bundle 快照保管。）

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

2026-11-22 重建过仓库：旧历史已废弃，当前从 1 个干净的初始提交开始。

```bash
cd ~/cs336
git log --oneline          # 查看提交历史
git status                 # 你写的代码会显示为 modified
git diff cs336_basics/     # 看自己改了什么
git add -A && git commit -m "feat(a1): BPE tokenizer"
git push                   # 推到 GitHub
```

分支是 `main`；提交身份是本仓库本地配置
（`jiangyifu017027 <108881497+jiangyifu017027@users.noreply.github.com>`），想改：

```bash
git config user.name "你的名字"
git config user.email "you@example.com"
```

**不入库的内容**（`.gitignore`，共约 41GB）：
- `data/`、`local-shared-data/`（训练语料/离线资产）、`.venv/`、`wheels/`、`.setup/`、`*.sqlite`
- `resources/`、`lectures/`（讲义与论文 PDF，仅本地保留，避免公开分发课程材料）

测试快照 `tests/_snapshots/*.npz` 和 `tests/fixtures/*` 是**要**入库的（测试依赖它们）。

### 备份

| 位置 | 内容 | 用途 |
|---|---|---|
| GitHub `origin`（**私有**） | 287 文件 / 83M，含作业代码、学习档案、文档 | 异地备份 + 多机同步 |
| `D:\CS336\` | 整仓工作副本（含数据、虚拟环境） | Windows 侧冗余 |
| `/mnt/d/cs336-snapshots/*.bundle` | 重建前的完整 git 历史 | 一次性快照兜底 |

```bash
git push      # 推 GitHub（凭证由 VS Code 提供）
```

从快照恢复：

```bash
git clone /mnt/d/cs336-snapshots/cs336-20261122-2223.bundle ~/cs336-old
```

注意：git 里**不含** 41GB 数据与课程材料；A1 的 14GB 语料、A4 的约 3GB offline 资产
需另行下载（见 A1 handout / README），或从 `D:\CS336\` 拷回。

## 排错

- `wsl` 报 localhost 代理提示：NAT 模式下 WSL 不继承 Windows 的 localhost 代理，属于提示信息；
  本机直连可用，若哪天 apt/pip 挂了再考虑 `.wslconfig` 里加镜像网络。
- 磁盘没释放：`wsl --shutdown` 后，`sparseVhd=true` 会在下次关闭时回收。
- 想彻底重来：删除 `~/cs336/.venv` 重新 `uv sync` 即可，不用动系统 Python。
