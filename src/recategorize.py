"""
src/recategorize.py — fix mis-categorized items (e.g. robots filed as generic 'tool'/'agents').

The owner noticed robotics being treated as a normal tool when it's really its own emerging domain
that deserves its own tab. Categories now include robotics/voice/3d/data/security; this re-tags
existing records whose name+description clearly belong to one of those emerging domains but are
currently sitting in 'other' or a mismatched bucket. Conservative: only moves on a strong keyword
hit, and never overwrites an already-correct emerging category. Free, mechanical.

Run:  python -m src.recategorize
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
NOW = datetime.now(timezone.utc).isoformat()

# emerging domain -> strong signal keywords. Order matters (first match wins).
DOMAINS = [
    ("robotics", ["robot", "robotic", "humanoid", "embodied", "drone", "actuator", "teleoper",
                  "boston dynamics", "unitree", "quadruped", "manipulation arm"]),
    ("voice", ["voice", "speech-to-text", "text-to-speech", " tts", " stt", "speech synthesis",
               "voice clone", "voice agent", "transcription model", "real-time voice"]),
    ("3d", ["3d model", "3d generation", "mesh", "gaussian splat", "nerf", "blender", "point cloud",
            "3d scene", "text-to-3d", "photogrammetry"]),
    ("security", ["prompt injection", "jailbreak", "guardrail", "red team", "ai security",
                  "llm security", "adversarial", "data exfiltration"]),
]
# only move items currently in these loose buckets (don't disturb confident categories)
LOOSE = {"other", "", "agents", "automation", "productivity", "research", "integration", None}


def _load(name):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return {}


def domain_of(blob: str) -> str | None:
    b = blob.lower()
    for dom, kws in DOMAINS:
        if any(k in b for k in kws):
            return dom
    return None


def main() -> int:
    moved = {}
    for fname, key, nk in [("tools.json", "tools", "name"), ("skills.json", "skills", "skill_name"),
                           ("models.json", "models", "name")]:
        d = _load(fname)
        items = d.get(key, []) if isinstance(d, dict) else []
        changed = 0
        for it in items:
            cur = (it.get("category") or "other").lower()
            if cur in {"robotics", "voice", "3d", "security"}:
                continue                                   # already an emerging category
            if cur not in {str(x).lower() if x else x for x in LOOSE}:
                continue                                   # in a confident bucket — leave it
            dom = domain_of(f"{it.get(nk, '')} {it.get('description', '')} {it.get('use_case', '')}")
            if dom and dom != cur:
                it["category"] = dom
                it["recategorized_at"] = NOW
                changed += 1
                moved[dom] = moved.get(dom, 0) + 1
        if changed:
            (DATA / fname).write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    summary = ", ".join(f"+{n} {dom}" for dom, n in sorted(moved.items())) or "nothing to move"
    print(f"recategorize: {summary}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
