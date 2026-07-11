"""
src/excava_engines.py — M2.1: THE ENGINE LAYER. Real brains behind every agent.

The 9 already-wired FREE families stay first-class and directly callable:
  Gemini x6 (rotated) · Groq x2 · Cerebras x2 · OpenRouter (free DeepSeek R1 / Qwen3 Coder) ·
  NVIDIA Nemotron · SambaNova · Mistral · GitHub Models — plus optional self-hosted Hermes
  (Ollama) and the OPTIONAL OmniRoute gateway (additional central route, never the sole path:
  set OMNIROUTE_URL + OMNIROUTE_KEY and route="omniroute" becomes available; everything works
  with it off). Claude rides Eitan's Pro (CLAUDE_CODE_OAUTH_TOKEN_REAL workflows) — it is a
  PREMIUM session/CI engine, not an HTTP call from here; agents mark work "needs-claude" and
  the claude.yml lane picks it up.

pick_engine(dept, difficulty): fast-first (Cerebras/Groq) for the bulk -> Gemini/grounded
for hard -> premium marked for Claude-grade work. Keys absent -> engine skipped gracefully;
every completion records {engine, model, ms} so chat messages carry "agent · engine" truthfully.

Run: python -m src.excava_engines --selftest
"""
from __future__ import annotations

import argparse
import json
import os
import time
import urllib.request
from pathlib import Path

# (name, kind, base_url, model, env_keys[, tier])  kind: gemini | openai | ollama
# Order matters: pick_engine returns the FIRST available engine of the wanted tier, so the
# PROVEN-working engines lead. CI selftest 2026-07-06 (run 28817002526): groq/sambanova/mistral/
# gh-models answer; cerebras 404s (bad model id — parked last); all Gemini keys are 429-exhausted
# by the analysis pipeline, so Gemini is NOT first-line for chat anymore.
CATALOG = [
    ("groq",       "openai", "https://api.groq.com/openai/v1",        "llama-3.3-70b-versatile",
     ["GROQ_API_KEY", "GROQ_API_KEY_2"], "fast"),
    ("sambanova",  "openai", "https://api.sambanova.ai/v1",           "Meta-Llama-3.3-70B-Instruct",
     ["SAMBANOVA_API_KEY"], "fast"),
    ("mistral",    "openai", "https://api.mistral.ai/v1",             "mistral-small-latest",
     ["MISTRAL_API_KEY"], "fast"),
    ("gh-models",  "openai", "https://models.github.ai/inference",    "openai/gpt-4o-mini",
     ["GH_MODELS_TOKEN", "GITHUB_TOKEN"], "grounded"),
    ("cerebras",   "openai", "https://api.cerebras.ai/v1",            "llama3.3-70b",
     ["CEREBRAS_API_KEY", "CEREBRAS_API_KEY_2"], "fast"),
    ("gemini",     "gemini", "",                                      "gemini-2.0-flash",
     ["EXTERNAL_REVIEW_API_KEY", "GEMINI_API_KEY", "GEMINI_API_KEY_2", "GEMINI_API_KEY_3",
      "GEMINI_API_KEY_4", "GEMINI_API_KEY_5", "GEMINI_API_KEY_6"], "grounded"),
    ("openrouter", "openai", "https://openrouter.ai/api/v1",          "deepseek/deepseek-r1:free",
     ["OPENROUTER_API_KEY"], "reasoning"),
    ("nvidia",     "openai", "https://integrate.api.nvidia.com/v1",   "meta/llama-3.3-70b-instruct",
     ["NVIDIA_API_KEY"], "grounded"),
    ("hermes",     "ollama", "http://localhost:11434/v1",             "hermes3",
     [], "reasoning"),
    ("omniroute",  "openai", "",                                      "auto",
     ["OMNIROUTE_KEY"], "gateway"),
]
_ROT: dict = {}


def _key(env_keys: list) -> str:
    live = [os.environ.get(k, "").strip() for k in env_keys]
    live = [k for k in live if k]
    if not live:
        return ""
    name = env_keys[0]
    _ROT[name] = (_ROT.get(name, -1) + 1) % len(live)   # rotate multi-key families
    return live[_ROT[name]]


def _health_rank() -> dict:
    """Engine ranking from the hourly benchmark canary (src/excava_experiments.py). Empty dict
    if no report yet or it's stale (>2h) — then catalog order stands."""
    try:
        h = json.load(open(Path(__file__).parent.parent / "data" / "excava" / "engine_health.json",
                           encoding="utf-8"))
        from datetime import datetime, timezone
        age = (datetime.now(timezone.utc) - datetime.fromisoformat(h["generated_at"])).total_seconds()
        if age > 2 * 3600:
            return {}
        return {n: i for i, n in enumerate(h.get("ranking", []))}
    except Exception:
        return {}


def healthy(report: dict | None = None) -> list[dict]:
    """Engines that BOTH have a key here AND answered the last benchmark canary. This is the pool
    rooms round-robin over so a debate really crosses models. Falls back to available() when the
    canary has no healthy data (first run / all-outage) — better one engine than silence."""
    av = available()
    try:
        if report is None:
            report = json.load(open(Path(__file__).parent.parent / "data" / "excava"
                                    / "engine_health.json", encoding="utf-8"))
        good = {r["engine"] for r in report.get("results", [])
                if r.get("status") in ("healthy", "answering-but-sloppy")}
        pool = [e for e in av if e["name"] in good]
        return pool or av
    except Exception:
        return av


