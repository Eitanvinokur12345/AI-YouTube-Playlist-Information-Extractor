# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-973` (dept) · 2026-07-28T11:00:16.920145+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run LLM Guard scanner on the current conversation’s input/output to detect leaks, injection, or unreal elements.
2. Verify all elements (e.g., commands, references) are real and not fake/dead.
3. Flag and quarantine any anomalies or policy violations for review.
4. Confirm the integrity of the conversation’s content before proceeding.
5. Log the scan results for audit purposes.
6. Proceed only if the scan passes all checks.

**What changed:** Scanner execution initiated.
