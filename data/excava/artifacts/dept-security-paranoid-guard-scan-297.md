# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-297` (dept) · 2026-07-09T22:00:45.721268+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:** Reject Warden’s plan; require triple-verification.

**Plan:**
1. Fetch vendor-signed SHA256SUMS and GPG-signed Release file for `rkhunter`/`tripwire` via HTTPS from Ubuntu’s official repo.
2. Verify GPG signature of the Release file against Ubuntu’s offline-trusted key.
3. Compare local binaries’ hashes against the signed SHA256SUMS and offline archive.
4. Only if checksums match, run `rkhunter` and `tripwire` to scan for rootkits/tampered files.
5. Cross-check open ports (`ss -tulnp`) and processes (`ps aux`) against known-good baselines.
6. Audit `/etc/cron*`, `/var/spool/cron`, and `/tmp` for unauthorized cron jobs.

**What changed:** Added GPG verification and offline hash comparison before running integrity tools.
