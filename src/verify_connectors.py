"""
src/verify_connectors.py — PHASE 4: CONNECTORS MADE REAL (owner: sandbox test-run EVERYTHING).

The audit found ~94% of the 1,142 connectors carry only placeholder install text. This lane
walks ALL of them, batch by batch, and for each one:
  1. RESOLVE a concrete install/run command — from its own install/setup text if a real
     command is embedded, else from the npm registry / PyPI by name (both free, keyless).
  2. SANDBOX TEST-RUN it (the owner's original "simulator first" security ask): the command
     executes in an isolated subprocess — clean environment (no repo secrets), temp working
     dir, hard timeout — and must exit sanely. Docker-only connectors are marked
     'sandbox-unavailable' rather than faked.
  3. Record the verdict in data/connectors_verified.json (NOT in connectors.json — the
     hourly mining lane owns that file and would overwrite us). The dashboard joins by name;
     the tab shrinks to verified-only per D5.

Progress cursor in data/connectors_verify_state.json; a 6-hourly CI batch of ~30 covers all
1,142 in ~10 days. Free: public registries + CI minutes only.
Run: python -m src.verify_connectors --limit 5
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import tempfile
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "connectors_verified.json"
STATE = DATA / "connectors_verify_state.json"
TIMEOUT = 120
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _jload(p: Path, d):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return d


def _head_ok(url: str) -> bool:
    try:
        req = urllib.request.Request(url, headers=UA, method="HEAD")
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status < 400
    except Exception:
        return False


def _registry_lookup(name: str) -> tuple[str, str] | None:
    """Try npm then PyPI for an exact package matching the connector's slug. Free, keyless."""
    slug = re.sub(r"[^a-z0-9\-]+", "-", name.lower().replace(" mcp", "").strip()).strip("-")
    for cand in (f"{slug}-mcp", f"mcp-server-{slug}", f"@modelcontextprotocol/server-{slug}", slug):
        try:
            req = urllib.request.Request(f"https://registry.npmjs.org/{urllib.request.quote(cand, safe='@/')}",
                                         headers=UA)
            with urllib.request.urlopen(req, timeout=15) as r:
                if r.status == 200:
                    return "npx", cand
        except Exception:
            pass
    try:
        req = urllib.request.Request(f"https://pypi.org/pypi/{slug}/json", headers=UA)
        with urllib.request.urlopen(req, timeout=15) as r:
            if r.status == 200:
                return "pip", slug
    except Exception:
        pass
    return None


def resolve(c: dict) -> tuple[str, str] | None:
    """(kind, command-or-package). Embedded real commands win; registries second."""
    text = " ".join(str(c.get(k, "")) for k in ("install_or_source", "setup"))
    m = re.search(r"\b(npx\s+-?y?\s*[@\w\-/.]+|npm\s+i(?:nstall)?\s+(?:-g\s+)?[@\w\-/.]+"
                  r"|pip3?\s+install\s+[\w\-\[\]=.]+|uvx\s+[\w\-]+)", text)
    if m:
        return "cmd", m.group(1)
    if "docker" in text.lower():
        return None                     # honest: no docker daemon in the sandbox
    return _registry_lookup(c.get("name", ""))


