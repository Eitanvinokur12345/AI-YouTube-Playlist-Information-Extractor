# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-111` (dept) · 2026-07-31T00:47:25.285182+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Warden runs LLM Guard scanner on the current input/output stream.
2. Security-w1 receives the real-time security verdict from the scan.
3. Verify all elements in the conversation are real (not fake/dead).
4. Detect and flag any leaks or injection attempts.
5. If threats are detected, quarantine the session and alert admins.
6. Log the scan results for audit and review.

**What changed:** LLM Guard scanner deployed on input/output stream for real-time security verification.
