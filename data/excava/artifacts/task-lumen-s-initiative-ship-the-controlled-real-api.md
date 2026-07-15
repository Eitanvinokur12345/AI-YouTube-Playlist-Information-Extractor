# [Lumen's initiative] Ship the controlled real API endpoint behind the feature flag tonight, limiting traffic to 5% of users, to quickly gathe

> visualization · task `lumen-s-initiative-ship--8184` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:**
Roll out the new API endpoint behind a feature flag with 5% traffic split using a progressive rollout strategy.

**Steps:**
1. **Enable feature flag in config:**
   - Edit `config/feature_flags.yml` to set `api_endpoint.enabled: true` with `rollout_percentage: 5`.
   - Commit and push to `main` branch.

2. **Deploy flag change to production:**
   - Run `kubectl apply -f k8s/feature-flag-configmap.yaml` to update the ConfigMap.
   - Trigger a rolling deployment with `kubectl rollout restart deployment/api-service -n production`.

3. **Verify traffic split:**
   - Check logs: `kubectl logs -l app=api-service -n production | grep "feature_flag=api_endpoint" | wc -l`.
   - Confirm 5% hit rate via Prometheus: `sum(rate(http_requests_total{flag="api_endpoint"}[5m])) by (flag) / sum(rate(http_requests_total[5m]))`.

4. **Monitor for errors:**
   - Watch Sentry for new errors: `sentry-cli monitor list --project api-service`.
   - Set up Datadog alert if error rate exceeds 0.1%: `datadog alerts create --query "sum:trace.api.errors{service:api-service}.as_rate() > 0.001"`.

5. **Rollback if needed:**
   - Revert flag to `rollout_percentage: 0` in `config/feature_flags.yml`.
   - Redeploy with `kubectl rollout restart deployment/api-service -n production`.

**Needs:**
- Access to
