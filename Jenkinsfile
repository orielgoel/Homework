pipeline {
    agent any
    stages {
        stage('Run rest_app') {
            steps {
                sh 'nohup python3 /Users/oriel.goel/PycharmProjects/Project/rest_app.py &'
            }
        }
        stage('Run web_app') {
            steps {
                sh 'nohup python3 /Users/oriel.goel/PycharmProjects/Project/web_app.py &'
            }
        }       
        stage('Run backend_testin') {
            steps {
                sh 'python3 /Users/oriel.goel/PycharmProjects/Project/backend_testing.py'
            }
        }
        stage('Run frontend_testin') {
            steps {
                sh 'python3 /Users/oriel.goel/PycharmProjects/Project/frontend_testing.py'
            }
        }

        stage('Run combined_testing') {
            steps {
                sh 'python3 /Users/oriel.goel/PycharmProjects/Project/combined_testing.py'
            }        
        }
        stage('Run clean_environment') {
            steps {
                sh 'python3 /Users/oriel.goel/PycharmProjects/Project/clean_environment.py'
            }        
        }
    }
}