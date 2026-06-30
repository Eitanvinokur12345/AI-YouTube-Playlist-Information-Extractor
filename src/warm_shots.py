"""
src/warm_shots.py — pre-generate design screenshots so previews load instantly (shorten the wait).

mShots / thum.io generate screenshots ASYNC: the first viewer gets "Generating Preview…". This step
hits each design's screenshot URL ahead of time (in the pipeline) so the providers cache the real image
before the owner ever opens the tab. Only warms designs whose URL we've verified resolves. Free,
parallel, capped, stdlib. Run:  python -m src.warm_shots
"""
from __future__ import annotations

import json
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"


def _hit(u: str) -> None:
    for ep in (f"https://s.wordpress.com/mshots/v1/{urllib.parse.quote(u, safe='')}?w=1200",
               f"https://image.thum.io/get/fullpage/width/1200/{u}"):
        try:
            urllib.request.urlopen(urllib.request.Request(ep, headers={"User-Agent": UA}), timeout=20).read(2048)
        except Exception:
            pass


def main() -> int:
    p = DATA / "designs.json"
    if not p.exists():
        print("warm_shots: no designs.json — skipped."); return 0
    designs = (json.load(open(p, encoding="utf-8")) or {}).get("designs", [])
    urls = [x.get("source_url") for x in designs
            if x.get("source_url") and x.get("url_status") == "ok"][:400]
    if urls:
        with ThreadPoolExecutor(max_workers=20) as ex:
            list(ex.map(_hit, urls))
    print(f"warm_shots: warmed {len(urls)} design screenshots (mShots + thum.io) so previews load fast.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
