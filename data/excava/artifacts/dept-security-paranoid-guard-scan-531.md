# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-531` (dept) · 2026-07-10T17:45:46.263382+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:** Full automated security scans of all external-facing systems will run every 24 hours, with alerts triaged by severity before logging.

**Plan:**
1. Deploy automated security scans covering all external-facing systems daily.
2. Implement pre-logging triage to suppress low-risk/transient issues and only alert on critical/high-severity findings.
3. Log triaged alerts quietly for periodic review without overwhelming the team.
4. Require manual review of all high-severity alerts within 24 hours of detection.
5. Document and maintain a "criticality filter" to classify systems by risk level for future tuning.

**What changed:** Alerts are now triaged *before* logging, not after suppression.
