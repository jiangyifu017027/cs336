#!/usr/bin/env bash
# Create/update one independent uv environment per assignment.
# Usage: ./scripts/setup_envs.sh [a1|a3|all]
# 2026-11-25 轻量计划：仅保留 A1（主线）与 A3（可选轻量版）；A2/A4/A5 已删除。
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-all}"

sync_one() {
  local name="$1"; shift
  local dir
  case "$name" in
    a1) dir="$ROOT/assignments/a1-basics/assignment1-basics" ;;
    a3) dir="$ROOT/assignments/a3-scaling/assignment3-scaling" ;;
    *) echo "unknown assignment: $name" >&2; return 1 ;;
  esac
  echo "==> $name: $dir"
  ( cd "$dir" && uv sync "$@" )
}

case "$TARGET" in
  a1) sync_one a1 ;;
  a3) sync_one a3 --extra server ;;   # 本地跑 A3 训练/服务需要 server extra
  all)
    sync_one a1
    sync_one a3 --extra server
    ;;
  *) echo "usage: $0 [a1|a3|all]" >&2; exit 2 ;;
esac

echo
echo "Done. Check with: ./scripts/check_envs.sh"
