# fetch-runner.ps1
# LOCAL runner — does the two things YouTube only allows from a RESIDENTIAL IP (it blocks the
# cloud/datacenter IPs that GitHub Actions uses):
#   1) BACKFILL real transcripts for already-seen videos (the big recovery — the cloud got a
#      real transcript for only ~0.3% of videos; the rest fell back to the description).
#   2) FETCH new playlist videos.
# Both re-queue work into data/_pending/ and push, so the cloud analyze stage re-extracts deeply
# under the anti-boilerplate gate. Free, no babysitting.
#
# Backfill needs NO key. Fetch needs YOUTUBE_API_KEY (set once, then reopen the terminal):
#     setx YOUTUBE_API_KEY "your-youtube-api-key"
# Register it to run nightly with sync\setup-sync.ps1.

$RepoPath = "$env:USERPROFILE\AI-YouTube-Skills"
$Branch   = "main"
Set-Location $RepoPath

Write-Host "[1/5] Pulling latest from GitHub..."
git pull --rebase origin $Branch

Write-Host "[2/5] Backfilling real transcripts (residential IP) — the recovery..."
# No API key needed. Gentle pace to avoid YouTube rate-limiting; bounded batch per run so the
# cloud can drain it. Non-fatal: rate-limits / missing captions are expected for some videos.
python -m src.backfill_transcripts --limit 80 --sleep 1.2

Write-Host "[2b/5] Whisper-transcribing videos (local ASR, light tiny model, small nightly batch)..."
# Whisper is the source of truth for raw spoken content (captions aren't guaranteed complete).
# mode=all upgrades every video to Whisper over time; tiny model + capped threads = gentle on
# the PC. CPU-bound, so a small batch per night. Skips gracefully if faster-whisper/yt-dlp
# aren't installed (run sync\install-transcription.ps1 once). No API key, no cost.
python -m src.transcribe_local --limit 15 --mode all --model tiny --cpu-threads 4

Write-Host "[3/5] Fetching NEW playlist videos (needs YOUTUBE_API_KEY)..."
if ($env:YOUTUBE_API_KEY) {
    python -m src.fetch
    if ($LASTEXITCODE -ne 0) { Write-Warning "fetch failed (exit $LASTEXITCODE) — continuing with backfill results." }
} else {
    Write-Warning "YOUTUBE_API_KEY not set — skipping new-video fetch. Set it with: setx YOUTUBE_API_KEY ""your-key"". (Backfill above still ran.)"
}

Write-Host "[4/5] Commit + push (explicit paths only; never -A / secrets / make_icon.py)..."
git add data/_pending data/skills.json data/status.json data/catch_up.json `
        data/daily_news.json data/weekly_news.json data/monthly_news.json 2>$null
$stamp = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mmZ")
git commit -m "local runner: backfill transcripts + fetch $stamp"
if ($LASTEXITCODE -eq 0) {
    git pull --rebase origin $Branch
    git push origin $Branch
    Write-Host "Pushed re-queued videos for deep re-analysis."
} else {
    Write-Host "Nothing new to commit this run."
}

Write-Host "[5/5] Mirroring brain/ -> Desktop..."
$Desktop   = "$env:USERPROFILE\OneDrive\Desktop"
$BrainDest = Join-Path $Desktop "Excavatortron Brain"
if (Test-Path "$RepoPath\brain") {
    robocopy "$RepoPath\brain" $BrainDest /E /R:2 /W:2 /NFL /NDL /NJH /NJS /NP | Out-Null
    if ($LASTEXITCODE -le 7) { $global:LASTEXITCODE = 0 }
}
Write-Host "Done. The cloud will re-analyze the re-queued videos with real transcripts."
