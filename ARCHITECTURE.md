# Architecture — Resilient AgentOps Gateway

## Current MVP

```text
index.html
  static gateway dashboard
  deterministic sample event model
  route/fallback/cost/risk/approval cards
  timeline and final handoff packet

scripts/verify_gateway.mjs
  opens the app in Chrome
  verifies headline, timeline rows, fallback row, and claim boundary
  captures screenshot

scripts/verify_claim_boundary.py
  fails if docs claim live TrueFoundry Gateway proof before a real proof file exists
```

## Event Shape

```json
{
  "step": "retrieval",
  "primary": "fast-model",
  "fallback": "reasoning-model",
  "status": "fallback_used",
  "risk": "missing evidence",
  "cost_usd": 0.018,
  "approval": "required",
  "evidence": "kb-ticket-1842"
}
```

## Next TrueFoundry Step

- install or access TrueFoundry Gateway
- route one real sample LLM call through it
- export request/response/fallback proof
- update README and verifier

Detailed account and proof steps are in `docs/TRUEFOUNDRY_INTEGRATION_PLAN.md`.
