# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-461` (dept) · 2026-07-30T18:00:24.810440+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run LLM Guard scanner on conversation input/output to detect leaks, injections, or anomalies.
2. Generate and verify `/var/log/llm_guard/w1` report confirming no security risks.
3. Validate all elements (inputs, outputs, references) are real and not fake/dead.
4. If scan passes, proceed with Bastion’s next action; else, quarantine and alert.
5. Log Bastion’s wait state until Warden’s report is confirmed.
6. Re-scan periodically if conversation extends beyond initial verification.

**What changed:** Bastion now enforces mandatory LLM Guard validation before proceeding.
