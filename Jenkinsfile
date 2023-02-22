pipeline {
    agent any
//     options {
//     buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
//   }
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                }
            }
        }
        stage('Pull code') {
            steps {
                git url: 'https://github.com/nirazz/DevopsExperts.git'
            }
        }
        stage('Run backend') {
            steps {
                script {
                    env.PATH = "${env.PATH}:/home/nir-raz/PycharmProjects/REST_API_PROJECT/venv/bin"
                    if (checkOs() == 'Windows') {
                        bat '/home/nir-raz/PycharmProjects/REST_API_PROJECT/venv/bin/python3 rest_app.py'
                    } else {
                        sh 'nohup /home/nir-raz/PycharmProjects/REST_API_PROJECT/venv/bin/python3 rest_app.py &'
                    }
                }
            }
        }
        stage('Run backend tests') {
            steps {
                sh '/home/nir-raz/PycharmProjects/REST_API_PROJECT/venv/bin/python3 backend_testing.py'
            }
        }
        stage('Clean environment') {
            steps {
                sh '/home/nir-raz/PycharmProjects/REST_API_PROJECT/venv/bin/python3 clean_environment.py'
            }
        }
//         stage('Build Docker image') {
//             steps {
//                 dir('/home/nir-raz/PycharmProjects/docker_test/Docker') {
//                     sh 'docker build -t myflask:${BUILD_NUMBER} .'
//                 }
//             }
//         }
//         stage('Push Docker image') {
//             steps {
//                 withCredentials([usernamePassword(credentialsId: 'dockerhubaccount', usernameVariable: '1nirazz', passwordVariable: 'Kat6886969')]) {
//                     sh "echo $PASSWORD | docker login -u $USERNAME --password-stdin"
//                 }
//                     sh "docker push myflask:${BUILD_NUMBER}"
//           }
//     }

//           stage('Build and push Docker image') {
//             steps {
//                 script {
//                     def registry = "1nirazz/ex_repo"
//                     def registryCredential = 'dockerhubaccount'
//                     def dockerImage = ''
//
//                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
//                    docker.withRegistry('', registryCredential) {
//                    dockerImage.push()
//                         }
//                     }
//                 }
//             }
//             post {
//                 always {
//                         sh '''
//                         if docker images | grep myflask:44 ; then
//                             docker rmi myflask:44
//                         fi
//                         '''
//                 }
//             }
//         }
         stage('Build and push Docker image') {
            steps {
                script {
                    def registry = "1nirazz/ex_repo"
                    def dockerImage = ''

                    withCredentials([usernamePassword(credentialsId: 'dockerhubaccount', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        dockerImage = docker.build(registry + ":$BUILD_NUMBER", "--file=/home/nir-raz/PycharmProjects/docker_test/Docker/Dockerfile", "/home/nir-raz/PycharmProjects/docker_test/Docker")
                        docker.withRegistry("https://registry.hub.docker.com", 'dockerhubaccount') {
                            dockerImage.push()
                        }
                    }
                }
            }
        }
        stage('Set compose image version') {
            steps {
                sh "echo IMAGE_TAG=${BUILD_NUMBER} > .env"
            }
        }
        stage('Run docker-compose up') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('Test dockerized app') {
            steps {
                sh 'python3 docker_backend_testing.py'
            }
        }
//         stage('Run frontend') {
//             steps {
//                 script {
//                     env.PATH = "${env.PATH}:/home/nir-raz/PycharmProjects/REST_API_PROJECT/venv/bin"
//                     if (checkOs() == 'Windows') {
//                         bat '/home/nir-raz/PycharmProjects/REST_API_PROJECT/venv/bin/python3 web_app.py'
//                     } else {
//                         sh 'nohup /home/nir-raz/PycharmProjects/REST_API_PROJECT/venv/bin/python3 web_app.py &'
//                     }
//                 }
//             }
//         }
//         stage('Run frontend tests') {
//             steps {
//                 sh '/home/nir-raz/PycharmProjects/REST_API_PROJECT/venv/bin/python3 frontend_testing.py'
//             }
//         }
//         stage('Run combined tests') {
//             steps {
//                 sh '/home/nir-raz/PycharmProjects/REST_API_PROJECT/venv/bin/python3 combined_testing.py'
//             }
//         }
           stage('Clean up Docker resources') {
               steps {
                   sh 'docker-compose down'
                   sh 'docker rmi myflask:${BUILD_NUMBER}'
               }
           }
    }
}

def checkOs(){
    if (isUnix()) {
        def uname = sh script: 'uname', returnStdout: true
        if (uname.startsWith("Darwin")) {
            return "Macos"
        }
        else {
            return "Linux"
        }
    }
    else {
        return "Windows"
    }
}