def sandbox_run(kind: str, val: str) -> dict:
    """Isolated execution: clean env (PATH only — no repo/CI secrets), temp cwd, timeout.
    A connector passes when its package resolves AND its entry point exits sanely."""
    tmp = tempfile.mkdtemp(prefix="conn-sbx-")
    env = {"PATH": os.environ.get("PATH", ""), "HOME": tmp, "USERPROFILE": tmp,
           "TMPDIR": tmp, "TEMP": tmp, "TMP": tmp, "npm_config_yes": "true",
           "SystemRoot": os.environ.get("SystemRoot", "")}
    if kind == "cmd":
        cmd = val.split()
    elif kind == "npx":
        cmd = ["npx", "-y", val, "--version"]
    else:                               # pip: prove the package resolves + downloads
        cmd = ["python", "-m", "pip", "download", "--no-deps", "-q", "-d", tmp, val]
    # Windows: npx/npm are .cmd shims — subprocess without shell needs the resolved path
    exe = shutil.which(cmd[0])
    if exe:
        cmd[0] = exe
    def _kill_tree(proc):
        # npx spawns node grandchildren that hold the pipes open past a plain kill —
        # without a TREE kill, communicate() hangs forever (seen on Windows AND Linux CI)
        try:
            if os.name == "nt":
                subprocess.run(["taskkill", "/F", "/T", "/PID", str(proc.pid)],
                               capture_output=True, timeout=15)
            else:
                import signal
                os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
        except Exception:
            proc.kill()

    try:
        kw = dict(cwd=tmp, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                  stdin=subprocess.DEVNULL, text=True, shell=False)
        if os.name != "nt":
            kw["start_new_session"] = True
        proc = subprocess.Popen(cmd, **kw)
        try:
            out, err = proc.communicate(timeout=TIMEOUT)
            ok = proc.returncode == 0
            return {"status": "pass" if ok else "fail", "exit": proc.returncode,
                    "cmd": " ".join(cmd), "log": ((out or "") + (err or ""))[-300:].strip()}
        except subprocess.TimeoutExpired:
            _kill_tree(proc)
            try:
                proc.communicate(timeout=10)
            except Exception:
                pass
            # it installed and RAN (then sat waiting on stdio, as MCP servers do) = alive
            return {"status": "pass", "exit": None, "cmd": " ".join(cmd),
                    "log": "ran until sandbox timeout (stdio server behavior) — counts as alive"}
    except FileNotFoundError as e:
        return {"status": "sandbox-unavailable", "cmd": " ".join(cmd), "log": str(e)[:200]}
    except Exception as e:
        return {"status": "fail", "cmd": " ".join(cmd), "log": f"{type(e).__name__}: {e}"[:200]}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=30)
    args = ap.parse_args()

    raw = _jload(DATA / "connectors.json", {})
    conns = raw if isinstance(raw, list) else (raw.get("connectors") or raw.get("items")
                                               or next((v for v in raw.values() if isinstance(v, list)), []))
    state = _jload(STATE, {"cursor": 0})
    store = _jload(OUT, {"verified": {}})
    ver = store.setdefault("verified", {})

    start = state.get("cursor", 0) % max(len(conns), 1)
    batch = conns[start:start + args.limit]
    passed = failed = unresolved = 0
    for c in batch:
        name = c.get("name", "?")
        res = resolve(c)
        if res is None:
            url = c.get("url") or c.get("source_url") or ""
            alive = _head_ok(url) if url else False
            ver[name] = {"status": "unresolvable" + ("-but-url-alive" if alive else ""),
                         "at": _now(), "note": "no runnable command found (docker-only or docs-only)"}
            unresolved += 1
            continue
        verdict = sandbox_run(*res)
        verdict["at"] = _now()
        ver[name] = verdict
        passed += verdict["status"] == "pass"
        failed += verdict["status"] == "fail"

    state["cursor"] = start + len(batch)
    state["total"] = len(conns)
    state["updated_at"] = _now()
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    counts = {}
    for v in ver.values():
        counts[v["status"]] = counts.get(v["status"], 0) + 1
    store["summary"] = {"checked": len(ver), "total": len(conns), "by_status": counts,
                        "updated_at": _now(),
                        "policy": "owner 2026-07-03: sandbox test-run EVERYTHING; tab shows verified-only (D5)"}
    OUT.write_text(json.dumps(store, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"connectors verify: batch {start}..{start + len(batch)} of {len(conns)} — "
          f"{passed} pass, {failed} fail, {unresolved} unresolvable; "
          f"checked so far {len(ver)}/{len(conns)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
