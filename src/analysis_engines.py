"""Stateless inference for content enrichment, independent of EXCAVA."""
from __future__ import annotations
import json
import os
import time
import urllib.request

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
    ("nvidia",     "openai", "https://integrate.api.nvidia.com/v1",   "meta/llama-3.3-70b-instruct",
     ["NVIDIA_API_KEY"], "grounded"),
    # ── M2 BRAIN FAMILIES — distinct model LINEAGES (§2). OpenRouter is a TRANSPORT (aggregator),
    # NOT a model: it is the base_url that CARRIES these models, each named by its real lineage.
    # (A generic "openrouter" engine was removed — it was pinned to deepseek-chat-v3, a phantom
    # duplicate of the deepseek entry that double-counted one model in the benchmark.) Free :free
    # tier, answer only where OPENROUTER_API_KEY lives (CI / VPS, §12); IDs track the plan's targets.
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

def available():
    out = []
    for name, kind, base, model, envs, tier in CATALOG:
        if name == "omniroute":
            base = os.environ.get("OMNIROUTE_URL", "").strip()
            if not base or not _key(envs):
                continue
        elif name == "hermes":
            if os.environ.get("HERMES_OLLAMA") != "1":
                continue
            model = os.environ.get("OLLAMA_MODEL", model)
        elif not _key(envs):
            continue
        out.append(dict(name=name, kind=kind, base=base, model=model, envs=envs, tier=tier))
    return out


def complete(prompt, max_tokens=700):
    errors = []
    for engine in available()[:3]:
        result = _call_one(engine, prompt, max_tokens)
        if result["ok"]:
            return dict(ok=True, text=result["text"], engine=engine["name"], model=engine["model"])
        errors.append(engine["name"] + ":" + str(result.get("status", 0)))
    return dict(ok=False, text="", engine="none", error=", ".join(errors) or "no engines configured")
