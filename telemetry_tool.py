"""Small scientific utility for summarizing network telemetry CSV files."""
from __future__ import annotations
import argparse
import csv
import json
import statistics
from pathlib import Path
from typing import Any

NUMERIC_FIELDS = ("latency_ms", "throughput_eps", "cpu_percent", "memory_mb")

def load_records(path: str | Path) -> list[dict[str, Any]]:
    """Read telemetry records from a CSV file and coerce known metrics to floats."""
    records: list[dict[str, Any]] = []
    with open(path, "r", newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames:
            raise ValueError("CSV file must contain a header row")
        for row_number, row in enumerate(reader, start=2):
            item: dict[str, Any] = dict(row)
            for field in NUMERIC_FIELDS:
                raw = row.get(field, "")
                if raw not in (None, ""):
                    try:
                        item[field] = float(raw)
                    except ValueError as exc:
                        raise ValueError(f"Invalid number in {field} at row {row_number}: {raw}") from exc
            records.append(item)
    return records

def summarize(records: list[dict[str, Any]]) -> dict[str, Any]:
    """Return record count and descriptive statistics for available numeric metrics."""
    result: dict[str, Any] = {"record_count": len(records), "metrics": {}}
    for field in NUMERIC_FIELDS:
        values = [float(r[field]) for r in records if r.get(field) not in (None, "")]
        if values:
            result["metrics"][field] = {
                "count": len(values),
                "mean": round(statistics.fmean(values), 4),
                "min": round(min(values), 4),
                "max": round(max(values), 4),
                "median": round(statistics.median(values), 4),
            }
    return result

def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize telemetry metrics from CSV.")
    parser.add_argument("csv_file", help="Path to a telemetry CSV file")
    parser.add_argument("--output", "-o", help="Optional JSON output path")
    args = parser.parse_args()
    summary = summarize(load_records(args.csv_file))
    rendered = json.dumps(summary, indent=2)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)

if __name__ == "__main__":
    main()
