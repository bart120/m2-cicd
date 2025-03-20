pipeline {
    agent none

    stages {
        stage('Checkout code') {
            agent any
            steps {
                git branch: 'source', url:'https://github.com/bart120/m2-cicd.git' //plugin git
                sh 'ls -R ${WORKSPACE}'
            }
        }
        stage('Build Backend') {
            agent {
                label 'docker-agent-python'
            }
            steps {
                sh 'ls -R ${WORKSPACE}' 
                sh 'pip install -r back/requirements.txt'
            }
        }
        stage('Test') {
            agent any
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            agent any
            steps {
                echo 'Deploying....'
            }
        }
    }
}