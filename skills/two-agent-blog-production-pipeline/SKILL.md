---
name: two-agent-blog-production-pipeline
description: "Use when automating blog post creation and publishing end-to-end with two specialized Claude Code agents — one for writing/image generation and one for CMS publishing."
---

# Two-Agent Blog Production Pipeline

## Overview
This skill uses two specialized AI agents in sequence to fully automate blog post creation and publishing. A writer agent drafts the post and generates a cover image; a publisher agent handles all CMS operations including slug, meta tags, cache rebuild, and URL logging.

## Key Techniques
- Assign distinct roles: writer agent (creative) vs. publisher agent (operational/CMS)
- Use a shared spec/brief file as the coordination layer between agents
- Have the publisher agent log the final published URL for traceability

## How to Apply
1. Create a shared spec file that defines the post topic, tone, target URL slug, and any brand constraints.
2. Run the writer agent (e.g., Nova) with the spec file — it drafts the post in the author's voice and generates a cover image.
3. Run the publisher agent (e.g., Rack) with the writer's output — it reads the blog-style file, publishes to the CMS, sets slug and meta tags, rebuilds the cache, and logs the URL.
4. Check the logged URL to confirm a successful publish.

## Examples
- Nova (writer agent) drafts a post in the author's voice and makes the cover image.
- Rack (publisher agent) reads the blog-style file, publishes to the CMS, sets slug and meta tags, rebuilds the cache, and logs the URL.
- A shared spec file keeps both agents in sync.

## Source
Extracted from: [Two AI agents run my blog, one writes one ships](https://www.youtube.com/watch?v=Mz2wJr-rj4I)
Channel: Professor Glitch
