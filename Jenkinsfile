pipeline {
    agent any

    environment {
        DOCKER_IMAGE_VERSION = "${BUILD_NUMBER}"
        DOCKER_IMAGE_BACKEND = "devop_prj_backend_app"  
        DOCKER_IMAGE_FRONTEND = "devop_prj_frontend_app"  
        DOCKER_IMAGE_MYSQL = "devop_prj_mysql_db"  
        DOCKER_REPO = "ostudent826/devops_experts_project"
        DOCKER_TOKEN = "dckr_pat_td8LmOyzWeqAfUcyW-3w37sJaTo"
        DOCKER_USER = "ostudent826"

        // Helm releases and chart paths
        RELEASE_BACKEND = "backend"
        RELEASE_FRONTEND = "frontend"
        RELEASE_DATABASE = "database"
        CHART_BACKEND = "./k8s_app/backend-chart"
        CHART_FRONTEND = "./k8s_app/frontend-chart"
        CHART_DATABASE = "./k8s_app/database-chart"
    }

    stages {
        stage('Pull Code') {
            steps {
                echo 'Pulling code from GitHub...'
                git url: 'https://github.com/ostudent826/devops_experts_project.git', branch: 'fourth-part'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install all libraries from requirements.txt
                    bat 'pip install -r prj-requirements.txt'
                }
            }
        }
        stage('Run Backend Server') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                        bat 'start /min /b python App/rest_app.py'

                }
            }
        }

        stage('Run Frontend Server') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                        bat 'start /min /b python App/web_app.py'

                }
            }
        }

        stage('Backend Testing') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                       bat 'python "Testing Scripts/backend_testing.py"'

                }
            }
        }

        stage('Frontend Testing') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                        bat 'python "Testing Scripts/frontend_testing.py"'

                }
            }
        }

        stage('Combined Testing') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                        bat 'python "Testing Scripts/combined_testing.py"'

                }
            }
        }

        stage('Clean Environment') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                        bat 'python "Testing Scripts/clean_environment.py"'

                }
            }
        }
        stage('Docker Login') {
            steps {
                script {
                    // Write the Docker token to a file securely
                    writeFile file: 'docker_token.txt', text: "${DOCKER_TOKEN}"
                    
                    // Use --password-stdin to read from the file
                    bat """
                    docker login --username ${DOCKER_USER} --password-stdin < docker_token.txt
                    """
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    dir('containers_images/backend_app') {
                        echo 'Building Backend Docker image...'
                        bat 'docker build -t %DOCKER_IMAGE_BACKEND%:%DOCKER_IMAGE_VERSION% .'
                    }
                    dir('containers_images/frontend_app') {
                        echo 'Building Frontend Docker image...'
                        bat 'docker build -t %DOCKER_IMAGE_FRONTEND%:%DOCKER_IMAGE_VERSION% .'
                    }
                    dir('containers_images/mysql_DB') {
                        echo 'Building MySQL Docker image...'
                        bat 'docker build -t %DOCKER_IMAGE_MYSQL%:%DOCKER_IMAGE_VERSION% .'
                    }
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {                      
                    echo 'Pushing Docker images...'
                    bat """
                    docker tag %DOCKER_IMAGE_BACKEND%:%DOCKER_IMAGE_VERSION% %DOCKER_REPO%:backend-%DOCKER_IMAGE_VERSION%
                    docker push %DOCKER_REPO%:backend-%DOCKER_IMAGE_VERSION%
                    
                    docker tag %DOCKER_IMAGE_FRONTEND%:%DOCKER_IMAGE_VERSION% %DOCKER_REPO%:frontend-%DOCKER_IMAGE_VERSION%
                    docker push %DOCKER_REPO%:frontend-%DOCKER_IMAGE_VERSION%
                    
                    docker tag %DOCKER_IMAGE_MYSQL%:%DOCKER_IMAGE_VERSION% %DOCKER_REPO%:mysql-%DOCKER_IMAGE_VERSION%
                    docker push %DOCKER_REPO%:mysql-%DOCKER_IMAGE_VERSION%
                    """

                }
            }
        }


        stage('Set Compose Image Version') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    echo 'Setting image version in .env file...'
                    bat 'echo IMAGE_TAG=%DOCKER_IMAGE_VERSION% > .env'
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

                    bat 'python "Testing Scripts/backend_testing.py"'
                    bat 'python "Testing Scripts/frontend_testing.py"'
                    bat 'python "Testing Scripts/combined_testing-container.py"'

                }
            }
        }

        stage('Clean Environment_containers') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    echo 'Cleaning up environment...'
                    bat """
                    docker-compose down
                    docker rmi %DOCKER_IMAGE_BACKEND%:%DOCKER_IMAGE_VERSION%
                    docker rmi %DOCKER_IMAGE_FRONTEND%:%DOCKER_IMAGE_VERSION%
                    docker rmi %DOCKER_IMAGE_MYSQL%:%DOCKER_IMAGE_VERSION%
                    docker image prune -f
                    docker volume rm devops_project_pipeline_third_part_mysql_data || echo "Volume not found"
                    docker volume prune -f
                    """
                }
            }
        }
    }

         stage('Deploy Helm Charts') {
            parallel {
                DeployBackend: {
                    steps {
                        script {
                            sh """
                            helm install ${RELEASE_BACKEND} ${CHART_BACKEND} \\
                                --set image.repository=${DOCKER_REPO} \\
                                --set image.tag=backend-${DOCKER_IMAGE_VERSION}
                            """
                        }
                    }
                }
                DeployFrontend: {
                    steps {
                        script {
                            sh """
                            helm install ${RELEASE_FRONTEND} ${CHART_FRONTEND} \\
                                --set image.repository=${DOCKER_REPO} \\
                                --set image.tag=frontend-${DOCKER_IMAGE_VERSION}
                            """
                        }
                    }
                }
                DeployDatabase: {
                    steps {
                        script {
                            sh """
                            helm install ${RELEASE_DATABASE} ${CHART_DATABASE} \\
                                --set image.repository=${DOCKER_REPO} \\
                                --set image.tag=database-${DOCKER_IMAGE_VERSION}
                            """
                        }
                    }
                }
            }
        }

    post {
        failure {
            emailext(
                subject: 'Build Failed: ${JOB_NAME} #${BUILD_NUMBER}',
                body: '${JELLY_SCRIPT,template="html"}',
                to: 'ofrigsp@gmail.com',
                replyTo: '$DEFAULT_REPLYTO',
                mimeType: 'text/html'
            )
        }
    }
}
