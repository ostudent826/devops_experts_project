pipeline {
    agent any

    environment {
        DOCKER_IMAGE_VERSION = "v1"
        DOCKER_IMAGE_BACKEND = "devop_prj_backend_app"  
        DOCKER_IMAGE_FRONTEND = "devop_prj_frontend_app"  
        DOCKER_IMAGE_MYSQL = "devop_prj_mysql_db"  
        DOCKER_REPO = "ostudent826/devops_experts_project"
        DOCKER_TOKEN = "dckr_pat_td8LmOyzWeqAfUcyW-3w37sJaTo"
    }

    stages {
        stage('Pull Code') {
            steps {
                echo 'Pulling code from GitHub...'
                git url: 'https://github.com/ostudent826/devops_experts_project.git', branch: 'third-part'
            }
        }

        stage('Run Backend Server') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    dir('Code Non container') {
                        bat 'start /min /b python rest_app.py'
                    }
                }
            }
        }

        stage('Run Frontend Server') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    dir('Code Non container') {
                        bat 'start /min /b python web_app.py'
                    }
                }
            }
        }

        stage('Backend Testing') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    dir('Code Non container') {
                        bat 'python backend_testing.py'
                    }
                }
            }
        }

        stage('Frontend Testing') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    dir('Code Non container') {
                        bat 'python frontend_testing.py'
                    }
                }
            }
        }

        stage('Combined Testing') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    dir('Code Non container') {
                        bat 'python combined_testing.py'
                    }
                }
            }
        }

        stage('Clean Environment') {
            steps {
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                    dir('Code Non container') {
                        bat 'python clean_environment.py'
                    }
                }
            }
        }
        stage("wait_prior_starting_smoke_testing") {
            def time = params.SLEEP_TIME_IN_SECONDS
                echo "Waiting ${SLEEP_TIME_IN_SECONDS} seconds for deployment to complete prior starting smoke testing"
        sleep time.toInteger(45) // seconds
        }
        //  stage('Docker Login') {
        //     steps {
        //         echo 'Authenticating with Docker Hub...'
        //         bat 'docker login --username ostudent826 --password %DOCKER_TOKEN%'
        //     }
        // }
        // stage('Build Docker Images') {
        //     steps {
        //         catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
        //             dir('third-part/containers images/backend') {
        //                 echo 'Building Backend Docker image...'
        //                 bat 'docker build -t %DOCKER_IMAGE_BACKEND%:%DOCKER_IMAGE_VERSION% .'
        //             }
        //             dir('third-part/containers images/frontend') {
        //                 echo 'Building Frontend Docker image...'
        //                 bat 'docker build -t %DOCKER_IMAGE_FRONTEND%:%DOCKER_IMAGE_VERSION% .'
        //             }
        //             dir('third-part/containers images/mysql') {
        //                 echo 'Building MySQL Docker image...'
        //                 bat 'docker build -t %DOCKER_IMAGE_MYSQL%:%DOCKER_IMAGE_VERSION% .'
        //             }
        //         }
        //     }
        // }

        // stage('Push Docker Images') {
        //     steps {
        //         catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
        //             echo 'Logging in to Docker Hub using token...'
        //             withCredentials([string(credentialsId: 'dckr_pat_td8LmOyzWeqAfUcyW-3w37sJaTo', variable: 'DOCKER_TOKEN')]) {
        //                 bat """
        //                 echo %DOCKER_TOKEN% | docker login -u ostudent826 --password-stdin
        //                 docker tag %DOCKER_IMAGE_BACKEND%:%DOCKER_IMAGE_VERSION% %DOCKER_REPO%/backend:%DOCKER_IMAGE_VERSION%
        //                 docker push %DOCKER_REPO%/backend:%DOCKER_IMAGE_VERSION%
        
        //                 docker tag %DOCKER_IMAGE_FRONTEND%:%DOCKER_IMAGE_VERSION% %DOCKER_REPO%/frontend:%DOCKER_IMAGE_VERSION%
        //                 docker push %DOCKER_REPO%/frontend:%DOCKER_IMAGE_VERSION%
        
        //                 docker tag %DOCKER_IMAGE_MYSQL%:%DOCKER_IMAGE_VERSION% %DOCKER_REPO%/mysql:%DOCKER_IMAGE_VERSION%
        //                 docker push %DOCKER_REPO%/mysql:%DOCKER_IMAGE_VERSION%
        //                 """
        //             }
        //         }
        //     }
        // }


        // stage('Set Compose Image Version') {
        //     steps {
        //         catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
        //             echo 'Setting image version in .env file...'
        //             bat 'echo IMAGE_TAG=%DOCKER_IMAGE_VERSION% > .env'
        //         }
        //     }
        // }

        // stage('Run Docker Compose') {
        //     steps {
        //         catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
        //             echo 'Starting services with docker-compose...'
        //             bat 'docker-compose up -d'
        //         }
        //     }
        // }

        

        // stage('Test Dockerized App') {
        //     steps {
        //         catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
        //          dir('third-part/Code Non Containers/backend') {
        //             echo 'Testing dockerized app with backend and frontend tests...'
        //             bat 'python backend_testing.py'
        //             bat 'python frontend_testing.py'
        //             bat 'python combined_testing.py'
        //          }
        //         }
        //     }
        // }

        // stage('Clean Environment_containers') {
        //     steps {
        //         catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
        //             echo 'Cleaning up environment...'
        //             bat """
        //             docker-compose down
        //             docker rmi %DOCKER_IMAGE_BACKEND%:%DOCKER_IMAGE_VERSION%
        //             docker rmi %DOCKER_IMAGE_FRONTEND%:%DOCKER_IMAGE_VERSION%
        //             docker rmi %DOCKER_IMAGE_MYSQL%:%DOCKER_IMAGE_VERSION%
        //             """
        //         }
        //     }
        // }
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
