import { spawn } from "node:child_process";
import { createServer } from "node:http";
import { createRequire } from "node:module";
import { existsSync } from "node:fs";
import { homedir } from "node:os";
import { dirname, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const THIS_FILE = fileURLToPath(import.meta.url);
const REPOSITORY_ROOT = resolve(dirname(THIS_FILE), "..");
const DEFAULT_HOST = "127.0.0.1";
const DEFAULT_PORT = 8797;
const MAX_INPUT_BYTES = 512_000;
const MAX_OUTPUT_BYTES = 8_000_000;
const TOOL_TIMEOUT_MS = 120_000;

const dependencyBases = [
  process.env.CAREER_MCP_REQUIRE_BASE,
  resolve(REPOSITORY_ROOT, "package.json"),
  resolve(homedir(), "Personal AI Workspace/app/package.json"),
].filter(Boolean);

const loadRuntimeDependency = (name) => {
  for (const base of dependencyBases) {
    if (!existsSync(base)) continue;
    try {
      const require = createRequire(base);
      return require(name);
    } catch {
      // Try the next already-installed dependency base.
    }
  }
  throw new Error(
    `missing-runtime-dependency:${name}; set CAREER_MCP_REQUIRE_BASE to a package.json with the official MCP SDK installed`,
  );
};

const { McpServer, createMcpHandler } = loadRuntimeDependency("@modelcontextprotocol/server");
const { z } = loadRuntimeDependency("zod");
const asToolResult = (value) => ({
  content: [{ type: "text", text: JSON.stringify(value) }],
  structuredContent: value,
});

const asToolError = (reason, detail = undefined) => ({
  isError: true,
  content: [{
    type: "text",
    text: JSON.stringify({ ok: false, reason, ...(detail ? { detail } : {}) }),
  }],
});

const runCareerScan = ({ scanConfig, careerContext }) => new Promise((resolvePromise, rejectPromise) => {
  const payload = JSON.stringify({ scanConfig, careerContext });
  if (Buffer.byteLength(payload, "utf8") > MAX_INPUT_BYTES) {
    rejectPromise(new Error("input-too-large"));
    return;
  }

  const python = [
    "import json,sys",
    "from scripts.career_scan import run_scan_review",
    "p=json.load(sys.stdin)",
    "r=run_scan_review(p['scanConfig'],p['careerContext'])",
    "print(json.dumps(r,ensure_ascii=False))",
  ].join(";");

  const child = spawn("python3", ["-c", python], {
    cwd: REPOSITORY_ROOT,
    stdio: ["pipe", "pipe", "pipe"],
  });
  const stdout = [];
  const stderr = [];
  let outputBytes = 0;
  let settled = false;
  const timer = setTimeout(() => {
    if (settled) return;
    child.kill("SIGTERM");
    settled = true;
    rejectPromise(new Error("scan-timeout"));
  }, TOOL_TIMEOUT_MS);

  child.stdout.on("data", (chunk) => {
    outputBytes += chunk.length;
    if (outputBytes > MAX_OUTPUT_BYTES) {
      child.kill("SIGTERM");
      return;
    }
    stdout.push(Buffer.from(chunk));
  });
  child.stderr.on("data", (chunk) => stderr.push(Buffer.from(chunk)));
  child.on("error", (error) => {
    if (settled) return;
    settled = true;
    clearTimeout(timer);
    rejectPromise(error);
  });
  child.on("close", (code) => {
    if (settled) return;
    settled = true;
    clearTimeout(timer);
    if (outputBytes > MAX_OUTPUT_BYTES) {
      rejectPromise(new Error("output-too-large"));
      return;
    }
    if (code !== 0) {
      const message = Buffer.concat(stderr).toString("utf8").trim();
      rejectPromise(new Error(message || `scan-exit-${code}`));
      return;
    }
    try {
      resolvePromise(JSON.parse(Buffer.concat(stdout).toString("utf8")));
    } catch {
      rejectPromise(new Error("invalid-scan-json"));
    }
  });
  child.stdin.end(payload);
});

const trimResult = (result, detailLevel) => {
  if (detailLevel === "summary") return result.summary;
  if (detailLevel === "review") {
    return {
      summary: result.summary,
      review: result.review,
      boundary: result.boundary,
    };
  }
  return result;
};
export const createCareerMcpServer = () => {
  const server = new McpServer(
    { name: "career-intelligence-remote", version: "0.2.5" },
    {
      instructions:
        "Read-only Career Intelligence job scanning. Use career.scan_and_review for bounded public vacancy scanning and exact-role review packets. Never treat triage as final Fit or submission authority. The server is stateless and does not persist Career context.",
      cacheHints: { "tools/list": { ttlMs: 60_000, cacheScope: "private" } },
    },
  );

  server.registerTool(
    "career.server_info",
    {
      title: "Get Career Intelligence server capabilities",
      description:
        "Return read-only runtime boundaries and supported official source adapters. No personal Career context is read or stored.",
      inputSchema: z.object({}),
      annotations: {
        readOnlyHint: true,
        destructiveHint: false,
        idempotentHint: true,
        openWorldHint: false,
      },
    },
    async () => asToolResult({
      service: "career-intelligence-remote",
      version: "0.2.5",
      stateless: true,
      persistence: false,
      supportedAdapters: {
        sap: "discovery-and-detail",
        tencent: "detail",
        kuaishou: "social-discovery-and-detail",
      },
      externalAction: false,
      application: false,
      canonicalWrite: false,
    }),
  );
  server.registerTool(
    "career.scan_and_review",
    {
      title: "Scan public jobs and create Career review packets",
      description:
        "Run one bounded read-only scan cycle: official public discovery/verification, dedupe, transparent triage, exact-role continuity and qualification/source gates. Personal context is request-scoped and never persisted. This tool does not apply, log in, upload, edit CV/Portfolio, or write Career canonical state.",
      inputSchema: z.object({
        scanConfig: z.record(z.string(), z.unknown()),
        careerContext: z.record(z.string(), z.unknown()),
        detailLevel: z.enum(["summary", "review", "full"]).default("review"),
      }),
      annotations: {
        readOnlyHint: true,
        destructiveHint: false,
        idempotentHint: true,
        openWorldHint: true,
      },
    },
    async ({ scanConfig, careerContext, detailLevel }) => {
      try {
        const result = await runCareerScan({ scanConfig, careerContext });
        return asToolResult(trimResult(result, detailLevel));
      } catch (error) {
        return asToolError(
          "scan-failed",
          error instanceof Error ? error.message : "unknown-error",
        );
      }
    },
  );

  return server;
};

const handler = createMcpHandler(
  () => createCareerMcpServer(),
  { legacy: "stateless", responseMode: "auto" },
);
const nodeRequestToWebRequest = async (request, host) => {
  const chunks = [];
  for await (const chunk of request) chunks.push(Buffer.from(chunk));
  const body = Buffer.concat(chunks);
  const headers = new Headers();
  for (const [name, value] of Object.entries(request.headers)) {
    if (value !== undefined) {
      headers.set(name, Array.isArray(value) ? value.join(", ") : value);
    }
  }
  return new Request(`http://${host}${request.url}`, {
    method: request.method,
    headers,
    body: body.length > 0 && request.method !== "GET" && request.method !== "HEAD"
      ? body
      : undefined,
    duplex: "half",
  });
};

const writeWebResponse = async (response, nodeResponse) => {
  nodeResponse.statusCode = response.status;
  response.headers.forEach((value, key) => nodeResponse.setHeader(key, value));
  if (!response.body) {
    nodeResponse.end();
    return;
  }
  const reader = response.body.getReader();
  try {
    while (true) {
      const next = await reader.read();
      if (next.done) break;
      nodeResponse.write(Buffer.from(next.value));
    }
  } finally {
    reader.releaseLock();
    nodeResponse.end();
  }
};
export const startCareerMcpHttpServer = async ({
  host = process.env.CAREER_MCP_HTTP_HOST ?? DEFAULT_HOST,
  port = Number(process.env.CAREER_MCP_HTTP_PORT ?? DEFAULT_PORT),
} = {}) => {
  if (host !== "127.0.0.1") throw new Error("career-mcp-must-bind-loopback");
  const httpServer = createServer(async (request, response) => {
    try {
      const url = new URL(request.url, `http://${request.headers.host ?? `${host}:${port}`}`);
      if (url.pathname === "/healthz") {
        response.writeHead(200, { "content-type": "application/json; charset=utf-8" });
        response.end(JSON.stringify({
          ok: true,
          service: "career-intelligence-remote",
          version: "0.2.5",
          stateless: true,
        }));
        return;
      }
      if (url.pathname !== "/mcp") {
        response.writeHead(404, { "content-type": "application/json; charset=utf-8" });
        response.end(JSON.stringify({ error: "not-found" }));
        return;
      }
      const requestHost = typeof request.headers.host === "string"
        ? request.headers.host
        : `${host}:${port}`;
      const webRequest = await nodeRequestToWebRequest(request, requestHost);
      await writeWebResponse(await handler.fetch(webRequest), response);
    } catch (error) {
      response.writeHead(500, { "content-type": "application/json; charset=utf-8" });
      response.end(JSON.stringify({
        error: "internal-error",
        detail: error instanceof Error ? error.message : "unknown-error",
      }));
    }
  });

  await new Promise((resolvePromise, rejectPromise) => {
    httpServer.once("error", rejectPromise);
    httpServer.listen(port, host, resolvePromise);
  });
  const address = httpServer.address();
  return {
    server: httpServer,
    host,
    port: typeof address === "object" && address ? address.port : port,
  };
};

const isEntrypoint = process.argv[1] && pathToFileURL(process.argv[1]).href === import.meta.url;
if (isEntrypoint) {
  startCareerMcpHttpServer().then(({ host, port }) => {
    console.error(`[career-mcp] listening on http://${host}:${port}/mcp`);
  }).catch((error) => {
    console.error(`[career-mcp] startup failed: ${error instanceof Error ? error.message : error}`);
    process.exitCode = 1;
  });
}
