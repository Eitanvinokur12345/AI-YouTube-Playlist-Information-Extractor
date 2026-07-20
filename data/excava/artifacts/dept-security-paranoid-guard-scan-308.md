# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-308` (dept) · 2026-07-20T17:06:38.738742+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run the LLM Guard scanner on the conversation’s input/output stream to detect leaks, injection, or fake elements.
2. Generate a security report flagging any anomalies or violations for verification.
3. Verify all elements in the conversation are real (not fake/dead) based on the scanner’s output.
4. If anomalies are detected, quarantine and investigate the affected elements.
5. Apply fixes or adjustments to eliminate confirmed leaks or injections.
6. Re-scan to confirm resolution of all flagged issues.

**What changed:** Scanner integration and verification steps added to enforce security.
