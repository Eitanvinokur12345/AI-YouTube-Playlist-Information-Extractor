# Raise G8 Personal fit (68/100): 20% of designs taste-tagged; Arena learning live; NOSG wired (next: taste beyond

> visual · task `raise-g8-personal-fit-68-84598` · **EXECUTION PLAN — NOT yet executed** · by mistral/mistral-small-latest

```markdown
**Approach:** Tag 20% of designs with taste labels, wire NOSG for live Arena learning, and extend taste beyond current scope.

**Steps:**
1. **Tagging:** Run `./scripts/tag_taste.py --threshold 0.2 --output data/taste_tags.json` to label 20% of designs in `designs/` (filter by `./scripts/filter_designs.py --size 17 --value 32`).
2. **Arena Learning:** Deploy `./services/arena_learning.yml` with `kubectl apply -f services/arena_learning.yml` (requires `kubectl` + `arena-learning:0.3.1` image).
3. **NOSG Wiring:** Update `config/nosg.json` with `{"taste_enabled": true, "arena_endpoint": "http://arena-learning:8080"}` and restart `nosg-service` (`systemctl restart nosg`).
4. **Taste Extension:** Add `taste_dimensions` to `schemas/design.json` (fields: `aesthetic`, `craftsmanship`, `innovation`) and regenerate docs (`./scripts/generate_docs.sh`).

**Needs:**
- `designs/` (17 small designs, value 32)
- `./scripts/tag_taste.py` (Python 3.10+, `taste-model:v1.2`)
- `arena-learning:0.3.1` (container image)
- `kubectl` + Kubernetes cluster (minikube for local)
- `nosg-service` (systemd service, config in `/etc/nosg/`)
```
