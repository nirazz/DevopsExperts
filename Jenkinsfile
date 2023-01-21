def python_path = '/home/nir-raz/PycharmProjects/REST_API_PROJECT/venv/bin/python3'
env.PATH = "${env.PATH}:${python_path}"

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
                    if (checkOs() == 'Windows') {
                        bat "${python_path} rest_app.py"
                    } else {
                        sh "nohup ${python_path} rest_app.py &"
                    }
                }
            }
        }
        stage('Run frontend') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat "${python_path} web_app.py"
                    } else {
                        sh "nohup ${python_path} web_app.py &"
                    }
                }
            }
        }
        stage('Run backend tests') {
            steps {
                sh "${python_path} backend_testing.py"
            }
        }
        stage('Run frontend tests') {
            steps {
                sh "${python_path} frontend_testing.py"
            }
        }
        stage('Run combined tests') {
            steps {
                sh "${python_path} combined_testing.py"
            }
        }
        stage('Clean environment') {
            steps {
                sh "${python_path} clean_environment.py"
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