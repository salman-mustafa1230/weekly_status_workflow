#!/usr/bin/env bash
# Weekly status pipeline — program-agnostic. Swap data/*.json and re-run.
#
#   ./scripts/run_status.sh           # load sources, then Claude CLI if installed
#   ./scripts/run_status.sh --print   # print the recipe (paste into any agent)
#   ./scripts/run_status.sh exec      # passed through as audience argument
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

AUDIENCE="both"
PRINT_ONLY=0
for arg in "$@"; do
  case "$arg" in
    --print|--print-prompt) PRINT_ONLY=1 ;;
    exec|team|both) AUDIENCE="$arg" ;;
    -h|--help)
      cat <<'EOF'
Usage: ./scripts/run_status.sh [--print] [exec|team|both]

Always writes extracted/raw-bundle.json from every data/*.json file.

If the Claude Code CLI (`claude`) is on PATH, runs the recipe headless.
Otherwise prints how to invoke the same recipe in Cursor or Claude Code.
EOF
      exit 0
      ;;
  esac
done

python3 scripts/load_sources.py

RECIPE="$ROOT/prompts/status-synthesis.md"
if [[ ! -f "$RECIPE" ]]; then
  echo "Missing $RECIPE" >&2
  exit 1
fi

PROMPT="$(cat "$RECIPE")

Audience argument: ${AUDIENCE}
"

if [[ "$PRINT_ONLY" -eq 1 ]]; then
  printf '%s' "$PROMPT"
  exit 0
fi

if command -v claude >/dev/null 2>&1; then
  echo "Running recipe with Claude Code CLI (audience=${AUDIENCE})..."
  exec claude -p "$PROMPT" --allowedTools "Bash,Read,Write,Edit"
fi

cat <<EOF
Sources loaded. No \`claude\` CLI on PATH, so the LLM step did not run.

Same recipe, three ways:

  Cursor       open this repo → type /weekly-status ${AUDIENCE}
  Claude Code  cd into this repo → type /weekly-status ${AUDIENCE}
  Headless     install Claude Code CLI, then:
               ./scripts/run_status.sh ${AUDIENCE}

To paste the recipe into ChatGPT / Gemini / another agent:
  ./scripts/run_status.sh --print
EOF
