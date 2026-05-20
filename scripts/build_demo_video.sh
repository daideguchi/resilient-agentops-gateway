#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FONT="/System/Library/Fonts/Supplemental/Arial.ttf"
EDGE_TTS_PYTHON="${EDGE_TTS_PYTHON:-python3.11}"
EDGE_TTS_VOICE="${EDGE_TTS_VOICE:-en-US-AvaNeural}"
EDGE_TTS_RATE="${EDGE_TTS_RATE:--6%}"
OUT="$ROOT/media/resilient-agentops-gateway-demo.mp4"
DRAFT_OUT="$ROOT/media/resilient-agentops-gateway-demo-draft.mp4"
TMP_DIR="$ROOT/media/.demo_video_tmp"

rm -rf "$TMP_DIR"
mkdir -p "$TMP_DIR"

make_text_slide() {
  local title="$1"
  local subtitle="$2"
  local footer="$3"
  local out="$4"

  magick -size 1920x1080 xc:"#f5f7f9" \
    -fill "#17202a" -draw "rectangle 0,0 1920,250" \
    -fill "#225d8d" -draw "rectangle 78,328 1842,358" \
    -fill "#ffffff" -font "$FONT" -pointsize 70 -annotate +82+146 "$title" \
    -fill "#e7f1fa" -font "$FONT" -pointsize 34 -annotate +86+216 "$subtitle" \
    -fill "#ffffff" -stroke "#d8e1ea" -strokewidth 3 -draw "roundrectangle 120,420 1800,760 24,24" \
    -stroke none -fill "#17202a" -font "$FONT" -pointsize 42 -annotate +170+526 "$footer" \
    -fill "#5f6f80" -font "$FONT" -pointsize 28 -annotate +170+650 "A verified public MVP with explicit TrueFoundry proof boundaries." \
    "$out"
}

make_screenshot_slide() {
  local src="$1"
  local title="$2"
  local subtitle="$3"
  local kicker="$4"
  local out="$5"

  magick "$src" \
    -resize 1920x \
    -crop 1920x1080+0+0 +repage \
    -fill "#10202ED9" -draw "rectangle 0,0 1920,164" \
    -fill "#000000CC" -draw "rectangle 0,790 1920,1080" \
    -font "$FONT" -fill "#BFE8FF" -pointsize 30 -annotate +72+64 "$kicker" \
    -font "$FONT" -fill white -pointsize 56 -annotate +72+126 "$title" \
    -font "$FONT" -fill white -pointsize 38 -annotate +72+900 "$subtitle" \
    "$out"
}

cat > "$TMP_DIR/narration.txt" <<'TEXT'
AI agents do not just need better answers. They need an operations layer.

Resilient AgentOps Gateway shows what happened when an agent had to route, fall back, stop, or ask for human approval.

At the top, the operator can see fallbacks used, approvals required, estimated cost, and blocked actions. This is the part that usually disappears inside logs.

The product is built around the TrueFoundry-style gateway story: routing, fallback, governance, and evidence.

The decision contract makes the operating rules explicit: retry, fallback, approval, or stop.

Each timeline row explains which model or tool path was tried, whether fallback was used, what risk was found, and whether human approval was required.

In this example, a risky refund action is blocked. The system does not hide that behind a polished final answer.

The handoff packet and evidence receipts let the next human or future agent resume without guessing. They include fallback count, blocked actions, approvals, cost, decision rules, simulated proof, blocked proof, and the exact claim boundary.

The next step is one real TrueFoundry Gateway smoke request and dashboard proof. Until then, the project keeps the boundary visible and machine-checkable.
TEXT

"$EDGE_TTS_PYTHON" -m edge_tts \
  --voice "$EDGE_TTS_VOICE" \
  --rate="$EDGE_TTS_RATE" \
  --file "$TMP_DIR/narration.txt" \
  --write-media "$TMP_DIR/narration.mp3"

make_text_slide \
  "Resilient AgentOps Gateway" \
  "A review cockpit for resilient AI agents" \
  "When agents fail, recover, or stop, the operator needs evidence." \
  "$TMP_DIR/slide-0.png"

make_screenshot_slide "$ROOT/media/resilient-agentops-gateway-pages-full.png" \
  "Operations Layer" \
  "Fallbacks, approvals, estimated cost, and blocked actions are visible." \
  "1 / 6  Gateway metrics" \
  "$TMP_DIR/slide-1.png"

make_screenshot_slide "$ROOT/media/resilient-agentops-gateway-pages-full.png" \
  "Fit And Decision Contract" \
  "Routing, fallback, approval, and stop rules are visible before risky work happens." \
  "2 / 6  Sponsor fit plus operating rules" \
  "$TMP_DIR/slide-2.png"

make_screenshot_slide "$ROOT/media/resilient-agentops-gateway-pages-full.png" \
  "Explainable Timeline" \
  "Every row shows primary path, fallback path, status, risk, and approval." \
  "3 / 6  Resilient execution" \
  "$TMP_DIR/slide-3.png"

make_screenshot_slide "$ROOT/media/resilient-agentops-gateway-pages-full.png" \
  "Risky Work Stops" \
  "A customer credit action is blocked until a human reviews it." \
  "4 / 6  Governance checkpoint" \
  "$TMP_DIR/slide-4.png"

make_screenshot_slide "$ROOT/media/resilient-agentops-gateway-full.png" \
  "Handoff And Receipts" \
  "The next human or future agent can resume from decision rules and evidence receipts." \
  "5 / 6  Resumable operations" \
  "$TMP_DIR/slide-5.png"

make_text_slide \
  "Honest Submission Boundary" \
  "Public MVP is verified. Live TrueFoundry Gateway proof is still required." \
  "The live verifier should fail until response proof and dashboard proof exist." \
  "$TMP_DIR/slide-6.png"

ffmpeg -y \
  -loop 1 -t 13 -i "$TMP_DIR/slide-0.png" \
  -loop 1 -t 13 -i "$TMP_DIR/slide-1.png" \
  -loop 1 -t 13 -i "$TMP_DIR/slide-2.png" \
  -loop 1 -t 13 -i "$TMP_DIR/slide-3.png" \
  -loop 1 -t 13 -i "$TMP_DIR/slide-4.png" \
  -loop 1 -t 13 -i "$TMP_DIR/slide-5.png" \
  -loop 1 -t 13 -i "$TMP_DIR/slide-6.png" \
  -i "$TMP_DIR/narration.mp3" \
  -filter_complex "[0:v][1:v][2:v][3:v][4:v][5:v][6:v]concat=n=7:v=1:a=0,format=yuv420p[v];[7:a]loudnorm=I=-16:TP=-1.5:LRA=11,volume=0.92[a]" \
  -map "[v]" -map "[a]" -r 30 -c:v libx264 -preset veryfast -crf 23 -c:a aac -b:a 192k -shortest -movflags +faststart "$OUT"

cp "$OUT" "$DRAFT_OUT"
rm -rf "$TMP_DIR"
echo "$OUT"
