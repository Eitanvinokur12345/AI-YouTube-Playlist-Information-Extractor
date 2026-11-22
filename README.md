# EXCAVATORTRON

A video knowledge library that retrieves content from YouTube playlists and the web, analyzes it, and organizes the extracted tools, skills, models, prompts, commands, connectors and design references.

## Finding original implementations

Start with [the publisher index](data/original_sources.json). Search `entries` by name, type or publisher. For a skill, `raw_url` retrieves the publisher’s exact SKILL.md, `package_url` opens its companion files at the same revision and `sha256` identifies the document bytes. For tools and MCP connectors, `url` opens the publisher’s implementation or product website. See [agent lookup instructions](AGENTS.md).

## Core workflow
1. Fetch the configured playlist, extra playlist IDs or direct YouTube URLs.
2. Recover captions or use the existing audio/visual analysis lane.
3. Extract grounded findings, keep their source links, and categorize them.
4. Browse findings in the knowledge library.
5. Refresh quality reports, related entries, reusable packages and public data exports.

A transcript establishes retrieval, not completed analysis. Historical records without explicit analysis evidence are labeled accordingly.

## Run locally
```powershell
python -m src.video_catalog
python -m http.server 8787 --bind 127.0.0.1
```

Open `http://127.0.0.1:8787/docs/`. For retrieval, install `requirements.txt` and configure the existing provider environment variables; secrets stay outside source control.

`config.json` retains the primary `playlist_id`. Optional `playlist_ids` and `video_urls` add more sources. The Fetch workflow accepts additional video/playlist URLs in `source_urls`; it does not execute URLs as shell commands.

## EXCAVA
The agentic OS is **preserved and disconnected** under [plugins/excava](plugins/excava/README.md). It is a candidate for a later optional plugin, not the main product. Its original source blobs, workflows and frontend are retained. Its data remains in the existing database. The core does not import or start it.

## Checks
```text
python -m unittest discover -s tests -v
python -m compileall -q src
node --check docs/dashboard.js
node --check docs/video-library.js
node --check docs/sw.js
```

See [SESSION_HANDOFF.md](SESSION_HANDOFF.md) for current scope and [HUB_API.md](HUB_API.md) for external data access.
