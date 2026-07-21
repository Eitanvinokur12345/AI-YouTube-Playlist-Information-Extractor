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
    ("cerebras",   "openai", "https://api.cerebras.ai/v1",            "llama3.1-8b",
     ["CEREBRAS_API_KEY", "CEREBRAS_API_KEY_2"], "fast"),
    ("gemini",     "gemini", "",                                      "gemini-2.0-flash",
     ["EXTERNAL_REVIEW_API_KEY", "GEMINI_API_KEY", "GEMINI_API_KEY_2", "GEMINI_API_KEY_3",
      "GEMINI_API_KEY_4", "GEMINI_API_KEY_5", "GEMINI_API_KEY_6"], "grounded"),
    ("openrouter", "openai", "https://openrouter.ai/api/v1",          "deepseek/deepseek-chat-v3-0324:free",
     ["OPENROUTER_API_KEY"], "reasoning"),
    ("nvidia",     "openai", "https://integrate.api.nvidia.com/v1",   "meta/llama-3.3-70b-instruct",
     ["NVIDIA_API_KEY"], "grounded"),
    # ── M2 BRAIN FAMILIES — distinct model LINEAGES (§2), free via OpenRouter's :free tier. They
    # answer only where OPENROUTER_API_KEY lives (CI / the VPS, §12). IDs track the plan's targets
    # (GLM-5.2 / DeepSeek V4 / Kimi K2.7) — bump each when the free tier lists the newer release.
    ("glm",        "openai", "https://openrouter.ai/api/v1",          "z-ai/glm-4.5-air:free",
     ["OPENROUTER_API_KEY"], "grounded"),
    ("deepseek",   "openai", "https://openrouter.ai/api/v1",          "deepseek/deepseek-chat-v3-0324:free",
     ["OPENROUTER_API_KEY"], "reasoning"),
    ("kimi",       "openai", "https://openrouter.ai/api/v1",          "moonshotai/kimi-k2:free",
     ["OPENROUTER_API_KEY"], "reasoning"),
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


# Model LINEAGE per engine — §2 diversity is about training lineage, NOT provider. groq / cerebras /
# sambanova / nvidia ALL serve the same llama-3.3-70b, so three of them in a "debate" is same-model
# correlated errors (banned). The OpenRouter fallback resolves to deepseek here too.
LINEAGE = {
    "groq": "llama", "cerebras": "llama", "sambanova": "llama", "nvidia": "llama",
    "gh-models": "gpt", "gemini": "gemini", "mistral": "mistral",
    "glm": "glm", "deepseek": "deepseek", "openrouter": "deepseek", "kimi": "kimi",
    "hermes": "qwen-local", "omniroute": "gateway",
}


def debate_engines(n: int = 3) -> list[dict]:
    """The Router's cross-family pick: up to n engines of DISTINCT model LINEAGES, health-ordered.
    This is what makes a debate REAL diversity (§2) — never two providers of one model, never the
    same lineage twice (correlated errors). Fewer than n families available -> return what exists."""
    seen, out = set(), []
    for e in healthy():
        lin = LINEAGE.get(e["name"], e["name"])
        if lin in seen:
            continue
        seen.add(lin)
        out.append(e)
        if len(out) >= n:
            break
    return out


def spoke_today() -> dict:
    """Which model LINEAGES actually POSTED in rooms today — real proof the debate crosses families,
    not just the configured roster. Reads the day's committed chat transcripts (data/excava/chats)."""
    from collections import Counter
    from datetime import datetime, timezone
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    chats = Path(__file__).parent.parent / "data" / "excava" / "chats" / day
    c: Counter = Counter()
    if chats.exists():
        for f in chats.glob("*.jsonl"):
            try:
                for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
                    if not line.strip():
                        continue
                    eng = (json.loads(line).get("engine", "") or "").split("/")[0]
                    if eng and eng != "system":
                        c[LINEAGE.get(eng, eng)] += 1
            except Exception:
                continue
    return dict(c.most_common())


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
            model = os.environ.get("OLLAMA_MODEL", model)  # host picks its size (3B laptop / 8B+ VPS)
        elif not _key(envs):
            continue
        out.append({"name": name, "kind": kind, "base": base, "model": model,
                    "envs": envs, "tier": tier})
    rank = _health_rank()
    if rank:
        out.sort(key=lambda e: rank.get(e["name"], 99))
    return out


