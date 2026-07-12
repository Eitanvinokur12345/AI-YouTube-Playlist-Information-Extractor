# Oracle Cloud signup — the 10-minute guide (R1, approved 2026-07-12)

Goal: one free VM that runs EXCAVA's beat every 5 minutes, 24/7, forever. Oracle's
"Always Free" tier is genuinely free — no time limit — as long as you never click "upgrade".

## Part A — the account (~5 min)
1. Go to **oracle.com/cloud/free** → press **Start for free**.
2. Country: Israel · your email + name → **Verify my email** (check your inbox, click the link).
3. Password; Customer type: **Individual**. Cloud Account Name: anything (e.g. `eitan-excava`).
4. **Home Region — choose carefully, it can't be changed.** Recommended: **Germany Central
   (Frankfurt)** or **Netherlands Northwest (Amsterdam)**. (Free ARM machines are scarce in
   busy regions; these two are usually OK. If "out of capacity" hits later, the fallback
   machine in Part B always works.)
5. Address + phone (SMS verification).
6. **Payment verification**: they ask for a card to prove you're human. A ~$1 hold appears
   and disappears; **Always Free never charges** unless YOU explicitly upgrade to a paid
   account. Don't upgrade, and it stays free forever.
7. Wait a few minutes for the "your account is ready" email → sign in to the console.

## Part B — the machine (~3 min)
1. Console menu ☰ → **Compute → Instances → Create instance**.
2. Name: `excava` · Image: **Ubuntu 22.04** (Canonical).
3. Shape → Change shape → **Ampere · VM.Standard.A1.Flex** → 2 OCPUs, 12 GB (inside the
   always-free 4 OCPU / 24 GB). If it says *out of capacity*: pick **AMD ·
   VM.Standard.E2.1.Micro** instead (always available, always free, enough for the beat).
4. Networking: leave defaults.
5. **SSH keys: choose "Generate a key pair for me" and press DOWNLOAD PRIVATE KEY** — save
   the file somewhere safe (e.g. `C:\Users\eitan\excava-vps.key`). Without it you can't get in.
6. **Create**. When it turns green, copy the **Public IP address**.

## Part C — EXCAVA moves in (~2 min)
1. On GitHub: **Settings → Developer settings → Fine-grained tokens → Generate new token** —
   Repository access: ONLY this repo · Permissions: **Contents: Read and write** → copy it.
2. On your PC, open PowerShell:
   `ssh -i C:\Users\eitan\excava-vps.key ubuntu@<the-public-IP>`   (answer `yes` once)
3. On the VM, paste (with your token filled in):
   ```
   export GH_TOKEN=paste_token_here
   export GH_REPO=Eitanvinokur12345/AI-YouTube-Playlist-Information-Extractor
   curl -fsSL https://raw.githubusercontent.com/$GH_REPO/main/deploy/vps_setup.sh | bash
   ```
4. Paste your engine keys into the file it tells you about:  `nano /opt/excava/env`
   (same names/values as your GitHub secrets page; Ctrl+O Enter, Ctrl+X to save/exit).
5. Done. Check it's alive: `systemctl list-timers excava-beat.timer`
   From now on the beat runs every 5 minutes even with your PC off. The GitHub cron keeps
   running too as a fallback — they share the same bus and don't collide.
