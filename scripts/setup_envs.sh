#!/usr/bin/env bash
# Create/update one independent uv environment per assignment.
# Usage: ./scripts/setup_envs.sh [a1|a2|a3|a4|a5|all]
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-all}"

sync_one() {
  local name="$1"; shift
  local dir
  case "$name" in
    a1) dir="$ROOT/assignments/a1-basics/assignment1-basics" ;;
    a2) dir="$ROOT/assignments/a2-systems/assignment2-systems" ;;
    a3) dir="$ROOT/assignments/a3-scaling/assignment3-scaling" ;;
    a4) dir="$ROOT/assignments/a4-data/assignment4-data" ;;
    a5) dir="$ROOT/assignments/a5-alignment/assignment5-alignment" ;;
    *) echo "unknown assignment: $name" >&2; return 1 ;;
  esac
  echo "==> $name: $dir"
  ( cd "$dir" && uv sync "$@" )
}

case "$TARGET" in
  a1) sync_one a1 ;;
  a2) sync_one a2 ;;
  a3) sync_one a3 --extra server ;;   # 本地跑 A3 训练/服务需要 server extra
  a4) sync_one a4 ;;
  a5) sync_one a5 --frozen ;;         # 官方 lock 里 gpu extra 与 macOS 冲突，--frozen 跳过重解析
                                      # 需要 vllm/flash-attn 时：uv sync --frozen --extra gpu
  all)
    sync_one a1
    sync_one a2
    sync_one a3 --extra server
    sync_one a4
    sync_one a5 --frozen
    ;;
  *) echo "usage: $0 [a1|a2|a3|a4|a5|all]" >&2; exit 2 ;;
esac

echo
echo "Done. Check with: ./scripts/check_envs.sh"
