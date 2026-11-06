# Assignment 5 — Practical Implementation

## Project
Scientific Telemetry CSV Analyzer: a Python command-line utility that reads telemetry CSV data and calculates descriptive statistics for latency, throughput, CPU and memory metrics.

## CI workflow
The Jenkins pipeline in `Jenkinsfile` performs these stages:
1. Checkout — obtains source code from the configured Git repository.
2. Verify Python — prints the Python version and checks Python syntax.
3. Unit tests — runs the standard-library unittest suite on every Jenkins build.
4. Analyze sample data — runs the analyzer against the supplied sample CSV and archives the JSON result.
5. Build Docker image — builds a versioned Docker image and tags it as latest.

The Docker image runs the existing analyzer. The Dockerfile runs the unit tests during image build as an additional safeguard.

## Local Docker commands
```bash
docker build -t scientific-telemetry-analyzer:local .
docker run --rm scientific-telemetry-analyzer:local sample_telemetry.csv
docker compose run --rm telemetry-analyzer
```

## Jenkins prerequisites
- Jenkins controller/agent with Git, Python 3 and Docker CLI installed.
- Docker daemon accessible to the Jenkins agent.
- A Pipeline job configured to use this repository and the `Jenkinsfile`.
- For a public repository no GitHub credentials are required for checkout.

## Pipeline setup
Create a Pipeline job and choose “Pipeline script from SCM”, Git, repository URL `https://github.com/Angarov2004/ass3_ASDP.git`, branch `*/assignment-5-devops`, script path `Jenkinsfile`. Start “Build Now”. A webhook or periodic SCM polling can be configured later for automatic triggering after commits.

## Scope and limitations
This implementation provides continuous integration and a containerized, repeatable execution environment. It builds an image but does not publish it to Docker Hub and does not deploy to a remote server or Kubernetes. Those steps require registry credentials and a deployment target and are not claimed as completed.
