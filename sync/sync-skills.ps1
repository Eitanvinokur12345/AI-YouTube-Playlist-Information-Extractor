# sync-skills.ps1
# Pulls the latest results from GitHub and copies them to your local Desktop folders.
# Runs via Task Scheduler (see setup-sync.ps1) or manually. Everything here is local
# and offline-friendly except the single `git pull` at the top.

# ── CONFIGURATION ──────────────────────────────────────────────────────────────
# $env:USERPROFILE is auto-detected — no changes needed on a standard setup.
$RepoPath = "$env:USERPROFILE\AI-YouTube-Skills"
$Desktop  = "$env:USERPROFILE\OneDrive\Desktop"

$ClaudeSkillsDest = Join-Path $Desktop "claude skills of eitan"   # Claude skill packages
$DataDest         = Join-Path $Desktop "AI Skills Data"           # read by the MCP server
# Non-Claude tools (gemini, chatgpt, ...) each get "<tool> skills of eitan" automatically.
# ───────────────────────────────────────────────────────────────────────────────

# Quiet robocopy flags: copy tree, overwrite changed files, never DELETE extra files in
# the destination (so your manually-added skills are preserved). Exit codes 0-7 = success.
$RC = @("/E", "/R:2", "/W:2", "/NFL", "/NDL", "/NJH", "/NJS", "/NP")

Write-Host "Pulling latest from GitHub..."
Set-Location $RepoPath
git pull origin main

# 1) Claude skill packages: skills/ -> "claude skills of eitan"
if (Test-Path "$RepoPath\skills") {
    Write-Host "Syncing Claude skills -> $ClaudeSkillsDest"
    robocopy "$RepoPath\skills" $ClaudeSkillsDest @RC | Out-Null
}

# 2) Other-tool skill packages: other-skills/<tool>/ -> "<tool> skills of eitan"
if (Test-Path "$RepoPath\other-skills") {
    Get-ChildItem "$RepoPath\other-skills" -Directory | ForEach-Object {
        $toolDest = Join-Path $Desktop "$($_.Name) skills of eitan"
        Write-Host "Syncing $($_.Name) skills -> $toolDest"
        robocopy $_.FullName $toolDest @RC | Out-Null
    }
}

# 3) Pipeline data (all 6 tabs) -> "AI Skills Data" (the MCP server reads this offline).
#    Skip the working folders (_pending / processed) — only the result JSONs are needed.
if (Test-Path "$RepoPath\data") {
    Write-Host "Syncing data -> $DataDest"
    robocopy "$RepoPath\data" $DataDest @RC /XD "_pending" "processed" | Out-Null
}

# 4) Obsidian brain: brain/ -> "Excavatortron Brain" (open this as a vault in Obsidian).
if (Test-Path "$RepoPath\brain") {
    $BrainDest = Join-Path $Desktop "Excavatortron Brain"
    Write-Host "Syncing brain -> $BrainDest"
    robocopy "$RepoPath\brain" $BrainDest @RC | Out-Null
}

# robocopy sets $LASTEXITCODE 1-7 on success; normalize so Task Scheduler shows success.
if ($LASTEXITCODE -le 7) { $global:LASTEXITCODE = 0 }

Write-Host "Done. Skills, other-tool skills, and data are up to date."
