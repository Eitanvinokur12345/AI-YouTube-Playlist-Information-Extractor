# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-830` (dept) · 2026-07-30T20:06:29.311744+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:** Warden's proposal to run LLM Guard in real-time scan mode is approved.

**Plan:**
1. Warden executes LLM Guard in real-time scan mode against the current input/output stream.
2. LLM Guard returns a verdict: "CLEAR" or "BLOCKED with details."
3. If "CLEAR," proceed with normal operations.
4. If "BLOCKED," analyze details and take corrective action (e.g., sanitize input, terminate session).
5. Log all scan results for audit purposes.
6. Repeat scans for every new input/output interaction.

**What changed:** Real-time security scanning is now enforced.
