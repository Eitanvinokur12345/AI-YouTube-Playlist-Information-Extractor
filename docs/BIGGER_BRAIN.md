# The Bigger Brain — Obsidian + Graphify

The dashboard's in-page graph is deliberately capped (~850 nodes) so it stays readable in a browser
canvas. For the *full* brain (every skill, tool, model, connector, prompt and their links — 3,000+
nodes) use the two heavy-duty surfaces below. They cover the two halves the owner asked to combine.

## 1. Graphify (graphify.net) — the huge interactive graph
Graphify is an open-source knowledge-graph tool that imports **GraphML**. The pipeline exports the
whole brain every cycle to **`data/brain.graphml`**.

- Download: `https://eitanvinokur12345.github.io/AI-YouTube-Playlist-Information-Extractor/data/brain.graphml`
- Each node carries `label`, `type` (skill/tool/model/connector/category/toolhub), `category`,
  `quality`, and `url` (the resolved homepage/GitHub), so you can colour by type, size by quality,
  and click through to the real tool.
- Load it into **Graphify** (or **Gephi** / **Neo4j** / **yEd** — all read GraphML) for a large,
  clustered, zoomable graph far beyond what a browser canvas can show.

## 2. Obsidian — the note brain
`src/build_brain.py` writes a full Obsidian vault (a note per skill/tool/prompt/connector, wikilinked
to category + tool hubs, with the structural Project notes). Open the vault in Obsidian and use its
own Graph View for the note-linked brain.

## How they combine
- **Graphify/GraphML** = the big-picture *structure* (clusters, hubs, the whole web at once).
- **Obsidian** = the *content* (readable notes you can edit, link, and grow).
Both are generated from the same `data/` store every cycle, so they stay in sync as the library grows.
The browser dashboard stays the fast, capped "map"; these are the deep tools.
