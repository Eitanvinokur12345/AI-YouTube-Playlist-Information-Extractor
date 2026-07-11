"""
src/history_mine.py — the REHABILITATION PLAN miner (owner 2026-07-11: "don't ignore the
history of the project — so many things need to happen and don't happen and are hidden there;
it will be an integral part of the 'EXCAVATORTRON and EXCAVA Rehabilitation Plan'").

What it does: reads the FULL owner history (data/excava/history.jsonl — every owner message
across all sessions, ingested by src.ingest_history) and mines WANT-signals: sentences where
the owner asked for something, complained something doesn't work, or demanded a change.
Repeated wants rank higher (he repeats what still hurts); recent wants rank higher.
Output: data/excava/rehab_plan.json — the ranked candidate list of possibly-unfulfilled wants,
each with the owner's own words + when + how often. The loop then asks the owner, a few at a
time, which are still unfulfilled (his 'question sequences at important places') and feeds the
confirmed ones into the program.

Free, stdlib-only. Run: python -m src.history_mine
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
HIST = ROOT / "data" / "excava" / "history.jsonl"
OUT = ROOT / "data" / "excava" / "rehab_plan.json"

# Signals that a sentence expresses a WANT / a PAIN (English; the transcripts are English).
WANT = re.compile(
    r"\b(i want|i need|i would like|you need to|you should|there should|add |make |must |"
    r"doesn'?t work|not work|isn'?t work|don'?t see|can'?t |cannot |missing|broken|fix |"
    r"change |improve |it should|needs to)\b", re.I)
NOISE = re.compile(r"^(ok|yes|no|continue|go on|thanks|good)\b", re.I)


def _sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+|\n+", text or "")
    return [p.strip() for p in parts if 25 <= len(p.strip()) <= 300]


def _fingerprint(s: str) -> frozenset:
    """Cheap topic fingerprint: the content words. Lets repeated wants cluster."""
    words = re.findall(r"[a-z][a-z\-]{3,}", s.lower())
    stop = {"want", "need", "should", "make", "this", "that", "there", "have", "with",
            "will", "would", "like", "them", "they", "your", "yours", "when", "what",
            "every", "thing", "things", "also", "just", "because", "about"}
    return frozenset(w for w in words if w not in stop)


def mine(top: int = 30) -> dict:
    clusters: list[dict] = []
    for ln in HIST.read_text(encoding="utf-8").splitlines():
        try:
            r = json.loads(ln)
        except Exception:
            continue
        if r.get("kind") != "owner_msg":
            continue
        for s in _sentences(r.get("text", "")):
            if NOISE.match(s) or not WANT.search(s):
                continue
            fp = _fingerprint(s)
            if len(fp) < 3:
                continue
            hit = None
            for c in clusters:                     # cluster by >=60% word overlap
                if len(fp & c["fp"]) >= 0.6 * min(len(fp), len(c["fp"])):
                    hit = c
                    break
            if hit:
                hit["count"] += 1
                hit["last_at"] = max(hit["last_at"], r.get("at", ""))
                if len(s) > len(hit["quote"]):     # keep the fullest phrasing
                    hit["quote"] = s
            else:
                clusters.append({"fp": fp, "quote": s, "count": 1,
                                 "first_at": r.get("at", ""), "last_at": r.get("at", ""),
                                 "session": r.get("session", "")})
    # rank: repetition orders the QUEUE, but does NOT decide importance — owner law 2026-07-11:
    # "something that appeared once doesn't mean it's not important". EVERY cluster is tracked;
    # the plan is DONE only when every request is fulfilled as he wanted (coverage below).
    clusters.sort(key=lambda c: (c["count"], c["last_at"]), reverse=True)
    prev_status: dict[str, str] = {}
    try:                                     # statuses survive re-mining (merge by quote)
        for it in json.load(open(OUT, encoding="utf-8")).get("items", []):
            if "unreviewed" not in it.get("status", "") and "ask the owner" not in it.get("status", ""):
                prev_status[it["quote"]] = it["status"]
    except Exception:
        pass
    items = [{"rank": i + 1, "quote": c["quote"], "times_raised": c["count"],
              "first": c["first_at"][:10], "last": c["last_at"][:10],
              "status": prev_status.get(c["quote"], "unreviewed — ask the owner")}
             for i, c in enumerate(clusters)]          # ALL clusters, not a top-N slice
    cov = {"total": len(items),
           "fulfilled": sum(1 for i in items if i["status"].startswith("fulfilled")),
           "in_progress": sum(1 for i in items if i["status"].startswith("in-progress")),
           "not_wanted": sum(1 for i in items if i["status"].startswith("not-wanted")),
           "unreviewed": sum(1 for i in items if i["status"].startswith("unreviewed"))}
    report = {"generated_at": datetime.now(timezone.utc).isoformat(),
              "source": f"{HIST.name} (full owner history, all sessions)",
              "done_when": "EVERY owner request ever made is fulfilled as he wanted — "
                           "coverage.fulfilled + not_wanted == coverage.total",
              "coverage": cov,
              "note": "EXCAVATORTRON & EXCAVA Rehabilitation Plan — every want-cluster from the "
                      "owner's own words, statuses persistent across re-mining; repetition orders "
                      "the queue, never importance. Question sequences resolve 'unreviewed' items.",
              "total_clusters": len(clusters), "items": items}
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    return report


def main() -> int:
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    r = mine()
    print(f"rehab-plan: {r['total_clusters']} want-clusters mined; top {len(r['items'])} saved")
    for it in r["items"][:10]:
        print(f"  #{it['rank']} ({it['times_raised']}x, last {it['last']}) {it['quote'][:90]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
