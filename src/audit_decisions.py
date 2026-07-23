"""src/audit_decisions.py — §7 machinery: the MASTER AUDIT's ~300 decisions are EITAN'S.

Parses EXCAVA_MASTER_AUDIT.md (numbered items with Claude's *Rec:* proposals) into
data/excava/overhaul_decisions.json, where verdicts land one clickable batch at a time.
Verdicts are honored before a milestone touches a feature (END PLAN §7).

  python -m src.audit_decisions seed             parse the MD -> JSON (keeps existing verdicts)
  python -m src.audit_decisions set 3 improve --note "add Groq+Cerebras first"
  python -m src.audit_decisions status           counts by verdict + next open batch
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
AUDIT_MD = ROOT / "EXCAVA_MASTER_AUDIT.md"
OUT = ROOT / "data" / "excava" / "overhaul_decisions.json"
VERDICTS = {"keep", "fix", "improve", "rebuild", "wire", "backlog", "remove"}


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def parse_audit() -> list[dict]:
    """Every `N. **title** — body -> *Rec: ...*` line under a `## SECTION X` heading."""
    items, section = [], ""
    for line in AUDIT_MD.read_text(encoding="utf-8").splitlines():
        sec = re.match(r"##\s+SECTION\s+(\w+)\s+—\s*(.*)", line)
        if sec:
            section = f"{sec.group(1)} — {re.sub(r'[*_`]', '', sec.group(2)).split('—')[0].strip()}"
            continue
        m = re.match(r"(\d+)\.\s+\*\*(.+?)\*\*\s*(.*)", line)
        if not m:
            continue
        body = re.sub(r"[*_`]", "", m.group(3)).strip(" —-")
        rec = ""
        rm = re.search(r"Rec:\s*(.+?)\.?\s*$", body)
        if rm:
            rec, body = rm.group(1).strip(), body[:rm.start()].strip(" →—-. ")
        items.append({"id": int(m.group(1)), "section": section,
                      "title": re.sub(r"[*_`]", "", m.group(2)).strip(),
                      "what": body[:300], "claude_rec": rec[:200],
                      "verdict": None, "note": None, "decided_at": None})
    return items


def seed() -> dict:
    doc = {"source": "EXCAVA_MASTER_AUDIT.md", "seeded_at": _now(), "items": parse_audit()}
    if OUT.exists():                      # never lose a decision Eitan already made
        old = {i["id"]: i for i in json.loads(OUT.read_text(encoding="utf-8")).get("items", [])}
        for it in doc["items"]:
            prev = old.get(it["id"])
            if prev and prev.get("verdict"):
                it.update({k: prev[k] for k in ("verdict", "note", "decided_at")})
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    return doc


def set_verdict(item_id: int, verdict: str, note: str | None = None) -> dict:
    verdict = verdict.lower().strip()
    if verdict not in VERDICTS:
        raise SystemExit(f"verdict must be one of {sorted(VERDICTS)}")
    doc = json.loads(OUT.read_text(encoding="utf-8"))
    for it in doc["items"]:
        if it["id"] == item_id:
            it.update({"verdict": verdict, "note": note, "decided_at": _now()})
            OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
            return it
    raise SystemExit(f"no item {item_id}")


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("seed")
    s = sub.add_parser("set")
    s.add_argument("id", type=int)
    s.add_argument("verdict")
    s.add_argument("--note", default=None)
    sub.add_parser("status")
    n = sub.add_parser("next")
    n.add_argument("-n", type=int, default=4)
    n.add_argument("--stage", action="store_true", help="append the batch to QUESTIONS.md for review")
    a = ap.parse_args()
    if a.cmd == "seed":
        doc = seed()
        decided = sum(1 for i in doc["items"] if i["verdict"])
        print(f"seeded {len(doc['items'])} items ({decided} already decided) -> {OUT}")
    elif a.cmd == "set":
        it = set_verdict(a.id, a.verdict, a.note)
        print(f"{it['id']}: {it['verdict']}  ({it['title'][:60]})")
    elif a.cmd == "next":
        doc = json.loads(OUT.read_text(encoding="utf-8"))
        batch = [i for i in doc["items"] if not i["verdict"]][:a.n]
        if not batch:
            print("all decided — no open items")
            return 0
        lines = [f"- **#{i['id']} [{i['section']}] {i['title']}** — {i['what'][:140]}"
                 f"  _(proposed: {i['claude_rec'][:80] or 'FIX'})_" for i in batch]
        block = "\n".join(lines)
        print(f"next {len(batch)} open audit decisions (§7):\n{block}")
        if a.stage:
            q = ROOT / "QUESTIONS.md"
            stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            hdr = (f"\n### Audit batch staged {stamp} — items #{batch[0]['id']}-#{batch[-1]['id']} "
                   f"(confirm with: python -m src.audit_decisions set <id> <verdict>)\n")
            with open(q, "a", encoding="utf-8") as fh:
                fh.write(hdr + block + "\n")
            print(f"staged {len(batch)} items -> {q}")
    else:
        doc = json.loads(OUT.read_text(encoding="utf-8"))
        counts: dict = {}
        for i in doc["items"]:
            counts[i["verdict"] or "OPEN"] = counts.get(i["verdict"] or "OPEN", 0) + 1
        nxt = [i["id"] for i in doc["items"] if not i["verdict"]][:4]
        print(json.dumps({"counts": counts, "next_batch": nxt}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
