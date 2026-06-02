# create-shortcut.ps1
# Puts an "AI Skills Dashboard" icon on your Desktop that opens the hosted dashboard.

$Desktop = "$env:USERPROFILE\OneDrive\Desktop"
if (-not (Test-Path $Desktop)) { $Desktop = "$env:USERPROFILE\Desktop" }

# GitHub Pages URL (enable Pages: repo Settings -> Pages -> Deploy from branch -> main -> / root).
$DashboardUrl = "https://eitanvinokur12345.github.io/AI-YouTube-Playlist-Information-Extractor/docs/"
$ShortcutPath = Join-Path $Desktop "AI Skills Dashboard.url"

@"
[InternetShortcut]
URL=$DashboardUrl
"@ | Set-Content -Path $ShortcutPath -Encoding ASCII

Write-Host "Created Desktop shortcut:"
Write-Host "  $ShortcutPath"
Write-Host "  -> $DashboardUrl"
