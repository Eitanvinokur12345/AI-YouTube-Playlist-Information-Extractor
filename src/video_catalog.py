"""Read-only catalog of video retrieval, analysis evidence and extracted categories."""
from __future__ import annotations
from collections import Counter, defaultdict
from datetime import datetime, timezone
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
VIDEO_ID = re.compile(r"^[A-Za-z0-9_-]{11}$")


def read(path, fallback):
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def build(data):
    index = read(data / "elements_index.json", {})
    elements = index if isinstance(index, list) else index.get("elements", [])
    related = defaultdict(list)
    for el in elements:
        for source in el.get("source_videos", []):
            vid = source.get("video_id", "") if isinstance(source, dict) else source
            if isinstance(vid, str) and VIDEO_ID.fullmatch(vid):
                related[vid].append(el)
    gemini = read(data / "gemini_analyzed.json", {})
    watched = set(gemini.get("video_ids", []))
    records, queued = {}, set()
    for folder in ["processed", "_pending"]:
        for path in sorted((data / folder).glob("*.json")):
            rec = read(path, {})
            vid = rec.get("video_id", path.stem)
            if not isinstance(vid, str) or not VIDEO_ID.fullmatch(vid):
                continue
            if folder == "_pending":
                queued.add(vid)
            old = records.setdefault(vid, {})
            for key, value in rec.items():
                if value not in (None, "", [], {}):
                    old[key] = value
    for vid in set(read(data / "skills.json", {}).get("videos_seen", [])) | watched:
        if isinstance(vid, str) and VIDEO_ID.fullmatch(vid):
            records.setdefault(vid, {})
    videos = []
    for vid, rec in records.items():
        analysis = rec.get("analysis") or {}
        confirmed = (vid in watched or rec.get("gemini_video_analyzed") is True or
                     isinstance(analysis, dict) and analysis.get("status") == "complete")
        source = rec.get("transcript_source", "")
        has_text = bool(rec.get("transcript")) and source in ("transcript", "whisper")
        findings = related[vid]
        videos.append({
            "video_id": vid, "title": rec.get("title") or vid,
            "channel": rec.get("channel_name", ""),
            "published_at": rec.get("publishedAt", ""),
            "url": "https://www.youtube.com/watch?v=" + vid,
            "stage": "analyzed" if confirmed else "queued" if vid in queued else "unconfirmed",
            "queued": vid in queued, "has_transcript": has_text,
            "retrieval": source if has_text else "description" if source == "description" else "metadata",
            "categories": sorted({el.get("category") or "other" for el in findings}),
            "elements": [{"id": el["id"], "name": el["name"], "type": el["type"]} for el in findings],
        })
    videos.sort(key=lambda v: (v["published_at"], v["video_id"]), reverse=True)
    status = read(data / "status.json", {})
    categories = Counter(c for v in videos for c in v["categories"])
    return {
        "schema_version": 1, "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_updated_at": max([status.get("last_fetch") or "", status.get("last_analyze") or "",
                                  gemini.get("updated_at") or ""]),
        "summary": {
            "total": len(videos), "analyzed": sum(v["stage"] == "analyzed" for v in videos),
            "queued": len(queued), "with_transcript": sum(v["has_transcript"] for v in videos),
            "unconfirmed": sum(v["stage"] == "unconfirmed" for v in videos),
            "elements": len(elements), "categories": dict(categories.most_common()),
        },
        "note": "Captions and processed-file placement do not establish completed analysis. "
                "Categories come from existing extracted findings; missing categories stay empty.",
        "videos": videos,
    }


def main():
    data = ROOT / "data"
    catalog = build(data)
    target = data / "video_catalog.json"
    temp = target.with_suffix(".json.tmp")
    temp.write_text(json.dumps(catalog, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    temp.replace(target)
    print(json.dumps(catalog["summary"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
