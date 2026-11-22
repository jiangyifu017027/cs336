#!/usr/bin/env bash
# Print the state of every assignment environment. Read-only.
set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

printf '%-4s %-10s %-42s %s\n' "#" "状态" "Python / 关键包" "路径"
for n in 1 2 3 4 5; do
  dir=$(echo "$ROOT"/assignments/a${n}-*/*/)
  dir="${dir%/}"
  if [ ! -x "$dir/.venv/bin/python" ]; then
    printf '%-4s %-10s %-42s %s\n' "a$n" "未安装" "-" "$dir"
    continue
  fi
  info=$("$dir/.venv/bin/python" - <<'PY' 2>/dev/null
import sys
parts=[f"py{sys.version_info.major}.{sys.version_info.minor}"]
try:
    import torch
    parts.append(f"torch{torch.__version__}")
    parts.append("cuda" if torch.cuda.is_available() else "cpu")
except Exception:
    parts.append("no-torch")
try:
    import jax
    parts.append(f"jax{jax.__version__}")
except Exception:
    pass
print(" / ".join(parts))
PY
)
  status="OK"
  case "$n" in
    1|2|4|5) [[ "$info" == *"no-torch"* ]] && status="待补" ;;
    3) [[ "$info" != *"jax"* ]] && status="待补" ;;
  esac
  printf '%-4s %-10s %-42s %s\n' "a$n" "$status" "$info" "$dir"
done

echo
echo "GPU:"
nvidia-smi --query-gpu=name,driver_version,memory.total,memory.used --format=csv,noheader 2>/dev/null || echo "  nvidia-smi unavailable"
