"""Materialize the immutable ledger from a local checkout of its pinned commit."""
import collections
import gzip
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

FREEZE = "2ce91d7becac95063a9842fd01cf0998b1ae16ea"
root = Path(sys.argv[1]).resolve()
if subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip() != FREEZE:
    raise SystemExit("Expected an exact frozen checkout")
sys.path.insert(0, str(root))
from src.element_model import TYPES, _get, _slug

ledger = collections.defaultdict(list)
def read(name):
    return json.loads((root / "data" / (name + ".json")).read_text())

def add(key, ref):
    if ref not in ledger[key]:
        ledger[key].append(ref)

def record_key(record):
    return hashlib.sha256(json.dumps(record, sort_keys=True, ensure_ascii=False).encode()).hexdigest()

def url(value, ref):
    if not isinstance(value, str) or not value.startswith(("http://", "https://")):
        return
    value = value.strip()
    key = "url:" + value.split("#")[0]
    try:
        parts = urlsplit(value)
        host, path = (parts.hostname or "").lower(), parts.path
        video = parse_qs(parts.query).get("v", [""])[0] if host in ("youtube.com", "www.youtube.com", "m.youtube.com") else ""
        if host == "youtu.be" or (host.endswith("youtube.com") and path.startswith(("/shorts/", "/embed/", "/live/"))):
            video = path.strip("/").split("/")[-1]
        if re.fullmatch(r"[A-Za-z0-9_-]{11}", video):
            key = "yt:" + video
        elif host == "github.com" and len(path.strip("/").split("/")) == 2:
            key = "repo:" + path.strip("/").removesuffix(".git").lower()
        elif host in ("arxiv.org", "www.arxiv.org") and path.startswith("/abs/"):
            key = "arxiv:" + re.sub(r"v\d+$", "", path[5:])
    except ValueError:
        key = "url:" + value
    add(key, ref)

for i, row in enumerate(read("video_catalog")["videos"]):
    add("yt:" + row["video_id"], f"video_catalog/videos/{i}")
for lane in ("processed", "_pending"):
    for file in sorted((root / "data" / lane).glob("*.json")):
        add("yt:" + file.stem, lane + "/" + file.name)
news = [(period + suffix, "entries") for period in ("daily", "weekly", "monthly") for suffix in ("_news", "_web_news")]
for name, field in [("web_news_store", "items"), ("social_intake", "items"), ("discovered_elements", "elements"), ("screen_urls", "urls")] + news:
    for i, row in enumerate(read(name)[field]):
        link = row.get("url") or row.get("link")
        ref = f"{name}/{field}/{i}"
        url(link, ref)
        if not link:
            add("record:" + record_key(row), ref)
for i, link in enumerate(read("mined_state")["urls"]):
    url(link, f"mined_state/urls/{i}")
for name, row in read("feeds_health")["feeds"].items():
    url(row["url"], "feeds_health/feeds/" + name)
config = json.loads((root / "config.json").read_text())
for i, row in enumerate(config["news_sources"]):
    url(row["url"], f"../config/news_sources/{i}")
for field in ("reddit_subreddits", "telegram_channels", "search_queries", "youtube_queries"):
    for i, value in enumerate(read("social_sources")[field]):
        add(field + ":" + value, f"social_sources/{field}/{i}")
for i, row in enumerate(read("elements_index")["elements"]):
    add(row["id"], f"elements_index/elements/{i}")
for kind, (filename, field, mapping) in TYPES.items():
    name = filename[:-5]
    for i, row in enumerate(read(name)[field]):
        slug = _get(row, mapping.get("slug", [])) or _slug(_get(row, mapping["name"]))
        ref = f"{name}/{field}/{i}"
        add(kind + ":" + slug, ref)
        for prop in ("url", "homepage", "github", "source_url", "install_or_source"):
            link = row.get(prop)
            if isinstance(link, str) and re.match(r"https?://(?:www\.)?(?:github\.com|youtube\.com|youtu\.be)/[^\s]+$", link):
                url(link, ref + "/" + prop)
