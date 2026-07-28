# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-209` (dept) · 2026-07-28T23:26:45.407895+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run LLM Guard scanner on conversation input/output to generate clean/dirty report.
2. Verify all elements (messages, users, links) are real and not fake/dead.
3. If scan is clean, proceed with confidence; if flagged, quarantine and review.
4. Log scan results and verification steps for audit.
5. If leaks/injection detected, terminate session and alert security.
6. If clean, archive conversation with integrity hash.

**What changed:** Scanner executed, verification pending report.
