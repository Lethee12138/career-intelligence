import json
import unittest
from pathlib import Path


class OfficialRuntimeConnectorTests(unittest.TestCase):
    def test_connector_sources_keep_verification_boundary(self):
        fixture = Path(__file__).parent / "fixtures" / "official-runtime-connectors-synthetic.json"
        data = json.loads(fixture.read_text())
        self.assertEqual(data["sources"][0]["status"], "OPEN_VERIFIED")
        self.assertEqual(data[1 if False else "sources"][1]["status"], "NEEDS_VERIFY")
        self.assertEqual(data["sources"][2]["status"], "NEEDS_VERIFY")


if __name__ == "__main__":
    unittest.main()