# Every distinct model LINEAGE is a brain — the 4 plan brains (§2, core=True) AND the existing
# good project models (Mistral / Gemini / GPT / Meta-Llama), which are strong distinct lineages
# already doing most of the talking. A brain = a model family given a role; the model does the
# talking. More real lineages = more diversity, so all of them belong in the roster + the debate.
LINEAGE_META = {
    "glm":        ("GLM-5.2",       "Zhipu",                        "leader · code & repos",   True),
    "deepseek":   ("DeepSeek V4",   "DeepSeek",                     "reasoning · cheap",       True),
    "qwen-local": ("Qwen / Llama",  "Alibaba/Meta · local Ollama",  "zero-quota · vision/tool", True),
    "kimi":       ("Kimi K2.7",     "Moonshot",                     "long-context · ingest",   True),
    "mistral":    ("Mistral",       "Mistral AI (EU)",              "fast generalist · multilingual", False),
    "gemini":     ("Gemini",        "Google",                       "grounded · long-context", False),
    "gpt":        ("GPT-4o-mini",   "OpenAI · GitHub Models",       "grounded · reliable",     False),
    "llama":      ("Llama-3.3 70B", "Meta · Groq/Cerebras/SambaNova/Nvidia", "fast · high-throughput", False),
}


def families() -> list[dict]:
    """EVERY distinct model lineage the project can field, as a brain (§2 diversity). A brain is a
    model family + role; the MODEL does the talking. The 4 plan brains are core=True; the existing
    good models (Mistral/Gemini/GPT/Llama) are first-class brains too. 'live' = an engine here
    serves that lineage now; 'needs-key' = configured, waiting on its key (§12)."""
    av = {e["name"] for e in available()}
    seen: dict = {}
    for name, kind, base, model, envs, tier in CATALOG:
        lin = LINEAGE.get(name, name)
        if lin == "gateway":                       # omniroute is a router, not a lineage
            continue
        live = name in av
        mdl = os.environ.get("OLLAMA_MODEL", model) if name == "hermes" else model
        if lin not in seen or (live and seen[lin]["status"] != "live"):
            fam, prov, role, core = LINEAGE_META.get(lin, (lin.title(), lin, "generalist", False))
            seen[lin] = {"family": fam, "lineage": prov, "role": role, "engine": name,
                         "model": mdl, "status": "live" if live else "needs-key", "core": core}
    roster = list(seen.values())
    roster.sort(key=lambda b: (not b["core"], b["status"] != "live", b["family"]))
    return roster


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
                headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}",
                         # canary 2026-07-11: groq+cerebras return Cloudflare 1010 (bot-block) for
                         # python-urllib's default agent — a browser UA is the documented cure
                         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                                       "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"})
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
    ap.add_argument("--brains", action="store_true", help="write the brain-family roster for the cockpit")
    a = ap.parse_args()
    if a.brains:
        from datetime import datetime, timezone
        roster = families()
        debate = [{"engine": e["name"], "lineage": LINEAGE.get(e["name"], e["name"]),
                   "model": e["model"]} for e in debate_engines(4)]
        doc = {"generated_at": datetime.now(timezone.utc).isoformat(), "brains": roster,
               "live": sum(1 for r in roster if r["status"] == "live"), "total": len(roster),
               "debate": debate, "debate_lineages": sorted({d["lineage"] for d in debate}),
               "spoke_today": spoke_today(),
               "note": "the plan's 3-4 generalist brains (§2), distinct lineages; a debate crosses "
                       "DISTINCT lineages only (never the same model twice); GLM/DeepSeek/Kimi need "
                       "OPENROUTER_API_KEY (§12), Qwen/Llama run local zero-quota"}
        out = Path(__file__).parent.parent / "data" / "excava" / "brains.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"brains roster: {doc['live']}/{doc['total']} live -> {[r['family']+':'+r['status'] for r in roster]}")
        return 0
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
