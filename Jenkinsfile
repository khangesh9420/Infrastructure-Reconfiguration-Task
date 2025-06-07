pipeline{
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
        stage('Build'){
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
            steps {
                echo 'Rinnung test and static code analysis using sonarqube'
                sh '''
                    docker run --rm -v $(pwd):/usr/src/app -w /usr/src/app sonarsource/sonar-scanner-cli \
                    -Dsonar.projectKey=flask_app \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://your-sonarqube-server:9000 \
                    -Dsonar.login=sonarqube-token
                '''
                }
            }
        }
    }
    
