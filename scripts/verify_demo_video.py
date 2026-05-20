#!/usr/bin/env python3
"""Verify the Gateway demo video has usable video and audio streams."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VIDEO = ROOT / "media" / "resilient-agentops-gateway-demo.mp4"


def main() -> int:
    if not VIDEO.exists():
        print(f"gateway_demo_video_missing={VIDEO}")
        return 1

    probe = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration,size",
            "-show_entries",
            "stream=index,codec_type,codec_name,width,height,duration",
            "-of",
            "json",
            str(VIDEO),
        ],
        text=True,
    )
    data = json.loads(probe)
    streams = data.get("streams", [])
    video_streams = [stream for stream in streams if stream.get("codec_type") == "video"]
    audio_streams = [stream for stream in streams if stream.get("codec_type") == "audio"]
    duration = float(data["format"]["duration"])
    size = int(data["format"]["size"])

    failures: list[str] = []
    if not video_streams:
        failures.append("missing video stream")
    if not audio_streams:
        failures.append("missing audio stream")
    if not (60 <= duration <= 150):
        failures.append(f"unexpected duration: {duration}")
    if size < 1_000_000:
        failures.append(f"video too small: {size}")
    if video_streams:
        video = video_streams[0]
        if video.get("width") != 1920 or video.get("height") != 1080:
            failures.append(f"unexpected resolution: {video.get('width')}x{video.get('height')}")

    if failures:
        print("gateway_demo_video_failed")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("gateway_demo_video_ok")
    print(f"duration={duration:.1f}")
    print(f"size={size}")
    print(f"video={video_streams[0]['codec_name']} 1920x1080")
    print(f"audio={audio_streams[0]['codec_name']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
