# Resilient AgentOps Gateway

Hackathon target: DevNetwork AI+ML Hackathon 2026

Track direction: TrueFoundry resilient agents

## Product Thesis

Agents do not just need better prompts. They need a visible gateway that shows failures, fallbacks, cost, risk, and human approval.

Resilient AgentOps Gateway is a dashboard for understanding how an AI workflow behaved when the first model/tool path was not good enough.

It is designed to make the TrueFoundry-style operations story visible: routing, fallback, governance, evidence, cost, and resume instructions.

The latest surface also includes an explicit decision contract and evidence receipts, so a reviewer can see when the gateway retries, when it falls back, when it pauses for human approval, and which proof is still simulated versus blocked.

## Judge Quick Read

Who it helps: teams running AI agents that need reliable operations, not just impressive final answers.

The problem: when an agent fails, retries, changes model, spends money, or needs human approval, that story often disappears inside logs.

How Resilient AgentOps Gateway solves it: the cockpit shows route decisions, fallback, risk, cost, approval gates, evidence receipts, and the handoff packet in one reviewable surface.

What is proven now: the public app, screenshots, demo video draft, verifiers, decision contract, Gateway I/O contract, and evidence receipts are live. TrueFoundry execution is intentionally not claimed until a real Gateway response and dashboard proof exist.

## Live Demo

GitHub Pages target:

```text
https://daideguchi.github.io/resilient-agentops-gateway/
```

## Demo Media

Current live screenshot:

![Resilient AgentOps Gateway live screenshot](media/resilient-agentops-gateway-pages-full.png)

Current local verification screenshot:

![Resilient AgentOps Gateway verification screenshot](media/resilient-agentops-gateway-full.png)

Demo video status: pending. Do not claim live TrueFoundry Gateway execution in the demo until sanitized response proof and dashboard proof exist.

Current local demo video:

```text
media/resilient-agentops-gateway-demo.mp4
```

Raw demo video URL:

```text
https://raw.githubusercontent.com/daideguchi/resilient-agentops-gateway/main/media/resilient-agentops-gateway-demo.mp4
```

This is a generated narration draft for review. It does not claim live TrueFoundry Gateway execution.

## Verify

```bash
node scripts/verify_gateway.mjs
python3 scripts/verify_no_secrets.py
python3 scripts/verify_readme_review_hub.py
python3 scripts/verify_claim_boundary.py
python3 scripts/verify_demo_video.py
```

Expected:

```text
gateway_verify_ok
track_fit_items=4
policy_items=4
receipt_items=4
contract_items=4
gateway_no_secrets_ok
gateway_readme_review_hub_ok
gateway_claim_boundary_ok
gateway_demo_video_ok
```

## TrueFoundry Status

The product is shaped for the TrueFoundry AI Gateway challenge direction, but no live TrueFoundry Gateway request has been made yet. The next integration step is documented in [docs/TRUEFOUNDRY_INTEGRATION_PLAN.md](docs/TRUEFOUNDRY_INTEGRATION_PLAN.md).

Future live-proof commands:

```bash
python3 scripts/truefoundry_smoke_request.py
python3 scripts/verify_truefoundry_live.py
```

These are expected to fail until a real TrueFoundry API key, virtual model, sanitized response proof, and dashboard screenshot exist.

## Submission Docs

- [Submission package](SUBMISSION_PACKAGE.md)
- [Architecture](ARCHITECTURE.md)
- [TrueFoundry integration plan](docs/TRUEFOUNDRY_INTEGRATION_PLAN.md)
- [Gateway I/O contract](docs/GATEWAY_IO_CONTRACT.md)
- [Devpost draft](submission/devpost-draft.md)
- [Demo script](submission/demo-script.md)
- [Build journey](submission/build-journey.md)

## Claim Boundary

This is a local/public MVP. TrueFoundry Gateway has not been installed or called yet. The UI is shaped for that track, but no live TrueFoundry execution is claimed.
