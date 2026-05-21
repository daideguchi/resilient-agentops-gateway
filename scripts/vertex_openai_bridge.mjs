#!/usr/bin/env node
import { createServer } from 'node:http';
import { createSign, randomUUID } from 'node:crypto';
import { readFile } from 'node:fs/promises';

const keyPath = process.env.GOOGLE_VERTEX_SERVICE_ACCOUNT_JSON;
const project = process.env.GOOGLE_VERTEX_PROJECT || 'pj260519';
const location = process.env.GOOGLE_VERTEX_LOCATION || 'us-central1';
const vertexModel = process.env.GOOGLE_VERTEX_MODEL || 'gemini-2.5-flash';
const bridgeModelId = process.env.BRIDGE_MODEL_ID || 'vertex-gemini-bridge';
const port = Number(process.env.PORT || process.env.BRIDGE_PORT || 8788);
const authToken = process.env.BRIDGE_AUTH_TOKEN || '';

if (!keyPath) {
  throw new Error('Set GOOGLE_VERTEX_SERVICE_ACCOUNT_JSON to a local service account JSON path.');
}

function base64url(input) {
  return Buffer.from(input)
    .toString('base64')
    .replaceAll('+', '-')
    .replaceAll('/', '_')
    .replaceAll('=', '');
}

function signJwt(serviceAccount) {
  const now = Math.floor(Date.now() / 1000);
  const header = { alg: 'RS256', typ: 'JWT' };
  const claim = {
    iss: serviceAccount.client_email,
    sub: serviceAccount.client_email,
    aud: 'https://oauth2.googleapis.com/token',
    scope: 'https://www.googleapis.com/auth/cloud-platform',
    iat: now,
    exp: now + 3600,
  };
  const unsigned = `${base64url(JSON.stringify(header))}.${base64url(JSON.stringify(claim))}`;
  const signer = createSign('RSA-SHA256');
  signer.update(unsigned);
  signer.end();
  return `${unsigned}.${signer.sign(serviceAccount.private_key, 'base64url')}`;
}

async function getAccessToken(serviceAccount) {
  const body = new URLSearchParams({
    grant_type: 'urn:ietf:params:oauth:grant-type:jwt-bearer',
    assertion: signJwt(serviceAccount),
  });
  const res = await fetch('https://oauth2.googleapis.com/token', {
    method: 'POST',
    headers: { 'content-type': 'application/x-www-form-urlencoded' },
    body,
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok || !data.access_token) {
    throw new Error(`OAuth token exchange failed: HTTP ${res.status} ${data.error || ''}`.trim());
  }
  return data.access_token;
}

function sendJson(res, status, payload) {
  res.writeHead(status, {
    'content-type': 'application/json; charset=utf-8',
    'access-control-allow-origin': '*',
    'access-control-allow-headers': 'authorization, content-type',
    'access-control-allow-methods': 'GET,POST,OPTIONS',
  });
  res.end(`${JSON.stringify(payload)}\n`);
}

async function readJsonBody(req) {
  const chunks = [];
  for await (const chunk of req) chunks.push(chunk);
  const raw = Buffer.concat(chunks).toString('utf8');
  return raw ? JSON.parse(raw) : {};
}

function authorize(req) {
  if (!authToken) return true;
  const header = req.headers.authorization || '';
  return header === `Bearer ${authToken}`;
}

function messagesToPrompt(messages = []) {
  return messages
    .map((message) => `${String(message.role || 'user').toUpperCase()}: ${String(message.content || '')}`)
    .join('\n\n')
    .trim();
}

async function callVertex(serviceAccount, payload) {
  const token = await getAccessToken(serviceAccount);
  const prompt = messagesToPrompt(payload.messages);
  const url = `https://${location}-aiplatform.googleapis.com/v1/projects/${project}/locations/${location}/publishers/google/models/${vertexModel}:generateContent`;
  const res = await fetch(url, {
    method: 'POST',
    headers: {
      authorization: `Bearer ${token}`,
      'content-type': 'application/json',
    },
    body: JSON.stringify({
      contents: [{ role: 'user', parts: [{ text: prompt || 'Return OK.' }] }],
      generationConfig: {
        temperature: Number(payload.temperature ?? 0),
        maxOutputTokens: Math.max(Number(payload.max_tokens ?? 128), 64),
      },
    }),
  });
  const data = await res.json().catch(() => ({}));
  const text = data?.candidates?.[0]?.content?.parts?.map((part) => part.text || '').join('\n').trim() || '';
  if (!res.ok || !text) {
    const message = data?.error?.message || data?.error?.status || 'empty Vertex response';
    throw new Error(`Vertex Gemini call failed: HTTP ${res.status} ${message}`);
  }
  return {
    text,
    usage: data?.usageMetadata || {},
  };
}

const serviceAccount = JSON.parse(await readFile(keyPath, 'utf8'));
if (serviceAccount.project_id !== project) {
  throw new Error(`Service account project mismatch: expected ${project}, got ${serviceAccount.project_id}`);
}

const server = createServer(async (req, res) => {
  try {
    if (req.method === 'OPTIONS') {
      return sendJson(res, 200, { ok: true });
    }
    if (!authorize(req)) {
      return sendJson(res, 401, { error: { message: 'unauthorized', type: 'auth_error' } });
    }
    const url = new URL(req.url || '/', 'http://127.0.0.1');
    if (req.method === 'GET' && (url.pathname === '/health' || url.pathname === '/')) {
      return sendJson(res, 200, { ok: true, model: bridgeModelId, provider: 'vertex_ai' });
    }
    if (req.method === 'GET' && (url.pathname === '/models' || url.pathname === '/v1/models')) {
      return sendJson(res, 200, {
        object: 'list',
        data: [{ id: bridgeModelId, object: 'model', owned_by: 'local-vertex-bridge' }],
      });
    }
    if (req.method === 'POST' && (url.pathname === '/chat/completions' || url.pathname === '/v1/chat/completions')) {
      const payload = await readJsonBody(req);
      const result = await callVertex(serviceAccount, payload);
      return sendJson(res, 200, {
        id: `chatcmpl-${randomUUID()}`,
        object: 'chat.completion',
        created: Math.floor(Date.now() / 1000),
        model: payload.model || bridgeModelId,
        choices: [
          {
            index: 0,
            message: { role: 'assistant', content: result.text },
            finish_reason: 'stop',
          },
        ],
        usage: {
          prompt_tokens: result.usage.promptTokenCount ?? null,
          completion_tokens: result.usage.candidatesTokenCount ?? null,
          total_tokens: result.usage.totalTokenCount ?? null,
        },
      });
    }
    return sendJson(res, 404, { error: { message: `not found: ${url.pathname}`, type: 'not_found' } });
  } catch (error) {
    return sendJson(res, 500, {
      error: {
        message: error instanceof Error ? error.message : String(error),
        type: 'bridge_error',
      },
    });
  }
});

server.listen(port, '127.0.0.1', () => {
  console.log(`vertex_openai_bridge_ready http://127.0.0.1:${port}`);
  console.log(`bridge_model_id=${bridgeModelId}`);
  console.log(`vertex_model=${vertexModel}`);
});
