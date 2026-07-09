# security: Paranoid guard: scan for leaks/injection; VERIFY elements are REAL (not fake/dead); DETECT

> Decision artifact · room `dept-security-paranoid-guard-scan-411` (dept) · 2026-07-09T13:33:27.951205+00:00
> Participants: Warden, Audit, Bastion · synthesized by mistral/mistral-small-latest

**Decision:** Reject Warden’s symlink verification as non-atomic; enforce real-time lstat() + O_NOFOLLOW checks to guarantee target state.

**Plan:**
1. Write C program using `lstat()` with `O_NOFOLLOW` to atomically verify symlink targets.
2. Compile the program with `-O2` for performance.
3. Run the program on `/` to detect dangling symlinks.
4. Output verified dangling symlinks with absolute paths.
5. Log results to `dangling_symlinks.log`.
6. Exit with `0` on success, `1` on detection.

**What changed:** Enforced atomic `lstat(O_NOFOLLOW)` verification replacing non-atomic `[ ! -e ]` checks.
