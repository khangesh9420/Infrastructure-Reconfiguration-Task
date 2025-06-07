pipeline {
    agent { label 'azureagent' }
    environment {
        DOCKER_REGISTRY = 'khangeshmatte123'
        BUILD_TAG = "${BUILD_NUMBER}"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'checked out code'
            }
        }
        stage('Build') {
            steps {
                echo 'Building api application'
                sh '''
                    ls -la
                    pwd
                    cd api
                    docker build -t ${DOCKER_REGISTRY}/flask_app:${BUILD_TAG} .
                '''
            }
        }
        stage('Test') {	
            environment {
                SONAR_HOST_URL = 'http://108.142.232.37:9000'
            }
            steps {
                withCredentials([string(credentialsId: 'sonarqube-token', variable: 'SONAR_TOKEN')]) {
                    sh """
                        echo 'Running static code analysis using SonarQube'
                        docker run --rm -v ${env.WORKSPACE}:/usr/src/app -w /usr/src/app sonarsource/sonar-scanner-cli \
                        -Dsonar.projectKey=flask_app \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=${SONAR_HOST_URL} \
                        -Dsonar.login=${SONAR_TOKEN}
                    """
                }
            }
        }
        stage('Push') {
            steps {
                echo 'Pushing image to Docker registry'
                withCredentials([usernamePassword(credentialsId: 'docker-creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh '''
                        echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                        docker push ${DOCKER_REGISTRY}/flask_app:${BUILD_TAG}
                    '''
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application'
                sh '''
                    docker pull ${DOCKER_REGISTRY}/flask_app:${BUILD_TAG}
                    docker rm -f flask_app || true
                    docker run -d --name flask_app -p 5000:5000 ${DOCKER_REGISTRY}/flask_app:${BUILD_TAG}
                '''
            }
        }
    }
}
