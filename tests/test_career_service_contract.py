import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CareerServiceContractTests(unittest.TestCase):
    def test_launchagent_is_separate_and_loopback_bound(self):
        script = (ROOT / "scripts/career-mcp-service.sh").read_text()
        self.assertIn('LABEL="com.career-intelligence.mcp"', script)
        self.assertIn("127.0.0.1:8797", script)
        self.assertNotIn("com.personal-ai-workspace.mcp", script)
        self.assertNotIn("127.0.0.1:8787", script)

    def test_service_uses_repository_server_and_health_gate(self):
        script = (ROOT / "scripts/career-mcp-service.sh").read_text()
        self.assertIn("mcp/career-mcp-http-server.mjs", script)
        self.assertIn("wait_healthy", script)
        self.assertIn("RunAtLoad", script)
        self.assertIn("KeepAlive", script)

    def test_service_has_bounded_lifecycle_commands(self):
        script = (ROOT / "scripts/career-mcp-service.sh").read_text()
        for command in (
            "install",
            "start",
            "stop",
            "restart",
            "status",
            "uninstall",
        ):
            self.assertIn(command, script)


if __name__ == "__main__":
    unittest.main()
