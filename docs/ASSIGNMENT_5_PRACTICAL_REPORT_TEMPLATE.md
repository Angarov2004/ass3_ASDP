# Assignment 5 — Practical Report (Complete after running Jenkins)

## 1. Objective
The objective was to automate testing and containerization of the Scientific Telemetry CSV Analyzer using Docker and Jenkins.

## 2. Implementation
The repository includes a Dockerfile, .dockerignore, docker-compose.yml and Jenkinsfile. The pipeline checks out the source, verifies Python syntax, runs unit tests, analyzes the sample CSV and builds a Docker image.

## 3. Execution evidence
Insert screenshots of:
- Jenkins job configuration showing the SCM repository and Jenkinsfile path.
- Successful Jenkins pipeline stage view.
- Console output showing all unit tests passed.
- Docker image visible in `docker images`.
- Container execution and generated JSON output.

## 4. Difficulties
Record the actual setup issues encountered, such as Docker daemon access for the Jenkins agent, required tools on the agent, or SCM configuration. Do not claim an issue occurred unless it was observed.

## 5. Conclusion
The pipeline automates testing and image construction. The Docker image packages the analyzer for repeatable execution. The pipeline is a CI implementation; registry publishing and remote deployment remain optional extensions and are not claimed unless configured and tested.
