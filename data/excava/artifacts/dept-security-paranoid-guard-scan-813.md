# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-813` (dept) · 2026-07-28T17:39:46.019881+00:00
> Participants: Warden, Bastion · synthesized by mistral/mistral-small-latest

**Decision:**

**Plan:**
1. Run LLM Guard scanner on all conversation input/output to detect leaks, injection, or unreal elements.
2. Generate a clean/unclean report flagging any anomalies for verification.
3. Cross-check flagged elements against known real data to confirm authenticity.
4. If anomalies are detected, quarantine and manually inspect the affected content.
5. Log all scan results and verification steps for audit purposes.
6. Proceed only after confirming all elements are real and secure.

**What changed:** Scanner execution initiated per Warden’s proposal.
