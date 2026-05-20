# Architecture — Resilient AgentOps Gateway

## Current MVP

```text
index.html
  static gateway dashboard
  deterministic sample event model
  route/fallback/cost/risk/approval cards
  TrueFoundry challenge-fit summary
  decision contract renderer
  evidence receipts renderer
  timeline and final handoff packet

scripts/verify_gateway.mjs
  opens the app in Chrome
  verifies headline, timeline rows, fallback row, and claim boundary
  verifies challenge-fit rows
  verifies decision-contract rows
  verifies evidence receipts, including blocked live TrueFoundry receipt
  captures screenshot

scripts/verify_claim_boundary.py
  fails if docs claim live TrueFoundry Gateway proof before a real proof file exists

scripts/truefoundry_smoke_request.py
  future live smoke test
  uses TRUEFOUNDRY_API_KEY and TRUEFOUNDRY_MODEL from env
  writes sanitized response metadata only

scripts/verify_truefoundry_live.py
  future live-proof gate
  fails until sanitized response proof and dashboard screenshot both exist
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

## Decision Contract Shape

```json
{
  "name": "Fallback",
  "trigger": "missing evidence or weak confidence",
  "action": "route to reasoning model",
  "owner": "gateway"
}
```

## Evidence Receipt Shape

```json
{
  "name": "TrueFoundry receipt",
  "status": "blocked",
  "note": "Replace with sanitized live Gateway response before claiming execution."
}
```

## Next TrueFoundry Step

- install or access TrueFoundry Gateway
- route one real sample LLM call through it
- export request/response/fallback proof
- update README and verifier

Detailed account and proof steps are in `docs/TRUEFOUNDRY_INTEGRATION_PLAN.md`.
