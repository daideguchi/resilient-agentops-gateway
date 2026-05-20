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
- TrueFoundry challenge-fit summary

## How We Built It

The current MVP is a static, deterministic gateway cockpit deployed on GitHub Pages. It includes a sample event model, a fallback timeline, a handoff packet, public screenshots, Playwright verification, and strict claim-boundary scripts.

## Links

- Live demo: https://daideguchi.github.io/resilient-agentops-gateway/
- GitHub: https://github.com/daideguchi/resilient-agentops-gateway
- Submission package: https://raw.githubusercontent.com/daideguchi/resilient-agentops-gateway/main/SUBMISSION_PACKAGE.md
- Screenshot: https://raw.githubusercontent.com/daideguchi/resilient-agentops-gateway/main/media/resilient-agentops-gateway-pages-full.png
- Demo video draft: https://raw.githubusercontent.com/daideguchi/resilient-agentops-gateway/main/media/resilient-agentops-gateway-demo.mp4

## Built With

HTML, CSS, JavaScript, Playwright, GitHub Pages, Python verification scripts

## What Is Still Needed Before Final Submission

- Create or access a real TrueFoundry AI Gateway workspace.
- Route one safe smoke request through the Gateway.
- Save sanitized response proof.
- Capture dashboard proof.
- Listen to and approve the generated demo video draft, then upload the final public video if Devpost requires a hosted player.
- DD must approve legal terms and final submission.

## Claim Boundary

TrueFoundry Gateway has not been installed or called yet. The project includes scripts that should fail until real Gateway proof exists.
