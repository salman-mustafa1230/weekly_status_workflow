#!/usr/bin/env bash
# Back-compat wrapper. Prefer ./scripts/run_status.sh
exec "$(cd "$(dirname "$0")" && pwd)/run_status.sh" "$@"
