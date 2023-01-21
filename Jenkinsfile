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
        stage('Pull code') {
            steps {
                git url: 'https://github.com/nirazz/DevopsExperts.git'
            }
        }
        stage('Run backend') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python rest_app.py'
                    } else {
                        sh 'nohup python rest_app.py &'
                    }
                }
            }
        }
        stage('Run frontend') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python web_app.py'
                    } else {
                        sh 'nohup python web_app.py &'
                    }
                }
            }
        }
        stage('Run backend tests') {
            steps {
                sh 'python backend_testing.py'
            }
        }
        stage('Run frontend tests') {
            steps {
                sh 'python frontend_testing.py'
            }
        }
        stage('Run combined tests') {
            steps {
                sh 'python combined_testing.py'
            }
        }
        stage('Clean environment') {
            steps {
                sh 'python clean_environment.py'
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