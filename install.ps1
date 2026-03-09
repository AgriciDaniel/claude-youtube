#!/usr/bin/env pwsh
# Claude YouTube Installer for Windows

$ErrorActionPreference = "Stop"

Write-Host "=== Installing claude-youtube ===" -ForegroundColor Cyan
Write-Host ""

# Check prerequisites
try {
    git --version | Out-Null
    Write-Host "Git detected" -ForegroundColor Green
} catch {
    Write-Host "Error: Git is required but not installed." -ForegroundColor Red
    exit 1
}

# Set paths
$SkillDir = "$env:USERPROFILE\.claude\skills\youtube"
$RepoUrl = "https://github.com/AgriciDaniel/claude-youtube"

# Create directories
New-Item -ItemType Directory -Force -Path $SkillDir | Out-Null

# Clone to temp directory
$TempDir = Join-Path $env:TEMP "claude-youtube-install-$(Get-Random)"

try {
    Write-Host "Downloading claude-youtube..." -ForegroundColor Yellow
    git clone --depth 1 $RepoUrl $TempDir 2>&1 | Out-Null

    # Copy skill files
    Write-Host "Installing skill files..." -ForegroundColor Yellow
    Copy-Item -Recurse -Force (Join-Path $TempDir "skills\claude-youtube\*") $SkillDir
} catch {
    Write-Host "Installation failed: $($_.Exception.Message)" -ForegroundColor Red
    throw
} finally {
    if (Test-Path $TempDir) {
        Remove-Item -Recurse -Force $TempDir
    }
}

Write-Host ""
Write-Host "claude-youtube installed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "Usage:" -ForegroundColor Cyan
Write-Host "  1. Start Claude Code:  claude"
Write-Host "  2. Run commands:       /youtube audit"
