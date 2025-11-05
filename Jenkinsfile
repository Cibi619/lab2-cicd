pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Env') {
            steps {
                bat """
                python -m venv venv
                venv\\Scripts\\pip install --upgrade pip
                venv\\Scripts\\pip install -r requirements.txt
                """
            }
        }

        stage('Run Application') {
            steps {
                bat """
                venv\\Scripts\\python factorial.py
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                venv\\Scripts\\pytest -q
                """
            }
        }
    }

    post {
    success {
        emailext(
            subject: "SUCCESS: Build #${env.BUILD_NUMBER}",
            body: "The build was successful!",
            to: "cibi.mit@gmail.com"
        )
    }
    failure {
        emailext(
            subject: "FAILED: Build #${env.BUILD_NUMBER}",
            body: "The build has failed. Please check Jenkins.",
            to: "cibi.mit@gmail.com"
        )
    }
}
}
