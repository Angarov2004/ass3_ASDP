# Scientific Telemetry CSV Analyzer

A small reproducible scientific-software utility that summarizes network-service telemetry stored in CSV files. It is suitable for basic experiments on latency, throughput, CPU and memory usage.

## Requirements
- Python 3.10+
- Git
- GitHub account for hosting and Actions CI

No third-party runtime dependencies are required.

## Run locally
```bash
python telemetry_tool.py sample_telemetry.csv
python telemetry_tool.py sample_telemetry.csv --output summary.json
python -m unittest -v
```

Input CSV can contain any columns, but these metric columns are recognized when present: `latency_ms`, `throughput_eps`, `cpu_percent`, `memory_mb`. The file must have a header row. Empty metric cells are ignored; malformed numeric values produce a row-specific error.

## Project layout
- `telemetry_tool.py` — CSV parsing and descriptive statistics
- `test_telemetry_tool.py` — automated unit tests
- `sample_telemetry.csv` — small example dataset
- `.github/workflows/ci.yml` — automated test workflow
- `LICENSE` — MIT License
- `.github/ISSUE_TEMPLATE/bug_report.md` — issue template

## Scientific reproducibility
Keep the raw dataset unchanged, record how it was collected, document units and sampling intervals, and save generated JSON summaries with the experiment notes. The included data are synthetic examples and must not be presented as production measurements.

## Git and GitHub setup
```bash
git init
git add .
git commit -m "Initial telemetry analyzer"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/scientific-telemetry-tool.git
git push -u origin main
```
Create a **public** repository on GitHub first, with the same name. Replace `YOUR_USERNAME` with your GitHub username. Then add repository topics such as `scientific-computing`, `telemetry`, and `python`.

## CI/CD
GitHub Actions runs the unit tests on pushes and pull requests. This project uses continuous integration (automated validation); it does not automatically publish a release, so deployment/release CD is not claimed.
