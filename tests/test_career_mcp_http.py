import json
import os
import shutil
import socket
import subprocess
import time
import unittest
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
SERVER = ROOT / "mcp/career-mcp-http-server.mjs"
DEFAULT_REQUIRE_BASE = (
    Path.home() / "Personal AI Workspace/app/package.json"
)


def _free_port():
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def _mcp_post(port, payload):
    request = Request(
        f"http://127.0.0.1:{port}/mcp",
        data=json.dumps(payload).encode(),
        headers={
            "content-type": "application/json",
            "accept": "application/json, text/event-stream",
        },
        method="POST",
    )
    with urlopen(request, timeout=20) as response:
        raw = response.read().decode()
    lines = [line[6:] for line in raw.splitlines() if line.startswith("data: ")]
    return json.loads(lines[-1] if lines else raw)


@unittest.skipUnless(
    shutil.which("node") and DEFAULT_REQUIRE_BASE.exists(),
    "requires Node and an already-installed official MCP SDK dependency base",
)
class CareerMcpHttpTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.port = _free_port()
        env = os.environ.copy()
        env["CAREER_MCP_HTTP_PORT"] = str(cls.port)
        env["CAREER_MCP_REQUIRE_BASE"] = str(DEFAULT_REQUIRE_BASE)
        cls.process = subprocess.Popen(
            ["node", str(SERVER)],
            cwd=ROOT,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        deadline = time.time() + 10
        while time.time() < deadline:
            try:
                with urlopen(
                    f"http://127.0.0.1:{cls.port}/healthz", timeout=1
                ) as response:
                    if json.loads(response.read())["ok"]:
                        return
            except Exception:
                time.sleep(0.1)
        raise RuntimeError("career MCP server did not become healthy")

    @classmethod
    def tearDownClass(cls):
        cls.process.terminate()
        try:
            cls.process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            cls.process.kill()

    def test_tools_list_exposes_only_bounded_read_tools(self):
        response = _mcp_post(
            self.port,
            {"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}},
        )
        tools = response["result"]["tools"]
        names = [tool["name"] for tool in tools]
        self.assertEqual(
            names, ["career.server_info", "career.scan_and_review"]
        )
        for tool in tools:
            self.assertTrue(tool["annotations"]["readOnlyHint"])
            self.assertFalse(tool["annotations"]["destructiveHint"])
            self.assertIn("outputSchema", tool)

        scan_tool = next(tool for tool in tools if tool["name"] == "career.scan_and_review")
        properties = scan_tool["inputSchema"]["properties"]
        self.assertNotIn("scanConfig", properties)
        self.assertNotIn("useConfiguredSources", properties)
        self.assertNotIn("useCurrentCareerContext", properties)
        self.assertIn("poolMode", properties)
        self.assertIn("careerContext", properties)
        self.assertIn("mode", properties)
        self.assertIn("discovery", properties)
        pool_schema = properties["poolMode"]
        self.assertEqual(set(pool_schema["enum"]), {"BROAD", "FOCUSED"})
        mode_schema = properties["mode"]
        self.assertEqual(
            set(mode_schema["enum"]),
            {"configured_review", "market_discovery", "hybrid_discovery"},
        )

    def test_server_info_is_stateless_and_non_persistent(self):
        response = _mcp_post(
            self.port,
            {
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/call",
                "params": {
                    "name": "career.server_info",
                    "arguments": {},
                },
            },
        )
        value = response["result"]["structuredContent"]
        self.assertEqual(value["version"], "0.2.8")
        self.assertTrue(value["stateless"])
        self.assertEqual(value["contextProvider"], "CURRENT_LOCAL_CONTEXT")
        self.assertFalse(value["contextPersistenceWrites"])
        self.assertFalse(value["application"])
        self.assertFalse(value["canonicalWrite"])

    def test_market_discovery_mode_uses_search_execution_handoff(self):
        response = _mcp_post(
            self.port,
            {
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {
                    "name": "career.scan_and_review",
                    "arguments": {
                        "mode": "market_discovery",
                        "detailLevel": "review",
                        "discovery": {
                            "capabilityProfile": {"profile_ref": "SYNTHETIC-PROFILE"},
                            "roleHypotheses": [{
                                "id": "H1",
                                "role_or_family": "Product / Digital Product",
                                "capability_root_refs": ["cap-product"],
                                "search_terms": {
                                    "China": {"title": [{"term": "Product Manager", "why": "family variant"}]},
                                    "UK": {"title": [{"term": "Product Manager", "why": "family variant"}]},
                                    "Other": {"title": [{"term": "Product Manager", "why": "family variant"}]},
                                },
                            }],
                            "candidates": [{
                                "company": "Synthetic Discovery Co",
                                "external_job_id": "DISC-1",
                                "role": "Product Manager",
                                "location": ["Hangzhou"],
                                "role_family": "Product / Digital Product",
                                "ai_involvement": "NONE",
                                "evidence_refs": ["SYN-E1"],
                            }],
                        },
                    },
                },
            },
        )
        value = response["result"]["structuredContent"]
        self.assertEqual(value["mode"], "market_discovery")
        self.assertEqual(value["scan_config_source"], "DISCOVERY_INPUT")
        self.assertEqual(value["discovery"]["handoff_schema_version"], "0.2.4")
        self.assertEqual(value["pool_view"]["candidates"][0]["role_family"], "Product / Digital Product")
        self.assertEqual(value["pool_view"]["candidates"][0]["next_action"], "VERIFY_OFFICIAL_SOURCE")


if __name__ == "__main__":
    unittest.main()
