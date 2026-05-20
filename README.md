# Resilient AgentOps Gateway

Hackathon target: DevNetwork AI+ML Hackathon 2026

Track direction: TrueFoundry resilient agents

## Product Thesis

Agents do not just need better prompts. They need a visible gateway that shows failures, fallbacks, cost, risk, and human approval.

Resilient AgentOps Gateway is a dashboard for understanding how an AI workflow behaved when the first model/tool path was not good enough.

## Live Demo

GitHub Pages target:

```text
https://daideguchi.github.io/resilient-agentops-gateway/
```

## Verify

```bash
node scripts/verify_gateway.mjs
python3 scripts/verify_claim_boundary.py
```

Expected:

```text
gateway_verify_ok
gateway_claim_boundary_ok
```

## TrueFoundry Status

The product is shaped for the TrueFoundry AI Gateway challenge direction, but no live TrueFoundry Gateway request has been made yet. The next integration step is documented in [docs/TRUEFOUNDRY_INTEGRATION_PLAN.md](docs/TRUEFOUNDRY_INTEGRATION_PLAN.md).

## Claim Boundary

This is a local/public MVP. TrueFoundry Gateway has not been installed or called yet. The UI is shaped for that track, but no live TrueFoundry execution is claimed.
