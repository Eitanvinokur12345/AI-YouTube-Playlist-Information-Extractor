# install-transcription.ps1 — one-time setup for local Whisper transcription (Tier-2 ASR).
# Installs faster-whisper (CPU int8 — no GPU needed) + yt-dlp. No ffmpeg binary required:
# faster-whisper decodes audio via its bundled libraries. Everything here is free.
#
# Run once:  powershell -ExecutionPolicy Bypass -File sync\install-transcription.ps1

Write-Host "Installing transcription dependencies (faster-whisper + yt-dlp)..."
python -m pip install --upgrade pip
python -m pip install faster-whisper yt-dlp
if ($LASTEXITCODE -ne 0) {
    Write-Warning "pip install failed. Make sure Python + pip are on PATH, then re-run."
    exit 1
}
Write-Host ""
Write-Host "Done. The first transcription downloads the light Whisper 'tiny' model (~75 MB) once."
Write-Host "Transcribe a batch now:  python -m src.transcribe_local --limit 15   (tiny model, all videos)"
Write-Host "It is already wired into sync\fetch-runner.ps1 to run a small batch nightly."
