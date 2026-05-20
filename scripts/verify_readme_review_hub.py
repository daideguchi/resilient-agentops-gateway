#!/usr/bin/env python3
"""Verify README works as the public review hub for judges."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

REQUIRED_MARKERS = [
    "# Resilient AgentOps Gateway",
    "Judge Quick Read",
    "Live Demo",
    "Demo Media",
    "Verify",
    "TrueFoundry Status",
    "Submission Docs",
    "Claim Boundary",
    "https://daideguchi.github.io/resilient-agentops-gateway/",
    "https://raw.githubusercontent.com/daideguchi/resilient-agentops-gateway/main/media/resilient-agentops-gateway-demo.mp4",
    "![Resilient AgentOps Gateway live screenshot]",
    "node scripts/verify_gateway.mjs",
    "python3 scripts/verify_no_secrets.py",
    "python3 scripts/verify_claim_boundary.py",
    "python3 scripts/verify_demo_video.py",
    "gateway_no_secrets_ok",
    "contract_items=4",
    "Gateway I/O contract",
    "no live TrueFoundry Gateway request has been made yet",
]


def main() -> int:
    text = README.read_text(encoding="utf-8")
    missing = [marker for marker in REQUIRED_MARKERS if marker not in text]
    if missing:
        print("gateway_readme_review_hub_failed", file=sys.stderr)
        for marker in missing:
            print(f"- missing: {marker}", file=sys.stderr)
        return 1

    print("gateway_readme_review_hub_ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
