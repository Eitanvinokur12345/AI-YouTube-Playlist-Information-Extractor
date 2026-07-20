"""src/local_worker.py — the LOCAL DRAIN: unattended enrichment on the owner's machine.

The stub problem is a race: mining ADDS stubs every beat, but LLM enrichment only ran when a
live session drove it (CI's free keys are usually 429-dead, so the CI lane degrades to keyless).
This worker is the fix — the owner's PC/VPS becomes a real enrichment host:

  ensure Ollama is up (start it if the machine rebooted) → run ONE deep_retrieve batch on the
  zero-quota local brain → record the result to data/excava/local_worker.json (the cockpit's
  G-O guardrail reads it — CI included, offline/online parity via the committed file) → ship
  the enriched owner files via git_safe (commit → sync → push → verify).

Registered as a Windows scheduled task (hourly, user session). Safe to run any time by hand:
  python -m src.local_worker            one batch + ship
  python -m src.local_worker --no-ship  one batch, leave the tree for a human session
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
STATUS = ROOT / "data" / "excava" / "local_worker.json"
OLLAMA_EXE = os.environ.get("OLLAMA_EXE", r"D:\excava\ollama\bin\ollama.exe")
OLLAMA_URL = "http://localhost:11434"
BATCH = int(os.environ.get("LOCAL_DRAIN_BATCH", "25"))


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def ollama_up(timeout: int = 4) -> bool:
    try:
        with urllib.request.urlopen(f"{OLLAMA_URL}/api/version", timeout=timeout):
            return True
    except Exception:
        return False


def ensure_ollama() -> bool:
    """The reboot-survival trick: if the server is down, start it (models dir on D:)."""
    if ollama_up():
        return True
    if not Path(OLLAMA_EXE).exists():
        return False
    env = dict(os.environ)
    env.setdefault("OLLAMA_MODELS", r"D:\excava\ollama\models")
    subprocess.Popen([OLLAMA_EXE, "serve"], env=env,
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                     creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    for _ in range(15):
        time.sleep(2)
        if ollama_up():
            return True
    return False


def run_batch() -> dict:
    """One deep_retrieve batch with the local brain; parse its honest summary line."""
    env = dict(os.environ)
    env["HERMES_OLLAMA"] = "1"
    env.setdefault("OLLAMA_MODEL", "llama3.2:3b")
    t0 = time.time()
    r = subprocess.run([sys.executable, "-m", "src.deep_retrieve", "--limit", str(BATCH)],
                       cwd=str(ROOT), env=env, capture_output=True, text=True, timeout=3000)
    out = (r.stdout or "") + (r.stderr or "")
    m = re.search(r"(\d+) enriched \((\d+) descriptions upgraded\); stubs now (\d+)", out)
    return {"ok": r.returncode == 0 and bool(m),
            "enriched": int(m.group(1)) if m else 0,
            "upgraded": int(m.group(2)) if m else 0,
            "stubs": int(m.group(3)) if m else -1,
            "minutes": round((time.time() - t0) / 60, 1),
            "tail": out.strip().splitlines()[-1][:200] if out.strip() else "(no output)"}


def ship(batch: dict) -> str:
    """Ship exactly the files enrichment owns (owner per-type files + evidence + state + status).
    git_safe does the whole safe dance: commit -> bundle (on D:) -> sync -> push -> verify."""
    from src import element_model as em
    candidates = [f"data/{spec[0]}" for spec in em.TYPES.values()]
    candidates += ["data/element_overrides.json", "data/deep_retrieve_state.json",
                   "data/excava/local_worker.json"]
    changed = subprocess.run(["git", "status", "--porcelain", "--", *candidates],
                             cwd=str(ROOT), capture_output=True, text=True).stdout
    files = [ln[3:].strip() for ln in changed.splitlines() if ln.strip()]
    if not files:
        return "nothing to ship"
    msg = (f"local-drain: {batch['enriched']} enriched ({batch['upgraded']} upgraded), "
           f"stubs {batch['stubs']} — unattended batch on the owner's machine "
           f"(zero-quota local brain, {batch['minutes']} min)")
    r = subprocess.run([sys.executable, "-m", "src.git_safe", "ship", "-m", msg, "-a", *files],
                       cwd=str(ROOT), capture_output=True, text=True, timeout=600)
    tail = (r.stdout or r.stderr or "").strip().splitlines()
    return tail[-1][:160] if tail else "ship: no output"


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-ship", action="store_true")
    a = ap.parse_args()

    status = {"at": _now(), "host": os.environ.get("COMPUTERNAME", "local"),
              "model": os.environ.get("OLLAMA_MODEL", "llama3.2:3b"), "batch_limit": BATCH}
    if not ensure_ollama():
        status.update({"ok": False, "note": "Ollama not reachable and could not be started"})
        STATUS.write_text(json.dumps(status, ensure_ascii=False, indent=1), encoding="utf-8")
        print("local-drain: OLLAMA DOWN — nothing done")
        return 1

    batch = run_batch()
    status.update({"ok": batch["ok"], **{k: batch[k] for k in
                   ("enriched", "upgraded", "stubs", "minutes")}, "note": batch["tail"]})
    STATUS.parent.mkdir(parents=True, exist_ok=True)
    STATUS.write_text(json.dumps(status, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"local-drain: {batch['tail']}")

    if not a.no_ship:
        print(f"local-drain: {ship(batch)}")
    try:                                    # the WHY chain survives unattended runs too
        from src.project_memory import log_manual
        log_manual(f"local-drain batch: {batch['enriched']} enriched, stubs {batch['stubs']}",
                   "unattended enrichment on the owner's machine — the stub race is only won "
                   "if the drain runs when no one is watching", ["data/excava/local_worker.json"],
                   by="local-worker")
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
