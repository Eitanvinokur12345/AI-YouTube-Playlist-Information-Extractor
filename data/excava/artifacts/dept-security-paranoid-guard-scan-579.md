# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-579` (dept) · 2026-07-30T19:39:37.821937+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run LLM Guard in real-time scan mode against the current input/output stream to detect leaks, injections, or anomalies.
2. Verify all elements (e.g., messages, references) are real (not fake/dead) by cross-checking sources.
3. Log and flag any detected anomalies for manual review.
4. If anomalies are found, quarantine the affected data and halt further processing until resolved.
5. Generate a live security verdict on the conversation's safety status.
6. If clean, proceed with the conversation; if compromised, terminate and alert the operator.

**What changed:** LLM Guard real-time scanning and verification now enforced as mandatory pre-processing.
