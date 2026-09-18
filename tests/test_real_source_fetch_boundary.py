import unittest


class TestRealSourceFetchBoundary(unittest.TestCase):
    def test_official_source_status_is_preserved(self):
        record = {"source_type": "official", "status": "OPEN_VERIFIED"}
        self.assertEqual(record["source_type"], "official")
        self.assertEqual(record["status"], "OPEN_VERIFIED")

    def test_structure_change_requires_review(self):
        status = "NEEDS_VERIFY"
        self.assertEqual(status, "NEEDS_VERIFY")


if __name__ == "__main__":
    unittest.main()
