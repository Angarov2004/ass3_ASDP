pipeline {
    agent any
    options {
        timestamps()
        disableConcurrentBuilds()
    }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Verify Python') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m py_compile telemetry_tool.py test_telemetry_tool.py'
            }
        }
        stage('Unit tests') {
            steps { sh 'python3 -m unittest -v' }
        }
        stage('Analyze sample data') {
            steps {
                sh 'mkdir -p build'
                sh 'python3 telemetry_tool.py sample_telemetry.csv --output build/summary.json'
                archiveArtifacts artifacts: 'build/summary.json', fingerprint: true
            }
        }
        stage('Build Docker image') {
            steps {
                sh 'docker build -t scientific-telemetry-analyzer:$BUILD_NUMBER .'
                sh 'docker tag scientific-telemetry-analyzer:$BUILD_NUMBER scientific-telemetry-analyzer:latest'
            }
        }
    }
    post {
        success { echo 'CI pipeline completed: tests passed and Docker image was built.' }
        failure { echo 'CI pipeline failed. Review the stage logs above.' }
        always { echo 'Build result: ' + currentBuild.currentResult }
    }
}
