---
name: memory-optimization-llms
description: "Running 70B or 405B parameter models on a single 4GB or 8GB GPU."
---

# Memory Optimization for LLMs

## Overview
Techniques used to reduce the memory footprint of large language models during inference, enabling them to run on hardware with limited VRAM.

**Use case:** Running 70B or 405B parameter models on a single 4GB or 8GB GPU.

## Key steps
1. Utilize layer-by-layer loading to stream model weights from disk to CPU RAM as needed.
2. Employ Flash Attention to maintain flat memory usage even with long input sequences.

## Details
- **Category:** data
- **Tool:** AirLLM  ·  **Quality:** 5/10

## Source
Extracted from: https://www.youtube.com/watch?v=WgYS3W04aVA
