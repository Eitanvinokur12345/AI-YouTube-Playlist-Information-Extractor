"""
src/mine_designs.py — collect AI-buildable website/app DESIGNS from beyond the videos.

The owner wants the Designs tab tailored to HIS taste (bold/colorful/maximalist + playful/retro/
brutalist) and fed from real AI-produced / open-source UIs, not only the playlist. This pulls
high-quality UI repos from GitHub (queries leaned to his taste: neobrutalism, creative, colorful,
landing pages, dashboards), keeping the live demo (repo homepage) + source + tech, and tags the
style. Free (GitHub search API; uses GITHUB_TOKEN if present for higher rate). Screenshots are added
at render time by the dashboard (free mshots), so no image storage here.

Run:  python -m src.mine_designs
"""
from __future__ import annotations

import json
import os
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
OUT = DATA / "designs.json"
NOW = datetime.now(timezone.utc).isoformat()
UA = "excavatortron-designs/1.0"

# query -> the owner's style tag it serves (his taste: bold/colorful/maximalist + playful/retro/brutalist)
QUERIES = [
    ("topic:neobrutalism stars:>80", ["playful", "brutalist"]),
    ("topic:brutalist-design stars:>40", ["brutalist"]),
    ("topic:creative-portfolio stars:>150", ["bold", "playful"]),
    ("colorful landing page in:name,description stars:>200", ["bold", "colorful"]),
    ("topic:awwwards stars:>60", ["bold"]),
    ("topic:landing-page stars:>500", ["bold"]),
    ("topic:dashboard topic:tailwindcss stars:>400", ["bold"]),
    ("gradient animated in:name,description topic:react stars:>150", ["colorful", "bold"]),
    ("topic:webgl creative in:description stars:>200", ["bold", "playful"]),
    ("topic:three-js portfolio stars:>150", ["bold", "playful"]),
    ("topic:awesome-design-tools stars:>300", ["bold"]),
    ("retro pixel ui in:name,description stars:>100", ["playful", "colorful"]),
    ("topic:shadcn-ui stars:>500", ["minimal", "bold"]),
    ("topic:framer-motion showcase stars:>120", ["bold", "playful"]),
    ("vibrant colorful saas template in:name,description stars:>120", ["colorful", "bold"]),
]


def _gh(q: str, token: str):
    url = ("https://api.github.com/search/repositories?sort=stars&order=desc&per_page=8&q="
           + urllib.parse.quote(q))
    h = {"User-Agent": UA, "Accept": "application/vnd.github+json"}
    if token:
        h["Authorization"] = f"Bearer {token}"
    try:
        req = urllib.request.Request(url, headers=h)
        return json.loads(urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace")).get("items", [])
    except Exception:
        return []


def main() -> int:
    token = (os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_MODELS_TOKEN") or "").strip()
    d = json.load(open(OUT, encoding="utf-8")) if OUT.exists() else {"designs": []}
    arr = d.get("designs", [])
    have = {str(x.get("name", "")).lower() for x in arr}
    added = 0
    for q, styles in QUERIES:
        for r in _gh(q, token):
            name = r.get("name")
            if not name or name.lower() in have:
                continue
            arr.append({
                "name": name, "slug": (r.get("full_name") or name).replace("/", "-").lower(),
                "kind": "website/app (open-source)",
                "look": (r.get("description") or "")[:200],
                "style_tags": styles,
                "tech": [r.get("language")] + (r.get("topics") or [])[:5] if r.get("language") else (r.get("topics") or [])[:5],
                "github": r.get("html_url"),
                "homepage": (r.get("homepage") or "").strip() or None,   # live demo if the repo set one
                "deploy_url": f"https://vercel.com/new/clone?repository-url={r.get('html_url')}",
                "rebuild_with": ["v0", "Lovable", "Bolt", "Cursor", "Tailwind"],
                "stars": r.get("stargazers_count", 0),
                "source_type": "github-designs", "added_at": NOW,
            })
            have.add(name.lower()); added += 1
        time.sleep(1.0)
    d["designs"] = arr
    OUT.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"mine_designs: +{added} designs from GitHub (tailored to taste); total {len(arr)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
