# Submission Package — Resilient AgentOps Gateway

## Title

Resilient AgentOps Gateway

## Short Description

A gateway cockpit for resilient AI agents, showing model fallback, cost, risk, approval, and evidence instead of hiding failures inside logs.

## Problem

AI agents fail in messy ways: model timeouts, high cost, unsafe actions, weak evidence, and unclear handoffs. Builders need more than a final answer. They need to see how the system recovered.

## Solution

Resilient AgentOps Gateway turns agent execution into a reviewable operations view:

- route decision
- fallback path
- risk reason
- cost estimate
- human approval checkpoint
- evidence reference
- final handoff status
- TrueFoundry challenge-fit summary for routing, fallback, governance, and evidence

## DevNetwork Fit

The best fit is the TrueFoundry resilient-agents challenge because the product is about gateway routing, fallbacks, and controlled recovery.

## Current Proof

```text
node scripts/verify_gateway.mjs
gateway_verify_ok
track_fit_items=4
python3 scripts/verify_claim_boundary.py
gateway_claim_boundary_ok
```

Screenshots:

```text
media/resilient-agentops-gateway-full.png
media/resilient-agentops-gateway-pages-full.png
```

Demo video: pending until the static walkthrough and any live TrueFoundry proof boundaries are final.

Demo video draft:

```text
media/resilient-agentops-gateway-demo.mp4
```

This draft does not claim live TrueFoundry Gateway execution.

## Claim Boundary

TrueFoundry has not been installed or called yet. This package does not claim live TrueFoundry execution.

## Integration Plan

The next live step is tracked in `docs/TRUEFOUNDRY_INTEGRATION_PLAN.md`: create a real TrueFoundry Gateway workspace/key, route one sample request through a virtual model, save dashboard or response proof under `media/`, then update the claim boundary.

`scripts/truefoundry_smoke_request.py` and `scripts/verify_truefoundry_live.py` are present for that step, but the live verifier is expected to fail until real TrueFoundry proof exists.
