#!/usr/bin/env python3
"""Verify that real TrueFoundry Gateway proof exists before live claims."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCREENSHOT = ROOT / "media" / "truefoundry-gateway-proof.png"
RESPONSE = ROOT / "media" / "truefoundry-gateway-response.json"
MIN_SCREENSHOT_BYTES = 20_000


def main() -> int:
    failures: list[str] = []

    if not SCREENSHOT.exists():
        failures.append(f"missing dashboard proof: {SCREENSHOT}")
    elif SCREENSHOT.stat().st_size < MIN_SCREENSHOT_BYTES:
        failures.append(f"dashboard proof too small: {SCREENSHOT.stat().st_size}")

    if not RESPONSE.exists():
        failures.append(f"missing sanitized response proof: {RESPONSE}")
    else:
        text = RESPONSE.read_text(encoding="utf-8")
        lowered = text.lower()
        if "authorization" in lowered or "bearer " in lowered or "api_key" in lowered:
            failures.append("response proof appears to contain secret material")
        try:
            data = json.loads(text)
        except json.JSONDecodeError as exc:
            failures.append(f"response proof is not valid JSON: {exc}")
        else:
            if data.get("sanitized") is not True:
                failures.append("response proof must set sanitized=true")
            base_url = data.get("gateway_base_url", "")
            if not (base_url.startswith("https://") and "truefoundry" in base_url):
                failures.append("response proof must use a TrueFoundry HTTPS Gateway base URL")
            if data.get("endpoint_path") not in {
                "/chat/completions",
                "/v1/chat/completions",
                "/api/inference/openai/chat/completions",
            }:
                failures.append("response proof endpoint_path must be a TrueFoundry OpenAI-compatible chat endpoint")
            if not data.get("response_id"):
                failures.append("response proof missing response_id")
            if "TrueFoundry gateway smoke OK" not in str(data.get("first_choice_text", "")):
                failures.append("response proof missing expected smoke response text")

    if failures:
        print("truefoundry_live_proof_missing")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("truefoundry_live_proof_ok")
    print(f"dashboard_proof={SCREENSHOT}")
    print(f"response_proof={RESPONSE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
