# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-399` (dept) · 2026-07-31T21:07:39.840093+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:** Bastion approves the Warden’s LLM Guard scan and will execute it.

**Plan:**
1. Bastion runs LLM Guard on the full input/output stream of this room.
2. Warden generates a scan report confirming clean status or flags for review.
3. Bastion verifies the report’s authenticity and flags (if any).
4. If clean, Bastion marks the room as secure; if flagged, Bastion isolates and reviews.
5. Bastion logs the scan results and decision for audit.
6. Warden and Bastion cross-validate the scan’s findings.

**What changed:** LLM Guard scan execution is now mandatory and verified by Bastion.
