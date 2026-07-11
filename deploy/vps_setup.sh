#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════════════════
# EXCAVA 24/7 VPS SETUP — one command, then it runs forever (R1, owner's #1 want, raised 45x)
#
# What this does on a fresh Ubuntu VM (e.g. Oracle Cloud "Always Free" ARM):
#   1. installs python3 + git
#   2. clones the repo using the deploy token you paste below
#   3. installs a systemd timer that runs the EXCAVA beat EVERY 5 MINUTES, 24/7,
#      committing + pushing results — no GitHub-cron throttling, no queued runs
#
# HOW TO USE (once, ~10 minutes):
#   a) create the VM: oracle.com/cloud/free -> Always Free -> Ampere ARM VM, Ubuntu 22.04+
#   b) on GitHub: Settings -> Developer settings -> Fine-grained tokens -> new token,
#      ONLY this repo, permission "Contents: Read and write" -> copy it
#   c) ssh into the VM and run:
#      export GH_TOKEN=paste_your_token_here
#      export GH_REPO=Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor
#      curl -fsSL https://raw.githubusercontent.com/$GH_REPO/main/deploy/vps_setup.sh | bash
#   d) add the SAME engine keys the Actions beat uses to /opt/excava/env (template written
#      by this script) — copy values from your GitHub secrets page.
#
# Safety: free-only (Always Free tier), pull-rebase before every beat, quarantine-never-delete
# is inherited from git_safe; the GitHub cron beat can stay on as a fallback — the bus dedupes.
# ═══════════════════════════════════════════════════════════════════════════════
set -euo pipefail

: "${GH_TOKEN:?set GH_TOKEN to a fine-grained repo token first}"
: "${GH_REPO:?set GH_REPO to owner/repo first}"

sudo apt-get update -y && sudo apt-get install -y python3 python3-pip git
sudo mkdir -p /opt/excava && sudo chown "$USER" /opt/excava
cd /opt/excava
if [ ! -d repo ]; then
  git clone "https://x-access-token:${GH_TOKEN}@github.com/${GH_REPO}.git" repo
fi
cd repo
git config user.name "excava-vps"
git config user.email "excava-vps@users.noreply.github.com"

# engine keys template (fill from your GitHub secrets page; the beat reads these env names)
if [ ! -f /opt/excava/env ]; then
  cat > /opt/excava/env <<'EOF'
GROQ_API_KEY=
GROQ_API_KEY_2=
SAMBANOVA_API_KEY=
MISTRAL_API_KEY=
GH_MODELS_TOKEN=
CEREBRAS_API_KEY=
GEMINI_API_KEY=
GEMINI_API_KEY_2=
OPENROUTER_API_KEY=
EOF
  echo ">>> EDIT /opt/excava/env and paste your keys (same names as GitHub secrets) <<<"
fi

# the beat unit: pull -> beat -> commit -> push, every 5 minutes, forever
sudo tee /etc/systemd/system/excava-beat.service >/dev/null <<EOF
[Unit]
Description=EXCAVA beat (one cycle)
[Service]
Type=oneshot
User=$USER
WorkingDirectory=/opt/excava/repo
EnvironmentFile=/opt/excava/env
ExecStart=/bin/bash -c 'git pull --rebase --autostash origin main || true; \
python3 -m src.excava || true; git add data; \
git commit -m "excava-vps beat: \$(date -u +%%Y-%%m-%%dT%%H:%%MZ)" || true; git push || true'
EOF

sudo tee /etc/systemd/system/excava-beat.timer >/dev/null <<EOF
[Unit]
Description=EXCAVA beat every 5 minutes, 24/7
[Timer]
OnBootSec=2min
OnUnitActiveSec=5min
[Install]
WantedBy=timers.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now excava-beat.timer
echo "═══ EXCAVA VPS beat installed: every 5 minutes, 24/7. Check: systemctl list-timers excava-beat.timer ═══"
