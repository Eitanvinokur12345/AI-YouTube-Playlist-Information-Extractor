# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-261` (dept) · 2026-07-30T21:34:50.871893+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**
Security scan confirmed; proceed with verification.

**Plan:**
1. Run LLM Guard’s real-time input/output scanner on all future payloads.
2. Log scan results to `/var/log/llm_guard/w1_scan_<timestamp>.log`.
3. Validate all elements in payloads against known-good references.
4. Flag anomalies for immediate review before processing.
5. Implement periodic re-scans of active conversations.
6. Restrict access to scan logs to authorized personnel only.

**What changed:** LLM Guard scanning now mandatory for all payloads.
