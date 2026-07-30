# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-328` (dept) · 2026-07-30T03:44:38.805261+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:** Exchange accepted as clean after verification.

**Plan:**
1. Run LLM Guard scanner on conversation input/output.
2. Verify scan report in `/var/log/llm_guard/w1_scan` for leaks/injections/unreal elements.
3. Confirm Warden’s scan report before accepting exchange.
4. Log verification status in `/var/log/llm_guard/verification.log`.
5. Mark conversation as sanitized if report is clean.
6. Proceed with secure processing if no anomalies detected.

**What changed:** Exchange validated via Warden’s LLM Guard scan and Bastion’s verification.
