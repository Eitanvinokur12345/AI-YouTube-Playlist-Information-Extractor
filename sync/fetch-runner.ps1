# fetch-runner.ps1
# LOCAL FETCH runner — pulls new playlist videos from your residential IP (YouTube throttles
# datacenter IPs, so fetching from home is more reliable than the cloud), writes
# data/_pending/*.json, and commits + pushes. The cloud pipeline then analyzes them.
# Also mirrors the Obsidian brain to the Desktop.
#
# Needs: git, python (with requirements.txt installed), and YOUTUBE_API_KEY in your env.
# Set the key ONCE (then reopen the terminal):
#     setx YOUTUBE_API_KEY "your-youtube-api-key"
# Register it to run automatically with sync\setup-sync.ps1. Free, no babysitting.

$ErrorActionPreference = "Stop"
$RepoPath = "$env:USERPROFILE\AI-YouTube-Skills"
$Branch   = "main"

Set-Location $RepoPath

if (-not $env:YOUTUBE_API_KEY) {
    Write-Error "YOUTUBE_API_KEY is not set. Run:  setx YOUTUBE_API_KEY ""your-key""  then reopen the terminal."
    exit 1
}

Write-Host "[1/5] Pulling latest from GitHub..."
git pull --rebase origin $Branch

Write-Host "[2/5] Fetching new videos from the playlist (residential IP)..."
python -m src.fetch
if ($LASTEXITCODE -ne 0) { Write-Error "fetch failed (exit $LASTEXITCODE)"; exit $LASTEXITCODE }

Write-Host "[3/5] Staging fetch outputs only (never -A, never secrets/make_icon.py)..."
# Stage ONLY the files the fetch stage writes — explicit paths per the project rules.
git add data/_pending data/skills.json data/status.json data/catch_up.json `
        data/daily_news.json data/weekly_news.json data/monthly_news.json

Write-Host "[4/5] Commit + push..."
$stamp = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mmZ")
git commit -m "fetch (local runner): $stamp"
if ($LASTEXITCODE -eq 0) {
    git pull --rebase origin $Branch
    git push origin $Branch
    Write-Host "Pushed new pending videos."
} else {
    Write-Host "Nothing new to commit."
}

Write-Host "[5/5] Mirroring brain/ -> Desktop..."
$Desktop   = "$env:USERPROFILE\OneDrive\Desktop"
$BrainDest = Join-Path $Desktop "Excavatortron Brain"
if (Test-Path "$RepoPath\brain") {
    robocopy "$RepoPath\brain" $BrainDest /E /R:2 /W:2 /NFL /NDL /NJH /NJS /NP | Out-Null
    if ($LASTEXITCODE -le 7) { $global:LASTEXITCODE = 0 }
}

Write-Host "Done — fetch complete; the cloud will analyze the new pending videos."
