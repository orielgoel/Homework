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
        stage('Build and push image') {
            environment {
                registry = "oriel360/devops_jenkins_project" // The name of your user and repository (which can be created manually)
            }
            steps {
                script {
                    dockerImage = docker.build(registry + ":$BUILD_NUMBER") // give a name and version to the image
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push() // push the image to the registry
                    }
                }
            }
            post {
                always {
                    sh "docker rmi $registry:$BUILD_NUMBER" // delete the local image at the end
                }
            }
        }
        stage('Delete GitHub Folder') {
            steps {
                sh 'rm -rf Project'
            }
        }
    }
}
