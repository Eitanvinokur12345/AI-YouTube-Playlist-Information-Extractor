# setup-sync.ps1
# Run this ONCE to: clone the repo, register the daily local sync job, and create the
# Desktop dashboard shortcut.

# ── CONFIGURATION ──────────────────────────────────────────────────────────────
$RepoPath = "$env:USERPROFILE\AI-YouTube-Skills"
# ───────────────────────────────────────────────────────────────────────────────
$RepoUrl    = "https://github.com/Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor"
$SyncScript = "$RepoPath\sync\sync-skills.ps1"

# 1) Clone the repo if it isn't here yet
if (-not (Test-Path $RepoPath)) {
    Write-Host "Cloning repo..."
    git clone $RepoUrl $RepoPath
} else {
    Write-Host "Repo already exists at $RepoPath"
}

# 2) Register a daily sync that pulls results into your Desktop folders.
#    -StartWhenAvailable runs it late if the PC was off at the scheduled time.
$Action = New-ScheduledTaskAction -Execute "powershell.exe" `
    -Argument "-NonInteractive -ExecutionPolicy Bypass -File `"$SyncScript`""
$Trigger  = New-ScheduledTaskTrigger -Daily -At "11:00AM"
$Settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Minutes 15) -StartWhenAvailable
Register-ScheduledTask -TaskName "SyncYouTubeSkills" -Action $Action -Trigger $Trigger `
    -Settings $Settings -RunLevel Highest -Force

# 3) Create the Desktop dashboard shortcut
& "$RepoPath\sync\create-shortcut.ps1"

Write-Host ""
Write-Host "Done! The local sync runs daily at 11:00 AM (change -At above to retime)."
Write-Host "Sync right now:       $SyncScript"
Write-Host "Open dashboard:       use the 'AI Skills Dashboard' shortcut on your Desktop"
Write-Host "Offline dashboard:    $RepoPath\sync\open-dashboard-local.ps1"
