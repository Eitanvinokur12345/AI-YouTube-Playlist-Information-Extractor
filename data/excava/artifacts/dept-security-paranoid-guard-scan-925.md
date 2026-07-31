# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-925` (dept) · 2026-07-31T09:28:21.934252+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:** Approve Warden’s LLM Guard real-time scanner for input/output verification.

**Plan:**
1. Warden runs LLM Guard’s real-time scanner on all new conversation input/output.
2. Scanner outputs "clean" or "flagged" with detailed anomalies if detected.
3. If "flagged," Bastion halts further processing and isolates the input/output.
4. Warden logs all scan results for audit.
5. Bastion verifies scanner integrity before each use.
6. Repeat scan for any modified or retransmitted content.

**What changed:** Enforced mandatory real-time scanning for all incoming/outgoing data.
