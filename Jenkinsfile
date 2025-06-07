pipeline{
    agent { label 'azureagent' }
    environment {
        DOCKER_REGISTRY = 'khangeshmatte123'
        BUILD_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage ('Checkout') {
            steps {
                checkout scm
                echo 'checked out code'
            }
        stage ('Build'){
            steps {
                echo 'Building api application'
                sh '''
                cd /api
                docker build -t ${DOCKER_REGISTRY}/flask_app:${BUILD_TAG} .
                '''
                 }
            }
        }
    }
}
