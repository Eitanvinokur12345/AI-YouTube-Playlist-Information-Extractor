"""Resolve catalogue leads to publisher artifacts; never import or execute upstream files."""
import argparse
import base64
import hashlib
import json
import os
import re
import subprocess
import tempfile
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
INDEX = DATA / "original_sources.json"
REGISTRIES = ("anthropics/skills", "openai/skills")
GH = re.compile(r"https://github\.com/([\w.-]+/[\w.-]+)(?=[/#?\s)]|$)", re.I)
HF = re.compile(r"^https://huggingface\.co/(?:(spaces|datasets)/)?([\w.-]+/[\w.-]+)/?$", re.I)
# Known publisher sites for products without a public implementation repository.
SITES = {"chatgpt": "https://chatgpt.com/", "claude": "https://claude.ai/",
         "perplexity": "https://www.perplexity.ai/", "notebooklm": "https://notebooklm.google/"}


def norm(value):
    return re.sub(r"[^a-z0-9]+", "-", str(value or "").lower()).strip("-")


def get(url):
    headers = {"User-Agent": "Excavatortron-originals", "Accept": "application/json"}
    if url.startswith("https://api.github.com/") and os.environ.get("GH_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GH_TOKEN"]
    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=12) as res:
            return json.load(res)
    except HTTPError as err:
        if err.code in (404, 410, 422, 451, 401) and not (err.code == 401 and "api.github.com" in url):
            return {}
        raise


def load(path, default):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def references(row):
    return [row.get(k) for k in ("original_url", "url", "github", "homepage", "source_url")
            if isinstance(row.get(k), str)]


def identity(row, typ):
    return norm(row.get("skill_name") or row.get("name") or row.get("slug"))


def video_links(row):
    ids = [row.get("source_video_id"), row.get("via_video_id"), row.get("source_video")]
    ids += [v.get("id") if isinstance(v, dict) else v for v in (row.get("source_videos") or [])[:3]]
    links = []
    for vid in ids:
        if not isinstance(vid, str) or not re.fullmatch(r"[\w-]{11}", vid):
            continue
        for directory in ("processed", "_pending"):
            rec = load(DATA / directory / (vid + ".json"), {})
            links.extend("https://github.com/" + repo for repo in GH.findall(rec.get("description") or ""))
    return links


def skill_metadata(content):
    text = content.decode("utf-8-sig")
    parts = re.split(r"^---[ \t]*\r?$", text, maxsplit=2, flags=re.M)
    if len(parts) != 3 or parts[0].strip() or not parts[2].strip():
        return None
    name = re.search(r"^name:[ \t]*([^\r\n#]+)", parts[1], re.M)
    if not name:
        return None
    desc = re.search(r"^description:[ \t]*([^\r\n]+)", parts[1], re.M)
    return name[1].strip(" '\""), (desc[1].strip(" '\"")[:420] if desc else "")


def scan_files(folder):
    run = subprocess.run(["clamscan", "--no-summary", "--alert-exceeds-max=yes", str(folder)],
                         capture_output=True, text=True)
    if run.returncode not in (0, 1):
        raise RuntimeError("ClamAV could not complete the original document scan")
    return {line[:-4] for line in run.stdout.splitlines() if line.endswith(": OK")}


def product_matches(name, repo):
    key = norm(repo.split("/")[-1])
    return name in {key, norm(repo.replace("/", "-")), key + "-mcp", "mcp-" + key}


