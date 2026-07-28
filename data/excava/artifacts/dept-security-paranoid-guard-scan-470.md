# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-470` (dept) · 2026-07-28T22:58:20.085931+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on all conversation input/output to detect leaks, injection, or anomalies.
2. Verify all elements (e.g., URLs, files, commands) are real and not fake/dead links.
3. Flag and quarantine any suspicious content or policy violations for review.
4. Cross-check scanner results with manual validation of critical elements.
5. Log and timestamp all scan actions for auditability.
6. If anomalies detected, isolate and analyze before proceeding.

**What changed:** Security scan and verification now mandatory for all inputs/outputs.
