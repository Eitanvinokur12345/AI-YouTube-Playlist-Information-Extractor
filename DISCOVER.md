# Web Tool Discovery (weekly, night)

Read by `.github/workflows/discover.yml` (weekly, night Israel time). Find **new AI tools that
are NOT yet in `data/tools.json`** from across the web and add them — with strong coverage of
**MCP servers** and **open-source / GitHub** projects. Governed by `config.tool_discovery`
(`mode`, `directories`, `web_search`, `emphasis`, `max_new_per_run`). Free: public web +
the Pro/Max subscription token. Night-gated by its schedule so it never eats daytime quota.

## Golden rules
1. **Only ADD net-new tools.** Load `data/tools.json` first; never duplicate. Dedup by name
   (case-insensitive) and obvious aliases. If a found tool already exists, at most enrich a
   missing field — do not create a second record.
2. **Never touch frozen/starred records or any other data file.** This stage only appends to
   `data/tools.json` (and re-sorts it).
3. **Be real, not boilerplate.** Apply CLAUDE.md's anti-boilerplate gate: a real name + a
   specific 1–2 sentence "what it does". No "X is an AI tool that enhances productivity" stubs.
4. **Respect the cap** `config.tool_discovery.max_new_per_run` (default 60). Stop when reached.

## Sources (`mode: "both"` → do BOTH)
- **Curated directories / GitHub** (`config.tool_discovery.directories`): GitHub Trending (AI
  topics) + "awesome-*" lists (**incl. `awesome-mcp-servers`** and awesome-ai/llm), Product Hunt
  AI, Hugging Face (models/Spaces), There's An AI For That. Use `WebFetch` on these.
- **Open web search** (`web_search: true`): `WebSearch` for queries like "new AI tools this
  week", "new MCP servers", "open source LLM tools GitHub", "AI tool launch <month> 2026".
- **Emphasis** (`emphasis`): prioritise **MCP servers** and **open-source** projects, but
  include strong closed tools too.

## For each genuinely new tool
Build a `tools.json` record exactly like CLAUDE.md Step 3b (name w/ version, slug, category ∈
`config.categories`, company, country, open_source, description, quality_score 1–10 from the
evidence you can see, `source_url` = where you found it). Plus:
- `discovered_via: "web_discovery"`, `discovered_at: <ISO>`.
- `is_open_source: true` for GitHub/OSS; `is_mcp: true` for MCP servers (also consider adding it
  to `data/connectors.json` if it's a connector/MCP server, per the connectors schema).
- `endorsement_video_ids: []` and `mentions: 0` (it came from the web, not a video).
- **`release_status`**: `"released"` normally, or **`"upcoming"`** if it's announced-but-not-yet-
  shipped (+ `expected_release`). Upcoming tools show in the **Coming Soon** tab.

## Step 2 — Resolve comment-gated resources (PUBLIC-only, never comment)

Some videos say *"comment X and I'll send you the link / the skills / the MCP / the tool"*. The
owner wants that resource — but you must NEVER post a comment, never automate any action on
YouTube, and never use the owner's account (that violates YouTube's ToS and gets accounts
banned). The "comment X" is just an engagement trick; the resource is almost always findable
**publicly elsewhere**. Read `data/comment_gated.json` and for each unresolved item:

1. **Web-search for it** (`WebSearch`): combine the creator/channel name + the resource or tool
   name + terms like `github`, `free`, `download`, plus the comment keyword if one was given.
   Try `<creator> <tool> repo`, `<tool name> github`, `<video title> resource`.
2. **Mine the creator's PUBLIC footprint**: the FULL video description (the link is often lower
   down / under "show more"), the **pinned comment** and the creator's own public replies, and
   the channel's About / linked site / Linktree / GitHub profile.
3. **If found**, follow the URL with `WebFetch` and extract its skills/tools/connectors exactly
   like Step 1's resource handling (an awesome-list / repo can yield MANY items, up to
   `max_items_per_resource`). Tag each record `discovered_via: "gated_resolved_public"` and set
   the `comment_gated` entry `status: "resolved"` with the `resolved_url`.
4. **If genuinely not findable publicly**, set `status: "unresolved"` and leave it for the owner
   (it stays in the dashboard's "Behind a comment-wall" list). Do not guess a URL.

This recovers most gated resources legitimately, with no account and no commenting.

## Finish
Re-sort `tools.json` (mentions desc, then quality desc, then name). Append a one-line note to
`data/discovery_log.json` (`{runs:[{ran_at, added, scanned_sources, notable[]}]}`). Commit.
Keep the whole run under a sensible token budget; if you approach it, finish the current tool,
log, and stop cleanly.
