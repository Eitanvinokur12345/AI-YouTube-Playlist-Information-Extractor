"""
src/source_bundles.py — give every item a SOURCE-VIDEO BUNDLE, earliest-first.

When info came from several videos, the item should carry the whole bundle of source videos, with
the FIRST entry being the earliest video that first revealed it. Adds `source_videos` (ordered list
of {id, url, title, date}) to each tool/skill/connector/model. The dashboard + activator use it so
you can trace anything back to where it first appeared. Free, mechanical.

Run:  python -m src.source_bundles
"""
from __future__ import annotations

import glob
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
PROCESSED = DATA / "processed"


def _load(p, d=None):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return d if d is not None else {}


def _date(r: dict) -> str:
    for k in ("published", "publishedAt", "publish_date", "upload_date", "date"):
        v = r.get(k)
        if v:
            return str(v)
    return "9999"           # unknown dates sort last


def video_index() -> dict:
    idx = {}
    for f in glob.glob(str(PROCESSED / "*.json")):
        r = _load(Path(f))
        if isinstance(r, dict) and r.get("video_id"):
            idx[r["video_id"]] = {"date": _date(r), "title": (r.get("title") or "")[:120]}
    return idx


def main() -> int:
    idx = video_index()

    def bundle(item) -> list:
        vids = list(dict.fromkeys((item.get("endorsement_video_ids") or [])
                                  + ([item.get("source_video_id")] if item.get("source_video_id") else [])))
        if not vids and item.get("source_url") and "watch?v=" in str(item.get("source_url")):
            vids = [str(item["source_url"]).split("watch?v=")[-1].split("&")[0]]
        vids = [v for v in vids if v]
        vids.sort(key=lambda v: idx.get(v, {}).get("date", "9999"))   # earliest first
        return [{"id": v, "url": f"https://www.youtube.com/watch?v={v}",
                 "title": idx.get(v, {}).get("title", "")} for v in vids]

    total = 0
    for fname, key in [("tools.json", "tools"), ("skills.json", "skills"),
                       ("connectors.json", "connectors"), ("models.json", "models")]:
        d = _load(DATA / fname)
        items = d.get(key, []) if isinstance(d, dict) else []
        changed = False
        for it in items:
            b = bundle(it)
            if b and it.get("source_videos") != b:
                it["source_videos"] = b
                changed = True
                total += 1
        if changed:
            (DATA / fname).write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"source_bundles: built ordered source-video bundles for {total} items (earliest-first).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
