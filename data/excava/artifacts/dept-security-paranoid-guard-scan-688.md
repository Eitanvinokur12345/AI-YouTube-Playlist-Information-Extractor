# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-688` (dept) · 2026-07-30T20:09:05.133203+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden runs LLM Guard in real-time scan mode against the current input/output stream.
2. LLM Guard produces a security verdict for every message before further processing.
3. Verify all elements are real (not fake/dead) post-scan.
4. Detect leaks/injections in real-time as messages are processed.
5. Flag or block any message failing the security verdict.
6. Log all scan results for auditing.

**What changed:** Real-time security scanning implemented with LLM Guard.
