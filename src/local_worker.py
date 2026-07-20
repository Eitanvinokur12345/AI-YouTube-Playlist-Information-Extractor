"""src/local_worker.py — the LOCAL DRAIN: unattended enrichment on the owner's machine.

The stub problem is a race: mining ADDS stubs every beat, but LLM enrichment only ran when a
live session drove it (CI's free keys are usually 429-dead, so the CI lane degrades to keyless).
This worker is the fix — the owner's PC/VPS becomes a real enrichment host:

  take the run lock → RECOVER: if a killed run left owner files dirty, ship them first →
  ensure Ollama is up (start it if the machine rebooted) → hold the machine awake → run ONE
  deep_retrieve batch on the zero-quota local brain → record the result to
  data/excava/local_worker.json (the cockpit's G-O guardrail reads it — CI included,
  offline/online parity via the committed file) → ship via git_safe (commit → sync → push →
  verify). Kill it anywhere (sleep, logoff, reboot): the next run ships the work in seconds.

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
LOCK = ROOT / "data" / "excava" / "local_worker.lock"
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


# Eitan's A2 verdict (2026-07-20): SEVERAL different local model FAMILIES, not one — the
# drain alternates families by hour, so even the local tier has real diversity.
MODELS = [m.strip() for m in os.environ.get(
    "LOCAL_DRAIN_MODELS", "llama3.2:3b,qwen2.5:3b").split(",") if m.strip()]


def pick_model() -> str:
    from datetime import datetime, timezone as _tz
    return MODELS[datetime.now(_tz.utc).hour % max(len(MODELS), 1)]


def run_batch(model: str) -> dict:
    """One deep_retrieve batch with the local brain; parse its honest summary line.
    HARD 25-min ceiling: Ollama STREAMS, so a starved trickling response resets every
    per-read socket timeout — the 22:01Z-hour run zombied 51 min at 1.3 CPU-sec. The
    ceiling kills honestly; leftovers ship at the next run's recovery step."""
    env = dict(os.environ)
    env["HERMES_OLLAMA"] = "1"
    env["OLLAMA_MODEL"] = model
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, "-m", "src.deep_retrieve", "--limit", str(BATCH)],
                           cwd=str(ROOT), env=env, capture_output=True, text=True, timeout=1500)
        out = (r.stdout or "") + (r.stderr or "")
        rc = r.returncode
    except subprocess.TimeoutExpired as e:
        out = ((e.stdout or b"").decode("utf-8", "replace") if isinstance(e.stdout, bytes)
               else (e.stdout or ""))
        out += "\nbatch hit the 25-min ceiling — killed (likely a trickling stream); " \
               "partial work ships via the next run's recovery"
        rc = -1
    m = re.search(r"(\d+) enriched \((\d+) descriptions upgraded\); stubs now (\d+)", out)
    return {"ok": rc == 0 and bool(m),
            "enriched": int(m.group(1)) if m else 0,
            "upgraded": int(m.group(2)) if m else 0,
            "stubs": int(m.group(3)) if m else -1,
            "minutes": round((time.time() - t0) / 60, 1),
            "tail": out.strip().splitlines()[-1][:200] if out.strip() else "(no output)"}


def _keep_awake(active: bool) -> None:
    """Hold the machine awake ONLY while a batch runs. The 18:19Z run died with 0xC000013A
    (sleep/logoff mid-batch) and stranded real enrichment in the working tree."""
    try:
        import ctypes  # ES_CONTINUOUS | ES_SYSTEM_REQUIRED while active; ES_CONTINUOUS to release
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000001 if active else 0x80000000)
    except Exception:
        pass


def owner_dirty() -> list:
    """The files this drain owns (owner per-type files + evidence + state + status + the WHY
    chain in project memory) that are modified RIGHT NOW. A non-empty answer at startup means
    an interrupted run left real work stranded in the tree."""
    from src import element_model as em
    candidates = [f"data/{spec[0]}" for spec in em.TYPES.values()]
    candidates += ["data/element_overrides.json", "data/deep_retrieve_state.json",
                   "data/excava/local_worker.json",
                   # the WHY log this worker writes AFTER shipping: without these in the ship
                   # set, the next run's sync (git_safe revert_ci_churn on data/) erases it.
                   "data/project_memory/episodes.jsonl", "data/project_memory/graph.json",
                   "data/project_memory/state.json"]
    changed = subprocess.run(["git", "status", "--porcelain", "--", *candidates],
                             cwd=str(ROOT), capture_output=True, text=True).stdout
    return [ln[3:].strip() for ln in changed.splitlines() if ln.strip()]


def ship(files: list, msg: str) -> str:
    """git_safe does the whole safe dance: commit -> bundle (on D:) -> sync -> push -> verify.
    Commit-FIRST is what makes this kill-safe: a bare sync reverts uncommitted data/ churn."""
    if not files:
        return "nothing to ship"
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

    # One drain at a time: a fresh lock means another run (scheduled or manual) is live.
    # A lock older than 50 min is a corpse from a killed run — take over.
    try:
        if LOCK.exists() and time.time() - LOCK.stat().st_mtime < 3000:
            print("local-drain: another run holds the lock — skipping")
            return 0
        LOCK.parent.mkdir(parents=True, exist_ok=True)
        LOCK.write_text(str(os.getpid()), encoding="utf-8")
    except Exception:
        pass

    _keep_awake(True)
    try:
        recovered = 0
        if not a.no_ship:
            leftovers = owner_dirty()   # a killed run's work ships FIRST — before Ollama,
            if leftovers:               # before the new batch. Never strand enrichment twice.
                recovered = len(leftovers)
                out = ship(leftovers, "local-drain: RECOVERED — an interrupted run's work "
                                      "ships before the new batch (kill-safe drain)")
                print(f"local-drain: RECOVERY of {recovered} stranded file(s): {out}")

        model = pick_model()
        status = {"at": _now(), "host": os.environ.get("COMPUTERNAME", "local"),
                  "model": model, "batch_limit": BATCH}
        if recovered:
            status["recovered_files"] = recovered
        if not ensure_ollama():
            status.update({"ok": False, "note": "Ollama not reachable and could not be started"})
            STATUS.write_text(json.dumps(status, ensure_ascii=False, indent=1), encoding="utf-8")
            print("local-drain: OLLAMA DOWN — nothing done")
            return 1

        batch = run_batch(model)
        status.update({"ok": batch["ok"], **{k: batch[k] for k in
                       ("enriched", "upgraded", "stubs", "minutes")}, "note": batch["tail"]})
        STATUS.parent.mkdir(parents=True, exist_ok=True)
        STATUS.write_text(json.dumps(status, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"local-drain: {batch['tail']}")

        if not a.no_ship:
            msg = (f"local-drain: {batch['enriched']} enriched ({batch['upgraded']} upgraded), "
                   f"stubs {batch['stubs']} — unattended batch on the owner's machine "
                   f"(zero-quota local brain, {batch['minutes']} min)")
            print(f"local-drain: {ship(owner_dirty(), msg)}")
        try:                                # the WHY chain survives unattended runs too
            from src.project_memory import log_manual
            log_manual(f"local-drain batch: {batch['enriched']} enriched, stubs {batch['stubs']}",
                       "unattended enrichment on the owner's machine — the stub race is only won "
                       "if the drain runs when no one is watching", ["data/excava/local_worker.json"],
                       by="local-worker")
        except Exception:
            pass
        return 0
    finally:
        _keep_awake(False)
        try:
            LOCK.unlink()
        except Exception:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
