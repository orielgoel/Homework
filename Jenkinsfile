pipeline {
    agent any
    environment {
        registry = "oriel360/devops_jenkins_project" // The name of your user and repository (which can be created manually)
        dockerfilePath = 'Project/Dockerfile'
    }
    stages {
        stage('Check and Delete Folder') {
            steps {
                script {
                    def folderPath = "/Users/oriel.goel/.jenkins/workspace/Project - Testing area/Project" // Replace with the actual folder path

                    if (fileExists(folderPath)) {
                        echo "Folder exists. Deleting..."
                        deleteDir() // Delete the entire workspace
                    } else {
                        echo "Folder does not exist."
                    }
                }
            }
        }
        stage('Pull Code From GitHub') {
            steps {
                sh 'git clone https://github.com/orielgoel/Project.git'
            }
        }
        stage('Update Dependencies') {
            steps {
                sh 'pip install --upgrade urllib3 chardet requests'
            }
        }
        stage('Run rest_app') {
            steps {
                sh 'nohup python3 Project/rest_app.py &'
            }
        }
        stage('Run backend_testing') {
            steps {
                sh 'python3 Project/backend_testing.py ${BUILD_NUMBER}'
            }
        }
        stage('Run clean_environment') {
            steps {
                sh 'python3 Project/clean_environment.py'
            }
        }
        stage('Set Image Build Number') {
            steps {
                sh 'echo IMAGE_TAG=${BUILD_NUMBER} > .env'
            }
        }
        stage('Build and Push Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                            docker.build(registry + ":$BUILD_NUMBER", "-f ${dockerfilePath} .").push("${BUILD_NUMBER}")
                        }
                    }
                }
            }
        }
    
        stage('Set compose image version') {
            steps {
                sh 'echo IMAGE_TAG=${BUILD_NUMBER} > .env'
            }
        }
        stage('Run Docker comnpose') {
            steps {
                sh 'docker-compose -f Project/docker-compose.yml up -d'
            }
        }
        stage('Test Docorized app') {
            steps {
                sh 'python3 Project/backend_testing.py ${BUILD_NUMBER}'
            }
        }
        stage('Docker compose down & clean Docker image') {
            steps {
                sh 'docker-compose -f Project/docker-compose.yml down; docker rmi $registry:$BUILD_NUMBER'
            }
        }









    }
}
