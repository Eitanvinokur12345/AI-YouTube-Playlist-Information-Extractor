# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-879` (dept) · 2026-07-30T18:02:02.070406+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Execute LLM Guard scanner on conversation input/output to verify no leaks or injection vectors.
2. Wait for Warden to produce a clean scan report in `/var/log/llm_guard/w1`.
3. Validate report integrity before proceeding.
4. Confirm all elements are real (not fake/dead) post-scan.
5. Proceed only if scan passes and verification succeeds.

**What changed:** Bastion enforced mandatory LLM Guard scan and verification before further actions.
