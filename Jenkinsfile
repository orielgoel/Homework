pipeline {
    agent any
    stages {
        stage('Pull Code From GitHub') {
            steps {
                sh 'git clone https://github.com/orielgoel/Project.git  '
            }
        }
        stage('Run rest_app') {
            steps {
                sh 'nohup python3 /Project/rest_app.py &'
            }
        }
        stage('Run web_app') {
            steps {
                sh 'nohup python3 /Project/web_app.py &'
            }
        }       
        stage('Run backend_testin') {
            steps {
                sh 'python3 /Project/backend_testing.py'
            }
        }
        stage('Run frontend_testin') {
            steps {
                sh 'python3 /Project/frontend_testing.py'
            }
        }

        stage('Run combined_testing') {
            steps {
                sh 'python3 /Project/combined_testing.py'
            }        
        }
        stage('Run clean_environment') {
            steps {
                sh 'python3 /Project/clean_environment.py'
            }        
        }
    }
}