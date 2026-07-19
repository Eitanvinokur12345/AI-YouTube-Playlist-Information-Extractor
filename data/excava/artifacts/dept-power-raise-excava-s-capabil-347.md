# power: Raise EXCAVA's capability by even 0.5%: find new tools, best/newest models, combine elemen

> Decision artifact · room `dept-power-raise-excava-s-capabil-347` (dept) · 2026-07-19T04:05:22.865426+00:00
> Participants: Dynamo, Gearbox, Torque · synthesized by mistral/mistral-small-latest

**Decision:**
Adopt Qwen2.5-72B-Instruct for EXCAVA after a 7-day shadow test, promoting it if stable.

**Plan:**
1. Run a 7-day shadow test of Qwen2.5-72B-Instruct (128K context) against Llama-3.2-3B-Instruct in EXCAVA.
2. Monitor stability, truncation, and output quality during the shadow test.
3. If stable with no truncation on long documents, promote Qwen2.5-72B-Instruct to production.
4. Archive Llama-3.2-3B-Instruct as a fallback.
5. Allocate compute budget to validate Qwen2.5-72B-Instruct’s 128K window long-term.
6. Document latency and cost trade-offs for future optimization.

**What changed:**
Qwen2.5-72B-Instruct replaces Llama-3.2-3B-Instruct in EXCAVA after successful shadow testing.
