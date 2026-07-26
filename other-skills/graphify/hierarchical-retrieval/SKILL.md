---
name: hierarchical-retrieval
description: "Efficiently querying complex knowledge bases to get relevant information without processing the entire corpus, minimizing token usage."
---

# Hierarchical Retrieval

## Overview
Retrieving information from a knowledge graph by navigating through different levels of abstraction (e.g., 'God nodes' for high-level, then drilling down).

**Use case:** Efficiently querying complex knowledge bases to get relevant information without processing the entire corpus, minimizing token usage.

## Key steps
1. Always prompt for 'God nodes' (high-level nodes) first to get an overview.
2. Then, use the LLM to 'extract' information from the graph, rather than asking it to 'go through' the entire graph.

## Details
- **Category:** data
- **Tool:** Graphify  ·  **Quality:** 5/10

## Source
Extracted from: https://www.youtube.com/watch?v=Ro3Xf1AxVjs
