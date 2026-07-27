# Deliver: Push link coverage toward 100% at +5%/day (the access gate)

> Decision artifact · room `war-deliver-push-link-coverage-t-428` (war) · 2026-07-27T08:09:42.168124+00:00
> Participants: Reel, Scriv, Chisel, Sift, Scope, Echo · synthesized by mistral/mistral-small-latest

**Decision:** Adopt the *Poisson-distributed delay* (40–50 minutes, mean 45) for alerts—hides the exact threshold while keeping the average predictable.

**Plan:**
1. Replace existing sliding-window/randomized-delay logic with a Poisson distribution (λ=45) for alert timing.
2. Implement ±5-minute jitter (40–50 min range) to obscure the true detection window.
3. Add debug mode flag to log the *actual* delay per alert for internal analysis.
4. Update alert documentation to reflect the new timing range (40–50 min).
5. Deploy to 10% of traffic for 24h A/B testing, then full rollout.
6. Monitor attacker evasion attempts via anomaly detection in alert logs.

**What changed:** Switched from fixed/jittered sliding windows to Poisson-distributed delays to balance debug clarity and attacker evasion resistance.
