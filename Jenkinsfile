pipeline {
    agent none

    stages {
        stage('Checkout code') {
            agent any
            steps {
                git branch: 'source', url:'https://github.com/bart120/m2-cicd.git' //plugin git
                sh 'ls -R ${WORKSPACE}'
                stash name: 'source-code', includes :'**'
            }
        }
        stage('Build Backend') {
            agent {
                label 'docker-agent-python'
            }
            steps {
                unstash 'source-code'
                sh 'ls -R ${WORKSPACE}' 
                sh 'pip install -r back/requirements.txt'
            }
        }
        stage('Test') {
             agent {
                label 'docker-agent-python-test'
            }
            steps {
                unstash 'source-code'
                sh 'cd backend && pytest || echo "No tests found"'
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