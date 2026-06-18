#!/usr/bin/env bash
# Run one query through the void_walker agent and save the answer to output.md.
#
# Pre-checks the V9 gateway, then runs code/query_runner.py.
#
# Usage:
#   ./run_query.sh "Compare 3 laptops under ₹80,000."
#   ./run_query.sh "Compare 5 AI coding tools by free plan and paid plan."
#   ./run_query.sh "Compare top 3 Hugging Face text-generation models sorted by likes."
#   ./run_query.sh "Compare 5 CNC/VMC training institutes in Bangalore."

set -o pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CODE_DIR="$SCRIPT_DIR/code"

# ── gateway pre-check ──────────────────────────────────────────────────────────
if ! curl -sf http://localhost:8109/v1/routers >/dev/null 2>&1; then
  echo "[run_query] V9 gateway is not responding at http://localhost:8109" >&2
  echo "       Starting it:  cd ../llm_gatewayV9 && uv run main.py" >&2
  echo "       (The runner will attempt to auto-launch it, but if that fails," >&2
  echo "        start it manually in another terminal.)" >&2
fi

if [[ $# -eq 0 ]]; then
  echo "Usage: $0 \"<your query>\"" >&2
  exit 1
fi

# ── run the agent ──────────────────────────────────────────────────────────────
(cd "$CODE_DIR" && uv run python query_runner.py "$@")

EXIT_CODE=$?
if [[ $EXIT_CODE -eq 0 ]]; then
  echo ""
  echo "[run_query] answer saved to $SCRIPT_DIR/output.md"
else
  echo "[run_query] agent run failed (exit code $EXIT_CODE)" >&2
fi

exit $EXIT_CODE