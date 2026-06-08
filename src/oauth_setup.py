"""
src/oauth_setup.py — ONE-TIME local helper to let Excavatortron edit your YouTube playlist.

What it does: opens your browser, you sign in to the Google account that OWNS the playlist and
consent, and it prints the three values to store as GitHub repo secrets so the cloud can add
approved videos for you. The refresh token never expires unless you revoke it; it stays in
GitHub secrets (never in the repo).

Before running, get an OAuth client:
  1. Google Cloud Console -> the project where your YouTube API key lives.
  2. APIs & Services -> Credentials -> Create credentials -> OAuth client ID -> type "Desktop app".
  3. Download its JSON (call it client_secret.json).
Then:
  pip install google-auth-oauthlib google-api-python-client
  python -m src.oauth_setup client_secret.json
"""
from __future__ import annotations

import json
import sys


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python -m src.oauth_setup path/to/client_secret.json")
        return
    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
    except Exception:
        print("Missing dep. Run:  pip install google-auth-oauthlib google-api-python-client")
        return
    path = sys.argv[1]
    flow = InstalledAppFlow.from_client_secrets_file(
        path, scopes=["https://www.googleapis.com/auth/youtube"])
    creds = flow.run_local_server(port=0)  # opens the browser for sign-in + consent
    cs = json.load(open(path, encoding="utf-8"))
    inst = cs.get("installed") or cs.get("web") or {}
    print("\n=== Add these THREE as GitHub repo secrets (Settings -> Secrets and variables -> Actions) ===")
    print("YOUTUBE_OAUTH_CLIENT_ID      =", inst.get("client_id"))
    print("YOUTUBE_OAUTH_CLIENT_SECRET  =", inst.get("client_secret"))
    print("YOUTUBE_OAUTH_REFRESH_TOKEN  =", creds.refresh_token)
    print("============================================================================================")
    print("After saving them, the daily 'Suggest sources' workflow adds approved videos automatically.")


if __name__ == "__main__":
    main()
