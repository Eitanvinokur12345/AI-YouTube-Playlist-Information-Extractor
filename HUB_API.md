# Excavatortron Hub API

Excavatortron is a free, self-running pipeline that mines a YouTube AI playlist + 50 web news
sources into a clean, **machine-readable hub of AI knowledge** — skills, tools, models, MCP
connectors, prompts, commands, and news. This page is for **other programs / future systems** that
want to consume the data (humans want the [dashboard](https://eitanvinokur12345.github.io/AI-YouTube-Playlist-Information-Extractor/docs/index.html)).

## One entry point

```
GET https://eitanvinokur12345.github.io/AI-YouTube-Playlist-Information-Extractor/data/hub.json
```

`hub.json` is a versioned **manifest**: it lists every dataset, its public URL, item count, and
field list, plus totals and a north-star description. Start there, then fetch the datasets you need.

- **CORS-open** — GitHub Pages sends `Access-Control-Allow-Origin: *`, so you can `fetch()` it from a browser app.
- **No key, no auth, no rate limit** (it's static JSON on a CDN).
- **Freshness** — the pipeline refreshes roughly every 3 hours. Poll `hub.json`'s `generated_at`
  (or any file) to detect updates.
- **Stable IDs** — content items carry a `slug` (skills/tools/connectors) you can key on.

## Datasets

Each content file is a JSON object shaped `{ <root_key>: [ ...items ] }`. The manifest's
`datasets[]` gives the exact `file`, `url`, `root_key`, `count`, and `fields` for each. Today:

| dataset | file | what |
|---|---|---|
| skills | `skills.json` | techniques you DO with AI |
| tools | `tools.json` | products/tools that exist |
| models | `models.json` | ranked AI models (subset of tools) |
| connectors | `connectors.json` | MCP servers / connectors |
| prompts | `prompts.json` | reusable prompts |
| commands | `commands.json` | slash / CLI commands |
| daily/weekly/monthly_news | `*_web_news.json` | AI news from 50 web sources (`entries`) |
| effectiveness | `effectiveness.json` | per-lane quality/rigidity scoreboard |
| health | `health.json` | live counts (transcript coverage + totals) |

## Example

```js
const hub = await (await fetch(BASE + "data/hub.json")).json();
const skillsUrl = hub.datasets.find(d => d.id === "skills").url;
const { skills } = await (await fetch(skillsUrl)).json();
console.log(skills.length, "skills; updated", hub.generated_at);
```

## Provenance & license

Data is derived from **public** content; transcripts are quoted verbatim. No personal data is
included. Use freely; attribution appreciated.
