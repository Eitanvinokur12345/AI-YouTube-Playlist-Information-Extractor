# sync-skills.ps1
# Pulls latest skills from GitHub and copies them to Claude skills folder
# Run this manually or via Task Scheduler

# ── CONFIGURATION ──────────────────────────────────────────────────────────────
# Set these to match your machine. $env:USERPROFILE is auto-detected (no changes needed).
$RepoPath   = "$env:USERPROFILE\AI-YouTube-Skills"
$SkillsDest = "$env:USERPROFILE\OneDrive\Desktop\claude skills"
# ───────────────────────────────────────────────────────────────────────────────

$SkillsSource = "$RepoPath\skills"

# Pull latest from GitHub
Write-Host "Pulling latest from GitHub..."
Set-Location $RepoPath
git pull origin main

# Copy new skill folders to Claude skills folder
Write-Host "Syncing skills..."
if (Test-Path $SkillsSource) {
    Get-ChildItem $SkillsSource -Directory | ForEach-Object {
        $destFolder = Join-Path $SkillsDest $_.Name
        if (-not (Test-Path $destFolder)) {
            Write-Host "New skill: $($_.Name)"
            Copy-Item $_.FullName $SkillsDest -Recurse
        }
    }
}

Write-Host "Done. Skills are up to date."
