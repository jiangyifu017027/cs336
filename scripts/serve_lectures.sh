#!/usr/bin/env bash
# Serve local CS336 lecture traces and slides.
# Usage: ./scripts/serve_lectures.sh [port]
set -euo pipefail
PORT="${1:-8000}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
echo "Serving $ROOT/resources at http://localhost:${PORT}/"
echo
echo "Open one of:"
for n in 01 02 06 08 10 12 13 14 17; do
  echo "  http://localhost:${PORT}/spring2025-lectures/index.html?trace=var/traces/lecture_${n}.json"
done
echo
echo "PDF slides are in resources/spring2025-lectures/nonexecutable/"
echo "Press Ctrl-C to stop."
exec python3 -m http.server "$PORT" --directory "$ROOT/resources"
