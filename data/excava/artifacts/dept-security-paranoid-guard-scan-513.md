# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-513` (dept) · 2026-07-29T20:45:34.543880+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on all conversation inputs/outputs in real time to detect leaks, injections, or tampering.
2. Verify the authenticity of all referenced elements (e.g., files, links, commands) by cross-checking their existence and integrity.
3. Flag and quarantine any detected anomalies or suspicious content for manual review.
4. Log all scan results and verification steps for audit purposes.
5. Terminate the session if critical tampering or unauthorized access is confirmed.

**What changed:** Scanner integration and element verification now enforce real-time security checks.