def available() -> list[dict]:
    """Engines whose keys/endpoints exist right now (never raises), ordered by measured health
    (benchmark ranking) when fresh, else catalog order."""
    out = []
    for name, kind, base, model, envs, tier in CATALOG:
        if name == "omniroute":
            base = os.environ.get("OMNIROUTE_URL", "").strip()
            if not base or not _key(envs):
                continue
        elif name == "hermes":
            if os.environ.get("HERMES_OLLAMA", "") != "1":
                continue                                  # opt-in: only when a local Ollama runs
        elif not _key(envs):
            continue
        out.append({"name": name, "kind": kind, "base": base, "model": model,
                    "envs": envs, "tier": tier})
    rank = _health_rank()
    if rank:
        out.sort(key=lambda e: rank.get(e["name"], 99))
    return out


def pick_engine(dept: str = "", difficulty: str = "normal") -> dict | None:
    """Routing policy: fast-first for the bulk; grounded/reasoning for hard; the security
    department always gets a grounded engine (its verdicts must not hallucinate)."""
    av = available()
    if not av:
        return None
    want = ("grounded", "reasoning") if (difficulty in ("hard", "grounded") or dept == "security") \
        else ("fast", "gateway", "grounded", "reasoning")
    for tier in want:
        for e in av:
            if e["tier"] == tier:
                return e
    return av[0]


def _gemini_text(key: str, model: str, prompt: str, timeout: int = 45) -> str:
    """Gemini generateContent for PLAIN free-form text (no forced JSON) — the chat/canary path."""
    url = (f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}")
    body = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode("utf-8")
    req = urllib.request.Request(url, data=body,
                                 headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        d = json.loads(resp.read().decode("utf-8", errors="replace"))
    return d["candidates"][0]["content"]["parts"][0]["text"]


def _call_one(e: dict, prompt: str, max_tokens: int = 700) -> dict:
    """ONE attempt at ONE engine — NO fallthrough. Returns {ok, text, ms, status, note}.
    status/note carry the REAL HTTP code + body snippet, so a failure reads as 'quota-429' /
    'bad-model-404' / 'bad-key-401', not a blank 'HTTPError'. This is the honest diagnosis the
    owner needs (2026-07-11: keys exist in repo secrets, yet engines fail — WHY matters)."""
    import urllib.error
    t0 = time.time()
    _ms = lambda: int((time.time() - t0) * 1000)
    try:
        if e["kind"] == "gemini":
            # PLAIN-TEXT gemini for CHAT — NOT bulk_analyze.call_gemini, which forces
            # responseMimeType=application/json + json.loads() and so throws on any free-form
            # reply like 'benchmark ok' (owner 2026-07-11: gemini keys exist yet gemini fails —
            # the chat path was wired to the analysis-JSON function). Analysis keeps its own path.
            text = _gemini_text(_key(e["envs"]), e["model"], prompt)
        else:
            key = _key(e["envs"]) if e["envs"] else "ollama"
            body = json.dumps({"model": e["model"], "max_tokens": max_tokens,
                               "messages": [{"role": "user", "content": prompt}]}).encode()
            req = urllib.request.Request(
                e["base"].rstrip("/") + "/chat/completions", data=body,
                headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                d = json.loads(resp.read().decode("utf-8", errors="replace"))
            text = d["choices"][0]["message"]["content"]
        text = str(text or "").strip()
        return {"ok": bool(text), "text": text, "ms": _ms(), "status": 200 if text else 0,
                "note": "" if text else "empty response"}
    except urllib.error.HTTPError as ex:
        try:
            snippet = ex.read().decode("utf-8", errors="replace")[:160]
        except Exception:
            snippet = ""
        klass = {429: "quota-429", 401: "bad-key-401", 403: "forbidden-403",
                 404: "bad-model-404", 400: "bad-request-400"}.get(ex.code, f"http-{ex.code}")
        return {"ok": False, "text": "", "ms": _ms(), "status": ex.code,
                "note": f"{klass}: {snippet}".strip()}
    except Exception as ex:
        return {"ok": False, "text": "", "ms": _ms(), "status": 0,
                "note": f"{type(ex).__name__}: {str(ex)[:120]}"}


def complete(prompt: str, engine: dict | None = None, dept: str = "",
             difficulty: str = "normal", max_tokens: int = 700) -> dict:
    """One completion. Returns {ok, text, engine, model, ms}. Falls through the canary-HEALTHY
    pool on failure — an outage never silences an agent, it just changes the badge. (Fallthrough
    is the HEALTHY pool, not the raw keyed list: a quota-dead engine used to eat a 60s timeout on
    every turn, leaving one survivor — the owner's 'agents aren't real' complaint, 2026-07-11.)"""
    tried = []
    pool = healthy()
    order = ([engine] if engine else []) + [e for e in pool if not engine or e["name"] != engine["name"]]
    if engine is None:
        first = pick_engine(dept, difficulty)
        order = ([first] if first else []) + [e for e in pool if not first or e["name"] != first["name"]]
    for e in order[:3]:
        r = _call_one(e, prompt, max_tokens)
        if r["ok"]:
            return {"ok": True, "text": r["text"], "engine": e["name"], "model": e["model"],
                    "ms": r["ms"]}
        tried.append(f"{e['name']}:{r['note'][:50]}")
    return {"ok": False, "text": "", "engine": "none", "model": "", "ms": 0,
            "error": "; ".join(tried) or "no engines configured"}


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    av = available()
    print(f"engines available here: {[e['name'] for e in av] or 'NONE (keys live in CI secrets)'}")
    if a.selftest:
        ok = 0
        for e in av:
            r = complete("Reply with exactly: OK", engine=e, max_tokens=8)
            print(f"  {e['name']:<11} {'PASS' if r['ok'] else 'fail'} "
                  f"({r['ms']}ms) {r.get('error', '')[:60]}")
            ok += r["ok"]
        print(f"selftest: {ok}/{len(av)} engines answered"
              + ("" if av else " — run inside CI (engine_selftest.yml) where the keys live"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
