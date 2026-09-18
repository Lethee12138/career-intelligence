import json
from pathlib import Path
import unittest


class TestOfficialCareerAdapterRuntime(unittest.TestCase):
    def test_official_source_runtime_boundary(self):
        path = Path(__file__).parent / "fixtures" / "official-runtime-synthetic.json"
        data = json.loads(path.read_text())

        self.assertEqual(data["source"]["source_type"], "official")
        self.assertEqual(data["source"]["authority_level"], "HIGH")
        self.assertEqual(data["job"]["status"], "OPEN_VERIFIED")

    def test_runtime_does_not_make_application_decision(self):
        path = Path(__file__).parent / "fixtures" / "official-runtime-synthetic.json"
        data = json.loads(path.read_text())

        self.assertNotIn("application_decision", data)
        self.assertNotIn("fit_score", data)


if __name__ == "__main__":
    unittest.main()
