# Devpost Draft — Resilient AgentOps Gateway

## Project Name

Resilient AgentOps Gateway

## Elevator Pitch

A gateway cockpit for resilient AI agents, showing model fallback, cost, risk, approval, evidence, and handoff instead of hiding recovery behavior inside logs.

## Inspiration

Many agent demos only show the final answer. In production, the hard part is what happened before the final answer: which model path was tried, why fallback was used, what risk was detected, and where a human had to approve or stop the workflow.

## What It Does

Resilient AgentOps Gateway turns agent execution into a reviewable operations surface:

- route decision
- fallback path
- risk reason
- estimated cost
- human approval checkpoint
- evidence reference
- final handoff packet
- decision contract for retry, fallback, approval, and stop rules
- Gateway I/O contract for request, route decision, response, and audit receipt
- evidence receipts that show what is simulated and which live proof is attached
- TrueFoundry challenge-fit summary

## How We Built It

The MVP is a deterministic gateway cockpit deployed on GitHub Pages. It includes a sample event model, a fallback timeline, a handoff packet, a decision contract, a Gateway I/O contract, evidence receipts, public screenshots, Playwright verification, strict claim-boundary scripts, and a sanitized live TrueFoundry Gateway smoke response.

## Links

- Live demo: https://daideguchi.github.io/resilient-agentops-gateway/
- GitHub: https://github.com/daideguchi/resilient-agentops-gateway
- Submission package: https://raw.githubusercontent.com/daideguchi/resilient-agentops-gateway/main/SUBMISSION_PACKAGE.md
- Screenshot: https://raw.githubusercontent.com/daideguchi/resilient-agentops-gateway/main/media/resilient-agentops-gateway-pages-full.png
- TrueFoundry proof screenshot: https://raw.githubusercontent.com/daideguchi/resilient-agentops-gateway/main/media/truefoundry-gateway-proof.png
- Sanitized Gateway response: https://raw.githubusercontent.com/daideguchi/resilient-agentops-gateway/main/media/truefoundry-gateway-response.json
- Demo video draft: https://raw.githubusercontent.com/daideguchi/resilient-agentops-gateway/main/media/resilient-agentops-gateway-demo.mp4

## Built With

HTML, CSS, JavaScript, Playwright, GitHub Pages, Python verification scripts, Gateway I/O contract, TrueFoundry AI Gateway

## What Is Still Needed Before Final Submission

- Listen to and approve the generated demo video draft, then upload the final public video if Devpost requires a hosted player.
- The project lead must approve legal terms and final submission.

## Claim Boundary

The demo timeline is a product scenario. The live integration claim is narrower: one TrueFoundry Gateway chat-completion request succeeded and is stored as sanitized response metadata plus dashboard proof.
