pipeline {
    agent any

    environment {
        DOCKER_IMAGE_BACKEND = "backend-image-name"  // Replace with your backend Docker image name
        DOCKER_IMAGE_FRONTEND = "frontend-image-name"  // Replace with your frontend Docker image name
        DOCKER_IMAGE_MYSQL = "mysql-image-name"  // Replace with your MySQL Docker image name
        DOCKER_REPO = "your-docker-hub-repo"   // Replace with your Docker Hub repo
    }

    stages {
        stage('Pull Code') {
            steps {
                echo 'Pulling code from GitHub...'
                git url: 'https://github.com/ostudent826/devops_experts_project.git', branch: 'third-part/Code Non container'
            }
        }

        stage('Run Backend Server') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    bat 'start /min /b python rest_app.py'
                }
            }
        }

        stage('Run Frontend Server') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    bat 'start /min /b python web_app.py'
                }
            }
        }

        stage('Backend Testing') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    bat 'python backend_testing.py'
                }
            }
        }

        stage('Frontend Testing') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    bat 'python frontend_testing.py'
                }
            }
        }

        stage('Combined Testing') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    bat 'python combined_testing.py'
                }
            }
        }

        stage('Clean Environment') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    bat 'python clean_environment.py'
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    dir('third-part/containers images/backend') {
                        echo 'Building Backend Docker image...'
                        bat 'docker build -t %DOCKER_IMAGE_BACKEND%:%BUILD_NUMBER% .'
                    }
                    dir('third-part/containers images/frontend') {
                        echo 'Building Frontend Docker image...'
                        bat 'docker build -t %DOCKER_IMAGE_FRONTEND%:%BUILD_NUMBER% .'
                    }
                    dir('third-part/containers images/mysql') {
                        echo 'Building MySQL Docker image...'
                        bat 'docker build -t %DOCKER_IMAGE_MYSQL%:%BUILD_NUMBER% .'
                    }
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    echo 'Pushing Docker images to Docker Hub...'
                    bat """
                    docker tag %DOCKER_IMAGE_BACKEND%:%BUILD_NUMBER% %DOCKER_REPO%/backend:%BUILD_NUMBER%
                    docker push %DOCKER_REPO%/backend:%BUILD_NUMBER%

                    docker tag %DOCKER_IMAGE_FRONTEND%:%BUILD_NUMBER% %DOCKER_REPO%/frontend:%BUILD_NUMBER%
                    docker push %DOCKER_REPO%/frontend:%BUILD_NUMBER%

                    docker tag %DOCKER_IMAGE_MYSQL%:%BUILD_NUMBER% %DOCKER_REPO%/mysql:%BUILD_NUMBER%
                    docker push %DOCKER_REPO%/mysql:%BUILD_NUMBER%
                    """
                }
            }
        }

        stage('Set Compose Image Version') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    echo 'Setting image version in .env file...'
                    bat 'echo IMAGE_TAG=%BUILD_NUMBER% > .env'
                }
            }
        }

        stage('Run Docker Compose') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    echo 'Starting services with docker-compose...'
                    bat 'docker-compose up -d'
                }
            }
        }

        stage('Test Dockerized App') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    echo 'Testing dockerized app with backend and frontend tests...'
                    bat 'python backend_testing.py'
                    bat 'python frontend_testing.py'
                    bat 'python combined_testing.py'
                }
            }
        }

        stage('Clean Environment') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    echo 'Cleaning up environment...'
                    bat """
                    docker-compose down
                    docker rmi %DOCKER_IMAGE_BACKEND%:%BUILD_NUMBER%
                    docker rmi %DOCKER_IMAGE_FRONTEND%:%BUILD_NUMBER%
                    docker rmi %DOCKER_IMAGE_MYSQL%:%BUILD_NUMBER%
                    docker rmi %DOCKER_REPO%/backend:%BUILD_NUMBER%
                    docker rmi %DOCKER_REPO%/frontend:%BUILD_NUMBER%
                    docker rmi %DOCKER_REPO%/mysql:%BUILD_NUMBER%
                    """
                }
            }
        }
    }

    post {
        failure {
            emailext(
                subject: 'Build Failed: ${JOB_NAME} #${BUILD_NUMBER}',
                body: '${JELLY_SCRIPT,template="html"}',
                to: 'eliran9657@gmail.com',
                replyTo: '$DEFAULT_REPLYTO',
                mimeType: 'text/html'
            )
        }
    }
}
