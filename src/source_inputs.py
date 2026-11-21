"""Validated additional playlists and individual YouTube video inputs."""
from __future__ import annotations
import os
import re
from urllib.parse import parse_qs, urlparse

VIDEO = re.compile(r"^[A-Za-z0-9_-]{11}$")
PLAYLIST = re.compile(r"^[A-Za-z0-9_-]{10,}$")
HOSTS = {"youtube.com", "www.youtube.com", "m.youtube.com", "music.youtube.com"}


def parse_source(value):
    value = value.strip()
    if VIDEO.fullmatch(value):
        return "video", value
    parsed = urlparse(value)
    if parsed.scheme not in {"https", "http"} or parsed.username or parsed.password:
        raise ValueError("Expected a YouTube video or playlist URL")
    host = (parsed.hostname or "").lower()
    query = parse_qs(parsed.query)
    if host in HOSTS:
        parts = parsed.path.strip("/").split("/")
        vid = query.get("v", [""])[0] if parsed.path == "/watch" else (
            parts[1] if len(parts) == 2 and parts[0] in {"shorts", "live", "embed"} else "")
        if VIDEO.fullmatch(vid):
            return "video", vid
        playlist = query.get("list", [""])[0]
        if PLAYLIST.fullmatch(playlist):
            return "playlist", playlist
    elif host == "youtu.be" and VIDEO.fullmatch(parsed.path.strip("/")):
        return "video", parsed.path.strip("/")
    raise ValueError("Unsupported or invalid YouTube source")


def configured_sources(config):
    playlists = [config["playlist_id"]] if config.get("playlist_id") else []
    playlists.extend(config.get("playlist_ids", []))
    videos = []
    values = list(config.get("video_urls", []))
    values.extend(filter(None, re.split(r"[\s,]+", os.environ.get("SOURCE_URLS", ""))))
    for value in values:
        kind, identifier = parse_source(value)
        (playlists if kind == "playlist" else videos).append(identifier)
    for identifier in playlists:
        if not isinstance(identifier, str) or not PLAYLIST.fullmatch(identifier):
            raise ValueError("Invalid configured playlist ID")
    return list(dict.fromkeys(playlists)), list(dict.fromkeys(videos))


def collect(youtube, config, playlist_fetcher):
    playlists, video_ids = configured_sources(config)
    records = {}
    for playlist in playlists:
        for record in playlist_fetcher(youtube, playlist):
            entry = records.setdefault(record["video_id"], {**record, "source_playlists": []})
            if playlist not in entry["source_playlists"]:
                entry["source_playlists"].append(playlist)
    missing = [vid for vid in video_ids if vid not in records]
    for start in range(0, len(missing), 50):
        response = youtube.videos().list(part="snippet", id=",".join(missing[start:start+50])).execute()
        for item in response.get("items", []):
            snippet = item.get("snippet", {})
            records[item["id"]] = {
                "video_id": item["id"], "title": snippet.get("title", ""),
                "description": snippet.get("description", ""),
                "publishedAt": snippet.get("publishedAt", ""),
                "channel_name": snippet.get("channelTitle", ""),
                "source_playlists": [], "discovered_via": "direct_url",
            }
    return list(records.values())
