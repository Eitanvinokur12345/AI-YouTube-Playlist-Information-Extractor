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

# 2b) Register the LOCAL FETCH runner (residential IP) — nightly at 3:00 AM.
#     Pulls new playlist videos from home, pushes them for the cloud to analyze, and mirrors
#     the brain to the Desktop. Requires YOUTUBE_API_KEY in your environment:
#         setx YOUTUBE_API_KEY "your-key"   (run once, then reopen the terminal)
$FetchScript = "$RepoPath\sync\fetch-runner.ps1"
if (-not $env:YOUTUBE_API_KEY) {
    Write-Warning "YOUTUBE_API_KEY is not set yet. Set it with:  setx YOUTUBE_API_KEY ""your-key""  then re-run this script (otherwise the fetch task will fail)."
}
$FetchAction   = New-ScheduledTaskAction -Execute "powershell.exe" `
    -Argument "-NonInteractive -ExecutionPolicy Bypass -File `"$FetchScript`""
$FetchTrigger  = New-ScheduledTaskTrigger -Daily -At "3:00AM"
$FetchSettings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Minutes 30) -StartWhenAvailable
Register-ScheduledTask -TaskName "FetchYouTubeSkills" -Action $FetchAction -Trigger $FetchTrigger `
    -Settings $FetchSettings -RunLevel Highest -Force

# 3) Create the Desktop dashboard shortcut
& "$RepoPath\sync\create-shortcut.ps1"

Write-Host ""
Write-Host "Done!"
Write-Host "  Local SYNC  runs daily at 11:00 AM  (pull results -> Desktop; change -At to retime)."
Write-Host "  Local FETCH runs daily at  3:00 AM  (pull new videos from home -> push for cloud analysis)."
Write-Host "Sync right now:       $SyncScript"
Write-Host "Fetch right now:      $FetchScript   (needs YOUTUBE_API_KEY)"
Write-Host "Open dashboard:       use the 'AI Skills Dashboard' shortcut on your Desktop"
Write-Host "Offline dashboard:    $RepoPath\sync\open-dashboard-local.ps1"