def refresh():
    old = load(INDEX, {})
    entries = {e["id"]: e for e in old.get("entries", [])}
    matches = dict(old.get("matches", {}))
    by_repo = defaultdict(list)
    hf = defaultdict(list)
    audit = load(DATA / "skill_scan.json", {}).get("skills", {})
    blocked = set()
    discoveries = defaultdict(set)
    for typ, fname in (("skill", "skills"), ("connector", "connectors"), ("tool", "tools")):
        for row in load(DATA / (fname + ".json"), {}).get(fname, []):
            name = identity(row, typ)
            if not name:
                continue
            key = typ + ":" + name
            source = row.get("source_url")
            if isinstance(source, str) and source.startswith("https://"):
                discoveries[key].add(source)
            if typ == "skill" and audit.get(row.get("slug"), {}).get("result") == "detected":
                blocked.add(key)
                matches.pop(key, None)
                continue
            if typ == "tool" and name in SITES:
                entries[key] = {"id": key, "type": typ, "name": row["name"], "url": SITES[name],
                                "kind": "publisher_website"}
                matches[key] = key
            urls = references(row)
            if typ == "skill":
                urls += video_links(row)
            for url in urls:
                m = GH.match(url)
                if m:
                    repo = m[1].removesuffix(".git").rstrip(".").lower()
                    by_repo[repo].append((key, name, row))
                m = HF.fullmatch(url)
                if m and typ == "tool" and product_matches(name, m[2]):
                    hf[(m[1] or "models", m[2])].append((key, row))

    cursor = old.get("cursor", 0)
    pool = sorted(set(by_repo) - set(REGISTRIES))
    def window(items, size):
        if not items:
            return []
        start = cursor % len(items)
        return (items[start:] + items[:start])[:size]

    # Bootstrap a few publisher-linked products; then rotate all observed owners.
    repos = list(dict.fromkeys([*REGISTRIES, "microsoft/playwright-mcp", "openai/codex",
                               "upstash/context7", *window(pool, 24)]))
    # Search for specifically named skills when a video omitted a URL. A search hit
    # is a candidate; only a publisher file plus independent attribution may bind it to a lead.
    pending = []
    for row in load(DATA / "skills.json", {}).get("skills", []):
        name = identity(row, "skill")
        key = "skill:" + name
        owner = str(row.get("publisher") or row.get("company") or "").strip()
        if (key not in matches and key not in blocked and len(name) >= 4 and
                re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]{0,38}", owner)):
            pending.append((key, name, owner, row))
    for key, name, owner, row in window(pending, 4):
        query = quote(f'user:{owner} "{name}"')
        for candidate in get("https://api.github.com/search/repositories?q=" + query + "&per_page=3").get("items", []):
            repo = candidate["full_name"].lower()
            if not candidate.get("fork") and repo.split("/")[0] == owner.lower():
                by_repo[repo].append((key, name, row))
                if repo not in repos:
                    repos.append(repo)
    with tempfile.TemporaryDirectory() as tmp:
        staged = {}
        for repo in repos:
            base = "https://api.github.com/repos/" + repo
            meta = get(base)
            if not meta or meta.get("fork") or meta.get("private") or meta.get("disabled"):
                continue
            full = meta["full_name"]
            root = "https://github.com/" + full
            for key, name, row in by_repo[repo]:
                if key.startswith("connector:") and not re.search(r"\bmcp\b|model context protocol",
                        " ".join([full, meta.get("description") or "", *meta.get("topics", [])]), re.I):
                    continue
                if key.startswith("skill:") or not product_matches(name, full):
                    continue
                eid = key.split(":")[0] + ":github:" + full.lower()
                entries[eid] = {"id": eid, "type": key.split(":")[0], "name": row["name"],
                                "publisher": meta["owner"]["login"], "url": root,
                                "kind": "publisher_repository"}
                matches[key] = eid
            leads = [r for r in by_repo[repo] if r[0].startswith("skill:")]
            if repo not in REGISTRIES and not leads:
                continue
            head = get(base + "/commits/" + quote(meta["default_branch"], safe=""))
            if not head.get("sha"):
                continue
            sha = head["sha"]
            tree = get(base + "/git/trees/" + sha + "?recursive=1")
            nodes = [n for n in tree.get("tree", []) if n.get("type") == "blob" and
                     n["path"].split("/")[-1] == "SKILL.md" and 0 < n.get("size", 0) <= 250000]
            for n in nodes:
                path = n["path"]
                folder = path.rsplit("/", 1)[0] if "/" in path else ""
                slug = norm(folder.rsplit("/", 1)[-1] or full.split("/")[-1])
                if repo in REGISTRIES and not path.startswith("skills/"):
                    continue
                if repo not in REGISTRIES and not any(name == slug or
                        url.rstrip("/").endswith("/" + path) for _, name, row in leads for url in references(row) + [""]):
                    continue
                eid = "skill:github:" + full.lower() + "/" + path
                blob = n["sha"]
                if eid in entries and entries[eid].get("blob") == blob and entries[eid].get("revision") == sha:
                    item = entries[eid]
                else:
                    obj = get(base + "/git/blobs/" + blob)
                    if not obj.get("content"):
                        continue
                    content = base64.b64decode(obj["content"])
                    if hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest() != blob:
                        raise ValueError("Git blob digest mismatch")
                    details = skill_metadata(content)
                    if not details:
                        continue
                    name, description = details
                    item = {"id": eid, "type": "skill", "kind": "upstream_skill_md", "name": name,
                            "description": description, "publisher": meta["owner"]["login"], "repo": root,
                            "revision": sha, "blob": blob, "sha256": hashlib.sha256(content).hexdigest(),
                            "url": root + "/blob/" + sha + "/" + quote(path),
                            "raw_url": "https://raw.githubusercontent.com/" + full + "/" + sha + "/" + quote(path),
                            "package_url": root + "/tree/" + sha + ("/" + quote(folder) if folder else "")}
                    dest = Path(tmp) / blob
                    dest.write_bytes(content)
                    staged[eid] = (str(dest), item)
                for key, name, row in leads:
                    if name == norm(item["name"]) or any(u == item["url"] for u in references(row)):
                        matches[key] = eid
        if staged:
            clean = scan_files(Path(tmp))
            for eid, (file, item) in staged.items():
                if file in clean:
                    entries[eid] = {**item, "scan": "no detection (SKILL.md bytes only)"}
                else:
                    entries.pop(eid, None)

    for (kind, rid) in window(sorted(hf), 12):
        meta = get("https://huggingface.co/api/" + kind + "/" + rid)
        if not meta.get("sha") or str(meta.get("id", "")).lower() != rid.lower():
            continue
        url = "https://huggingface.co/" + ("" if kind == "models" else kind + "/") + rid
        for key, row in hf[(kind, rid)]:
            eid = "tool:huggingface:" + kind + "/" + rid
            entries[eid] = {"id": eid, "type": "tool", "name": row["name"], "publisher": rid.split("/")[0],
                            "kind": "publisher_repository", "url": url, "revision": meta["sha"]}
            matches[key] = eid
    matches = {k: v for k, v in matches.items() if v in entries and k not in blocked}
    if not any(v.get("raw_url") for v in entries.values()):
        raise RuntimeError("No upstream skill documents available")
    doc = {"version": 1, "updated_at": datetime.now(timezone.utc).isoformat(), "cursor": cursor + 24,
           "entries": sorted(entries.values(), key=lambda e: e["id"]), "matches": matches,
           "discovered_via": {k: sorted(discoveries[k]) for k in matches if discoveries[k]}}
    INDEX.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Published {len(entries)} originals and {len(matches)} catalogue matches")


def search(query, kind=None, limit=10):
    words = norm(query).split("-")
    hits = []
    for item in load(INDEX, {}).get("entries", []):
        if kind and item["type"] != kind:
            continue
        name = norm(item["name"])
        text = norm(" ".join([name, item.get("publisher", ""), item.get("description", ""), item.get("repo", "")]))
        if all(word in text for word in words):
            hits.append((name == norm(query), sum(word in name for word in words), item))
    hits.sort(key=lambda hit: (-int(hit[0]), -hit[1], hit[2]["id"]))
    return [item for _, _, item in hits[:limit]]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--find", help="Search published originals locally and output JSON")
    parser.add_argument("--type", choices=("skill", "tool", "connector"))
    args = parser.parse_args()
    if args.find is None:
        refresh()
    else:
        print(json.dumps(search(args.find, args.type), indent=2, ensure_ascii=False))
