# Gateway I/O Contract

Resilient AgentOps Gateway should make every important route decision replayable.

This document defines the minimum request, route decision, response, and audit receipt shape. It is designed to be replaced by live TrueFoundry Gateway proof once a real workspace is available.

## Request

```json
{
  "task_id": "support-refund-1842",
  "task": "Review refund request and draft next operator action",
  "risk_class": "customer-credit-action",
  "budget_limit_usd": 0.1,
  "requires_evidence": true,
  "requires_human_approval": true
}
```

## Route Decision

```json
{
  "primary_model": "fast-model",
  "fallback_model": "reasoning-model",
  "retry_rule": "retry once on timeout or rate limit",
  "fallback_rule": "fallback when evidence is missing or confidence is weak",
  "stop_rule": "block customer-facing or money-moving action until human approval"
}
```

## Response

```json
{
  "status": "blocked",
  "answer_summary": "Refund action requires human approval",
  "fallback_used": true,
  "estimated_cost_usd": 0.067,
  "approvals_required": 2,
  "blocked_actions": ["refund action"]
}
```

## Audit Receipt

```json
{
  "route_receipt": "primary and fallback paths are visible",
  "policy_receipt": "blocked action names the stop rule",
  "cost_receipt": "estimated cost is recorded",
  "proof_boundary": "replace simulated receipt with real TrueFoundry response before claiming live execution"
}
```

## Stoplines

- Do not claim live TrueFoundry execution from this static contract.
- Do not commit a TrueFoundry API key.
- Do not store private customer data in a public receipt.
- Do not remove the human approval gate for customer-facing or money-moving actions.
