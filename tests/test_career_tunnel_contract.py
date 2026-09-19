import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CareerTunnelContractTests(unittest.TestCase):
    def test_career_tunnel_is_separate_from_paw_transport(self):
        script = (ROOT / "scripts/career-mcp-tunnel.sh").read_text()
        self.assertIn("127.0.0.1:8797/mcp", script)
        self.assertNotIn("127.0.0.1:8787/mcp", script)
        self.assertNotIn("tunnel_6a837fad5fcc819196104e74450a22f2", script)
        self.assertIn("CAREER_TUNNEL_ID", script)
        self.assertIn("CAREER_TUNNEL_RUNTIME_KEY_FILE", script)

    def test_runtime_secret_is_external_and_permission_checked(self):
        script = (ROOT / "scripts/career-mcp-tunnel.sh").read_text()
        self.assertIn('file:$RUNTIME_KEY_FILE', script)
        self.assertIn('mode 0600 or 0400', script)
        self.assertNotIn(
            "OpenAI Tunnel/credentials/control-plane-api-key",
            script,
        )

    def test_remote_server_is_loopback_stateless_and_read_only(self):
        server = (ROOT / "mcp/career-mcp-http-server.mjs").read_text()
        self.assertIn('const DEFAULT_HOST = "127.0.0.1"', server)
        self.assertIn('career.scan_and_review', server)
        self.assertIn('readOnlyHint: true', server)
        self.assertIn('stateless: true', server)
        self.assertIn('contextPersistenceWrites: false', server)
        self.assertNotIn("writeFile", server)
        self.assertNotIn("exec(", server)

    def test_tunnel_profile_uses_official_remote_http_sample(self):
        script = (ROOT / "scripts/career-mcp-tunnel.sh").read_text()
        self.assertIn("sample_mcp_remote_no_auth", script)
        self.assertIn("tunnel-client", script)
        self.assertIn("PAW tunnel/config mutation: none", script)


if __name__ == "__main__":
    unittest.main()
