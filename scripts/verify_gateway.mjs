import fs from 'node:fs';
import path from 'node:path';
import { chromium } from 'playwright';

const chromePath = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const root = path.resolve('.');
const outDir = path.join(root, 'media');
fs.mkdirSync(outDir, { recursive: true });

const browser = await chromium.launch({ headless: true, executablePath: chromePath });

try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 950 } });
  await page.goto(`file://${path.join(root, 'index.html')}`, { waitUntil: 'networkidle' });
  const h1 = await page.locator('h1').innerText();
  if (h1 !== 'Resilient AgentOps Gateway') {
    throw new Error(`unexpected h1: ${h1}`);
  }
  const fallbackRows = await page.locator('text=fallback_used').count();
  if (fallbackRows < 2) {
    throw new Error(`fallback rows missing: ${fallbackRows}`);
  }
  const fitItems = await page.locator('.fit-item').count();
  if (fitItems < 4) {
    throw new Error(`track fit items missing: ${fitItems}`);
  }
  const packet = JSON.parse(await page.locator('#packet').innerText());
  if (packet.claim_boundary !== 'No live TrueFoundry Gateway execution is claimed yet.') {
    throw new Error('claim boundary mismatch');
  }
  if (!Array.isArray(packet.track_fit) || packet.track_fit.length < 4) {
    throw new Error('track fit packet missing');
  }
  await page.screenshot({ path: path.join(outDir, 'resilient-agentops-gateway-full.png'), fullPage: true });
  const bytes = fs.statSync(path.join(outDir, 'resilient-agentops-gateway-full.png')).size;
  if (bytes < 80_000) {
    throw new Error(`screenshot too small: ${bytes}`);
  }
  console.log('gateway_verify_ok');
  console.log(`fallback_rows=${fallbackRows}`);
  console.log(`track_fit_items=${fitItems}`);
  console.log(`bytes=${bytes}`);
} finally {
  await browser.close();
}
