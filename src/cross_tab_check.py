"""
src/cross_tab_check.py — the single-tab guarantee (cross-tab consistency).

Part of the self-improvement system. Mechanical and FREE (no Claude / no engine calls), so it
runs every cycle regardless of the token budget. It guarantees a given thing lives in exactly ONE
tab: a name/slug must not appear as BOTH a skill and a tool. (Real example it fixes: "Impeccable"
is a Claude design skill — slug `impeccable` — but the extractor also filed it as a Tool with a
bogus company="Impeccable".) It:
  1. finds records present in BOTH data/skills.json and data/tools.json — matched on SLUG first
     (the canonical dedup key), then on normalized name, so it catches mismatched display names
     ("Impeccable" the tool == "Impeccable — Claude Design Knowledge Skill" the skill, same slug),
  2. decides which tab it really belongs to via a skill-ness vs tool-ness score that DISCOUNTS an
     echoed company (company == name) and BOOSTS genuine skill signals,
  3. removes it from the WRONG tab — NEVER touching a frozen/starred/locked record — and backs the
     removed record up to data/_removed_cross_tab.json (audit trail, reversible),
  4. on a raw score TIE, applies CLAUDE.md's own anti-boilerplate gate as the tie-break: a skill
     with zero captured technique evidence (no tips / slash_commands / general_tips) colliding
     with a tool of the same name isn't a technique at all — it's the product being echoed back
     as a "skill" (e.g. a `skills/claude-code` package whose body was just "Claude Code is an AI
     tool by Anthropic. It assists with software development...", the exact forbidden template).
     That tie resolves to the tool, and any now-orphaned SKILL.md package folder is deleted too
     (mirrors Step 5's merge cleanup). A genuine tie (either side has real captured evidence) is
     still FLAGGED, not decided automatically,
  5. writes data/cross_tab_conflicts.json (the audit the dashboard/self-check reads).

Run standalone:        python -m src.cross_tab_check
Preview only (no edit): python -m src.cross_tab_check --dry-run
It also runs at the end of every free bulk-analyze cycle (see bulk_analyze.yml), so any newly
introduced duplicate is resolved within one cycle.
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"


def _norm(s) -> str:
    return re.sub(r"[^a-z0-9]", "", str(s or "").lower())


def _load(name):
    try:
        return json.load(open(DATA / name, encoding="utf-8"))
    except Exception:
        return {}


def _save(name, obj) -> None:
    (DATA / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def _is_frozen(rec: dict) -> bool:
    """A record is frozen if explicitly starred / locked — never auto-remove these."""
    return bool(rec.get("starred") or rec.get("locked") or rec.get("frozen"))


def _frozen_slugs() -> set:
    """Extra frozen identities from data/stars.json, whatever shape it takes."""
    keys: set = set()
    stars = _load("stars.json")
    items = []
    if isinstance(stars, dict):
        for v in stars.values():
            items += v if isinstance(v, list) else [v]
    elif isinstance(stars, list):
        items = stars
    for it in items:
        keys.add(_norm(it.get("slug") or it.get("name") if isinstance(it, dict) else it))
    return {k for k in keys if k}


def _keys(rec: dict, *fields) -> set:
    """All identity keys for a record (slug + any name fields), normalized."""
    ks = set()
    for f in fields:
        k = _norm(rec.get(f))
        if k:
            ks.add(k)
    return ks


def _skill_score(s: dict) -> int:
    """How 'skill-like' (a technique / way of doing) the record looks."""
    sc = 0
    desc = str(s.get("description", "")).lower()
    if s.get("use_case"):
        sc += 2
    if s.get("tips"):
        sc += 1
    if s.get("slash_commands") or "command" in desc:
        sc += 1
    if s.get("is_claude_skill") or s.get("target_tool") or "skill" in desc:
        sc += 2
    return sc


def _has_concrete_technique(s: dict) -> bool:
    """True if the skill record captured any real technique evidence (tips, real slash
    commands, or general tips) beyond just restating what the product is. Per CLAUDE.md
    Step 3's anti-boilerplate gate: 'if a video only mentions a product without teaching a
    concrete technique, record the tool ... and emit no skill.' A colliding skill with none
    of this evidence is exactly that case, mis-filed as a skill instead of skipped."""
    return bool(s.get("tips")) or bool(s.get("slash_commands")) or bool(s.get("general_tips"))


def _skill_pkg_dir(s: dict) -> Path | None:
    """Where this skill's SKILL.md package folder would live, if it has one (Step 3 routing)."""
    slug = s.get("slug")
    if not slug:
        return None
    target = str(s.get("target_tool") or "claude").lower()
    flat = ROOT / "skills" / slug
    if target == "claude" and flat.is_dir():
        return flat
    other = ROOT / "other-skills" / target / slug
    if other.is_dir():
        return other
    # fall back to a scan — target_tool on these older/mis-filed records is unreliable
    if flat.is_dir():
        return flat
    for cand in (ROOT / "other-skills").glob(f"*/{slug}"):
        if cand.is_dir():
            return cand
    return None


