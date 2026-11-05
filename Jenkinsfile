pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Install') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    . .venv/bin/activate
                    python -m pytest
                '''
            }
        }
        stage('Archive') {
            steps {
                sh "tar -czf my-python-app-${env.BUILD_NUMBER}.tar.gz app requirements.txt"
                archiveArtifacts artifacts: "my-python-app-${env.BUILD_NUMBER}.tar.gz", fingerprint: true
            }
        }
    }
}