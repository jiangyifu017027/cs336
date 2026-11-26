# 2026-11-26 协作模式变更：AI 直接实现作业代码 + 手机端 workflow

## 决定（用户明确要求）

1. 用户是业余自学者（非 Stanford 注册学生，无成绩/学分场景），放弃 2026-11-25 定的"AI 只当助教、不写代码"模式，改为：**用户口述核心思路 → AI 直接编写/修改作业代码并运行测试验证**。
2. 用户后续主要用手机指挥：计划通过 Paseo（self-hosted，ACP 接入 Kimi Code CLI，支持 web/mobile）在手机浏览器操作；手机浏览器看代码走 GitHub 私有仓库（origin 已确认配置）。

## 已同步的文件

- 根 `AGENTS.md`：作业边界重写、协作方式扩大、skills 清单更新
- `assignments/a1-basics/assignment1-basics/AGENTS.md`、`assignments/a3-scaling/assignment3-scaling/AGENTS.md`：顶部加本地覆盖说明（课程原文保留）
- `learning/progress.md`：协作方式、当前位置、下一步最小动作、待办清单
- `STATUS.md`：AI 可直接运行环境检查与作业命令
- `.agents/skills/cs336-assignment/SKILL.md`：整体改为实现模式
- `.agents/skills/cs336-study/SKILL.md`：实现请求转 cs336-assignment
- skill 修改需 `/reload` 后在新会话稳定生效（已提醒用户）

## 保留的规矩

- 不搜索、不指向第三方 CS336 作业实现。
- AI 实现的代码**不作为** knowledge-map 掌握度证据；掌握度仍以用户自评 + 用户独立产出的证据为准。
- 学习档案如实记录"AI 按用户思路实现"，不伪造进度。

## 下一步

用户口述 train_bpe 实现思路 → AI 读 handout §2.3–2.7 与 `tests/adapters.py` → 实现并跑 `tests/test_train_bpe.py` → 逐段中文解释实现。
