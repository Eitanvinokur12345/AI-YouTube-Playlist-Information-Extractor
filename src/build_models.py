"""
src/build_models.py — mirror the AI MODELS out of tools.json into data/models.json.

Models are a subset of tools (the ones that ARE foundation/AI models, not apps built on them).
The dashboard's Tool Rating tab + the reference self-check (Q17-20) expect data/models.json
populated; it had been empty because nothing classified tools as models. This does it mechanically
(name/slug matches a known model family), deduped + ranked by quality_score. No Claude, stdlib only.

Usage:  python -m src.build_models
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"

# Known foundation/AI model FAMILIES (lowercase). A tool whose name/slug contains one of these
# (as a word-ish token) is treated as a model. Kept specific to avoid mislabeling apps.
FAMILIES = [
    "gpt", "o1", "o3", "o4", "chatgpt", "claude", "sonnet", "opus", "haiku", "gemini", "gemma",
    "llama", "mistral", "mixtral", "deepseek", "qwen", "grok", "phi", "command r", "command-r",
    "nova", "titan", "falcon", "ernie", "yi-", "doubao", "kimi", "minimax", "hunyuan", "step-",
    "sora", "veo", "flux", "stable diffusion", "sdxl", "dall-e", "dalle", "midjourney", "imagen",
    "ideogram", "recraft", "kling", "runway gen", "gen-3", "gen-4", "pika", "luma", "dream machine",
    "seedance", "seedream", "wan ", "cogvideo", "mochi", "ltx", "hailuo", "suno", "udio", "whisper",
    "elevenlabs", "playground v", "nemotron", "olmo", "dbrx", "jamba", "reka", "pixtral", "aya",
]
_FAM_RX = re.compile("|".join(re.escape(f) for f in FAMILIES))

# Products that contain a model token but are TOOLS/apps, not models — don't mirror them.
EXCLUDE = ("claude code", "claude desktop", "claude.ai", "gemini cli", "gemini code",
           "gpt store", "gpts", "custom gpt", "chatgpt plus", "chatgpt team", "openai api",
           "llama index", "llamaindex", "ollama", "lm studio", "grok cli")


def _is_model(t: dict) -> bool:
    name = f" {(t.get('name') or '').lower()} {(t.get('slug') or '').lower()} "
    if any(x in name for x in EXCLUDE):
        return False
    if _FAM_RX.search(name):
        return True
    cat = (t.get("category") or "").lower()
    # an image/video/audio GENERATOR with an explicit version reads as a model, not an app
    return cat in ("image creation", "video creation", "audio creation") and bool(t.get("model_version"))


def main() -> int:
    tools = (json.load(open(DATA / "tools.json", encoding="utf-8")) if (DATA / "tools.json").exists() else {}).get("tools", [])
    # dedup by IDENTITY = name+version (what makes a model unique), keeping the highest quality
    best = {}
    for t in tools:
        if not _is_model(t):
            continue
        ident = (str(t.get("name") or "").lower().strip(), str(t.get("model_version") or "").lower().strip())
        if ident == ("", ""):
            continue
        cur = best.get(ident)
        if cur is None or (t.get("quality_score") or 0) > (cur.get("quality_score") or 0):
            best[ident] = t
    models = []
    for t in best.values():
        slug = (t.get("slug") or (t.get("name") or "").lower().replace(" ", "-")).lower()
        models.append({
            "name": t.get("name"), "slug": slug, "category": t.get("category") or "other",
            "model_version": t.get("model_version", ""), "company": t.get("company", ""),
            "country": t.get("country", ""), "open_source": t.get("open_source", False),
            "quality_score": t.get("quality_score", 0), "description": t.get("description", ""),
            "source_url": t.get("source_url", ""), "source_video_id": t.get("source_video_id", ""),
            "endorsement_video_ids": t.get("endorsement_video_ids", []),
        })
    models.sort(key=lambda m: (m.get("quality_score") or 0), reverse=True)
    out = {"updated_at": datetime.now(timezone.utc).isoformat(), "models": models,
           "note": "AI models mirrored from tools.json (foundation/generation models, ranked)."}
    json.dump(out, open(DATA / "models.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"models: {len(models)} mirrored from {len(tools)} tools "
          f"(top: {', '.join(m['name'] for m in models[:6] if m['name'])})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
