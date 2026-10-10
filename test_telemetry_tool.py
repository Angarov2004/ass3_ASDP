import csv
import tempfile
import unittest
from pathlib import Path
from telemetry_tool import load_records, summarize

class TelemetryToolTests(unittest.TestCase):
    def test_summarize_numeric_fields(self):
        data = [
            {"latency_ms": 10.0, "throughput_eps": 100.0},
            {"latency_ms": 20.0, "throughput_eps": 200.0},
        ]
        result = summarize(data)
        self.assertEqual(result["record_count"], 2)
        self.assertEqual(result["metrics"]["latency_ms"]["mean"], 15.0)
        self.assertEqual(result["metrics"]["throughput_eps"]["max"], 200.0)

    def test_load_csv(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.csv"
            path.write_text("latency_ms,throughput_eps\n12.5,90\n15.5,110\n", encoding="utf-8")
            records = load_records(path)
            self.assertEqual(len(records), 2)
            self.assertEqual(records[0]["latency_ms"], 12.5)

    def test_invalid_number_has_row_context(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.csv"
            path.write_text("latency_ms\nslow\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "row 2"):
                load_records(path)

if __name__ == "__main__":
    unittest.main()
