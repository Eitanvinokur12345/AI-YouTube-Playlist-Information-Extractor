---
name: code-knowledge-graph-for-claude-code
description: "Use when working on large codebases with Claude Code to eliminate repeated file reads and dramatically reduce token costs by building a queryable Graphify knowledge graph first."
---

# Codebase Knowledge Graph for Claude Code Token Savings

## Overview
This technique uses Graphify to convert a code repository into a persistent, queryable knowledge graph before starting a Claude Code session. Instead of Claude Code re-reading source files on every query, it traverses the pre-built graph to find files, functions, and dependencies — reducing token consumption by up to 71x.

## Key Techniques
- **One-time indexing**: Graphify reads the entire codebase once and produces a graph database of file relationships, function calls, and imports.
- **Query without reading**: Claude Code queries the graph at any time without touching the underlying files.
- **Claude-assisted installation**: Tell Claude Code to install and configure Graphify — it handles the setup automatically.

## How to Apply
1. Have a local repository (clone one if needed, e.g. `git clone <repo>`).
2. Ask Claude Code: "Install Graphify and index this repository."
3. Claude Code installs Graphify, runs the indexer, and confirms the graph is built.
4. For any codebase question, ask Claude Code to query the graph rather than reading files directly.
5. The graph persists between sessions — only re-index when the codebase changes significantly.

## Examples
- Cloning Flask (a Python web framework) and asking Claude Code to map all route handlers without reading every file.
- Using the graph to find all usages of a deprecated function across a 500-file codebase in seconds.
- Asking "which modules import utils.py?" from the graph instead of running a grep over the whole repo.

## Source
Extracted from: [This map stops Claude Code re-reading your files](https://www.youtube.com/watch?v=1X6aW0zzSaw)
Channel: Renato Dinis | Build With AI
