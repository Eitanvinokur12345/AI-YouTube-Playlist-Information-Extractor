"""
src/resource_check.py — do we HAVE what a task needs, before anyone starts it?

The owner's rule: check resources before carrying out tasks. This inventories everything the system
depends on — engine keys, daily Gemini video quota, special secrets (residential proxy, Bright Data),
the data library itself — and derives a `can_do` map per task type. EXCAVA consults it before picking
up work (missing resource → task HELD with the reason, not attempted); the cockpit shows it as a fuel
gauge. Runs in CI where the secrets live (locally it just reports what's visible). Free, stdlib.

Run:  python -m src.resource_check
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "resources.json"
NOW = datetime.now(timezone.utc)

ENGINE_VARS = (["EXTERNAL_REVIEW_API_KEY", "GEMINI_API_KEY"] + [f"GEMINI_API_KEY_{i}" for i in range(2, 9)]
               + ["GROQ_API_KEY", "GROQ_API_KEY_2", "CEREBRAS_API_KEY", "CEREBRAS_API_KEY_2",
                  "GH_MODELS_TOKEN", "OPENROUTER_API_KEY", "NVIDIA_API_KEY", "SAMBANOVA_API_KEY",
                  "MISTRAL_API_KEY"])


def _load(name, d=None):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return d if d is not None else {}


def _env(n):
    return bool((os.environ.get(n) or "").strip())


def main() -> int:
    gem = [n for n in ENGINE_VARS if n.startswith(("GEMINI", "EXTERNAL")) and _env(n)]
    fast = [n for n in ("GROQ_API_KEY", "GROQ_API_KEY_2", "CEREBRAS_API_KEY", "CEREBRAS_API_KEY_2",
                        "SAMBANOVA_API_KEY") if _env(n)]
    engines = [n for n in ENGINE_VARS if _env(n)]
    today = NOW.strftime("%Y-%m-%d")
    used_watch = (_load("gemini_analyzed.json").get("daily", {}) or {}).get(today, 0)
    used_visual = (_load("visual_state.json").get("daily", {}) or {}).get(today, 0)
    watch_budget = 440 * max(len(gem), 1)
    visual_budget = 300 * max(len(gem), 1)
    lib_ok = len(_load("tools.json").get("tools", [])) > 500 and len(_load("skills.json").get("skills", [])) > 500
    mem_vecs = len(_load("memory_index.json").get("vectors", {}))

    resources = {
        "engine_keys": {"ok": len(engines) >= 3, "have": len(engines),
                        "note": f"{len(engines)} engine keys visible ({len(gem)} Gemini, {len(fast)} fast)"},
        "gemini_video_quota": {"ok": bool(gem) and used_watch < watch_budget * 0.9,
                               "note": f"watch {used_watch}/{watch_budget}m + visual {used_visual}/{visual_budget}m used today"},
        "yt_proxy": {"ok": _env("YT_PROXY_URL"),
                     "note": "residential proxy for transcripts" if _env("YT_PROXY_URL")
                             else "MISSING — add secret YT_PROXY_URL to unlock the transcript lane (~100x analysis)"},
        "brightdata": {"ok": _env("BRIGHTDATA_API_TOKEN"), "note": "Bright Data web token (5k req/mo free)"},
        "github_token": {"ok": _env("GITHUB_TOKEN") or _env("GH_TOKEN"), "note": "commit/push from CI"},
        "library": {"ok": lib_ok, "note": "data library intact" if lib_ok else "LIBRARY LOOKS COLLAPSED — data_guard should restore"},
        "semantic_memory": {"ok": mem_vecs > 200, "note": f"{mem_vecs} vectors"},
    }
    # what each TASK TYPE needs -> can we do it right now?
    can_do = {
        "resolve-links": {"ok": len(engines) >= 1, "needs": "any engine key"},
        "analyze-videos": {"ok": resources["gemini_video_quota"]["ok"], "needs": "Gemini key + daily video quota"},
        "visual-extract": {"ok": bool(gem) and used_visual < visual_budget * 0.9, "needs": "Gemini key + visual quota"},
        "fetch-transcripts": {"ok": _env("YT_PROXY_URL"), "needs": "YT_PROXY_URL secret (residential proxy)"},
        "embed-memory": {"ok": bool(gem), "needs": "Gemini key"},
        "mine-competitors": {"ok": True, "needs": "network only (free)"},
        "screenshots-designs": {"ok": True, "needs": "free screenshot services"},
        "create-drafts": {"ok": len(engines) >= 3 and lib_ok, "needs": "engine pool + intact library"},
    }
    missing = [k for k, v in resources.items() if not v["ok"]]
    OUT.write_text(json.dumps({"generated_at": NOW.isoformat(), "in_ci": _env("GITHUB_ACTIONS"),
                               "resources": resources, "can_do": can_do, "missing": missing},
                              ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"resource_check: {len(engines)} engines; missing: {', '.join(missing) or 'nothing critical'}; "
          f"can_do: {sum(1 for v in can_do.values() if v['ok'])}/{len(can_do)} task types.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
