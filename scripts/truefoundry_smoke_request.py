#!/usr/bin/env python3
"""Run one safe TrueFoundry AI Gateway smoke request and save sanitized proof."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "media" / "truefoundry-gateway-response.json"


def env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise SystemExit(f"missing required env: {name}")
    return value


def main() -> int:
    api_key = env("TRUEFOUNDRY_API_KEY")
    model = env("TRUEFOUNDRY_MODEL")
    base_url = os.environ.get("TRUEFOUNDRY_BASE_URL", "https://gateway.truefoundry.ai").rstrip("/")
    endpoint_path = os.environ.get("TRUEFOUNDRY_ENDPOINT_PATH", "/chat/completions").strip()
    if not endpoint_path.startswith("/"):
        endpoint_path = f"/{endpoint_path}"
    endpoint = f"{base_url}{endpoint_path}"

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are verifying a hackathon gateway smoke test. Reply briefly.",
            },
            {
                "role": "user",
                "content": "Return exactly: TrueFoundry gateway smoke OK",
            },
        ],
        "temperature": 0,
        "max_tokens": 32,
    }
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "resilient-agentops-gateway-proof/1.0",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            body = response.read().decode("utf-8", errors="replace")
            status = response.status
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print("truefoundry_smoke_failed")
        print(f"status={exc.code}")
        print(body[:800])
        return 1

    parsed = json.loads(body)
    sanitized = {
        "sanitized": True,
        "claim_boundary": "live_truefoundry_gateway_execution_response_captured_dashboard_screenshot_still_required",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "gateway_base_url": base_url,
        "endpoint_path": endpoint_path,
        "model": model,
        "status": status,
        "response_id": parsed.get("id"),
        "object": parsed.get("object"),
        "created": parsed.get("created"),
        "usage": parsed.get("usage"),
        "first_choice_finish_reason": (parsed.get("choices") or [{}])[0].get("finish_reason"),
        "first_choice_text": ((parsed.get("choices") or [{}])[0].get("message") or {}).get("content"),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(sanitized, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("truefoundry_smoke_ok")
    print(f"proof_response={OUT}")
    print("dashboard_screenshot_still_required=media/truefoundry-gateway-proof.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
