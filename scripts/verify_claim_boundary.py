#!/usr/bin/env python3
"""Fail if the repo claims live TrueFoundry proof before proof exists."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROOF_FILE = ROOT / "media" / "truefoundry-gateway-proof.png"
TEXT_FILES = [
    ROOT / "README.md",
    ROOT / "SUBMISSION_PACKAGE.md",
    ROOT / "ARCHITECTURE.md",
    ROOT / "docs" / "TRUEFOUNDRY_INTEGRATION_PLAN.md",
    ROOT / "index.html",
]

UNSAFE_PHRASES = [
    "truefoundry gateway has been installed",
    "truefoundry gateway is installed",
    "truefoundry gateway execution verified",
    "live truefoundry execution verified",
    "truefoundry live call verified",
    "truefoundry gateway call verified",
    "truefoundry gateway proof complete",
    "prize eligibility complete",
]


def main() -> int:
    combined = "\n".join(path.read_text(encoding="utf-8").lower() for path in TEXT_FILES if path.exists())
    if not PROOF_FILE.exists():
        for phrase in UNSAFE_PHRASES:
            if phrase in combined:
                print("gateway_claim_boundary_failed")
                print(f"unsafe_phrase={phrase}")
                print(f"missing_proof={PROOF_FILE}")
                return 1
    print("gateway_claim_boundary_ok")
    print(f"truefoundry_proof_file_exists={PROOF_FILE.exists()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
