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
                bat """
                    py -m venv venv
                    call venv\\Scripts\\activate
                    pip install -r requirements.txt
                """
            }
        }
        stage('Test') {
            steps {
                bat """
                    call venv\\Scripts\\activate
                    pytest -k test_function_to_test --junitxml=results.xml
                """
            }
        }
    }
    post {
        always {
            junit 'results.xml'
        }
    }
}
