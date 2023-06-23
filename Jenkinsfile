pipeline {
    agent any
    environment {
        registry = "oriel360/devops_jenkins_project" // The name of your user and repository (which can be created manually)
        dockerfilePath = 'Dockerfile'
    }
    stages {
        stage('Check and Delete Folder') {
            steps {
                script {
                    def folderPath = "/Users/oriel.goel/.jenkins/workspace/Testing_area/Project" // Replace with the actual folder path

                    if (fileExists(folderPath)) {
                        echo "Folder exists. Deleting..."
                        deleteDir() // Delete the entire workspace
                    } else {
                        echo "Folder does not exist."
                    }
                }
            }
        }
        stage('Pull Code') {
            steps {
                git 'https://github.com/orielgoel/Project.git'
            }
        }
        stage('Update Dependencies') {
            steps {
                sh 'pip install --upgrade urllib3 chardet requests --quiet'
            }
        }
        stage('Run rest_app') {
            steps {
                sh 'nohup python3 rest_app.py &'
            }
        }
        stage('Run backend_testing') {
            steps {
                sh 'python3 backend_testing.py ${BUILD_NUMBER}'
            }
        }
        stage('Run clean_environment') {
            steps {
                sh 'python3 clean_environment.py'
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
                sh 'docker-compose -f docker-compose.yml up -d'
            }
        }
        stage('Test Docorized app') {
            steps {
                sh 'python3 docker_backend_testing.py ${BUILD_NUMBER}'
            }
        }
        stage('Clean compose environment') {
            steps {
                sh 'docker-compose -f docker-compose.yml down; docker rmi $registry:$BUILD_NUMBER'
            }
        }
        stage('Deploy HELM Chart') {
            steps {
                sh 'helm install my-release oci://registry-1.docker.io/oriel360/myapp --set image.version=${registry}:${BUILD_NUMBER}'
            }
        }

        stage('Write service URL into k8s_url.txt') {
            steps {
                sh 'nohup minikube service myapp-service --url > k8s_url.txt &'
            }
        }

        stage('Test Deployed App') {
            steps {
                sh 'python3 K8S_backend_testing.py ${BUILD_NUMBER}'
            }
        }

        stage('Clean HELM Environment') {
            steps {
                sh 'helm delete my-release'
            }
        }








    }
}