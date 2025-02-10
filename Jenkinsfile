pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup') {
            steps {
                sh 'py -m venv venv'
                sh 'venv\Scripts\activate && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                // Run tests on a specific function, for example:
                sh 'venv\Scripts\activate && pytest -k test_function_to_test --junitxml=results.xml'
            }
        }
    }
    post {
        always {
            junit 'results.xml'
        }
    }
}
