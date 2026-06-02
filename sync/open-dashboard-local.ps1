# open-dashboard-local.ps1
# View the dashboard fully OFFLINE from your local clone (no internet needed).
# It serves the repo over http://localhost so the dashboard can read ../data — browsers
# block reading JSON from file:// pages, which is why a tiny local server is used.
# Leave this window open while viewing; press Ctrl+C to stop it when you're done.

$RepoPath = "$env:USERPROFILE\AI-YouTube-Skills"
$Port = 8765

if (-not (Test-Path $RepoPath)) {
    Write-Host "Repo not found at $RepoPath. Run setup-sync.ps1 first."
    return
}

Set-Location $RepoPath
Start-Process "http://localhost:$Port/docs/"
Write-Host "Serving $RepoPath at http://localhost:$Port/  (Ctrl+C to stop)"
python -m http.server $Port
