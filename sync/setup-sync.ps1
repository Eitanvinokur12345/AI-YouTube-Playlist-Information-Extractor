# setup-sync.ps1
# Run this ONCE to: clone the repo and register a daily Task Scheduler job

# ── CONFIGURATION ──────────────────────────────────────────────────────────────
# Set these to match your machine. $env:USERPROFILE is auto-detected (no changes needed).
$RepoPath   = "$env:USERPROFILE\AI-YouTube-Skills"
$SkillsDest = "$env:USERPROFILE\OneDrive\Desktop\claude skills"
# ───────────────────────────────────────────────────────────────────────────────

$RepoUrl    = "https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor"
$SyncScript = "$RepoPath\sync\sync-skills.ps1"

# Clone repo if not already cloned
if (-not (Test-Path $RepoPath)) {
    Write-Host "Cloning repo..."
    git clone $RepoUrl $RepoPath
} else {
    Write-Host "Repo already exists at $RepoPath"
}

# Register Task Scheduler job (runs daily at 11:00 AM)
$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NonInteractive -File `"$SyncScript`""
$Trigger = New-ScheduledTaskTrigger -Daily -At "11:00AM"
$Settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Minutes 10)
Register-ScheduledTask -TaskName "SyncYouTubeSkills" -Action $Action -Trigger $Trigger -Settings $Settings -RunLevel Highest -Force

Write-Host "Done! Skills will sync daily at 11:00 AM."
Write-Host "To sync right now, run: $SyncScript"