def _tool_score(t: dict) -> int:
    """How 'tool-like' (a real product) the record looks — echoed company doesn't count."""
    sc = 0
    name = _norm(t.get("name"))
    company = _norm(t.get("company"))
    if company and company != name:          # a REAL company, not the name echoed back
        sc += 2
    if t.get("model_version") or t.get("version"):
        sc += 1
    if t.get("country"):
        sc += 1
    if t.get("pricing") or t.get("release_status") in ("released", "ga", "available"):
        sc += 1
    return sc


def run(apply: bool = True) -> dict:
    skills_d = _load("skills.json")
    tools_d = _load("tools.json")
    skills = list(skills_d.get("skills", []))
    tools = list(tools_d.get("tools", []))
    frozen = _frozen_slugs()

    # index every skill by ALL its identity keys (slug + names) so a tool matches via any of them
    skill_by_key: dict = {}
    for s in skills:
        for k in _keys(s, "slug", "skill_name", "name"):
            skill_by_key.setdefault(k, s)

    conflicts = []
    drop_skill_ids: set = set()
    drop_tool_ids: set = set()
    seen_pairs: set = set()
    for t in tools:
        s = None
        for k in _keys(t, "slug", "name"):
            if k in skill_by_key:
                s = skill_by_key[k]
                break
        if s is None:
            continue
        pair = (id(s), id(t))
        if pair in seen_pairs:
            continue
        seen_pairs.add(pair)

        name = s.get("skill_name") or t.get("name") or "?"
        slug = _norm(t.get("slug") or t.get("name"))
        ss, ts = _skill_score(s), _tool_score(t)
        s_frozen = _is_frozen(s) or slug in frozen
        t_frozen = _is_frozen(t) or slug in frozen
        if ss > ts and not t_frozen:
            verdict = "kept-skill (removed from Tools)"
            drop_tool_ids.add(id(t))
        elif ts > ss and not s_frozen:
            verdict = "kept-tool (removed from Skills)"
            drop_skill_ids.add(id(s))
        elif ss == ts:
            if not s_frozen and not _has_concrete_technique(s):
                verdict = "kept-tool (removed from Skills — boilerplate tie-break)"
                drop_skill_ids.add(id(s))
            else:
                verdict = "kept-both (tie — needs review)"
        else:
            verdict = "kept-both (frozen — manual review)"
        conflicts.append({"name": name, "slug": slug,
                          "skill_score": ss, "tool_score": ts, "verdict": verdict})

    removed = []
    deleted_pkg_dirs = []
    if apply and (drop_skill_ids or drop_tool_ids):
        dropped_slugs = set()
        for s in skills:
            if id(s) in drop_skill_ids:
                removed.append({"tab": "skills", "name": s.get("skill_name"),
                                "slug": s.get("slug"), "source_url": s.get("source_url")})
                if s.get("slug"):
                    dropped_slugs.add(s["slug"])
                pkg = _skill_pkg_dir(s)
                if pkg is not None:
                    shutil.rmtree(pkg, ignore_errors=True)
                    deleted_pkg_dirs.append(str(pkg.relative_to(ROOT)))
        for t in tools:
            if id(t) in drop_tool_ids:
                removed.append({"tab": "tools", "name": t.get("name"),
                                "slug": t.get("slug"), "source_url": t.get("source_url")})
        skills_d["skills"] = [s for s in skills if id(s) not in drop_skill_ids]
        tools_d["tools"] = [t for t in tools if id(t) not in drop_tool_ids]
        _save("skills.json", skills_d)
        _save("tools.json", tools_d)
        # Prune data/index.json for dropped slugs too — analyze_batch.py's index-first dedup
        # (CLAUDE.md Step 3) trusts `slug in index_data` to mean "the skill still exists"; a
        # stale entry pointing at a now-deleted skill crashes its merge branch (existing=None)
        # the next time a video re-extracts the same slug. Keep the index truthful.
        idx = _load("index.json")
        if isinstance(idx, dict) and dropped_slugs:
            for slug in dropped_slugs:
                idx.pop(slug, None)
            _save("index.json", idx)
        log = _load("_removed_cross_tab.json")
        if not isinstance(log, dict):
            log = {"removed": []}
        log["removed"] = (log.get("removed", []) + removed)[-500:]
        _save("_removed_cross_tab.json", log)

    report = {
        "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_collisions": len(conflicts),
        "removed_from_tools": len(drop_tool_ids),
        "removed_from_skills": len(drop_skill_ids),
        "flagged_for_review": sum(1 for c in conflicts if "review" in c["verdict"]),
        "deleted_pkg_dirs": deleted_pkg_dirs,
        "conflicts": conflicts,
    }
    _save("cross_tab_conflicts.json", report)
    return report


def main() -> None:
    apply = "--dry-run" not in sys.argv
    r = run(apply=apply)
    head = "DRY-RUN — " if not apply else ""
    print(f"{head}cross-tab check: {r['total_collisions']} collision(s) — "
          f"removed {r['removed_from_tools']} from Tools + {r['removed_from_skills']} from Skills, "
          f"{r['flagged_for_review']} flagged for review.")
    for c in r["conflicts"]:
        print(f"  - {c['name']}  (skill {c['skill_score']} vs tool {c['tool_score']}) -> {c['verdict']}")
    if r.get("deleted_pkg_dirs"):
        print(f"  deleted {len(r['deleted_pkg_dirs'])} orphaned SKILL.md folder(s): "
              f"{', '.join(r['deleted_pkg_dirs'])}")


if __name__ == "__main__":
    main()
