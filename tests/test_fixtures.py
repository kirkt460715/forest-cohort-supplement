import csv
import json
import unittest
from pathlib import Path


DATA = Path(__file__).resolve().parents[1] / "data"


class FixtureContractTests(unittest.TestCase):
    def test_declared_sources_have_headers_and_records(self):
        manifest = json.loads((DATA / "manifest.json").read_text(encoding="utf-8"))
        for filename, columns in manifest["sources"].items():
            with self.subTest(source=filename):
                with (DATA / filename).open(encoding="utf-8", newline="") as source:
                    reader = csv.DictReader(source)
                    self.assertEqual(reader.fieldnames, columns)
                    rows = list(reader)
                    self.assertTrue(rows)
                    for row in rows:
                        self.assertNotIn(None, row)
                        self.assertNotIn(None, row.values())

    def records(self, filename):
        with (DATA / filename).open(encoding="utf-8", newline="") as source:
            return list(csv.DictReader(source))

    def test_positions_have_declared_frames_and_previous_positions(self):
        positions = self.records("positions.csv")
        ids = {row["position_id"] for row in positions}
        self.assertLessEqual({row["frame_id"] for row in positions}, {row["frame_id"] for row in self.records("sample_frames.csv")})
        self.assertLessEqual({key for row in positions for key in row["prior_position"].split("|") if key}, ids)
        self.assertTrue(any(row["observed_state"] == "替补存活" for row in positions))
        self.assertTrue(any("|" in row["prior_position"] for row in positions))


if __name__ == "__main__":
    unittest.main()
