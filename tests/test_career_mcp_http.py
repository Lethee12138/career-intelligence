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
        self.assertTrue(value["stateless"])
        self.assertFalse(value["persistence"])
        self.assertFalse(value["application"])
        self.assertFalse(value["canonicalWrite"])

    def test_scan_tool_composes_core_without_network_for_empty_source_set(self):
        response = _mcp_post(
            self.port,
            {
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {
                    "name": "career.scan_and_review",
                    "arguments": {
                        "scanConfig": {
                            "scan_id": "mcp-empty",
                            "sources": [],
                        },
                        "careerContext": {
                            "candidate_context": {
                                "new_ssot": False,
                                "as_of": "2026-09-19",
                            }
                        },
                        "detailLevel": "summary",
                    },
                },
            },
        )
        value = response["result"]["structuredContent"]
        self.assertEqual(value["scan_id"], "mcp-empty")
        self.assertEqual(value["raw_record_count"], 0)
        self.assertEqual(value["review_packet_count"], 0)
        self.assertFalse(value["external_action"])
        self.assertTrue(value["human_review_required"])


if __name__ == "__main__":
    unittest.main()
