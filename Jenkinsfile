pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                }
            }
        }
//         stage('Pull code') {
//             steps {
//                 git url: 'https://github.com/nirazz/DevopsExperts.git'
//             }
//         }
        stage('Run backend') {
            steps {
                script {
                    env.PATH = "${env.PATH}:/home/nir-raz/PycharmProjects/REST_API_PROJECT/venv/bin"
                    if (checkOs() == 'Windows') {
                        bat 'python3 rest_app.py'
                    } else {
                        sh 'nohup python3 rest_app.py &'
                    }
                }
            }
        }
        stage('Run frontend') {
            steps {
                script {
                    env.PATH = "${env.PATH}:/home/nir-raz/PycharmProjects/REST_API_PROJECT/venv/bin"
                    if (checkOs() == 'Windows') {
                        bat 'python3 web_app.py'
                    } else {
                        sh 'nohup python3 web_app.py &'
                    }
                }
            }
        }
        stage('Run backend tests') {
            steps {
                sh 'python3 backend_testing.py'
            }
        }
        stage('Run frontend tests') {
            steps {
                sh 'python3 frontend_testing.py'
            }
        }
        stage('Run combined tests') {
            steps {
                sh 'python3 combined_testing.py'
            }
        }
        stage('Clean environment') {
            steps {
                sh 'python3 clean_environment.py'
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