#!/usr/bin/env python3
"""Fail if obvious provider secrets are committed to the public repo."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "node_modules", "media"}
TEXT_SUFFIXES = {".html", ".js", ".mjs", ".py", ".md", ".json", ".css", ".txt", ".yml", ".yaml"}

PATTERNS = [
    ("private_key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |)?PRIVATE KEY-----")),
    ("google_api_key", re.compile(r"\bAIza[0-9A-Za-z_-]{20,}\b")),
    ("openai_key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("fireworks_key", re.compile(r"\bfw_[A-Za-z0-9_-]{20,}\b")),
    (
        "truefoundry_api_key_assignment",
        re.compile(r"TRUEFOUNDRY_API_KEY\s*=\s*(?!real_key\b|your_key\b|placeholder\b)[\"']?[A-Za-z0-9_-]{20,}"),
    ),
]


def should_scan(path: Path) -> bool:
    if any(part in SKIP_DIRS for part in path.parts):
        return False
    return path.suffix in TEXT_SUFFIXES


def main() -> int:
    failures: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or not should_scan(path.relative_to(ROOT)):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for name, pattern in PATTERNS:
            if pattern.search(text):
                failures.append(f"{path.relative_to(ROOT)}: {name}")

    if failures:
        print("gateway_no_secrets_failed", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("gateway_no_secrets_ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
