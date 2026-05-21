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
  verifies evidence receipts, including attached live TrueFoundry receipt
  captures screenshot

scripts/verify_claim_boundary.py
  fails if docs claim live TrueFoundry Gateway proof before a real proof file exists

scripts/truefoundry_smoke_request.py
  live smoke test
  uses TRUEFOUNDRY_API_KEY and TRUEFOUNDRY_MODEL from env
  writes sanitized response metadata only

scripts/verify_truefoundry_live.py
  live-proof gate
  requires sanitized response proof and dashboard screenshot
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
  "status": "attached",
  "note": "Sanitized live Gateway response and dashboard proof are stored under media/."
}
```

## TrueFoundry Proof

- TrueFoundry self-hosted model account is configured
- one Gateway chat-completion response is saved as sanitized JSON
- dashboard proof is saved as a public-safe screenshot
- runtime keys remain outside the repository

Detailed account and proof steps are in `docs/TRUEFOUNDRY_INTEGRATION_PLAN.md`.
