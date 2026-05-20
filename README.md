# Resilient AgentOps Gateway

Hackathon target: DevNetwork AI+ML Hackathon 2026

Track direction: TrueFoundry resilient agents

## Product Thesis

Agents do not just need better prompts. They need a visible gateway that shows failures, fallbacks, cost, risk, and human approval.

Resilient AgentOps Gateway is a dashboard for understanding how an AI workflow behaved when the first model/tool path was not good enough.

It is designed to make the TrueFoundry-style operations story visible: routing, fallback, governance, evidence, cost, and resume instructions.

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
track_fit_items=4
gateway_claim_boundary_ok
```

## TrueFoundry Status

The product is shaped for the TrueFoundry AI Gateway challenge direction, but no live TrueFoundry Gateway request has been made yet. The next integration step is documented in [docs/TRUEFOUNDRY_INTEGRATION_PLAN.md](docs/TRUEFOUNDRY_INTEGRATION_PLAN.md).

Future live-proof commands:

```bash
python3 scripts/truefoundry_smoke_request.py
python3 scripts/verify_truefoundry_live.py
```

These are expected to fail until a real TrueFoundry API key, virtual model, sanitized response proof, and dashboard screenshot exist.

## Claim Boundary

This is a local/public MVP. TrueFoundry Gateway has not been installed or called yet. The UI is shaped for that track, but no live TrueFoundry execution is claimed.
