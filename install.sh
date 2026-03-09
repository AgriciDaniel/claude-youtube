#!/usr/bin/env bash
set -euo pipefail

# Claude YouTube Installer

main() {
    SKILL_DIR="${HOME}/.claude/skills/youtube"
    REPO_URL="https://github.com/AgriciDaniel/claude-youtube"

    echo "=== Installing claude-youtube ==="
    echo ""

    # Check prerequisites
    command -v git >/dev/null 2>&1 || { echo "Error: git is required but not installed."; exit 1; }

    # Create directories
    mkdir -p "${SKILL_DIR}"

    # Clone to temp directory
    TEMP_DIR=$(mktemp -d)
    trap "rm -rf ${TEMP_DIR}" EXIT

    echo "Downloading claude-youtube..."
    git clone --depth 1 "${REPO_URL}" "${TEMP_DIR}/claude-youtube" 2>/dev/null

    # Copy skill files
    echo "Installing skill files..."
    cp -r "${TEMP_DIR}/claude-youtube/skills/claude-youtube/"* "${SKILL_DIR}/"

    echo ""
    echo "claude-youtube installed successfully!"
    echo ""
    echo "Usage:"
    echo "  1. Start Claude Code:  claude"
    echo "  2. Run commands:       /youtube audit"
    echo ""
    echo "To uninstall: curl -fsSL ${REPO_URL}/raw/main/uninstall.sh | bash"
}

main "$@"