for name in ("skills", "gemini_analyzed", "visual_state"):
    doc = read(name)
    for field in ("videos_seen", "video_ids", "failed_ids"):
        for i, value in enumerate(doc.get(field, [])):
            if isinstance(value, str) and re.fullmatch(r"[a-zA-Z0-9_-]{11}", value):
                add("yt:" + value, f"{name}/{field}/{i}")
for field, rows in read("comment_gated").items():
    for i, row in enumerate(rows):
        if isinstance(row, dict) and row.get("video_id"):
            add("yt:" + row["video_id"], f"comment_gated/{field}/{i}")
for i, row in enumerate(read("original_sources")["entries"]):
    url(row.get("repo") or row.get("url"), f"original_sources/entries/{i}")
for name in ("commands_quarantine", "deleted_commands", "deleted_skills", "creations_quarantine", "_removed_cross_tab"):
    doc = read(name)
    field = next((k for k in ("quarantined", "items", "removed") if k in doc), "")
    for i, row in enumerate(doc[field] if field else doc):
        add("archived:" + record_key(row.get("record", row)), name + "/" + (field + "/" if field else "") + str(i))
for i, process in enumerate(read("pipeline_scout")["processes"]):
    for j, row in enumerate(process.get("finds", [])):
        url(row.get("link"), f"pipeline_scout/processes/{i}/finds/{j}")
for field, groups in read("tips").items():
    for topic, rows in groups.items():
        for i, row in enumerate(rows):
            add("tip:" + record_key(row), f"tips/{field}/{topic}/{i}")
for i, row in enumerate(read("packages")["packages"]):
    add("package:" + row["id"], f"packages/packages/{i}")
for i, row in enumerate(read("channel_suggestions")["suggestions"]):
    add("channel:" + row["channel_id"], f"channel_suggestions/suggestions/{i}")
    for j, video in enumerate(row["videos"]):
        url(video["url"], f"channel_suggestions/suggestions/{i}/videos/{j}")
for field in ("playlist_id", "playlist_ids", "video_urls"):
    values = config.get(field, [])
    for i, value in enumerate([values] if isinstance(values, str) else values):
        if field.startswith("playlist"):
            add("playlist:" + value, "../config/" + field)
        else:
            url(value, f"../config/{field}/{i}")
social = {"x.com", "twitter.com", "reddit.com", "www.reddit.com", "huggingface.co", "t.me", "github.com", "www.github.com", "youtube.com", "www.youtube.com", "youtu.be"}
for lane in ("processed", "_pending"):
    for file in sorted((root / "data" / lane).glob("*.json")):
        row = json.loads(file.read_text())
        for field in ("links", "description"):
            value = row.get(field, [])
            value = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)
            for link in re.findall(r"""https?://[^\s<>"'()\\]+""", value):
                link = link.rstrip(".,;!?]")
                try:
                    parts = urlsplit(link)
                    if parts.hostname in social and len(parts.path.strip("/")) > 1:
                        url(link, lane + "/" + file.name + "#" + field)
                except ValueError:
                    continue
expected = json.loads(Path(__file__).with_name("scope-summary.json").read_text())
counts = collections.Counter(k.partition(":")[0] for k in ledger)
if dict(counts) != expected["by_namespace"]:
    raise ValueError(f"Namespace counts differ: {counts}")
dest = Path(sys.argv[2])
with gzip.GzipFile(str(dest), "wb", compresslevel=9, mtime=0) as stream:
    for key, refs in sorted(ledger.items()):
        stream.write((json.dumps([key, refs], separators=(",", ":"), ensure_ascii=False) + "\n").encode())
print(f"{len(ledger)} IDs, SHA-256 {hashlib.sha256(dest.read_bytes()).hexdigest()}")
