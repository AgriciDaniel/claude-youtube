#!/usr/bin/env bash
set -euo pipefail

main() {
    echo "Uninstalling claude-youtube..."

    # Remove skill directory
    rm -rf "${HOME}/.claude/skills/youtube"

    echo "claude-youtube uninstalled."
    echo "Restart Claude Code to complete removal."
}

main "$@"
