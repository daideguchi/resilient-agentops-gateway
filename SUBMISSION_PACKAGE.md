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
- decision contract for retry, fallback, approval, and stop rules
- Gateway I/O contract for request, route decision, response, and audit receipt
- evidence receipts that separate simulated product workflow from attached live TrueFoundry proof
- TrueFoundry challenge-fit summary for routing, fallback, governance, and evidence

## DevNetwork Fit

The best fit is the TrueFoundry resilient-agents challenge because the product is about gateway routing, fallbacks, and controlled recovery.

## Current Proof

```text
node scripts/verify_gateway.mjs
gateway_verify_ok
track_fit_items=4
policy_items=4
receipt_items=4
contract_items=4
python3 scripts/verify_claim_boundary.py
gateway_claim_boundary_ok

python3 scripts/verify_no_secrets.py
gateway_no_secrets_ok

python3 scripts/verify_readme_review_hub.py
gateway_readme_review_hub_ok
```

Screenshots:

```text
media/resilient-agentops-gateway-full.png
media/resilient-agentops-gateway-pages-full.png
```

Demo video: draft walkthrough. Live TrueFoundry proof is attached separately as screenshot + sanitized response JSON.

Demo video draft:

```text
media/resilient-agentops-gateway-demo.mp4
https://raw.githubusercontent.com/daideguchi/resilient-agentops-gateway/main/media/resilient-agentops-gateway-demo.mp4
```

The repository now contains live TrueFoundry Gateway proof files:

```text
media/truefoundry-gateway-proof.png
media/truefoundry-gateway-response.json
```

## Claim Boundary

The product demo timeline is simulated. The live integration claim is intentionally narrow: one TrueFoundry Gateway chat-completion request succeeded with a sanitized 200 response, and the configured model account is visible in the dashboard screenshot.

## Integration Plan

The live step in `docs/TRUEFOUNDRY_INTEGRATION_PLAN.md` is complete. `scripts/verify_truefoundry_live.py` verifies the sanitized response JSON and screenshot without exposing API keys.
