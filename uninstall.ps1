#!/usr/bin/env pwsh
# claude-youtube uninstaller for Windows

$ErrorActionPreference = "Stop"

Write-Host "=== Uninstalling claude-youtube ===" -ForegroundColor Cyan
Write-Host ""

$SkillDir = Join-Path $env:USERPROFILE ".claude" "skills" "youtube"
if (Test-Path $SkillDir) {
    Remove-Item -Recurse -Force $SkillDir
    Write-Host "  Removed: $SkillDir" -ForegroundColor Green
}

Write-Host ""
Write-Host "=== claude-youtube uninstalled ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Restart Claude Code to complete removal." -ForegroundColor Yellow
