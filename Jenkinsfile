pipeline {
    agent any
    stages {
        stage('Pull Code From GitHub') {
            steps {
                sh 'git clone https://github.com/orielgoel/Project.git'
            }
        }
        stage('Run rest_app') {
            steps {
                sh 'nohup python3 Project/rest_app.py &'
            }
        }
      
        stage('Run backend_testing') {
            steps {
                sh 'python3 Project/backend_testing.py'
            }
        }

        stage('Run clean_environment') {
            steps {
                sh 'python3 Project/clean_environment.py'
            }        
        }
        stage('Delete Github Folder') {
            steps {
                sh 'rm -rf Project'
            }        
        }



    }
}