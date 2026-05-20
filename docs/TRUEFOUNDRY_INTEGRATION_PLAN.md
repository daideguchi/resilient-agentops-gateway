# TrueFoundry Integration Plan

## Current Status

TrueFoundry Gateway has not been installed or called yet.

Resilient AgentOps Gateway is currently a public MVP that demonstrates the review surface a builder needs around model routing, fallback, cost, risk, approval, evidence, and handoff. Prize or challenge claims should not say a live TrueFoundry Gateway execution happened until real Gateway evidence exists.

## What We Know From Public Sources

- TrueFoundry describes AI Gateway as the proxy layer between applications and LLM providers / MCP servers, with governance and observability.
- TrueFoundry virtual models support routing across target models with load balancing, failover, retries, and fallback behavior behind one stable model name.
- TrueFoundry documents priority-based routing, latency-based routing, unhealthy target handling, and dashboard visibility for target traffic.
- TrueFoundry documents a global Gateway endpoint at `https://gateway.truefoundry.ai` for AI Model Gateway and MCP Gateway traffic.

Source links:

- https://www.truefoundry.com/docs/ai-gateway/intro-to-llm-gateway
- https://www.truefoundry.com/docs/ai-gateway/virtual-model
- https://www.truefoundry.com/docs/ai-gateway/globally-distributed-saas

## Required Human / Account Step

Install or access a real TrueFoundry AI Gateway workspace and create a project-specific API key.

Do not:

- paste a fake Gateway key
- claim a live Gateway call from the static demo
- use another project account without permission
- submit a live-integration claim before evidence exists

## Integration Slot

When the real workspace is available:

1. Create a virtual model with at least one primary target and one fallback target.
2. Route one small sample chat request through TrueFoundry Gateway.
3. Capture the response metadata or dashboard trace that proves which route was used.
4. Save proof under `media/`, for example `media/truefoundry-gateway-proof.png`.
5. Save a sanitized request / response artifact if allowed, for example `media/truefoundry-gateway-response.json`.
6. Update README, submission package, and the app packet from "not called yet" to the real verified status.

## Verification Command To Add Later

```bash
python3 scripts/verify_truefoundry_live.py
```

That verifier should only pass when a real Gateway proof file exists and the repo no longer relies only on the static MVP.
