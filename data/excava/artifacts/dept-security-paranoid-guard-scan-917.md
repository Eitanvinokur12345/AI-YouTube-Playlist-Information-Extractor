# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-917` (dept) · 2026-07-31T15:11:44.394347+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. **Run LLM Guard’s input/output scanner** on the active conversation to detect leaks, injection attempts, or anomalies in the exchange.
2. **Verify all elements (inputs/outputs, context, participants)** are real and not fake/dead by cross-checking with the original session state.
3. **Flag and quarantine** any suspicious or unverified content for further review.
4. **Log the scan results** in a secure audit trail for traceability.
5. **Re-run the scanner** post-quarantine to confirm no residual threats remain.
6. **Close the room** if no critical issues are detected, or escalate to the Warden if anomalies persist.

**What changed:** Room scan initiated; verification of real elements enforced.
