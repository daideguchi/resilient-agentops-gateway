# TrueFoundry Integration Plan

## Current Status

Live proof is complete.

Resilient AgentOps Gateway now includes a configured TrueFoundry self-hosted model account and one verified OpenAI-compatible Gateway chat-completion response. The product timeline remains a demo scenario, but the Gateway integration proof is real and stored as sanitized artifacts under `media/`.

## What We Know From Public Sources

- TrueFoundry describes AI Gateway as the proxy layer between applications and LLM providers / MCP servers, with governance and observability.
- TrueFoundry virtual models support routing across target models with load balancing, failover, retries, and fallback behavior behind one stable model name.
- TrueFoundry documents priority-based routing, latency-based routing, unhealthy target handling, and dashboard visibility for target traffic.
- TrueFoundry documents API keys as Personal Access Tokens or Virtual Account tokens, passed as bearer tokens.
- TrueFoundry's OpenAI-compatible chat route is `POST /chat/completions` under the Gateway base URL. Hosted control planes can also use a tenant base such as `https://<tenant>.truefoundry.cloud/api/llm`.

Source links:

- https://www.truefoundry.com/docs/gateway
- https://www.truefoundry.com/docs/generating-truefoundry-api-keys
- https://www.truefoundry.com/docs/ai-gateway/chat-completions-overview

## Completed Integration Slot

1. Created a TrueFoundry tenant and configured a self-hosted OpenAI-compatible model account.
2. Routed one small sample chat request through TrueFoundry Gateway.
3. Captured sanitized response metadata at `media/truefoundry-gateway-response.json`.
4. Captured a public-safe dashboard proof at `media/truefoundry-gateway-proof.png`.
5. Updated README, submission package, and the app packet from "not called yet" to the real verified status.

## Smoke Request

```bash
export TRUEFOUNDRY_API_KEY="..."
export TRUEFOUNDRY_MODEL="fireworks-openai-compatible/Vertex-Gemini-Bridge"
export TRUEFOUNDRY_BASE_URL="https://<tenant>.truefoundry.cloud/api/llm"
export TRUEFOUNDRY_ENDPOINT_PATH="/chat/completions"
python3 scripts/truefoundry_smoke_request.py
```

The smoke script writes only sanitized response metadata to `media/truefoundry-gateway-response.json`.

## Live Proof Verifier

```bash
python3 scripts/verify_truefoundry_live.py
```

This verifier is intentionally strict. It passes only when both the sanitized response proof and the real dashboard screenshot exist.
